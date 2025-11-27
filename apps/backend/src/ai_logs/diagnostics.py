"""
PHASE 7.13 — AI Diagnostics

Provides diagnostic summaries from AI logs.
Pure log-based analysis - no AI model usage, no performance impact.
"""
import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


# Log directory - uses /app/data in Docker, falls back to local path
LOG_DIR = Path(os.environ.get("AI_LOG_DIR", "/app/data/ai_logs"))


def get_daily_diagnostics() -> dict[str, Any]:
    """
    Compute daily diagnostics from AI logs.

    Returns deterministic structured dict with:
    - ai_calls_today: Total AI engine calls
    - average_latency_ms: Average latency (if tracked)
    - error_count: Number of error events
    - recommendation_types: Breakdown of recommendation types
    - next_step_usage: Count of next_step calls
    - summary_generated: Count of summary generations
    - engines_active: List of active engines

    This function is designed to be fast and never impact AI performance.
    """
    today = datetime.utcnow().strftime("%Y-%m-%d")
    log_file = LOG_DIR / f"{today}.log"

    # Default response when no logs exist
    diagnostics = {
        "date": today,
        "ai_calls_today": 0,
        "average_latency_ms": 0.0,
        "error_count": 0,
        "recommendation_types": {},
        "next_step_usage": 0,
        "summary_generated": 0,
        "pattern_analysis": 0,
        "engines_active": [],
        "event_breakdown": {},
        "status": "operational",
    }

    if not log_file.exists():
        diagnostics["status"] = "no_logs_today"
        return diagnostics

    try:
        engines = set()
        event_counts: dict[str, int] = defaultdict(int)
        recommendation_types: dict[str, int] = defaultdict(int)
        latencies: list[float] = []
        error_count = 0

        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue

                event_type = entry.get("event_type", "unknown")
                engine = entry.get("engine", "unknown")
                payload = entry.get("payload", {})

                # Count events
                event_counts[event_type] += 1
                engines.add(engine)

                # Track specific event types
                if event_type == "recommendation_generated":
                    rec_type = payload.get("type", "unknown")
                    recommendation_types[rec_type] += 1

                if event_type == "next_step_selected":
                    diagnostics["next_step_usage"] += 1

                if event_type == "summary_generated":
                    diagnostics["summary_generated"] += 1

                if event_type == "pattern_analysis":
                    diagnostics["pattern_analysis"] += 1

                if event_type == "error":
                    error_count += 1

                # Track latency if present
                if "latency_ms" in payload:
                    try:
                        latencies.append(float(payload["latency_ms"]))
                    except (ValueError, TypeError):
                        pass

        # Compile final diagnostics
        diagnostics["ai_calls_today"] = sum(event_counts.values())
        diagnostics["error_count"] = error_count
        diagnostics["recommendation_types"] = dict(recommendation_types)
        diagnostics["engines_active"] = sorted(engines)
        diagnostics["event_breakdown"] = dict(event_counts)

        if latencies:
            diagnostics["average_latency_ms"] = round(
                sum(latencies) / len(latencies), 2
            )

    except Exception:
        # Never let diagnostics fail - return partial data
        diagnostics["status"] = "partial_error"

    return diagnostics
