"""
Phase 8.1 — Raw Studyflow Sessions Schema
Pure Pydantic models, zero logic.
"""

from datetime import datetime
from typing import Literal, Optional, List
from pydantic import BaseModel, Field
from uuid import UUID


class RawStudyflowSession(BaseModel):
    """
    Raw studyflow session as captured from user study activities.
    No transformations applied — pure event capture.
    """

    session_id: str = Field(..., description="Unique session identifier")
    event_type: Literal[
        "session_started",
        "session_ended",
        "session_paused",
        "session_resumed",
        "break_started",
        "break_ended",
        "focus_changed",
    ] = Field(..., description="Type of session event")
    user_id: UUID = Field(..., description="User who owns the session")
    timestamp: datetime = Field(..., description="Event timestamp (injected clock)")
    duration_minutes: Optional[int] = Field(
        None, ge=0, description="Duration in minutes if applicable"
    )
    focus_score: Optional[float] = Field(
        None, ge=0.0, le=1.0, description="Focus score 0-1 if measured"
    )
    tasks_in_session: List[UUID] = Field(
        default_factory=list, description="Tasks worked on during session"
    )
    module_context: Optional[UUID] = Field(
        None, description="Module being studied if applicable"
    )
    interruptions: Optional[int] = Field(
        None, ge=0, description="Number of interruptions recorded"
    )
    energy_level: Optional[Literal["low", "medium", "high"]] = Field(
        None, description="Self-reported energy level"
    )
    metadata: dict = Field(
        default_factory=dict, description="Additional unstructured metadata"
    )

    class Config:
        frozen = True  # Immutable raw events
        json_schema_extra = {
            "example": {
                "session_id": "sess_001",
                "event_type": "session_ended",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "timestamp": "2025-11-27T12:00:00Z",
                "duration_minutes": 45,
                "focus_score": 0.85,
                "tasks_in_session": ["123e4567-e89b-12d3-a456-426614174001"],
                "module_context": "123e4567-e89b-12d3-a456-426614174002",
                "interruptions": 2,
                "energy_level": "high",
                "metadata": {"pomodoro_count": 2},
            }
        }
