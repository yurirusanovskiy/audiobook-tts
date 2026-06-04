from fastapi import APIRouter
from api.v1.routes import characters, dictionary, processing

v1_router = APIRouter()

v1_router.include_router(characters.router)
v1_router.include_router(dictionary.router)
v1_router.include_router(processing.router)
