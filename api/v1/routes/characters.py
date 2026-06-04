from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from db.database import get_session
from db.models import Character, CharacterLanguageProfile

router = APIRouter(prefix="/characters", tags=["Characters"])

@router.get("/", response_model=List[Character])
def read_characters(session: Session = Depends(get_session)):
    characters = session.exec(select(Character)).all()
    return characters

@router.get("/{character_id}", response_model=Character)
def read_character(character_id: str, session: Session = Depends(get_session)):
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/", response_model=Character)
def create_character(character: Character, session: Session = Depends(get_session)):
    db_char = session.get(Character, character.id)
    if db_char:
        raise HTTPException(status_code=400, detail="Character with this ID already exists")
    session.add(character)
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
