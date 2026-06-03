from typing import Optional
from sqlmodel import SQLModel, Field

class Character(SQLModel, table=True):
    id: str = Field(
        primary_key=True, 
        description="Unique identifier for the character, used in YAML files (e.g., 'alex', 'ai_core')"
    )
    name: str = Field(
        index=True, 
        description="Display name of the character for UI/Logs"
    )
    language_code: str = Field(
        index=True, 
        description="Language locale of the voice (e.g., 'ru-RU', 'en-US', 'ro-RO')"
    )
    voice_id: str = Field(
        description="Google TTS voice name, e.g., 'en-US-Journey-F'"
    )
    pitch: str = Field(
        default="+0st", 
        description="Voice pitch adjustment in semitones (e.g., '+2st', '-3st') to create kids or giants"
    )
    speed: float = Field(
        default=1.0, 
        description="Voice speed adjustment (0.5 to 2.0)"
    )

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
