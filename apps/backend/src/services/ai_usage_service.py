"""
AI Usage Service - Track and analyze OpenAI API usage per user
==============================================================

Logs every AI call with tokens and cost for:
- Dallas chat
- AI Quiz generation
- AI Quiz feedback
- Any other AI features

Provides analytics by user, week, and feature.
"""
import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID

# Model pricing (USD per 1K tokens) - Updated Dec 2024
MODEL_PRICING = {
    "gpt-3.5-turbo": {
        "input": 0.0005,   # $0.50 per 1M input tokens
        "output": 0.0015,  # $1.50 per 1M output tokens
    },
    "gpt-4": {
        "input": 0.03,     # $30 per 1M input tokens
        "output": 0.06,    # $60 per 1M output tokens
    },
    "gpt-4-turbo": {
        "input": 0.01,     # $10 per 1M input tokens
        "output": 0.03,    # $30 per 1M output tokens
    },
    "gpt-4o": {
        "input": 0.005,    # $5 per 1M input tokens
        "output": 0.015,   # $15 per 1M output tokens
    },
    "gpt-4o-mini": {
        "input": 0.00015,  # $0.15 per 1M input tokens
        "output": 0.0006,  # $0.60 per 1M output tokens
    },
}


def calculate_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    """Calculate cost in USD for a given model and token usage."""
    pricing = MODEL_PRICING.get(model, MODEL_PRICING["gpt-3.5-turbo"])

    input_cost = (prompt_tokens / 1000) * pricing["input"]
    output_cost = (completion_tokens / 1000) * pricing["output"]

    return round(input_cost + output_cost, 6)


