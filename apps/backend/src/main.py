from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.settings import settings
from .core.logging import configure_logging
from .api.router import api_router

# Import seeding functions
from .db.module_repository import list_modules
from .db.seeds.bootcamp_v3_data import get_bootcamp_summary

# Import ILE content for interactive tasks
from .db.seeds.ile_sample_content import SAMPLE_PERMISSIONS_TASK
from .db.seeds.module_01_linux_content import MODULE_01_TASKS

configure_logging()
logger = logging.getLogger(__name__)


def auto_seed_if_empty():
    """
    Automatically seed the database if it's empty.
    This ensures Bootcamp v3.0 content is always available after deploys.
    """
    # Import here to avoid circular imports
    from .db.module_repository import create_module, list_modules
    from .db.task_repository import create_task
    from .db.track_repository import create_track, list_tracks, get_track_by_slug
    from .db.lab_repository import create_lab
    from .db.project_repository import create_project
    from .db.seeds.bootcamp_v3_data import get_tracks, get_modules, get_bootcamp_summary
    from .schemas.module import ModuleCreate
    from .schemas.task import TaskCreate
    from .schemas.track import TrackCreate
    from .schemas.lab import LabCreate
    from .schemas.project import ProjectCreate

    # Check if we already have data
    existing_modules = list_modules()
    summary = get_bootcamp_summary()

    if len(existing_modules) >= summary["modules"]:
        logger.info(f"✅ Database already seeded: {len(existing_modules)} modules found")
        return

    logger.info("🌱 Auto-seeding Bootcamp v3.0 content...")

    # Track mapping for module creation
    track_id_map: dict[str, any] = {}

    # Create tracks
    tracks_created = 0
    for track_data in get_tracks():
        track = create_track(TrackCreate(
            name=track_data["name"],
            slug=track_data["slug"],
            description=track_data["description"],
            color=track_data["color"],
            icon=track_data["icon"],
            order_index=track_data["order_index"],
        ))
        track_id_map[track_data["slug"]] = track.id
        tracks_created += 1

    # Create modules, tasks, labs, and projects
    modules_created = 0
    tasks_created = 0
    labs_created = 0
    projects_created = 0

    for module_data in get_modules():
        # Get track ID
        track_id = track_id_map.get(module_data["track_slug"])

        # Create the module
        module = create_module(ModuleCreate(
            track_id=track_id,
            name=module_data["name"],
            slug=module_data["slug"],
            description=module_data.get("description"),
            order_index=module_data["order_index"],
            difficulty=module_data.get("difficulty", "intermediate"),
            estimated_hours=module_data.get("estimated_hours", 10.0),
            prerequisites=module_data.get("prerequisites", []),
        ))
        modules_created += 1

        # Create tasks for this module
        for idx, task_data in enumerate(module_data.get("tasks", [])):
            task_title = task_data["title"]

            # Check if we have ILE content for this task
            ile_content = None
            if task_title == "Understanding File Permissions" or "file permissions" in task_title.lower():
                ile_content = SAMPLE_PERMISSIONS_TASK
            elif task_title in MODULE_01_TASKS:
                ile_content = MODULE_01_TASKS[task_title]

            # Use ILE content if available, otherwise use original task data
            if ile_content:
                content_blocks = ile_content.get("content_blocks")
                requirements = ile_content.get("requirements")
                description = ile_content.get("description") or task_data.get("description")
                estimated_minutes = ile_content.get("estimated_minutes") or task_data.get("estimated_minutes")
                xp_reward = ile_content.get("xp_reward") or task_data.get("xp_reward")
            else:
                content_blocks = task_data.get("content_blocks")
                requirements = task_data.get("requirements")
                description = task_data.get("description")
                estimated_minutes = task_data.get("estimated_minutes")
                xp_reward = task_data.get("xp_reward")

            difficulty = task_data.get("difficulty", "medium")
            estimated_minutes = estimated_minutes or {"easy": 10, "medium": 15, "hard": 25}.get(difficulty, 15)
            xp_reward = xp_reward or {"easy": 20, "medium": 30, "hard": 50}.get(difficulty, 30)

            create_task(TaskCreate(
                module_id=module.id,
                title=task_title,
                description=description,
                content=task_data.get("content"),
                content_blocks=content_blocks,
                requirements=requirements,
                order_index=idx + 1,
                difficulty=difficulty,
                estimated_minutes=estimated_minutes,
                xp_reward=xp_reward,
            ))
            tasks_created += 1

        # Create labs for this module
        for idx, lab_data in enumerate(module_data.get("labs", [])):
            create_lab(LabCreate(
                module_id=module.id,
                title=lab_data["title"],
                slug=lab_data["slug"],
                estimated_hours=lab_data.get("hours", 2.0),
                order_index=idx + 1,
                difficulty="medium",
                xp_reward=int(lab_data.get("hours", 2.0) * 50),
            ))
            labs_created += 1

        # Create project for this module (if exists)
        project_data = module_data.get("project")
        if project_data:
            create_project(ProjectCreate(
                module_id=module.id,
                title=project_data["title"],
                slug=project_data["slug"],
                description=project_data.get("description"),
                deliverables=project_data.get("deliverables", []),
                xp_reward=project_data.get("xp_reward", 500),
                estimated_hours=project_data.get("estimated_hours", 5.0),
            ))
            projects_created += 1

    logger.info(
        f"✅ Seeded Bootcamp v3.0: {tracks_created} tracks, {modules_created} modules, "
        f"{tasks_created} tasks, {labs_created} labs, {projects_created} projects"
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: startup and shutdown events."""
    # Startup
    logger.info("🚀 Starting DevOps Hub Backend...")

    # Run database migrations if PostgreSQL is configured
    from .db.database import is_db_configured, init_db
    if is_db_configured():
        logger.info("🗄️ PostgreSQL detected - initializing tables...")
        try:
            init_db()
            logger.info("✅ Database tables ready!")
        except Exception as e:
            logger.error(f"❌ Database init failed: {e}")
    else:
        logger.info("📝 Using in-memory storage (no DATABASE_URL)")

    auto_seed_if_empty()
    logger.info("✅ Backend ready!")

    yield  # App runs here

    # Shutdown
    logger.info("👋 Shutting down DevOps Hub Backend...")


app = FastAPI(title="saas-backend", version=settings.PROJECT_VERSION, lifespan=lifespan)

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


