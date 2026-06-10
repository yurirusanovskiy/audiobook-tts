import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Dict, Optional
from pydantic import BaseModel
from db.database import get_session
from db.models import Character, Project, ProjectCharacterLink
from core.preprocessor import PreprocessorFactory
from core.gemini_client import GeminiAudioClient
from db.crud import get_dictionary_for_language

router = APIRouter(prefix="/processing", tags=["Processing"])

class SceneLine(BaseModel):
    character_id: Optional[str] = None
    text: str
    language_override: Optional[str] = None
    prompt_override: Optional[str] = None

class ProcessSceneRequest(BaseModel):
    scene_id: str

class PreprocessRequest(BaseModel):
    project_id: str
    lines: List[SceneLine]

class ProcessSceneResponse(BaseModel):
    scene_id: str
    audio_file_url: str

class ProcessedLine(BaseModel):
    character_id: Optional[str] = None
    original_text: str
    processed_text: str

class PreprocessOnlyResponse(BaseModel):
    scene_id: str
    processed_lines: List[ProcessedLine]

def _process_lines(project_id: str, lines, session: Session):
    from db.models import CharacterLanguageProfile
    from typing import Optional
    
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    processed_lines = []
    script = []
    
    # Cache preprocessors and dictionaries for this request
    preprocessors = {}
    dictionaries = {}
    
    for line in lines:
        if line.character_id is None:
            # Handle narrator/unassigned lines
            char = None
            lang = line.language_override if line.language_override else project.language_code
            final_line_prompt = line.prompt_override or ""
        else:
            char = session.get(Character, line.character_id)
            if not char:
                raise HTTPException(status_code=404, detail=f"Character '{line.character_id}' not found in DB")
                
            link = session.get(ProjectCharacterLink, {"project_id": project_id, "character_id": line.character_id})
            if not link:
                raise HTTPException(status_code=400, detail=f"Character '{line.character_id}' is not linked to project '{project_id}'")
                
            # 1. Determine language for this line
            lang = line.language_override if line.language_override else project.language_code
            
            # 2. Base Prompt
            base_prompt = line.prompt_override if line.prompt_override else char.prompt_style
            
            # 3. Check for Language Profile to get Accents
            profile = session.exec(select(CharacterLanguageProfile).where(
                CharacterLanguageProfile.character_id == char.id,
                CharacterLanguageProfile.language_code == lang
            )).first()
            
            final_line_prompt = base_prompt or ""
            if profile and not profile.is_native and profile.accent_description:
                if final_line_prompt:
                    final_line_prompt += f". {profile.accent_description}"
                else:
                    final_line_prompt = profile.accent_description
        
        if lang not in preprocessors:
            try:
                preprocessors[lang] = PreprocessorFactory.get_preprocessor(lang)
                dictionaries[lang] = get_dictionary_for_language(session, lang)
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
                
        # Preprocess text
        processed_text = preprocessors[lang].process(line.text, dictionaries[lang])
        
        processed_lines.append(ProcessedLine(
            character_id=char.id if char else None,
            original_text=line.text,
            processed_text=processed_text
        ))
        script.append((char, processed_text, final_line_prompt))
        
    return project, script, processed_lines

@router.post("/preprocess-only", response_model=PreprocessOnlyResponse)
def preprocess_only(request: PreprocessRequest, session: Session = Depends(get_session)):
    """
    Test endpoint to see how the text will be processed (dictionary + ML) 
    before sending it to the Gemini TTS engine.
    """
    _, _, processed_lines = _process_lines(request.project_id, request.lines, session)
        
    return PreprocessOnlyResponse(
        scene_id="preview",
        processed_lines=processed_lines
    )

@router.post("/process-scene", response_model=ProcessSceneResponse)
def process_scene(request: ProcessSceneRequest, session: Session = Depends(get_session)):
    from db.models import Scene
    
    scene = session.get(Scene, request.scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
        
    lines = sorted(scene.lines, key=lambda l: l.order_index)
    if not lines:
        raise HTTPException(status_code=400, detail="Scene has no lines to process")
        
    project, script, _ = _process_lines(scene.project_id, lines, session)
        
    # 2. Generate audio using Gemini TTS
    client = GeminiAudioClient()
    try:
        # Save output in a project-specific folder
        output_dir = f"static/audio/{project.id}"
        os.makedirs(output_dir, exist_ok=True)
        
        file_path = client.generate_scene_audio(request.scene_id, script, output_dir=output_dir)
        
        # Save the audio url back to the Scene
        scene.audio_url = f"/{file_path}"
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio generation failed: {str(e)}")
        
    return ProcessSceneResponse(
        scene_id=request.scene_id,
        audio_file_url=f"/{file_path}"
    )
