import os
from jinja2 import Environment, FileSystemLoader
from db.models import Character

# Get the absolute path to the templates directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Initialize Jinja2 environment
env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=False  # We do not want HTML escaping since SSML needs raw brackets, although text itself might need some escaping if it contains < or &
)

def escape_ssml(text: str) -> str:
    """Basic XML escaping to prevent SSML injection from the raw text."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def generate_ssml(text: str, character: Character) -> str:
    """
    Renders the SSML template with the character's voice settings and the processed text.
    """
    template = env.get_template("audio_tag.xml.j2")
    safe_text = escape_ssml(text)
    
    # Render the template
    ssml_output = template.render(
        text=safe_text,
        character=character
    )
    
    # Clean up whitespace slightly
    return ssml_output.strip()
