from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel
import uuid
import os

from db.database import get_session
from db.models import Scene, SceneLine, Project, Character, DictionaryEntry, ProjectCharacterLink
from core.gemini_client import GeminiTextClient, GeminiAudioClient
from core.preprocessor import PreprocessorFactory

router = APIRouter()

class GenerateFromTextRequest(BaseModel):
    title: str
    raw_text: str

class SceneLineCreate(BaseModel):
    character_id: Optional[str] = None
    text: str
    phonetic_text: Optional[str] = None
    language_override: Optional[str] = None
    prompt_override: Optional[str] = None
    is_manual_phonetics: bool = False

class SceneCreate(BaseModel):
    title: str
    lines: List[SceneLineCreate]

from datetime import datetime

class LineAudioTakeResponse(BaseModel):
    id: int
    audio_url: str
    take_number: int
    created_at: datetime

class SceneLineResponse(BaseModel):
    id: int
    scene_id: str
    character_id: Optional[str]
    text: str
    phonetic_text: Optional[str]
    language_override: Optional[str]
    prompt_override: Optional[str]
    order_index: int
    is_manual_phonetics: bool
    audio_url: Optional[str]
    audio_takes: List[LineAudioTakeResponse] = []

class SceneResponse(BaseModel):
    id: str
    project_id: str
    title: Optional[str]
    order_index: int
    status: str
    raw_text: Optional[str]
    audio_url: Optional[str]

class SceneDetailResponse(SceneResponse):
    lines: List[SceneLineResponse]

@router.get("/projects/{project_id}/scenes", response_model=List[SceneResponse])
def get_project_scenes(project_id: str, session: Session = Depends(get_session)):
    """List all scenes for a project, ordered by order_index."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    scenes = session.exec(select(Scene).where(Scene.project_id == project_id).order_by(Scene.order_index)).all()
    return scenes

@router.post("/projects/{project_id}/scenes", response_model=SceneDetailResponse)
def create_scene(project_id: str, scene_in: SceneCreate, session: Session = Depends(get_session)):
    """Create a new scene with its lines for a project."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    scene_id = f"scene_{uuid.uuid4().hex[:8]}"
    
    # Calculate next order index
    scenes = session.exec(select(Scene).where(Scene.project_id == project_id)).all()
    next_order = max([s.order_index for s in scenes] + [-1]) + 1
    
    scene = Scene(
        id=scene_id,
        project_id=project_id,
        title=scene_in.title,
        order_index=next_order
    )
    session.add(scene)
    
    for i, line_in in enumerate(scene_in.lines):
        line = SceneLine(
            scene_id=scene_id,
            character_id=line_in.character_id,
            text=line_in.text,
            language_override=line_in.language_override,
            prompt_override=line_in.prompt_override,
            order_index=i
        )
        session.add(line)
        
    session.commit()
    session.refresh(scene)
    return scene

@router.post("/projects/{project_id}/scenes/generate-from-text", response_model=SceneDetailResponse)
def generate_scene_from_text(project_id: str, request: GenerateFromTextRequest, session: Session = Depends(get_session)):
    """Automatically extracts script from raw text using Gemini 3.5 Flash and creates a scene."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    characters = project.characters
    
    text_client = GeminiTextClient()
    try:
        extracted_lines = text_client.extract_script_from_text(request.raw_text, characters)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    # Convert ExtractedLine to SceneLineCreate
    scene_lines = []
    for line in extracted_lines:
        scene_lines.append(SceneLineCreate(
            character_id=line.character_id,
            text=line.text,
            prompt_override=line.prompt_override,
            language_override=line.language_override
        ))
        
    scene_in = SceneCreate(
        title=request.title,
        lines=scene_lines
    )
    
    return create_scene(project_id, scene_in, session)

@router.get("/scenes/{scene_id}", response_model=SceneDetailResponse)
def get_scene(scene_id: str, session: Session = Depends(get_session)):
    """Get a specific scene and its lines."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    # ensure lines are ordered
    scene.lines = sorted(scene.lines, key=lambda l: l.order_index)
    return scene

