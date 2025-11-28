"""
Track Schemas - Pydantic models for Track API validation
Phase C.1: Seed Bootcamp v3.0 Content (Redo)
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class TrackBase(BaseModel):
    """Base track schema with common fields"""
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Track name"
    )
    slug: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="URL-friendly identifier"
    )
    description: str = Field(
        ...,
        max_length=500,
        description="Track description"
    )
    color: str = Field(
        ...,
        pattern=r'^#[0-9a-fA-F]{6}$',
        description="Hex color code (e.g., #6366f1)"
    )
    icon: str = Field(
        ...,
        max_length=10,
        description="Emoji or icon identifier"
    )
    order_index: int = Field(
        ...,
        ge=1,
        le=10,
        description="Display order (1-10)"
    )
    is_active: bool = Field(default=True, description="Whether track is active")

    class Config:
        from_attributes = True


class TrackCreate(BaseModel):
    """Schema for creating a new track"""
    name: str = Field(..., min_length=2, max_length=100)
    slug: str = Field(..., min_length=2, max_length=50)
    description: str = Field(..., max_length=500)
    color: str = Field(..., pattern=r'^#[0-9a-fA-F]{6}$')
    icon: str = Field(..., max_length=10)
    order_index: int = Field(..., ge=1, le=10)

    @field_validator("slug")
    @classmethod
    def validate_slug(cls, v: str) -> str:
        """Validate slug format"""
        v = v.strip().lower()
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError("Slug must be alphanumeric with hyphens/underscores only")
        return v


class TrackUpdate(BaseModel):
    """Schema for updating an existing track"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    color: Optional[str] = Field(None, pattern=r'^#[0-9a-fA-F]{6}$')
    icon: Optional[str] = Field(None, max_length=10)
    order_index: Optional[int] = Field(None, ge=1, le=10)
    is_active: Optional[bool] = None


class TrackInDB(TrackBase):
    """Schema for track data stored in database"""
    id: UUID
    created_at: datetime
    updated_at: datetime


class TrackPublic(TrackBase):
    """Schema for public track data in API responses"""
    id: UUID
    created_at: datetime
    updated_at: datetime


class TrackWithModules(TrackPublic):
    """Track with its modules (for detailed views)"""
    modules: list["ModulePublicMinimal"] = []


# Forward reference for circular import
class ModulePublicMinimal(BaseModel):
    """Minimal module info for track listing"""
    id: UUID
    name: str
    slug: str
    order_index: int
    is_active: bool

    class Config:
        from_attributes = True


# Update forward references
TrackWithModules.model_rebuild()


def create_track_in_db(
    name: str,
    slug: str,
    description: str,
    color: str,
    icon: str,
    order_index: int,
    is_active: bool = True,
) -> TrackInDB:
    """Factory function to create a new TrackInDB"""
    now = datetime.utcnow()
    return TrackInDB(
        id=uuid4(),
        name=name.strip(),
        slug=slug.strip().lower(),
        description=description.strip(),
        color=color,
        icon=icon,
        order_index=order_index,
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
