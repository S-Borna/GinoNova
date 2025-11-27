"""
PHASE 7.14 — Debug Frames

Builds deterministic, serializable debug frames for AI engine diagnostics.
Provides error isolation without modifying live API behavior.

Debug frames capture:
- Engine identification
- Context validation status
- Output validation status
- Error messages
- Schema/key introspection
- Timestamps
"""
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


# Log directory - uses /app/data in Docker, falls back to local path
LOG_DIR = Path(os.environ.get("AI_LOG_DIR", "/app/data/ai_logs"))


def build_debug_frame(
    context: dict[str, Any],
    engine: str,
    output: Optional[dict[str, Any]],
    errors: list[str],
) -> dict[str, Any]:
    """
    Build a deterministic debug frame for AI engine diagnostics.

    All fields are serializable and deterministic. This function
    NEVER raises exceptions - errors are captured in the frame.

    Args:
        context: The input context dict passed to the engine
        engine: Name of the AI engine (e.g., "recommendation_service")
        output: The output dict from the engine, or None if failed
        errors: List of error messages encountered

    Returns:
        Deterministic debug frame dict with schema:
        {
            "engine": str,
            "context_valid": bool,
            "output_valid": bool,
            "errors": list[str],
            "context_schema": list[str],
            "output_keys": list[str],
            "timestamp": str (ISO8601)
        }
    """
    try:
        # Validate context
        context_valid = (
            context is not None
            and isinstance(context, dict)
            and len(context) > 0
        )

        # Extract context schema (sorted keys for determinism)
        context_schema: list[str] = []
        if context and isinstance(context, dict):
            context_schema = sorted(context.keys())

        # Validate output
        output_valid = (
            output is not None
            and isinstance(output, dict)
            and len(output) > 0
            and len(errors) == 0
        )

        # Extract output keys (sorted for determinism)
        output_keys: list[str] = []
        if output and isinstance(output, dict):
            output_keys = sorted(output.keys())

        # Build frame
        frame = {
            "engine": engine,
            "context_valid": context_valid,
            "output_valid": output_valid,
            "errors": errors,
            "context_schema": context_schema,
            "output_keys": output_keys,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

        return frame

    except Exception as e:
        # Fallback frame if something goes wrong
        return {
            "engine": engine,
            "context_valid": False,
            "output_valid": False,
            "errors": [f"Debug frame build error: {str(e)}"] + errors,
            "context_schema": [],
            "output_keys": [],
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }


def get_recent_debug_frames(limit: int = 25) -> list[dict[str, Any]]:
    """
    Retrieve the most recent debug frames from AI logs.

    Reads debug frame entries from today's log file and returns
    them in newest-first order.

    Args:
        limit: Maximum number of frames to return (default 25)

    Returns:
        List of debug frames, newest first
    """
    frames: list[dict[str, Any]] = []

    try:
        # Try reading from today's log file
        today = datetime.utcnow().strftime("%Y-%m-%d")
        log_file = LOG_DIR / f"{today}.log"

        if not log_file.exists():
            return []

        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    entry = json.loads(line)
                    # Only include debug_frame events
                    if entry.get("event_type") == "debug_frame":
                        payload = entry.get("payload", {})
                        if isinstance(payload, dict):
                            frames.append(payload)
                except json.JSONDecodeError:
                    continue

        # Return newest first, limited
        frames.reverse()
        return frames[:limit]

    except Exception:
        # Never fail - return empty list on any error
        return []


def log_debug_frame(frame: dict[str, Any]) -> None:
    """
    Log a debug frame to the AI logs.

    Uses the same log format as ai_logs.logger but specifically
    for debug frame events.

    Args:
        frame: The debug frame dict to log
    """
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)

        today = datetime.utcnow().strftime("%Y-%m-%d")
        log_file = LOG_DIR / f"{today}.log"

        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "phase": "7.14",
            "engine": frame.get("engine", "unknown"),
            "event_type": "debug_frame",
            "request_id": None,
            "user_id": None,
            "payload": frame,
        }

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, default=str) + "\n")

    except Exception:
        # Never let logging affect runtime behavior
        pass
