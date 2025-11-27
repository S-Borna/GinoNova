"""
Studyflow Schemas - Pydantic models for Studyflow API validation
Phase 4.0: Studyflow Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class StudyflowBase(BaseModel):
    """Base studyflow schema with common fields"""
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Studyflow title (3-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional studyflow description (max 500 characters)"
    )
    order: int = Field(
        default=1,
        gt=0,
        description="Position in the module (must be > 0)"
    )
    is_active: bool = Field(default=True, description="Whether studyflow is active")

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Validate and normalize studyflow title"""
        v = v.strip()
        if len(v) < 3:
            raise ValueError("Studyflow title must be at least 3 characters")
        return v

    @field_validator("order")
    @classmethod
    def validate_order(cls, v: int) -> int:
        """Validate order is positive"""
        if v <= 0:
            raise ValueError("Order must be greater than 0")
        return v

    class Config:
        from_attributes = True


class StudyflowCreate(BaseModel):
    """Schema for creating a new studyflow"""
    module_id: UUID = Field(..., description="UUID of the parent module")
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Studyflow title (3-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional studyflow description (max 500 characters)"
    )
    order: int = Field(
        default=1,
        gt=0,
        description="Position in the module (must be > 0)"
    )

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Validate and normalize studyflow title"""
        v = v.strip()
        if len(v) < 3:
            raise ValueError("Studyflow title must be at least 3 characters")
        return v

    @field_validator("order")
    @classmethod
    def validate_order(cls, v: int) -> int:
        """Validate order is positive"""
        if v <= 0:
            raise ValueError("Order must be greater than 0")
        return v


class StudyflowUpdate(BaseModel):
    """Schema for updating an existing studyflow"""
    title: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100,
        description="Studyflow title (3-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional studyflow description (max 500 characters)"
    )
    order: Optional[int] = Field(
        None,
        gt=0,
        description="Position in the module (must be > 0)"
    )
    is_active: Optional[bool] = Field(None, description="Whether studyflow is active")

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: Optional[str]) -> Optional[str]:
        """Validate and normalize studyflow title if provided"""
        if v is not None:
            v = v.strip()
            if len(v) < 3:
                raise ValueError("Studyflow title must be at least 3 characters")
        return v

    @field_validator("order")
    @classmethod
    def validate_order(cls, v: Optional[int]) -> Optional[int]:
        """Validate order is positive if provided"""
        if v is not None and v <= 0:
            raise ValueError("Order must be greater than 0")
        return v


class StudyflowInDB(StudyflowBase):
    """Schema for studyflow data stored in database"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


class StudyflowPublic(StudyflowBase):
    """Schema for public studyflow data in API responses"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


def create_studyflow_in_db(
    module_id: UUID,
    title: str,
    description: Optional[str] = None,
    order: int = 1,
    is_active: bool = True,
) -> StudyflowInDB:
    """Factory function to create a new StudyflowInDB with generated UUID and timestamps"""
    now = datetime.utcnow()
    return StudyflowInDB(
        id=uuid4(),
        module_id=module_id,
        title=title.strip(),
        description=description,
        order=order,
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
