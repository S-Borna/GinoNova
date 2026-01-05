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


def _normalize_task_difficulty(difficulty: str) -> str:
    """
    Normalize difficulty values for TaskCreate schema.
    TaskCreate uses: 'easy', 'medium', 'hard'
    Maps legacy values like 'beginner', 'intermediate', 'advanced', 'expert', 'mixed' to valid ones.
    """
    difficulty_lower = difficulty.lower() if difficulty else "medium"

    # Map to valid TaskCreate difficulty values: easy, medium, hard
    mapping = {
        "beginner": "easy",
        "easy": "easy",
        "intermediate": "medium",
        "medium": "medium",
        "mixed": "medium",
        "advanced": "hard",
        "hard": "hard",
        "expert": "hard",
    }

    return mapping.get(difficulty_lower, "medium")


def _normalize_module_difficulty(difficulty: str) -> str:
    """
    Normalize difficulty values for ModuleCreate schema.
    ModuleCreate uses: 'beginner', 'intermediate', 'advanced', 'expert'
    """
    difficulty_lower = difficulty.lower() if difficulty else "intermediate"

    valid_difficulties = ["beginner", "intermediate", "advanced", "expert"]

    # Map task-style difficulties to module-style
    mapping = {
        "easy": "beginner",
        "medium": "intermediate",
        "hard": "advanced",
        "mixed": "intermediate",
    }

    if difficulty_lower in valid_difficulties:
        return difficulty_lower
    return mapping.get(difficulty_lower, "intermediate")


