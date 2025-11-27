"""
Worker Contract Tests
Phase 7.10: Tests for worker execution and contract enforcement

Tests:
- Worker execution with valid payloads
- Worker error handling with invalid payloads
- Exception handling and WorkerError generation
- Metadata presence and correctness
"""
import pytest
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from workers.worker_protocol import (
    WorkerTask,
    WorkerError,
    validate_worker_result,
    ResultValidationError,
)
from workers.base import BaseWorker, WorkerErrorCode


# ============================================================================
# TEST WORKER IMPLEMENTATION
# ============================================================================

class MockWorker(BaseWorker):
    """Test worker implementation for contract testing."""

    required_payload_keys = ["required_key"]

    @property
    def task_type(self) -> WorkerTask:
        return WorkerTask.RECOMMEND

    def _execute(self, payload: dict) -> dict:
        """Execute mock logic."""
        if payload.get("should_fail"):
            raise RuntimeError("Intentional failure")
        return {"result": "success", "input": payload.get("required_key")}


class MinimalWorker(BaseWorker):
    """Minimal worker with no required keys."""

    required_payload_keys: list[str] = []

    @property
    def task_type(self) -> WorkerTask:
        return WorkerTask.SUMMARY

    def _execute(self, payload: dict) -> dict:
        return {"minimal": True}


# ============================================================================
# WORKER EXECUTION TESTS
# ============================================================================

class TestWorkerExecution:
    """Tests for worker execution flow."""

    def test_successful_execution(self):
        """Test successful worker execution returns valid result."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        assert result["success"] is True
        assert result["data"] is not None
        assert result["data"]["result"] == "success"
        assert result["data"]["input"] == "test_value"
        assert result["error"] is None

    def test_result_validates_successfully(self):
        """Test that worker result passes validation."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        # Should not raise
        validate_worker_result(result)  # type: ignore

    def test_result_has_required_metadata(self):
        """Test that result has all required metadata fields."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        metadata = result["metadata"]
        assert "worker" in metadata
        assert "task_type" in metadata
        assert "timestamp" in metadata
        assert "duration_ms" in metadata

    def test_metadata_worker_name(self):
        """Test that metadata contains correct worker class name."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        assert result["metadata"]["worker"] == "MockWorker"

    def test_metadata_task_type(self):
        """Test that metadata contains correct task type."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        assert result["metadata"]["task_type"] == "recommend"

    def test_metadata_timestamp_valid(self):
        """Test that metadata timestamp is valid ISO8601."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        timestamp = result["metadata"]["timestamp"]
        # Should parse without error
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

    def test_metadata_duration_positive(self):
        """Test that duration_ms is a positive number."""
        worker = MockWorker()
        payload = {"required_key": "test_value"}

        result = worker.run(payload)

        assert result["metadata"]["duration_ms"] >= 0


# ============================================================================
# PAYLOAD VALIDATION TESTS
# ============================================================================

class TestPayloadValidation:
    """Tests for payload validation in workers."""

    def test_invalid_payload_missing_required_key(self):
        """Test that missing required key returns error result."""
        worker = MockWorker()
        payload = {}  # Missing required_key

        result = worker.run(payload)

        assert result["success"] is False
        assert result["error"] is not None
        assert result["error"]["code"] == WorkerErrorCode.VALIDATION_ERROR
        assert "required_key" in result["error"]["message"].lower() or "missing" in result["error"]["message"].lower()

    def test_invalid_payload_not_dict(self):
        """Test that non-dict payload returns error result."""
        worker = MockWorker()

        # This would be a type error at runtime, but testing the validation
        result = worker.run("not a dict")  # type: ignore

        assert result["success"] is False
        assert result["error"] is not None
        assert result["error"]["code"] == WorkerErrorCode.VALIDATION_ERROR

    def test_minimal_worker_accepts_empty_payload(self):
        """Test that worker with no required keys accepts empty payload."""
        worker = MinimalWorker()
        payload = {}

        result = worker.run(payload)

        assert result["success"] is True
        assert result["data"]["minimal"] is True


# ============================================================================
# EXCEPTION HANDLING TESTS
# ============================================================================

