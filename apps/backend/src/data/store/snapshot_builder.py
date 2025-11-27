"""
Phase 8.3 + 8.6 — Snapshot Builder
Periodic materializations for AI context.
Daily snapshot generation.
"""

from typing import Dict, Any, Optional, List
from threading import Lock

from .memory_store import get_task_events, get_session_events, get_activity_events


# Snapshot storage
_daily_snapshots: Dict[str, Dict[str, Any]] = {}
_snapshot_lock = Lock()


def build_daily_snapshot(user_id: str, date_key: str) -> Dict[str, Any]:
    """
    Build a daily snapshot for a user on a specific date.
    Aggregates task stats, difficulty stats, studyflow patterns, and XP deltas.
    Stores in memory_store under daily_snapshots.
    
    Args:
        user_id: User ID to build snapshot for
        date_key: Date in YYYY-MM-DD format
        
    Returns:
        Daily snapshot dict
    """
    # Get all events for this user
    task_events = get_task_events(user_id=user_id)
    session_events = get_session_events(user_id=user_id)
    activity_events = get_activity_events(user_id=user_id)
    
    # Filter to the specific date
    task_events = [e for e in task_events if e.date_key == date_key]
    session_events = [e for e in session_events if e.date_key == date_key]
    activity_events = [e for e in activity_events if e.date_key == date_key]
    
    # Build task stats
    task_stats = _build_task_stats(task_events)
    
    # Build difficulty stats
    difficulty_stats = _build_difficulty_stats(task_events)
    
    # Build studyflow patterns
    studyflow_patterns = _build_studyflow_patterns(session_events)
    
    # Build XP deltas
    xp_deltas = _build_xp_deltas(task_events, activity_events)
    
    snapshot = {
        "user_id": user_id,
        "date_key": date_key,
        "task_stats": task_stats,
        "difficulty_stats": difficulty_stats,
        "studyflow_patterns": studyflow_patterns,
        "xp_deltas": xp_deltas,
        "event_counts": {
            "tasks": len(task_events),
            "sessions": len(session_events),
            "activities": len(activity_events),
        },
    }
    
    # Store snapshot
    snapshot_key = f"{user_id}:{date_key}"
    with _snapshot_lock:
        _daily_snapshots[snapshot_key] = snapshot
    
    return snapshot


def _build_task_stats(task_events: List) -> Dict[str, Any]:
    """Build task statistics from normalized task events."""
    if not task_events:
        return {
            "total_events": 0,
            "completions": 0,
            "failures": 0,
            "completion_rate": 0.0,
            "total_duration_minutes": 0,
            "avg_duration_minutes": 0.0,
            "total_xp": 0,
            "unique_tasks": 0,
            "unique_modules": 0,
        }
    
    completions = sum(1 for e in task_events if e.is_completion)
    failures = sum(1 for e in task_events if e.is_failure)
    total_duration = sum(e.duration_minutes or 0 for e in task_events)
    total_xp = sum(e.xp_awarded for e in task_events)
    unique_tasks = len(set(e.task_id for e in task_events))
    unique_modules = len(set(e.module_id for e in task_events if e.module_id))
    
    attempts = completions + failures
    completion_rate = completions / attempts if attempts > 0 else 0.0
    avg_duration = total_duration / len(task_events) if task_events else 0.0
    
    return {
        "total_events": len(task_events),
        "completions": completions,
        "failures": failures,
        "completion_rate": round(completion_rate, 3),
        "total_duration_minutes": total_duration,
        "avg_duration_minutes": round(avg_duration, 2),
        "total_xp": total_xp,
        "unique_tasks": unique_tasks,
        "unique_modules": unique_modules,
    }


