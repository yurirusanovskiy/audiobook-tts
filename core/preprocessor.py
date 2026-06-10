import re
from abc import ABC, abstractmethod
from typing import Dict, Optional

class BasePreprocessor(ABC):
    def __init__(self, language_code: str):
        self.language_code = language_code

    @abstractmethod
    def process(self, text: str, dictionary: Dict[str, str]) -> str:
        """Process text using language-specific logic and apply the phonetic dictionary."""
        pass

    def apply_dictionary(self, text: str, dictionary: Dict[str, str]) -> str:
        """Helper to apply phonetic replacements safely using whole-word regex matches."""
        if not dictionary:
            return text
            
        processed_text = text
        for word, replacement in dictionary.items():
            # Use regex to replace whole words only (case-insensitive)
            # This prevents replacing "he" inside "the"
            # Note: \b works well for English/Russian/Spanish/Romanian. 
            # For Hebrew, we might need a more specialized regex if \b doesn't cover all edge cases, 
            # but for an MVP this is the standard approach.
            pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
            processed_text = pattern.sub(replacement, processed_text)
            
        return processed_text

class EnglishPreprocessor(BasePreprocessor):
    def process(self, text: str, dictionary: Dict[str, str]) -> str:
        return self.apply_dictionary(text, dictionary)

class RomanianPreprocessor(BasePreprocessor):
    def process(self, text: str, dictionary: Dict[str, str]) -> str:
        return self.apply_dictionary(text, dictionary)

class SpanishPreprocessor(BasePreprocessor):
    def process(self, text: str, dictionary: Dict[str, str]) -> str:
        return self.apply_dictionary(text, dictionary)

class HebrewPreprocessor(BasePreprocessor):
    def process(self, text: str, dictionary: Dict[str, str]) -> str:
        return self.apply_dictionary(text, dictionary)

class RussianPreprocessor(BasePreprocessor):
    def __init__(self, language_code: str):
        super().__init__(language_code)
        self._accentuator = None

    def _get_accentuator(self):
        """Lazy load ruaccent so it doesn't consume RAM if not processing Russian."""
        if self._accentuator is None:
            print("[RussianPreprocessor] Loading ruaccent model...")
            from ruaccent import RUAccent
            # Initialize the model (using default or lightweight parameters depending on requirements)
            self._accentuator = RUAccent()
            self._accentuator.load(omograph_model_size='big_poetry', use_dictionary=True)
            print("[RussianPreprocessor] ruaccent model loaded.")
        return self._accentuator

    def process(self, text: str, dictionary: Dict[str, str]) -> str:
        """
        Flow for Russian:
        1. Replace dictionary words with unique English placeholders (e.g. CWORD0)
        2. Pass text through ruaccent (it ignores English words and processes Russian)
        3. Replace placeholders with the actual phonetic rules from the dictionary.
        Priority: User Dictionary > ruaccent ML.
        """
        if not dictionary:
            accentuator = self._get_accentuator()
            try:
                return accentuator.process_all(text)
            except Exception as e:
                print(f"[RussianPreprocessor] Warning: ruaccent failed ({e}), returning original text.")
                return text

        # 1. Protection phase (Placeholders)
        protected_text = text
        placeholder_map = {}
        
        for i, (word, replacement) in enumerate(dictionary.items()):
            placeholder = f"CWORD{i}"
            placeholder_map[placeholder] = replacement
            # Replace original word with placeholder
            pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
            protected_text = pattern.sub(placeholder, protected_text)

        # 2. Process the text with ruaccent
        accentuator = self._get_accentuator()
        try:
            processed_text = accentuator.process_all(protected_text)
        except Exception as e:
            print(f"[RussianPreprocessor] Warning: ruaccent failed ({e}), using original text.")
            processed_text = protected_text

        # 3. Restoration phase (Apply user phonetics)
        final_text = processed_text
        for placeholder, replacement in placeholder_map.items():
            final_text = final_text.replace(placeholder, replacement)
            
        # 4. Convert '+' to Unicode Combining Acute Accent (\u0301)
        # This converts both ruaccent's output AND the user's dictionary '+' marks
        final_text = re.sub(r'\+(.)', r'\1\u0301', final_text)
            
        return final_text

class PreprocessorFactory:
    _instances: Dict[str, BasePreprocessor] = {}

    @classmethod
    def get_preprocessor(cls, language_code: str) -> BasePreprocessor:
        """
        Returns the appropriate preprocessor singleton for the given language.
        Example language_code: 'en-US', 'ru-RU', 'ro-RO', 'he-IL', 'es-ES'.
        """
        prefix = language_code.lower().split('-')[0]  # Extract 'en', 'ru', 'ro', etc.
        
        if prefix not in cls._instances:
            match prefix:
                case 'ru':
                    cls._instances[prefix] = RussianPreprocessor(language_code)
                case 'en':
                    cls._instances[prefix] = EnglishPreprocessor(language_code)
                case 'ro':
                    cls._instances[prefix] = RomanianPreprocessor(language_code)
                case 'es':
                    cls._instances[prefix] = SpanishPreprocessor(language_code)
                case 'he':
                    cls._instances[prefix] = HebrewPreprocessor(language_code)
                case _:
                    # Fallback to English/Default for unknown languages
                    cls._instances[prefix] = EnglishPreprocessor(language_code)
                
        return cls._instances[prefix]
