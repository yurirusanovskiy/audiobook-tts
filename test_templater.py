from core.templater import generate_ssml
from db.models import Character

def test():
    # Create a dummy character
    narrator = Character(
        id="narrator_ru",
        name="Narrator",
        language_code="ru-RU",
        voice_id="ru-RU-Wavenet-A",
        pitch="-2st",
        speed=1.05
    )
    
    text = "З+амок б+ыл закр+ыт на З+амок."
    
    # Generate SSML
    ssml = generate_ssml(text, narrator)
    print("--- Generated SSML ---")
    print(ssml)
    print("----------------------")

if __name__ == "__main__":
    test()
