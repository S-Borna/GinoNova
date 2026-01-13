"""
Analytics Service - Real analytics tracking and aggregation
Replaces mock data with actual database-backed analytics
"""
from datetime import datetime, timedelta, date, timezone
from typing import Optional, List, Dict, Any
from uuid import UUID
from sqlalchemy import func, and_, desc
from sqlalchemy.orm import Session
from collections import defaultdict
import logging

from src.db.models import User, Progress, StudyflowSession, AIUsageLog, ExamResult
from src.db.models_analytics import AnalyticsEvent, DailyStats, UserInsights, ModuleAnalytics

logger = logging.getLogger(__name__)


class AnalyticsService:
    """Service for tracking and aggregating user analytics"""

    def __init__(self, db: Session):
        self.db = db

    # =========================================================================
    # EVENT TRACKING
    # =========================================================================

    def track_event(
        self,
        user_id: UUID,
        event_type: str,
        event_data: Dict[str, Any] = None,
        session_id: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None
    ) -> AnalyticsEvent:
        """
        Track an analytics event in the database
        """
        event = AnalyticsEvent(
            user_id=user_id,
            event_type=event_type,
            event_data=event_data or {},
            session_id=session_id,
            ip_address=ip_address,
            user_agent=user_agent,
            created_at=datetime.utcnow()
        )

        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)

        logger.info(f"Event tracked: {event_type} for user {user_id}")
        return event

    # =========================================================================
    # DAILY STATS AGGREGATION
    # =========================================================================

    def update_daily_stats(self, user_id: UUID, target_date: date = None) -> DailyStats:
        """
        Update or create daily stats for a user
        Aggregates data from various sources
        """
        if target_date is None:
            target_date = datetime.utcnow().date()

        # Get or create daily stats record
        daily_stats = self.db.query(DailyStats).filter(
            and_(
                DailyStats.user_id == user_id,
                DailyStats.date == target_date
            )
        ).first()

        if not daily_stats:
            daily_stats = DailyStats(
                user_id=user_id,
                date=target_date
            )
            self.db.add(daily_stats)

        # Calculate date range for queries
        day_start = datetime.combine(target_date, datetime.min.time())
        day_end = day_start + timedelta(days=1)

        # Study minutes from studyflow sessions
        study_minutes = self.db.query(
            func.sum(StudyflowSession.actual_duration)
        ).filter(
            and_(
                StudyflowSession.user_id == user_id,
                StudyflowSession.started_at >= day_start,
                StudyflowSession.started_at < day_end,
                StudyflowSession.status == 'completed'
            )
        ).scalar() or 0

        # Tasks completed
        tasks_completed = self.db.query(func.count(Progress.id)).filter(
            and_(
                Progress.user_id == user_id,
                Progress.task_id.isnot(None),
                Progress.status == 'completed',
                Progress.completed_at >= day_start,
                Progress.completed_at < day_end
            )
        ).scalar() or 0

        # Tasks attempted (started but not necessarily completed)
        tasks_attempted = self.db.query(func.count(Progress.id)).filter(
            and_(
                Progress.user_id == user_id,
                Progress.task_id.isnot(None),
                Progress.created_at >= day_start,
                Progress.created_at < day_end
            )
        ).scalar() or 0

        # XP earned
        xp_earned = self.db.query(func.sum(Progress.xp_earned)).filter(
            and_(
                Progress.user_id == user_id,
                Progress.completed_at >= day_start,
                Progress.completed_at < day_end
            )
        ).scalar() or 0

        # Study sessions count
        sessions_count = self.db.query(func.count(StudyflowSession.id)).filter(
            and_(
                StudyflowSession.user_id == user_id,
                StudyflowSession.started_at >= day_start,
                StudyflowSession.started_at < day_end
            )
        ).scalar() or 0

        # AI calls
        ai_calls = self.db.query(func.count(AIUsageLog.id)).filter(
            and_(
                AIUsageLog.user_id == user_id,
                AIUsageLog.created_at >= day_start,
                AIUsageLog.created_at < day_end
            )
        ).scalar() or 0

        # Modules touched (unique module IDs worked on)
        modules_touched = self.db.query(Progress.module_id).filter(
            and_(
                Progress.user_id == user_id,
                Progress.module_id.isnot(None),
                Progress.updated_at >= day_start,
                Progress.updated_at < day_end
            )
        ).distinct().all()

        module_ids = [str(m[0]) for m in modules_touched if m[0]]

        # Update stats
        daily_stats.study_minutes = study_minutes
        daily_stats.tasks_completed = tasks_completed
        daily_stats.tasks_attempted = tasks_attempted
        daily_stats.xp_earned = xp_earned
        daily_stats.sessions_count = sessions_count
        daily_stats.ai_calls = ai_calls
        daily_stats.modules_touched = module_ids
        daily_stats.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(daily_stats)

        return daily_stats

    def get_daily_stats(
        self,
        user_id: UUID,
        days: int = 30
    ) -> List[DailyStats]:
        """
        Get daily stats for a user for the last N days
        """
        end_date = datetime.utcnow().date()
        start_date = end_date - timedelta(days=days)

        stats = self.db.query(DailyStats).filter(
            and_(
                DailyStats.user_id == user_id,
                DailyStats.date >= start_date,
                DailyStats.date <= end_date
            )
        ).order_by(DailyStats.date.asc()).all()

        return stats

    # =========================================================================
    # USER ANALYTICS
    # =========================================================================

    def get_user_analytics_summary(self, user_id: UUID) -> Dict[str, Any]:
        """
        Get comprehensive analytics summary for a user
        """
        # Get user
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return {}

        # Total study hours from all completed sessions
        total_study_minutes = self.db.query(
            func.sum(StudyflowSession.actual_duration)
        ).filter(
            and_(
                StudyflowSession.user_id == user_id,
                StudyflowSession.status == 'completed'
            )
        ).scalar() or 0

        total_study_hours = round(total_study_minutes / 60.0, 1)

        # Tasks completed
        tasks_completed = self.db.query(func.count(Progress.id)).filter(
            and_(
                Progress.user_id == user_id,
                Progress.task_id.isnot(None),
                Progress.status == 'completed'
            )
        ).scalar() or 0

        # Average session length
        avg_session = self.db.query(
            func.avg(StudyflowSession.actual_duration)
        ).filter(
            and_(
                StudyflowSession.user_id == user_id,
                StudyflowSession.status == 'completed',
                StudyflowSession.actual_duration.isnot(None)
            )
        ).scalar() or 0

        # Weekly activity (last 7 days)
        weekly_activity = []
        for i in range(6, -1, -1):
            day_date = datetime.utcnow().date() - timedelta(days=i)
            stats = self.db.query(DailyStats).filter(
                and_(
                    DailyStats.user_id == user_id,
                    DailyStats.date == day_date
                )
            ).first()

            weekly_activity.append(stats.study_minutes if stats else 0)

        # Favorite study time (morning, afternoon, evening, night)
        favorite_time = self._calculate_favorite_study_time(user_id)

        return {
            "total_study_hours": total_study_hours,
            "tasks_completed": tasks_completed,
            "current_streak": user.current_streak,
            "longest_streak": user.longest_streak,
            "favorite_time": favorite_time,
            "weekly_activity": weekly_activity,
            "avg_session_length": int(avg_session)
        }

    def _calculate_favorite_study_time(self, user_id: UUID) -> str:
        """
        Calculate user's favorite study time based on session start times
        """
        sessions = self.db.query(StudyflowSession.started_at).filter(
            StudyflowSession.user_id == user_id
        ).all()

        if not sessions:
            return "evening"

        time_buckets = {"morning": 0, "afternoon": 0, "evening": 0, "night": 0}

        for session in sessions:
            hour = session[0].hour
            if 6 <= hour < 12:
                time_buckets["morning"] += 1
            elif 12 <= hour < 17:
                time_buckets["afternoon"] += 1
            elif 17 <= hour < 22:
                time_buckets["evening"] += 1
            else:
                time_buckets["night"] += 1

        return max(time_buckets, key=time_buckets.get)

    # =========================================================================
    # ACTIVITY HEATMAP
    # =========================================================================

    def get_activity_heatmap(self, user_id: UUID, weeks: int = 12) -> Dict[str, int]:
        """
        Get activity heatmap data (like GitHub contribution graph)
        Returns dict of date -> activity_count
        """
        end_date = datetime.utcnow().date()
        start_date = end_date - timedelta(weeks=weeks)

        stats = self.db.query(DailyStats).filter(
            and_(
                DailyStats.user_id == user_id,
                DailyStats.date >= start_date,
                DailyStats.date <= end_date
            )
        ).all()

        heatmap = {}
        for stat in stats:
            date_str = stat.date.isoformat()
            # Calculate activity score (tasks + sessions)
            activity_score = stat.tasks_completed + stat.sessions_count
            heatmap[date_str] = activity_score

        return heatmap

    # =========================================================================
    # LEADERBOARD
    # =========================================================================

    def get_leaderboard(
        self,
        period: str = "week",
        metric: str = "xp",
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Get leaderboard based on various metrics
        """
        # Calculate date range
        now = datetime.utcnow()
        if period == "day":
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif period == "week":
            start_date = now - timedelta(days=7)
        elif period == "month":
            start_date = now - timedelta(days=30)
        else:  # all
            start_date = datetime(2020, 1, 1)

        if metric == "xp":
            # Get users with most XP earned in period
            results = self.db.query(
                User.id,
                User.full_name,
                User.email,
                User.avatar_url,
                func.sum(Progress.xp_earned).label('total')
            ).join(
                Progress, Progress.user_id == User.id
            ).filter(
                Progress.completed_at >= start_date
            ).group_by(
                User.id
            ).order_by(
                desc('total')
            ).limit(limit).all()

        elif metric == "tasks":
            # Get users with most tasks completed
            results = self.db.query(
                User.id,
                User.full_name,
                User.email,
                User.avatar_url,
                func.count(Progress.id).label('total')
            ).join(
                Progress, Progress.user_id == User.id
            ).filter(
                and_(
                    Progress.task_id.isnot(None),
                    Progress.status == 'completed',
                    Progress.completed_at >= start_date
                )
            ).group_by(
                User.id
            ).order_by(
                desc('total')
            ).limit(limit).all()

        elif metric == "streak":
            # Get users with longest current streak
            results = self.db.query(
                User.id,
                User.full_name,
                User.email,
                User.avatar_url,
                User.current_streak.label('total')
            ).filter(
                User.current_streak > 0
            ).order_by(
                desc(User.current_streak)
            ).limit(limit).all()

        elif metric == "hours":
            # Get users with most study hours
            results = self.db.query(
                User.id,
                User.full_name,
                User.email,
                User.avatar_url,
                func.sum(StudyflowSession.actual_duration).label('total')
            ).join(
                StudyflowSession, StudyflowSession.user_id == User.id
            ).filter(
                and_(
                    StudyflowSession.status == 'completed',
                    StudyflowSession.started_at >= start_date
                )
            ).group_by(
                User.id
            ).order_by(
                desc('total')
            ).limit(limit).all()

        else:
            return []

        # Format results
        leaderboard = []
        for idx, result in enumerate(results, 1):
            leaderboard.append({
                "rank": idx,
                "user_id": str(result.id),
                "name": result.full_name or result.email.split('@')[0],
                "avatar_url": result.avatar_url,
                "value": int(result.total) if result.total else 0
            })

        return leaderboard

    # =========================================================================
    # ADMIN ANALYTICS
    # =========================================================================

    def get_platform_overview(self) -> Dict[str, Any]:
        """
        Get platform-wide analytics overview for admin
        """
        now = datetime.utcnow()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        week_ago = now - timedelta(days=7)

        # Total users
        total_users = self.db.query(func.count(User.id)).scalar() or 0

        # Active today
        active_today = self.db.query(func.count(User.id)).filter(
            User.last_activity_at >= today_start
        ).scalar() or 0

        # Active this week
        active_week = self.db.query(func.count(User.id)).filter(
            User.last_activity_at >= week_ago
        ).scalar() or 0

        # Total study hours
        total_study_minutes = self.db.query(
            func.sum(StudyflowSession.actual_duration)
        ).filter(
            StudyflowSession.status == 'completed'
        ).scalar() or 0

        total_study_hours = round(total_study_minutes / 60.0, 1)

        # Tasks completed today
        tasks_today = self.db.query(func.count(Progress.id)).filter(
            and_(
                Progress.task_id.isnot(None),
                Progress.status == 'completed',
                Progress.completed_at >= today_start
            )
        ).scalar() or 0

        # Popular modules (most active users)
        popular_modules = self.db.query(
            Progress.module_id,
            func.count(func.distinct(Progress.user_id)).label('user_count')
        ).filter(
            and_(
                Progress.module_id.isnot(None),
                Progress.updated_at >= week_ago
            )
        ).group_by(
            Progress.module_id
        ).order_by(
            desc('user_count')
        ).limit(5).all()

        return {
            "total_users": total_users,
            "active_today": active_today,
            "active_this_week": active_week,
            "total_study_hours": total_study_hours,
            "tasks_completed_today": tasks_today,
            "popular_modules": [str(m[0]) for m in popular_modules if m[0]],
            "conversion_rate": 0  # Would need payment data
        }

    def get_exam_statistics(self) -> Dict[str, Any]:
        """
        Get exam/tenta statistics for admin dashboard
        """
        # Total exams taken
        total_exams = self.db.query(func.count(ExamResult.id)).filter(
            ExamResult.completed == True
        ).scalar() or 0

        # Average score
        avg_score = self.db.query(
            func.avg(ExamResult.score_percent)
        ).filter(
            ExamResult.completed == True
        ).scalar() or 0.0

        # Pass rate (assuming 50% is passing)
        passed = self.db.query(func.count(ExamResult.id)).filter(
            and_(
                ExamResult.completed == True,
                ExamResult.score_percent >= 50
            )
        ).scalar() or 0

        pass_rate = round((passed / total_exams * 100), 1) if total_exams > 0 else 0

        # Recent exams (last 10)
        recent_exams = self.db.query(ExamResult).filter(
            ExamResult.completed == True
        ).order_by(
            desc(ExamResult.completed_at)
        ).limit(10).all()

        recent_list = []
        for exam in recent_exams:
            user = self.db.query(User).filter(User.id == exam.user_id).first()
            recent_list.append({
                "user_name": user.full_name if user else "Unknown",
                "score": round(exam.score_percent, 1),
                "questions": exam.question_count,
                "duration": exam.duration_minutes,
                "completed_at": exam.completed_at.isoformat()
            })

        return {
            "total_exams": total_exams,
            "average_score": round(avg_score, 1),
            "pass_rate": pass_rate,
            "recent_exams": recent_list
        }
