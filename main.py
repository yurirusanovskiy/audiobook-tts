from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from db.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs on startup
    print("Starting up (Alembic manages the DB)...")
    yield
    # This runs on shutdown
    print("Shutting down...")

app = FastAPI(
    title="Audiobook TTS Engine",
    description="API for managing audiobook characters, dictionaries, and generating TTS audio.",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Audiobook TTS Engine"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
