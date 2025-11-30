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
from datetime import datetime, timedelta
from uuid import UUID
import math

from ..db.module_repository import create_module, clear_modules, list_modules
from ..db.task_repository import create_task, clear_tasks, list_tasks
from ..db.track_repository import create_track, clear_tracks, list_tracks, get_track_by_slug
from ..db.lab_repository import create_lab, clear_labs, list_labs
from ..db.project_repository import create_project, clear_projects, list_projects
from ..db import user_repository, progress_repository
from ..db.database import is_db_configured
from ..db.seeds.bootcamp_v3_data import (
    get_tracks,
    get_modules,
    get_bootcamp_summary,
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
            "content/health", "seed-bootcamp", "seed-status", "clear-data"
        ]
    }


# ==============================================================================
# USER MANAGEMENT ENDPOINTS
# ==============================================================================

@admin_router.get("/users", response_model=AdminUsersListResponse)
def list_all_users(
    response: Response,
    current_user: CurrentUser,
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    search: Optional[str] = Query(None, description="Search by email or name"),
    status: Optional[str] = Query(None, pattern="^(active|inactive|all)$"),
) -> AdminUsersListResponse:
    """
    Get all users with their stats (admin only).

    Supports pagination, search, and filtering.
    """
    add_phase_header(response)
    require_admin(current_user)

    users = user_repository.list_users()
    all_modules = list_modules()
    all_tasks = list_tasks()

    now = datetime.utcnow()
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

        user_xp = getattr(user, 'total_xp', tasks_completed * 25)
        last_active = user.updated_at
        if progress_records:
            latest = max(progress_records, key=lambda p: p.updated_at)
            if latest.updated_at > last_active:
                last_active = latest.updated_at

        user_details.append(AdminUserDetail(
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
            labs_completed=labs_completed,
            projects_completed=projects_completed,
            total_study_time=0,
            created_at=user.created_at,
            updated_at=user.updated_at,
            last_activity_at=last_active,
        ))

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
    """
    add_phase_header(response)
    require_admin(current_user)

    users = user_repository.list_users()
    tracks = list_tracks()
    modules = list_modules()
    tasks = list_tasks()
    labs = list_labs()
    projects = list_projects()

    now = datetime.utcnow()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_ago = now - timedelta(days=7)

    # User stats
    total_users = len(users)
    active_users = sum(1 for u in users if u.is_active)
    admin_users = sum(1 for u in users if is_admin(u))
    users_today = sum(1 for u in users if u.created_at >= today_start)
    users_this_week = sum(1 for u in users if u.created_at >= week_ago)

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

    try:
        from ..db.seeds.bootcamp_v4_content import seed_v4_content
        result = seed_v4_content()

        return SeedV4Response(
            success=result["status"] == "success",
            status=result["status"],
            tracks=result.get("tracks", 0),
            modules=result.get("modules", 0),
            tasks=result.get("tasks", 0),
            total_hours=result.get("total_hours", 0),
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to seed v4 content: {str(e)}"
        )


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
┌─────────────────────────────────────────┐
│           User Space (Ring 3)           │
├─────────────────────────────────────────┤
│    System Call Interface (syscall)      │
├─────────────────────────────────────────┤
│         Linux Kernel (Ring 0)           │
│  ┌─────────┬─────────┬─────────┐        │
│  │ Process │ Memory  │  File   │        │
│  │ Sched.  │  Mgmt   │ Systems │        │
│  └─────────┴─────────┴─────────┘        │
│  ┌─────────┬─────────┬─────────┐        │
│  │ Network │ Device  │   IPC   │        │
│  │  Stack  │ Drivers │         │        │
│  └─────────┴─────────┴─────────┘        │
└─────────────────────────────────────────┘
```

### macOS: XNU Hybrid Kernel
```
┌─────────────────────────────────────────┐
│           User Space (Ring 3)           │
├─────────────────────────────────────────┤
│        BSD Layer (POSIX APIs)           │
├─────────────────────────────────────────┤
│           Mach Microkernel              │
│  ┌─────────┬─────────┬─────────┐        │
│  │  Tasks  │  Ports  │ Memory  │        │
│  │         │  (IPC)  │  Mgmt   │        │
│  └─────────┴─────────┴─────────┘        │
├─────────────────────────────────────────┤
│         I/O Kit (Device Drivers)        │
└─────────────────────────────────────────┘
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
╭─ ~/projects/devopshub main ✔ 3m 42s 
╰─❯ kubectl get pods
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
git che<TAB>     # → checkout
kubectl get p<TAB>  # → pods

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
┌─────────────────────────────────────────────┐
│                   COMMIT                    │
│  tree: abc123...                            │
│  parent: def456...                          │
│  author: Said <said@dev.com>                │
│  message: "Add feature X"                   │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│                    TREE                     │
│  blob: 789abc... README.md                  │
│  blob: 012def... src/main.py                │
│  tree: 345ghi... src/utils/                 │
└─────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│                    BLOB                     │
│  (raw file content)                         │
│  # My Project                               │
│  This is the README...                      │
└─────────────────────────────────────────────┘
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
# git cat-file -t <hash>  → typ
# git cat-file -p <hash>  → innehåll

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
refs/heads/main ──────┐
                      ▼
                  [Commit C]
                      │
refs/heads/feature ───┤
                      │
                      ▼
                  [Commit B]
                      │
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
┌────────────────────────────────────────┐
│              INODE                      │
├────────────────────────────────────────┤
│ • File type (file, dir, link, etc)     │
│ • Permissions (rwxrwxrwx)              │
│ • Owner (UID)                          │
│ • Group (GID)                          │
│ • Size                                 │
│ • Timestamps (atime, mtime, ctime)     │
│ • Link count                           │
│ • Data block pointers                  │
└────────────────────────────────────────┘
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
    ┌─────────────────────┐     ┌─────────────────────┐
    │   App A  │  App B   │     │   App A  │  App B   │
    ├──────────┼──────────┤     ├──────────┼──────────┤
    │  Guest   │  Guest   │     │  Bins/   │  Bins/   │
    │   OS     │   OS     │     │  Libs    │  Libs    │
    ├──────────┴──────────┤     ├──────────┴──────────┤
    │     Hypervisor      │     │  Container Runtime  │
    ├─────────────────────┤     ├─────────────────────┤
    │      Host OS        │     │      Host OS        │
    ├─────────────────────┤     ├─────────────────────┤
    │     Hardware        │     │     Hardware        │
    └─────────────────────┘     └─────────────────────┘
    
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

