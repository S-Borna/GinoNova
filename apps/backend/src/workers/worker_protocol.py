"""
Worker Protocol Definitions
Phase 7.9: TypedDicts, enums, and interfaces for worker layer

This module defines the contracts for the async worker integration layer.
All payloads are TypedDicts for type safety and serialization compatibility.
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Optional, TypedDict
from uuid import UUID


# ============================================================================
# WORKER TASK ENUM
# ============================================================================

class WorkerTask(str, Enum):
    """
    Deterministic enum of all worker task types.
    Each maps to a specific worker implementation.
    """
    RECOMMEND = "recommend"
    NEXT_STEP = "next_step"
    DIFFICULTY = "difficulty"
    SUMMARY = "summary"


# ============================================================================
# PAYLOAD TYPEDDICTS
# ============================================================================

class RecommendPayload(TypedDict):
    """Payload for recommendation worker."""
    user_id: Optional[str]
    limit: int
    include_reasoning: bool


class NextStepPayload(TypedDict):
    """Payload for next step worker."""
    user_id: Optional[str]


class DifficultyPayload(TypedDict):
    """Payload for difficulty estimation worker."""
    user_id: Optional[str]
    task_id: str


class SummaryPayload(TypedDict):
    """Payload for daily summary worker."""
    user_id: Optional[str]


# ============================================================================
# WORKER RESULT
# ============================================================================

class WorkerResult(TypedDict):
    """
    Standard result structure from all workers.

    Attributes:
        success: Whether the task completed successfully
        task_type: The WorkerTask enum value
        data: The actual result payload (task-specific)
        error: Error message if success=False
        metadata: Optional metadata (timing, cache info, etc.)
    """
    success: bool
    task_type: str
    data: Optional[dict[str, Any]]
    error: Optional[str]
    metadata: dict[str, Any]


# ============================================================================
# BASE WORKER PROTOCOL
# ============================================================================

class BaseWorkerProtocol(ABC):
    """
    Protocol interface for all AI workers.

    All workers must:
    1. Define their task_type
    2. Implement run() method
    3. Return WorkerResult
    """

    @property
    @abstractmethod
    def task_type(self) -> WorkerTask:
        """Return the worker's task type."""
        ...

    @abstractmethod
    def run(self, payload: dict[str, Any]) -> WorkerResult:
        """
        Execute the worker task.

        Args:
            payload: Task-specific payload (TypedDict)

        Returns:
            WorkerResult with success status and data
        """
        ...
