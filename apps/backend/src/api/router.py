from fastapi import APIRouter
from .system import system_router
from .auth import auth_router
from .version import router as version_router
from .modules import modules_router
from .tasks import tasks_router
from .studyflow import studyflow_router
from .progress import progress_router
from .dashboard import dashboard_router

api_router = APIRouter()

api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(version_router, prefix="/version", tags=["version"])
api_router.include_router(modules_router, prefix="/modules", tags=["modules"])
api_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
api_router.include_router(studyflow_router, prefix="/studyflow", tags=["studyflow"])
api_router.include_router(progress_router, prefix="/progress", tags=["progress"])
api_router.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])
