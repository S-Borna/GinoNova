"""
Progress Schemas - Pydantic models for Progress API validation
Phase 5.0: Progress Engine Foundation
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator, model_validator

from ..models.progress import sync_status_from_progress


ProgressStatus = Literal["not_started", "in_progress", "completed"]


class ProgressBase(BaseModel):
    """Base progress schema with common fields"""
    user_id: UUID = Field(..., description="UUID of the user")
    module_id: Optional[UUID] = Field(None, description="UUID of the module (mutually exclusive)")
    task_id: Optional[UUID] = Field(None, description="UUID of the task (mutually exclusive)")
    studyflow_id: Optional[UUID] = Field(None, description="UUID of the studyflow (mutually exclusive)")
    progress: int = Field(default=0, ge=0, le=100, description="Progress percentage (0-100)")

    @model_validator(mode="after")
    def validate_exactly_one_target(self) -> "ProgressBase":
        """Ensure exactly one of module_id, task_id, studyflow_id is set"""
        targets = [self.module_id, self.task_id, self.studyflow_id]
        set_targets = [t for t in targets if t is not None]

        if len(set_targets) != 1:
            raise ValueError("Exactly one of module_id, task_id, or studyflow_id must be set")

        return self

    class Config:
        from_attributes = True


class ProgressCreate(BaseModel):
    """Schema for creating a new progress record"""
    user_id: UUID = Field(..., description="UUID of the user")
    module_id: Optional[UUID] = Field(None, description="UUID of the module (mutually exclusive)")
    task_id: Optional[UUID] = Field(None, description="UUID of the task (mutually exclusive)")
    studyflow_id: Optional[UUID] = Field(None, description="UUID of the studyflow (mutually exclusive)")
    progress: int = Field(default=0, ge=0, le=100, description="Progress percentage (0-100)")

    @model_validator(mode="after")
    def validate_exactly_one_target(self) -> "ProgressCreate":
        """Ensure exactly one of module_id, task_id, studyflow_id is set"""
        targets = [self.module_id, self.task_id, self.studyflow_id]
        set_targets = [t for t in targets if t is not None]

        if len(set_targets) != 1:
            raise ValueError("Exactly one of module_id, task_id, or studyflow_id must be set")

        return self


class ProgressUpdate(BaseModel):
    """Schema for updating an existing progress record"""
    progress: Optional[int] = Field(None, ge=0, le=100, description="Progress percentage (0-100)")

    # Note: We don't allow updating the target (module_id/task_id/studyflow_id)
    # Once a progress record is created for a target, the target is fixed


class ProgressInDB(BaseModel):
    """Schema for progress data stored in database"""
    id: UUID
    user_id: UUID
    module_id: Optional[UUID] = None
    task_id: Optional[UUID] = None
    studyflow_id: Optional[UUID] = None
    status: ProgressStatus
    progress: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProgressPublic(BaseModel):
    """Schema for public progress data in API responses"""
    id: UUID
    user_id: UUID
    module_id: Optional[UUID] = None
    task_id: Optional[UUID] = None
    studyflow_id: Optional[UUID] = None
    status: ProgressStatus
    progress: int
    created_at: datetime
    updated_at: datetime

    @property
    def target_type(self) -> str:
        """Get the type of target this progress is tracking"""
        if self.module_id:
            return "module"
        elif self.task_id:
            return "task"
        elif self.studyflow_id:
            return "studyflow"
        return "unknown"

    @property
    def target_id(self) -> Optional[UUID]:
        """Get the target ID"""
        return self.module_id or self.task_id or self.studyflow_id


def create_progress_in_db(
    user_id: UUID,
    module_id: Optional[UUID] = None,
    task_id: Optional[UUID] = None,
    studyflow_id: Optional[UUID] = None,
    progress: int = 0,
) -> ProgressInDB:
    """Factory function to create a new ProgressInDB with generated UUID and timestamps"""
    now = datetime.utcnow()
    status = sync_status_from_progress(progress)

    return ProgressInDB(
        id=uuid4(),
        user_id=user_id,
        module_id=module_id,
        task_id=task_id,
        studyflow_id=studyflow_id,
        status=status,
        progress=progress,
        created_at=now,
        updated_at=now,
    )
