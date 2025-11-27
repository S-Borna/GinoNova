"""
AI Worker Integration Layer
Phase 7.9: Stubbed worker interfaces for future async pipelines

This package defines:
- Worker protocols and TypedDict payloads
- Base worker class with validation and logging
- Stubbed worker implementations for each AI service

NOTE: This phase is STUBS ONLY - no actual async scheduling,
queues, or background jobs. Workers are called synchronously
via direct invocation for now.
"""
from .worker_protocol import (
    WorkerTask,
    WorkerResult,
    RecommendPayload,
    NextStepPayload,
    DifficultyPayload,
    SummaryPayload,
    BaseWorkerProtocol,
)
from .base import BaseWorker
from .recommend_worker import RecommendWorker
from .next_step_worker import NextStepWorker
from .difficulty_worker import DifficultyWorker
from .summary_worker import SummaryWorker

__all__ = [
    # Protocol
    "WorkerTask",
    "WorkerResult",
    "RecommendPayload",
    "NextStepPayload",
    "DifficultyPayload",
    "SummaryPayload",
    "BaseWorkerProtocol",
    # Base
    "BaseWorker",
    # Workers
    "RecommendWorker",
    "NextStepWorker",
    "DifficultyWorker",
    "SummaryWorker",
]
