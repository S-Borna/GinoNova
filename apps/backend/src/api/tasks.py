"""
Tasks Router - API endpoints for task management
Phase 3.0: Tasks Foundation
Phase v4.0: Added related tasks (fördjupning) endpoint
Phase v4.1: Added module_id query parameter support
"""
from uuid import UUID
from typing import List, Optional

from fastapi import APIRouter, Response, status, Query

from ..schemas.task import TaskCreate, TaskUpdate, TaskPublic, TaskWithRelated
from ..services.task_service import task_service

tasks_router = APIRouter()

# Phase version header
PHASE_VERSION = "4.1"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


@tasks_router.get("/status")
def tasks_status(response: Response):
    """Check tasks module status"""
    add_phase_header(response)
    return {
        "tasks": "configured",
        "phase": PHASE_VERSION,
        "endpoints": ["list", "list_by_module", "get", "create", "update", "delete"]
    }


@tasks_router.get("/", response_model=list[TaskPublic])
def list_tasks(
    response: Response,
    module_id: Optional[UUID] = Query(None, description="Filter tasks by module UUID"),
):
    """
    List tasks, optionally filtered by module.

    Args:
        module_id: Optional UUID to filter tasks by module

    Returns:
        List of all tasks, or tasks for the specified module
    """
    add_phase_header(response)
    if module_id:
        return task_service.list_tasks_for_module(module_id)
    return task_service.list_tasks()


@tasks_router.get("/module/slug/{module_slug}", response_model=list[TaskPublic])
def list_tasks_by_module_slug(module_slug: str, response: Response):
    """
    List all tasks for a module identified by slug.

    Args:
        module_slug: Slug of the module (e.g., 'linux-mastery')

    Returns:
        List of TaskPublic objects belonging to the module

    Raises:
        404: If module not found
    """
    add_phase_header(response)
    return task_service.list_tasks_for_module_slug(module_slug)


@tasks_router.get("/module/{module_id}", response_model=list[TaskPublic])
def list_tasks_by_module(module_id: UUID, response: Response):
    """
    List all tasks for a specific module.

    Args:
        module_id: UUID of the module

    Returns:
        List of TaskPublic objects belonging to the module

    Raises:
        404: If module not found
    """
    add_phase_header(response)
    return task_service.list_tasks_for_module(module_id)


@tasks_router.get("/{task_id}", response_model=TaskPublic)
def get_task(task_id: UUID, response: Response):
    """
    Get a specific task by ID.

    Args:
        task_id: UUID of the task to retrieve

    Returns:
        TaskPublic object

    Raises:
        404: If task not found
    """
    add_phase_header(response)
    return task_service.get_task_by_id(task_id)


@tasks_router.get("/{task_id}/related", response_model=List[TaskPublic])
def get_related_tasks(task_id: UUID, response: Response):
    """
    Get related advanced/deep-dive tasks for a standard task.

    This endpoint returns optional "fördjupning" (deep dive) tasks
    that are linked to the specified task. These are NOT locked -
    users can try them anytime for extra XP.

    Args:
        task_id: UUID of the parent/standard task

    Returns:
        List of related TaskPublic objects (advanced/deep_dive tier)

    Raises:
        404: If task not found
    """
    add_phase_header(response)
    return task_service.get_related_tasks(task_id)


@tasks_router.get("/{task_id}/with-related", response_model=TaskWithRelated)
def get_task_with_related(task_id: UUID, response: Response):
    """
    Get a task with its related advanced/deep-dive tasks included.

    Convenience endpoint that returns the task and all related
    fördjupning tasks in a single response.

    Args:
        task_id: UUID of the task to retrieve

    Returns:
        TaskWithRelated object with task + related_tasks array

    Raises:
        404: If task not found
    """
    add_phase_header(response)
    return task_service.get_task_with_related(task_id)


@tasks_router.post("/", response_model=TaskPublic, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, response: Response):
    """
    Create a new task.

    Args:
        data: TaskCreate schema with:
            - module_id: UUID of the parent module
            - title: Task title (3-100 chars, unique per module)
            - description: Optional description (max 500 chars)
            - difficulty: easy | medium | hard (default: medium)

    Returns:
        Created TaskPublic object

    Raises:
        404: If module not found
        409: If task title already exists in this module
        422: If validation fails
    """
    add_phase_header(response)
    return task_service.create_task(data)


@tasks_router.put("/{task_id}", response_model=TaskPublic)
def update_task(task_id: UUID, data: TaskUpdate, response: Response):
    """
    Update an existing task.

    Args:
        task_id: UUID of the task to update
        data: TaskUpdate schema with optional fields:
            - title: New task title (3-100 chars)
            - description: New description (max 500 chars)
            - difficulty: easy | medium | hard
            - is_active: Whether task is active

    Returns:
        Updated TaskPublic object

    Raises:
        404: If task not found
        409: If new title conflicts with existing task in same module
        422: If validation fails
    """
    add_phase_header(response)
    return task_service.update_task(task_id, data)


@tasks_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID, response: Response):
    """
    Delete a task.

    Args:
        task_id: UUID of the task to delete

    Raises:
        404: If task not found
    """
    add_phase_header(response)
    task_service.delete_task(task_id)
    return None
