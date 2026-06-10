# Audiobook TTS Generator (Backend)

This is the FastAPI backend for the **Audiobook TTS Generator**. It serves as the core engine that handles data persistence, text preprocessing, and integration with the Google Gemini Text-to-Speech API.

## 🚀 Features

- **RESTful API**: Clean, well-documented endpoints for Projects, Scenes, Characters, and Dictionary management.
- **Database Architecture**: SQLite database with declarative models via `SQLModel` and schema migrations managed by `Alembic`.
- **Russian Phonetic Preprocessing**: Uses `ruaccent` to automatically place stress marks on Russian text, drastically improving the pronunciation accuracy of the TTS engine.
- **Multi-Speaker TTS Engine**: Integrates with `google-genai` (Gemini 3.1 Flash TTS Preview) to synthesize realistic, expressive, multi-character dialogues in a single generation pass.
- **Dynamic Prompting**: Combines base character traits (gender, age, accent) with line-specific expressions (e.g., "screaming", "crying") into structured Gemini prompts.

## 🛠 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [SQLModel](https://sqlmodel.tiangolo.com/) + SQLite
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **TTS Engine**: Google Gemini API (`google-genai`)
- **NLP / Phonetics**: `ruaccent`
- **Package Manager**: `uv`

## 📦 Getting Started

### Prerequisites
- Python 3.10+
- `uv` (Python package manager)
- A valid Google Gemini API Key

### Installation

1. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

2. Set up your environment variables. Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. Run database migrations:
   ```bash
   uv run alembic upgrade head
   ```

4. Start the development server:
   ```bash
   uv run uvicorn main:app --reload --reload-exclude '*.db'
   ```

The API will be available at `http://localhost:8000`. 
Interactive API documentation (Swagger UI) is available at `http://localhost:8000/docs`.

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

*Disclaimer: This project uses the `ruaccent` library and the Google Gemini API. Please ensure your usage complies with the [Google API Terms of Service](https://developers.google.com/terms).*
