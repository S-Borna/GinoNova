"""
AI Engine Response Schemas
Phase 7.2: Extracted schemas for service layer

These schemas define the response models for the AI Engine API.
They are kept separate from the controller to avoid circular imports.

Note: Will be moved to packages/shared in Phase 7.3.
"""
from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


# ============================================================================
# RECOMMENDATION SCHEMAS
# ============================================================================

class TaskRecommendation(BaseModel):
    """Recommended task with confidence score."""
    task_id: str = Field(..., description="UUID of the recommended task")
    title: str = Field(..., description="Task title")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score (0.0-1.0)")
    reason: Optional[str] = Field(None, description="Explanation for the recommendation")


class ModuleRecommendation(BaseModel):
    """Recommended module with confidence score."""
    module_id: str = Field(..., description="UUID of the recommended module")
    name: str = Field(..., description="Module name")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score (0.0-1.0)")
    reason: Optional[str] = Field(None, description="Explanation for the recommendation")


class StudyflowRecommendation(BaseModel):
    """Recommended studyflow session configuration."""
    mode: Literal["pomodoro", "taskrunner", "sprint"] = Field(..., description="Recommended session mode")
    duration: int = Field(..., ge=5, le=120, description="Recommended duration in minutes")
    intensity: Literal["low", "medium", "high"] = Field(..., description="Recommended intensity level")


class Recommendations(BaseModel):
    """Container for all recommendation types."""
    next_task: Optional[TaskRecommendation] = Field(None, description="Recommended next task")
    next_module: Optional[ModuleRecommendation] = Field(None, description="Recommended next module")
    studyflow: Optional[StudyflowRecommendation] = Field(None, description="Recommended studyflow config")


class RecommendationsResponse(BaseModel):
    """Full recommendations response."""
    recommendations: Recommendations
    generated_at: datetime = Field(..., description="When recommendations were generated")
    expires_at: datetime = Field(..., description="When recommendations expire (cache TTL)")


# ============================================================================
# NEXT STEP SCHEMAS
# ============================================================================

class NextStepResponse(BaseModel):
    """Single next action recommendation."""
    action_type: Literal["task", "module", "studyflow", "break"] = Field(..., description="Type of recommended action")
    action_id: Optional[str] = Field(None, description="ID of the recommended item (if applicable)")
    title: str = Field(..., description="Human-readable action title")
    description: str = Field(..., description="Explanation of why this action is recommended")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    estimated_duration: Optional[int] = Field(None, description="Estimated time in minutes")
    generated_at: datetime


# ============================================================================
# DIFFICULTY SCHEMAS
# ============================================================================

class DifficultyEstimate(BaseModel):
    """Task difficulty estimate for a specific user."""
    task_id: str = Field(..., description="UUID of the task")
    base_difficulty: Literal["easy", "medium", "hard"] = Field(..., description="Original task difficulty")
    user_adjusted_difficulty: float = Field(..., ge=1.0, le=5.0, description="User-adjusted difficulty (1.0-5.0)")
    estimated_duration: int = Field(..., ge=1, description="Estimated completion time in minutes")
    success_probability: float = Field(..., ge=0.0, le=1.0, description="Estimated success probability")
    prerequisites_met: bool = Field(..., description="Whether user has completed prerequisites")
    generated_at: datetime


# ============================================================================
# SUMMARY SCHEMAS
# ============================================================================

class SummaryHighlight(BaseModel):
    """A single highlight from the daily summary."""
    type: Literal["achievement", "progress", "streak", "recommendation"] = Field(..., description="Type of highlight")
    title: str = Field(..., description="Highlight title")
    description: str = Field(..., description="Highlight description")
    metric: Optional[str] = Field(None, description="Associated metric value")


class DailySummaryResponse(BaseModel):
    """Daily AI-generated summary for user."""
    date: str = Field(..., description="Date of the summary (YYYY-MM-DD)")
    greeting: str = Field(..., description="Personalized greeting message")
    highlights: list[SummaryHighlight] = Field(default_factory=list, description="Key highlights")
    tasks_completed: int = Field(..., ge=0, description="Number of tasks completed today")
    xp_earned: int = Field(..., ge=0, description="XP earned today")
    study_minutes: int = Field(..., ge=0, description="Total study time in minutes")
    streak_days: int = Field(..., ge=0, description="Current streak in days")
    motivation_message: str = Field(..., description="AI-generated motivation message")
    generated_at: datetime


# ============================================================================
# STATUS SCHEMA
# ============================================================================

class AIStatusResponse(BaseModel):
    """AI Engine status check response."""
    phase: str
    feature: str
    status: str
    engines: dict[str, str]
    cache_enabled: bool
    fallback_mode: str
