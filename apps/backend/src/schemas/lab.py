"""
Lab Schemas - Pydantic models for Lab API validation
Phase C.1: Seed Bootcamp v3.0 Content (Redo)
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class LabBase(BaseModel):
    """Base lab schema with common fields"""
    title: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Lab title"
    )
    slug: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="URL-friendly identifier"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Brief description"
    )
    estimated_hours: float = Field(
        default=2.0,
        ge=0.5,
        le=20.0,
        description="Estimated hours to complete"
    )
    instructions: Optional[str] = Field(
        None,
        description="Markdown content with lab instructions"
    )
    expected_outcomes: list[str] = Field(
        default_factory=list,
        description="List of expected outcomes"
    )
    hints: list[str] = Field(
        default_factory=list,
        description="List of hints"
    )
    difficulty: Literal["easy", "medium", "hard"] = Field(
        default="medium",
        description="Lab difficulty level"
    )
    order_index: int = Field(
        default=0,
        ge=0,
        description="Display order within module"
    )
    xp_reward: int = Field(
        default=100,
        ge=0,
        le=1000,
        description="XP earned on completion"
    )
    is_active: bool = Field(default=True)

    class Config:
        from_attributes = True


class LabCreate(BaseModel):
    """Schema for creating a new lab"""
    module_id: UUID
    title: str = Field(..., min_length=3, max_length=200)
    slug: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    estimated_hours: float = Field(default=2.0, ge=0.5, le=20.0)
    instructions: Optional[str] = None
    expected_outcomes: list[str] = Field(default_factory=list)
    hints: list[str] = Field(default_factory=list)
    difficulty: Literal["easy", "medium", "hard"] = "medium"
    order_index: int = Field(default=0, ge=0)
    xp_reward: int = Field(default=100, ge=0, le=1000)

    @field_validator("slug")
    @classmethod
    def validate_slug(cls, v: str) -> str:
        v = v.strip().lower()
        if not v.replace("-", "").replace("_", "").replace(".", "").isalnum():
            raise ValueError("Slug must be alphanumeric with hyphens/underscores/dots only")
        return v


class LabUpdate(BaseModel):
    """Schema for updating an existing lab"""
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    estimated_hours: Optional[float] = Field(None, ge=0.5, le=20.0)
    instructions: Optional[str] = None
    expected_outcomes: Optional[list[str]] = None
    hints: Optional[list[str]] = None
    difficulty: Optional[Literal["easy", "medium", "hard"]] = None
    order_index: Optional[int] = Field(None, ge=0)
    xp_reward: Optional[int] = Field(None, ge=0, le=1000)
    is_active: Optional[bool] = None


class LabInDB(LabBase):
    """Schema for lab data stored in database"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


class LabPublic(LabBase):
    """Schema for public lab data in API responses"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


def create_lab_in_db(
    module_id: UUID,
    title: str,
    slug: str,
    description: Optional[str] = None,
    estimated_hours: float = 2.0,
    instructions: Optional[str] = None,
    expected_outcomes: Optional[list[str]] = None,
    hints: Optional[list[str]] = None,
    difficulty: Literal["easy", "medium", "hard"] = "medium",
    order_index: int = 0,
    xp_reward: int = 100,
    is_active: bool = True,
) -> LabInDB:
    """Factory function to create a new LabInDB"""
    now = datetime.utcnow()
    return LabInDB(
        id=uuid4(),
        module_id=module_id,
        title=title.strip(),
        slug=slug.strip().lower(),
        description=description,
        estimated_hours=estimated_hours,
        instructions=instructions,
        expected_outcomes=expected_outcomes or [],
        hints=hints or [],
        difficulty=difficulty,
        order_index=order_index,
        xp_reward=xp_reward,
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
