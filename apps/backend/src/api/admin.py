"""
Admin API - Administrative endpoints for system management
Phase C.1: Seed Bootcamp Content
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..db.module_repository import create_module, clear_modules, list_modules
from ..db.task_repository import create_task, clear_tasks, list_tasks
from ..db.seeds.bootcamp_data import get_bootcamp_seed_data, get_module_count, get_task_count
from ..schemas.module import ModuleCreate
from ..schemas.task import TaskCreate


admin_router = APIRouter()


class SeedResponse(BaseModel):
    """Response schema for seed operations"""
    success: bool
    message: str
    modules_created: int
    tasks_created: int


class SeedStatusResponse(BaseModel):
    """Response schema for seed status check"""
    seeded: bool
    module_count: int
    task_count: int


@admin_router.post("/seed-bootcamp", response_model=SeedResponse)
def seed_bootcamp(clear_existing: bool = True) -> SeedResponse:
    """
    Seed the database with bootcamp modules and tasks.

    Args:
        clear_existing: If True, clear existing modules and tasks before seeding.
                       Defaults to True for idempotent seeding.

    Returns:
        SeedResponse with counts of created modules and tasks.
    """
    try:
        # Optionally clear existing data
        if clear_existing:
            clear_tasks()
            clear_modules()

        # Get seed data
        bootcamp_data = get_bootcamp_seed_data()

        modules_created = 0
        tasks_created = 0

        # Create modules and their tasks
        for module_data in bootcamp_data:
            # Create the module
            module = create_module(ModuleCreate(
                name=module_data["name"],
                description=module_data.get("description"),
            ))
            modules_created += 1

            # Create tasks for this module
            for task_data in module_data.get("tasks", []):
                create_task(TaskCreate(
                    module_id=module.id,
                    title=task_data["title"],
                    description=task_data.get("description"),
                    difficulty=task_data.get("difficulty", "medium"),
                ))
                tasks_created += 1

        return SeedResponse(
            success=True,
            message=f"Successfully seeded {modules_created} modules with {tasks_created} tasks",
            modules_created=modules_created,
            tasks_created=tasks_created,
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
        SeedStatusResponse with current module and task counts.
    """
    modules = list_modules()
    tasks = list_tasks()

    expected_modules = get_module_count()
    expected_tasks = get_task_count()

    # Consider seeded if we have at least the expected number
    is_seeded = len(modules) >= expected_modules and len(tasks) >= expected_tasks

    return SeedStatusResponse(
        seeded=is_seeded,
        module_count=len(modules),
        task_count=len(tasks),
    )


@admin_router.delete("/clear-data")
def clear_all_data() -> dict:
    """
    Clear all modules and tasks from the database.

    ⚠️ WARNING: This is a destructive operation.

    Returns:
        Confirmation message with counts of deleted items.
    """
    modules_before = len(list_modules())
    tasks_before = len(list_tasks())

    clear_tasks()
    clear_modules()

    return {
        "success": True,
        "message": "All data cleared",
        "modules_deleted": modules_before,
        "tasks_deleted": tasks_before,
    }
