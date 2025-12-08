"""
Task Progress Router - ILE Phase 1
API endpoints for interactive task progress tracking
"""
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Response, Query

from ..schemas.content_blocks import (
    TaskBlockProgress,
    TaskBlockProgressUpdate,
    TaskProgressResponse,
    QuizAnswer,
    TerminalCommand,
)
from ..core.deps import CurrentUser
from ..db.database import is_db_configured
from ..db import task_block_progress_repository as progress_repo
from ..db.task_repository import get_task_by_id
from ..db import user_repository


task_progress_router = APIRouter()

PHASE_VERSION = "ILE.1"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# STATUS ENDPOINT
# ==============================================================================

@task_progress_router.get("/status")
def task_progress_status(response: Response):
    """Check task progress module status"""
    add_phase_header(response)
    return {
        "task_progress": "configured",
        "phase": PHASE_VERSION,
        "feature": "Interactive Learning Engine",
        "database": "postgres" if is_db_configured() else "memory",
        "endpoints": [
            "GET /tasks/{task_id}/progress",
            "POST /tasks/{task_id}/progress/start",
            "POST /tasks/{task_id}/progress/block",
            "POST /tasks/{task_id}/progress/quiz",
            "POST /tasks/{task_id}/progress/terminal",
            "POST /tasks/{task_id}/progress/time",
            "POST /tasks/{task_id}/progress/complete",
        ]
    }


# ==============================================================================
# PROGRESS ENDPOINTS
# ==============================================================================

def _calculate_progress_response(
    progress: TaskBlockProgress,
    task_xp_reward: int = 25,
    content_blocks: list = None,
) -> TaskProgressResponse:
    """Calculate progress statistics from TaskBlockProgress"""
    content_blocks = content_blocks or []

    # Count block types
    quiz_blocks = [i for i, b in enumerate(content_blocks) if isinstance(b, dict) and b.get("type") == "quiz"]
    terminal_blocks = [i for i, b in enumerate(content_blocks) if isinstance(b, dict) and b.get("type") == "terminal"]

    # Count completions
    blocks_completed = sum(1 for bp in progress.block_progress if bp.completed)
    blocks_total = len(content_blocks) if content_blocks else 0

    quizzes_correct = sum(1 for qa in progress.quiz_answers if qa.is_correct)
    quizzes_total = len(quiz_blocks)

    # Terminal completion (check if all expected commands done for each block)
    terminals_completed = 0
    for block_idx in terminal_blocks:
        block_commands = [tc for tc in progress.terminal_history if tc.block_index == block_idx and tc.was_correct]
        if block_commands:  # At least one correct command
            terminals_completed += 1
    terminals_total = len(terminal_blocks)

    # Calculate progress percent
    progress_percent = 0
    if blocks_total > 0:
        progress_percent = int((blocks_completed / blocks_total) * 100)

    # Calculate potential XP (base + quiz bonuses)
    xp_potential = task_xp_reward
    for block in content_blocks:
        if isinstance(block, dict) and block.get("type") == "quiz":
            xp_potential += block.get("xp_bonus", 5)

    return TaskProgressResponse(
        task_id=progress.task_id,
        user_id=progress.user_id,
        status=progress.status,
        progress_percent=progress_percent,
        blocks_completed=blocks_completed,
        blocks_total=blocks_total,
        quizzes_correct=quizzes_correct,
        quizzes_total=quizzes_total,
        terminals_completed=terminals_completed,
        terminals_total=terminals_total,
        xp_earned=progress.xp_earned,
        xp_potential=xp_potential,
        time_spent=progress.total_time_spent,
        started_at=progress.started_at,
        completed_at=progress.completed_at,
    )


@task_progress_router.get("/{task_id}/progress", response_model=TaskProgressResponse)
def get_task_progress(
    task_id: UUID,
    response: Response,
    current_user: CurrentUser,
):
    """
    Get progress for a specific task.

    Returns progress statistics including:
    - Overall completion percentage
    - Blocks completed
    - Quiz answers
    - Terminal commands completed
    - XP earned
    """
    add_phase_header(response)

    # Get task to validate it exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Get progress (may be None if not started)
    progress = progress_repo.get_progress(current_user.id, task_id)

    if not progress:
        # Return empty progress
        return TaskProgressResponse(
            task_id=task_id,
            user_id=current_user.id,
            status="not_started",
            progress_percent=0,
            blocks_completed=0,
            blocks_total=len(getattr(task, 'content_blocks', []) or []),
            quizzes_correct=0,
            quizzes_total=0,
            terminals_completed=0,
            terminals_total=0,
            xp_earned=0,
            xp_potential=task.xp_reward,
            time_spent=0,
            started_at=None,
            completed_at=None,
        )

    content_blocks = getattr(task, 'content_blocks', []) or []
    return _calculate_progress_response(progress, task.xp_reward, content_blocks)


@task_progress_router.post("/{task_id}/progress/start", response_model=TaskProgressResponse)
def start_task(
    task_id: UUID,
    response: Response,
    current_user: CurrentUser,
):
    """
    Start tracking progress for a task.

    Creates a new progress record if one doesn't exist.
    """
    add_phase_header(response)

    # Validate task exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Create or get existing progress
    progress = progress_repo.create_progress(current_user.id, task_id)

    # Update last_activity_at for online status tracking
    user_repository.update_user(current_user.id, last_activity_at=datetime.utcnow())

    content_blocks = getattr(task, 'content_blocks', []) or []
    return _calculate_progress_response(progress, task.xp_reward, content_blocks)


