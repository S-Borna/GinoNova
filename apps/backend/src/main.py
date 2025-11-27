from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.settings import settings
from .core.logging import configure_logging
from .api.router import api_router

configure_logging()
app = FastAPI(title="saas-backend", version=settings.PROJECT_VERSION)

# Parse origins - support comma-separated list or "*"
origins = settings.API_ORIGINS.split(",") if settings.API_ORIGINS != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

# REQUIRED BY Railway & PaaS health checks
@app.get("/.well-known/health")
def well_known_health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")


