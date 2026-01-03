"""
Task Repository - Hybrid storage (PostgreSQL when available, in-memory fallback)
Phase 3.0: Tasks Foundation
Phase 4.0: Added parent_task_id support for related tasks (fördjupning)
Phase 5.0: Hybrid PostgreSQL/in-memory support
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.task import TaskInDB, TaskCreate, TaskUpdate, create_task_in_db
from .database import is_db_configured, get_db_context


# In-memory storage for tasks (fallback when PostgreSQL not available)
_tasks_db: dict[UUID, TaskInDB] = {}


def _task_model_to_in_db(task_model) -> TaskInDB:
    """Convert SQLAlchemy Task model to TaskInDB schema."""
    return TaskInDB(
        id=task_model.id,
        module_id=task_model.module_id,
        title=task_model.title,
        description=task_model.description,
        content=task_model.content,
        content_blocks=task_model.content_blocks or [],
        requirements=task_model.requirements or [],
        order_index=task_model.order_index,
        difficulty=task_model.difficulty,
        estimated_minutes=task_model.estimated_minutes,
        xp_reward=task_model.xp_reward,
        is_active=task_model.is_active,
        task_tier=getattr(task_model, 'task_tier', 'standard'),
        parent_task_id=getattr(task_model, 'parent_task_id', None),
        created_at=task_model.created_at,
        updated_at=task_model.updated_at,
    )


def get_task_by_id(task_id: UUID) -> Optional[TaskInDB]:
    """
    Get a task by its UUID.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        task_id: The UUID of the task to retrieve

    Returns:
        TaskInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            task_model = db.query(models.Task).filter(models.Task.id == task_id).first()
            if task_model:
                return _task_model_to_in_db(task_model)
            return None
    else:
        # Fallback to in-memory
        return _tasks_db.get(task_id)


def get_task_by_title_and_module(title: str, module_id: UUID) -> Optional[TaskInDB]:
    """
    Get a task by its title within a specific module (case-insensitive).
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        title: The title of the task to retrieve
        module_id: The UUID of the module

    Returns:
        TaskInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            task_model = db.query(models.Task).filter(
                models.Task.module_id == module_id,
                models.Task.title.ilike(title.strip())
            ).first()
            if task_model:
                return _task_model_to_in_db(task_model)
            return None
    else:
        # Fallback to in-memory
        normalized_title = title.strip().lower()
        for task in _tasks_db.values():
            if task.module_id == module_id and task.title.lower() == normalized_title:
                return task
        return None


def list_tasks() -> list[TaskInDB]:
    """
    List all tasks.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Returns:
        List of all TaskInDB objects
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            task_models = db.query(models.Task).order_by(models.Task.order_index).all()
            return [_task_model_to_in_db(t) for t in task_models]
    else:
        # Fallback to in-memory
        return list(_tasks_db.values())


def list_tasks_by_module(module_id: UUID) -> list[TaskInDB]:
    """
    List all tasks for a specific module.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        module_id: The UUID of the module

    Returns:
        List of TaskInDB objects belonging to the module
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            task_models = db.query(models.Task).filter(
                models.Task.module_id == module_id
            ).order_by(models.Task.order_index).all()
            return [_task_model_to_in_db(t) for t in task_models]
    else:
        # Fallback to in-memory
        return [task for task in _tasks_db.values() if task.module_id == module_id]


def get_tasks_by_parent_id(parent_task_id: UUID) -> list[TaskInDB]:
    """
    Get all tasks that are related to a parent task (fördjupning/deep dive tasks).
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        parent_task_id: The UUID of the parent task

    Returns:
        List of TaskInDB objects that have this parent_task_id
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            task_models = db.query(models.Task).filter(
                models.Task.parent_task_id == parent_task_id
            ).order_by(models.Task.order_index).all()
            return [_task_model_to_in_db(t) for t in task_models]
    else:
        # Fallback to in-memory
        return [
            task for task in _tasks_db.values()
            if getattr(task, 'parent_task_id', None) == parent_task_id
        ]


def create_task(data: TaskCreate) -> TaskInDB:
    """
    Create a new task.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        data: TaskCreate schema with task data

    Returns:
        The created TaskInDB object
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        from datetime import datetime
        with get_db_context() as db:
            task_model = models.Task(
                module_id=data.module_id,
                title=data.title,
                description=data.description,
                content=data.content,
                content_blocks=data.content_blocks or [],
                requirements=data.requirements or [],
                order_index=data.order_index,
                difficulty=data.difficulty,
                estimated_minutes=data.estimated_minutes,
                xp_reward=data.xp_reward,
                task_tier=getattr(data, 'task_tier', 'standard'),
                parent_task_id=getattr(data, 'parent_task_id', None),
                is_active=True,
            )
            db.add(task_model)
            db.commit()
            db.refresh(task_model)
            return _task_model_to_in_db(task_model)
    else:
        # Fallback to in-memory
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
            task_tier=getattr(data, 'task_tier', 'standard'),
            parent_task_id=getattr(data, 'parent_task_id', None),
        )
        _tasks_db[task.id] = task
        return task


def update_task(task_id: UUID, data: TaskUpdate) -> Optional[TaskInDB]:
    """
    Update an existing task.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        task_id: The UUID of the task to update
        data: TaskUpdate schema with fields to update

    Returns:
        Updated TaskInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            task_model = db.query(models.Task).filter(models.Task.id == task_id).first()
            if not task_model:
                return None

            # Update fields
            update_fields = data.model_dump(exclude_unset=True)
            for field, value in update_fields.items():
                if value is not None:
                    setattr(task_model, field, value)
            
            # Update timestamp
            task_model.updated_at = datetime.utcnow()
            
            db.commit()
            db.refresh(task_model)
            return _task_model_to_in_db(task_model)
    else:
        # Fallback to in-memory
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
