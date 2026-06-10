import sys
from dotenv import load_dotenv
load_dotenv()
from core.gemini_client import GeminiTextClient

client = GeminiTextClient()
try:
    print("Discovering...")
    res = client.discover_characters("Mr. Holmes sat down. Dr. Watson was amazed.")
    print("Res:", res)
except Exception as e:
    import traceback
    traceback.print_exc()
