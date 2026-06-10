import os
from sqlalchemy import select
from db.models import CharacterLanguageProfile

# we need to edit scenes.py
with open("api/v1/routes/scenes.py", "r") as f:
    content = f.read()

# I will just write a function to construct the prompt string.
