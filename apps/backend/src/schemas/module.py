"""
Module Schemas - Pydantic models for Module API validation
Phase 2.0: Modules Foundation
Updated for Bootcamp v3.0 (C.1 Redo)
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class ModuleBase(BaseModel):
    """Base module schema with common fields"""
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Module name (2-100 characters)"
    )
    slug: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="URL-friendly identifier"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional module description (max 500 characters)"
    )
    order_index: int = Field(
        default=1,
        ge=1,
        le=50,
        description="Module number/order (1-50)"
    )
    difficulty: Literal["beginner", "intermediate", "advanced", "expert"] = Field(
        default="intermediate",
        description="Module difficulty level"
    )
    estimated_hours: float = Field(
        default=10.0,
        ge=1.0,
        le=50.0,
        description="Estimated hours to complete"
    )
    prerequisites: list[str] = Field(
        default_factory=list,
        description="List of prerequisite module slugs"
    )
    is_active: bool = Field(default=True, description="Whether module is active")

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate and normalize module name"""
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Module name must be at least 2 characters")
        return v

    class Config:
        from_attributes = True


class ModuleCreate(BaseModel):
    """Schema for creating a new module"""
    track_id: Optional[UUID] = Field(None, description="Parent track UUID")
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Module name (2-100 characters)"
    )
    slug: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="URL-friendly identifier"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional module description (max 500 characters)"
    )
    order_index: int = Field(default=1, ge=1, le=50)
    difficulty: Literal["beginner", "intermediate", "advanced", "expert"] = "intermediate"
    estimated_hours: float = Field(default=10.0, ge=1.0, le=50.0)
    prerequisites: list[str] = Field(default_factory=list)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate and normalize module name"""
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Module name must be at least 2 characters")
        return v

    @field_validator("slug")
    @classmethod
    def validate_slug(cls, v: str) -> str:
        v = v.strip().lower()
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError("Slug must be alphanumeric with hyphens/underscores only")
        return v


class ModuleUpdate(BaseModel):
    """Schema for updating an existing module"""
    track_id: Optional[UUID] = None
    name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="Module name (2-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional module description (max 500 characters)"
    )
    order_index: Optional[int] = Field(None, ge=1, le=50)
    difficulty: Optional[Literal["beginner", "intermediate", "advanced", "expert"]] = None
    estimated_hours: Optional[float] = Field(None, ge=1.0, le=50.0)
    prerequisites: Optional[list[str]] = None
    is_active: Optional[bool] = Field(None, description="Whether module is active")

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        """Validate and normalize module name if provided"""
        if v is not None:
            v = v.strip()
            if len(v) < 2:
                raise ValueError("Module name must be at least 2 characters")
        return v


class ModuleInDB(ModuleBase):
    """Schema for module data stored in database"""
    id: UUID
    track_id: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime


class ModulePublic(ModuleBase):
    """Schema for public module data in API responses"""
    id: UUID
    track_id: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime


class ModuleWithDetails(ModulePublic):
    """Module with tasks, labs, and project"""
    tasks: list["TaskPublicMinimal"] = []
    labs: list["LabPublicMinimal"] = []
    project: Optional["ProjectPublicMinimal"] = None


# Forward references for circular imports
class TaskPublicMinimal(BaseModel):
    """Minimal task info for module listing"""
    id: UUID
    title: str
    difficulty: str
    is_active: bool

    class Config:
        from_attributes = True


class LabPublicMinimal(BaseModel):
    """Minimal lab info for module listing"""
    id: UUID
    title: str
    estimated_hours: float
    difficulty: str

    class Config:
        from_attributes = True


class ProjectPublicMinimal(BaseModel):
    """Minimal project info for module listing"""
    id: UUID
    title: str
    xp_reward: int

    class Config:
        from_attributes = True


# Update forward references
ModuleWithDetails.model_rebuild()


def create_module_in_db(
    name: str,
    slug: str,
    description: Optional[str] = None,
    track_id: Optional[UUID] = None,
    order_index: int = 1,
    difficulty: Literal["beginner", "intermediate", "advanced", "expert"] = "intermediate",
    estimated_hours: float = 10.0,
    prerequisites: Optional[list[str]] = None,
    is_active: bool = True,
) -> ModuleInDB:
    """Factory function to create a new ModuleInDB with generated UUID and timestamps"""
    now = datetime.utcnow()
    return ModuleInDB(
        id=uuid4(),
        track_id=track_id,
        name=name.strip(),
        slug=slug.strip().lower(),
        description=description,
        order_index=order_index,
        difficulty=difficulty,
        estimated_hours=estimated_hours,
        prerequisites=prerequisites or [],
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
