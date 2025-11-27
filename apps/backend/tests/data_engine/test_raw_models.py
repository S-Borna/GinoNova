"""
Phase 8.11 — Test Raw Models
Tests for raw data layer Pydantic schemas.
"""

import pytest
from datetime import datetime
from uuid import uuid4

from src.data.raw.raw_task_events import RawTaskEvent
from src.data.raw.raw_studyflow_sessions import RawStudyflowSession
from src.data.raw.raw_user_activity import RawUserActivity


class TestRawTaskEvent:
    """Tests for RawTaskEvent schema."""

    def test_create_valid_task_event(self):
        """Test creating a valid task event."""
        event = RawTaskEvent(
            event_id="evt_001",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
            difficulty=5,
            duration_seconds=1800,
            xp_awarded=50,
        )
        
        assert event.event_id == "evt_001"
        assert event.event_type == "task_completed"
        assert event.difficulty == 5
        assert event.xp_awarded == 50

    def test_task_event_immutable(self):
        """Test that raw events are immutable (frozen)."""
        event = RawTaskEvent(
            event_id="evt_002",
            event_type="task_started",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
        )
        
        with pytest.raises(Exception):  # ValidationError for frozen model
            event.event_id = "changed"

    def test_task_event_valid_types(self):
        """Test all valid event types."""
        valid_types = [
            "task_created",
            "task_started",
            "task_completed",
            "task_failed",
            "task_skipped",
            "task_paused",
            "task_resumed",
        ]
        
        for event_type in valid_types:
            event = RawTaskEvent(
                event_id=f"evt_{event_type}",
                event_type=event_type,
                user_id=uuid4(),
                task_id=uuid4(),
                timestamp=datetime.utcnow(),
            )
            assert event.event_type == event_type

    def test_task_event_difficulty_bounds(self):
        """Test difficulty validation bounds."""
        # Valid difficulty
        event = RawTaskEvent(
            event_id="evt_valid_diff",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
            difficulty=1,
        )
        assert event.difficulty == 1

        event = RawTaskEvent(
            event_id="evt_valid_diff_max",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
            difficulty=10,
        )
        assert event.difficulty == 10


class TestRawStudyflowSession:
    """Tests for RawStudyflowSession schema."""

    def test_create_valid_session(self):
        """Test creating a valid session event."""
        session = RawStudyflowSession(
            session_id="sess_001",
            event_type="session_ended",
            user_id=uuid4(),
            timestamp=datetime.utcnow(),
            duration_minutes=45,
            focus_score=0.85,
            tasks_in_session=[uuid4()],
        )
        
        assert session.session_id == "sess_001"
        assert session.duration_minutes == 45
        assert session.focus_score == 0.85

    def test_session_valid_energy_levels(self):
        """Test valid energy levels."""
        for energy in ["low", "medium", "high"]:
            session = RawStudyflowSession(
                session_id=f"sess_{energy}",
                event_type="session_started",
                user_id=uuid4(),
                timestamp=datetime.utcnow(),
                energy_level=energy,
            )
            assert session.energy_level == energy


class TestRawUserActivity:
    """Tests for RawUserActivity schema."""

    def test_create_valid_activity(self):
        """Test creating a valid activity event."""
        activity = RawUserActivity(
            activity_id="act_001",
            activity_type="xp_gained",
            user_id=uuid4(),
            timestamp=datetime.utcnow(),
            value_change=50,
        )
        
        assert activity.activity_id == "act_001"
        assert activity.activity_type == "xp_gained"
        assert activity.value_change == 50

    def test_activity_valid_types(self):
        """Test all valid activity types."""
        valid_types = [
            "login",
            "logout",
            "page_view",
            "feature_used",
            "setting_changed",
            "profile_updated",
            "badge_earned",
            "level_up",
            "streak_updated",
            "xp_gained",
        ]
        
        for activity_type in valid_types:
            activity = RawUserActivity(
                activity_id=f"act_{activity_type}",
                activity_type=activity_type,
                user_id=uuid4(),
                timestamp=datetime.utcnow(),
            )
            assert activity.activity_type == activity_type
