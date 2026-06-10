from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlmodel import Session, select
from typing import List, Optional
from pydantic import BaseModel
from db.database import get_session
from db.models import Project, Character, ProjectCharacterLink, Scene
import uuid
from datetime import datetime
from core.text_chunker import chunk_text

router = APIRouter(prefix="/projects", tags=["Projects"])

class ProjectReadWithStats(BaseModel):
    model_config = {"from_attributes": True}
    
    id: str
    title: str
    language_code: str
    created_at: datetime
    total_scenes: int = 0
    completed_scenes: int = 0

@router.get("/", response_model=List[ProjectReadWithStats])
def read_projects(session: Session = Depends(get_session)):
    projects = session.exec(select(Project)).all()
    results = []
    for p in projects:
        scenes = session.exec(select(Scene).where(Scene.project_id == p.id)).all()
        total_scenes = len(scenes)
        completed_scenes = sum(1 for s in scenes if s.status == "completed")
        p_stats = ProjectReadWithStats.model_validate(p)
        p_stats.total_scenes = total_scenes
        p_stats.completed_scenes = completed_scenes
        results.append(p_stats)
    return results

@router.post("/", response_model=Project)
def create_project(project: Project, session: Session = Depends(get_session)):
    if not project.id:
        project.id = f"project_{uuid.uuid4().hex[:8]}"
        
    db_project = session.get(Project, project.id)
    if db_project:
        raise HTTPException(status_code=400, detail="Project with this ID already exists")
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

@router.get("/{project_id}", response_model=Project)
def read_project(project_id: str, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    language_code: Optional[str] = None

@router.put("/{project_id}", response_model=Project)
def update_project(project_id: str, project_in: ProjectUpdate, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if project_in.title is not None:
        project.title = project_in.title
    if project_in.language_code is not None:
        project.language_code = project_in.language_code
        
    session.commit()
    session.refresh(project)
    return project

@router.delete("/{project_id}")
def delete_project(project_id: str, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    session.delete(project)
    session.commit()
    return {"ok": True, "message": "Project and all associated scenes deleted"}

@router.get("/{project_id}/characters", response_model=List[Character])
def read_project_characters(project_id: str, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.characters

class DiscoverCharactersRequest(BaseModel):
    raw_text: str

class CharacterDiscoverySuggestion(BaseModel):
    discovered_name: str
    traits: str
    gender: str
    age_category: str
    action: str  # "create_new" or "use_existing"
    existing_character_id: Optional[str] = None
    suggested_voice_id: Optional[str] = None

@router.post("/{project_id}/characters/discover", response_model=List[CharacterDiscoverySuggestion])
def discover_characters(project_id: str, req: DiscoverCharactersRequest, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # 1. Ask Gemini to discover characters in the text
    from core.gemini_client import GeminiTextClient
    client = GeminiTextClient()
    try:
        discovered_chars = client.discover_characters(req.raw_text)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Gemini API Error: {str(e)}")

    # 2. Find currently used voices in this project to avoid conflicts
    used_voices = {c.voice_id for c in project.characters}
    available_voices = ["Puck", "Charon", "Kore", "Fenrir", "Aoede"]

    suggestions = []
    
    for d_char in discovered_chars:
        # Search DB for matching gender and age
        # (Case insensitive or direct match)
        stmt = select(Character).where(
            Character.gender == d_char.gender,
            Character.age_category == d_char.age_category
        )
        matching_chars = session.exec(stmt).all()
        
        suggestion = CharacterDiscoverySuggestion(
            discovered_name=d_char.discovered_name,
            traits=d_char.traits,
            gender=d_char.gender,
            age_category=d_char.age_category,
            action="create_new"
        )

        # Try to find an existing character whose voice is not already taken by someone else in this project
        best_match = None
        for mc in matching_chars:
            if mc in project.characters:
                # Already linked, perfect! Use this.
                best_match = mc
                break
            if mc.voice_id not in used_voices:
                best_match = mc
                break

        if best_match:
            suggestion.action = "use_existing"
            suggestion.existing_character_id = best_match.id
            # Also register the voice as used for subsequent characters in this loop
            used_voices.add(best_match.voice_id)
        else:
            suggestion.action = "create_new"
            # Pick a free voice
            free_voices = [v for v in available_voices if v not in used_voices]
            if free_voices:
                suggestion.suggested_voice_id = free_voices[0]
                used_voices.add(free_voices[0])
            else:
                # Fallback if we run out of unique voices
                suggestion.suggested_voice_id = "Kore"

        suggestions.append(suggestion)

    return suggestions

class BatchSaveCharactersRequest(BaseModel):
    suggestions: List[CharacterDiscoverySuggestion]

@router.post("/{project_id}/characters/batch")
def batch_save_characters(project_id: str, req: BatchSaveCharactersRequest, session: Session = Depends(get_session)):
    import uuid
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    for suggestion in req.suggestions:
        if suggestion.action == "use_existing" and suggestion.existing_character_id:
            char = session.get(Character, suggestion.existing_character_id)
            if char and char not in project.characters:
                project.characters.append(char)
        elif suggestion.action == "create_new":
            new_id = str(uuid.uuid4())
            char = Character(
                id=new_id,
                name=suggestion.discovered_name,
                voice_id=suggestion.suggested_voice_id or "Kore",
                prompt_style=suggestion.traits,
                gender=suggestion.gender,
                age_category=suggestion.age_category
            )
            session.add(char)
            project.characters.append(char)
            
    session.commit()
    return {"ok": True, "message": f"Saved {len(req.suggestions)} characters to project"}

@router.post("/{project_id}/characters/{character_id}")
def link_character_to_project(project_id: str, character_id: str, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    character = session.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
        
    link = session.get(ProjectCharacterLink, {"project_id": project_id, "character_id": character_id})
    if link:
        return {"ok": True, "message": "Already linked"}
        
    new_link = ProjectCharacterLink(project_id=project_id, character_id=character_id)
    session.add(new_link)
    session.commit()
    return {"ok": True, "message": "Character linked to project"}

@router.delete("/{project_id}/characters/{character_id}")
def unlink_character_from_project(project_id: str, character_id: str, session: Session = Depends(get_session)):
    link = session.get(ProjectCharacterLink, {"project_id": project_id, "character_id": character_id})
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
        
    session.delete(link)
    session.commit()
    return {"ok": True, "message": "Character unlinked from project"}

@router.post("/{project_id}/upload-book")
async def upload_book(project_id: str, file: UploadFile = File(...), session: Session = Depends(get_session)):
    """Uploads a book file, extracts text, chunks it, and creates Scenes."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    content_bytes = await file.read()
    
    from core.file_parser import parse_uploaded_file
    raw_text = parse_uploaded_file(file.filename, content_bytes)
        
    from core.ml_text_chunker import chunk_text_semantically
    chunks = chunk_text_semantically(raw_text, max_chars=7000)
    
    # Calculate next order index for scenes
    existing_scenes = session.exec(select(Scene).where(Scene.project_id == project_id)).all()
    next_order = max([s.order_index for s in existing_scenes] + [-1]) + 1
    
    created_count = 0
    for chunk in chunks:
        scene_id = f"scene_{uuid.uuid4().hex[:8]}"
        scene = Scene(
            id=scene_id,
            project_id=project_id,
            title=f"Scene {next_order + created_count + 1}",
            order_index=next_order + created_count,
            raw_text=chunk
        )
        session.add(scene)
        created_count += 1
        
    session.commit()
    
    return {
        "ok": True, 
        "message": f"Successfully chunked book into {created_count} scenes.",
        "scenes_created": created_count
    }



