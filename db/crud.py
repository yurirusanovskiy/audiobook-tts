from typing import Dict, List
from sqlmodel import Session, select
from db.models import DictionaryEntry

def get_dictionary_for_language(session: Session, language_code: str) -> Dict[str, str]:
    """
    Fetches all dictionary entries for a specific language and returns them as a key-value mapping.
    The language_code is expected to be either a full locale (e.g., 'ru-RU') or just the prefix ('ru').
    We match based on the language prefix to keep things simple.
    """
    prefix = language_code.lower().split('-')[0]
    
    statement = select(DictionaryEntry).where(DictionaryEntry.language == prefix)
    results = session.exec(statement).all()
    
    return {entry.word: entry.phonetic_replacement for entry in results}

def get_available_dictionary_languages(session: Session) -> List[str]:
    """
    Returns a list of unique language codes that currently have entries in the dictionary.
    Useful for the frontend to show which languages have custom rules.
    """
    statement = select(DictionaryEntry.language).distinct()
    results = session.exec(statement).all()
    
    return list(results)
