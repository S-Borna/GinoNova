"""
Task Schemas - Pydantic models for Task API validation
Phase 3.0: Tasks Foundation
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


DifficultyLevel = Literal["easy", "medium", "hard"]


class TaskBase(BaseModel):
    """Base task schema with common fields"""
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Task title (3-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional task description (max 500 characters)"
    )
    difficulty: DifficultyLevel = Field(
        default="medium",
        description="Task difficulty: easy, medium, or hard"
    )
    is_active: bool = Field(default=True, description="Whether task is active")

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Validate and normalize task title"""
        v = v.strip()
        if len(v) < 3:
            raise ValueError("Task title must be at least 3 characters")
        return v

    @field_validator("difficulty")
    @classmethod
    def validate_difficulty(cls, v: str) -> str:
        """Validate difficulty level"""
        valid_levels = {"easy", "medium", "hard"}
        if v not in valid_levels:
            raise ValueError(f"Difficulty must be one of: {', '.join(valid_levels)}")
        return v

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    """Schema for creating a new task"""
    module_id: UUID = Field(..., description="UUID of the parent module")
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Task title (3-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional task description (max 500 characters)"
    )
    difficulty: DifficultyLevel = Field(
        default="medium",
        description="Task difficulty: easy, medium, or hard"
    )

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Validate and normalize task title"""
        v = v.strip()
        if len(v) < 3:
            raise ValueError("Task title must be at least 3 characters")
        return v

    @field_validator("difficulty")
    @classmethod
    def validate_difficulty(cls, v: str) -> str:
        """Validate difficulty level"""
        valid_levels = {"easy", "medium", "hard"}
        if v not in valid_levels:
            raise ValueError(f"Difficulty must be one of: {', '.join(valid_levels)}")
        return v


class TaskUpdate(BaseModel):
    """Schema for updating an existing task"""
    title: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100,
        description="Task title (3-100 characters)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional task description (max 500 characters)"
    )
    difficulty: Optional[DifficultyLevel] = Field(
        None,
        description="Task difficulty: easy, medium, or hard"
    )
    is_active: Optional[bool] = Field(None, description="Whether task is active")

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: Optional[str]) -> Optional[str]:
        """Validate and normalize task title if provided"""
        if v is not None:
            v = v.strip()
            if len(v) < 3:
                raise ValueError("Task title must be at least 3 characters")
        return v

    @field_validator("difficulty")
    @classmethod
    def validate_difficulty(cls, v: Optional[str]) -> Optional[str]:
        """Validate difficulty level if provided"""
        if v is not None:
            valid_levels = {"easy", "medium", "hard"}
            if v not in valid_levels:
                raise ValueError(f"Difficulty must be one of: {', '.join(valid_levels)}")
        return v


class TaskInDB(TaskBase):
    """Schema for task data stored in database"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


class TaskPublic(TaskBase):
    """Schema for public task data in API responses"""
    id: UUID
    module_id: UUID
    created_at: datetime
    updated_at: datetime


def create_task_in_db(
    module_id: UUID,
    title: str,
    description: Optional[str] = None,
    difficulty: DifficultyLevel = "medium",
    is_active: bool = True,
) -> TaskInDB:
    """Factory function to create a new TaskInDB with generated UUID and timestamps"""
    now = datetime.utcnow()
    return TaskInDB(
        id=uuid4(),
        module_id=module_id,
        title=title.strip(),
        description=description,
        difficulty=difficulty,
        is_active=is_active,
        created_at=now,
        updated_at=now,
    )
