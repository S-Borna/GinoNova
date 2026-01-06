"""
Exam Results API Routes
Endpoints for saving and retrieving exam simulation results
"""

from datetime import datetime, timezone, timedelta
from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, desc, and_
from sqlalchemy.orm import Session

from src.core.deps import get_current_user
from src.db.database import get_db
from src.db.models import User, ExamResult
from src.schemas.user import UserPublic

router = APIRouter()


# =============================================================================
# SCHEMAS
# =============================================================================

class ExamResultCreate(BaseModel):
    """Schema for creating a new exam result"""
    duration_minutes: int
    question_count: int
    sources: List[str] = []
    include_g: bool = True
    include_vg: bool = True
    grading_mode: str = "live"
    
    correct_answers: int
    wrong_answers: int
    skipped_answers: int = 0
    score_percent: float
    
    g_correct: int = 0
    g_total: int = 0
    vg_correct: int = 0
    vg_total: int = 0
    
    time_spent_seconds: int
    started_at: Optional[datetime] = None
    completed: bool = True


class ExamResultResponse(BaseModel):
    id: str
    user_id: str
    duration_minutes: int
    question_count: int
    sources: List[str]
    correct_answers: int
    wrong_answers: int
    skipped_answers: int
    score_percent: float
    g_correct: int
    g_total: int
    vg_correct: int
    vg_total: int
    time_spent_seconds: int
    completed_at: datetime
    completed: bool

    class Config:
        from_attributes = True


class UserExamStats(BaseModel):
    user_id: str
    email: str
    full_name: Optional[str]
    total_exams: int
    avg_score: float
    best_score: float
    total_questions_answered: int
    total_correct: int
    avg_time_minutes: float
    last_exam_at: Optional[datetime]


class ExamStatsOverview(BaseModel):
    total_exams: int
    total_exams_today: int
    total_exams_week: int
    total_questions_answered: int
    avg_score: float
    avg_time_minutes: float
    unique_users: int
    top_performers: List[UserExamStats]
    recent_exams: List[ExamResultResponse]
    score_distribution: dict  # {0-20: count, 20-40: count, ...}
    by_source: List[dict]


# =============================================================================
# USER ENDPOINTS
# =============================================================================

@router.post("/submit", response_model=ExamResultResponse)
async def submit_exam_result(
    data: ExamResultCreate,
    db: Session = Depends(get_db),
    current_user: UserPublic = Depends(get_current_user)
):
    """Submit exam results after completing a simulation"""
    exam_result = ExamResult(
        user_id=current_user.id,
        duration_minutes=data.duration_minutes,
        question_count=data.question_count,
        sources=data.sources,
        include_g=data.include_g,
        include_vg=data.include_vg,
        grading_mode=data.grading_mode,
        correct_answers=data.correct_answers,
        wrong_answers=data.wrong_answers,
        skipped_answers=data.skipped_answers,
        score_percent=data.score_percent,
        g_correct=data.g_correct,
        g_total=data.g_total,
        vg_correct=data.vg_correct,
        vg_total=data.vg_total,
        time_spent_seconds=data.time_spent_seconds,
        started_at=data.started_at,
        completed_at=datetime.now(timezone.utc),
        completed=data.completed
    )
    
    db.add(exam_result)
    db.commit()
    db.refresh(exam_result)
    
    return ExamResultResponse(
        id=str(exam_result.id),
        user_id=str(exam_result.user_id),
        duration_minutes=exam_result.duration_minutes,
        question_count=exam_result.question_count,
        sources=exam_result.sources or [],
        correct_answers=exam_result.correct_answers,
        wrong_answers=exam_result.wrong_answers,
        skipped_answers=exam_result.skipped_answers,
        score_percent=exam_result.score_percent,
        g_correct=exam_result.g_correct,
        g_total=exam_result.g_total,
        vg_correct=exam_result.vg_correct,
        vg_total=exam_result.vg_total,
        time_spent_seconds=exam_result.time_spent_seconds,
        completed_at=exam_result.completed_at,
        completed=exam_result.completed
    )


@router.get("/my-results", response_model=List[ExamResultResponse])
async def get_my_exam_results(
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: UserPublic = Depends(get_current_user)
):
    """Get current user's exam history"""
    results = db.query(ExamResult).filter(
        ExamResult.user_id == current_user.id
    ).order_by(desc(ExamResult.completed_at)).limit(limit).all()
    
    return [
        ExamResultResponse(
            id=str(r.id),
            user_id=str(r.user_id),
            duration_minutes=r.duration_minutes,
            question_count=r.question_count,
            sources=r.sources or [],
            correct_answers=r.correct_answers,
            wrong_answers=r.wrong_answers,
            skipped_answers=r.skipped_answers,
            score_percent=r.score_percent,
            g_correct=r.g_correct,
            g_total=r.g_total,
            vg_correct=r.vg_correct,
            vg_total=r.vg_total,
            time_spent_seconds=r.time_spent_seconds,
            completed_at=r.completed_at,
            completed=r.completed
        ) for r in results
    ]


@router.get("/my-stats")
async def get_my_exam_stats(
    db: Session = Depends(get_db),
    current_user: UserPublic = Depends(get_current_user)
):
    """Get current user's exam statistics"""
    results = db.query(ExamResult).filter(
        ExamResult.user_id == current_user.id,
        ExamResult.completed == True
    ).all()
    
    if not results:
        return {
            "total_exams": 0,
            "avg_score": 0,
            "best_score": 0,
            "total_questions": 0,
            "total_correct": 0,
            "avg_time_minutes": 0,
            "improvement_trend": []
        }
    
    total_questions = sum(r.question_count for r in results)
    total_correct = sum(r.correct_answers for r in results)
    avg_score = sum(r.score_percent for r in results) / len(results)
    best_score = max(r.score_percent for r in results)
    avg_time = sum(r.time_spent_seconds for r in results) / len(results) / 60
    
    # Get last 10 scores for trend
    recent = sorted(results, key=lambda x: x.completed_at)[-10:]
    improvement_trend = [{"date": r.completed_at.isoformat(), "score": r.score_percent} for r in recent]
    
    return {
        "total_exams": len(results),
        "avg_score": round(avg_score, 1),
        "best_score": round(best_score, 1),
        "total_questions": total_questions,
        "total_correct": total_correct,
        "avg_time_minutes": round(avg_time, 1),
        "improvement_trend": improvement_trend
    }
