import os
import wave
from typing import List, Tuple, Dict, Any, Optional
from google import genai
from google.genai import types
from db.models import Character
from pydantic import BaseModel

class GeminiAudioClient:
    def __init__(self):
        # GEMINI_API_KEY must be set in the environment
        self.client = genai.Client()

    def generate_audio_chunk(self, file_path: str, script: List[Tuple[Character, str, str]]) -> str:
        """
        Generates audio for a multi-speaker chunk using Gemini TTS.
        `script` is a list of tuples: (Character, processed_text, final_line_prompt)
        """
        if not script:
            raise ValueError("Empty script provided.")
            
        prompt_parts = []
        speaker_configs = []
        seen_speakers = {}

        for char, text, line_prompt in script:
            # Accumulate the dialogue with line-specific emotional/accent instructions
            if line_prompt:
                prompt_parts.append(f"({char.id} speaks: {line_prompt})")
            prompt_parts.append(f"{char.id}: {text}")
            
            # Keep track of unique speakers to configure their voices
            if char.id not in seen_speakers:
                seen_speakers[char.id] = char
                voice_name = char.voice_id if char.voice_id else "Kore"
                
                speaker_configs.append(
                    types.SpeakerVoiceConfig(
                        speaker=char.id,
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=voice_name
                            )
                        )
                    )
                )

        # Build prompt instructions
        speaker_names = list(seen_speakers.keys())
        speakers_list = ", ".join(speaker_names)
        
        instructions = [f"TTS the following conversation between {speakers_list}:"]
        
        # Inject global character styles (from Casting step)
        for char_id, char_obj in seen_speakers.items():
            if char_obj.prompt_style:
                instructions.append(f"Note on {char_id}'s voice: {char_obj.prompt_style}")
            if char_obj.pitch_override:
                instructions.append(f"Note on {char_id}'s pitch: Speak in a {char_obj.pitch_override} pitch.")
                
        instructions.append("\n" + "\n".join(prompt_parts))
        
        full_prompt = "\n".join(instructions)

        # Handle Gemini API limits: multi-speaker only supports EXACTLY 2 voices.
        if len(speaker_configs) == 1:
            speech_config = types.SpeechConfig(
                voice_config=speaker_configs[0].voice_config
            )
        else:
            # API strictly requires 2
            speech_config = types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=speaker_configs[:2]
                )
            )

        import time
        max_retries = 3
        base_delay = 2
        response = None
        
        for attempt in range(max_retries):
            try:
                # Gemini API call
                response = self.client.models.generate_content(
                    model="gemini-3.1-flash-tts-preview",
                    contents=full_prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["AUDIO"],
                        speech_config=speech_config,
                    )
                )
                break  # Success
            except Exception as e:
                print(f"Gemini API Error (Attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    raise RuntimeError(f"Gemini API failed after {max_retries} attempts: {str(e)}") from e
                time.sleep(base_delay)
                base_delay *= 2

        try:
            data = response.candidates[0].content.parts[0].inline_data.data
        except (IndexError, AttributeError) as e:
            raise RuntimeError(f"Failed to extract audio data from Gemini response. Response: {response}") from e

        # Save to wave file and normalize
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self._save_wave_file(file_path, data)
        
        from core.audio_utils import normalize_wav
        normalize_wav(file_path)
        
        return file_path

    def _save_wave_file(self, filename: str, pcm_data: bytes, channels: int = 1, rate: int = 24000, sample_width: int = 2):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm_data)

class ExtractedLine(BaseModel):
    character_id: Optional[str]
    text: str
    prompt_override: Optional[str] = None
    language_override: Optional[str] = None

class DiscoveredCharacter(BaseModel):
    discovered_name: str
    traits: str
    gender: str
    age_category: str

class GeminiTextClient:
    def __init__(self):
        self.client = genai.Client()
        
    def extract_script_from_text(self, raw_text: str, characters: List[Character]) -> List[ExtractedLine]:
        """
        Uses Gemini 3.5 Flash to automatically extract a script from raw text.
        """
        prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts", "script_extractor.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            system_instruction = f.read()
            
        char_list_str = "\n".join([f"- ID: {c.id}, Name: {c.name}, Role/Voice: {c.prompt_style or 'Default'}" for c in characters])
        
        user_prompt = f"CHARACTERS:\n{char_list_str}\n\nRAW_TEXT:\n{raw_text}"
        
        models_to_try = ["gemini-3.5-flash", "gemini-3.1-flash", "gemini-2.5-pro"]
        
        for model_name in models_to_try:
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        response_mime_type="application/json",
                        response_schema=list[ExtractedLine],
                    )
                )
                break # Success!
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                if model_name == models_to_try[-1]:
                    raise RuntimeError(f"All fallback models failed. Last error: {e}")
        
        import json
        
        try:
            data = json.loads(response.text)
            lines = [ExtractedLine(**item) for item in data]
            return lines
        except Exception as e:
            raise RuntimeError(f"Failed to parse Gemini 3.5 Flash output: {e}\nRaw response: {response.text}")

    def discover_characters(self, raw_text: str) -> List[DiscoveredCharacter]:
        """
        Uses Gemini 3.5 Flash to identify all unique characters in the text, their gender, and age.
        """
        prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts", "character_discoverer.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            system_instruction = f.read()
            
        user_prompt = f"RAW_TEXT:\n{raw_text}"
        
        models_to_try = ["gemini-3.5-flash", "gemini-3.1-flash", "gemini-2.5-pro"]
        
        for model_name in models_to_try:
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        response_mime_type="application/json",
                        response_schema=list[DiscoveredCharacter],
                    )
                )
                break # Success!
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                if model_name == models_to_try[-1]:
                    raise RuntimeError(f"All fallback models failed. Last error: {e}")
        
        import json
        
        try:
            data = json.loads(response.text)
            chars = [DiscoveredCharacter(**item) for item in data]
            return chars
        except Exception as e:
            raise RuntimeError(f"Failed to parse Gemini 3.5 Flash output for discovery: {e}\nRaw response: {response.text}")
