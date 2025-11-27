"""
Worker Protocol Definitions
Phase 7.10: TypedDicts, enums, interfaces, and validation for worker layer

This module defines the contracts for the async worker integration layer.
All payloads are TypedDicts for type safety and serialization compatibility.
Includes strict validation functions for contract enforcement.
"""
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Optional, TypedDict


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
# ERROR TYPEDDICT
# ============================================================================

class WorkerError(TypedDict):
    """
    Standardized error structure for worker failures.

    Attributes:
        code: Error code identifier (e.g., "VALIDATION_ERROR", "ENGINE_ERROR")
        message: Human-readable error message
    """
    code: str
    message: str


# ============================================================================
# WORKER RESULT
# ============================================================================

class WorkerResultMetadata(TypedDict):
    """
    Required metadata fields for WorkerResult.

    Attributes:
        worker: Name of the worker class that produced the result
        task_type: The WorkerTask enum value as string
        timestamp: ISO8601 formatted timestamp of result creation
        duration_ms: Task execution duration in milliseconds
    """
    worker: str
    task_type: str
    timestamp: str
    duration_ms: float


class WorkerResult(TypedDict):
    """
    Standard result structure from all workers.

    Attributes:
        success: Whether the task completed successfully
        data: The actual result payload (task-specific), None on error
        error: WorkerError dict if success=False, None on success
        metadata: Required metadata (worker, task_type, timestamp, duration_ms)
    """
    success: bool
    data: Optional[dict[str, Any]]
    error: Optional[WorkerError]
    metadata: WorkerResultMetadata


# ============================================================================
# VALIDATION FUNCTIONS
# ============================================================================

class PayloadValidationError(Exception):
    """Raised when payload validation fails."""
    pass


class ResultValidationError(Exception):
    """Raised when result validation fails."""
    pass


# Required keys for each payload type
PAYLOAD_REQUIRED_KEYS: dict[WorkerTask, list[str]] = {
    WorkerTask.RECOMMEND: ["limit", "include_reasoning"],
    WorkerTask.NEXT_STEP: [],
    WorkerTask.DIFFICULTY: ["task_id"],
    WorkerTask.SUMMARY: [],
}


def validate_worker_payload(
    payload: dict[str, Any],
    task_type: WorkerTask,
) -> None:
    """
    Validate that a payload matches the expected structure for a task type.

    Args:
        payload: The payload dict to validate
        task_type: The WorkerTask type to validate against

    Raises:
        PayloadValidationError: If payload is invalid
    """
    if not isinstance(payload, dict):
        raise PayloadValidationError(
            f"Payload must be a dictionary, got {type(payload).__name__}"
        )

    required_keys = PAYLOAD_REQUIRED_KEYS.get(task_type, [])
    missing_keys = [key for key in required_keys if key not in payload]

    if missing_keys:
        raise PayloadValidationError(
            f"Missing required keys for {task_type.value}: {missing_keys}"
        )


# Required metadata keys
REQUIRED_METADATA_KEYS = ["worker", "task_type", "timestamp", "duration_ms"]


def validate_worker_result(result: dict[str, Any]) -> None:
    """
    Validate that a WorkerResult matches the expected structure.

    Args:
        result: The result dict to validate

    Raises:
        ResultValidationError: If result is invalid
    """
    if not isinstance(result, dict):
        raise ResultValidationError(
            f"Result must be a dictionary, got {type(result).__name__}"
        )

    # Check required top-level keys
    required_keys = ["success", "data", "error", "metadata"]
    missing_keys = [key for key in required_keys if key not in result]
    if missing_keys:
        raise ResultValidationError(
            f"Missing required result keys: {missing_keys}"
        )

    # Validate success is bool
    if not isinstance(result["success"], bool):
        raise ResultValidationError(
            f"'success' must be a boolean, got {type(result['success']).__name__}"
        )

    # Validate data is dict or None
    if result["data"] is not None and not isinstance(result["data"], dict):
        raise ResultValidationError(
            f"'data' must be a dictionary or None, got {type(result['data']).__name__}"
        )

    # Validate error structure
    if result["success"] is False:
        if result["error"] is None:
            raise ResultValidationError(
                "Failed result (success=False) must have an error object"
            )
        if not isinstance(result["error"], dict):
            raise ResultValidationError(
                f"'error' must be a dictionary, got {type(result['error']).__name__}"
            )
        if "code" not in result["error"] or "message" not in result["error"]:
            raise ResultValidationError(
                "Error object must contain 'code' and 'message' keys"
            )

    # Validate metadata
    if not isinstance(result["metadata"], dict):
        raise ResultValidationError(
            f"'metadata' must be a dictionary, got {type(result['metadata']).__name__}"
        )

    missing_metadata = [
        key for key in REQUIRED_METADATA_KEYS
        if key not in result["metadata"]
    ]
    if missing_metadata:
        raise ResultValidationError(
            f"Missing required metadata keys: {missing_metadata}"
        )

    # Validate timestamp format (ISO8601)
    timestamp = result["metadata"]["timestamp"]
    if not isinstance(timestamp, str):
        raise ResultValidationError(
            f"'timestamp' must be a string, got {type(timestamp).__name__}"
        )

    # Basic ISO8601 format check
    try:
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        raise ResultValidationError(
            f"'timestamp' must be valid ISO8601 format, got: {timestamp}"
        )


# ============================================================================
# BASE WORKER PROTOCOL
# ============================================================================

class BaseWorkerProtocol(ABC):
    """
    Protocol interface for all AI workers.

    All workers must:
    1. Define their task_type
    2. Implement run() method
    3. Return validated WorkerResult
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
