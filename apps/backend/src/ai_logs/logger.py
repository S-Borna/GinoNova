"""
PHASE 7.13 — AI Event Logger

Structured JSON logging for AI engine events.
Appends to /app/data/ai_logs/YYYY-MM-DD.log

IMPORTANT: This logger NEVER influences runtime behavior.
It is purely observational and has no side effects on AI outputs.
"""
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


# Log directory - uses /app/data in Docker, falls back to local path
LOG_DIR = Path(os.environ.get("AI_LOG_DIR", "/app/data/ai_logs"))


def _ensure_log_dir() -> None:
    """Ensure log directory exists."""
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
    except (PermissionError, OSError):
        # In environments where we can't write, silently skip
        pass


def _get_log_file() -> Path:
    """Get today's log file path."""
    today = datetime.utcnow().strftime("%Y-%m-%d")
    return LOG_DIR / f"{today}.log"


def log_ai_event(
    event_type: str,
    payload: dict[str, Any],
    *,
    engine: str = "unknown",
    phase: str = "7.13",
    request_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> None:
    """
    Log an AI engine event.

    This function is designed to NEVER raise exceptions or affect
    the calling code's behavior. All errors are silently caught.

    Args:
        event_type: Type of event (e.g., "recommendation_generated")
        payload: Event-specific data
        engine: Name of the AI engine
        phase: CMP phase identifier
        request_id: Optional request tracking ID
        user_id: Optional user ID
    """
    try:
        _ensure_log_dir()

        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "phase": phase,
            "engine": engine,
            "event_type": event_type,
            "request_id": request_id,
            "user_id": str(user_id) if user_id else None,
            "payload": payload,
        }

        log_file = _get_log_file()
        
        # Append JSON line to log file
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, default=str) + "\n")

    except Exception:
        # CRITICAL: Never let logging affect runtime behavior
        # Silently ignore all errors
        pass