def seed_content():
    """
    Seed content från content/ — ENDA källan till moduler/tasks.

    Denna funktion:
    1. Kollar om data redan finns
    2. Om inte, skapar tracks och moduler från content/
    3. Om data finns, uppdaterar tasks för hands-on modulen (idempotent update)
    4. Loggar vad som hände
    """
    from .db.module_repository import create_module, list_modules, get_module_by_slug
    from .db.task_repository import create_task, get_task_by_title_and_module, update_task, list_tasks_by_module
    from .db.track_repository import create_track, list_tracks, get_track_by_slug
    from .db.lab_repository import create_lab
    from .db.project_repository import create_project
    from .schemas.module import ModuleCreate, ModuleUpdate
    from .schemas.task import TaskCreate, TaskUpdate
    from .schemas.track import TrackCreate
    from .schemas.lab import LabCreate
    from .schemas.project import ProjectCreate

    # Import från NYA content-strukturen
    from .db.seeds.content import (
        get_all_modules,
        get_tracks,
        get_bootcamp_summary,
    )

    # Kolla om det finns content att seeda
    modules_to_seed = get_all_modules()
    if not modules_to_seed:
        logger.info("📭 No content to seed — content/ is empty (this is fine!)")
        return

    # Kolla om PostgreSQL är tillgängligt
    from .db.database import is_db_configured, get_db_context
    use_postgres = is_db_configured()
    
    # Hämta befintliga moduler (använd PostgreSQL om tillgängligt)
    if use_postgres:
        from .db import models
        with get_db_context() as db:
            existing_modules = db.query(models.Module).all()
            existing_tracks = db.query(models.Track).all()
    else:
        existing_modules = list_modules()
        existing_tracks = list_tracks()

    # Skapa/uppdatera tracks först
    track_id_map: dict[str, any] = {}
    for track_data in get_tracks():
        # Hitta befintlig track (använd PostgreSQL om tillgängligt)
        existing_track_id = None
        if use_postgres:
            with get_db_context() as db:
                existing_track = db.query(models.Track).filter(
                    models.Track.slug == track_data["slug"]
                ).first()
                if existing_track:
                    existing_track_id = existing_track.id  # Hämta ID inuti context
        elif existing_tracks:
            existing_track = get_track_by_slug(track_data["slug"])
            if existing_track:
                existing_track_id = existing_track.id
        
        if existing_track_id:
            track_id_map[track_data["slug"]] = existing_track_id
        else:
            # Skapa ny track (använd PostgreSQL om tillgängligt)
            if use_postgres:
                with get_db_context() as db:
                    new_track = models.Track(
                        name=track_data["name"],
                        slug=track_data["slug"],
                        description=track_data.get("description"),
                        color=track_data.get("color", "#6366f1"),
                        icon=track_data.get("icon", "📚"),
                        order_index=track_data.get("order_index", 1),
                    )
                    db.add(new_track)
                    db.commit()
                    db.refresh(new_track)
                    track_id_map[track_data["slug"]] = new_track.id
            else:
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

    # Om data redan finns, uppdatera bara hands-on modulen
    if existing_modules:
        logger.info(f"📝 Content exists: {len(existing_modules)} modules - checking for updates...")

        # Hitta hands-on modulen specifikt (använd PostgreSQL om tillgängligt)
        hands_on_module = None
        hands_on_module_id = None
        
        if use_postgres:
            # Hämta från PostgreSQL
            from .db import models
            with get_db_context() as db:
                db_module = db.query(models.Module).filter(
                    models.Module.slug == "hands-on-lab"
                ).first()
                if db_module:
                    hands_on_module_id = db_module.id
                    logger.info(f"✅ Found Hands-On Lab module in PostgreSQL: {db_module.id}")
        else:
            # Fallback till in-memory
            hands_on_module = get_module_by_slug("hands-on-lab")
            if hands_on_module:
                hands_on_module_id = hands_on_module.id
        
        if hands_on_module_id:
            # Hitta hands-on modulen i content
            hands_on_data = next((m for m in modules_to_seed if m.get("slug") == "hands-on-lab"), None)
            if hands_on_data:
                logger.info("🔄 Updating Hands-On Lab module tasks...")
                tasks_updated = 0
                tasks_created = 0
                
                if use_postgres:
                    # Använd PostgreSQL direkt
                    from .db import models
                    with get_db_context() as db:
                        for idx, task_data in enumerate(hands_on_data.get("tasks", [])):
                            # Hitta befintlig task i databasen
                            existing_task = db.query(models.Task).filter(
                                models.Task.module_id == hands_on_module_id,
                                models.Task.title.ilike(task_data["title"])
                            ).first()

                            # Normalisera difficulty
                            task_difficulty = _normalize_task_difficulty(task_data.get("difficulty", "medium"))

                            # Ensure order_index is always >= 1
                            task_order_index = task_data.get("order_index")
                            if task_order_index is None or task_order_index < 1:
                                task_order_index = idx + 1

                            estimated_minutes = task_data.get("estimated_minutes") or {
                                "easy": 15,
                                "medium": 30,
                                "hard": 45,
                            }.get(task_difficulty, 30)
                            xp_reward = task_data.get("xp_reward") or {
                                "easy": 50,
                                "medium": 100,
                                "hard": 150,
                            }.get(task_difficulty, 100)

                            if existing_task:
                                # Uppdatera befintlig task i databasen
                                existing_task.title = task_data["title"]
                                existing_task.description = task_data.get("description")
                                existing_task.content = task_data.get("content")  # VIKTIGT: Uppdatera content!
                                existing_task.content_blocks = task_data.get("content_blocks")
                                existing_task.requirements = task_data.get("requirements")
                                existing_task.order_index = task_order_index
                                existing_task.difficulty = task_difficulty
                                existing_task.estimated_minutes = estimated_minutes
                                existing_task.xp_reward = xp_reward
                                from datetime import datetime
                                existing_task.updated_at = datetime.utcnow()
                                tasks_updated += 1
                            else:
                                # Skapa ny task i databasen
                                new_task = models.Task(
                                    module_id=hands_on_module_id,
                                    title=task_data["title"],
                                    description=task_data.get("description"),
                                    content=task_data.get("content"),  # VIKTIGT: Sätt content!
                                    content_blocks=task_data.get("content_blocks"),
                                    requirements=task_data.get("requirements"),
                                    order_index=task_order_index,
                                    difficulty=task_difficulty,
                                    estimated_minutes=estimated_minutes,
                                    xp_reward=xp_reward,
                                )
                                db.add(new_task)
                                tasks_created += 1
                        db.commit()
                        logger.info(f"✅ Updated Hands-On Lab in PostgreSQL: {tasks_updated} tasks updated, {tasks_created} tasks created")
                else:
                    # Fallback till in-memory storage
                    for idx, task_data in enumerate(hands_on_data.get("tasks", [])):
                        # Hitta befintlig task
                        existing_task = get_task_by_title_and_module(task_data["title"], hands_on_module_id)

                        # Normalisera difficulty
                        task_difficulty = _normalize_task_difficulty(task_data.get("difficulty", "medium"))

                        # Ensure order_index is always >= 1
                        task_order_index = task_data.get("order_index")
                        if task_order_index is None or task_order_index < 1:
                            task_order_index = idx + 1

                        estimated_minutes = task_data.get("estimated_minutes") or {
                            "easy": 15,
                            "medium": 30,
                            "hard": 45,
                        }.get(task_difficulty, 30)
                        xp_reward = task_data.get("xp_reward") or {
                            "easy": 50,
                            "medium": 100,
                            "hard": 150,
                        }.get(task_difficulty, 100)

                        if existing_task:
                            # Uppdatera befintlig task
                            update_task(
                                existing_task.id,
                                TaskUpdate(
                                    title=task_data["title"],
                                    description=task_data.get("description"),
                                    content=task_data.get("content"),
                                    content_blocks=task_data.get("content_blocks"),
                                    requirements=task_data.get("requirements"),
                                    order_index=task_order_index,
                                    difficulty=task_difficulty,
                                    estimated_minutes=estimated_minutes,
                                    xp_reward=xp_reward,
                                )
                            )
                            tasks_updated += 1
                        else:
                            # Skapa ny task
                            create_task(
                                TaskCreate(
                                    module_id=hands_on_module_id,
                                    title=task_data["title"],
                                    description=task_data.get("description"),
                                    content=task_data.get("content"),
                                    content_blocks=task_data.get("content_blocks"),
                                    requirements=task_data.get("requirements"),
                                    order_index=task_order_index,
                                    difficulty=task_difficulty,
                                    estimated_minutes=estimated_minutes,
                                    xp_reward=xp_reward,
                                )
                            )
                            tasks_created += 1
                    logger.info(f"✅ Updated Hands-On Lab (in-memory): {tasks_updated} tasks updated, {tasks_created} tasks created")
                return
            else:
                logger.info("⚠️  Hands-On Lab module not found in content - skipping update")
                return
        else:
            logger.info("⚠️  Hands-On Lab module not found in database - will create on next full seed")
            return

    # Initial seeding - skapa allt från början
    logger.info(f"🌱 Seeding content: {len(modules_to_seed)} modules...")

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
                difficulty=_normalize_module_difficulty(module_data.get("difficulty", "intermediate")),
                estimated_hours=module_data.get("estimated_hours", 10.0),
                prerequisites=module_data.get("prerequisites", []),
            )
        )
        modules_created += 1

        # Skapa tasks
        for idx, task_data in enumerate(module_data.get("tasks", [])):
            task_difficulty = _normalize_task_difficulty(task_data.get("difficulty", "medium"))

            estimated_minutes = task_data.get("estimated_minutes") or {
                "easy": 15,
                "medium": 30,
                "hard": 45,
            }.get(task_difficulty, 30)
            xp_reward = task_data.get("xp_reward") or {
                "easy": 50,
                "medium": 100,
                "hard": 150,
            }.get(task_difficulty, 100)

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
                    difficulty=task_difficulty,
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

# Admin v2 routes
from .api.routes.admin_v2 import router as admin_v2_router
app.include_router(admin_v2_router, prefix="/api/admin-v2", tags=["admin-v2"])
