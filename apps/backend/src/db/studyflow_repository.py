"""
Studyflow Repository - In-memory storage for studyflows
Phase 4.0: Studyflow Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.studyflow import StudyflowInDB, StudyflowCreate, StudyflowUpdate, create_studyflow_in_db


# In-memory storage for studyflows (will be replaced with PostgreSQL later)
_studyflows_db: dict[UUID, StudyflowInDB] = {}


def get_studyflow_by_id(studyflow_id: UUID) -> Optional[StudyflowInDB]:
    """
    Get a studyflow by its UUID.

    Args:
        studyflow_id: The UUID of the studyflow to retrieve

    Returns:
        StudyflowInDB if found, None otherwise
    """
    return _studyflows_db.get(studyflow_id)


def get_studyflow_by_module_and_order(module_id: UUID, order: int) -> Optional[StudyflowInDB]:
    """
    Get a studyflow by module_id and order (unique constraint).

    Args:
        module_id: The UUID of the module
        order: The order position in the module

    Returns:
        StudyflowInDB if found, None otherwise
    """
    for studyflow in _studyflows_db.values():
        if studyflow.module_id == module_id and studyflow.order == order:
            return studyflow
    return None


def list_studyflows() -> list[StudyflowInDB]:
    """
    List all studyflows.

    Returns:
        List of all StudyflowInDB objects
    """
    return list(_studyflows_db.values())


def list_studyflows_by_module(module_id: UUID) -> list[StudyflowInDB]:
    """
    List all studyflows for a specific module, sorted by order.

    Args:
        module_id: The UUID of the module

    Returns:
        List of StudyflowInDB objects belonging to the module, sorted by order
    """
    studyflows = [sf for sf in _studyflows_db.values() if sf.module_id == module_id]
    return sorted(studyflows, key=lambda x: x.order)


def create_studyflow(data: StudyflowCreate) -> StudyflowInDB:
    """
    Create a new studyflow.

    Args:
        data: StudyflowCreate schema with studyflow data

    Returns:
        The created StudyflowInDB object
    """
    studyflow = create_studyflow_in_db(
        module_id=data.module_id,
        title=data.title,
        description=data.description,
        order=data.order,
    )
    _studyflows_db[studyflow.id] = studyflow
    return studyflow


def update_studyflow(studyflow_id: UUID, data: StudyflowUpdate) -> Optional[StudyflowInDB]:
    """
    Update an existing studyflow.

    Args:
        studyflow_id: The UUID of the studyflow to update
        data: StudyflowUpdate schema with fields to update

    Returns:
        Updated StudyflowInDB if found, None otherwise
    """
    existing = _studyflows_db.get(studyflow_id)
    if not existing:
        return None

    # Create updated studyflow with new values
    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    # Update timestamp
    updated_data["updated_at"] = datetime.utcnow()

    updated_studyflow = StudyflowInDB(**updated_data)
    _studyflows_db[studyflow_id] = updated_studyflow
    return updated_studyflow


def delete_studyflow(studyflow_id: UUID) -> bool:
    """
    Delete a studyflow by its UUID.

    Args:
        studyflow_id: The UUID of the studyflow to delete

    Returns:
        True if deleted, False if not found
    """
    if studyflow_id in _studyflows_db:
        del _studyflows_db[studyflow_id]
        return True
    return False


def clear_studyflows() -> None:
    """Clear all studyflows (for testing purposes)"""
    _studyflows_db.clear()
