import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
from pydantic import BaseModel
from db.database import get_session
from db.models import Character, CharacterLanguageProfile
from core.gemini_client import GeminiAudioClient
from core.preprocessor import PreprocessorFactory

class CharacterResponse(BaseModel):
    id: str
    name: str
    voice_id: str
    prompt_style: Optional[str] = None
    gender: Optional[str] = None
    age_category: Optional[str] = None
    sample_audio_url: Optional[str] = None
    language_profiles: List[CharacterLanguageProfile] = []

router = APIRouter(prefix="/characters", tags=["Characters"])

@router.get("/", response_model=List[CharacterResponse])
def read_characters(session: Session = Depends(get_session)):
    characters = session.exec(select(Character)).all()
    return characters

@router.get("/{character_id}", response_model=CharacterResponse)
def read_character(character_id: str, session: Session = Depends(get_session)):
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/", response_model=CharacterResponse)
def create_character(character: Character, session: Session = Depends(get_session)):
    db_char = session.get(Character, character.id)
    if db_char:
        raise HTTPException(status_code=400, detail="Character with this ID already exists")
    session.add(character)
    session.commit()
    session.refresh(character)
    return character

class CharacterUpdate(BaseModel):
    name: Optional[str] = None
    voice_id: Optional[str] = None
    prompt_style: Optional[str] = None
    gender: Optional[str] = None
    age_category: Optional[str] = None

@router.put("/{character_id}", response_model=CharacterResponse)
def update_character(character_id: str, char_in: CharacterUpdate, session: Session = Depends(get_session)):
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    if char_in.name is not None:
        character.name = char_in.name
    if char_in.voice_id is not None:
        character.voice_id = char_in.voice_id
    if char_in.prompt_style is not None:
        character.prompt_style = char_in.prompt_style
    if char_in.gender is not None:
        character.gender = char_in.gender
    if char_in.age_category is not None:
        character.age_category = char_in.age_category
        
    session.commit()
    session.refresh(character)
    return character

@router.delete("/{character_id}")
def delete_character(character_id: str, session: Session = Depends(get_session)):
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    session.delete(character)
    session.commit()
    return {"ok": True}

@router.post("/{character_id}/language-profiles/", response_model=CharacterLanguageProfile)
def create_language_profile(character_id: str, profile: CharacterLanguageProfile, session: Session = Depends(get_session)):
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
        
    profile.character_id = character_id
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile

@router.delete("/{character_id}/language-profiles/{profile_id}")
def delete_language_profile(character_id: str, profile_id: int, session: Session = Depends(get_session)):
    profile = session.get(CharacterLanguageProfile, profile_id)
    if not profile or profile.character_id != character_id:
        raise HTTPException(status_code=404, detail="Profile not found")
        
    session.delete(profile)
    session.commit()
    return {"ok": True}

class CharacterLanguageProfileUpdate(BaseModel):
    language_code: Optional[str] = None
    is_native: Optional[bool] = None
    accent_description: Optional[str] = None

@router.put("/{character_id}/language-profiles/{profile_id}", response_model=CharacterLanguageProfile)
def update_language_profile(character_id: str, profile_id: int, profile_in: CharacterLanguageProfileUpdate, session: Session = Depends(get_session)):
    profile = session.get(CharacterLanguageProfile, profile_id)
    if not profile or profile.character_id != character_id:
        raise HTTPException(status_code=404, detail="Profile not found")
        
    if profile_in.language_code is not None:
        profile.language_code = profile_in.language_code
    if profile_in.is_native is not None:
        profile.is_native = profile_in.is_native
    if profile_in.accent_description is not None:
        profile.accent_description = profile_in.accent_description
        
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile

@router.post("/{character_id}/generate-sample", response_model=CharacterResponse)
def generate_sample(character_id: str, session: Session = Depends(get_session)):
    char = session.get(Character, character_id)
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")
        
    # Construct base sample text
    text = f"Привет! Меня зовут {char.name}, а так звучит мой голос."
    
    # Run through ruaccent
    try:
        preprocessor = PreprocessorFactory.get_preprocessor("ru-RU")
        text_for_tts = preprocessor.process(text, {})
    except Exception as e:
        print(f"Failed to run ruaccent for sample: {e}")
        text_for_tts = text
        
    # Build prompt
    parts = []
    if char.gender:
        parts.append(char.gender.capitalize())
    if char.age_category:
        parts.append(char.age_category.capitalize())
    if char.pitch_override:
        parts.append(char.pitch_override.capitalize() + " pitch")
        
    base_voice = ", ".join(parts)
    final_prompt = f"[{base_voice}]" if base_voice else ""
    if char.prompt_style:
        final_prompt += f" {char.prompt_style}."
        
    profile = next((p for p in char.language_profiles if p.language_code.lower().startswith("ru")), None)
    if profile:
        if profile.is_native:
            final_prompt += " Speaks native Russian."
        elif profile.accent_description:
            final_prompt += f" Speaks Russian with {profile.accent_description}."
            
    final_prompt = final_prompt.strip()
    
    # Save to file path setup
    os.makedirs("static/samples", exist_ok=True)
    filename = f"{char.id}.wav"
    filepath = os.path.join("static", "samples", filename)

    # Call Gemini
    audio_client = GeminiAudioClient()
    try:
        # Wrap into the script tuple expected by generate_audio_chunk
        # (Character, text, line_prompt)
        script = [(char, text_for_tts, final_prompt)]
        audio_client.generate_audio_chunk(filepath, script)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini generation failed: {e}")
        
    # Update DB
    url = f"/static/samples/{filename}"
    char.sample_audio_url = url
    session.add(char)
    session.commit()
    session.refresh(char)
    
    return char
