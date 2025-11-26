from fastapi import APIRouter
from ..core.settings import settings

router = APIRouter()

@router.get("/version")
def version():
    return {"version": settings.PROJECT_VERSION}
