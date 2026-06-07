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

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.v1.router import v1_router

app = FastAPI(
    title="Audiobook TTS Engine",
    description="API for managing audiobook characters, dictionaries, and generating TTS audio.",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory for serving generated audio files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API v1 routes
app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Audiobook TTS Engine"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
