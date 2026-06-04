from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
from pydantic import BaseModel
from db.database import get_session
from db.models import Project, Character, ProjectCharacterLink

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=List[Project])
def read_projects(session: Session = Depends(get_session)):
    return session.exec(select(Project)).all()

@router.post("/", response_model=Project)
def create_project(project: Project, session: Session = Depends(get_session)):
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
