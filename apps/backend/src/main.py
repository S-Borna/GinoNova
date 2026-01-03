"""
DevOps Hub Backend — Main Application
=====================================

Clean architecture med enkel content-seeding.
All content kommer från: src/db/seeds/content/

Version: 2.0.0 - Linux 24/7 module
"""

from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.settings import settings
from .core.logging import configure_logging
from .api.router import api_router

configure_logging()
logger = logging.getLogger(__name__)


# =============================================================================
# CONTENT SEEDING — Enkel och ren
# =============================================================================


def _normalize_difficulty(difficulty: str) -> str:
    """
    Normalize difficulty values to valid Pydantic enum values.
    Maps invalid values like 'mixed' to valid ones.
    """
    valid_difficulties = ["beginner", "intermediate", "advanced", "expert"]
    difficulty_lower = difficulty.lower() if difficulty else "intermediate"
    
    # Map invalid values
    if difficulty_lower == "mixed":
        return "intermediate"
    if difficulty_lower == "easy":
        return "beginner"
    if difficulty_lower == "hard":
        return "advanced"
    
    # Return if valid, otherwise default to intermediate
    return difficulty_lower if difficulty_lower in valid_difficulties else "intermediate"


def seed_content():
    """
    Seed content från content/ — ENDA källan till moduler/tasks.

    Denna funktion:
    1. Kollar om data redan finns
    2. Om inte, skapar tracks och moduler från content/
    3. Loggar vad som hände
    """
    from .db.module_repository import create_module, list_modules
    from .db.task_repository import create_task
    from .db.track_repository import create_track, list_tracks
    from .db.lab_repository import create_lab
    from .db.project_repository import create_project
    from .schemas.module import ModuleCreate
    from .schemas.task import TaskCreate
    from .schemas.track import TrackCreate
    from .schemas.lab import LabCreate
    from .schemas.project import ProjectCreate

    # Import från NYA content-strukturen
    from .db.seeds.content import (
        get_all_modules,
        get_tracks,
        get_bootcamp_summary,
    )

    # Kolla om vi redan har data
    existing_modules = list_modules()
    summary = get_bootcamp_summary()

    if existing_modules:
        logger.info(f"✅ Content already loaded: {len(existing_modules)} modules")
        return

    # Kolla om det finns content att seeda
    modules_to_seed = get_all_modules()
    if not modules_to_seed:
        logger.info("📭 No content to seed — content/ is empty (this is fine!)")
        return

    logger.info(f"🌱 Seeding content: {len(modules_to_seed)} modules...")

    # Skapa tracks först
    track_id_map: dict[str, any] = {}
    for track_data in get_tracks():
        track = create_track(
            TrackCreate(
                name=track_data["name"],
                slug=track_data["slug"],
                description=track_data["description"],
                color=track_data["color"],
                icon=track_data["icon"],
                order_index=track_data["order_index"],
            )
        )
        track_id_map[track_data["slug"]] = track.id

    # Skapa moduler och tasks
    modules_created = 0
    tasks_created = 0
    labs_created = 0
    projects_created = 0

    for module_data in modules_to_seed:
        # Hämta track ID
        track_id = track_id_map.get(module_data.get("track_slug"))

        # Skapa modulen
        module_name = module_data.get("name") or module_data.get(
            "title", module_data["slug"]
        )
        module = create_module(
            ModuleCreate(
                track_id=track_id,
                name=module_name,
                slug=module_data["slug"],
                description=module_data.get("description"),
                order_index=module_data.get("order_index", modules_created + 1),
                difficulty=_normalize_difficulty(module_data.get("difficulty", "intermediate")),
                estimated_hours=module_data.get("estimated_hours", 10.0),
                prerequisites=module_data.get("prerequisites", []),
            )
        )
        modules_created += 1

        # Skapa tasks
        for idx, task_data in enumerate(module_data.get("tasks", [])):
            difficulty = task_data.get("difficulty", "medium")
            if difficulty not in ("easy", "medium", "hard"):
                difficulty = "medium"

            estimated_minutes = task_data.get("estimated_minutes") or {
                "easy": 15,
                "medium": 30,
                "hard": 45,
            }.get(difficulty, 30)
            xp_reward = task_data.get("xp_reward") or {
                "easy": 50,
                "medium": 100,
                "hard": 150,
            }.get(difficulty, 100)

            # Ensure order_index is always >= 1
            task_order_index = task_data.get("order_index")
            if task_order_index is None or task_order_index < 1:
                task_order_index = idx + 1
            
            create_task(
                TaskCreate(
                    module_id=module.id,
                    title=task_data["title"],
                    description=task_data.get("description"),
                    content=task_data.get("content"),
                    content_blocks=task_data.get("content_blocks"),
                    requirements=task_data.get("requirements"),
                    order_index=task_order_index,
                    difficulty=difficulty,
                    estimated_minutes=estimated_minutes,
                    xp_reward=xp_reward,
                )
            )
            tasks_created += 1

        # Skapa labs (om finns)
        for idx, lab_data in enumerate(module_data.get("labs", [])):
            create_lab(
                LabCreate(
                    module_id=module.id,
                    title=lab_data["title"],
                    slug=lab_data.get("slug", f"lab-{idx+1}"),
                    estimated_hours=lab_data.get("hours", 2.0),
                    order_index=idx + 1,
                    difficulty="medium",
                    xp_reward=int(lab_data.get("hours", 2.0) * 50),
                )
            )
            labs_created += 1

        # Skapa projekt (om finns)
        project_data = module_data.get("project")
        if project_data:
            create_project(
                ProjectCreate(
                    module_id=module.id,
                    title=project_data["title"],
                    slug=project_data.get("slug", "project"),
                    description=project_data.get("description"),
                    deliverables=project_data.get("deliverables", []),
                    xp_reward=project_data.get("xp_reward", 500),
                    estimated_hours=project_data.get("estimated_hours", 5.0),
                )
            )
            projects_created += 1

    logger.info(
        f"✅ Seeded: {modules_created} modules, {tasks_created} tasks, "
        f"{labs_created} labs, {projects_created} projects"
    )


