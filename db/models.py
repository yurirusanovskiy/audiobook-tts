from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class ProjectCharacterLink(SQLModel, table=True):
    project_id: str = Field(foreign_key="project.id", primary_key=True)
    character_id: str = Field(foreign_key="character.id", primary_key=True)

class Project(SQLModel, table=True):
    id: str = Field(primary_key=True, description="Unique identifier for the project, e.g., 'harry_potter_1'")
    title: str = Field(index=True, description="Human-readable title of the book/project")
    language_code: str = Field(default="ru-RU", description="Default language of the project")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    characters: List["Character"] = Relationship(back_populates="projects", link_model=ProjectCharacterLink)

class CharacterLanguageProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    character_id: str = Field(foreign_key="character.id", index=True)
    language_code: str = Field(index=True, description="The language this profile applies to (e.g., 'ru-RU')")
    is_native: bool = Field(default=True, description="True if the character speaks this language perfectly")
    accent_description: Optional[str] = Field(default=None, description="e.g., 'Speaks with a heavy French accent'")
    
    character: "Character" = Relationship(back_populates="language_profiles")

class Character(SQLModel, table=True):
    id: str = Field(
        primary_key=True, 
        description="Unique identifier for the character, used in YAML files (e.g., 'alex', 'ai_core')"
    )
    name: str = Field(
        index=True, 
        description="Display name of the character for UI/Logs"
    )
    voice_id: str = Field(description="Gemini prebuilt voice name, e.g. 'Kore' or 'Puck'")
    prompt_style: Optional[str] = Field(default=None, description="Natural language instructions for the TTS model, e.g. 'Read fast and cheerfully'")
    
    projects: List[Project] = Relationship(back_populates="characters", link_model=ProjectCharacterLink)
    language_profiles: List[CharacterLanguageProfile] = Relationship(back_populates="character")

class DictionaryEntry(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, 
        primary_key=True
    )
    language: str = Field(
        index=True, 
        description="Language code to prevent rules leaking across languages (e.g., 'ru', 'ro')"
    )
    word: str = Field(
        index=True, 
        unique=True, 
        description="The original word/phrase to be replaced"
    )
    phonetic_replacement: str = Field(
        description="The phonetic pronunciation or custom replacement"
    )
