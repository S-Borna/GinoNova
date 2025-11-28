from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.settings import settings
from .core.logging import configure_logging
from .api.router import api_router

configure_logging()
app = FastAPI(title="saas-backend", version=settings.PROJECT_VERSION)

# CORS: Allow all origins in development, specific origins in production
# Note: allow_credentials=True requires specific origins, not "*"
default_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://saids-devopshub.netlify.app",
    "https://*.netlify.app",
]

# Parse custom origins from settings if provided
if settings.API_ORIGINS and settings.API_ORIGINS != "*":
    custom_origins = [o.strip() for o in settings.API_ORIGINS.split(",")]
    origins = list(set(default_origins + custom_origins))
else:
    origins = default_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex=r"https://.*\.netlify\.app",  # Allow all Netlify subdomains
)

@app.get("/health")
def health():
    return {"status": "ok"}

# REQUIRED BY Railway & PaaS health checks
@app.get("/.well-known/health")
def well_known_health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")


