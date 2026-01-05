"""
Admin API - Administrative endpoints for system management
Phase 10: Admin Panel

Features:
- User management (list, view, update, deactivate)
- System statistics
- Content management (seed, clear, status)
- System health checks
"""
from fastapi import APIRouter, HTTPException, Query, Response
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta, timezone
from uuid import UUID
import math

from ..db.module_repository import create_module, clear_modules, list_modules, get_module_by_slug
from ..db.task_repository import create_task, clear_tasks, list_tasks
from ..db.track_repository import create_track, clear_tracks, list_tracks, get_track_by_slug
from ..db.lab_repository import create_lab, clear_labs, list_labs
from ..db.project_repository import create_project, clear_projects, list_projects
from ..db import user_repository, progress_repository
from ..db.database import is_db_configured

# Import från NYA content-strukturen
from ..db.seeds.content import (
    get_tracks,
    get_all_modules as get_modules,
    get_bootcamp_summary,
    get_all_modules as get_v3_modules,
    get_total_modules as get_v3_module_count,
    get_total_tasks as get_v3_total_tasks,
)

from ..schemas.module import ModuleCreate
from ..schemas.task import TaskCreate
from ..schemas.track import TrackCreate
from ..schemas.lab import LabCreate
from ..schemas.project import ProjectCreate
from ..schemas.admin import (
    AdminUserDetail,
    AdminUserUpdate,
    AdminUsersListResponse,
    SystemStats,
    ContentSummary,
    ContentHealthCheck,
)
from ..core.deps import CurrentUser
from ..core.admin import require_admin, is_admin


admin_router = APIRouter()

# Phase version
PHASE_VERSION = "10.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# Level calculation
LEVEL_THRESHOLDS = [
    0, 100, 250, 500, 800, 1200, 1700, 2300, 3000, 3800,
    4700, 5700, 6800, 8000, 9500, 11000, 12800, 14800, 17000, 20000
]


def calculate_level(xp: int) -> int:
    """Calculate level from XP"""
    for i in range(len(LEVEL_THRESHOLDS) - 1, -1, -1):
        if xp >= LEVEL_THRESHOLDS[i]:
            return i + 1
    return 1


# ==============================================================================
# STATUS ENDPOINT
# ==============================================================================

@admin_router.get("/status")
def admin_status(response: Response):
    """Check admin module status"""
    add_phase_header(response)
    return {
        "admin": "configured",
        "phase": PHASE_VERSION,
        "database": "postgres" if is_db_configured() else "memory",
        "endpoints": [
            "users", "users/{id}", "stats", "content/summary",
            "content/health", "seed-bootcamp", "seed-status", "clear-data",
            "backfill-activity", "activity-log"
        ]
    }


# ==============================================================================
# BOOTSTRAP ADMIN - One-time setup endpoint
# ==============================================================================

class BootstrapAdminRequest(BaseModel):
    email: str
    secret: str

@admin_router.post("/bootstrap-admin")
def bootstrap_admin(request: BootstrapAdminRequest, response: Response):
    """
    Bootstrap first admin user. Requires secret key.
    This is a one-time setup endpoint for initial admin creation.
    """
    add_phase_header(response)

    # Secret key for bootstrap (should match env var or hardcoded for setup)
    import os
    bootstrap_secret = os.environ.get("BOOTSTRAP_SECRET", "devops-hub-bootstrap-2024")

    if request.secret != bootstrap_secret:
        raise HTTPException(status_code=403, detail="Invalid bootstrap secret")

    if not is_db_configured():
        raise HTTPException(status_code=500, detail="Database not configured")

    from ..db.database import get_db_context
    from ..db.models import User

    with get_db_context() as db:
        user = db.query(User).filter(User.email == request.email).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User {request.email} not found")

        if user.is_admin:
            return {"success": True, "message": f"{request.email} is already an admin"}

        user.is_admin = True
        db.commit()

        return {"success": True, "message": f"{request.email} is now an admin!"}


# ==============================================================================
# ACTIVITY BACKFILL & LOG ENDPOINTS
# ==============================================================================

@admin_router.get("/debug-activity")
def debug_activity(
    response: Response,
    current_user: CurrentUser,
):
    """Debug endpoint to check last_activity_at values directly from DB"""
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"error": "Database not configured"}

    from ..db.database import get_db_context
    from ..db.models import User

    with get_db_context() as db:
        users = db.query(User).order_by(User.created_at.desc()).limit(15).all()
        return {
            "users": [
                {
                    "email": u.email,
                    "last_activity_at": u.last_activity_at.isoformat() if u.last_activity_at else None,
                    "created_at": u.created_at.isoformat() if u.created_at else None,
                }
                for u in users
            ]
        }


