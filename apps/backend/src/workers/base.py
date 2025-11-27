"""
Base Worker Implementation
Phase 7.9: Abstract base class for all AI workers

Provides:
- Payload validation
- Task start/end logging
- Deterministic result construction
"""
from abc import abstractmethod
from datetime import datetime, timezone
from typing import Any, Optional
import logging

from .worker_protocol import BaseWorkerProtocol, WorkerTask, WorkerResult


# ============================================================================
# LOGGER
# ============================================================================

logger = logging.getLogger(__name__)


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
    - validate_payload()
    - log_task_start()
    - log_task_end()
    - Deterministic WorkerResult construction
    """

    # Override in subclass to define required payload keys
    required_payload_keys: list[str] = []

    def validate_payload(self, payload: dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        Validate that payload contains all required keys.

        Args:
            payload: The payload dict to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(payload, dict):
            return False, "Payload must be a dictionary"

        missing_keys = [
            key for key in self.required_payload_keys
            if key not in payload
        ]

        if missing_keys:
            return False, f"Missing required keys: {missing_keys}"

        return True, None

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
        error: Optional[str] = None
    ) -> float:
        """
        Log task end and return duration.

        Args:
            start_time: Task start timestamp
            success: Whether task succeeded
            error: Error message if failed

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
                "task_type": self.task_type.value,
                "success": success,
                "duration_ms": duration_ms,
                "error": error,
            }
        )
        return duration_ms

    def _build_result(
        self,
        success: bool,
        data: Optional[dict[str, Any]] = None,
        error: Optional[str] = None,
        duration_ms: float = 0.0,
    ) -> WorkerResult:
        """
        Build a deterministic WorkerResult.

        Args:
            success: Whether task succeeded
            data: Result data payload
            error: Error message if failed
            duration_ms: Task duration

        Returns:
            WorkerResult TypedDict
        """
        return WorkerResult(
            success=success,
            task_type=self.task_type.value,
            data=data,
            error=error,
            metadata={
                "duration_ms": duration_ms,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "worker_version": "7.9-stub",
            }
        )

    @abstractmethod
    def _execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the worker's core logic.

        Subclasses implement this to perform actual work.

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
            # Log failure
            duration_ms = self.log_task_end(
                start_time,
                success=False,
                error=str(e)
            )

            return self._build_result(
                success=False,
                error=str(e),
                duration_ms=duration_ms,
            )
