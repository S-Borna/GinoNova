"""
Module Repository - In-memory storage for modules
Phase 2.0: Modules Foundation
Updated for Bootcamp v3.0 (C.1 Redo)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.module import ModuleInDB, ModuleCreate, ModuleUpdate, create_module_in_db


# In-memory storage for modules (will be replaced with PostgreSQL in Phase 2+)
_modules_db: dict[UUID, ModuleInDB] = {}


def get_module_by_id(module_id: UUID) -> Optional[ModuleInDB]:
    """
    Get a module by its UUID.

    Args:
        module_id: The UUID of the module to retrieve

    Returns:
        ModuleInDB if found, None otherwise
    """
    return _modules_db.get(module_id)


def get_module_by_name(name: str) -> Optional[ModuleInDB]:
    """
    Get a module by its name (case-insensitive).

    Args:
        name: The name of the module to retrieve

    Returns:
        ModuleInDB if found, None otherwise
    """
    normalized_name = name.strip().lower()
    for module in _modules_db.values():
        if module.name.lower() == normalized_name:
            return module
    return None


def get_module_by_slug(slug: str) -> Optional[ModuleInDB]:
    """
    Get a module by its slug (case-insensitive).

    Args:
        slug: The slug of the module to retrieve

    Returns:
        ModuleInDB if found, None otherwise
    """
    normalized_slug = slug.strip().lower()
    for module in _modules_db.values():
        if module.slug.lower() == normalized_slug:
            return module
    return None


def get_modules_by_track(track_id: UUID) -> list[ModuleInDB]:
    """
    Get all modules for a specific track, ordered by order_index.

    Args:
        track_id: The UUID of the track

    Returns:
        List of ModuleInDB objects for this track
    """
    track_modules = [m for m in _modules_db.values() if m.track_id == track_id]
    return sorted(track_modules, key=lambda m: m.order_index)


def list_modules() -> list[ModuleInDB]:
    """
    List all modules ordered by order_index.

    Returns:
        List of all ModuleInDB objects
    """
    return sorted(_modules_db.values(), key=lambda m: m.order_index)


def create_module(data: ModuleCreate) -> ModuleInDB:
    """
    Create a new module.

    Args:
        data: ModuleCreate schema with module data

    Returns:
        The created ModuleInDB object
    """
    module = create_module_in_db(
        name=data.name,
        slug=data.slug,
        description=data.description,
        track_id=data.track_id,
        order_index=data.order_index,
        difficulty=data.difficulty,
        estimated_hours=data.estimated_hours,
        prerequisites=data.prerequisites,
    )
    _modules_db[module.id] = module
    return module


def update_module(module_id: UUID, data: ModuleUpdate) -> Optional[ModuleInDB]:
    """
    Update an existing module.

    Args:
        module_id: The UUID of the module to update
        data: ModuleUpdate schema with fields to update

    Returns:
        Updated ModuleInDB if found, None otherwise
    """
    existing = _modules_db.get(module_id)
    if not existing:
        return None

    # Create updated module with new values
    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    # Update timestamp
    updated_data["updated_at"] = datetime.utcnow()

    updated_module = ModuleInDB(**updated_data)
    _modules_db[module_id] = updated_module
    return updated_module


def delete_module(module_id: UUID) -> bool:
    """
    Delete a module by its UUID.

    Args:
        module_id: The UUID of the module to delete

    Returns:
        True if deleted, False if not found
    """
    if module_id in _modules_db:
        del _modules_db[module_id]
        return True
    return False


def clear_modules() -> None:
    """Clear all modules (for testing purposes)"""
    _modules_db.clear()
