"""
Tasks Router - API endpoints for task management
Phase 3.0: Tasks Foundation
"""
from uuid import UUID

from fastapi import APIRouter, Response, status

from ..schemas.task import TaskCreate, TaskUpdate, TaskPublic
from ..services.task_service import task_service

tasks_router = APIRouter()

# Phase version header
PHASE_VERSION = "3.0"


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
def list_tasks(response: Response):
    """
    List all tasks.

    Returns list of all tasks in the system.
    """
    add_phase_header(response)
    return task_service.list_tasks()


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