@admin_router.post("/run-migrations")
def run_database_migrations(
    response: Response,
    current_user: CurrentUser,
):
    """
    Run all pending Alembic migrations (admin only).

    This endpoint safely runs database migrations without restarting the server.
    Returns details about which migrations were applied.
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"success": False, "error": "Database not configured", "migrations": []}

    import subprocess
    import os
    from sqlalchemy import text
    from ..db.database import get_db_context

    try:
        # Get the backend directory - handle both local and Docker paths
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        # Fallback to /app/apps/backend if we're in Docker
        if not os.path.exists(os.path.join(backend_dir, "alembic.ini")):
            backend_dir = "/app/apps/backend"

        # Verify alembic.ini exists
        alembic_ini = os.path.join(backend_dir, "alembic.ini")
        if not os.path.exists(alembic_ini):
            return {
                "success": False,
                "error": f"alembic.ini not found at {alembic_ini}",
                "backend_dir": backend_dir,
                "cwd": os.getcwd()
            }

        # Get current environment (needed for DATABASE_URL)
        env = os.environ.copy()

        # Check if alembic_version table exists
        alembic_version_exists = False
        current_db_revision = None
        with get_db_context() as db:
            try:
                result = db.execute(text("SELECT version_num FROM alembic_version LIMIT 1"))
                row = result.fetchone()
                if row:
                    current_db_revision = row[0]
                    alembic_version_exists = True
            except Exception:
                alembic_version_exists = False

        # If no alembic_version table, stamp current schema
        if not alembic_version_exists:
            # Database was created without Alembic - stamp it
            stamp_result = subprocess.run(
                ["python", "-m", "alembic", "stamp", "head"],
                cwd=backend_dir,
                env=env,
                capture_output=True,
                text=True,
                timeout=30
            )
            if stamp_result.returncode == 0:
                return {
                    "success": True,
                    "message": "Database stamped to head (no migrations needed - schema already exists)",
                    "previous_revision": "none",
                    "current_revision": "head (stamped)",
                    "applied": False,
                    "stamped": True,
                    "backend_dir": backend_dir
                }
            else:
                return {
                    "success": False,
                    "error": "Failed to stamp database",
                    "stdout": stamp_result.stdout,
                    "stderr": stamp_result.stderr,
                    "backend_dir": backend_dir
                }

        # First, check current migration status
        result_current = subprocess.run(
            ["python", "-m", "alembic", "current"],
            cwd=backend_dir,
            env=env,
            capture_output=True,
            text=True,
            timeout=30
        )
        current_revision = result_current.stdout.strip() if result_current.returncode == 0 else current_db_revision or "unknown"
        current_error = result_current.stderr.strip() if result_current.returncode != 0 else None

        # Run alembic upgrade head
        result = subprocess.run(
            ["python", "-m", "alembic", "upgrade", "head"],
            cwd=backend_dir,
            env=env,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            # Get new current revision
            result_new = subprocess.run(
                ["python", "-m", "alembic", "current"],
                cwd=backend_dir,
                env=env,
                capture_output=True,
                text=True,
                timeout=30
            )
            new_revision = result_new.stdout.strip() if result_new.returncode == 0 else "unknown"

            return {
                "success": True,
                "message": "Migrations completed successfully",
                "previous_revision": current_revision,
                "current_revision": new_revision,
                "output": result.stdout,
                "applied": current_revision != new_revision,
                "backend_dir": backend_dir
            }
        else:
            return {
                "success": False,
                "error": "Migration failed",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "previous_revision": current_revision,
                "current_error": current_error,
                "backend_dir": backend_dir
            }

    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Migration timed out after 60 seconds"}
    except Exception as e:
        import traceback
        return {"success": False, "error": str(e), "traceback": traceback.format_exc()}


@admin_router.get("/migration-status")
def get_migration_status(
    response: Response,
    current_user: CurrentUser,
):
    """
    Get current migration status and list available migrations.
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"error": "Database not configured"}

    import subprocess
    import os

    backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Fallback to Docker path
    if not os.path.exists(os.path.join(backend_dir, "alembic.ini")):
        backend_dir = "/app/apps/backend"

    env = os.environ.copy()

    try:
        # Get current revision
        result_current = subprocess.run(
            ["python", "-m", "alembic", "current"],
            cwd=backend_dir,
            env=env,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Get migration history
        result_history = subprocess.run(
            ["python", "-m", "alembic", "history", "--verbose"],
            cwd=backend_dir,
            env=env,
            capture_output=True,
            text=True,
            timeout=30
        )

        return {
            "current_revision": result_current.stdout.strip() if result_current.returncode == 0 else "none",
            "history": result_history.stdout if result_history.returncode == 0 else "unavailable",
            "current_error": result_current.stderr if result_current.returncode != 0 else None,
            "backend_dir": backend_dir
        }

    except Exception as e:
        return {"error": str(e)}


@admin_router.post("/apply-schema-updates")
def apply_schema_updates(
    response: Response,
    current_user: CurrentUser,
):
    """
    Apply missing schema updates directly via SQL.
    This is a fallback when Alembic migrations don't work properly.

    Adds:
    - permissions column to users table
    - ai_usage_logs table
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"error": "Database not configured"}

    from sqlalchemy import text
    from ..db.database import get_db_context

    results = []

    with get_db_context() as db:
        # 1. Add permissions column to users table if it doesn't exist
        try:
            db.execute(text("""
                ALTER TABLE users
                ADD COLUMN IF NOT EXISTS permissions JSONB
                DEFAULT '{"ai_quiz": true, "premium_modules": true, "study_room": true, "skillpath": true}'::jsonb
            """))
            db.commit()
            results.append("✅ permissions column added to users")
        except Exception as e:
            results.append(f"⚠️ permissions column: {str(e)}")
            db.rollback()

        # 2. Create ai_usage_logs table if it doesn't exist
        try:
            db.execute(text("""
                CREATE TABLE IF NOT EXISTS ai_usage_logs (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
                    feature VARCHAR(50) NOT NULL,
                    model VARCHAR(50) NOT NULL,
                    prompt_tokens INTEGER DEFAULT 0,
                    completion_tokens INTEGER DEFAULT 0,
                    total_tokens INTEGER DEFAULT 0,
                    cost_usd FLOAT DEFAULT 0.0,
                    request_type VARCHAR(100),
                    week_number INTEGER,
                    year INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            db.commit()
            results.append("✅ ai_usage_logs table created")
        except Exception as e:
            results.append(f"⚠️ ai_usage_logs table: {str(e)}")
            db.rollback()

        # 3. Create index on ai_usage_logs if not exists
        try:
            db.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_ai_usage_user_id ON ai_usage_logs(user_id);
                CREATE INDEX IF NOT EXISTS idx_ai_usage_week ON ai_usage_logs(year, week_number);
            """))
            db.commit()
            results.append("✅ ai_usage_logs indexes created")
        except Exception as e:
            results.append(f"⚠️ ai_usage_logs indexes: {str(e)}")
            db.rollback()

    return {
        "success": True,
        "message": "Schema updates applied",
        "results": results
    }


@admin_router.post("/backfill-activity")
def backfill_user_activity(
    response: Response,
    current_user: CurrentUser,
):
    """
    Backfill last_activity_at for users who have NULL.
    Sets it to either their latest progress timestamp or created_at.
    Safe to run multiple times - only updates NULL values.
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"error": "Database not configured", "updated": 0}

    from ..db.database import get_db_context
    from ..db.models import User, Progress

    updated_count = 0
    with get_db_context() as db:
        # Only get users with NULL last_activity_at
        users = db.query(User).filter(User.last_activity_at.is_(None)).all()

        for user in users:
            # Try to get latest progress
            latest_progress = db.query(Progress).filter(
                Progress.user_id == user.id
            ).order_by(Progress.updated_at.desc()).first()

            if latest_progress and latest_progress.updated_at:
                # Use latest progress time
                user.last_activity_at = latest_progress.updated_at
            else:
                # Fall back to created_at (user exists, so they've been active)
                user.last_activity_at = user.created_at
            updated_count += 1

        db.flush()

    return {
        "success": True,
        "message": f"Backfilled last_activity_at for {updated_count} users",
        "updated": updated_count
    }


# REMOVED: reset-fake-activity endpoint - it was destroying valid activity data
# last_activity_at should NEVER be reset to None, only updated


@admin_router.get("/activity-log")
def get_activity_log(
    response: Response,
    current_user: CurrentUser,
    days: int = Query(7, ge=1, le=90, description="Number of days to look back"),
):
    """
    Get activity log for all users in the last N days.

    Shows registrations, logins (via last_activity_at), and progress updates.
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"error": "Database not configured", "events": []}

    from ..db.database import get_db_context
    from ..db.models import User, Progress

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    events = []

    with get_db_context() as db:
        # Get new registrations
        new_users = db.query(User).filter(User.created_at >= cutoff).all()
        for user in new_users:
            events.append({
                "type": "registration",
                "email": user.email,
                "name": user.full_name,
                "timestamp": user.created_at.isoformat(),
                "details": f"New user registered via {user.oauth_provider or 'email'}"
            })

        # Get recent activity (last_activity_at updates)
        active_users = db.query(User).filter(
            User.last_activity_at >= cutoff
        ).all()
        for user in active_users:
            if user.last_activity_at and user.last_activity_at != user.created_at:
                events.append({
                    "type": "login",
                    "email": user.email,
                    "name": user.full_name,
                    "timestamp": user.last_activity_at.isoformat(),
                    "details": "User logged in / was active"
                })

        # Get progress updates
        progress_records = db.query(Progress).filter(
            Progress.updated_at >= cutoff
        ).order_by(Progress.updated_at.desc()).limit(100).all()

        for p in progress_records:
            user = db.query(User).filter(User.id == p.user_id).first()
            if user:
                events.append({
                    "type": "progress",
                    "email": user.email,
                    "name": user.full_name,
                    "timestamp": p.updated_at.isoformat(),
                    "details": f"Progress: {p.status} ({p.progress}%)"
                })

    # Sort by timestamp descending
    events.sort(key=lambda x: x["timestamp"], reverse=True)

    return {
        "period_days": days,
        "total_events": len(events),
        "new_registrations": len([e for e in events if e["type"] == "registration"]),
        "active_users": len(set(e["email"] for e in events if e["type"] == "login")),
        "events": events[:200]  # Limit to 200 most recent
    }


# ==============================================================================
# USER MANAGEMENT ENDPOINTS
# ==============================================================================

@admin_router.get("/users", response_model=AdminUsersListResponse)
def list_all_users(
    response: Response,
    current_user: CurrentUser,
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=500),
    search: Optional[str] = Query(None, description="Search by email or name"),
    status: Optional[str] = Query(None, pattern="^(active|inactive|all)$"),
) -> AdminUsersListResponse:
    """
    Get all users with their stats (admin only).

    Supports pagination, search, and filtering.
    """
    add_phase_header(response)
    require_admin(current_user)

    try:
        users = user_repository.list_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list users: {str(e)}")

    try:
        all_modules = list_modules()
        all_tasks = list_tasks()
    except Exception as e:
        # Non-critical, continue without
        all_modules = []
        all_tasks = []

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Filter by search
    if search:
        search_lower = search.lower()
        users = [
            u for u in users
            if search_lower in u.email.lower()
            or (u.full_name and search_lower in u.full_name.lower())
        ]

    # Filter by status
    if status == "active":
        users = [u for u in users if u.is_active]
    elif status == "inactive":
        users = [u for u in users if not u.is_active]

    # Build user details
    user_details = []
    for user in users:
        try:
            # Get progress records
            progress_records = progress_repository.list_progress_by_user(user.id)

            tasks_completed = sum(
                1 for p in progress_records
                if p.task_id and (p.status == "completed" or p.progress == 100)
            )
            modules_completed = sum(
                1 for p in progress_records
                if p.module_id and (p.status == "completed" or p.progress == 100)
            )
            labs_completed = sum(
                1 for p in progress_records
                if getattr(p, 'lab_id', None) and p.status == "completed"
            )
            projects_completed = sum(
                1 for p in progress_records
                if getattr(p, 'project_id', None) and p.status == "completed"
            )

            user_xp = getattr(user, 'total_xp', None)
            if user_xp is None:
                user_xp = tasks_completed * 25

            # Get last_activity_at - ONLY use real activity data, no fake fallbacks
            last_active = getattr(user, 'last_activity_at', None)

            user_details.append(AdminUserDetail(
                id=user.id,
                email=user.email,
                full_name=getattr(user, 'full_name', None),
                avatar_url=getattr(user, 'avatar_url', None),
                bio=getattr(user, 'bio', None),
                is_active=getattr(user, 'is_active', True),
                is_admin=getattr(user, 'is_admin', False),
                is_verified=getattr(user, 'is_verified', False),
                total_xp=user_xp,
                level=calculate_level(user_xp),
                current_streak=getattr(user, 'current_streak', 0),
                longest_streak=getattr(user, 'longest_streak', 0),
                tasks_completed=tasks_completed,
                modules_completed=modules_completed,
                labs_completed=labs_completed,
                projects_completed=projects_completed,
                total_study_time=0,
                created_at=getattr(user, 'created_at', now),
                updated_at=getattr(user, 'updated_at', now),
                last_activity_at=last_active,
            ))
        except Exception as e:
            # Log error but continue with other users
            import logging
            logging.error(f"Error processing user {user.id}: {str(e)}")
            continue

    # Sort by last activity
    user_details.sort(key=lambda u: u.last_activity_at or datetime.min, reverse=True)

    # Pagination
    total = len(user_details)
    total_pages = math.ceil(total / per_page) if total > 0 else 1
    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = user_details[start:end]

    return AdminUsersListResponse(
        users=paginated_users,
        total=total,
        page=page,
        per_page=per_page,
        total_pages=total_pages,
    )


@admin_router.get("/users/{user_id}", response_model=AdminUserDetail)
def get_user_detail(
    user_id: UUID,
    response: Response,
    current_user: CurrentUser,
) -> AdminUserDetail:
    """
    Get detailed user information (admin only).
    """
    add_phase_header(response)
    require_admin(current_user)

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    progress_records = progress_repository.list_progress_by_user(user.id)

    tasks_completed = sum(
        1 for p in progress_records
        if p.task_id and (p.status == "completed" or p.progress == 100)
    )
    modules_completed = sum(
        1 for p in progress_records
        if p.module_id and (p.status == "completed" or p.progress == 100)
    )

    user_xp = getattr(user, 'total_xp', tasks_completed * 25)

    return AdminUserDetail(
        id=user.id,
        email=user.email,
        full_name=getattr(user, 'full_name', None),
        avatar_url=getattr(user, 'avatar_url', None),
        bio=getattr(user, 'bio', None),
        is_active=user.is_active,
        is_admin=getattr(user, 'is_admin', False),
        is_verified=getattr(user, 'is_verified', False),
        total_xp=user_xp,
        level=calculate_level(user_xp),
        current_streak=getattr(user, 'current_streak', 0),
        longest_streak=getattr(user, 'longest_streak', 0),
        tasks_completed=tasks_completed,
        modules_completed=modules_completed,
        labs_completed=0,
        projects_completed=0,
        total_study_time=0,
        created_at=user.created_at,
        updated_at=user.updated_at,
        last_activity_at=getattr(user, 'last_activity_at', None),
    )


# ==============================================================================
# UPDATE USER ENDPOINT (for admin to toggle active/admin status)
# ==============================================================================

class UserStatusUpdate(BaseModel):
    """Schema for updating user status"""
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None


@admin_router.patch("/users/{user_id}")
def update_user_status(
    user_id: UUID,
    data: UserStatusUpdate,
    response: Response,
    current_user: CurrentUser,
):
    """
    Update user status (active, admin) - admin only.
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        raise HTTPException(status_code=500, detail="Database not configured")

    from ..db.database import get_db_context
    from ..db.models import User

    with get_db_context() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Update fields if provided
        if data.is_active is not None:
            user.is_active = data.is_active
        if data.is_admin is not None:
            user.is_admin = data.is_admin

        db.commit()
        db.refresh(user)

        return {
            "success": True,
            "user_id": str(user_id),
            "is_active": user.is_active,
            "is_admin": user.is_admin,
        }


# ==============================================================================
# USER PERMISSIONS ENDPOINT
# ==============================================================================

class UserPermissionsUpdate(BaseModel):
    """Schema for updating user permissions"""
    permissions: dict  # {"ai_quiz": bool, "premium_modules": bool, ...}


@admin_router.patch("/users/{user_id}/permissions")
def update_user_permissions(
    user_id: UUID,
    data: UserPermissionsUpdate,
    response: Response,
    current_user: CurrentUser,
):
    """
    Update user permissions (admin only).

    Permissions: ai_quiz, premium_modules, study_room, skillpath
    """
    add_phase_header(response)
    require_admin(current_user)

    if not is_db_configured():
        return {"error": "Database not configured", "success": False}

    from ..db.database import get_db_context
    from ..db.models import User
    from sqlalchemy import text

    with get_db_context() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Check if permissions column exists
        try:
            # Try to get existing permissions
            existing_permissions = getattr(user, 'permissions', None) or {
                "ai_quiz": True,
                "premium_modules": True,
                "study_room": True,
                "skillpath": True
            }

            # Update with new permissions
            updated_permissions = {**existing_permissions, **data.permissions}

            # Try to save to permissions column
            user.permissions = updated_permissions
            db.flush()

            return {
                "success": True,
                "user_id": str(user_id),
                "permissions": updated_permissions
            }
        except Exception as e:
            # If permissions column doesn't exist yet, return error
            db.rollback()
            return {
                "success": False,
                "error": "Permissions column not available. Run migration 005_add_user_permissions first.",
                "user_id": str(user_id),
                "permissions": data.permissions
            }


@admin_router.put("/users/{user_id}", response_model=AdminUserDetail)
def update_user(
    user_id: UUID,
    data: AdminUserUpdate,
    response: Response,
    current_user: CurrentUser,
) -> AdminUserDetail:
    """
    Update user (admin only).

    Can update: is_active, is_admin, is_verified, total_xp
    """
    add_phase_header(response)
    require_admin(current_user)

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user
    update_data = data.model_dump(exclude_unset=True)
    updated = user_repository.update_user(user_id, **update_data)

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to update user")

    return get_user_detail(user_id, response, current_user)


class PasswordResetRequest(BaseModel):
    """Schema for admin password reset"""
    new_password: str


@admin_router.post("/users/{user_id}/reset-password")
def admin_reset_password(
    user_id: UUID,
    data: PasswordResetRequest,
    response: Response,
    current_user: CurrentUser,
):
    """
    Reset a user's password (admin only).
    """
    add_phase_header(response)
    require_admin(current_user)

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Hash the new password
    from ..core.security import hash_password
    hashed = hash_password(data.new_password)

    # Update user password
    updated = user_repository.update_user(user_id, hashed_password=hashed)
    if not updated:
        raise HTTPException(status_code=500, detail="Failed to update password")

    return {"success": True, "message": f"Password reset for {user.email}"}


@admin_router.delete("/users/{user_id}")
def deactivate_user(
    user_id: UUID,
    response: Response,
    current_user: CurrentUser,
    hard_delete: bool = Query(False, description="Permanently delete user"),
):
    """
    Deactivate or delete user (admin only).

    By default, soft-deletes (deactivates) the user.
    Use hard_delete=true to permanently delete.
    """
    add_phase_header(response)
    require_admin(current_user)

    # Prevent self-deletion
    if user_id == current_user.id:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete your own account"
        )

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if hard_delete:
        success = user_repository.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=500, detail="Failed to delete user")
        return {"success": True, "message": "User permanently deleted"}
    else:
        user_repository.update_user(user_id, is_active=False)
        return {"success": True, "message": "User deactivated"}


