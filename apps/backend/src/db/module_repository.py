"""
Module Repository - Hybrid storage (PostgreSQL when available, in-memory fallback)
Phase 2.0: Modules Foundation
Updated for Bootcamp v3.0 (C.1 Redo)
Phase 5.0: Hybrid PostgreSQL/in-memory support
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.module import ModuleInDB, ModuleCreate, ModuleUpdate, create_module_in_db
from .database import is_db_configured, get_db_context


# In-memory storage for modules (fallback when PostgreSQL not available)
_modules_db: dict[UUID, ModuleInDB] = {}


def _module_model_to_in_db(module_model) -> ModuleInDB:
    """Convert SQLAlchemy Module model to ModuleInDB schema."""
    return ModuleInDB(
        id=module_model.id,
        track_id=module_model.track_id,
        name=module_model.name,
        slug=module_model.slug,
        description=module_model.description,
        order_index=module_model.order_index,
        difficulty=module_model.difficulty,
        estimated_hours=module_model.estimated_hours,
        prerequisites=module_model.prerequisites or [],
        is_active=module_model.is_active,
        created_at=module_model.created_at,
        updated_at=module_model.updated_at,
    )


def get_module_by_id(module_id: UUID) -> Optional[ModuleInDB]:
    """
    Get a module by its UUID.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        module_id: The UUID of the module to retrieve

    Returns:
        ModuleInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_model = db.query(models.Module).filter(models.Module.id == module_id).first()
            if module_model:
                return _module_model_to_in_db(module_model)
            return None
    else:
        # Fallback to in-memory
        return _modules_db.get(module_id)


def get_module_by_name(name: str) -> Optional[ModuleInDB]:
    """
    Get a module by its name (case-insensitive).
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        name: The name of the module to retrieve

    Returns:
        ModuleInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_model = db.query(models.Module).filter(
                models.Module.name.ilike(name.strip())
            ).first()
            if module_model:
                return _module_model_to_in_db(module_model)
            return None
    else:
        # Fallback to in-memory
        normalized_name = name.strip().lower()
        for module in _modules_db.values():
            if module.name.lower() == normalized_name:
                return module
        return None


def get_module_by_slug(slug: str) -> Optional[ModuleInDB]:
    """
    Get a module by its slug (case-insensitive).
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        slug: The slug of the module to retrieve

    Returns:
        ModuleInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_model = db.query(models.Module).filter(
                models.Module.slug == slug.strip().lower()
            ).first()
            if module_model:
                return _module_model_to_in_db(module_model)
            return None
    else:
        # Fallback to in-memory
        normalized_slug = slug.strip().lower()
        for module in _modules_db.values():
            if module.slug.lower() == normalized_slug:
                return module
        return None


def get_modules_by_track(track_id: UUID) -> list[ModuleInDB]:
    """
    Get all modules for a specific track, ordered by order_index.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        track_id: The UUID of the track

    Returns:
        List of ModuleInDB objects for this track
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_models = db.query(models.Module).filter(
                models.Module.track_id == track_id
            ).order_by(models.Module.order_index).all()
            return [_module_model_to_in_db(m) for m in module_models]
    else:
        # Fallback to in-memory
        track_modules = [m for m in _modules_db.values() if m.track_id == track_id]
        return sorted(track_modules, key=lambda m: m.order_index)


def list_modules() -> list[ModuleInDB]:
    """
    List all modules ordered by order_index.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Returns:
        List of all ModuleInDB objects
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_models = db.query(models.Module).order_by(models.Module.order_index).all()
            return [_module_model_to_in_db(m) for m in module_models]
    else:
        # Fallback to in-memory
        return sorted(_modules_db.values(), key=lambda m: m.order_index)


def create_module(data: ModuleCreate) -> ModuleInDB:
    """
    Create a new module.
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        data: ModuleCreate schema with module data

    Returns:
        The created ModuleInDB object
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_model = models.Module(
                name=data.name,
                slug=data.slug,
                description=data.description,
                track_id=data.track_id,
                order_index=data.order_index,
                difficulty=data.difficulty,
                estimated_hours=data.estimated_hours,
                prerequisites=data.prerequisites or [],
                is_active=True,
            )
            db.add(module_model)
            db.commit()
            db.refresh(module_model)
            return _module_model_to_in_db(module_model)
    else:
        # Fallback to in-memory
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
    Uses PostgreSQL if available, otherwise in-memory storage.

    Args:
        module_id: The UUID of the module to update
        data: ModuleUpdate schema with fields to update

    Returns:
        Updated ModuleInDB if found, None otherwise
    """
    if is_db_configured():
        # Use PostgreSQL
        from . import models
        with get_db_context() as db:
            module_model = db.query(models.Module).filter(models.Module.id == module_id).first()
            if not module_model:
                return None

            # Update fields
            update_fields = data.model_dump(exclude_unset=True)
            for field, value in update_fields.items():
                if value is not None:
                    setattr(module_model, field, value)
            
            # Update timestamp
            module_model.updated_at = datetime.utcnow()
            
            db.commit()
            db.refresh(module_model)
            return _module_model_to_in_db(module_model)
    else:
        # Fallback to in-memory
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
