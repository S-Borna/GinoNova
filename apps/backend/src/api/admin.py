"""
Admin API - Administrative endpoints for system management
Phase C.1: Seed Bootcamp v3.0 Content (Redo)

Updated to support Bootcamp v3.0 with:
- 4 Tracks
- 15 Modules
- 60+ Labs
- 15+ Projects
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from uuid import UUID

from ..db.module_repository import create_module, clear_modules, list_modules
from ..db.task_repository import create_task, clear_tasks, list_tasks
from ..db.track_repository import create_track, clear_tracks, list_tracks, get_track_by_slug
from ..db.lab_repository import create_lab, clear_labs, list_labs
from ..db.project_repository import create_project, clear_projects, list_projects
from ..db import user_repository, progress_repository
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
from ..core.deps import CurrentUser


admin_router = APIRouter()


# Temporary admin email check
ADMIN_EMAIL = "said.ebadi@hotmail.com"


class AdminUserResponse(BaseModel):
    """Response schema for admin user list"""
    id: str
    full_name: Optional[str]
    email: str
    created_at: datetime
    total_xp: int
    level: int
    tasks_completed: int


class AdminUsersListResponse(BaseModel):
    """Response schema for admin users list"""
    users: List[AdminUserResponse]
    total: int


def calculate_level(xp: int) -> int:
    """Calculate level from XP (simple formula: level = 1 + xp // 100)"""
    return 1 + xp // 100


@admin_router.get("/users", response_model=AdminUsersListResponse)
def list_all_users(current_user: CurrentUser) -> AdminUsersListResponse:
    """
    Get all users with their stats.
    
    Only accessible to admin (said.ebadi@hotmail.com).
    
    Returns:
        List of users with id, name, email, created_at, total_xp, level, tasks_completed
    """
    # Check if user is admin
    if current_user.email.lower() != ADMIN_EMAIL:
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    
    users = user_repository.list_users()
    user_responses = []
    
    for user in users:
        # Get progress records for this user
        progress_records = progress_repository.list_progress_by_user(user.id)
        
        # Count completed tasks (status == "completed" or progress == 100)
        tasks_completed = sum(
            1 for p in progress_records 
            if p.task_id and (p.status == "completed" or p.progress == 100)
        )
        
        # Calculate XP (25 per completed task for now)
        total_xp = tasks_completed * 25
        
        user_responses.append(AdminUserResponse(
            id=str(user.id),
            full_name=user.full_name,
            email=user.email,
            created_at=user.created_at,
            total_xp=total_xp,
            level=calculate_level(total_xp),
            tasks_completed=tasks_completed,
        ))
    
    return AdminUsersListResponse(
        users=user_responses,
        total=len(user_responses)
    )


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
def seed_bootcamp(clear_existing: bool = True) -> SeedResponse:
    """
    Seed the database with Bootcamp v3.0 content.

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


@admin_router.get("/seed-status", response_model=SeedStatusResponse)
def get_seed_status() -> SeedStatusResponse:
    """
    Check the current seed status of the database.

    Returns:
        SeedStatusResponse with current counts vs expected.
    """
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
def get_bootcamp_content_summary() -> BootcampSummaryResponse:
    """
    Get a summary of Bootcamp v3.0 content.

    Returns:
        BootcampSummaryResponse with content counts.
    """
    summary = get_bootcamp_summary()
    return BootcampSummaryResponse(**summary)


@admin_router.delete("/clear-data")
def clear_all_data() -> dict:
    """
    Clear all bootcamp data from the database.

    ⚠️ WARNING: This is a destructive operation.

    Returns:
        Confirmation message with counts of deleted items.
    """
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
