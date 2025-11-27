"""
Phase 8.11 — Test Dispatcher
Tests for the event dispatcher pipeline.
"""

import pytest
from datetime import datetime
from uuid import uuid4

from src.data.raw.raw_task_events import RawTaskEvent
from src.data.raw.raw_studyflow_sessions import RawStudyflowSession
from src.data.raw.raw_user_activity import RawUserActivity
from src.data.dispatcher.dispatcher import dispatch_event, dispatch_batch
from src.data.store.memory_store import clear_store, get_store_stats


class TestDispatcher:
    """Tests for event dispatcher."""

    def setup_method(self):
        """Clear store before each test."""
        clear_store()

    def test_dispatch_task_event(self):
        """Test dispatching a task event."""
        raw = RawTaskEvent(
            event_id="evt_dispatch_001",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
            difficulty=5,
        )

        result = dispatch_event(raw, "task")

        assert result["status"] == "dispatched"
        assert result["category"] == "task"
        assert result["event_id"] == "evt_dispatch_001"

        # Verify stored
        stats = get_store_stats()
        assert stats["task_events_count"] == 1

    def test_dispatch_session_event(self):
        """Test dispatching a session event."""
        raw = RawStudyflowSession(
            session_id="sess_dispatch_001",
            event_type="session_ended",
            user_id=uuid4(),
            timestamp=datetime.utcnow(),
            duration_minutes=30,
        )

        result = dispatch_event(raw, "session")

        assert result["status"] == "dispatched"
        assert result["category"] == "session"

        stats = get_store_stats()
        assert stats["session_events_count"] == 1

    def test_dispatch_activity_event(self):
        """Test dispatching an activity event."""
        raw = RawUserActivity(
            activity_id="act_dispatch_001",
            activity_type="xp_gained",
            user_id=uuid4(),
            timestamp=datetime.utcnow(),
            value_change=25,
        )

        result = dispatch_event(raw, "activity")

        assert result["status"] == "dispatched"
        assert result["category"] == "activity"

        stats = get_store_stats()
        assert stats["activity_events_count"] == 1

    def test_dispatch_invalid_category(self):
        """Test dispatching with invalid category raises error."""
        raw = RawTaskEvent(
            event_id="evt_invalid",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
        )

        with pytest.raises(ValueError) as exc_info:
            dispatch_event(raw, "invalid_category")

        assert "Unknown event category" in str(exc_info.value)

    def test_dispatch_batch(self):
        """Test batch event dispatch."""
        events = [
            RawTaskEvent(
                event_id=f"evt_batch_{i}",
                event_type="task_completed",
                user_id=uuid4(),
                task_id=uuid4(),
                timestamp=datetime.utcnow(),
            )
            for i in range(5)
        ]

        result = dispatch_batch(events, "task")

        assert result["status"] == "batch_complete"
        assert result["total"] == 5
        assert result["success"] == 5
        assert result["errors"] == []

        stats = get_store_stats()
        assert stats["task_events_count"] == 5

    def test_dispatch_maintains_order(self):
        """Test that dispatch maintains deterministic order."""
        user_id = uuid4()
        events = [
            RawTaskEvent(
                event_id=f"evt_order_{i}",
                event_type="task_completed",
                user_id=user_id,
                task_id=uuid4(),
                timestamp=datetime(2025, 11, 27, 10, i, 0),
            )
            for i in range(3)
        ]

        dispatch_batch(events, "task")

        from src.data.store.memory_store import get_task_events
        stored = get_task_events(user_id=str(user_id))

        # Should be sorted newest first
        assert len(stored) == 3
        timestamps = [e.timestamp_iso for e in stored]
        assert timestamps == sorted(timestamps, reverse=True)