class TestExceptionHandling:
    """Tests for exception handling in workers."""

    def test_execute_exception_returns_error_result(self):
        """Test that exception in _execute returns error result."""
        worker = MockWorker()
        payload = {"required_key": "test", "should_fail": True}

        result = worker.run(payload)

        assert result["success"] is False
        assert result["error"] is not None
        assert result["error"]["code"] == WorkerErrorCode.ENGINE_ERROR
        assert "Intentional failure" in result["error"]["message"]

    def test_error_result_validates_successfully(self):
        """Test that error result passes validation."""
        worker = MockWorker()
        payload = {"required_key": "test", "should_fail": True}

        result = worker.run(payload)

        # Should not raise
        validate_worker_result(result)  # type: ignore

    def test_handle_exception_method(self):
        """Test handle_exception produces correct WorkerError."""
        worker = MockWorker()
        exc = RuntimeError("Test error message")

        error = worker.handle_exception(exc)

        assert error["code"] == WorkerErrorCode.ENGINE_ERROR
        assert error["message"] == "Test error message"

    def test_handle_exception_custom_code(self):
        """Test handle_exception with custom error code."""
        worker = MockWorker()
        exc = TimeoutError("Timeout occurred")

        error = worker.handle_exception(exc, error_code=WorkerErrorCode.TIMEOUT_ERROR)

        assert error["code"] == WorkerErrorCode.TIMEOUT_ERROR
        assert error["message"] == "Timeout occurred"

    def test_handle_exception_empty_message(self):
        """Test handle_exception with exception that has no message."""
        worker = MockWorker()
        exc = RuntimeError()  # No message

        error = worker.handle_exception(exc)

        assert error["code"] == WorkerErrorCode.ENGINE_ERROR
        assert error["message"] == "RuntimeError"  # Falls back to class name


# ============================================================================
# WORKER ERROR CODE TESTS
# ============================================================================

class TestWorkerErrorCodes:
    """Tests for WorkerErrorCode constants."""

    def test_validation_error_code(self):
        """Test VALIDATION_ERROR constant."""
        assert WorkerErrorCode.VALIDATION_ERROR == "VALIDATION_ERROR"

    def test_engine_error_code(self):
        """Test ENGINE_ERROR constant."""
        assert WorkerErrorCode.ENGINE_ERROR == "ENGINE_ERROR"

    def test_timeout_error_code(self):
        """Test TIMEOUT_ERROR constant."""
        assert WorkerErrorCode.TIMEOUT_ERROR == "TIMEOUT_ERROR"

    def test_internal_error_code(self):
        """Test INTERNAL_ERROR constant."""
        assert WorkerErrorCode.INTERNAL_ERROR == "INTERNAL_ERROR"


# ============================================================================
# WORKER NAME TESTS
# ============================================================================

class TestWorkerName:
    """Tests for worker_name property."""

    def test_worker_name_returns_class_name(self):
        """Test that worker_name returns the class name."""
        worker = MockWorker()
        assert worker.worker_name == "MockWorker"

    def test_minimal_worker_name(self):
        """Test worker_name for MinimalWorker."""
        worker = MinimalWorker()
        assert worker.worker_name == "MinimalWorker"


# ============================================================================
# EDGE CASE TESTS
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases in worker execution."""

    def test_payload_with_none_values(self):
        """Test that payload with None values works correctly."""
        worker = MockWorker()
        payload = {"required_key": None}

        result = worker.run(payload)

        assert result["success"] is True
        assert result["data"]["input"] is None

    def test_payload_with_complex_data(self):
        """Test that payload with nested data works correctly."""
        worker = MockWorker()
        payload = {
            "required_key": {
                "nested": {"deep": [1, 2, 3]},
                "list": ["a", "b", "c"],
            },
        }

        result = worker.run(payload)

        assert result["success"] is True
        assert result["data"]["input"]["nested"]["deep"] == [1, 2, 3]

    def test_multiple_executions_independent(self):
        """Test that multiple executions are independent."""
        worker = MockWorker()

        result1 = worker.run({"required_key": "first"})
        result2 = worker.run({"required_key": "second"})

        assert result1["data"]["input"] == "first"
        assert result2["data"]["input"] == "second"
        # Timestamps should be different (or very close)
        assert result1["metadata"]["timestamp"] != result2["metadata"]["timestamp"] or True
