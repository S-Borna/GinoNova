"""
Task Repository - In-memory storage for tasks
Phase 3.0: Tasks Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.task import TaskInDB, TaskCreate, TaskUpdate, create_task_in_db


# In-memory storage for tasks (will be replaced with PostgreSQL in Phase 3+)
_tasks_db: dict[UUID, TaskInDB] = {}


def get_task_by_id(task_id: UUID) -> Optional[TaskInDB]:
    """
    Get a task by its UUID.

    Args:
        task_id: The UUID of the task to retrieve

    Returns:
        TaskInDB if found, None otherwise
    """
    return _tasks_db.get(task_id)


def get_task_by_title_and_module(title: str, module_id: UUID) -> Optional[TaskInDB]:
    """
    Get a task by its title within a specific module (case-insensitive).

    Args:
        title: The title of the task to retrieve
        module_id: The UUID of the module

    Returns:
        TaskInDB if found, None otherwise
    """
    normalized_title = title.strip().lower()
    for task in _tasks_db.values():
        if task.module_id == module_id and task.title.lower() == normalized_title:
            return task
    return None


def list_tasks() -> list[TaskInDB]:
    """
    List all tasks.

    Returns:
        List of all TaskInDB objects
    """
    return list(_tasks_db.values())


def list_tasks_by_module(module_id: UUID) -> list[TaskInDB]:
    """
    List all tasks for a specific module.

    Args:
        module_id: The UUID of the module

    Returns:
        List of TaskInDB objects belonging to the module
    """
    return [task for task in _tasks_db.values() if task.module_id == module_id]


def create_task(data: TaskCreate) -> TaskInDB:
    """
    Create a new task.

    Args:
        data: TaskCreate schema with task data

    Returns:
        The created TaskInDB object
    """
    task = create_task_in_db(
        module_id=data.module_id,
        title=data.title,
        description=data.description,
        content=data.content,
        content_blocks=data.content_blocks,
        requirements=data.requirements,
        order_index=data.order_index,
        difficulty=data.difficulty,
        estimated_minutes=data.estimated_minutes,
        xp_reward=data.xp_reward,
    )
    _tasks_db[task.id] = task
    return task


def update_task(task_id: UUID, data: TaskUpdate) -> Optional[TaskInDB]:
    """
    Update an existing task.

    Args:
        task_id: The UUID of the task to update
        data: TaskUpdate schema with fields to update

    Returns:
        Updated TaskInDB if found, None otherwise
    """
    existing = _tasks_db.get(task_id)
    if not existing:
        return None

    # Create updated task with new values
    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    # Update timestamp
    updated_data["updated_at"] = datetime.utcnow()

    updated_task = TaskInDB(**updated_data)
    _tasks_db[task_id] = updated_task
    return updated_task


def delete_task(task_id: UUID) -> bool:
    """
    Delete a task by its UUID.

    Args:
        task_id: The UUID of the task to delete

    Returns:
        True if deleted, False if not found
    """
    if task_id in _tasks_db:
        del _tasks_db[task_id]
        return True
    return False


def clear_tasks() -> None:
    """Clear all tasks (for testing purposes)"""
    _tasks_db.clear()
