"""
Progress Repository - In-memory storage for progress records
Phase 5.0: Progress Engine Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.progress import ProgressInDB, ProgressCreate, ProgressUpdate, create_progress_in_db
from ..models.progress import sync_status_from_progress


# In-memory storage for progress records
_progress_db: dict[UUID, ProgressInDB] = {}


def get_progress_by_id(progress_id: UUID) -> Optional[ProgressInDB]:
    """
    Get a progress record by its UUID.

    Args:
        progress_id: The UUID of the progress record to retrieve

    Returns:
        ProgressInDB if found, None otherwise
    """
    return _progress_db.get(progress_id)


def list_progress_by_user(user_id: UUID) -> list[ProgressInDB]:
    """
    List all progress records for a specific user.

    Args:
        user_id: The UUID of the user

    Returns:
        List of ProgressInDB objects belonging to the user
    """
    return [p for p in _progress_db.values() if p.user_id == user_id]


def list_progress_by_module(module_id: UUID) -> list[ProgressInDB]:
    """
    List all progress records for a specific module.

    Args:
        module_id: The UUID of the module

    Returns:
        List of ProgressInDB objects for the module
    """
    return [p for p in _progress_db.values() if p.module_id == module_id]


def list_progress_by_task(task_id: UUID) -> list[ProgressInDB]:
    """
    List all progress records for a specific task.

    Args:
        task_id: The UUID of the task

    Returns:
        List of ProgressInDB objects for the task
    """
    return [p for p in _progress_db.values() if p.task_id == task_id]


def list_progress_by_studyflow(studyflow_id: UUID) -> list[ProgressInDB]:
    """
    List all progress records for a specific studyflow.

    Args:
        studyflow_id: The UUID of the studyflow

    Returns:
        List of ProgressInDB objects for the studyflow
    """
    return [p for p in _progress_db.values() if p.studyflow_id == studyflow_id]


def get_progress_by_user_and_target(
    user_id: UUID,
    module_id: Optional[UUID] = None,
    task_id: Optional[UUID] = None,
    studyflow_id: Optional[UUID] = None,
) -> Optional[ProgressInDB]:
    """
    Get progress record for a user and specific target (unique constraint check).

    Args:
        user_id: The UUID of the user
        module_id: Optional module UUID
        task_id: Optional task UUID
        studyflow_id: Optional studyflow UUID

    Returns:
        ProgressInDB if found, None otherwise
    """
    for progress in _progress_db.values():
        if progress.user_id != user_id:
            continue

        if module_id and progress.module_id == module_id:
            return progress
        if task_id and progress.task_id == task_id:
            return progress
        if studyflow_id and progress.studyflow_id == studyflow_id:
            return progress

    return None


def create_progress(data: ProgressCreate) -> ProgressInDB:
    """
    Create a new progress record.

    Args:
        data: ProgressCreate schema with progress data

    Returns:
        The created ProgressInDB object
    """
    progress = create_progress_in_db(
        user_id=data.user_id,
        module_id=data.module_id,
        task_id=data.task_id,
        studyflow_id=data.studyflow_id,
        progress=data.progress,
    )
    _progress_db[progress.id] = progress
    return progress


def update_progress(progress_id: UUID, data: ProgressUpdate) -> Optional[ProgressInDB]:
    """
    Update an existing progress record.

    Args:
        progress_id: The UUID of the progress record to update
        data: ProgressUpdate schema with fields to update

    Returns:
        Updated ProgressInDB if found, None otherwise
    """
    existing = _progress_db.get(progress_id)
    if not existing:
        return None

    # Create updated progress with new values
    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    # Sync status from progress if progress was updated
    if "progress" in update_fields and update_fields["progress"] is not None:
        updated_data["status"] = sync_status_from_progress(updated_data["progress"])

    # Update timestamp
    updated_data["updated_at"] = datetime.utcnow()

    updated_progress = ProgressInDB(**updated_data)
    _progress_db[progress_id] = updated_progress
    return updated_progress


def delete_progress(progress_id: UUID) -> bool:
    """
    Delete a progress record by its UUID.

    Args:
        progress_id: The UUID of the progress record to delete

    Returns:
        True if deleted, False if not found
    """
    if progress_id in _progress_db:
        del _progress_db[progress_id]
        return True
    return False


def clear_progress() -> None:
    """Clear all progress records (for testing purposes)"""
    _progress_db.clear()
