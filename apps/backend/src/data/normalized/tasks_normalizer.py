"""
Phase 8.2 — Task Events Normalizer
Deterministic normalization of raw task events.
"""

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field
from uuid import UUID

from ..raw.raw_task_events import RawTaskEvent


class NormalizedTaskEvent(BaseModel):
    """
    Normalized task event with computed fields and strict typing.
    Deterministic transformation from raw events.
    """

    event_id: str = Field(..., description="Original event identifier")
    event_type: str = Field(..., description="Normalized event type")
    user_id: str = Field(..., description="User ID as string")
    task_id: str = Field(..., description="Task ID as string")
    module_id: Optional[str] = Field(None, description="Module ID as string")
    timestamp_iso: str = Field(..., description="ISO8601 timestamp string")
    date_key: str = Field(..., description="Date key YYYY-MM-DD for indexing")
    hour_of_day: int = Field(..., ge=0, le=23, description="Hour of day 0-23")
    day_of_week: int = Field(..., ge=0, le=6, description="Day of week 0=Mon, 6=Sun")
    difficulty_bucket: Literal["easy", "medium", "hard", "extreme"] = Field(
        ..., description="Difficulty bucket for grouping"
    )
    duration_minutes: Optional[int] = Field(
        None, ge=0, description="Duration in minutes"
    )
    xp_awarded: int = Field(default=0, ge=0, description="XP awarded, defaulted to 0")
    is_completion: bool = Field(..., description="Whether this is a completion event")
    is_failure: bool = Field(..., description="Whether this is a failure event")

    class Config:
        frozen = True


def _difficulty_to_bucket(difficulty: Optional[int]) -> Literal["easy", "medium", "hard", "extreme"]:
    """
    Convert numeric difficulty to bucket.
    Deterministic mapping.
    """
    if difficulty is None or difficulty <= 3:
        return "easy"
    elif difficulty <= 5:
        return "medium"
    elif difficulty <= 7:
        return "hard"
    else:
        return "extreme"


def normalize_task_event(raw: RawTaskEvent) -> NormalizedTaskEvent:
    """
    Normalize a raw task event into a deterministic normalized record.
    No randomness, no time.now() — uses provided timestamp.

    Args:
        raw: Raw task event from capture layer

    Returns:
        NormalizedTaskEvent with computed fields
    """
    ts = raw.timestamp

    return NormalizedTaskEvent(
        event_id=raw.event_id,
        event_type=raw.event_type,
        user_id=str(raw.user_id),
        task_id=str(raw.task_id),
        module_id=str(raw.module_id) if raw.module_id else None,
        timestamp_iso=ts.isoformat(),
        date_key=ts.strftime("%Y-%m-%d"),
        hour_of_day=ts.hour,
        day_of_week=ts.weekday(),
        difficulty_bucket=_difficulty_to_bucket(raw.difficulty),
        duration_minutes=(
            raw.duration_seconds // 60 if raw.duration_seconds else None
        ),
        xp_awarded=raw.xp_awarded or 0,
        is_completion=raw.event_type == "task_completed",
        is_failure=raw.event_type == "task_failed",
    )
