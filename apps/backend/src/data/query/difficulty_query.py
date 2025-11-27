"""
Phase 8.5 — Difficulty Query Engine
Safe, deterministic read-only queries for difficulty analysis.
Used by AI engines for adaptive difficulty recommendations.
"""

from typing import Dict, Any, Literal

from ..store.memory_store import get_task_events
from ..store.indexes import get_events_by_difficulty


def query_difficulty_distribution(user_id: str) -> Dict[str, Any]:
    """
    Query difficulty distribution for a user.
    Shows what difficulty levels user engages with.
    
    Args:
        user_id: User ID to query
        
    Returns:
        Dict with difficulty distribution
    """
    events = get_task_events(user_id=user_id)
    
    if not events:
        return {
            "user_id": user_id,
            "has_data": False,
            "distribution": {"easy": 0, "medium": 0, "hard": 0, "extreme": 0},
        }
    
    # Count by difficulty
    distribution = {"easy": 0, "medium": 0, "hard": 0, "extreme": 0}
    for event in events:
        distribution[event.difficulty_bucket] += 1
    
    total = sum(distribution.values())
    percentages = {
        k: round(v / total * 100, 2) if total > 0 else 0.0
        for k, v in distribution.items()
    }
    
    # Find dominant difficulty (deterministic: alphabetical tie-breaker)
    sorted_dist = sorted(distribution.items(), key=lambda x: (-x[1], x[0]))
    dominant = sorted_dist[0][0] if sorted_dist else "medium"
    
    return {
        "user_id": user_id,
        "has_data": True,
        "total_events": total,
        "distribution": distribution,
        "percentages": percentages,
        "dominant_difficulty": dominant,
    }


def query_difficulty_performance(user_id: str) -> Dict[str, Any]:
    """
    Query user performance by difficulty level.
    Shows completion rates per difficulty.
    
    Args:
        user_id: User ID to query
        
    Returns:
        Dict with performance by difficulty
    """
    events = get_task_events(user_id=user_id)
    
    if not events:
        return {
            "user_id": user_id,
            "has_data": False,
            "performance": {},
        }
    
    # Aggregate by difficulty
    stats: Dict[str, Dict[str, int]] = {
        "easy": {"completions": 0, "failures": 0, "total": 0, "xp": 0, "duration": 0},
        "medium": {"completions": 0, "failures": 0, "total": 0, "xp": 0, "duration": 0},
        "hard": {"completions": 0, "failures": 0, "total": 0, "xp": 0, "duration": 0},
        "extreme": {"completions": 0, "failures": 0, "total": 0, "xp": 0, "duration": 0},
    }
    
    for event in events:
        bucket = event.difficulty_bucket
        stats[bucket]["total"] += 1
        stats[bucket]["xp"] += event.xp_awarded
        stats[bucket]["duration"] += event.duration_minutes or 0
        if event.is_completion:
            stats[bucket]["completions"] += 1
        if event.is_failure:
            stats[bucket]["failures"] += 1
    
    # Calculate rates
    performance = {}
    for bucket, data in stats.items():
        attempts = data["completions"] + data["failures"]
        performance[bucket] = {
            "total_events": data["total"],
            "completions": data["completions"],
            "failures": data["failures"],
            "completion_rate": round(
                data["completions"] / attempts, 3
            ) if attempts > 0 else 0.0,
            "total_xp": data["xp"],
            "avg_duration_minutes": round(
                data["duration"] / data["total"], 2
            ) if data["total"] > 0 else 0.0,
        }
    
    return {
        "user_id": user_id,
        "has_data": True,
        "performance": performance,
    }


def query_recommended_difficulty(user_id: str) -> Dict[str, Any]:
    """
    Query recommended difficulty level for a user.
    Based on recent performance trends.
    
    Args:
        user_id: User ID to query
        
    Returns:
        Dict with difficulty recommendation
    """
    performance = query_difficulty_performance(user_id)
    
    if not performance["has_data"]:
        return {
            "user_id": user_id,
            "has_data": False,
            "recommended": "medium",
            "reasoning": "No data available, defaulting to medium",
        }
    
    perf_data = performance["performance"]
    
    # Find optimal difficulty based on completion rate and engagement
    # Target: ~70-85% completion rate (challenge but not frustration)
    optimal_range = (0.70, 0.85)
    
    candidates = []
    difficulty_order = ["easy", "medium", "hard", "extreme"]
    
    for bucket in difficulty_order:
        data = perf_data[bucket]
        rate = data["completion_rate"]
        events = data["total_events"]
        
        if events < 3:
            # Not enough data for this difficulty
            continue
        
        # Score based on how close to optimal range
        if optimal_range[0] <= rate <= optimal_range[1]:
            score = 1.0  # Perfect range
        elif rate > optimal_range[1]:
            score = 0.8  # Too easy
        else:
            score = 0.6  # Too hard
        
        candidates.append({
            "bucket": bucket,
            "rate": rate,
            "events": events,
            "score": score,
        })
    
    if not candidates:
        return {
            "user_id": user_id,
            "has_data": True,
            "recommended": "medium",
            "reasoning": "Insufficient events per difficulty, defaulting to medium",
        }
    
    # Sort by score desc, then by difficulty progression for tie-breaker
    # (prefer harder when equal score)
    difficulty_rank = {"easy": 0, "medium": 1, "hard": 2, "extreme": 3}
    candidates = sorted(
        candidates,
        key=lambda x: (-x["score"], -difficulty_rank[x["bucket"]])
    )
    
    best = candidates[0]
    
    # Determine reasoning
    if best["rate"] > optimal_range[1]:
        reasoning = f"High success rate ({best['rate']:.0%}) at {best['bucket']}, consider increasing difficulty"
        # Suggest next level up if available
        current_rank = difficulty_rank[best["bucket"]]
        if current_rank < 3:
            next_level = difficulty_order[current_rank + 1]
            recommended = next_level
        else:
            recommended = best["bucket"]
    elif best["rate"] < optimal_range[0]:
        reasoning = f"Lower success rate ({best['rate']:.0%}) at {best['bucket']}, consider maintaining or decreasing"
        recommended = best["bucket"]
    else:
        reasoning = f"Optimal success rate ({best['rate']:.0%}) at {best['bucket']}"
        recommended = best["bucket"]
    
    return {
        "user_id": user_id,
        "has_data": True,
        "recommended": recommended,
        "reasoning": reasoning,
        "analysis": candidates,
    }
