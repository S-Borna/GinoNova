"""
Phase 8.11 — Test Normalizers
Tests for data normalization layer.
"""

import pytest
from datetime import datetime
from uuid import uuid4

from src.data.raw.raw_task_events import RawTaskEvent
from src.data.raw.raw_studyflow_sessions import RawStudyflowSession
from src.data.raw.raw_user_activity import RawUserActivity
from src.data.normalized.tasks_normalizer import normalize_task_event
from src.data.normalized.session_normalizer import normalize_studyflow_session
from src.data.normalized.activity_normalizer import normalize_user_activity


class TestTaskNormalizer:
    """Tests for task event normalization."""

    def test_normalize_task_event(self):
        """Test normalizing a task event."""
        raw = RawTaskEvent(
            event_id="evt_001",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime(2025, 11, 27, 10, 30, 0),
            difficulty=5,
            duration_seconds=1800,
            xp_awarded=50,
        )
        
        normalized = normalize_task_event(raw)
        
        assert normalized.event_id == "evt_001"
        assert normalized.event_type == "task_completed"
        assert normalized.date_key == "2025-11-27"
        assert normalized.hour_of_day == 10
        assert normalized.day_of_week == 3  # Thursday
        assert normalized.difficulty_bucket == "medium"
        assert normalized.duration_minutes == 30
        assert normalized.xp_awarded == 50
        assert normalized.is_completion is True
        assert normalized.is_failure is False

    def test_difficulty_buckets(self):
        """Test difficulty bucket mapping."""
        test_cases = [
            (1, "easy"),
            (3, "easy"),
            (4, "medium"),
            (5, "medium"),
            (6, "hard"),
            (7, "hard"),
            (8, "extreme"),
            (10, "extreme"),
            (None, "easy"),
        ]
        
        for difficulty, expected_bucket in test_cases:
            raw = RawTaskEvent(
                event_id=f"evt_diff_{difficulty}",
                event_type="task_completed",
                user_id=uuid4(),
                task_id=uuid4(),
                timestamp=datetime.utcnow(),
                difficulty=difficulty,
            )
            normalized = normalize_task_event(raw)
            assert normalized.difficulty_bucket == expected_bucket, f"Failed for difficulty={difficulty}"

    def test_completion_vs_failure_flags(self):
        """Test completion and failure flag calculation."""
        # Completion event
        raw_completed = RawTaskEvent(
            event_id="evt_completed",
            event_type="task_completed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
        )
        normalized = normalize_task_event(raw_completed)
        assert normalized.is_completion is True
        assert normalized.is_failure is False

        # Failure event
        raw_failed = RawTaskEvent(
            event_id="evt_failed",
            event_type="task_failed",
            user_id=uuid4(),
            task_id=uuid4(),
            timestamp=datetime.utcnow(),
        )
        normalized = normalize_task_event(raw_failed)
        assert normalized.is_completion is False
        assert normalized.is_failure is True


class TestSessionNormalizer:
    """Tests for session event normalization."""

    def test_normalize_session_event(self):
        """Test normalizing a session event."""
        raw = RawStudyflowSession(
            session_id="sess_001",
            event_type="session_ended",
            user_id=uuid4(),
            timestamp=datetime(2025, 11, 27, 14, 0, 0),
            duration_minutes=45,
            focus_score=0.85,
            tasks_in_session=[uuid4()],
            interruptions=2,
        )
        
        normalized = normalize_studyflow_session(raw)
        
        assert normalized.session_id == "sess_001"
        assert normalized.date_key == "2025-11-27"
        assert normalized.hour_of_day == 14
        assert normalized.focus_bucket == "peak"
        assert normalized.duration_minutes == 45
        assert normalized.tasks_count == 1
        assert normalized.is_session_end is True
        assert normalized.productivity_score > 0

    def test_focus_buckets(self):
        """Test focus score bucket mapping."""
        test_cases = [
            (0.1, "low"),
            (0.29, "low"),
            (0.3, "medium"),
            (0.59, "medium"),
            (0.6, "high"),
            (0.84, "high"),
            (0.85, "peak"),
            (1.0, "peak"),
            (None, "low"),
        ]
        
        for focus_score, expected_bucket in test_cases:
            raw = RawStudyflowSession(
                session_id=f"sess_focus_{focus_score}",
                event_type="session_ended",
                user_id=uuid4(),
                timestamp=datetime.utcnow(),
                focus_score=focus_score,
            )
            normalized = normalize_studyflow_session(raw)
            assert normalized.focus_bucket == expected_bucket, f"Failed for focus={focus_score}"


class TestActivityNormalizer:
    """Tests for activity event normalization."""

    def test_normalize_activity_event(self):
        """Test normalizing an activity event."""
        raw = RawUserActivity(
            activity_id="act_001",
            activity_type="xp_gained",
            user_id=uuid4(),
            timestamp=datetime(2025, 11, 27, 9, 0, 0),
            value_change=50,
        )
        
        normalized = normalize_user_activity(raw)
        
        assert normalized.activity_id == "act_001"
        assert normalized.activity_category == "progression"
        assert normalized.date_key == "2025-11-27"
        assert normalized.hour_of_day == 9
        assert normalized.is_xp_event is True
        assert normalized.value_delta == 50

    def test_activity_categories(self):
        """Test activity category mapping."""
        test_cases = [
            ("login", "auth"),
            ("logout", "auth"),
            ("page_view", "navigation"),
            ("feature_used", "navigation"),
            ("xp_gained", "progression"),
            ("level_up", "progression"),
            ("badge_earned", "progression"),
            ("profile_updated", "engagement"),
        ]
        
        for activity_type, expected_category in test_cases:
            raw = RawUserActivity(
                activity_id=f"act_{activity_type}",
                activity_type=activity_type,
                user_id=uuid4(),
                timestamp=datetime.utcnow(),
            )
            normalized = normalize_user_activity(raw)
            assert normalized.activity_category == expected_category

    def test_milestone_detection(self):
        """Test milestone event detection."""
        milestone_types = ["badge_earned", "level_up"]
        non_milestone_types = ["xp_gained", "login", "page_view"]
        
        for activity_type in milestone_types:
            raw = RawUserActivity(
                activity_id=f"act_{activity_type}",
                activity_type=activity_type,
                user_id=uuid4(),
                timestamp=datetime.utcnow(),
            )
            normalized = normalize_user_activity(raw)
            assert normalized.is_milestone is True
        
        for activity_type in non_milestone_types:
            raw = RawUserActivity(
                activity_id=f"act_{activity_type}",
                activity_type=activity_type,
                user_id=uuid4(),
                timestamp=datetime.utcnow(),
            )
            normalized = normalize_user_activity(raw)
            assert normalized.is_milestone is False