@router.post("/scenes/{scene_id}/extract", response_model=SceneDetailResponse)
def extract_script(scene_id: str, session: Session = Depends(get_session)):
    """Extract script from existing scene's raw_text."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    if not scene.raw_text:
        raise HTTPException(status_code=400, detail="Scene has no raw text")
        
    project = session.get(Project, scene.project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    text_client = GeminiTextClient()
    try:
        extracted_lines = text_client.extract_script_from_text(scene.raw_text, project.characters)
    except Exception as e:
        scene.status = "error"
        session.commit()
        raise HTTPException(status_code=500, detail=str(e))
        
    # Ensure Narrator character exists for this project
    narrator = None
    for char in project.characters:
        if char.name.lower() == "narrator":
            narrator = char
            break
            
    if not narrator:
        import uuid
        narrator = Character(
            id=str(uuid.uuid4()),
            name="Narrator",
            gender="Any",
            age_category="Any",
            traits="Clear, articulate",
            voice_id="Aoede",
            prompt_style="Calm and clear"
        )
        session.add(narrator)
        session.commit()
        session.refresh(narrator)
        session.add(ProjectCharacterLink(project_id=project.id, character_id=narrator.id))
        session.commit()

    # Delete old lines if any
    for line in scene.lines:
        session.delete(line)
        
    for i, line in enumerate(extracted_lines):
        scene_line = SceneLine(
            scene_id=scene_id,
            character_id=line.character_id if line.character_id else narrator.id,
            text=line.text,
            prompt_override=line.prompt_override,
            language_override=line.language_override,
            order_index=i
        )
        session.add(scene_line)
        
    scene.status = "extracted"
    session.commit()
    session.refresh(scene)
    scene.lines = sorted(scene.lines, key=lambda l: l.order_index)
    return scene

class SceneLineUpdate(BaseModel):
    id: Optional[int] = None
    character_id: Optional[str] = None
    text: str
    phonetic_text: Optional[str] = None
    language_override: Optional[str] = None
    prompt_override: Optional[str] = None
    is_manual_phonetics: bool = False
    audio_url: Optional[str] = None

class SceneUpdate(BaseModel):
    title: Optional[str] = None
    lines: Optional[List[SceneLineUpdate]] = None

@router.put("/scenes/{scene_id}", response_model=SceneDetailResponse)
def update_scene(scene_id: str, scene_in: SceneUpdate, session: Session = Depends(get_session)):
    """Update a scene's title or its lines without losing relations."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
        
    if scene_in.title is not None:
        scene.title = scene_in.title
        
    if scene_in.lines is not None:
        # Create a mapping of existing lines by ID
        existing_lines = {line.id: line for line in scene.lines}
        
        # Keep track of updated IDs to know which to delete
        updated_ids = set()
        
        for i, line_in in enumerate(scene_in.lines):
            if line_in.id and line_in.id in existing_lines:
                # Update existing line
                line = existing_lines[line_in.id]
                line.character_id = line_in.character_id
                line.text = line_in.text
                line.phonetic_text = line_in.phonetic_text
                line.language_override = line_in.language_override
                line.prompt_override = line_in.prompt_override
                if line_in.audio_url is not None:
                    line.audio_url = line_in.audio_url
                line.order_index = i
                line.is_manual_phonetics = line_in.is_manual_phonetics
                updated_ids.add(line_in.id)
            else:
                # Add new line
                line = SceneLine(
                    scene_id=scene_id,
                    character_id=line_in.character_id,
                    text=line_in.text,
                    audio_url=line_in.audio_url,
                    phonetic_text=line_in.phonetic_text,
                    language_override=line_in.language_override,
                    prompt_override=line_in.prompt_override,
                    order_index=i,
                    is_manual_phonetics=line_in.is_manual_phonetics
                )
                session.add(line)
                
        # Delete lines that were not in the updated list
        for line_id, line in existing_lines.items():
            if line_id not in updated_ids:
                session.delete(line)
            
    session.commit()
    session.refresh(scene)
    scene.lines = sorted(scene.lines, key=lambda l: l.order_index)
    return scene

