import sys
from db.database import engine
from sqlmodel import Session
from api.v1.routes.projects import read_projects

try:
    with Session(engine) as session:
        results = read_projects(session)
        print("Success:", results)
except Exception as e:
    import traceback
    traceback.print_exc()
