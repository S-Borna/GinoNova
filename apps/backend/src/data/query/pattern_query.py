"""
Phase 8.5 — Pattern Query Engine
Safe, deterministic read-only queries for study patterns.
Used by AI engines for context building.
"""

from typing import Dict, Any, List

from ..store.memory_store import get_session_events


def query_study_patterns(
    user_id: str,
    days: int = 7,
) -> Dict[str, Any]:
    """
    Query study patterns for a user over recent days.
    Returns deterministic, aggregated results.

    Args:
        user_id: User ID to query
        days: Number of recent days to include

    Returns:
        Dict with study pattern analysis
    """
    events = get_session_events(user_id=user_id)

    # Filter to ended sessions only for meaningful patterns
    ended_sessions = [e for e in events if e.is_session_end]

    if not ended_sessions:
        return {
            "user_id": user_id,
            "has_data": False,
            "patterns": {},
        }

    # Group by date
    by_date: Dict[str, List] = {}
    for session in ended_sessions:
        date = session.date_key
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(session)

    # Get recent days (sorted for determinism)
    sorted_dates = sorted(by_date.keys(), reverse=True)[:days]

    # Calculate daily patterns
    daily_patterns = []
    for date in sorted_dates:
        sessions = by_date[date]
        total_duration = sum(s.duration_minutes for s in sessions)
        avg_focus = sum(
            {"low": 0.2, "medium": 0.5, "high": 0.75, "peak": 0.95}[s.focus_bucket]
            for s in sessions
        ) / len(sessions) if sessions else 0.0
        avg_productivity = sum(s.productivity_score for s in sessions) / len(sessions) if sessions else 0.0

        daily_patterns.append({
            "date": date,
            "sessions": len(sessions),
            "total_duration_minutes": total_duration,
            "avg_focus": round(avg_focus, 3),
            "avg_productivity": round(avg_productivity, 3),
        })

    # Aggregate patterns
    total_sessions = sum(p["sessions"] for p in daily_patterns)
    total_duration = sum(p["total_duration_minutes"] for p in daily_patterns)
    avg_focus_overall = sum(p["avg_focus"] for p in daily_patterns) / len(daily_patterns) if daily_patterns else 0.0
    avg_productivity_overall = sum(p["avg_productivity"] for p in daily_patterns) / len(daily_patterns) if daily_patterns else 0.0

    return {
        "user_id": user_id,
        "has_data": True,
        "days_analyzed": len(daily_patterns),
        "patterns": {
            "daily": daily_patterns,
            "aggregates": {
                "total_sessions": total_sessions,
                "total_duration_minutes": total_duration,
                "avg_sessions_per_day": total_sessions / len(daily_patterns) if daily_patterns else 0.0,
                "avg_duration_per_day": total_duration / len(daily_patterns) if daily_patterns else 0.0,
                "avg_focus": round(avg_focus_overall, 3),
                "avg_productivity": round(avg_productivity_overall, 3),
            },
        },
    }


def query_peak_hours(user_id: str) -> Dict[str, Any]:
    """
    Query peak study hours for a user.
    Identifies when user is most productive.

    Args:
        user_id: User ID to query

    Returns:
        Dict with peak hour analysis
    """
    events = get_session_events(user_id=user_id)
    ended_sessions = [e for e in events if e.is_session_end]

    if not ended_sessions:
        return {
            "user_id": user_id,
            "has_data": False,
            "peak_hours": [],
        }

    # Aggregate by hour
    hour_stats: Dict[int, Dict[str, float]] = {}
    for session in ended_sessions:
        hour = session.hour_of_day
        if hour not in hour_stats:
            hour_stats[hour] = {
                "sessions": 0,
                "total_duration": 0,
                "total_productivity": 0.0,
            }
        hour_stats[hour]["sessions"] += 1
        hour_stats[hour]["total_duration"] += session.duration_minutes
        hour_stats[hour]["total_productivity"] += session.productivity_score

    # Calculate averages and rank
    hour_rankings = []
    for hour, stats in hour_stats.items():
        avg_productivity = stats["total_productivity"] / stats["sessions"] if stats["sessions"] > 0 else 0.0
        avg_duration = stats["total_duration"] / stats["sessions"] if stats["sessions"] > 0 else 0.0

        hour_rankings.append({
            "hour": hour,
            "sessions": stats["sessions"],
            "avg_duration_minutes": round(avg_duration, 2),
            "avg_productivity": round(avg_productivity, 3),
            # Score: weighted combination for ranking
            "score": round(avg_productivity * 0.7 + min(avg_duration / 60, 1) * 0.3, 3),
        })

    # Sort by score descending, then by hour for determinism
    hour_rankings = sorted(hour_rankings, key=lambda x: (-x["score"], x["hour"]))

    # Top 3 peak hours
    peak_hours = hour_rankings[:3]

    return {
        "user_id": user_id,
        "has_data": True,
        "peak_hours": [h["hour"] for h in peak_hours],
        "hour_analysis": hour_rankings,
    }


def query_productivity_trends(
    user_id: str,
    days: int = 14,
) -> Dict[str, Any]:
    """
    Query productivity trends over time.
    Shows how productivity is changing.

    Args:
        user_id: User ID to query
        days: Number of recent days to analyze

    Returns:
        Dict with productivity trend analysis
    """
    events = get_session_events(user_id=user_id)
    ended_sessions = [e for e in events if e.is_session_end]

    if not ended_sessions:
        return {
            "user_id": user_id,
            "has_data": False,
            "trend": "unknown",
            "details": {},
        }

    # Group by date
    by_date: Dict[str, List] = {}
    for session in ended_sessions:
        date = session.date_key
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(session)

    # Get recent days
    sorted_dates = sorted(by_date.keys(), reverse=True)[:days]

    if len(sorted_dates) < 2:
        return {
            "user_id": user_id,
            "has_data": True,
            "trend": "insufficient_data",
            "details": {"days_available": len(sorted_dates)},
        }

    # Calculate daily productivity
    daily_productivity = []
    for date in reversed(sorted_dates):  # Oldest to newest for trend
        sessions = by_date[date]
        avg_prod = sum(s.productivity_score for s in sessions) / len(sessions) if sessions else 0.0
        daily_productivity.append({
            "date": date,
            "productivity": round(avg_prod, 3),
        })

    # Calculate trend (simple linear direction)
    if len(daily_productivity) >= 2:
        first_half = daily_productivity[:len(daily_productivity)//2]
        second_half = daily_productivity[len(daily_productivity)//2:]

        first_avg = sum(d["productivity"] for d in first_half) / len(first_half) if first_half else 0.0
        second_avg = sum(d["productivity"] for d in second_half) / len(second_half) if second_half else 0.0

        if second_avg > first_avg + 0.05:
            trend = "improving"
        elif second_avg < first_avg - 0.05:
            trend = "declining"
        else:
            trend = "stable"
    else:
        trend = "insufficient_data"

    return {
        "user_id": user_id,
        "has_data": True,
        "trend": trend,
        "details": {
            "days_analyzed": len(daily_productivity),
            "daily_productivity": daily_productivity,
            "overall_avg": round(
                sum(d["productivity"] for d in daily_productivity) / len(daily_productivity), 3
            ) if daily_productivity else 0.0,
        },
    }
