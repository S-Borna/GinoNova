"""
Phase 8.1 — Raw Task Events Schema
Pure Pydantic models, zero logic.
"""

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field
from uuid import UUID


class RawTaskEvent(BaseModel):
    """
    Raw task event as captured from user actions.
    No transformations applied — pure event capture.
    """

    event_id: str = Field(..., description="Unique event identifier")
    event_type: Literal[
        "task_created",
        "task_started",
        "task_completed",
        "task_failed",
        "task_skipped",
        "task_paused",
        "task_resumed",
    ] = Field(..., description="Type of task event")
    user_id: UUID = Field(..., description="User who triggered the event")
    task_id: UUID = Field(..., description="Task associated with the event")
    module_id: Optional[UUID] = Field(None, description="Module context if applicable")
    timestamp: datetime = Field(..., description="Event timestamp (injected clock)")
    difficulty: Optional[int] = Field(
        None, ge=1, le=10, description="Task difficulty at event time"
    )
    duration_seconds: Optional[int] = Field(
        None, ge=0, description="Duration if applicable"
    )
    xp_awarded: Optional[int] = Field(None, ge=0, description="XP awarded if any")
    metadata: dict = Field(
        default_factory=dict, description="Additional unstructured metadata"
    )

    class Config:
        frozen = True  # Immutable raw events
        json_schema_extra = {
            "example": {
                "event_id": "evt_001",
                "event_type": "task_completed",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "task_id": "123e4567-e89b-12d3-a456-426614174001",
                "module_id": "123e4567-e89b-12d3-a456-426614174002",
                "timestamp": "2025-11-27T10:00:00Z",
                "difficulty": 5,
                "duration_seconds": 1800,
                "xp_awarded": 50,
                "metadata": {"attempt": 1},
            }
        }
