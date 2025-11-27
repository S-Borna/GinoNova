"""
Worker Protocol Tests
Phase 7.10: Tests for validation functions and TypedDict structures

Tests:
- validate_worker_payload() behavior
- validate_worker_result() behavior
- Error types and messages
"""
import pytest
from datetime import datetime, timezone

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from workers.worker_protocol import (
    WorkerTask,
    WorkerResult,
    WorkerResultMetadata,
    WorkerError,
    PayloadValidationError,
    ResultValidationError,
    validate_worker_payload,
    validate_worker_result,
    PAYLOAD_REQUIRED_KEYS,
    REQUIRED_METADATA_KEYS,
)


# ============================================================================
# PAYLOAD VALIDATION TESTS
# ============================================================================

class TestValidateWorkerPayload:
    """Tests for validate_worker_payload function."""

    def test_valid_recommend_payload(self):
        """Test that valid recommend payload passes validation."""
        payload = {
            "user_id": "user-123",
            "limit": 5,
            "include_reasoning": True,
        }
        # Should not raise
        validate_worker_payload(payload, WorkerTask.RECOMMEND)

    def test_valid_difficulty_payload(self):
        """Test that valid difficulty payload passes validation."""
        payload = {
            "user_id": "user-123",
            "task_id": "task-456",
        }
        # Should not raise
        validate_worker_payload(payload, WorkerTask.DIFFICULTY)

    def test_valid_next_step_payload_minimal(self):
        """Test that minimal next_step payload passes (no required keys)."""
        payload = {}
        # Should not raise - next_step has no required keys
        validate_worker_payload(payload, WorkerTask.NEXT_STEP)

    def test_valid_summary_payload_minimal(self):
        """Test that minimal summary payload passes (no required keys)."""
        payload = {"user_id": None}
        # Should not raise
        validate_worker_payload(payload, WorkerTask.SUMMARY)

    def test_invalid_payload_not_dict(self):
        """Test that non-dict payload raises PayloadValidationError."""
        with pytest.raises(PayloadValidationError) as exc_info:
            validate_worker_payload("not a dict", WorkerTask.RECOMMEND)  # type: ignore
        assert "must be a dictionary" in str(exc_info.value)

    def test_invalid_payload_missing_keys(self):
        """Test that missing required keys raises PayloadValidationError."""
        payload = {
            "user_id": "user-123",
            # Missing: limit, include_reasoning
        }
        with pytest.raises(PayloadValidationError) as exc_info:
            validate_worker_payload(payload, WorkerTask.RECOMMEND)
        assert "Missing required keys" in str(exc_info.value)
        assert "limit" in str(exc_info.value)

    def test_invalid_difficulty_missing_task_id(self):
        """Test that difficulty payload without task_id fails."""
        payload = {
            "user_id": "user-123",
            # Missing: task_id
        }
        with pytest.raises(PayloadValidationError) as exc_info:
            validate_worker_payload(payload, WorkerTask.DIFFICULTY)
        assert "task_id" in str(exc_info.value)


# ============================================================================
# RESULT VALIDATION TESTS
# ============================================================================

