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
    count: int = Field(default=10, ge=1, le=100)
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(default="intermediate")
    focus_area: Optional[str] = Field(default=None)
    force_new: bool = Field(default=True, description="Generate fresh questions (skip cache)")


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

# Premium = All logged-in users have access
# No whitelist needed anymore


def check_quiz_access(user: UserPublic) -> bool:
    """Check if user has access to AI Quiz feature.

    Premium = logged in. All authenticated users have access.
    """
    # All logged-in users have access (premium = inlogg)
    return True


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

    NOW ASYNC: Uses parallel batches for large counts (100 questions in ~15-20s).
    Does NOT block other requests or tabs.

    - **module_slug**: Which module to generate questions from
    - **quiz_type**: "flashcard" or "mcq"
    - **count**: Number of questions (1-100)
    - **difficulty**: beginner, intermediate, or advanced
    - **focus_area**: Optional specific topic to focus on
    """
    # Check access
    if not check_quiz_access(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="AI Quiz Generator is a premium feature. Coming soon!"
        )

    import logging
    logger = logging.getLogger(__name__)

    from src.services.quiz_service import generate_quiz_async, get_module_content_for_quiz

    logger.info(f"🎯 Quiz request: module={request.module_slug}, type={request.quiz_type}, difficulty={request.difficulty}, count={request.count}")

    # Get module content
    content = get_module_content_for_quiz(request.module_slug)
    if not content:
        logger.error(f"❌ Module content not found for: {request.module_slug}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{request.module_slug}' not found. Available modules: linux-247, linux-tentaplugg, hands-on-lab"
        )

    logger.info(f"✅ Found content for {request.module_slug}: {len(content)} chars")

    # Extract module title
    module_title = request.module_slug.replace("-", " ").title()
    if content.startswith("# Module:"):
        first_line = content.split("\n")[0]
        module_title = first_line.replace("# Module:", "").strip()

    # Generate quiz ASYNC - doesn't block other requests!
    try:
        result = await generate_quiz_async(
            module_title=module_title,
            content=content,
            quiz_type=request.quiz_type,
            count=request.count,
            difficulty=request.difficulty,
            focus_area=request.focus_area,
            use_cache=not request.force_new
        )
    except Exception as e:
        logger.error(f"❌ Quiz generation exception: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Quiz generation error: {str(e)}"
        )

    if not result:
        logger.error(f"❌ Quiz generation returned None for {request.module_slug}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Quiz generation failed. Check OpenAI API key and service availability."
        )

    questions = result.get("questions", [])

    # Log AI Quiz completion for admin dashboard
    try:
        from .admin_v2 import add_activity_log
        
        # Get user display name
        user_name = getattr(current_user, 'full_name', None) or current_user.email.split('@')[0]
        
        # Format difficulty nicely
        difficulty_display = {
            'easy': 'Lätt',
            'medium': 'Medium', 
            'hard': 'Svår'
        }.get(request.difficulty, request.difficulty)
        
        add_activity_log(
            activity_type="ai_quiz",
            user_id=str(current_user.id),
            user_email=current_user.email,
            user_name=user_name,
            details=f"{user_name} • AI Quiz • {len(questions)} frågor • {module_title}"
        )
    except Exception as e:
        logger.debug(f"[ActivityLog] Failed to log AI quiz: {e}")

    return QuizResponse(
        questions=questions,
        metadata=QuizMetadata(
            module=module_title,
            quiz_type=request.quiz_type,
            difficulty=request.difficulty,
            count=len(questions),
            generated_at=datetime.utcnow().isoformat(),
            focus_area=request.focus_area
        )
    )


@router.get("/modules")
async def get_available_modules(
    current_user: UserPublic = Depends(get_current_user)
):
    """Get list of modules available for quiz generation.

    Returns:
    - Camp DevOps modules (Linux 24/7, Linux Tentaplugg, Hands-On Lab)
    - Static question sources (Manpage Tenta, Omtenta 2.0, etc.)

    AI Quiz generates NEW questions based on the content/style of these sources,
    unlike Tenta Simulator which shows the actual static questions.
    """
    # Get Camp DevOps modules dynamically from content source
    from src.db.seeds.content import get_camp_devops_modules

    camp_modules = get_camp_devops_modules()

    available_modules = [
        {
            "slug": m.get("slug"),
            "title": m.get("name", m.get("slug", "").replace("-", " ").title()),
            "description": m.get("description", "")
        }
        for m in camp_modules
    ]

    # Add static question sources (same as Tenta Simulator)
    # AI generates NEW questions based on these, not showing the static ones
    static_sources = [
        {
            "slug": "manpage-tenta",
            "title": "📚 Manpage Tenta",
            "description": "AI-genererade frågor baserat på Linux manpage-tenta (298 frågor som källa)"
        },
        {
            "slug": "omtenta-2",
            "title": "🎯 Omtenta 2.0",
            "description": "AI-genererade frågor baserat på Omtenta 2.0 innehåll"
        },
        {
            "slug": "handson",
            "title": "🔧 Hands-On Labs",
            "description": "AI-genererade frågor baserat på praktiska labbövningar"
        },
        {
            "slug": "linux-commands",
            "title": "💻 Linux Kommandon",
            "description": "AI-genererade frågor baserat på Linux kommandoreferens"
        },
    ]

    # Combine and return
    all_sources = available_modules + static_sources

    return {"modules": all_sources}
