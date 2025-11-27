"""
PHASE 7.15 — AI Execution Map

Provides rolling in-memory storage for AI engine execution records.
Maximum 50 entries retained for debugging and analysis.
"""
from datetime import datetime
from threading import Lock
from typing import Any


# Rolling in-memory execution storage
_MAX_EXECUTIONS = 50
_executions: list[dict[str, Any]] = []
_lock = Lock()


def record_execution(
    engine_name: str,
    input_keys: list[str],
    output_keys: list[str],
) -> dict[str, Any]:
    """
    Record an AI engine execution event.

    Stores execution metadata in a rolling in-memory list.
    Thread-safe with a maximum of 50 entries.

    Args:
        engine_name: Name of the engine that executed
        input_keys: List of input context keys
        output_keys: List of output keys produced

    Returns:
        The recorded execution entry
    """
    entry = {
        "engine": engine_name,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "input_keys": sorted(input_keys),
        "output_keys": sorted(output_keys),
        "input_count": len(input_keys),
        "output_count": len(output_keys),
    }

    with _lock:
        _executions.append(entry)
        # Trim to max size
        while len(_executions) > _MAX_EXECUTIONS:
            _executions.pop(0)

    return entry


def get_recent_executions(limit: int = 50) -> list[dict[str, Any]]:
    """
    Get recent AI engine execution records.

    Returns entries in newest-first order.

    Args:
        limit: Maximum number of entries to return (default 50)

    Returns:
        List of execution records, newest first
    """
    with _lock:
        # Return copy in reverse order (newest first)
        result = list(reversed(_executions))
        return result[:limit]


def clear_executions() -> int:
    """
    Clear all execution records.

    Returns:
        Number of entries cleared
    """
    with _lock:
        count = len(_executions)
        _executions.clear()
        return count
