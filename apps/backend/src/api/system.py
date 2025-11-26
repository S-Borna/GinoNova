from fastapi import APIRouter
from pydantic import BaseModel
from ..core.settings import settings

class SystemInfo(BaseModel):
    service: str
    version: str

system_router = APIRouter()

@system_router.get("/info", response_model=SystemInfo)
def system_info():
    return SystemInfo(
        service="saas-backend",
        version=settings.PROJECT_VERSION
    )

@system_router.get("/health")
def system_health():
    return {"status": "ok"}

