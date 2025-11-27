"""
Phase 8.2 — Studyflow Session Normalizer
Deterministic normalization of raw studyflow sessions.
"""

from typing import Literal, Optional, List
from pydantic import BaseModel, Field

from ..raw.raw_studyflow_sessions import RawStudyflowSession


class NormalizedStudyflowSession(BaseModel):
    """
    Normalized studyflow session with computed fields and strict typing.
    Deterministic transformation from raw events.
    """

    session_id: str = Field(..., description="Original session identifier")
    event_type: str = Field(..., description="Normalized event type")
    user_id: str = Field(..., description="User ID as string")
    timestamp_iso: str = Field(..., description="ISO8601 timestamp string")
    date_key: str = Field(..., description="Date key YYYY-MM-DD for indexing")
    hour_of_day: int = Field(..., ge=0, le=23, description="Hour of day 0-23")
    day_of_week: int = Field(..., ge=0, le=6, description="Day of week 0=Mon, 6=Sun")
    duration_minutes: int = Field(default=0, ge=0, description="Duration in minutes")
    focus_bucket: Literal["low", "medium", "high", "peak"] = Field(
        ..., description="Focus score bucket"
    )
    tasks_count: int = Field(default=0, ge=0, description="Number of tasks in session")
    task_ids: List[str] = Field(
        default_factory=list, description="Task IDs as strings"
    )
    module_id: Optional[str] = Field(None, description="Module ID as string")
    interruptions: int = Field(default=0, ge=0, description="Interruption count")
    energy_level: str = Field(default="medium", description="Energy level")
    is_session_end: bool = Field(..., description="Whether this ends a session")
    productivity_score: float = Field(
        ..., ge=0.0, le=1.0, description="Computed productivity score"
    )

    class Config:
        frozen = True


def _focus_to_bucket(focus_score: Optional[float]) -> Literal["low", "medium", "high", "peak"]:
    """
    Convert numeric focus score to bucket.
    Deterministic mapping.
    """
    if focus_score is None or focus_score < 0.3:
        return "low"
    elif focus_score < 0.6:
        return "medium"
    elif focus_score < 0.85:
        return "high"
    else:
        return "peak"


def _compute_productivity(
    duration: int,
    focus_score: Optional[float],
    tasks_count: int,
    interruptions: int,
) -> float:
    """
    Compute deterministic productivity score from session metrics.
    Formula: base from focus * duration factor * task bonus - interruption penalty
    All operations are deterministic.
    """
    base = focus_score if focus_score is not None else 0.5

    # Duration factor: longer focused sessions are more productive (capped)
    duration_factor = min(duration / 60.0, 1.5) if duration > 0 else 0.5

    # Task bonus: more tasks completed = higher productivity
    task_factor = 1.0 + (min(tasks_count, 5) * 0.1)

    # Interruption penalty
    interruption_penalty = min(interruptions * 0.05, 0.3)

    score = base * duration_factor * task_factor - interruption_penalty

    # Clamp to 0-1
    return max(0.0, min(1.0, score))


def normalize_studyflow_session(raw: RawStudyflowSession) -> NormalizedStudyflowSession:
    """
    Normalize a raw studyflow session into a deterministic normalized record.
    No randomness, no time.now() — uses provided timestamp.

    Args:
        raw: Raw studyflow session from capture layer

    Returns:
        NormalizedStudyflowSession with computed fields
    """
    ts = raw.timestamp
    duration = raw.duration_minutes or 0
    tasks_count = len(raw.tasks_in_session)
    interruptions = raw.interruptions or 0

    return NormalizedStudyflowSession(
        session_id=raw.session_id,
        event_type=raw.event_type,
        user_id=str(raw.user_id),
        timestamp_iso=ts.isoformat(),
        date_key=ts.strftime("%Y-%m-%d"),
        hour_of_day=ts.hour,
        day_of_week=ts.weekday(),
        duration_minutes=duration,
        focus_bucket=_focus_to_bucket(raw.focus_score),
        tasks_count=tasks_count,
        task_ids=sorted([str(tid) for tid in raw.tasks_in_session]),  # Sorted for determinism
        module_id=str(raw.module_context) if raw.module_context else None,
        interruptions=interruptions,
        energy_level=raw.energy_level or "medium",
        is_session_end=raw.event_type == "session_ended",
        productivity_score=_compute_productivity(
            duration, raw.focus_score, tasks_count, interruptions
        ),
    )
