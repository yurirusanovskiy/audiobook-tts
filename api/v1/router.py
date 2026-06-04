from fastapi import APIRouter
from api.v1.routes import characters, dictionary, processing, projects, scenes

v1_router = APIRouter()

v1_router.include_router(characters.router, prefix="/characters", tags=["Characters"])
v1_router.include_router(dictionary.router)
v1_router.include_router(processing.router, prefix="/processing", tags=["Processing"])
v1_router.include_router(projects.router, prefix="", tags=["Projects"])
v1_router.include_router(scenes.router, prefix="", tags=["Scenes"])
