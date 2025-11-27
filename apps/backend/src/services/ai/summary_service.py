"""
Summary Service
Phase 7.3: AI service layer with shared schemas

Generates AI-powered daily and weekly summaries for users.
Currently returns placeholder data; actual AI logic in Phase 7.4+.
"""
import logging
from datetime import datetime
from typing import Optional
from uuid import UUID

from shared.ai import DailySummaryResponse, SummaryHighlight

logger = logging.getLogger(__name__)


class SummaryService:
    """
    Service for generating AI-powered learning summaries.

    Phase 7.2: Stub implementation with placeholder responses.
    Phase 7.4+: Will aggregate real user data and generate insights.
    """

    def __init__(self) -> None:
        """Initialize the summary service."""
        logger.info("SummaryService initialized (stub mode)")

    def get_daily_summary(
        self,
        user_id: Optional[UUID],
    ) -> DailySummaryResponse:
        """
        Generate a daily learning summary for a user.

        Includes:
        - Tasks completed today
        - XP earned
        - Study time
        - Streak status
        - Key achievements and highlights
        - Motivational messaging

        Args:
            user_id: Optional user UUID for personalized summary

        Returns:
            DailySummaryResponse with full daily summary

        Note:
            Phase 7.2: Returns static placeholder data.
            Phase 7.4+: Will aggregate actual user activity data.
        """
        logger.info(f"get_daily_summary called: user_id={user_id}")

        now = datetime.utcnow()
        today = now.strftime("%Y-%m-%d")

        # Build placeholder highlights
        highlights = [
            SummaryHighlight(
                type="achievement",
                title="Learning Streak!",
                description="You've maintained a 5-day learning streak.",
                metric="5 days",
            ),
            SummaryHighlight(
                type="progress",
                title="Module Progress",
                description="You're 60% through the Docker Fundamentals module.",
                metric="60%",
            ),
            SummaryHighlight(
                type="recommendation",
                title="Next Focus Area",
                description="Consider starting the Kubernetes module next.",
                metric=None,
            ),
        ]

        response = DailySummaryResponse(
            date=today,
            greeting="Good progress today! Here's your learning summary.",
            highlights=highlights,
            tasks_completed=3,
            xp_earned=150,
            study_minutes=45,
            streak_days=5,
            motivation_message=(
                "Keep up the momentum! You're making excellent progress "
                "on your DevOps journey."
            ),
            generated_at=now,
        )

        logger.debug(
            f"Returning daily summary: date={response.date}, "
            f"tasks={response.tasks_completed}, xp={response.xp_earned}"
        )
        return response

    def get_weekly_summary(
        self,
        user_id: UUID,
    ) -> dict:
        """
        Generate a weekly learning summary for a user.

        Args:
            user_id: User UUID for personalized summary

        Returns:
            Dictionary with weekly summary data

        Note:
            Phase 7.2: Returns minimal placeholder.
            Phase 7.5+: Will implement full weekly summary.
        """
        logger.info(f"get_weekly_summary called: user_id={user_id}")

        now = datetime.utcnow()

        # Placeholder for future implementation
        return {
            "week_start": "2025-11-24",
            "week_end": "2025-11-30",
            "status": "not_implemented",
            "message": "Weekly summaries will be available in Phase 7.5",
            "generated_at": now.isoformat(),
        }

    def generate_motivation_message(
        self,
        user_id: UUID,
        context: str = "general",
    ) -> str:
        """
        Generate a contextual motivation message.

        Args:
            user_id: User UUID for personalization
            context: Context for the message (general, streak, achievement, etc.)

        Returns:
            Motivational message string

        Note:
            Phase 7.2: Returns static messages.
            Phase 7.4+: Will use LLM for personalized messages.
        """
        logger.info(
            f"generate_motivation_message called: "
            f"user_id={user_id}, context={context}"
        )

        messages = {
            "general": "Keep up the great work! Every step forward counts.",
            "streak": "Amazing streak! Consistency is the key to mastery.",
            "achievement": "Congratulations on your achievement! You're crushing it!",
            "comeback": "Welcome back! Ready to continue your learning journey?",
            "milestone": "You've reached a milestone! Time to celebrate your progress.",
        }

        return messages.get(context, messages["general"])
