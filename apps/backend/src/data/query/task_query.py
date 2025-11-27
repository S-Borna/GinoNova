"""
Phase 8.5 — Task Query Engine
Safe, deterministic read-only queries for task data.
Used by AI engines for context building.
"""

from typing import Dict, Any, List, Optional

from ..store.memory_store import get_task_events
from ..store.indexes import get_events_by_module, get_events_by_date


def query_user_tasks(
    user_id: str,
    limit: int = 100,
    date_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Query task events for a user.
    Returns deterministic, sorted results.
    
    Args:
        user_id: User ID to query
        limit: Max events to return
        date_key: Optional date filter (YYYY-MM-DD)
        
    Returns:
        Dict with task events and metadata
    """
    events = get_task_events(user_id=user_id, limit=limit)
    
    if date_key:
        events = [e for e in events if e.date_key == date_key]
    
    # Sort for determinism: by timestamp desc, then event_id
    events = sorted(events, key=lambda e: (e.timestamp_iso, e.event_id), reverse=True)
    
    return {
        "user_id": user_id,
        "total_events": len(events),
        "date_filter": date_key,
        "events": [e.model_dump() for e in events[:limit]],
    }


def query_task_completions(
    user_id: str,
    days: int = 7,
) -> Dict[str, Any]:
    """
    Query task completion statistics for a user.
    Aggregates over recent days.
    
    Args:
        user_id: User ID to query
        days: Number of recent days to include
        
    Returns:
        Dict with completion stats
    """
    events = get_task_events(user_id=user_id)
    
    # Group by date
    by_date: Dict[str, Dict[str, int]] = {}
    for event in events:
        date = event.date_key
        if date not in by_date:
            by_date[date] = {"completions": 0, "failures": 0, "total": 0}
        by_date[date]["total"] += 1
        if event.is_completion:
            by_date[date]["completions"] += 1
        if event.is_failure:
            by_date[date]["failures"] += 1
    
    # Sort dates descending
    sorted_dates = sorted(by_date.keys(), reverse=True)[:days]
    
    daily_stats = [
        {
            "date": date,
            **by_date[date],
            "completion_rate": (
                by_date[date]["completions"] / 
                (by_date[date]["completions"] + by_date[date]["failures"])
                if (by_date[date]["completions"] + by_date[date]["failures"]) > 0
                else 0.0
            ),
        }
        for date in sorted_dates
    ]
    
    total_completions = sum(d["completions"] for d in daily_stats)
    total_failures = sum(d["failures"] for d in daily_stats)
    total_attempts = total_completions + total_failures
    
    return {
        "user_id": user_id,
        "days_included": len(daily_stats),
        "daily_stats": daily_stats,
        "totals": {
            "completions": total_completions,
            "failures": total_failures,
            "attempts": total_attempts,
            "completion_rate": (
                total_completions / total_attempts if total_attempts > 0 else 0.0
            ),
        },
    }


def query_task_by_module(
    user_id: str,
    module_id: str,
) -> Dict[str, Any]:
    """
    Query task events for a specific module.
    
    Args:
        user_id: User ID to query
        module_id: Module ID to filter by
        
    Returns:
        Dict with module task stats
    """
    result = get_events_by_module(module_id=module_id, user_id=user_id)
    task_events = result["task_events"]
    
    completions = sum(1 for e in task_events if e.is_completion)
    failures = sum(1 for e in task_events if e.is_failure)
    total_xp = sum(e.xp_awarded for e in task_events)
    total_duration = sum(e.duration_minutes or 0 for e in task_events)
    
    # Difficulty distribution
    difficulty_dist = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
    for event in task_events:
        difficulty_dist[event.difficulty_bucket] += 1
    
    return {
        "user_id": user_id,
        "module_id": module_id,
        "total_events": len(task_events),
        "completions": completions,
        "failures": failures,
        "completion_rate": completions / (completions + failures) if (completions + failures) > 0 else 0.0,
        "total_xp": total_xp,
        "total_duration_minutes": total_duration,
        "difficulty_distribution": difficulty_dist,
    }


def get_task_summary(user_id: str) -> Dict[str, Any]:
    """
    Get a comprehensive task summary for a user.
    Used by AI engines for context building.
    
    Args:
        user_id: User ID to summarize
        
    Returns:
        Dict with comprehensive task summary
    """
    events = get_task_events(user_id=user_id)
    
    if not events:
        return {
            "user_id": user_id,
            "has_data": False,
            "total_events": 0,
            "summary": {},
        }
    
    # Basic stats
    completions = sum(1 for e in events if e.is_completion)
    failures = sum(1 for e in events if e.is_failure)
    total_xp = sum(e.xp_awarded for e in events)
    total_duration = sum(e.duration_minutes or 0 for e in events)
    
    # Time distribution
    hour_dist: Dict[int, int] = {}
    for event in events:
        hour_dist[event.hour_of_day] = hour_dist.get(event.hour_of_day, 0) + 1
    
    # Find peak hour (deterministic tie-breaker: lower hour wins)
    sorted_hours = sorted(hour_dist.items(), key=lambda x: (-x[1], x[0]))
    peak_hour = sorted_hours[0][0] if sorted_hours else 0
    
    # Day distribution
    day_dist: Dict[int, int] = {}
    for event in events:
        day_dist[event.day_of_week] = day_dist.get(event.day_of_week, 0) + 1
    
    sorted_days = sorted(day_dist.items(), key=lambda x: (-x[1], x[0]))
    peak_day = sorted_days[0][0] if sorted_days else 0
    
    # Difficulty preference
    diff_dist = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
    for event in events:
        diff_dist[event.difficulty_bucket] += 1
    
    sorted_diff = sorted(diff_dist.items(), key=lambda x: (-x[1], x[0]))
    preferred_difficulty = sorted_diff[0][0] if sorted_diff else "medium"
    
    # Unique metrics
    unique_tasks = len(set(e.task_id for e in events))
    unique_modules = len(set(e.module_id for e in events if e.module_id))
    unique_dates = len(set(e.date_key for e in events))
    
    return {
        "user_id": user_id,
        "has_data": True,
        "total_events": len(events),
        "summary": {
            "completions": completions,
            "failures": failures,
            "completion_rate": completions / (completions + failures) if (completions + failures) > 0 else 0.0,
            "total_xp": total_xp,
            "total_duration_minutes": total_duration,
            "avg_duration_minutes": total_duration / len(events) if events else 0.0,
            "unique_tasks": unique_tasks,
            "unique_modules": unique_modules,
            "active_days": unique_dates,
            "peak_hour": peak_hour,
            "peak_day": peak_day,
            "preferred_difficulty": preferred_difficulty,
            "difficulty_distribution": diff_dist,
        },
    }