@router.delete("/scenes/{scene_id}")
def delete_scene(scene_id: str, session: Session = Depends(get_session)):
    """Delete a scene and its lines."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    
    session.delete(scene)
    session.commit()
    return {"status": "ok"}

def _build_scene_chunks(scene: Scene, session: Session) -> list[list[tuple]]:
    """
    Groups scene lines into multi-speaker chunks, applying phonetics and extracting character instances.
    Returns: List of chunks. Each chunk is a list of tuples: (SceneLine, Character, processed_text).
    """
    project = session.get(Project, scene.project_id)
    lines = sorted(scene.lines, key=lambda l: l.order_index)
    if not lines:
        return []

    lang = project.language_code
    prefix = lang.lower().split('-')[0]
    db_dict = session.exec(select(DictionaryEntry).where(DictionaryEntry.language == prefix)).all()
    dictionary = {entry.word: entry.phonetic_replacement for entry in db_dict}
    preprocessor = PreprocessorFactory.get_preprocessor(lang)

    narrator = Character(id="narrator", name="Narrator", voice_id="Aoede", prompt_style="Calm and clear")
    script_items = []

    for line in lines:
        if line.is_manual_phonetics:
            processed_text = line.text
        else:
            line_lang = line.language_override if line.language_override else lang
            if line_lang != lang:
                line_preprocessor = PreprocessorFactory.get_preprocessor(line_lang)
                line_prefix = line_lang.lower().split('-')[0]
                line_dict_entries = session.exec(select(DictionaryEntry).where(DictionaryEntry.language == line_prefix)).all()
                line_dict = {e.word: e.phonetic_replacement for e in line_dict_entries}
                processed_text = line_preprocessor.process(line.text, line_dict)
            else:
                processed_text = preprocessor.process(line.text, dictionary)
        
        char = line.character if line.character else narrator
        script_items.append((line, char, processed_text))

    chunks = []
    current_chunk = []
    current_speakers = set()

    for item in script_items:
        line, char, processed_text = item
        
        if char.id == "narrator":
            if current_chunk and "narrator" not in current_speakers:
                chunks.append(current_chunk)
                current_chunk = []
                current_speakers = set()
            current_chunk.append(item)
            current_speakers.add(char.id)
        else:
            if "narrator" in current_speakers:
                chunks.append(current_chunk)
                current_chunk = []
                current_speakers = set()
                
            if char.id not in current_speakers and len(current_speakers) == 2:
                chunks.append(current_chunk)
                current_chunk = []
                current_speakers = set()
                
            current_chunk.append(item)
            current_speakers.add(char.id)
            
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


@router.post("/scenes/{scene_id}/generate-audio", response_model=SceneDetailResponse)
def generate_audio(scene_id: str, session: Session = Depends(get_session)):
    """Generate audio for a scene using Gemini TTS after preprocessing text."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
        
    project = session.get(Project, scene.project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if not scene.lines:
        raise HTTPException(status_code=400, detail="Scene has no lines to generate audio from.")

    chunks = _build_scene_chunks(scene, session)
    
    audio_client = GeminiAudioClient()
    from core.audio_utils import stitch_wavs
    import os
    
    scene_dir = f"static/audio/{scene_id}_stems"
    os.makedirs(scene_dir, exist_ok=True)
    
    chunk_files = []
    try:
        for idx, chunk in enumerate(chunks):
            # Extract script items from chunk: (Character, processed_text, prompt_override)
            script = [(item[1], item[2], item[0].prompt_override) for item in chunk]
            
            speakers_in_chunk = sorted(list(set([c.id for _, c, _ in chunk])))
            speakers_str = "_and_".join(speakers_in_chunk)
            chunk_file_path = os.path.join(scene_dir, f"{idx+1:02d}_{scene_id}_{speakers_str}.wav")
            
            # Generate audio for chunk
            audio_client.generate_audio_chunk(chunk_file_path, script)
            chunk_files.append(chunk_file_path)
            
            # Update audio_url for all lines in the chunk
            final_url = f"/{chunk_file_path}"
            for line, char, _ in chunk:
                line.audio_url = final_url
                session.add(line)
            
        # Stitch them together
        final_file_path = f"static/audio/{scene_id}.wav"
        stitch_wavs(chunk_files, final_file_path)
        
    except Exception as e:
        scene.status = "error"
        session.commit()
        raise HTTPException(status_code=500, detail=f"Audio generation failed: {str(e)}")
        
    scene.audio_url = f"/static/audio/{scene_id}.wav"
    scene.status = "completed"
    session.commit()
    session.refresh(scene)
    
    scene.lines = sorted(scene.lines, key=lambda l: l.order_index)
    return scene


from fastapi.responses import FileResponse
import zipfile
import shutil

@router.get("/scenes/{scene_id}/download-stems")
def download_scene_stems(scene_id: str, session: Session = Depends(get_session)):
    """Downloads all generated stems for a scene as a ZIP file."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
        
    scene_dir = f"static/audio/{scene_id}_stems"
    if not os.path.exists(scene_dir) or not os.listdir(scene_dir):
        raise HTTPException(status_code=404, detail="Stems not found for this scene. Please generate audio first.")
        
    zip_path = f"static/audio/{scene_id}_stems.zip"
    
    # Create zip file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(scene_dir):
            for file in files:
                if file.endswith('.wav'):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file)
                    
    return FileResponse(
        path=zip_path, 
        filename=f"{scene_id}_stems.zip", 
        media_type='application/zip'
    )

@router.post("/scenes/{scene_id}/lines/{line_id}/generate-audio", response_model=SceneLineResponse)
def generate_line_audio(scene_id: str, line_id: int, session: Session = Depends(get_session)):
    """Generate audio for the logical chunk containing a single scene line using Gemini TTS."""
    from db.models import LineAudioTake
    import time
    from core.audio_utils import stitch_wavs
    import os
    
    line = session.get(SceneLine, line_id)
    if not line or line.scene_id != scene_id:
        raise HTTPException(status_code=404, detail="Line not found")
        
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")

    # 1. Chunk the entire scene
    chunks = _build_scene_chunks(scene, session)
    
    # 2. Find the chunk that contains the target line
    target_chunk = None
    target_idx = -1
    for idx, chunk in enumerate(chunks):
        if any(item[0].id == line_id for item in chunk):
            target_chunk = chunk
            target_idx = idx
            break
            
    if not target_chunk:
        raise HTTPException(status_code=500, detail="Line not found in any chunk")
        
    # 3. Generate audio for this specific chunk
    audio_client = GeminiAudioClient()
    scene_dir = f"static/audio/{scene_id}_stems"
    os.makedirs(scene_dir, exist_ok=True)
    
    # Extract script items from chunk: (Character, processed_text, prompt_override)
    script = [(item[1], item[2], item[0].prompt_override) for item in target_chunk]
    
    speakers_in_chunk = sorted(list(set([c.id for _, c, _ in target_chunk])))
    speakers_str = "_and_".join(speakers_in_chunk)
    
    # Calculate next take number based on the primary line requested
    take_number = len(line.audio_takes) + 1
    # Add timestamp to ensure uniqueness and prevent overwriting
    timestamp = int(time.time())
    chunk_file_path = os.path.join(scene_dir, f"{target_idx+1:02d}_{scene_id}_{speakers_str}_take{take_number}_{timestamp}.wav")
    
    try:
        audio_client.generate_audio_chunk(chunk_file_path, script)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio generation failed: {str(e)}")

    final_url = f"/{chunk_file_path}"
    
    # Update audio_url for all lines in the chunk
    for chunk_line, _, _ in target_chunk:
        chunk_line.audio_url = final_url
        
        # We'll create for all lines in the chunk.
        t_num = len(chunk_line.audio_takes) + 1
        take = LineAudioTake(
            scene_line_id=chunk_line.id,
            audio_url=final_url,
            take_number=t_num
        )
        session.add(take)
        session.add(chunk_line)
        
    # Flush to ensure DB has updated audio_urls before we read them for stitching
    session.flush()
        
    # 4. Re-stitch the full scene
    # We reconstruct the file paths for all chunks using the saved audio_url of the first line in each chunk
    chunk_files = []
    for idx, chunk in enumerate(chunks):
        c_line = chunk[0][0]
        if c_line.audio_url:
            c_path = c_line.audio_url.lstrip("/") # Remove leading slash to get local path
            if os.path.exists(c_path):
                chunk_files.append(c_path)
            
    if chunk_files:
        final_scene_file = f"static/audio/{scene_id}.wav"
        stitch_wavs(chunk_files, final_scene_file)
        scene.audio_url = f"/{final_scene_file}"
        session.add(scene)
    
    session.commit()
    session.refresh(line)
    
    return line
