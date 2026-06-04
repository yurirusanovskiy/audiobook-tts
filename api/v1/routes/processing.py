import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from pydantic import BaseModel
from db.database import get_session
from db.models import Character
from core.preprocessor import PreprocessorFactory
from core.gemini_client import GeminiAudioClient

router = APIRouter(prefix="/processing", tags=["Processing"])

class SceneLine(BaseModel):
    character_id: str
    text: str

class ProcessSceneRequest(BaseModel):
    scene_id: str
    language_code: str = "ru-RU"
    lines: List[SceneLine]

class ProcessSceneResponse(BaseModel):
    scene_id: str
    audio_file_url: str

class ProcessedLine(BaseModel):
    character_id: str
    original_text: str
    processed_text: str

class PreprocessOnlyResponse(BaseModel):
    scene_id: str
    processed_lines: List[ProcessedLine]

from db.crud import get_dictionary_for_language

@router.post("/preprocess-only", response_model=PreprocessOnlyResponse)
def preprocess_only(request: ProcessSceneRequest, session: Session = Depends(get_session)):
    """
    Test endpoint to see how the text will be processed (dictionary + ML) 
    before sending it to the Gemini TTS engine.
    """
    processed_lines = []
    
    try:
        preprocessor = PreprocessorFactory.get_preprocessor(request.language_code)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    dictionary = get_dictionary_for_language(session, request.language_code)
        
    for line in request.lines:
        char = session.get(Character, line.character_id)
        if not char:
            raise HTTPException(status_code=404, detail=f"Character '{line.character_id}' not found in DB")
        
        # Preprocess text
        processed_text = preprocessor.process(line.text, dictionary)
        
        processed_lines.append(ProcessedLine(
            character_id=char.id,
            original_text=line.text,
            processed_text=processed_text
        ))
        
    return PreprocessOnlyResponse(
        scene_id=request.scene_id,
        processed_lines=processed_lines
    )

@router.post("/process-scene", response_model=ProcessSceneResponse)
def process_scene(request: ProcessSceneRequest, session: Session = Depends(get_session)):
    # 1. Map requested lines to DB characters and preprocess text
    script = []
    
    try:
        preprocessor = PreprocessorFactory.get_preprocessor(request.language_code)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    dictionary = get_dictionary_for_language(session, request.language_code)
        
    for line in request.lines:
        char = session.get(Character, line.character_id)
        if not char:
            raise HTTPException(status_code=404, detail=f"Character '{line.character_id}' not found in DB")
        
        # Preprocess text (apply custom dictionary, ruaccent, etc.)
        processed_text = preprocessor.process(line.text, dictionary)
        
        script.append((char, processed_text))
        
    # 2. Generate audio using Gemini TTS
    client = GeminiAudioClient()
    try:
        # We save output in a public folder to serve it statically
        output_dir = "static/audio"
        file_path = client.generate_scene_audio(request.scene_id, script, output_dir=output_dir)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio generation failed: {str(e)}")
        
    return ProcessSceneResponse(
        scene_id=request.scene_id,
        # Create a URL path relative to the root where static files are mounted
        audio_file_url=f"/{file_path}"
    )