def _build_difficulty_stats(task_events: List) -> Dict[str, Any]:
    """Build difficulty distribution from normalized task events."""
    if not task_events:
        return {
            "distribution": {"easy": 0, "medium": 0, "hard": 0, "extreme": 0},
            "completion_by_difficulty": {"easy": 0.0, "medium": 0.0, "hard": 0.0, "extreme": 0.0},
        }
    
    distribution = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
    completions_by_diff = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
    attempts_by_diff = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
    
    for e in task_events:
        bucket = e.difficulty_bucket
        distribution[bucket] += 1
        if e.is_completion or e.is_failure:
            attempts_by_diff[bucket] += 1
            if e.is_completion:
                completions_by_diff[bucket] += 1
    
    completion_rates = {}
    for bucket in ["easy", "medium", "hard", "extreme"]:
        if attempts_by_diff[bucket] > 0:
            completion_rates[bucket] = round(
                completions_by_diff[bucket] / attempts_by_diff[bucket], 3
            )
        else:
            completion_rates[bucket] = 0.0
    
    return {
        "distribution": distribution,
        "completion_by_difficulty": completion_rates,
    }


def _build_studyflow_patterns(session_events: List) -> Dict[str, Any]:
    """Build studyflow patterns from normalized session events."""
    if not session_events:
        return {
            "total_sessions": 0,
            "total_duration_minutes": 0,
            "avg_duration_minutes": 0.0,
            "avg_focus_score": 0.0,
            "avg_productivity": 0.0,
            "peak_hours": [],
            "interruption_rate": 0.0,
        }
    
    ended_sessions = [e for e in session_events if e.is_session_end]
    
    total_duration = sum(e.duration_minutes for e in ended_sessions)
    avg_duration = total_duration / len(ended_sessions) if ended_sessions else 0.0
    
    # Focus bucket to numeric for averaging
    focus_map = {"low": 0.2, "medium": 0.5, "high": 0.75, "peak": 0.95}
    avg_focus = sum(focus_map[e.focus_bucket] for e in ended_sessions) / len(ended_sessions) if ended_sessions else 0.0
    
    avg_productivity = sum(e.productivity_score for e in ended_sessions) / len(ended_sessions) if ended_sessions else 0.0
    
    total_interruptions = sum(e.interruptions for e in ended_sessions)
    interruption_rate = total_interruptions / len(ended_sessions) if ended_sessions else 0.0
    
    # Find peak hours (hours with most sessions)
    hour_counts: Dict[int, int] = {}
    for e in session_events:
        hour_counts[e.hour_of_day] = hour_counts.get(e.hour_of_day, 0) + 1
    
    # Sort hours by count descending, take top 3
    sorted_hours = sorted(hour_counts.items(), key=lambda x: (-x[1], x[0]))
    peak_hours = [h for h, _ in sorted_hours[:3]]
    
    return {
        "total_sessions": len(ended_sessions),
        "total_duration_minutes": total_duration,
        "avg_duration_minutes": round(avg_duration, 2),
        "avg_focus_score": round(avg_focus, 3),
        "avg_productivity": round(avg_productivity, 3),
        "peak_hours": peak_hours,
        "interruption_rate": round(interruption_rate, 2),
    }


def _build_xp_deltas(task_events: List, activity_events: List) -> Dict[str, Any]:
    """Build XP deltas from task and activity events."""
    task_xp = sum(e.xp_awarded for e in task_events)
    
    activity_xp = sum(
        e.value_delta for e in activity_events if e.is_xp_event
    )
    
    milestones = sum(1 for e in activity_events if e.is_milestone)
    
    return {
        "task_xp": task_xp,
        "activity_xp": activity_xp,
        "total_xp": task_xp + activity_xp,
        "milestones_achieved": milestones,
    }


def get_snapshot(user_id: str, date_key: str) -> Optional[Dict[str, Any]]:
    """
    Get a stored daily snapshot.
    
    Args:
        user_id: User ID
        date_key: Date in YYYY-MM-DD format
        
    Returns:
        Snapshot dict or None if not found
    """
    snapshot_key = f"{user_id}:{date_key}"
    with _snapshot_lock:
        return _daily_snapshots.get(snapshot_key)


def get_all_snapshots(user_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Get all stored snapshots, optionally filtered by user.
    Returns sorted by date descending for determinism.
    
    Args:
        user_id: Optional user ID filter
        
    Returns:
        List of snapshot dicts, sorted newest first
    """
    with _snapshot_lock:
        snapshots = list(_daily_snapshots.values())
    
    if user_id:
        snapshots = [s for s in snapshots if s["user_id"] == user_id]
    
    # Sort by date descending
    snapshots = sorted(snapshots, key=lambda s: s["date_key"], reverse=True)
    
    return snapshots
