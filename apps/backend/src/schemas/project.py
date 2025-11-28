"""
Project Schemas - Pydantic models for Project API validation
Phase C.1: Seed Bootcamp v3.0 Content (Redo)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class ProjectBase(BaseModel):
    """Base project schema with common fields"""
    title: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Project title"
    )
    slug: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="URL-friendly identifier"
    )
    description: Optional[str] = Field(
        None,
        max_length=1000,
        description="Project overview"
    )
    requirements: Optional[str] = Field(
        None,
        description="Markdown content with detailed requirements"
    )
    deliverables: list[str] = Field(
        default_factory=list,
        description="List of deliverables to submit"
    )
    xp_reward: int = Field(
        default=500,
        ge=0,
        le=5000,
        description="XP earned on completion"
    )
    estimated_hours: float = Field(
        default=5.0,
        ge=1.0,
        le=50.0,
        description="Estimated hours to complete"
    )
    is_active: bool = Field(default=True)

    class Config:
        from_attributes = True


class ProjectCreate(BaseModel):
    """Schema for creating a new project"""
    module_id: UUID
    title: str = Field(..., min_length=3, max_length=200)
    slug: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    requirements: Optional[str] = None
    deliverables: list[str] = Field(default_factory=list)
    xp_reward: int = Field(default=500, ge=0, le=5000)
    estimated_hours: float = Field(default=5.0, ge=1.0, le=50.0)

    @field_validator("slug")
    @classmethod
    def validate_slug(cls, v: str) -> str:
        v = v.strip().lower()
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError("Slug must be alphanumeric with hyphens/underscores only")
        return v


class ProjectUpdate(BaseModel):
    """Schema for updating an existing project"""
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    requirements: Optional[str] = None
    deliverables: Optional[list[str]] = None
    xp_reward: Optional[int] = Field(None, ge=0, le=5000)
    estimated_hours: Optional[float] = Field(None, ge=1.0, le=50.0)
    is_active: Optional[bool] = None


class ProjectInDB(ProjectBase):
    """Schema for project data stored in database"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


class ProjectPublic(ProjectBase):
    """Schema for public project data in API responses"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


def create_project_in_db(
    module_id: UUID,
    title: str,
    slug: str,
    description: Optional[str] = None,
    requirements: Optional[str] = None,
    deliverables: Optional[list[str]] = None,
    xp_reward: int = 500,
    estimated_hours: float = 5.0,
    is_active: bool = True,
) -> ProjectInDB:
    """Factory function to create a new ProjectInDB"""
    now = datetime.utcnow()
    return ProjectInDB(
        id=uuid4(),
        module_id=module_id,
        title=title.strip(),
        slug=slug.strip().lower(),
        description=description,
        requirements=requirements,
        deliverables=deliverables or [],
        xp_reward=xp_reward,
        estimated_hours=estimated_hours,
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