def log_ai_usage(
    feature: str,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    user_id: Optional[UUID] = None,
    request_type: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """
    Log an AI API call to the database.

    Args:
        feature: 'dallas', 'ai_quiz', 'ai_chat', etc.
        model: 'gpt-3.5-turbo', 'gpt-4', etc.
        prompt_tokens: Number of input tokens
        completion_tokens: Number of output tokens
        user_id: Optional user UUID
        request_type: Optional request type for more detail

    Returns:
        Dict with usage info or None if logging failed
    """
    from .db.database import is_db_configured, get_db_context
    from .db.models import AIUsageLog

    if not is_db_configured():
        # Return usage info even if not saved to DB
        return {
            "logged": False,
            "feature": feature,
            "model": model,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "cost_usd": calculate_cost(model, prompt_tokens, completion_tokens),
        }

    try:
        now = datetime.utcnow()
        iso_calendar = now.isocalendar()

        cost = calculate_cost(model, prompt_tokens, completion_tokens)

        with get_db_context() as db:
            log_entry = AIUsageLog(
                id=uuid.uuid4(),
                user_id=user_id,
                feature=feature,
                model=model,
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
                cost_usd=cost,
                request_type=request_type,
                created_at=now,
                week_number=iso_calendar[1],
                year=iso_calendar[0],
            )
            db.add(log_entry)
            db.flush()

            return {
                "logged": True,
                "id": str(log_entry.id),
                "feature": feature,
                "model": model,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
                "cost_usd": cost,
            }
    except Exception as e:
        print(f"Error logging AI usage: {e}")
        return None


def get_user_usage_stats(
    user_id: UUID,
    year: Optional[int] = None,
    week: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Get AI usage statistics for a specific user.

    Args:
        user_id: User UUID
        year: Optional year filter
        week: Optional week filter

    Returns:
        Dict with usage stats
    """
    from .db.database import is_db_configured, get_db_context
    from .db.models import AIUsageLog
    from sqlalchemy import func

    if not is_db_configured():
        return {"error": "Database not configured"}

    try:
        with get_db_context() as db:
            query = db.query(
                func.count(AIUsageLog.id).label('total_calls'),
                func.sum(AIUsageLog.prompt_tokens).label('total_prompt_tokens'),
                func.sum(AIUsageLog.completion_tokens).label('total_completion_tokens'),
                func.sum(AIUsageLog.total_tokens).label('total_tokens'),
                func.sum(AIUsageLog.cost_usd).label('total_cost'),
            ).filter(AIUsageLog.user_id == user_id)

            if year:
                query = query.filter(AIUsageLog.year == year)
            if week:
                query = query.filter(AIUsageLog.week_number == week)

            result = query.first()

            # Get breakdown by feature
            feature_query = db.query(
                AIUsageLog.feature,
                func.count(AIUsageLog.id).label('calls'),
                func.sum(AIUsageLog.total_tokens).label('tokens'),
                func.sum(AIUsageLog.cost_usd).label('cost'),
            ).filter(AIUsageLog.user_id == user_id)

            if year:
                feature_query = feature_query.filter(AIUsageLog.year == year)
            if week:
                feature_query = feature_query.filter(AIUsageLog.week_number == week)

            feature_breakdown = feature_query.group_by(AIUsageLog.feature).all()

            return {
                "user_id": str(user_id),
                "year": year,
                "week": week,
                "totals": {
                    "calls": result.total_calls or 0,
                    "prompt_tokens": result.total_prompt_tokens or 0,
                    "completion_tokens": result.total_completion_tokens or 0,
                    "total_tokens": result.total_tokens or 0,
                    "cost_usd": round(result.total_cost or 0, 4),
                },
                "by_feature": [
                    {
                        "feature": f.feature,
                        "calls": f.calls,
                        "tokens": f.tokens or 0,
                        "cost_usd": round(f.cost or 0, 4),
                    }
                    for f in feature_breakdown
                ],
            }
    except Exception as e:
        return {"error": str(e)}


def get_all_users_usage(
    year: Optional[int] = None,
    week: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Get AI usage statistics for all users (admin view).

    Returns list of users with their usage stats.
    """
    from .db.database import is_db_configured, get_db_context
    from .db.models import AIUsageLog, User
    from sqlalchemy import func

    if not is_db_configured():
        return []

    try:
        with get_db_context() as db:
            query = db.query(
                AIUsageLog.user_id,
                User.email,
                User.full_name,
                func.count(AIUsageLog.id).label('total_calls'),
                func.sum(AIUsageLog.total_tokens).label('total_tokens'),
                func.sum(AIUsageLog.cost_usd).label('total_cost'),
            ).outerjoin(User, AIUsageLog.user_id == User.id)

            if year:
                query = query.filter(AIUsageLog.year == year)
            if week:
                query = query.filter(AIUsageLog.week_number == week)

            results = query.group_by(
                AIUsageLog.user_id, User.email, User.full_name
            ).order_by(func.sum(AIUsageLog.cost_usd).desc()).all()

            return [
                {
                    "user_id": str(r.user_id) if r.user_id else "anonymous",
                    "email": r.email or "Anonymous",
                    "full_name": r.full_name or "-",
                    "total_calls": r.total_calls,
                    "total_tokens": r.total_tokens or 0,
                    "total_cost_usd": round(r.total_cost or 0, 4),
                }
                for r in results
            ]
    except Exception as e:
        print(f"Error getting all users usage: {e}")
        return []


def get_weekly_summary(year: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Get weekly usage summary for all weeks.

    Returns list of weeks with total usage.
    """
    from .db.database import is_db_configured, get_db_context
    from .db.models import AIUsageLog
    from sqlalchemy import func

    if not is_db_configured():
        return []

    try:
        now = datetime.utcnow()
        target_year = year or now.year

        with get_db_context() as db:
            results = db.query(
                AIUsageLog.year,
                AIUsageLog.week_number,
                func.count(AIUsageLog.id).label('total_calls'),
                func.count(func.distinct(AIUsageLog.user_id)).label('unique_users'),
                func.sum(AIUsageLog.total_tokens).label('total_tokens'),
                func.sum(AIUsageLog.cost_usd).label('total_cost'),
            ).filter(
                AIUsageLog.year == target_year
            ).group_by(
                AIUsageLog.year, AIUsageLog.week_number
            ).order_by(
                AIUsageLog.week_number.desc()
            ).all()

            return [
                {
                    "year": r.year,
                    "week": r.week_number,
                    "total_calls": r.total_calls,
                    "unique_users": r.unique_users,
                    "total_tokens": r.total_tokens or 0,
                    "total_cost_usd": round(r.total_cost or 0, 4),
                }
                for r in results
            ]
    except Exception as e:
        print(f"Error getting weekly summary: {e}")
        return []
