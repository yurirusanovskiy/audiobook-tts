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
            import ruaccent.accent_model
            import numpy as np
            
            # Monkey-patch AccentModel.put_accent to fix missing token_type_ids in ONNX input
            original_put_accent = ruaccent.accent_model.AccentModel.put_accent
            def patched_put_accent(self_obj, word):
                def softmax(x):
                    e_x = np.exp(x - np.max(x))
                    return e_x / e_x.sum(axis=-1, keepdims=True)
                lower_word = word.lower()
                inputs = self_obj.tokenizer(lower_word, return_tensors="np")
                inputs = {k: v.astype(np.int64) for k, v in inputs.items()}
                if "token_type_ids" not in inputs:
                    inputs["token_type_ids"] = np.zeros_like(inputs["input_ids"])
                outputs = self_obj.session.run(None, inputs)
                output_names = {output_key.name: idx for idx, output_key in enumerate(self_obj.session.get_outputs())}
                logits = outputs[output_names["logits"]]
                probabilities = softmax(logits)
                scores = np.max(probabilities, axis=-1)[0]
                labels = np.argmax(logits, axis=-1)[0]
                pred_with_scores = [{'label': self_obj.id2label[str(label)], 'score': float(score)} 
                                    for label, score in zip(labels, scores)]
                stressed_word = self_obj.render_stress(word, pred_with_scores)
                return stressed_word

            ruaccent.accent_model.AccentModel.put_accent = patched_put_accent

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
        4. Convert '+' to Unicode Combining Acute Accent (\u0301)
        Priority: User Dictionary > ruaccent ML.
        """
        protected_text = text
        placeholder_map = {}
        
        if dictionary:
            for i, (word, replacement) in enumerate(dictionary.items()):
                placeholder = f"CWORD{i}"
                placeholder_map[placeholder] = replacement
                
                # Treat 'е' and 'ё' as equivalent in the regex pattern
                escaped_word = re.escape(word)
                mapped_chars = []
                for char in escaped_word:
                    if char.lower() in ('е', 'ё'):
                        mapped_chars.append('[еёЕЁ]')
                    else:
                        mapped_chars.append(char)
                escaped_word = "".join(mapped_chars)
                
                pattern = re.compile(rf'\b{escaped_word}\b', re.IGNORECASE)
                protected_text = pattern.sub(placeholder, protected_text)

        accentuator = self._get_accentuator()
        try:
            processed_text = accentuator.process_all(protected_text)
        except Exception as e:
            print(f"[RussianPreprocessor] Warning: ruaccent failed ({e}), using original text.")
            processed_text = protected_text

        final_text = processed_text
        if dictionary:
            for placeholder, replacement in placeholder_map.items():
                final_text = final_text.replace(placeholder, replacement)
            
        # Convert '+' to Unicode Combining Acute Accent (\u0301)
        # We use string concatenation to safely pass the unicode character to re.sub
        final_text = re.sub(r'\+(.)', r'\1' + '\u0301', final_text)
            
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
