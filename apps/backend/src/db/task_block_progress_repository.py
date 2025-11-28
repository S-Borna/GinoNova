"""
Task Block Progress Repository - ILE Phase 1
Data access layer for interactive task progress tracking
"""
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from .database import is_db_configured, get_db_context
from ..schemas.content_blocks import (
    TaskBlockProgress as TaskBlockProgressSchema,
    BlockProgress,
    QuizAnswer,
    TerminalCommand,
)


# In-memory storage for development
TASK_PROGRESS: dict[str, TaskBlockProgressSchema] = {}


def _get_key(user_id: UUID, task_id: UUID) -> str:
    """Generate storage key for user+task combination"""
    return f"{user_id}:{task_id}"


def _get_model():
    """Lazy import of TaskBlockProgress model"""
    from .models import TaskBlockProgress as TaskBlockProgressModel
    return TaskBlockProgressModel


def _model_to_schema(model) -> TaskBlockProgressSchema:
    """Convert SQLAlchemy model to Pydantic schema"""
    return TaskBlockProgressSchema(
        user_id=model.user_id,
        task_id=model.task_id,
        status=model.status,
        block_progress=[BlockProgress(**bp) for bp in (model.block_progress or [])],
        quiz_answers=[QuizAnswer(**qa) for qa in (model.quiz_answers or [])],
        terminal_history=[TerminalCommand(**tc) for tc in (model.terminal_history or [])],
        started_at=model.started_at,
        completed_at=model.completed_at,
        total_time_spent=model.total_time_spent or 0,
        xp_earned=model.xp_earned or 0,
    )


def get_progress(user_id: UUID, task_id: UUID) -> Optional[TaskBlockProgressSchema]:
    """
    Get task progress for a user.

    Args:
        user_id: User UUID
        task_id: Task UUID

    Returns:
        TaskBlockProgress or None if not started
    """
    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()
            return _model_to_schema(progress) if progress else None

    key = _get_key(user_id, task_id)
    return TASK_PROGRESS.get(key)


def create_progress(user_id: UUID, task_id: UUID) -> TaskBlockProgressSchema:
    """
    Create new task progress record.

    Args:
        user_id: User UUID
        task_id: Task UUID

    Returns:
        New TaskBlockProgress
    """
    now = datetime.utcnow()

    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            # Check if already exists
            existing = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()

            if existing:
                return _model_to_schema(existing)

            progress = Model(
                user_id=user_id,
                task_id=task_id,
                status="in_progress",
                block_progress=[],
                quiz_answers=[],
                terminal_history=[],
                started_at=now,
                total_time_spent=0,
                xp_earned=0,
            )
            db.add(progress)
            db.flush()
            db.refresh(progress)
            return _model_to_schema(progress)

    key = _get_key(user_id, task_id)
    if key in TASK_PROGRESS:
        return TASK_PROGRESS[key]

    progress = TaskBlockProgressSchema(
        user_id=user_id,
        task_id=task_id,
        status="in_progress",
        block_progress=[],
        quiz_answers=[],
        terminal_history=[],
        started_at=now,
        total_time_spent=0,
        xp_earned=0,
    )
    TASK_PROGRESS[key] = progress
    return progress


def update_block_progress(
    user_id: UUID,
    task_id: UUID,
    block_index: int,
    completed: bool = True,
) -> Optional[TaskBlockProgressSchema]:
    """
    Update progress for a specific block.

    Args:
        user_id: User UUID
        task_id: Task UUID
        block_index: Index of the block
        completed: Whether block is completed

    Returns:
        Updated TaskBlockProgress
    """
    now = datetime.utcnow()

    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()

            if not progress:
                return None

            # Update block progress
            block_progress = list(progress.block_progress or [])

            # Find or create block entry
            found = False
            for bp in block_progress:
                if bp.get("block_index") == block_index:
                    bp["completed"] = completed
                    bp["attempts"] = bp.get("attempts", 0) + 1
                    if completed:
                        bp["completed_at"] = now.isoformat()
                    found = True
                    break

            if not found:
                block_progress.append({
                    "block_index": block_index,
                    "completed": completed,
                    "attempts": 1,
                    "completed_at": now.isoformat() if completed else None,
                })

            progress.block_progress = block_progress
            progress.updated_at = now
            db.flush()
            db.refresh(progress)
            return _model_to_schema(progress)

    # In-memory update
    key = _get_key(user_id, task_id)
    progress = TASK_PROGRESS.get(key)
    if not progress:
        return None

    # Update block progress
    found = False
    for bp in progress.block_progress:
        if bp.block_index == block_index:
            bp.completed = completed
            bp.attempts += 1
            if completed:
                bp.completed_at = now
            found = True
            break

    if not found:
        progress.block_progress.append(BlockProgress(
            block_index=block_index,
            completed=completed,
            attempts=1,
            completed_at=now if completed else None,
        ))

    return progress


