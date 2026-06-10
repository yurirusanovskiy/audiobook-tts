from sqlmodel import Session, select
from db.database import engine
from db.models import Project, Character, ProjectCharacterLink, SceneLine
import uuid

def run():
    with Session(engine) as session:
        projects = session.exec(select(Project)).all()
        for project in projects:
            narrator = None
            for char in project.characters:
                if char.name.lower() == "narrator":
                    narrator = char
                    break
            
            if not narrator:
                print(f"Creating Narrator for project {project.id}")
                narrator = Character(
                    id=str(uuid.uuid4()),
                    name="Narrator",
                    gender="Any",
                    age_category="Any",
                    traits="Clear, articulate",
                    voice_id="Aoede",
                    prompt_style="Calm and clear"
                )
                session.add(narrator)
                session.commit()
                session.refresh(narrator)
                session.add(ProjectCharacterLink(project_id=project.id, character_id=narrator.id))
                session.commit()
                
            lines = session.exec(select(SceneLine).where(SceneLine.character_id == None)).all()
            # Only update lines for scenes belonging to this project
            for line in lines:
                if line.scene and line.scene.project_id == project.id:
                    line.character_id = narrator.id
                    session.add(line)
            session.commit()

if __name__ == "__main__":
    run()
