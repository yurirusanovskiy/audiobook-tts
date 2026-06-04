import requests

BASE_URL = "http://localhost:8000/api/v1"

def print_result(name, res):
    print(f"--- {name} ---")
    print(f"Status: {res.status_code}")
    print(f"Response: {res.json()}")
    print("-" * 30 + "\n")

def test_characters():
    print("=== Testing Characters API ===")
    
    # 1. Create Character
    char_data = {
        "id": "test_narrator",
        "name": "Test Narrator",
        "language_code": "ru-RU",
        "voice_id": "Puck",
        "prompt_style": "Speak clearly"
    }
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

if __name__ == "__main__":
    try:
        # Check if server is up
        requests.get("http://localhost:8000/")
        test_characters()
        test_dictionary()
    except requests.exceptions.ConnectionError:
        print("Error: FastAPI server is not running on http://localhost:8000")
