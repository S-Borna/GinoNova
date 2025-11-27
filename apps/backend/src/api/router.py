from fastapi import APIRouter
from .system import system_router
from .auth import auth_router
from .version import router as version_router
from .modules import modules_router

api_router = APIRouter()

api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(version_router, prefix="/version", tags=["version"])
api_router.include_router(modules_router, prefix="/modules", tags=["modules"])
