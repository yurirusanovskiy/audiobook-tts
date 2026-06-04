from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel
import uuid

from db.database import get_session
from db.models import Scene, SceneLine, Project
from core.gemini_client import GeminiTextClient

router = APIRouter()

class GenerateFromTextRequest(BaseModel):
    title: str
    raw_text: str

class SceneLineCreate(BaseModel):
    character_id: Optional[str] = None
    text: str
    language_override: Optional[str] = None
    prompt_override: Optional[str] = None

class SceneCreate(BaseModel):
    title: str
    lines: List[SceneLineCreate]

class SceneLineResponse(BaseModel):
    id: int
    scene_id: str
    character_id: Optional[str]
    text: str
    language_override: Optional[str]
    prompt_override: Optional[str]
    order_index: int

class SceneResponse(BaseModel):
    id: str
    project_id: str
    title: Optional[str]
    order_index: int
    audio_url: Optional[str]

class SceneDetailResponse(SceneResponse):
    lines: List[SceneLineResponse]

@router.get("/projects/{project_id}/scenes", response_model=List[SceneResponse])
def get_project_scenes(project_id: str, session: Session = Depends(get_session)):
    """List all scenes for a project, ordered by order_index."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    scenes = session.exec(select(Scene).where(Scene.project_id == project_id).order_by(Scene.order_index)).all()
    return scenes

@router.post("/projects/{project_id}/scenes", response_model=SceneDetailResponse)
def create_scene(project_id: str, scene_in: SceneCreate, session: Session = Depends(get_session)):
    """Create a new scene with its lines for a project."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    scene_id = f"scene_{uuid.uuid4().hex[:8]}"
    
    # Calculate next order index
    scenes = session.exec(select(Scene).where(Scene.project_id == project_id)).all()
    next_order = max([s.order_index for s in scenes] + [-1]) + 1
    
    scene = Scene(
        id=scene_id,
        project_id=project_id,
        title=scene_in.title,
        order_index=next_order
    )
    session.add(scene)
    
    for i, line_in in enumerate(scene_in.lines):
        line = SceneLine(
            scene_id=scene_id,
            character_id=line_in.character_id,
            text=line_in.text,
            language_override=line_in.language_override,
            prompt_override=line_in.prompt_override,
            order_index=i
        )
        session.add(line)
        
    session.commit()
    session.refresh(scene)
    return scene

@router.post("/projects/{project_id}/scenes/generate-from-text", response_model=SceneDetailResponse)
def generate_scene_from_text(project_id: str, request: GenerateFromTextRequest, session: Session = Depends(get_session)):
    """Automatically extracts script from raw text using Gemini 3.5 Flash and creates a scene."""
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    characters = project.characters
    
    text_client = GeminiTextClient()
    try:
        extracted_lines = text_client.extract_script_from_text(request.raw_text, characters)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    # Convert ExtractedLine to SceneLineCreate
    scene_lines = []
    for line in extracted_lines:
        scene_lines.append(SceneLineCreate(
            character_id=line.character_id,
            text=line.text,
            prompt_override=line.prompt_override,
            language_override=line.language_override
        ))
        
    scene_in = SceneCreate(
        title=request.title,
        lines=scene_lines
    )
    
    return create_scene(project_id, scene_in, session)

@router.get("/scenes/{scene_id}", response_model=SceneDetailResponse)
def get_scene(scene_id: str, session: Session = Depends(get_session)):
    """Get a specific scene and its lines."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    # ensure lines are ordered
    scene.lines = sorted(scene.lines, key=lambda l: l.order_index)
    return scene

class SceneUpdate(BaseModel):
    title: Optional[str] = None
    lines: Optional[List[SceneLineCreate]] = None

@router.put("/scenes/{scene_id}", response_model=SceneDetailResponse)
def update_scene(scene_id: str, scene_in: SceneUpdate, session: Session = Depends(get_session)):
    """Update a scene's title or completely overwrite its lines."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
        
    if scene_in.title is not None:
        scene.title = scene_in.title
        
    if scene_in.lines is not None:
        # Delete existing lines
        for line in scene.lines:
            session.delete(line)
            
        # Add new lines
        for i, line_in in enumerate(scene_in.lines):
            line = SceneLine(
                scene_id=scene_id,
                character_id=line_in.character_id,
                text=line_in.text,
                language_override=line_in.language_override,
                prompt_override=line_in.prompt_override,
                order_index=i
            )
            session.add(line)
            
    session.commit()
    session.refresh(scene)
    scene.lines = sorted(scene.lines, key=lambda l: l.order_index)
    return scene

@router.delete("/scenes/{scene_id}")
def delete_scene(scene_id: str, session: Session = Depends(get_session)):
    """Delete a scene and its lines."""
    scene = session.get(Scene, scene_id)
    if not scene:
        raise HTTPException(status_code=404, detail="Scene not found")
    
    session.delete(scene)
    session.commit()
    return {"status": "ok"}
