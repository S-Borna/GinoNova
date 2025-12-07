"""
Quiz API Routes - AI-powered quiz generation endpoints
Only accessible by specific users (premium feature).
"""
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from datetime import datetime

from src.core.deps import get_current_user
from src.schemas.user import UserPublic

router = APIRouter(prefix="/quiz", tags=["quiz"])


# === Schemas ===

class QuizGenerateRequest(BaseModel):
    module_slug: str = Field(..., description="Module slug to generate quiz from")
    quiz_type: Literal["flashcard", "mcq"] = Field(default="mcq")
    count: int = Field(default=10, ge=1, le=20)
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(default="intermediate")
    focus_area: Optional[str] = Field(default=None)


class QuizMetadata(BaseModel):
    module: str
    quiz_type: str
    difficulty: str
    count: int
    generated_at: str
    focus_area: Optional[str] = None


class QuizResponse(BaseModel):
    questions: List[dict]
    metadata: QuizMetadata


class FeatureAccessResponse(BaseModel):
    has_access: bool
    feature: str
    message: str


# === Access Control ===

QUIZ_ACCESS_USERS = {
    "said.ebadi@hotmail.com",
}


def check_quiz_access(user: UserPublic) -> bool:
    """Check if user has access to AI Quiz feature"""
    if hasattr(user, 'is_admin') and user.is_admin:
        return True
    return user.email.lower() in QUIZ_ACCESS_USERS


# === Endpoints ===

@router.get("/access", response_model=FeatureAccessResponse)
async def check_access(
    current_user: UserPublic = Depends(get_current_user)
):
    """Check if current user has access to AI Quiz feature."""
    has_access = check_quiz_access(current_user)

    if has_access:
        return FeatureAccessResponse(
            has_access=True,
            feature="ai_quiz",
            message="You have access to AI Quiz Generator"
        )
    else:
        return FeatureAccessResponse(
            has_access=False,
            feature="ai_quiz",
            message="AI Quiz Generator is a premium feature. Coming soon!"
        )


@router.post("/generate", response_model=QuizResponse)
async def generate_quiz(
    request: QuizGenerateRequest,
    current_user: UserPublic = Depends(get_current_user)
):
    """
    Generate AI-powered quiz questions for a module.

    - **module_slug**: Which module to generate questions from
    - **quiz_type**: "flashcard" or "mcq"
    - **count**: Number of questions (1-20)
    - **difficulty**: beginner, intermediate, or advanced
    - **focus_area**: Optional specific topic to focus on

    Quiz content is generated from the ACTUAL module node content,
    which includes Docker-style V3 formatting with tables, ASCII diagrams,
    code examples, and practical DevOps knowledge.
    """
    # Check access
    if not check_quiz_access(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="AI Quiz Generator is a premium feature. Coming soon!"
        )

    # Import service
    from src.services.quiz_service import generate_quiz as gen_quiz, get_module_content_for_quiz

    # Get module content from ACTUAL node data (not just metadata)
    content = get_module_content_for_quiz(request.module_slug)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{request.module_slug}' not found"
        )

    # Extract module title from content
    module_title = request.module_slug.replace("-", " ").title()
    if content.startswith("# Module:"):
        first_line = content.split("\n")[0]
        module_title = first_line.replace("# Module:", "").strip()

    # Generate quiz from actual node content
    result = gen_quiz(
        module_title=module_title,
        content=content,
        quiz_type=request.quiz_type,
        count=request.count,
        difficulty=request.difficulty,
        focus_area=request.focus_area
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Quiz generation failed. OpenAI service may be unavailable."
        )

    return QuizResponse(
        questions=result.get("questions", []),
        metadata=QuizMetadata(
            module=module_title,
            quiz_type=request.quiz_type,
            difficulty=request.difficulty,
            count=len(result.get("questions", [])),
            generated_at=datetime.utcnow().isoformat(),
            focus_area=request.focus_area
        )
    )


@router.get("/modules")
async def get_available_modules(
    current_user: UserPublic = Depends(get_current_user)
):
    """Get list of modules available for quiz generation."""
    from src.db.module_repository import list_modules

    modules = list_modules()

    return {
        "modules": [
            {
                "slug": getattr(m, 'slug', m.name.lower().replace(' ', '-')),
                "title": m.name,
                "description": getattr(m, 'description', f"Module: {m.name}")
            }
            for m in modules
        ]
    }
