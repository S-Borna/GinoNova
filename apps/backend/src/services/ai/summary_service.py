"""
Summary Service
Phase 7.5: AI service layer with rule engine integration

Generates AI-powered daily and weekly summaries using the
deterministic rule engine's compute_daily_highlights function.
"""
import logging
from datetime import datetime
from typing import Optional
from uuid import UUID

from shared.ai import (
    DailySummaryResponse,
    SummaryHighlight,
    # Engine imports
    compute_daily_highlights,
    UserContext,
    ProgressData,
)

logger = logging.getLogger(__name__)


class SummaryService:
    """
    Service for generating AI-powered learning summaries.

    Phase 7.5: Uses compute_daily_highlights from the rule engine
    to generate personalized, deterministic summaries.
    """

    def __init__(self) -> None:
        """Initialize the summary service."""
        logger.info("SummaryService initialized (engine=active)")

    def get_daily_summary(
        self,
        user_id: Optional[UUID],
    ) -> DailySummaryResponse:
        """
        Generate a daily learning summary for a user.

        Uses the rule engine to compute highlights based on:
        - Tasks completed today
        - XP earned
        - Study time
        - Streak status
        - Module progress
        - Achievements

        Args:
            user_id: Optional user UUID for personalized summary

        Returns:
            DailySummaryResponse with full daily summary
        """
        logger.info(f"get_daily_summary called: user_id={user_id}")

        now = datetime.utcnow()
        today = now.strftime("%Y-%m-%d")

        # Build context and progress data
        user_ctx = self._build_user_context(user_id)
        progress = self._get_progress_data(user_id)

        # Compute highlights using rule engine
        raw_highlights = compute_daily_highlights(user_ctx, progress)

        logger.debug(f"Computed {len(raw_highlights)} highlights")

        # Convert engine highlights to schema highlights
        highlights = [
            SummaryHighlight(
                type=h["type"],
                title=h["title"],
                description=h["description"],
                metric=h.get("metric"),
            )
            for h in raw_highlights
        ]

        # Generate greeting based on time and progress
        greeting = self._generate_greeting(user_ctx, progress)

        # Generate motivation message
        motivation = self._generate_motivation(user_ctx, progress)

        response = DailySummaryResponse(
            date=today,
            greeting=greeting,
            highlights=highlights,
            tasks_completed=progress.get("tasks_completed_today", 0),
            xp_earned=progress.get("xp_earned_today", 0),
            study_minutes=progress.get("study_minutes_today", 0),
            streak_days=progress.get("streak_days", 0),
            motivation_message=motivation,
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
            Phase 7.5: Returns computed summary based on weekly progress.
            Full weekly summary schema in future phases.
        """
        logger.info(f"get_weekly_summary called: user_id={user_id}")

        now = datetime.utcnow()
        progress = self._get_weekly_progress_data(user_id)

        # Aggregate weekly stats
        total_tasks = progress.get("tasks_completed_week", 0)
        total_xp = progress.get("xp_earned_week", 0)
        total_minutes = progress.get("study_minutes_week", 0)
        streak = progress.get("streak_days", 0)

        # Determine week quality
        if total_tasks >= 15 and total_minutes >= 300:
            quality = "exceptional"
            message = "Outstanding week! You're making incredible progress."
        elif total_tasks >= 10 or total_minutes >= 180:
            quality = "great"
            message = "Great week! Keep building on this momentum."
        elif total_tasks >= 5 or total_minutes >= 60:
            quality = "good"
            message = "Solid progress this week. Every step counts!"
        else:
            quality = "needs_improvement"
            message = "Room to grow! Try setting smaller daily goals next week."

        return {
            "week_start": "2025-11-24",
            "week_end": "2025-11-30",
            "status": "computed",
            "quality": quality,
            "tasks_completed": total_tasks,
            "xp_earned": total_xp,
            "study_minutes": total_minutes,
            "streak_days": streak,
            "message": message,
            "generated_at": now.isoformat(),
        }

    def generate_motivation_message(
        self,
        user_id: UUID,
        context: str = "general",
    ) -> str:
        """
        Generate a contextual motivation message.

        Uses deterministic rules based on context type.

        Args:
            user_id: User UUID for personalization
            context: Context for the message

        Returns:
            Motivational message string
        """
        logger.info(
            f"generate_motivation_message called: "
            f"user_id={user_id}, context={context}"
        )

        user_ctx = self._build_user_context(user_id)
        streak = user_ctx.get("streak_days", 0)
        xp = user_ctx.get("xp", 0)

        # Context-based messages with personalization
        messages = {
            "general": self._general_motivation(streak, xp),
            "streak": self._streak_motivation(streak),
            "achievement": "Congratulations on your achievement! You're crushing it!",
            "comeback": "Welcome back! Ready to continue your learning journey?",
            "milestone": "You've reached a milestone! Time to celebrate your progress.",
            "morning": "Fresh start to the day! Great time for focused learning.",
            "evening": "Wind down with some light review. Consistency beats intensity.",
        }

        return messages.get(context, messages["general"])

    def _generate_greeting(
        self,
        user_ctx: UserContext,
        progress: ProgressData,
    ) -> str:
        """Generate personalized greeting based on context."""
        time_of_day = user_ctx.get("time_of_day", "afternoon")
        tasks = progress.get("tasks_completed_today", 0)

        greetings = {
            "morning": "Good morning! Ready to learn something new?",
            "afternoon": "Good afternoon! Here's your progress update.",
            "evening": "Good evening! Let's review your day.",
            "night": "Working late? Here's what you've accomplished.",
        }

        base_greeting = greetings.get(time_of_day, "Hello!")

        if tasks >= 5:
            return f"{base_greeting} Incredible productivity today!"
        elif tasks >= 3:
            return f"{base_greeting} Great progress so far!"
        elif tasks > 0:
            return f"{base_greeting} You're making progress!"
        else:
            return f"{base_greeting}"

    def _generate_motivation(
        self,
        user_ctx: UserContext,
        progress: ProgressData,
    ) -> str:
        """Generate motivation message based on progress."""
        streak = progress.get("streak_days", 0)
        tasks = progress.get("tasks_completed_today", 0)
        xp = progress.get("xp_earned_today", 0)

        if streak >= 7 and tasks >= 3:
            return "You're on fire! Your consistency is paying off. Keep this momentum going!"
        elif streak >= 7:
            return f"Amazing {streak}-day streak! Consistency is the key to mastery."
        elif tasks >= 5:
            return "Productivity champion! You've crushed it today."
        elif xp >= 200:
            return "Great XP gains! You're leveling up fast."
        elif tasks >= 1:
            return "Every task completed is a step forward. Keep it up!"
        else:
            return "Ready to start? Even 15 minutes of focused learning makes a difference."

    def _general_motivation(self, streak: int, xp: int) -> str:
        """Generate general motivation based on stats."""
        if streak >= 14:
            return f"Two weeks strong! Your {streak}-day streak shows true dedication."
        elif streak >= 7:
            return "A full week of learning! You're building great habits."
        elif xp >= 5000:
            return "Over 5000 XP! You're becoming a DevOps expert."
        elif xp >= 1000:
            return "Solid progress! Keep building your knowledge base."
        else:
            return "Keep up the great work! Every step forward counts."

    def _streak_motivation(self, streak: int) -> str:
        """Generate streak-specific motivation."""
        if streak >= 30:
            return f"Legendary {streak}-day streak! You're in the top tier of learners."
        elif streak >= 14:
            return f"Two weeks and counting! {streak} days of dedication."
        elif streak >= 7:
            return f"One week milestone! {streak} days of consistent learning."
        elif streak >= 3:
            return f"{streak} days in a row! Building momentum."
        elif streak > 0:
            return "Streak started! Come back tomorrow to keep it going."
        else:
            return "Start a new streak today! Consistency beats intensity."

    def _build_user_context(self, user_id: Optional[UUID]) -> UserContext:
        """Build user context for summary generation."""
        hour = datetime.utcnow().hour
        if hour < 12:
            time_of_day = "morning"
        elif hour < 18:
            time_of_day = "afternoon"
        elif hour < 21:
            time_of_day = "evening"
        else:
            time_of_day = "night"

        return {
            "user_id": str(user_id) if user_id else "anonymous",
            "skill_level": "intermediate",
            "streak_days": 5,
            "xp": 1500,
            "completed_module_ids": ["docker-basics", "linux-fundamentals"],
            "completed_task_ids": ["task-001", "task-002", "task-003"],
            "focus_energy": "high" if hour < 16 else "medium",
            "time_of_day": time_of_day,
            "available_minutes": 45,
        }

    def _get_progress_data(self, user_id: Optional[UUID]) -> ProgressData:
        """
        Get daily progress data for a user.

        Phase 7.5: Returns deterministic sample data.
        Phase 7.6+: Will query from DB.
        """
        # Deterministic sample data
        return {
            "tasks_completed_today": 3,
            "xp_earned_today": 150,
            "study_minutes_today": 45,
            "streak_days": 5,
            "modules_in_progress": [
                {
                    "id": "kubernetes-101",
                    "name": "Introduction to Kubernetes",
                    "total_tasks": 12,
                    "completed_tasks": 4,
                },
                {
                    "id": "ci-cd-pipelines",
                    "name": "CI/CD Pipeline Fundamentals",
                    "total_tasks": 10,
                    "completed_tasks": 6,
                },
            ],
            "recent_achievements": [
                "Completed Docker Fundamentals module",
            ],
        }

    def _get_weekly_progress_data(self, user_id: UUID) -> dict:
        """Get weekly aggregated progress data."""
        return {
            "tasks_completed_week": 18,
            "xp_earned_week": 850,
            "study_minutes_week": 240,
            "streak_days": 5,
        }
