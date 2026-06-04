import requests

BASE_URL = "http://localhost:8000/api/v1"

def print_result(name, res):
    print(f"--- {name} ---")
    print(f"Status: {res.status_code}")
    try:
        print(f"Response: {res.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response (Raw): {res.text}")
    print("-" * 30 + "\n")

def test_characters():
    print("=== Testing Characters API ===")
    
    # 1. Create Character
    char_data = {
        "id": "test_narrator",
        "name": "Test Narrator",
        "voice_id": "Puck",
        "prompt_style": "Speak clearly"
    }
    # Delete first if exists
    requests.delete(f"{BASE_URL}/characters/test_narrator")
    
    res = requests.post(f"{BASE_URL}/characters/", json=char_data)
    print_result("CREATE Character", res)
    
    # 2. Get All Characters
    res = requests.get(f"{BASE_URL}/characters/")
    print_result("GET All Characters", res)
    
    # 3. Get Single Character
    res = requests.get(f"{BASE_URL}/characters/test_narrator")
    print_result("GET Single Character", res)
    
    # 4. Delete Character
    res = requests.delete(f"{BASE_URL}/characters/test_narrator")
    print_result("DELETE Character", res)
    
    # 5. Verify Deletion
    res = requests.get(f"{BASE_URL}/characters/test_narrator")
    print_result("GET Deleted Character (Should be 404)", res)

def test_dictionary():
    print("=== Testing Dictionary API ===")
    
    # 1. Create Dictionary Entry
    dict_data = {
        "language": "ru",
        "word": "замок",
        "phonetic_replacement": "зам+ок"
    }
    res = requests.post(f"{BASE_URL}/dictionary/", json=dict_data)
    print_result("CREATE Dictionary Entry", res)
    
    entry_id = res.json().get("id")
    
    # 2. Get All Dictionary Entries
    res = requests.get(f"{BASE_URL}/dictionary/")
    print_result("GET All Dictionary Entries", res)
    
    # 3. Get Dictionary Entries by Language
    res = requests.get(f"{BASE_URL}/dictionary/?language=ru")
    print_result("GET Dictionary Entries (language=ru)", res)
    
    # 4. Get Dictionary Entries by wrong Language
    res = requests.get(f"{BASE_URL}/dictionary/?language=en")
    print_result("GET Dictionary Entries (language=en, should be empty)", res)
    
    # 5. Delete Dictionary Entry
    if entry_id:
        res = requests.delete(f"{BASE_URL}/dictionary/{entry_id}")
        print_result("DELETE Dictionary Entry", res)
        
        # 6. Verify Deletion
        res = requests.get(f"{BASE_URL}/dictionary/")
        print_result("GET All Dictionary (After deletion)", res)
    else:
        print("Failed to extract entry_id, skipping deletion tests.")