@task_progress_router.post("/{task_id}/progress/block")
def update_block_completion(
    task_id: UUID,
    block_index: int,
    completed: bool,
    response: Response,
    current_user: CurrentUser,
):
    """
    Update completion status for a specific block.
    """
    add_phase_header(response)

    # Validate task exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Ensure progress exists
    progress = progress_repo.get_progress(current_user.id, task_id)
    if not progress:
        progress = progress_repo.create_progress(current_user.id, task_id)

    # Update block
    updated = progress_repo.update_block_progress(
        current_user.id, task_id, block_index, completed
    )

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to update progress")

    content_blocks = getattr(task, 'content_blocks', []) or []
    return _calculate_progress_response(updated, task.xp_reward, content_blocks)


@task_progress_router.post("/{task_id}/progress/quiz")
def record_quiz_answer(
    task_id: UUID,
    response: Response,
    current_user: CurrentUser,
    block_index: int = Query(..., description="Index of the quiz block"),
    selected_option: int = Query(..., description="Index of selected option"),
    is_correct: bool = Query(..., description="Whether answer was correct"),
):
    """
    Record a quiz answer.
    """
    add_phase_header(response)

    # Validate task exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Ensure progress exists
    progress = progress_repo.get_progress(current_user.id, task_id)
    if not progress:
        progress = progress_repo.create_progress(current_user.id, task_id)

    # Record answer
    quiz_answer = QuizAnswer(
        block_index=block_index,
        selected_option=selected_option,
        is_correct=is_correct,
        answered_at=datetime.utcnow(),
    )

    updated = progress_repo.add_quiz_answer(current_user.id, task_id, quiz_answer)

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to record quiz answer")

    # Also mark block as completed if answer is correct
    if is_correct:
        progress_repo.update_block_progress(current_user.id, task_id, block_index, True)

    content_blocks = getattr(task, 'content_blocks', []) or []
    return _calculate_progress_response(updated, task.xp_reward, content_blocks)


@task_progress_router.post("/{task_id}/progress/terminal")
def record_terminal_command(
    task_id: UUID,
    response: Response,
    current_user: CurrentUser,
    block_index: int = Query(..., description="Index of the terminal block"),
    command_index: int = Query(..., description="Index of command in expected list"),
    command: str = Query(..., description="Command entered by user"),
    was_correct: bool = Query(..., description="Whether command was correct"),
):
    """
    Record a terminal command.
    """
    add_phase_header(response)

    # Validate task exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Ensure progress exists
    progress = progress_repo.get_progress(current_user.id, task_id)
    if not progress:
        progress = progress_repo.create_progress(current_user.id, task_id)

    # Record command
    terminal_command = TerminalCommand(
        block_index=block_index,
        command_index=command_index,
        command=command,
        was_correct=was_correct,
        timestamp=datetime.utcnow(),
    )

    updated = progress_repo.add_terminal_command(current_user.id, task_id, terminal_command)

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to record terminal command")

    content_blocks = getattr(task, 'content_blocks', []) or []
    return _calculate_progress_response(updated, task.xp_reward, content_blocks)


@task_progress_router.post("/{task_id}/progress/time")
def update_time_spent(
    task_id: UUID,
    response: Response,
    current_user: CurrentUser,
    seconds: int = Query(..., ge=0, description="Seconds to add"),
):
    """
    Update time spent on task.
    """
    add_phase_header(response)

    # Validate task exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Ensure progress exists
    progress = progress_repo.get_progress(current_user.id, task_id)
    if not progress:
        progress = progress_repo.create_progress(current_user.id, task_id)

    updated = progress_repo.update_time_spent(current_user.id, task_id, seconds)

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to update time")

    content_blocks = getattr(task, 'content_blocks', []) or []
    return _calculate_progress_response(updated, task.xp_reward, content_blocks)


@task_progress_router.post("/{task_id}/progress/complete", response_model=TaskProgressResponse)
def complete_task_endpoint(
    task_id: UUID,
    response: Response,
    current_user: CurrentUser,
):
    """
    Mark task as completed and award XP.

    Calculates total XP including quiz bonuses.
    """
    add_phase_header(response)

    # Validate task exists
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Get progress
    progress = progress_repo.get_progress(current_user.id, task_id)
    if not progress:
        raise HTTPException(status_code=400, detail="Task not started")

    # Calculate XP
    base_xp = task.xp_reward
    bonus_xp = 0

    content_blocks = getattr(task, 'content_blocks', []) or []

    # Add quiz bonuses for correct answers
    for qa in progress.quiz_answers:
        if qa.is_correct and qa.block_index < len(content_blocks):
            block = content_blocks[qa.block_index]
            if isinstance(block, dict) and block.get("type") == "quiz":
                bonus_xp += block.get("xp_bonus", 5)

    total_xp = base_xp + bonus_xp

    # Complete task
    updated = progress_repo.complete_task(current_user.id, task_id, total_xp)

    if not updated:
        raise HTTPException(status_code=500, detail="Failed to complete task")

    # Update last_activity_at for online status tracking
    user_repository.update_user(current_user.id, last_activity_at=datetime.utcnow())

    # TODO: Update user's total XP in user model

    return _calculate_progress_response(updated, task.xp_reward, content_blocks)


# ==============================================================================
# BULK ENDPOINTS
# ==============================================================================

@task_progress_router.get("/user/all")
def get_all_user_progress(
    response: Response,
    current_user: CurrentUser,
):
    """
    Get all task progress for current user.
    """
    add_phase_header(response)

    progress_list = progress_repo.get_user_task_progress(current_user.id)

    return {
        "user_id": str(current_user.id),
        "total_tasks_started": len(progress_list),
        "completed": sum(1 for p in progress_list if p.status == "completed"),
        "in_progress": sum(1 for p in progress_list if p.status == "in_progress"),
        "total_xp_earned": sum(p.xp_earned for p in progress_list),
        "total_time_spent": sum(p.total_time_spent for p in progress_list),
    }