# =============================================================================
# APPLICATION LIFESPAN
# =============================================================================


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: startup and shutdown events."""
    logger.info("🚀 Starting DevOps Hub Backend...")

    # Initialize PostgreSQL if configured
    from .db.database import is_db_configured, init_db

    if is_db_configured():
        logger.info("🗄️ PostgreSQL detected — initializing tables...")
        try:
            init_db()
            logger.info("✅ Database tables ready!")
        except Exception as e:
            logger.error(f"❌ Database init failed: {e}")
    else:
        logger.info("📝 Using in-memory storage (no DATABASE_URL)")

    # Initialize Redis if configured
    from .db.redis_client import is_redis_configured

    if is_redis_configured():
        logger.info("🔴 Redis connected!")
    else:
        logger.info("📝 Redis not configured — caching disabled")

    # Seed content
    seed_content()

    logger.info("✅ Backend ready!")

    yield  # App runs here

    logger.info("👋 Shutting down DevOps Hub Backend...")


# =============================================================================
# FASTAPI APPLICATION
# =============================================================================

app = FastAPI(
    title="DevOpsHub API",
    version=settings.PROJECT_VERSION,
    lifespan=lifespan,
    redirect_slashes=False,
)

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "https://ginonova.com",
    "https://www.ginonova.com",
    "https://saids-devopshub.netlify.app",
    "https://saasprojekt.netlify.app",
]

if settings.API_ORIGINS and settings.API_ORIGINS != "*":
    custom_origins = [o.strip() for o in settings.API_ORIGINS.split(",")]
    origins = list(set(origins + custom_origins))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex=r"https://.*\.netlify\.app",
)


# =============================================================================
# HEALTH CHECKS
# =============================================================================


@app.get("/health")
def health():
    """Detailed health check."""
    from .db.database import is_db_configured
    from .db.redis_client import is_redis_configured, get_redis_client
    from .db.module_repository import list_modules

    status = {
        "status": "ok",
        "postgresql": "disconnected",
        "redis": "disconnected",
        "modules_count": 0,
    }

    try:
        modules = list_modules()
        status["modules_count"] = len(modules)
    except Exception:
        pass

    if is_db_configured():
        status["postgresql"] = "connected"

    if is_redis_configured():
        try:
            client = get_redis_client()
            if client:
                client.ping()
                status["redis"] = "connected"
        except Exception:
            pass

    return status


@app.get("/.well-known/health")
def well_known_health():
    """PaaS health check endpoint."""
    return {"status": "ok"}


# =============================================================================
# API ROUTES
# =============================================================================

app.include_router(api_router, prefix="/api")
