import os
import wave
import json
import re
import time
from typing import List, Tuple, Dict, Any, Optional
import datetime
from fastapi import HTTPException
from sqlmodel import Session, select
from db.database import engine
from db.models import Character, APIKey, Settings
from pydantic import BaseModel
from google import genai
from google.genai import types

def _get_active_api_key() -> str | None:
    with Session(engine) as sess:
        settings = sess.exec(select(Settings)).first()
        if settings and settings.active_api_key_id:
            key = sess.get(APIKey, settings.active_api_key_id)
            if key and not key.is_exhausted:
                return key.key_value
        
        # Fallback to first non-exhausted key
        key = sess.exec(select(APIKey).where(APIKey.is_exhausted == False)).first()
        if key:
            if settings:
                settings.active_api_key_id = key.id
                sess.add(settings)
                sess.commit()
            return key.key_value
        
        # Fallback to environment variable if no DB keys are active
        return os.environ.get("GEMINI_API_KEY")

def _mark_key_exhausted_and_switch(api_key_value: str):
    if not api_key_value:
        return
    with Session(engine) as sess:
        key = sess.exec(select(APIKey).where(APIKey.key_value == api_key_value)).first()
        if key:
            key.is_exhausted = True
            key.exhausted_until = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
            
            settings = sess.exec(select(Settings)).first()
            next_key = sess.exec(select(APIKey).where(APIKey.is_exhausted == False, APIKey.id != key.id)).first()
            if settings:
                settings.active_api_key_id = next_key.id if next_key else None
                sess.add(settings)
            sess.add(key)
            sess.commit()
            print(f"API Key {key.name} marked as exhausted. Switched to next key.")

class GeminiAudioClient:
    def __init__(self):
        self.api_key = _get_active_api_key()
        if not self.api_key:
            raise RuntimeError("No active Gemini API key found in Settings or Environment.")
        self.client = genai.Client(api_key=self.api_key)

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
            # Gemini TTS API strictly supports max 2 speakers per call.
            # The chunker should guarantee this, but log a warning if not.
            if len(speaker_configs) > 2:
                speaker_ids = [sc.speaker for sc in speaker_configs]
                print(f"WARNING: chunk has {len(speaker_configs)} unique speakers {speaker_ids}, "
                      f"truncating to first 2. Check chunking logic.")
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
                error_str = str(e)
                print(f"Gemini API Error (Attempt {attempt + 1}/{max_retries}): {error_str}")
                
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    print("RESOURCE_EXHAUSTED. Rotating API Key...")
                    _mark_key_exhausted_and_switch(self.api_key)
                    new_key = _get_active_api_key()
                    if new_key and new_key != self.api_key:
                        print("Successfully rotated to new key.")
                        self.api_key = new_key
                        self.client = genai.Client(api_key=self.api_key)
                        continue
                        
                    match = re.search(r'Please retry in ([0-9.]+)s', error_str)
                    if match:
                        wait_time = int(float(match.group(1))) + 1
                        print(f"Rate limit hit. Waiting {wait_time}s before retrying...")
                        time.sleep(wait_time)
                    else:
                        time.sleep(10)
                    continue

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

def _handle_gemini_error(e: Exception) -> Exception:
    error_str = str(e)
    if "RESOURCE_EXHAUSTED" in error_str or "429" in error_str:
        match = re.search(r'Please retry in ([0-9.]+)s', error_str)
        if match:
            wait_time = int(float(match.group(1)))
            return HTTPException(status_code=429, detail=f"Gemini API rate limit exceeded. Please wait {wait_time} seconds and try again.")
        return HTTPException(status_code=429, detail="Gemini API rate limit exceeded. Please wait a minute and try again.")
    if "UNAVAILABLE" in error_str or "503" in error_str:
        return HTTPException(status_code=503, detail="Gemini API is currently overloaded (503). Please try again in a few moments.")
    return RuntimeError(f"All fallback models failed. Last error: {e}")

class GeminiTextClient:
    def __init__(self):
        self.api_key = _get_active_api_key()
        if not self.api_key:
            raise RuntimeError("No active Gemini API key found in Settings or Environment.")
        self.client = genai.Client(api_key=self.api_key)

    def _generate_with_retry(self, user_prompt: str, system_instruction: str, response_schema: Any, max_retries: int = 3) -> Any:
        models_to_try = ["gemini-3.5-flash", "gemini-3.1-flash", "gemini-2.5-pro"]
        
        for attempt in range(max_retries):
            for model_name in models_to_try:
                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            response_mime_type="application/json",
                            response_schema=response_schema,
                        )
                    )
                    return response
                except Exception as e:
                    error_str = str(e)
                    print(f"Model {model_name} failed (Attempt {attempt+1}/{max_retries}): {error_str}")
                    
                    if "404" in error_str or "NOT_FOUND" in error_str:
                        continue
                    if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                        # Auto-rotate key
                        print("RESOURCE_EXHAUSTED. Rotating API Key...")
                        _mark_key_exhausted_and_switch(self.api_key)
                        # Re-init client with new key
                        new_key = _get_active_api_key()
                        if new_key and new_key != self.api_key:
                            print("Successfully rotated to new key.")
                            self.api_key = new_key
                            self.client = genai.Client(api_key=self.api_key)
                            # Do not break, just let it retry immediately with the new key!
                            continue
                            
                        # If no other keys, fallback to wait logic
                        match = re.search(r'Please retry in ([0-9.]+)s', error_str)
                        if match:
                            wait_time = int(float(match.group(1))) + 1
                            print(f"Rate limit hit. Waiting {wait_time}s before retrying...")
                            time.sleep(wait_time)
                        else:
                            time.sleep(10)
                        break 
                    if "503" in error_str or "UNAVAILABLE" in error_str:
                        time.sleep(5)
                        continue
            
            if attempt < max_retries - 1:
                time.sleep(5)
                
        raise RuntimeError("All models and retries failed.")
        
    def extract_script_from_text(self, raw_text: str, characters: List) -> List[ExtractedLine]:
        """
        Uses Gemini 3.5 Flash to automatically extract a script from raw text.
        `characters` can be List[Character] or List[ProjectCharacterResponse] (which has alias).
        The alias (project-specific book name) is used as the primary Name in the prompt so
        Gemini can match character names as they appear in the source text.
        """
        prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts", "script_extractor.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            system_instruction = f.read()

        # Use alias (project-specific name) as the Name sent to Gemini so it can match
        # names as they appear in the book. Fall back to global name if no alias set.
        char_list_str = "\n".join([
            f"- ID: {c.id}, Name: {getattr(c, 'alias', None) or c.name}, Role/Voice: {c.prompt_style or 'Default'}"
            for c in characters
        ])
        
        user_prompt = f"CHARACTERS:\n{char_list_str}\n\nRAW_TEXT:\n{raw_text}"
        
        response = self._generate_with_retry(user_prompt, system_instruction, list[ExtractedLine])
        
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
        
        response = self._generate_with_retry(user_prompt, system_instruction, list[DiscoveredCharacter])
        
        try:
            data = json.loads(response.text)
            chars = [DiscoveredCharacter(**item) for item in data]
            return chars
        except Exception as e:
            raise RuntimeError(f"Failed to parse Gemini 3.5 Flash output for discovery: {e}\nRaw response: {response.text}")
