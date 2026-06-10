import requests
import json

data = {
  "word": "test_word",
  "phonetic_replacement": "test_word",
  "language": "ru-RU",
  "entry_type": "word"
}

# Assuming an entry with ID 1 exists, otherwise we just want to see validation errors.
response = requests.put('http://127.0.0.1:8000/api/v1/dictionary/1', json=data)
print("Status:", response.status_code)
print("Response:", response.text)
