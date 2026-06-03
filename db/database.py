import os
from typing import Generator
from sqlmodel import SQLModel, create_engine, Session

# Import models to ensure they are registered with SQLModel's metadata
from db.models import Character, DictionaryEntry

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///audiobook_core.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)

def create_db_and_tables():
    """Create all tables in the database if they don't exist yet."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Dependency for getting a database session."""
    with Session(engine) as session:
        yield session
