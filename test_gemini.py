import os
from db.models import Character
from core.gemini_client import GeminiAudioClient

def test_gemini_tts():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable is not set.")
        print("Please set it before running this test: export GEMINI_API_KEY='your_key'")
        return

    client = GeminiAudioClient()

    # Create mock characters
    narrator = Character(
        id="narrator",
        name="Narrator",
        voice_id="Puck",
        prompt_style="Read slowly and calmly like a storyteller."
    )
    
    hero = Character(
        id="hero",
        name="Hero",
        voice_id="Kore",
        prompt_style="Read loudly, cheerfully, and fast!"
    )

    # Create a mock scene script
    script = [
        (narrator, "Однажды в студеную зимнюю пору, я из лесу вышел."),
        (narrator, "Был сильный мороз."),
        (hero, "Эй, я здесь! Как дела?"),
        (narrator, "Ответил он с улыбкой.")
    ]

    print("Generating audio for scene...")
    try:
        output_file = client.generate_scene_audio(
            scene_id="test_scene_1",
            script=script,
            output_dir="test_outputs"
        )
        print(f"Success! Audio saved to: {output_file}")
    except Exception as e:
        print(f"Error generating audio: {e}")

if __name__ == "__main__":
    test_gemini_tts()