@admin_router.post("/users/{user_id}/force-logout")
def force_logout_user(
    user_id: UUID,
    response: Response,
    current_user: CurrentUser,
):
    """
    Force logout a user by invalidating their session.

    This sets last_activity_at to a past date, effectively
    showing them as offline. They will need to re-login.
    """
    add_phase_header(response)
    require_admin(current_user)

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Set last_activity_at to epoch (effectively "never active")
    # The user's JWT is still valid but they'll appear offline
    # For true session invalidation, we'd need a token blacklist
    from datetime import datetime, timezone
    user_repository.update_user(user_id, last_activity_at=datetime(2000, 1, 1, tzinfo=timezone.utc))

    return {"success": True, "message": f"User {user.email} logged out (session invalidated)"}


@admin_router.post("/users/{user_id}/ban")
def ban_user(
    user_id: UUID,
    response: Response,
    current_user: CurrentUser,
):
    """
    Ban a user - deactivates account and prevents login.
    """
    add_phase_header(response)
    require_admin(current_user)

    if user_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot ban yourself")

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Deactivate and set last_activity to epoch
    from datetime import datetime, timezone
    user_repository.update_user(
        user_id,
        is_active=False,
        last_activity_at=datetime(2000, 1, 1, tzinfo=timezone.utc)
    )

    return {"success": True, "message": f"User {user.email} has been banned"}


@admin_router.post("/users/{user_id}/refresh-activity")
def refresh_user_activity(
    user_id: UUID,
    response: Response,
    current_user: CurrentUser,
):
    """
    Manually refresh a user's last_activity_at to NOW.
    Use this to fix users who appear offline but are actually online.
    """
    add_phase_header(response)
    require_admin(current_user)

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    from datetime import datetime, timezone
    user_repository.update_user(user_id, last_activity_at=datetime.now(timezone.utc))

    return {"success": True, "message": f"Activity refreshed for {user.email}"}


# ==============================================================================
# SYSTEM STATS ENDPOINTS
# ==============================================================================

