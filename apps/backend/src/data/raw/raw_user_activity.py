"""
Phase 8.1 — Raw User Activity Schema
Pure Pydantic models, zero logic.
"""

from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field
from uuid import UUID


class RawUserActivity(BaseModel):
    """
    Raw user activity event for general platform interactions.
    No transformations applied — pure event capture.
    """

    activity_id: str = Field(..., description="Unique activity identifier")
    activity_type: Literal[
        "login",
        "logout",
        "page_view",
        "feature_used",
        "setting_changed",
        "profile_updated",
        "badge_earned",
        "level_up",
        "streak_updated",
        "xp_gained",
    ] = Field(..., description="Type of user activity")
    user_id: UUID = Field(..., description="User who performed the activity")
    timestamp: datetime = Field(..., description="Event timestamp (injected clock)")
    page_path: Optional[str] = Field(
        None, description="Page path if page_view or feature_used"
    )
    feature_name: Optional[str] = Field(
        None, description="Feature name if feature_used"
    )
    value_change: Optional[int] = Field(
        None, description="Numeric value change (e.g., XP amount, streak count)"
    )
    previous_value: Optional[int] = Field(
        None, description="Previous value if applicable"
    )
    new_value: Optional[int] = Field(None, description="New value if applicable")
    device_type: Optional[Literal["desktop", "mobile", "tablet"]] = Field(
        None, description="Device type if tracked"
    )
    session_id: Optional[str] = Field(
        None, description="Browser/app session ID if applicable"
    )
    metadata: dict = Field(
        default_factory=dict, description="Additional unstructured metadata"
    )

    class Config:
        frozen = True  # Immutable raw events
        json_schema_extra = {
            "example": {
                "activity_id": "act_001",
                "activity_type": "xp_gained",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "timestamp": "2025-11-27T10:30:00Z",
                "feature_name": "task_completion",
                "value_change": 50,
                "previous_value": 100,
                "new_value": 150,
                "device_type": "desktop",
                "session_id": "browser_sess_123",
                "metadata": {"source": "task_complete"},
            }
        }
