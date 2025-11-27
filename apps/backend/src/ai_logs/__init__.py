"""
PHASE 7.13 — AI Logs + Telemetry Diagnostics

This module provides internal logging and diagnostics for the AI Engine.
No business logic changes - pure observability layer.
"""

from .logger import log_ai_event
from .diagnostics import get_daily_diagnostics

__all__ = ["log_ai_event", "get_daily_diagnostics"]