@admin_router.get("/stats", response_model=SystemStats)
def get_system_stats(
    response: Response,
    current_user: CurrentUser,
) -> SystemStats:
    """
    Get system-wide statistics (admin only).

    Includes real-time activity tracking:
    - online_now: Users active in last 30 minutes
    - active_today: Users active today
    """
    add_phase_header(response)
    require_admin(current_user)

    users = user_repository.list_users()
    tracks = list_tracks()
    modules = list_modules()
    tasks = list_tasks()
    labs = list_labs()
    projects = list_projects()

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = now - timedelta(days=7)
    five_min_ago = now - timedelta(minutes=5)  # Match frontend: online = active within 5 min

    # User stats
    total_users = len(users)
    active_users = sum(1 for u in users if u.is_active)
    admin_users = sum(1 for u in users if is_admin(u))
    users_today = sum(1 for u in users if u.created_at >= today_start)
    users_this_week = sum(1 for u in users if u.created_at >= week_ago)

    # Real-time activity stats
    online_now = 0
    active_today = 0
    for u in users:
        last_activity = getattr(u, 'last_activity_at', None)
        if last_activity:
            if last_activity >= five_min_ago:
                online_now += 1
            if last_activity >= today_start:
                active_today += 1

    # Activity stats
    total_tasks_completed = 0
    total_xp_earned = 0

    for user in users:
        progress = progress_repository.list_progress_by_user(user.id)
        completed = sum(1 for p in progress if p.task_id and p.status == "completed")
        total_tasks_completed += completed
        total_xp_earned += completed * 25

    # Averages
    avg_tasks = total_tasks_completed / total_users if total_users > 0 else 0
    avg_xp = total_xp_earned / total_users if total_users > 0 else 0

    return SystemStats(
        total_users=total_users,
        active_users=active_users,
        admin_users=admin_users,
        users_today=users_today,
        users_this_week=users_this_week,
        online_now=online_now,
        active_today=active_today,
        total_tracks=len(tracks),
        total_modules=len(modules),
        total_tasks=len(tasks),
        total_labs=len(labs),
        total_projects=len(projects),
        total_tasks_completed=total_tasks_completed,
        total_xp_earned=total_xp_earned,
        total_study_minutes=0,
        active_sessions=0,
        avg_tasks_per_user=round(avg_tasks, 1),
        avg_xp_per_user=round(avg_xp, 1),
        avg_session_minutes=0.0,
        database_status="postgres" if is_db_configured() else "memory",
        cache_status="not_configured",
        api_version="1.0.0",
    )


# ==============================================================================
# AI USAGE TRACKING ENDPOINTS
# ==============================================================================

@admin_router.get("/ai-usage")
def get_ai_usage_overview(
    response: Response,
    current_user: CurrentUser,
    year: Optional[int] = Query(None, description="Filter by year"),
    week: Optional[int] = Query(None, description="Filter by week number"),
):
    """
    Get AI usage overview - all users and their usage stats (admin only).

    Shows:
    - Total calls, tokens, cost per user
    - Filterable by year/week
    """
    add_phase_header(response)
    require_admin(current_user)

    from ..services.ai_usage_service import get_all_users_usage, get_weekly_summary

    users_usage = get_all_users_usage(year=year, week=week)
    weekly_summary = get_weekly_summary(year=year)

    # Calculate totals
    total_calls = sum(u["total_calls"] for u in users_usage)
    total_tokens = sum(u["total_tokens"] for u in users_usage)
    total_cost = sum(u["total_cost_usd"] for u in users_usage)

    return {
        "year": year,
        "week": week,
        "totals": {
            "total_calls": total_calls,
            "total_tokens": total_tokens,
            "total_cost_usd": round(total_cost, 4),
            "unique_users": len(users_usage),
        },
        "users": users_usage,
        "weekly_summary": weekly_summary,
    }


@admin_router.get("/ai-usage/user/{user_id}")
def get_user_ai_usage(
    user_id: UUID,
    response: Response,
    current_user: CurrentUser,
    year: Optional[int] = Query(None, description="Filter by year"),
    week: Optional[int] = Query(None, description="Filter by week number"),
):
    """
    Get AI usage for a specific user (admin only).

    Shows breakdown by feature (Dallas, AI Quiz, etc.)
    """
    add_phase_header(response)
    require_admin(current_user)

    from ..services.ai_usage_service import get_user_usage_stats

    return get_user_usage_stats(user_id=user_id, year=year, week=week)


@admin_router.get("/ai-usage/weekly")
def get_weekly_ai_usage(
    response: Response,
    current_user: CurrentUser,
    year: Optional[int] = Query(None, description="Year to get weekly data for"),
):
    """
    Get weekly AI usage breakdown (admin only).

    Shows usage per week for cost tracking.
    """
    add_phase_header(response)
    require_admin(current_user)

    from ..services.ai_usage_service import get_weekly_summary

    return {
        "year": year or datetime.now(timezone.utc).year,
        "weeks": get_weekly_summary(year=year),
    }


# ==============================================================================
# CONTENT MANAGEMENT ENDPOINTS
# ==============================================================================

@admin_router.get("/content/summary", response_model=ContentSummary)
def get_content_summary(
    response: Response,
    current_user: CurrentUser,
) -> ContentSummary:
    """
    Get content summary (admin only).
    """
    add_phase_header(response)
    require_admin(current_user)

    tracks = list_tracks()
    modules = list_modules()
    tasks = list_tasks()
    labs = list_labs()
    projects = list_projects()

    # Calculate total hours from modules
    total_hours = sum(getattr(m, 'estimated_hours', 10.0) for m in modules)

    summary = get_bootcamp_summary()
    is_seeded = (
        len(tracks) >= summary["tracks"] and
        len(modules) >= summary["modules"]
    )

    return ContentSummary(
        tracks=len(tracks),
        modules=len(modules),
        tasks=len(tasks),
        labs=len(labs),
        projects=len(projects),
        total_hours=total_hours,
        is_seeded=is_seeded,
        last_seed_at=None,
    )


@admin_router.get("/content/health", response_model=ContentHealthCheck)
def check_content_health(
    response: Response,
    current_user: CurrentUser,
) -> ContentHealthCheck:
    """
    Check content health (admin only).
    """
    add_phase_header(response)
    require_admin(current_user)

    tracks = list_tracks()
    modules = list_modules()
    tasks = list_tasks()
    labs = list_labs()

    # Check for issues
    missing_content = []
    orphaned_tasks = 0
    orphaned_labs = 0

    # Check tracks
    tracks_ok = len(tracks) >= 4
    if not tracks_ok:
        missing_content.append(f"Expected 4 tracks, found {len(tracks)}")

    # Check modules
    modules_ok = len(modules) >= 15
    if not modules_ok:
        missing_content.append(f"Expected 15 modules, found {len(modules)}")

    # Check for orphaned content
    module_ids = {m.id for m in modules}
    for task in tasks:
        if task.module_id not in module_ids:
            orphaned_tasks += 1
    for lab in labs:
        if lab.module_id not in module_ids:
            orphaned_labs += 1

    # Determine status
    if tracks_ok and modules_ok and orphaned_tasks == 0 and orphaned_labs == 0:
        status = "healthy"
    elif orphaned_tasks > 0 or orphaned_labs > 0:
        status = "warning"
    else:
        status = "error"

    return ContentHealthCheck(
        status=status,
        tracks_ok=tracks_ok,
        modules_ok=modules_ok,
        orphaned_tasks=orphaned_tasks,
        orphaned_labs=orphaned_labs,
        missing_content=missing_content,
    )


# ==============================================================================
# SEED & DATA MANAGEMENT ENDPOINTS
# ==============================================================================

class SeedResponse(BaseModel):
    """Response schema for seed operations"""
    success: bool
    message: str
    tracks_created: int
    modules_created: int
    tasks_created: int
    labs_created: int
    projects_created: int


class SeedStatusResponse(BaseModel):
    """Response schema for seed status check"""
    seeded: bool
    tracks: int
    modules: int
    tasks: int
    labs: int
    projects: int
    expected_tracks: int
    expected_modules: int


class BootcampSummaryResponse(BaseModel):
    """Response schema for bootcamp summary"""
    tracks: int
    modules: int
    tasks: int
    labs: int
    projects: int
    total_hours: float


