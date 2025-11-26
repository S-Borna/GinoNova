from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/status")
def auth_status():
    return {"auth": "not-configured"}
