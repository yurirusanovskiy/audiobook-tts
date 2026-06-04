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
    language_code: str = Field(default="ru-RU", description="Locale language code, e.g. 'ru-RU' or 'en-US'")
    voice_id: str = Field(description="Gemini prebuilt voice name, e.g. 'Kore' or 'Puck'")
    prompt_style: Optional[str] = Field(default=None, description="Natural language instructions for the TTS model, e.g. 'Read fast and cheerfully'")

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
