"""
AI Chat API Routes - Phase 16
Chat, hints, and explanation endpoints.
"""
from fastapi import APIRouter, HTTPException, Query, Depends
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
from datetime import datetime
import logging
import uuid as uuid_module

from ...services.ai_assistant import (
    get_ai_response,
    get_hint,
    explain_concept,
    suggest_next_steps
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ai", tags=["ai-assistant"])


# Request/Response models
class ChatMessageRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    context: Optional[dict] = None


class ChatMessageResponse(BaseModel):
    response: str
    session_id: str
    tokens_used: int
    quota_remaining: Optional[int] = None


class HintRequest(BaseModel):
    task_id: str
    task_title: str
    task_description: str
    user_question: str
    user_attempt: Optional[str] = None


class HintResponse(BaseModel):
    hint: str
    tokens_used: int


class ExplainRequest(BaseModel):
    concept: str
    context: Optional[str] = None
    level: str = "intermediate"  # beginner, intermediate, advanced


class ExplainResponse(BaseModel):
    explanation: str
    tokens_used: int


class NextStepsRequest(BaseModel):
    completed_modules: List[str] = []
    current_module: Optional[str] = None
    user_goals: Optional[str] = None


# Daily AI quota (will be checked against plan)
FREE_QUOTA = 3
PRO_QUOTA = 999  # Effectively unlimited


async def get_user_quota(user_id: UUID) -> int:
    """Get remaining AI quota for today."""
    # TODO: Implement actual quota tracking
    # 1. Get user's plan
    # 2. Get today's usage from ai_usage_logs
    # 3. Calculate remaining
    return FREE_QUOTA


@router.post("/chat", response_model=ChatMessageResponse)
async def chat(
    request: ChatMessageRequest,
    user_id: Optional[UUID] = Query(None)
):
    """
    Send a message to the AI assistant.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    # Check quota
    quota = await get_user_quota(user_id)
    if quota <= 0:
        raise HTTPException(
            status_code=429,
            detail="Daily AI quota exceeded. Upgrade to Pro for unlimited access."
        )

    # Generate or use existing session ID
    session_id = request.session_id or str(uuid_module.uuid4())

    # Get AI response
    result = await get_ai_response(
        message=request.message,
        context=request.context,
        history=[]  # TODO: Load from database
    )

    if result["error"] == "not_configured":
        raise HTTPException(status_code=503, detail=result["response"])

    # TODO: Save message to database
    # TODO: Decrement quota

    logger.info(f"AI chat for user {user_id}: {result['tokens_used']} tokens")

    return ChatMessageResponse(
        response=result["response"],
        session_id=session_id,
        tokens_used=result["tokens_used"],
        quota_remaining=quota - 1
    )


@router.post("/hint", response_model=HintResponse)
async def get_task_hint(
    request: HintRequest,
    user_id: Optional[UUID] = Query(None)
):
    """
    Get a hint for a specific task.
    Hints guide without giving the answer directly.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    # Check quota
    quota = await get_user_quota(user_id)
    if quota <= 0:
        raise HTTPException(
            status_code=429,
            detail="Daily AI quota exceeded"
        )

    result = await get_hint(
        task_title=request.task_title,
        task_description=request.task_description,
        user_question=request.user_question,
        user_attempt=request.user_attempt
    )

    if result["error"] == "not_configured":
        raise HTTPException(status_code=503, detail="AI not configured")

    logger.info(f"AI hint for user {user_id}, task {request.task_id}")

    return HintResponse(
        hint=result["hint"],
        tokens_used=result["tokens_used"]
    )


@router.post("/explain", response_model=ExplainResponse)
async def explain(
    request: ExplainRequest,
    user_id: Optional[UUID] = Query(None)
):
    """
    Get an explanation of a DevOps concept.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    result = await explain_concept(
        concept=request.concept,
        context=request.context,
        level=request.level
    )

    if result["error"] == "not_configured":
        raise HTTPException(status_code=503, detail="AI not configured")

    return ExplainResponse(
        explanation=result["explanation"],
        tokens_used=result["tokens_used"]
    )


@router.post("/suggest-next")
async def suggest_next(
    request: NextStepsRequest,
    user_id: Optional[UUID] = Query(None)
):
    """
    Get personalized suggestions for next learning steps.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    result = await suggest_next_steps(
        completed_modules=request.completed_modules,
        current_module=request.current_module,
        user_goals=request.user_goals
    )

    return {
        "suggestions": result["suggestions"],
        "tokens_used": result["tokens_used"]
    }


@router.get("/history/{session_id}")
async def get_chat_history(
    session_id: str,
    user_id: Optional[UUID] = Query(None)
):
    """
    Get chat history for a session.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    # TODO: Fetch from database
    return {
        "session_id": session_id,
        "messages": [],
        "created_at": datetime.utcnow().isoformat()
    }


@router.get("/sessions")
async def get_chat_sessions(
    user_id: Optional[UUID] = Query(None),
    limit: int = Query(10, le=50)
):
    """
    Get user's chat sessions.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    # TODO: Fetch from database
    return {
        "sessions": [],
        "total": 0
    }


@router.get("/quota")
async def get_ai_quota(
    user_id: Optional[UUID] = Query(None)
):
    """
    Get user's current AI usage quota.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="Authentication required")

    quota = await get_user_quota(user_id)

    return {
        "daily_limit": FREE_QUOTA,  # TODO: Get from user's plan
        "used_today": FREE_QUOTA - quota,
        "remaining": quota,
        "resets_at": "00:00 UTC"
    }
