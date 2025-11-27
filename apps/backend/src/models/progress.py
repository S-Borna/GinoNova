"""
Progress Model - Data model for tracking user progress
Phase 5.0: Progress Engine Foundation
"""
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID


ProgressStatus = Literal["not_started", "in_progress", "completed"]


class Progress:
    """
    Progress entity representing a user's progress on a module, task, or studyflow.

    Attributes:
        id: Unique identifier (UUID)
        user_id: UUID of the user
        module_id: UUID of the module (mutually exclusive with task_id/studyflow_id)
        task_id: UUID of the task (mutually exclusive with module_id/studyflow_id)
        studyflow_id: UUID of the studyflow (mutually exclusive with module_id/task_id)
        status: Progress status (not_started, in_progress, completed)
        progress: Percentage of completion (0-100)
        created_at: Timestamp of creation
        updated_at: Timestamp of last update

    Rules:
        - Exactly ONE of module_id, task_id, studyflow_id must be set
        - progress=0 => status="not_started"
        - progress 1-99 => status="in_progress"
        - progress=100 => status="completed"
    """

    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        module_id: Optional[UUID] = None,
        task_id: Optional[UUID] = None,
        studyflow_id: Optional[UUID] = None,
        status: ProgressStatus = "not_started",
        progress: int = 0,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.user_id = user_id
        self.module_id = module_id
        self.task_id = task_id
        self.studyflow_id = studyflow_id
        self.status = status
        self.progress = progress
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self) -> str:
        target = self._get_target_type()
        return f"Progress(id={self.id}, user_id={self.user_id}, target={target}, progress={self.progress}%)"

    def _get_target_type(self) -> str:
        if self.module_id:
            return f"module:{self.module_id}"
        elif self.task_id:
            return f"task:{self.task_id}"
        elif self.studyflow_id:
            return f"studyflow:{self.studyflow_id}"
        return "unknown"


def sync_status_from_progress(progress: int) -> ProgressStatus:
    """
    Derive status from progress percentage.

    Args:
        progress: Integer 0-100

    Returns:
        ProgressStatus based on progress value
    """
    if progress <= 0:
        return "not_started"
    elif progress >= 100:
        return "completed"
    else:
        return "in_progress"