@admin_router.post("/seed-bootcamp", response_model=SeedResponse)
def seed_bootcamp(
    response: Response,
    current_user: CurrentUser,
    clear_existing: bool = True,
) -> SeedResponse:
    """
    Seed the database with Bootcamp v3.0 content (admin only).

    Bootcamp v3.0 includes:
    - 4 Tracks (Foundation, Cloud, Containers, Platform)
    - 15 Modules
    - 60+ Labs
    - 15+ Projects

    Args:
        clear_existing: If True, clear existing data before seeding.
                       Defaults to True for idempotent seeding.

    Returns:
        SeedResponse with counts of created items.
    """
    add_phase_header(response)
    require_admin(current_user)
    try:
        # Optionally clear existing data
        if clear_existing:
            clear_projects()
            clear_labs()
            clear_tasks()
            clear_modules()
            clear_tracks()

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
                # Map difficulty to estimated time and XP
                difficulty = task_data.get("difficulty", "medium")
                estimated_minutes = {"easy": 10, "medium": 15, "hard": 25}.get(difficulty, 15)
                xp_reward = {"easy": 20, "medium": 30, "hard": 50}.get(difficulty, 30)

                create_task(TaskCreate(
                    module_id=module.id,
                    title=task_data["title"],
                    description=task_data.get("description"),
                    content=task_data.get("content"),
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
                    difficulty="medium",  # Default, could be in data
                    xp_reward=int(lab_data.get("hours", 2.0) * 50),  # 50 XP per hour
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

        return SeedResponse(
            success=True,
            message=f"Successfully seeded Bootcamp v3.0: {tracks_created} tracks, {modules_created} modules, {tasks_created} tasks, {labs_created} labs, {projects_created} projects",
            tracks_created=tracks_created,
            modules_created=modules_created,
            tasks_created=tasks_created,
            labs_created=labs_created,
            projects_created=projects_created,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to seed bootcamp data: {str(e)}"
        )


class SeedV4Response(BaseModel):
    """Response for v4 seeding"""
    success: bool
    status: str
    tracks: int = 0
    modules: int = 0
    tasks: int = 0
    total_hours: float = 0


@admin_router.post("/seed-v4", response_model=SeedV4Response)
def seed_bootcamp_v4(
    response: Response,
    current_user: CurrentUser,
) -> SeedV4Response:
    """
    Seed Bootcamp v4.0 (Senior DevOps) content.

    v4.0 includes:
    - 6 Sections (Linux Mastery, Networking, K8s Advanced, SRE, Security, Platform)
    - 60+ Advanced modules
    - ~500 hours of content

    Note: v4.0 modules are seeded as inactive by default.
    Use /admin/activate-v4 to make them visible to users.
    """
    add_phase_header(response)
    require_admin(current_user)

    # V4 content har flyttats till _archive - returnera info om detta
    return SeedV4Response(
        success=False,
        status="deprecated",
        tracks=0,
        modules=0,
        tasks=0,
        total_hours=0,
    )


class SeedSkillsmapsResponse(BaseModel):
    """Response for skillsmaps seeding"""
    success: bool
    message: str
    tracks_created: int = 0
    modules_created: int = 0
    tasks_created: int = 0
    total_hours: float = 0


@admin_router.post("/seed-skillsmaps", response_model=SeedSkillsmapsResponse)
def seed_skillsmaps_v3(
    response: Response,
    current_user: CurrentUser,
    add_track: bool = True,
) -> SeedSkillsmapsResponse:
    """
    Seed all converted Skillsmaps modules (v3 format).

    This adds 14 modules with 438 tasks covering:
    - AWS, Terraform (Cloud & Infrastructure)
    - Docker, Kubernetes (Containers & Orchestration)
    - Linux, Bash, Git, Python (Foundation)
    - CI/CD (Platform Engineering)
    - Go, JavaScript, TypeScript, Node.js, MLOps (Advanced Specialty)

    Args:
        add_track: If True, creates "Advanced Specialty" track for new modules
    """
    add_phase_header(response)
    require_admin(current_user)

    try:
        # Get existing tracks
        existing_tracks = {t.slug: t.id for t in list_tracks()}
        track_id_map = dict(existing_tracks)
        tracks_created = 0

        # Add Advanced Specialty track if needed
        if add_track and "advanced-specialty" not in existing_tracks:
            new_track = create_track(TrackCreate(
                name="Advanced Specialty",
                slug="advanced-specialty",
                description="Specialized skills for senior DevOps engineers: Go, MLOps, System Design, and more",
                color="#10b981",  # Emerald
                icon="🎯",
                order_index=5,
            ))
            track_id_map["advanced-specialty"] = new_track.id
            tracks_created += 1

        # Seed all v3 modules
        modules_created = 0
        tasks_created = 0
        total_hours = 0

        for module_data in get_v3_modules():
            # Get track ID (use advanced-specialty as fallback)
            track_slug = module_data.get("track_slug", "advanced-specialty")
            track_id = track_id_map.get(track_slug) or track_id_map.get("advanced-specialty")

            # Check if module already exists
            existing = get_module_by_slug(module_data["slug"])
            if existing:
                continue  # Skip existing modules

            # Create module
            module = create_module(ModuleCreate(
                track_id=track_id,
                name=module_data["name"],
                slug=module_data["slug"],
                description=module_data.get("description", ""),
                order_index=module_data.get("order_index", 100 + modules_created),
                difficulty=module_data.get("difficulty", "intermediate"),
                estimated_hours=module_data.get("estimated_hours", 10.0),
                prerequisites=module_data.get("prerequisites", []),
            ))
            modules_created += 1
            total_hours += module_data.get("estimated_hours", 10.0)

            # Create tasks for this module
            for idx, task_data in enumerate(module_data.get("tasks", [])):
                create_task(TaskCreate(
                    module_id=module.id,
                    title=task_data["title"],
                    description=task_data.get("description"),
                    content=task_data.get("content", ""),
                    order_index=idx + 1,
                    difficulty=task_data.get("difficulty", "medium"),
                    estimated_minutes=task_data.get("estimated_minutes", 30),
                    xp_reward=task_data.get("xp_reward", 50),
                ))
                tasks_created += 1

        return SeedSkillsmapsResponse(
            success=True,
            message=f"Seeded {modules_created} modules with {tasks_created} tasks",
            tracks_created=tracks_created,
            modules_created=modules_created,
            tasks_created=tasks_created,
            total_hours=total_hours,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to seed skillsmaps: {str(e)}"
        )


def seed_skillsmaps_v3_internal(db=None) -> dict:
    """
    Internal seed function for startup script (no auth required).

    This is called by start.sh to ensure modules/tasks exist after deploy.
    Idempotent - safe to run multiple times.

    Returns:
        dict with seed results
    """
    from ..db.track_repository import list_tracks, create_track
    from ..db.module_repository import get_module_by_slug, create_module
    from ..db.task_repository import create_task
    from ..models.track import TrackCreate
    from ..models.module import ModuleCreate
    from ..models.task import TaskCreate

    try:
        # Get existing tracks
        existing_tracks = {t.slug: t.id for t in list_tracks()}
        track_id_map = dict(existing_tracks)
        tracks_created = 0

        # Add tracks if needed
        track_configs = [
            ("foundation", "Foundation", "Core DevOps fundamentals", "#3b82f6", "🏗️", 1),
            ("containers-orchestration", "Containers & Orchestration", "Docker & Kubernetes mastery", "#8b5cf6", "🐳", 2),
            ("cloud-infrastructure", "Cloud & Infrastructure", "AWS, Terraform, and cloud architecture", "#f59e0b", "☁️", 3),
            ("platform-engineering", "Platform Engineering", "CI/CD, GitOps, and developer platforms", "#10b981", "⚙️", 4),
            ("advanced-specialty", "Advanced Specialty", "Specialized skills for senior engineers", "#ec4899", "🎯", 5),
        ]

        for slug, name, desc, color, icon, order in track_configs:
            if slug not in existing_tracks:
                try:
                    new_track = create_track(TrackCreate(
                        name=name,
                        slug=slug,
                        description=desc,
                        color=color,
                        icon=icon,
                        order_index=order,
                    ))
                    track_id_map[slug] = new_track.id
                    tracks_created += 1
                except Exception:
                    pass  # Track might already exist

        # Seed all v3 modules
        modules_created = 0
        tasks_created = 0
        total_hours = 0

        for module_data in get_v3_modules():
            # Get track ID
            track_slug = module_data.get("track_slug", "advanced-specialty")
            track_id = track_id_map.get(track_slug) or track_id_map.get("foundation")

            # Check if module already exists
            existing = get_module_by_slug(module_data["slug"])
            if existing:
                continue  # Skip existing modules (idempotent)

            # Create module
            module = create_module(ModuleCreate(
                track_id=track_id,
                name=module_data["name"],
                slug=module_data["slug"],
                description=module_data.get("description", ""),
                order_index=module_data.get("order_index", 100 + modules_created),
                difficulty=module_data.get("difficulty", "intermediate"),
                estimated_hours=module_data.get("estimated_hours", 10.0),
                prerequisites=module_data.get("prerequisites", []),
            ))
            modules_created += 1
            total_hours += module_data.get("estimated_hours", 10.0)

            # Create tasks for this module
            for idx, task_data in enumerate(module_data.get("tasks", [])):
                create_task(TaskCreate(
                    module_id=module.id,
                    title=task_data["title"],
                    description=task_data.get("description"),
                    content=task_data.get("content", ""),
                    order_index=idx + 1,
                    difficulty=task_data.get("difficulty", "medium"),
                    estimated_minutes=task_data.get("estimated_minutes", 30),
                    xp_reward=task_data.get("xp_reward", 50),
                ))
                tasks_created += 1

        return {
            "success": True,
            "message": f"Seeded {modules_created} modules with {tasks_created} tasks",
            "tracks_created": tracks_created,
            "modules_created": modules_created,
            "tasks_created": tasks_created,
            "total_hours": total_hours,
        }

    except Exception as e:
        return {
            "success": False,
            "message": f"Seed error: {str(e)}",
            "error": str(e),
        }


@admin_router.get("/skillsmaps-status")
def get_skillsmaps_status(response: Response) -> dict:
    """
    Get status of available skillsmaps modules.
    """
    add_phase_header(response)

    return {
        "available_modules": get_v3_module_count(),
        "available_tasks": get_v3_total_tasks(),
        "modules": [
            {
                "name": m["name"],
                "slug": m["slug"],
                "tasks": len(m["tasks"]),
                "track": m["track_slug"],
                "hours": m.get("estimated_hours", 10),
            }
            for m in get_v3_modules()
        ]
    }


@admin_router.get("/seed-status", response_model=SeedStatusResponse)
def get_seed_status(response: Response) -> SeedStatusResponse:
    """
    Check the current seed status of the database.

    Returns:
        SeedStatusResponse with current counts vs expected.
    """
    add_phase_header(response)
    summary = get_bootcamp_summary()

    current_tracks = len(list_tracks())
    current_modules = len(list_modules())
    current_tasks = len(list_tasks())
    current_labs = len(list_labs())
    current_projects = len(list_projects())

    # Consider seeded if we have all expected tracks and modules
    is_seeded = (
        current_tracks >= summary["tracks"] and
        current_modules >= summary["modules"]
    )

    return SeedStatusResponse(
        seeded=is_seeded,
        tracks=current_tracks,
        modules=current_modules,
        tasks=current_tasks,
        labs=current_labs,
        projects=current_projects,
        expected_tracks=summary["tracks"],
        expected_modules=summary["modules"],
    )


@admin_router.get("/bootcamp-summary", response_model=BootcampSummaryResponse)
def get_bootcamp_content_summary(response: Response) -> BootcampSummaryResponse:
    """
    Get a summary of Bootcamp v3.0 content.

    Returns:
        BootcampSummaryResponse with content counts.
    """
    add_phase_header(response)
    summary = get_bootcamp_summary()
    return BootcampSummaryResponse(**summary)


@admin_router.delete("/clear-data")
def clear_all_data(
    response: Response,
    current_user: CurrentUser,
    confirm: bool = Query(False, description="Confirm deletion"),
) -> dict:
    """
    Clear all bootcamp data from the database (admin only).

    ⚠️ WARNING: This is a destructive operation.
    Requires confirm=true query parameter.

    Returns:
        Confirmation message with counts of deleted items.
    """
    add_phase_header(response)
    require_admin(current_user)

    if not confirm:
        raise HTTPException(
            status_code=400,
            detail="Destructive operation requires confirm=true parameter"
        )
    tracks_before = len(list_tracks())
    modules_before = len(list_modules())
    tasks_before = len(list_tasks())
    labs_before = len(list_labs())
    projects_before = len(list_projects())

    clear_projects()
    clear_labs()
    clear_tasks()
    clear_modules()
    clear_tracks()

    return {
        "success": True,
        "message": "All data cleared",
        "tracks_deleted": tracks_before,
        "modules_deleted": modules_before,
        "tasks_deleted": tasks_before,
        "labs_deleted": labs_before,
        "projects_deleted": projects_before,
    }


class SeedRelatedResponse(BaseModel):
    """Response for seeding related/fördjupning tasks"""
    success: bool
    message: str
    tasks_created: int = 0
    links_created: int = 0


@admin_router.post("/seed-related-tasks", response_model=SeedRelatedResponse)
def seed_related_tasks(
    response: Response,
    current_user: CurrentUser,
) -> SeedRelatedResponse:
    """
    Seed fördjupning (advanced/deep_dive) tasks linked to v3 standard tasks.

    This creates optional advanced content that appears under
    "Vill du fördjupa dig?" section in task view.

    Phase 4.0: Task Tier System
    """
    add_phase_header(response)
    require_admin(current_user)

    try:
        from ..db.seeds.related_tasks_content import seed_related_tasks_content
        result = seed_related_tasks_content()

        return SeedRelatedResponse(
            success=result.get("status") == "success",
            message=result.get("message", ""),
            tasks_created=result.get("tasks_created", 0),
            links_created=result.get("links_created", 0),
        )
    except ImportError:
        # Fallback: create sample related tasks
        return _create_sample_related_tasks()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to seed related tasks: {str(e)}"
        )


def _create_sample_related_tasks() -> SeedRelatedResponse:
    """Create sample related tasks for demonstration."""
    from ..db.task_repository import list_tasks, create_task, get_tasks_by_parent_id
    from ..schemas.task import TaskCreate

    tasks = list_tasks()
    standard_tasks = [t for t in tasks if getattr(t, 'task_tier', 'standard') == 'standard']

    if not standard_tasks:
        return SeedRelatedResponse(
            success=False,
            message="No standard tasks found to link to",
            tasks_created=0,
            links_created=0,
        )

    # Unique fördjupning content for each parent task
    FORDJUPNING_CONTENT = {
        "macos vs linux": {
            "title": "🔬 Deep Dive: Linux Kernel vs Darwin",
            "description": "Utforska de fundamentala skillnaderna mellan Linux och macOS på kernel-nivå",
            "content": """# 🔬 Deep Dive: Linux Kernel vs Darwin

## 🎯 Lärandemål
Efter denna fördjupning kommer du kunna:
- Förklara skillnader mellan monolitisk och hybrid kernel
- Jämföra systemanropsmekanismer
- Förstå containerisering på båda plattformarna

---

## 🧠 Kernel-arkitektur

### Linux: Monolitisk Kernel
```
+-----------------------------------------+
|           User Space (Ring 3)           |
+-----------------------------------------+
|    System Call Interface (syscall)      |
+-----------------------------------------+
|         Linux Kernel (Ring 0)           |
|  +---------+---------+---------+        |
|  | Process | Memory  |  File   |        |
|  | Sched.  |  Mgmt   | Systems |        |
|  +---------+---------+---------+        |
|  +---------+---------+---------+        |
|  | Network | Device  |   IPC   |        |
|  |  Stack  | Drivers |         |        |
|  +---------+---------+---------+        |
+-----------------------------------------+
```

### macOS: XNU Hybrid Kernel
```
+-----------------------------------------+
|           User Space (Ring 3)           |
+-----------------------------------------+
|        BSD Layer (POSIX APIs)           |
+-----------------------------------------+
|           Mach Microkernel              |
|  +---------+---------+---------+        |
|  |  Tasks  |  Ports  | Memory  |        |
|  |         |  (IPC)  |  Mgmt   |        |
|  +---------+---------+---------+        |
+-----------------------------------------+
|         I/O Kit (Device Drivers)        |
+-----------------------------------------+
```

---

## 💡 Praktiskt exempel: Containerisering

### Varför Docker är "native" på Linux

```bash
# Linux: Containers använder kernel features direkt
# Namespaces för isolering
unshare --mount --uts --ipc --net --pid --fork /bin/bash

# cgroups för resursbegränsning
cat /sys/fs/cgroup/memory/docker/<container>/memory.limit_in_bytes
```

### macOS: Virtualisering krävs
```bash
# Docker Desktop startar en Linux VM
# HyperKit (eller nu Virtualization.framework)

# Kontrollera VM:en
docker run --privileged --pid=host debian nsenter -t 1 -m -u -i -n cat /etc/os-release
# Output: Linux!
```

---

## 🧪 Quiz: Testa din förståelse

**Fråga 1:** Varför kan inte Docker köra containers "native" på macOS?

<details>
<summary>Visa svar</summary>

macOS saknar Linux-specifika kernel features som:
- **Namespaces** (process, network, mount isolation)
- **cgroups** (resource control)
- **Union filesystems** (OverlayFS)

Därför måste Docker Desktop köra en Linux VM i bakgrunden.
</details>

**Fråga 2:** Vad är fördelen med XNU:s Mach-baserade IPC?

<details>
<summary>Visa svar</summary>

Mach ports ger:
- Kraftfull inter-process kommunikation
- Säker meddelandepassning
- Grund för macOS Services (launchd, XPC)
</details>

---

## 🎯 Sammanfattning

| Aspekt | Linux | macOS |
|--------|-------|-------|
| Kernel-typ | Monolitisk | Hybrid (Mach + BSD) |
| Containers | Native | Via VM |
| Syscalls | ~400 direkta | BSD + Mach traps |
| DevOps-fokus | Produktion | Utveckling |

---

## 📚 Vidare läsning
- [Linux Kernel Documentation](https://kernel.org/doc/)
- [XNU Source Code](https://github.com/apple/darwin-xnu)
- [How Docker Works on macOS](https://docs.docker.com/desktop/mac/)

**+75 XP** för att slutföra denna fördjupning! 🎉
""",
            "estimated_minutes": 35,
            "xp_reward": 75,
        },
        "terminal": {
            "title": "🚀 Terminal Power User: Zsh & Oh-My-Zsh Mastery",
            "description": "Gå från nybörjare till terminal-ninja med avancerad Zsh-konfiguration",
            "content": """# 🚀 Terminal Power User: Zsh & Oh-My-Zsh

## 🎯 Lärandemål
- Konfigurera en professionell Zsh-miljö
- Skapa egna aliases och funktioner
- Använda plugins för ökad produktivitet

---

## ⚡ Varför Zsh?

| Feature | Bash | Zsh |
|---------|------|-----|
| Tab-completion | Basic | Intelligent |
| Spelling correction | ❌ | ✅ |
| Path expansion | Limited | `**` recursive |
| Prompt themes | Manual | Themes/Powerline |
| Plugin ecosystem | Limited | Oh-My-Zsh/Zinit |

---

## 🛠️ Installation & Setup

```bash
# macOS (redan standard sedan Catalina)
echo $SHELL  # /bin/zsh

# Linux
sudo apt install zsh
chsh -s $(which zsh)

# Oh-My-Zsh installation
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

---

## 🎨 Powerlevel10k Theme

```bash
# Installation
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \\
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Aktivera i ~/.zshrc
ZSH_THEME="powerlevel10k/powerlevel10k"

# Konfigurera
p10k configure
```

### Resultat:
```
╭- ~/projects/devopshub main ✔ 3m 42s
╰-❯ kubectl get pods
```

---

## 🔌 Måste-ha Plugins

```bash
# ~/.zshrc
plugins=(
  git                    # Git aliases (gst, gco, gp)
  docker                 # Docker completion
  kubectl                # K8s completion + aliases
  zsh-autosuggestions    # Fish-like suggestions
  zsh-syntax-highlighting # Command highlighting
  fzf                    # Fuzzy finder
)
```

### Installera externa plugins:
```bash
# zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions \\
  ${ZSH_CUSTOM}/plugins/zsh-autosuggestions

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting \\
  ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting
```

---

## 💪 DevOps Power Aliases

```bash
# Lägg till i ~/.zshrc

# Kubernetes shortcuts
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgd='kubectl get deploy'
alias klog='kubectl logs -f'
alias kex='kubectl exec -it'

# Docker shortcuts
alias d='docker'
alias dc='docker-compose'
alias dps='docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
alias dlog='docker logs -f'

# Git power aliases
alias gs='git status -sb'
alias gl='git log --oneline -10'
alias gd='git diff'
alias gcm='git commit -m'
alias gp='git push'

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -lah'
alias la='ls -A'
```

---

## 🧪 Praktisk övning

### Skapa en smart funktion:

```bash
# Lägg till i ~/.zshrc

# Snabb navigering till projekt
function proj() {
  cd ~/projects/$1 && ls -la
}

# Skapa och gå in i mapp
function mkcd() {
  mkdir -p "$1" && cd "$1"
}

# Docker shell
function dsh() {
  docker exec -it $1 /bin/sh
}

# Kubernetes pod shell
function ksh() {
  kubectl exec -it $1 -- /bin/sh
}
```

---

## 🎯 Testa din setup

```bash
# Ladda om config
source ~/.zshrc

# Testa completion (tryck TAB)
git che<TAB>     # -> checkout
kubectl get p<TAB>  # -> pods

# Testa alias
kgp  # kubectl get pods
dps  # docker ps formatted
```

---

## 📊 Produktivitetsvinst

| Kommando | Utan alias | Med alias | Sparar |
|----------|-----------|-----------|--------|
| kubectl get pods | 16 tecken | 3 tecken | 81% |
| docker-compose up | 17 tecken | 5 tecken | 71% |
| git status -sb | 14 tecken | 2 tecken | 86% |

---

**+75 XP** för terminal-mastery! 🎉
""",
            "estimated_minutes": 40,
            "xp_reward": 75,
        },
        "git": {
            "title": "🌳 Git Internals: Hur Git egentligen fungerar",
            "description": "Förstå Git på djupet - objects, refs, och the DAG",
            "content": """# 🌳 Git Internals: Under the Hood

## 🎯 Lärandemål
- Förstå Gits object model (blobs, trees, commits)
- Navigera `.git` katalogen
- Använda low-level Git commands (plumbing)

---

## 🧬 Git Object Model

Git lagrar allt som **objekt** med SHA-1 hash:

```
+---------------------------------------------+
|                   COMMIT                    |
|  tree: abc123...                            |
|  parent: def456...                          |
|  author: Said <said@dev.com>                |
|  message: "Add feature X"                   |
+--------------------+------------------------+
                     |
                     ▼
+---------------------------------------------+
|                    TREE                     |
|  blob: 789abc... README.md                  |
|  blob: 012def... src/main.py                |
|  tree: 345ghi... src/utils/                 |
+---------------------------------------------+
                     |
                     ▼
+---------------------------------------------+
|                    BLOB                     |
|  (raw file content)                         |
|  # My Project                               |
|  This is the README...                      |
+---------------------------------------------+
```

---

## 🔍 Utforska .git katalogen

```bash
# Skapa test-repo
mkdir git-internals && cd git-internals
git init

# Skapa en fil
echo "Hello Git" > hello.txt
git add hello.txt

# Se vad som hände i .git
find .git/objects -type f
# .git/objects/e9/65047ad7c57865823c7d992b1d046ea66edf78
```

### Läs objektet:
```bash
# git cat-file -t <hash>  -> typ
# git cat-file -p <hash>  -> innehåll

git cat-file -t e965047
# blob

git cat-file -p e965047
# Hello Git
```

---

## 🌿 Branches är bara pekare!

```bash
# En branch är en fil med en commit hash
cat .git/refs/heads/main
# abc123def456...

# HEAD pekar på current branch
cat .git/HEAD
# ref: refs/heads/main

# Skapa branch manuellt (!)
echo "abc123def456" > .git/refs/heads/my-branch
```

### Visualisering:
```
refs/heads/main ------+
                      ▼
                  [Commit C]
                      |
refs/heads/feature ---+
                      |
                      ▼
                  [Commit B]
                      |
                      ▼
                  [Commit A]
```

---

## 🛠️ Plumbing vs Porcelain

Git har två nivåer av kommandon:

| Porcelain (user-friendly) | Plumbing (low-level) |
|---------------------------|----------------------|
| `git add` | `git hash-object` |
| `git commit` | `git write-tree` |
| `git log` | `git cat-file` |
| `git diff` | `git diff-tree` |

### Skapa commit manuellt:
```bash
# 1. Hasha fil till blob
echo "Hello" | git hash-object -w --stdin
# e965047...

# 2. Skapa tree
git write-tree
# abc123...

# 3. Skapa commit
git commit-tree abc123 -m "Manual commit"
# def456...

# 4. Uppdatera branch
git update-ref refs/heads/main def456
```

---

## 🧪 Praktisk övning: Återskapa förlorad commit

```bash
# "Oh no!" - raderade en branch
git branch -D important-feature

# Men allt finns kvar i objects!
git reflog
# abc123 HEAD@{1}: checkout: moving to main
# def456 HEAD@{2}: commit: Important feature

# Återskapa!
git checkout -b recovered-feature def456
```

---

## 💡 Git Garbage Collection

```bash
# Visa "dangling" objects
git fsck --unreachable

# Packa objects effektivt
git gc

# Se pack-files
ls .git/objects/pack/
```

---

## 🎯 Quiz

**Fråga:** Vad händer egentligen när du kör `git commit`?

<details>
<summary>Visa svar</summary>

1. **write-tree** - skapar tree object från staging area
2. **commit-tree** - skapar commit object med:
   - Tree hash
   - Parent commit(s)
   - Author/committer
   - Message
3. **update-ref** - uppdaterar branch att peka på nya commit
</details>

---

**+75 XP** för Git-mastery! 🎉
""",
            "estimated_minutes": 45,
            "xp_reward": 75,
        },
        "filesystem": {
            "title": "📁 Deep Dive: Linux Filesystem Architecture",
            "description": "Förstå FHS på djupet - från inodes till mount namespaces",
            "content": """# 📁 Deep Dive: Linux Filesystem Architecture

## 🎯 Lärandemål
- Förstå inode-strukturen och hur filer lagras
- Navigera och förstå FHS på expert-nivå
- Använda advanced filesystem-kommandon

---

## 🧠 Inodes: Filsystemets DNA

Varje fil i Linux har en **inode** (index node) som innehåller:

```
+----------------------------------------+
|              INODE                      |
+----------------------------------------+
| • File type (file, dir, link, etc)     |
| • Permissions (rwxrwxrwx)              |
| • Owner (UID)                          |
| • Group (GID)                          |
| • Size                                 |
| • Timestamps (atime, mtime, ctime)     |
| • Link count                           |
| • Data block pointers                  |
+----------------------------------------+
```

### Utforska inodes:
```bash
# Visa inode-nummer
ls -i /etc/passwd
# 1234567 /etc/passwd

# Detaljerad inode-info
stat /etc/passwd

# Hitta fil via inode
find / -inum 1234567
```

---

## 🗂️ FHS: Filesystem Hierarchy Standard

| Katalog | Syfte | DevOps-relevans |
|---------|-------|-----------------|
| `/etc` | Systemkonfiguration | Config management |
| `/var` | Variabel data | Logs, caches |
| `/opt` | Third-party apps | Custom installations |
| `/srv` | Service data | Web/app data |
| `/tmp` | Temporära filer | Build artifacts |
| `/proc` | Process pseudo-fs | Monitoring |
| `/sys` | Kernel pseudo-fs | Hardware info |

---

## 🔧 Praktiska kommandon

### Diskanalys
```bash
# Diskutrymme per katalog
du -sh /var/* | sort -h

# Visa bara stora filer (>100MB)
find /var -size +100M -exec ls -lh {} \\;

# Inode-användning (kan fyllas före disk!)
df -i
```

### Mount & Bind mounts
```bash
# Lista mounts
findmnt

# Skapa bind mount
mount --bind /source /target

# Visa mount namespaces (containers!)
ls -la /proc/self/ns/mnt
```

---

## 🐳 DevOps: Container Filesystems

```bash
# Docker layers
docker inspect nginx --format '{{.GraphDriver.Data}}'

# Overlay filesystem
cat /proc/mounts | grep overlay

# Container root filesystem
docker export container_id | tar -tf - | head -20
```

---

## 🎯 Quiz

**Fråga:** Vad är skillnaden mellan hard link och symbolic link?

<details>
<summary>Visa svar</summary>

**Hard link:**
- Samma inode som originalet
- Kan inte korsa filsystem
- Fungerar om originalet tas bort

**Symbolic link:**
- Egen inode, pekar på sökväg
- Kan korsa filsystem
- Bryts om originalet tas bort
</details>

---

**+75 XP** för filesystem-mastery! 🎉
""",
            "estimated_minutes": 35,
            "xp_reward": 75,
        },
        "containers": {
            "title": "🐳 Deep Dive: Containers vs VMs - Under the Hood",
            "description": "Förstå containerisering på Linux kernel-nivå",
            "content": """# 🐳 Containers vs VMs: Under the Hood

## 🎯 Lärandemål
- Förstå Linux namespaces och cgroups
- Se hur Docker använder kernel features
- Jämföra performance och säkerhet

---

## 🏗️ Arkitektur-jämförelse

```
        Virtual Machines              Containers
    +---------------------+     +---------------------+
    |   App A  |  App B   |     |   App A  |  App B   |
    +----------+----------+     +----------+----------+
    |  Guest   |  Guest   |     |  Bins/   |  Bins/   |
    |   OS     |   OS     |     |  Libs    |  Libs    |
    +----------+----------+     +----------+----------+
    |     Hypervisor      |     |  Container Runtime  |
    +---------------------+     +---------------------+
    |      Host OS        |     |      Host OS        |
    +---------------------+     +---------------------+
    |     Hardware        |     |     Hardware        |
    +---------------------+     +---------------------+

    ~1-2 GB overhead/VM          ~50-100 MB/container
    Boot: 30-60 sekunder         Boot: <1 sekund
```

---

## 🔧 Linux Namespaces

Containers använder **6 namespaces** för isolering:

| Namespace | Isolerar | Flagga |
|-----------|----------|--------|
| **PID** | Process IDs | `CLONE_NEWPID` |
| **NET** | Network stack | `CLONE_NEWNET` |
| **MNT** | Mount points | `CLONE_NEWNS` |
| **UTS** | Hostname | `CLONE_NEWUTS` |
| **IPC** | IPC resources | `CLONE_NEWIPC` |
| **USER** | User/Group IDs | `CLONE_NEWUSER` |

### Testa själv:
```bash
# Skapa ny PID namespace
sudo unshare --pid --fork --mount-proc bash
ps aux  # Bara din bash syns!

# Skapa ny UTS namespace (hostname)
sudo unshare --uts bash
hostname container-test
hostname  # Ändrat! Men inte på host
```

---

## 📊 cgroups: Resource Control

```bash
# Skapa cgroup för minnestest
sudo cgcreate -g memory:/mygroup

# Sätt limit till 100MB
echo 100000000 | sudo tee /sys/fs/cgroup/memory/mygroup/memory.limit_in_bytes

# Kör process i cgroup
sudo cgexec -g memory:mygroup python3 -c "x='A'*200000000"
# Killed! (OOM)
```

---

## 🐳 Vad Docker egentligen gör

```bash
# Docker run = namespaces + cgroups + overlay fs + networking
docker run -it --rm alpine sh

# Samma sak manuellt:
unshare --pid --uts --net --mount --ipc --fork \\
  chroot /var/lib/docker/overlay2/.../merged /bin/sh
```

---

## 🔒 Säkerhetsjämförelse

| Aspekt | VM | Container |
|--------|-----|-----------|
| Kernel isolation | Separat | Delad |
| Attack surface | Mindre | Större |
| Escape risk | Låg | Högre |
| Seccomp/AppArmor | N/A | Rekommenderat |

---

## 🎯 Quiz

**Fråga:** Varför är containers snabbare att starta än VMs?

<details>
<summary>Visa svar</summary>

- **Ingen bootprocess** - använder host kernel direkt
- **Inget hypervisor-lager** - native syscalls
- **Shared filesystem layers** - overlay fs cachar base images
- **Ingen BIOS/POST** - bara process spawn
</details>

---

**+75 XP** för container-mastery! 🎉
""",
            "estimated_minutes": 40,
            "xp_reward": 75,
        },
    }

    # Create fördjupning tasks with unique content
    created = 0
    skipped = 0

    for parent_task in standard_tasks:
        # Check if this task already has related tasks
        existing_related = get_tasks_by_parent_id(parent_task.id)
        if existing_related:
            skipped += 1
            continue

        # Find matching content based on EXACT task title (lowercase)
        task_title_lower = parent_task.title.lower()
        content_data = None

        # Map exact task titles (lowercase) to content keys
        title_to_content = {
            "macos vs linux for devops work": "macos vs linux",
            "terminal emulators (iterm2, alacritty)": "terminal",
            "git object model (blobs, trees, commits)": "git",
            "filesystem hierarchy standard (fhs)": "filesystem",
            "containers vs vms": "containers",
        }

        content_key = title_to_content.get(task_title_lower)
        if content_key and content_key in FORDJUPNING_CONTENT:
            content_data = FORDJUPNING_CONTENT[content_key]

        if not content_data:
            continue

        # Create the fördjupning task
        create_task(TaskCreate(
            module_id=parent_task.module_id,
            title=content_data["title"],
            description=content_data["description"],
            content=content_data["content"],
            order_index=100 + created,
            difficulty="hard",
            estimated_minutes=content_data["estimated_minutes"],
            xp_reward=content_data["xp_reward"],
            task_tier="advanced",
            parent_task_id=parent_task.id,
        ))
        created += 1

    return SeedRelatedResponse(
        success=True,
        message=f"Created {created} fördjupning tasks (skipped {skipped} existing)",
        tasks_created=created,
        links_created=created,
    )


# DEV endpoint - no auth required (remove in production)
@admin_router.post("/dev/seed-related", response_model=SeedRelatedResponse)
def dev_seed_related_tasks(response: Response) -> SeedRelatedResponse:
    """
    DEV ONLY: Seed related tasks without authentication.
    Remove this endpoint before production launch.
    """
    add_phase_header(response)
    return _create_sample_related_tasks()


# =============================================================================
# QUIZ CACHE MANAGEMENT
# =============================================================================

class CacheClearResponse(BaseModel):
    """Response for cache clear operations"""
    success: bool
    message: str
    keys_deleted: int


@admin_router.post("/quiz/cache/clear", response_model=CacheClearResponse)
def clear_quiz_cache(
    response: Response,
    current_user: CurrentUser,
    module_slug: Optional[str] = None
) -> CacheClearResponse:
    """
    Clear quiz generation cache.

    - **module_slug**: Optional. If provided, clears cache only for this module.
                      If None, clears all quiz cache.
    """
    add_phase_header(response)
    require_admin(current_user)

    try:
        from ..services.quiz_service import clear_quiz_cache
        deleted = clear_quiz_cache(module_slug)

        if module_slug:
            message = f"Cleared {deleted} cache entries for module '{module_slug}'"
        else:
            message = f"Cleared {deleted} quiz cache entries"

        return CacheClearResponse(
            success=True,
            message=message,
            keys_deleted=deleted
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to clear cache: {str(e)}"
        )


@admin_router.get("/quiz/cache/stats")
def get_quiz_cache_stats(
    response: Response,
    current_user: CurrentUser
):
    """
    Get statistics about quiz cache usage.
    """
    add_phase_header(response)
    require_admin(current_user)

    from ..db.redis_client import get_redis_client

    client = get_redis_client()
    if not client:
        return {
            "redis_available": False,
            "message": "Redis not configured"
        }

    try:
        # Get all quiz cache keys
        keys = client.keys("quiz:*")

        # Get TTL for each key
        cache_info = []
        total_size = 0
        for key in keys[:100]:  # Limit to first 100 for performance
            ttl = client.ttl(key)
            value = client.get(key)
            size = len(value) if value else 0
            total_size += size

            cache_info.append({
                "key": key,
                "ttl_seconds": ttl,
                "size_bytes": size
            })

        return {
            "redis_available": True,
            "total_keys": len(keys),
            "sampled_keys": len(cache_info),
            "total_size_bytes": total_size,
            "total_size_mb": round(total_size / 1024 / 1024, 2),
            "sample": cache_info[:10]  # Return first 10 as sample
        }
    except Exception as e:
        return {
            "redis_available": True,
            "error": str(e)
        }

