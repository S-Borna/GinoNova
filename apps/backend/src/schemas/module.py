"""
Module Schemas - Pydantic models for Module API validation
Phase 2.0: Modules Foundation
"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class ModuleBase(BaseModel):
    """Base module schema with common fields"""
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Module name (2-50 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=300,
        description="Optional module description (max 300 characters)"
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
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Module name (2-50 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=300,
        description="Optional module description (max 300 characters)"
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate and normalize module name"""
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Module name must be at least 2 characters")
        return v


class ModuleUpdate(BaseModel):
    """Schema for updating an existing module"""
    name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=50,
        description="Module name (2-50 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=300,
        description="Optional module description (max 300 characters)"
    )
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
    created_at: datetime
    updated_at: datetime


class ModulePublic(ModuleBase):
    """Schema for public module data in API responses"""
    id: UUID
    created_at: datetime
    updated_at: datetime


def create_module_in_db(
    name: str,
    description: Optional[str] = None,
    is_active: bool = True,
) -> ModuleInDB:
    """Factory function to create a new ModuleInDB with generated UUID and timestamps"""
    now = datetime.utcnow()
    return ModuleInDB(
        id=uuid4(),
        name=name.strip(),
        description=description,
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
