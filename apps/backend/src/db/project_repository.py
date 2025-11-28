"""
Project Repository - In-memory storage for projects
Phase C.1: Seed Bootcamp v3.0 Content (Redo)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..schemas.project import ProjectInDB, ProjectCreate, ProjectUpdate, create_project_in_db


# In-memory storage for projects
_projects_db: dict[UUID, ProjectInDB] = {}


def get_project_by_id(project_id: UUID) -> Optional[ProjectInDB]:
    """Get a project by its UUID."""
    return _projects_db.get(project_id)


def get_project_by_slug(slug: str) -> Optional[ProjectInDB]:
    """Get a project by its slug (case-insensitive)."""
    normalized_slug = slug.strip().lower()
    for project in _projects_db.values():
        if project.slug.lower() == normalized_slug:
            return project
    return None


def get_project_by_module(module_id: UUID) -> Optional[ProjectInDB]:
    """Get the project for a specific module (one project per module)."""
    for project in _projects_db.values():
        if project.module_id == module_id:
            return project
    return None


def list_projects() -> list[ProjectInDB]:
    """List all projects."""
    return list(_projects_db.values())


def create_project(data: ProjectCreate) -> ProjectInDB:
    """Create a new project."""
    project = create_project_in_db(
        module_id=data.module_id,
        title=data.title,
        slug=data.slug,
        description=data.description,
        requirements=data.requirements,
        deliverables=data.deliverables,
        xp_reward=data.xp_reward,
        estimated_hours=data.estimated_hours,
    )
    _projects_db[project.id] = project
    return project


def update_project(project_id: UUID, data: ProjectUpdate) -> Optional[ProjectInDB]:
    """Update an existing project."""
    existing = _projects_db.get(project_id)
    if not existing:
        return None

    updated_data = existing.model_dump()
    update_fields = data.model_dump(exclude_unset=True)

    for field, value in update_fields.items():
        if value is not None:
            updated_data[field] = value

    updated_data["updated_at"] = datetime.utcnow()
    updated_project = ProjectInDB(**updated_data)
    _projects_db[project_id] = updated_project
    return updated_project


def delete_project(project_id: UUID) -> bool:
    """Delete a project by its UUID."""
    if project_id in _projects_db:
        del _projects_db[project_id]
        return True
    return False


def clear_projects() -> None:
    """Clear all projects (for testing/seeding)."""
    _projects_db.clear()


def get_project_count() -> int:
    """Return total number of projects."""
    return len(_projects_db)
