import re
text = "зам+ок"
result = re.sub(r'\+(.)', r'\1\u0301', text)
print(f"ORIGINAL: {text}")
print(f"RESULT: {result}")