def test_projects_and_processing():
    print("=== Testing Projects & Processing API ===")
    
    # 1. Create Character (Jean - French guy)
    char_data = {
        "id": "test_jean",
        "name": "Jean Dupont",
        "voice_id": "Puck",
        "prompt_style": "Speak elegantly"
    }
    # Clean up first if needed
    requests.delete(f"{BASE_URL}/characters/test_jean")
    
    res = requests.post(f"{BASE_URL}/characters/", json=char_data)
    print_result("CREATE Character (Jean)", res)
    
    # 1.5 Create Language Profiles
    # Native French
    prof_fr = {
        "language_code": "fr-FR",
        "is_native": True
    }
    requests.post(f"{BASE_URL}/characters/test_jean/language-profiles/", json=prof_fr)
    
    # Russian with French Accent
    prof_ru = {
        "language_code": "ru-RU",
        "is_native": False,
        "accent_description": "Speaks Russian with a heavy French accent, rolling his R's"
    }
    requests.post(f"{BASE_URL}/characters/test_jean/language-profiles/", json=prof_ru)
    print("Created Language Profiles for Jean")
    
    # 2. Create Project (Russian book)
    project_data = {
        "id": "test_book_1",
        "title": "Russian Book with French Guest",
        "language_code": "ru-RU"
    }
    requests.post(f"{BASE_URL}/projects/", json=project_data) # Ignore if exists
    print("CREATE Project")
    
    # 3. Link Character to Project
    requests.post(f"{BASE_URL}/projects/test_book_1/characters/test_jean")
    print("LINK Character to Project")
    
    # 4. Test Scenes API
    scene_data = {
        "title": "Chapter 1",
        "lines": [
            {
                "character_id": "test_jean",
                "text": "Здравствуйте, меня зовут Жан." # Russian (should append accent)
            },
            {
                "character_id": "test_jean",
                "text": "Bonjour tout le monde!",
                "language_override": "fr-FR" # French override (native, no accent)
            },
            {
                "character_id": "test_jean",
                "text": "И я хочу кушать.",
                "prompt_override": "Whisper" # Should combine whisper + French accent
            }
        ]
    }
    res = requests.post(f"{BASE_URL}/projects/test_book_1/scenes", json=scene_data)
    print_result("CREATE Scene", res)
    scene_id = res.json().get("id")
    
    # 5. Test Preprocessing
    process_data = {
        "project_id": "test_book_1",
        "lines": scene_data["lines"]
    }
    res = requests.post(f"{BASE_URL}/processing/preprocess-only", json=process_data)
    print_result("TEST Preprocessing (Accents & Overrides)", res)
    
    # 6. Test Process Scene (Will fail if no API key, but we want to see it reach the endpoint)
    if scene_id:
        process_scene_data = {
            "scene_id": scene_id
        }
        res = requests.post(f"{BASE_URL}/processing/process-scene", json=process_scene_data)
        print_result("TEST Process Scene", res)
    
    # 7. Cleanup
    requests.delete(f"{BASE_URL}/projects/test_book_1") # Cascade deletes scenes and lines
    requests.delete(f"{BASE_URL}/projects/test_book_1/characters/test_jean")
    requests.delete(f"{BASE_URL}/characters/test_jean")

def test_ai_script_extractor():
    print("=== Testing AI Script Extractor (Phase 5) ===")
    print("Note: This requires a valid GEMINI_API_KEY to succeed.")
    
    # 1. Create a Project and some Characters
    requests.post(f"{BASE_URL}/projects/", json={"id": "ai_book_1", "title": "AI Test", "language_code": "ru-RU"})
    requests.post(f"{BASE_URL}/characters/", json={"id": "ai_alice", "name": "Alice", "voice_id": "Aoede"})
    requests.post(f"{BASE_URL}/characters/", json={"id": "ai_bob", "name": "Bob", "voice_id": "Puck"})
    
    requests.post(f"{BASE_URL}/projects/ai_book_1/characters/ai_alice")
    requests.post(f"{BASE_URL}/projects/ai_book_1/characters/ai_bob")
    
    # 2. Test generate-from-text endpoint
    raw_text = """
    Alice walked into the room, looking pale. 
    "Did you see the ghost, Bob?" she whispered nervously.
    Bob laughed out loud. "Ghosts aren't real, Alice! Stop acting like a child."
    """
    
    generate_data = {
        "title": "Chapter 1: The Ghost",
        "raw_text": raw_text
    }
    
    res = requests.post(f"{BASE_URL}/projects/ai_book_1/scenes/generate-from-text", json=generate_data)
    print_result("TEST AI Script Extractor", res)
    
    # 3. Cleanup
    requests.delete(f"{BASE_URL}/projects/ai_book_1")
    requests.delete(f"{BASE_URL}/characters/ai_alice")
    requests.delete(f"{BASE_URL}/characters/ai_bob")

if __name__ == "__main__":
    try:
        # Check if server is up
        requests.get("http://localhost:8000/")
        test_characters()
        test_dictionary()
        test_projects_and_processing()
        test_ai_script_extractor()
    except requests.exceptions.ConnectionError:
        print("Error: FastAPI server is not running on http://localhost:8000")
