import os
import wave
from typing import List, Tuple
from google import genai
from google.genai import types
from db.models import Character

class GeminiAudioClient:
    def __init__(self):
        # GEMINI_API_KEY must be set in the environment
        self.client = genai.Client()

    def generate_scene_audio(self, scene_id: str, script: List[Tuple[Character, str]], output_dir: str = "output") -> str:
        """
        Generates audio for a multi-speaker scene using Gemini TTS.
        `script` is a list of tuples: (Character, processed_text)
        """
        if not script:
            raise ValueError("Empty script provided.")
            
        prompt_parts = []
        speaker_configs = []
        seen_speakers = {}

        for char, text in script:
            # Accumulate the dialogue
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
        
        # Add prompt styles if any character has one
        for char_id, char in seen_speakers.items():
            if char.prompt_style:
                instructions.append(f"{char_id} should speak: {char.prompt_style}")
                
        instructions.append("\n" + "\n".join(prompt_parts))
        
        full_prompt = "\n".join(instructions)

        # Gemini API call
        response = self.client.models.generate_content(
            model="gemini-3.1-flash-tts-preview",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=speaker_configs
                    )
                ),
            )
        )

        try:
            data = response.candidates[0].content.parts[0].inline_data.data
        except (IndexError, AttributeError) as e:
            raise RuntimeError(f"Failed to extract audio data from Gemini response. Response: {response}") from e

        # Save to wave file
        os.makedirs(output_dir, exist_ok=True)
        file_name = os.path.join(output_dir, f"{scene_id}.wav")
        self._save_wave_file(file_name, data)
        
        return file_name

    def _save_wave_file(self, filename: str, pcm_data: bytes, channels: int = 1, rate: int = 24000, sample_width: int = 2):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm_data)
