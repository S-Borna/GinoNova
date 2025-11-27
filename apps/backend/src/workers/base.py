"""
Base Worker Implementation
Phase 7.10: Abstract base class for all AI workers

Provides:
- Strict payload validation with contract enforcement
- Deterministic error objects (WorkerError)
- Task start/end logging
- Result validation before return
"""
from abc import abstractmethod
from datetime import datetime, timezone
from typing import Any, Optional
import logging

from .worker_protocol import (
    BaseWorkerProtocol,
    WorkerResult,
    WorkerResultMetadata,
    WorkerError,
    PayloadValidationError,
    validate_worker_payload,
    validate_worker_result,
)


# ============================================================================
# LOGGER
# ============================================================================

logger = logging.getLogger(__name__)


# ============================================================================
# ERROR CODES
# ============================================================================

class WorkerErrorCode:
    """Standardized error codes for worker failures."""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    ENGINE_ERROR = "ENGINE_ERROR"
    TIMEOUT_ERROR = "TIMEOUT_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"


# ============================================================================
# BASE WORKER
# ============================================================================

class BaseWorker(BaseWorkerProtocol):
    """
    Abstract base class for all AI workers.

    Subclasses must implement:
    - task_type property
    - _execute(payload) method

    Base class provides:
    - validate_payload() with contract enforcement
    - handle_exception() for standardized error handling
    - log_task_start() / log_task_end()
    - Deterministic WorkerResult construction with validation
    """

    # Override in subclass to define required payload keys
    required_payload_keys: list[str] = []

    @property
    def worker_name(self) -> str:
        """Return the worker class name for metadata."""
        return self.__class__.__name__

    def validate_payload(self, payload: dict[str, Any]) -> tuple[bool, Optional[WorkerError]]:
        """
        Validate that payload contains all required keys.

        Args:
            payload: The payload dict to validate

        Returns:
            Tuple of (is_valid, error) where error is WorkerError or None
        """
        try:
            # Use protocol validation
            validate_worker_payload(payload, self.task_type)

            # Additional custom validation for subclass required keys
            if not isinstance(payload, dict):
                return False, WorkerError(
                    code=WorkerErrorCode.VALIDATION_ERROR,
                    message="Payload must be a dictionary",
                )

            missing_keys = [
                key for key in self.required_payload_keys
                if key not in payload
            ]

            if missing_keys:
                return False, WorkerError(
                    code=WorkerErrorCode.VALIDATION_ERROR,
                    message=f"Missing required keys: {missing_keys}",
                )

            return True, None

        except PayloadValidationError as e:
            return False, WorkerError(
                code=WorkerErrorCode.VALIDATION_ERROR,
                message=str(e),
            )

    def handle_exception(
        self,
        exc: Exception,
        error_code: str = WorkerErrorCode.ENGINE_ERROR,
    ) -> WorkerError:
        """
        Convert an exception to a standardized WorkerError.

        Args:
            exc: The exception that was raised
            error_code: Error code to use (default: ENGINE_ERROR)

        Returns:
            WorkerError dict with code and message
        """
        error_message = str(exc) if str(exc) else exc.__class__.__name__
        return WorkerError(
            code=error_code,
            message=error_message,
        )

    def log_task_start(self, payload: dict[str, Any]) -> datetime:
        """
        Log task start and return start timestamp.

        Args:
            payload: The task payload

        Returns:
            Start timestamp
        """
        start_time = datetime.now(timezone.utc)
        logger.info(
            f"[{self.task_type.value}] Task started",
            extra={
                "worker": self.worker_name,
                "task_type": self.task_type.value,
                "payload_keys": list(payload.keys()),
                "start_time": start_time.isoformat(),
            }
        )
        return start_time

    def log_task_end(
        self,
        start_time: datetime,
        success: bool,
        error: Optional[WorkerError] = None
    ) -> float:
        """
        Log task end and return duration.

        Args:
            start_time: Task start timestamp
            success: Whether task succeeded
            error: WorkerError if failed

        Returns:
            Duration in milliseconds
        """
        end_time = datetime.now(timezone.utc)
        duration_ms = (end_time - start_time).total_seconds() * 1000

        log_level = logging.INFO if success else logging.ERROR
        logger.log(
            log_level,
            f"[{self.task_type.value}] Task {'completed' if success else 'failed'}",
            extra={
                "worker": self.worker_name,
                "task_type": self.task_type.value,
                "success": success,
                "duration_ms": duration_ms,
                "error": error,
            }
        )
        return duration_ms

    def _build_metadata(self, duration_ms: float) -> WorkerResultMetadata:
        """
        Build standardized metadata for WorkerResult.

        Args:
            duration_ms: Task duration in milliseconds

        Returns:
            WorkerResultMetadata dict
        """
        return WorkerResultMetadata(
            worker=self.worker_name,
            task_type=self.task_type.value,
            timestamp=datetime.now(timezone.utc).isoformat(),
            duration_ms=duration_ms,
        )

    def _build_result(
        self,
        success: bool,
        data: Optional[dict[str, Any]] = None,
        error: Optional[WorkerError] = None,
        duration_ms: float = 0.0,
        extra_metadata: Optional[dict[str, Any]] = None,
    ) -> WorkerResult:
        """
        Build a deterministic, validated WorkerResult.

        Args:
            success: Whether task succeeded
            data: Result data payload
            error: WorkerError if failed
            duration_ms: Task duration
            extra_metadata: Additional metadata to include

        Returns:
            WorkerResult TypedDict
        """
        # Build base metadata
        metadata = self._build_metadata(duration_ms)

        # Merge extra metadata if provided
        if extra_metadata:
            metadata = {**metadata, **extra_metadata}  # type: ignore

        result = WorkerResult(
            success=success,
            data=data,
            error=error,
            metadata=metadata,  # type: ignore
        )

        # Validate result before returning
        try:
            validate_worker_result(result)  # type: ignore
        except Exception as e:
            # If validation fails, return an error result instead
            logger.error(
                f"[{self.task_type.value}] Result validation failed: {e}",
                extra={"worker": self.worker_name}
            )
            return WorkerResult(
                success=False,
                data=None,
                error=WorkerError(
                    code=WorkerErrorCode.INTERNAL_ERROR,
                    message=f"Result validation failed: {e}",
                ),
                metadata=self._build_metadata(duration_ms),  # type: ignore
            )

        return result

    @abstractmethod
    def _execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the worker's core logic.

        Subclasses implement this to perform actual work.
        Should raise exceptions on failure (handled by run()).

        Args:
            payload: Validated payload

        Returns:
            Result data dict
        """
        ...

    def run(self, payload: dict[str, Any]) -> WorkerResult:
        """
        Execute the worker task with validation and logging.

        Args:
            payload: Task payload

        Returns:
            WorkerResult with success status and data
        """
        # Validate payload
        is_valid, error = self.validate_payload(payload)
        if not is_valid:
            return self._build_result(
                success=False,
                error=error,
            )

        # Log start
        start_time = self.log_task_start(payload)

        try:
            # Execute core logic
            data = self._execute(payload)

            # Log end
            duration_ms = self.log_task_end(start_time, success=True)

            return self._build_result(
                success=True,
                data=data,
                duration_ms=duration_ms,
            )

        except Exception as e:
            # Convert exception to WorkerError
            worker_error = self.handle_exception(e)

            # Log failure
            duration_ms = self.log_task_end(
                start_time,
                success=False,
                error=worker_error,
            )

            return self._build_result(
                success=False,
                error=worker_error,
                duration_ms=duration_ms,
            )
