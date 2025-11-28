"""
Lab Repository - In-memory storage for labs
Phase C.1: Seed Bootcamp v3.0 Content (Redo)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.lab import LabInDB, LabCreate, LabUpdate, create_lab_in_db


# In-memory storage for labs
_labs_db: dict[UUID, LabInDB] = {}


def get_lab_by_id(lab_id: UUID) -> Optional[LabInDB]:
    """Get a lab by its UUID."""
    return _labs_db.get(lab_id)


def get_lab_by_slug(slug: str) -> Optional[LabInDB]:
    """Get a lab by its slug (case-insensitive)."""
    normalized_slug = slug.strip().lower()
    for lab in _labs_db.values():
        if lab.slug.lower() == normalized_slug:
            return lab
    return None


def get_labs_by_module(module_id: UUID) -> list[LabInDB]:
    """Get all labs for a specific module, ordered by order_index."""
    module_labs = [lab for lab in _labs_db.values() if lab.module_id == module_id]
    return sorted(module_labs, key=lambda lab: lab.order_index)


def list_labs() -> list[LabInDB]:
    """List all labs."""
    return list(_labs_db.values())


def create_lab(data: LabCreate) -> LabInDB:
    """Create a new lab."""
    lab = create_lab_in_db(
        module_id=data.module_id,
        title=data.title,
        slug=data.slug,
        description=data.description,
        estimated_hours=data.estimated_hours,
        instructions=data.instructions,
        expected_outcomes=data.expected_outcomes,
        hints=data.hints,
        difficulty=data.difficulty,
        order_index=data.order_index,
        xp_reward=data.xp_reward,
    )
    _labs_db[lab.id] = lab
    return lab


def update_lab(lab_id: UUID, data: LabUpdate) -> Optional[LabInDB]:
    """Update an existing lab."""
    existing = _labs_db.get(lab_id)
    if not existing:
        return None

    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    updated_data["updated_at"] = datetime.utcnow()
    updated_lab = LabInDB(**updated_data)
    _labs_db[lab_id] = updated_lab
    return updated_lab


def delete_lab(lab_id: UUID) -> bool:
    """Delete a lab by its UUID."""
    if lab_id in _labs_db:
        del _labs_db[lab_id]
        return True
    return False


def clear_labs() -> None:
    """Clear all labs (for testing/seeding)."""
    _labs_db.clear()


def get_lab_count() -> int:
    """Return total number of labs."""
    return len(_labs_db)