def add_quiz_answer(
    user_id: UUID,
    task_id: UUID,
    quiz_answer: QuizAnswer,
) -> Optional[TaskBlockProgressSchema]:
    """
    Record a quiz answer.

    Args:
        user_id: User UUID
        task_id: Task UUID
        quiz_answer: The quiz answer to record

    Returns:
        Updated TaskBlockProgress
    """
    now = datetime.utcnow()

    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()

            if not progress:
                return None

            quiz_answers = list(progress.quiz_answers or [])
            quiz_answers.append(quiz_answer.model_dump())
            progress.quiz_answers = quiz_answers
            progress.updated_at = now
            db.flush()
            db.refresh(progress)
            return _model_to_schema(progress)

    key = _get_key(user_id, task_id)
    progress = TASK_PROGRESS.get(key)
    if not progress:
        return None

    progress.quiz_answers.append(quiz_answer)
    return progress


def add_terminal_command(
    user_id: UUID,
    task_id: UUID,
    terminal_command: TerminalCommand,
) -> Optional[TaskBlockProgressSchema]:
    """
    Record a terminal command.

    Args:
        user_id: User UUID
        task_id: Task UUID
        terminal_command: The command to record

    Returns:
        Updated TaskBlockProgress
    """
    now = datetime.utcnow()

    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()

            if not progress:
                return None

            terminal_history = list(progress.terminal_history or [])
            terminal_history.append(terminal_command.model_dump())
            progress.terminal_history = terminal_history
            progress.updated_at = now
            db.flush()
            db.refresh(progress)
            return _model_to_schema(progress)

    key = _get_key(user_id, task_id)
    progress = TASK_PROGRESS.get(key)
    if not progress:
        return None

    progress.terminal_history.append(terminal_command)
    return progress


def update_time_spent(
    user_id: UUID,
    task_id: UUID,
    seconds_delta: int,
) -> Optional[TaskBlockProgressSchema]:
    """
    Add time spent on task.

    Args:
        user_id: User UUID
        task_id: Task UUID
        seconds_delta: Seconds to add

    Returns:
        Updated TaskBlockProgress
    """
    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()

            if not progress:
                return None

            progress.total_time_spent = (progress.total_time_spent or 0) + seconds_delta
            progress.updated_at = datetime.utcnow()
            db.flush()
            db.refresh(progress)
            return _model_to_schema(progress)

    key = _get_key(user_id, task_id)
    progress = TASK_PROGRESS.get(key)
    if not progress:
        return None

    progress.total_time_spent += seconds_delta
    return progress


def complete_task(
    user_id: UUID,
    task_id: UUID,
    xp_earned: int,
) -> Optional[TaskBlockProgressSchema]:
    """
    Mark task as completed.

    Args:
        user_id: User UUID
        task_id: Task UUID
        xp_earned: Total XP earned

    Returns:
        Updated TaskBlockProgress
    """
    now = datetime.utcnow()

    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress = db.query(Model).filter(
                Model.user_id == user_id,
                Model.task_id == task_id
            ).first()

            if not progress:
                return None

            progress.status = "completed"
            progress.completed_at = now
            progress.xp_earned = xp_earned
            progress.updated_at = now
            db.flush()
            db.refresh(progress)
            return _model_to_schema(progress)

    key = _get_key(user_id, task_id)
    progress = TASK_PROGRESS.get(key)
    if not progress:
        return None

    progress.status = "completed"
    progress.completed_at = now
    progress.xp_earned = xp_earned
    return progress


def get_user_task_progress(user_id: UUID) -> List[TaskBlockProgressSchema]:
    """
    Get all task progress for a user.

    Args:
        user_id: User UUID

    Returns:
        List of TaskBlockProgress
    """
    if is_db_configured():
        Model = _get_model()
        with get_db_context() as db:
            progress_list = db.query(Model).filter(Model.user_id == user_id).all()
            return [_model_to_schema(p) for p in progress_list]

    return [p for key, p in TASK_PROGRESS.items() if str(p.user_id) == str(user_id)]
