"""
Phase 8.2 — User Activity Normalizer
Deterministic normalization of raw user activity events.
"""

from typing import Literal, Optional
from pydantic import BaseModel, Field

from ..raw.raw_user_activity import RawUserActivity


class NormalizedUserActivity(BaseModel):
    """
    Normalized user activity with computed fields and strict typing.
    Deterministic transformation from raw events.
    """

    activity_id: str = Field(..., description="Original activity identifier")
    activity_type: str = Field(..., description="Normalized activity type")
    activity_category: Literal["auth", "navigation", "progression", "engagement"] = Field(
        ..., description="Activity category for grouping"
    )
    user_id: str = Field(..., description="User ID as string")
    timestamp_iso: str = Field(..., description="ISO8601 timestamp string")
    date_key: str = Field(..., description="Date key YYYY-MM-DD for indexing")
    hour_of_day: int = Field(..., ge=0, le=23, description="Hour of day 0-23")
    day_of_week: int = Field(..., ge=0, le=6, description="Day of week 0=Mon, 6=Sun")
    page_path: Optional[str] = Field(None, description="Normalized page path")
    feature_name: Optional[str] = Field(None, description="Feature name")
    value_delta: int = Field(default=0, description="Value change amount")
    device_type: str = Field(default="unknown", description="Device type")
    session_id: Optional[str] = Field(None, description="Session ID if available")
    is_xp_event: bool = Field(..., description="Whether this involves XP change")
    is_milestone: bool = Field(..., description="Whether this is a milestone event")

    class Config:
        frozen = True


def _categorize_activity(
    activity_type: str,
) -> Literal["auth", "navigation", "progression", "engagement"]:
    """
    Categorize activity type into high-level category.
    Deterministic mapping.
    """
    auth_types = {"login", "logout"}
    navigation_types = {"page_view", "feature_used"}
    progression_types = {"xp_gained", "level_up", "badge_earned", "streak_updated"}

    if activity_type in auth_types:
        return "auth"
    elif activity_type in navigation_types:
        return "navigation"
    elif activity_type in progression_types:
        return "progression"
    else:
        return "engagement"


def _is_milestone_event(activity_type: str) -> bool:
    """
    Determine if activity is a milestone event.
    Deterministic check.
    """
    milestone_types = {"badge_earned", "level_up"}
    return activity_type in milestone_types


def normalize_user_activity(raw: RawUserActivity) -> NormalizedUserActivity:
    """
    Normalize a raw user activity into a deterministic normalized record.
    No randomness, no time.now() — uses provided timestamp.

    Args:
        raw: Raw user activity from capture layer

    Returns:
        NormalizedUserActivity with computed fields
    """
    ts = raw.timestamp

    return NormalizedUserActivity(
        activity_id=raw.activity_id,
        activity_type=raw.activity_type,
        activity_category=_categorize_activity(raw.activity_type),
        user_id=str(raw.user_id),
        timestamp_iso=ts.isoformat(),
        date_key=ts.strftime("%Y-%m-%d"),
        hour_of_day=ts.hour,
        day_of_week=ts.weekday(),
        page_path=raw.page_path,
        feature_name=raw.feature_name,
        value_delta=raw.value_change or 0,
        device_type=raw.device_type or "unknown",
        session_id=raw.session_id,
        is_xp_event=raw.activity_type == "xp_gained",
        is_milestone=_is_milestone_event(raw.activity_type),
    )