class TestValidateWorkerResult:
    """Tests for validate_worker_result function."""

    def test_valid_success_result(self):
        """Test that valid success result passes validation."""
        result = {
            "success": True,
            "data": {"recommendation": "test"},
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 123.45,
            },
        }
        # Should not raise
        validate_worker_result(result)

    def test_valid_error_result(self):
        """Test that valid error result passes validation."""
        result = {
            "success": False,
            "data": None,
            "error": {
                "code": "ENGINE_ERROR",
                "message": "Something went wrong",
            },
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 50.0,
            },
        }
        # Should not raise
        validate_worker_result(result)

    def test_invalid_result_not_dict(self):
        """Test that non-dict result raises ResultValidationError."""
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result("not a dict")  # type: ignore
        assert "must be a dictionary" in str(exc_info.value)

    def test_invalid_result_missing_keys(self):
        """Test that missing top-level keys raises error."""
        result = {
            "success": True,
            # Missing: data, error, metadata
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "Missing required result keys" in str(exc_info.value)

    def test_invalid_result_success_not_bool(self):
        """Test that non-boolean success raises error."""
        result = {
            "success": "yes",  # Should be bool
            "data": None,
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 0.0,
            },
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "must be a boolean" in str(exc_info.value)

    def test_invalid_result_data_not_dict(self):
        """Test that non-dict data raises error."""
        result = {
            "success": True,
            "data": "not a dict",  # Should be dict or None
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 0.0,
            },
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "must be a dictionary or None" in str(exc_info.value)

    def test_invalid_error_result_missing_error(self):
        """Test that failed result without error raises error."""
        result = {
            "success": False,
            "data": None,
            "error": None,  # Should have error when success=False
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 0.0,
            },
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "must have an error object" in str(exc_info.value)

    def test_invalid_error_missing_code(self):
        """Test that error without code raises error."""
        result = {
            "success": False,
            "data": None,
            "error": {
                # Missing: code
                "message": "Something went wrong",
            },
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 0.0,
            },
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "code" in str(exc_info.value)

    def test_invalid_metadata_missing_keys(self):
        """Test that metadata missing required keys raises error."""
        result = {
            "success": True,
            "data": None,
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                # Missing: task_type, timestamp, duration_ms
            },
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "Missing required metadata keys" in str(exc_info.value)

    def test_invalid_timestamp_format(self):
        """Test that invalid timestamp format raises error."""
        result = {
            "success": True,
            "data": None,
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": "not-a-timestamp",
                "duration_ms": 0.0,
            },
        }
        with pytest.raises(ResultValidationError) as exc_info:
            validate_worker_result(result)
        assert "valid ISO8601 format" in str(exc_info.value)


# ============================================================================
# TYPEDDICT STRUCTURE TESTS
# ============================================================================

class TestTypedDictStructures:
    """Tests for TypedDict structure correctness."""

    def test_worker_task_enum_values(self):
        """Test that WorkerTask enum has expected values."""
        assert WorkerTask.RECOMMEND.value == "recommend"
        assert WorkerTask.NEXT_STEP.value == "next_step"
        assert WorkerTask.DIFFICULTY.value == "difficulty"
        assert WorkerTask.SUMMARY.value == "summary"

    def test_payload_required_keys_mapping(self):
        """Test that PAYLOAD_REQUIRED_KEYS has entries for all tasks."""
        assert WorkerTask.RECOMMEND in PAYLOAD_REQUIRED_KEYS
        assert WorkerTask.NEXT_STEP in PAYLOAD_REQUIRED_KEYS
        assert WorkerTask.DIFFICULTY in PAYLOAD_REQUIRED_KEYS
        assert WorkerTask.SUMMARY in PAYLOAD_REQUIRED_KEYS

    def test_required_metadata_keys(self):
        """Test that REQUIRED_METADATA_KEYS contains expected keys."""
        assert "worker" in REQUIRED_METADATA_KEYS
        assert "task_type" in REQUIRED_METADATA_KEYS
        assert "timestamp" in REQUIRED_METADATA_KEYS
        assert "duration_ms" in REQUIRED_METADATA_KEYS


# ============================================================================
# EDGE CASE TESTS
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_payload_with_extra_keys(self):
        """Test that payload with extra keys passes validation."""
        payload = {
            "user_id": "user-123",
            "limit": 5,
            "include_reasoning": True,
            "extra_key": "should be ignored",
        }
        # Should not raise - extra keys are allowed
        validate_worker_payload(payload, WorkerTask.RECOMMEND)

    def test_result_with_extra_metadata(self):
        """Test that result with extra metadata passes validation."""
        result = {
            "success": True,
            "data": None,
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_ms": 0.0,
                "triggered_rules": ["rule1", "rule2"],
                "custom_key": "custom_value",
            },
        }
        # Should not raise - extra metadata is allowed
        validate_worker_result(result)

    def test_result_with_utc_z_timestamp(self):
        """Test that timestamp with Z suffix passes validation."""
        result = {
            "success": True,
            "data": None,
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": "2025-01-15T12:00:00Z",
                "duration_ms": 0.0,
            },
        }
        # Should not raise - Z is valid ISO8601
        validate_worker_result(result)

    def test_result_with_offset_timestamp(self):
        """Test that timestamp with offset passes validation."""
        result = {
            "success": True,
            "data": None,
            "error": None,
            "metadata": {
                "worker": "TestWorker",
                "task_type": "recommend",
                "timestamp": "2025-01-15T12:00:00+05:30",
                "duration_ms": 0.0,
            },
        }
        # Should not raise - offset is valid ISO8601
        validate_worker_result(result)
