"""
Studyflow API Routes
Flashcards och Quiz för alla moduler
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import random

router = APIRouter(tags=["studyflow-practice"])


# === Schemas ===

class Flashcard(BaseModel):
    id: str
    front: str
    back: str
    topic_id: str
    topic_title: str


class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct: int
    explanation: Optional[str] = None
    topic_id: str
    topic_title: str


class StudyflowTopic(BaseModel):
    id: str
    title: str
    flashcard_count: int
    quiz_count: int


class StudyflowModule(BaseModel):
    slug: str
    title: str
    description: str
    icon: str
    topic_count: int
    flashcard_count: int
    quiz_count: int


class StudyflowModuleDetail(BaseModel):
    slug: str
    title: str
    description: str
    icon: str
    topics: List[StudyflowTopic]


class FlashcardsResponse(BaseModel):
    flashcards: List[Flashcard]
    total: int
    module_title: str


class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
    total: int
    module_title: str


# === Data Import ===

def get_modules():
    """Import studyflow modules"""
    try:
        from src.db.seeds.studyflow.registry import STUDYFLOW_MODULES
        return STUDYFLOW_MODULES
    except ImportError:
        return {}


# === Endpoints ===

@router.get("/modules", response_model=List[StudyflowModule])
async def list_modules():
    """Lista alla moduler tillgängliga för studyflow"""
    modules = get_modules()
    result = []

    for slug, module in modules.items():
        topics = module.get("topics", [])

        flashcard_count = sum(len(t.get("flashcards", [])) for t in topics)
        quiz_count = sum(len(t.get("multiple_choice", [])) for t in topics)

        result.append(StudyflowModule(
            slug=slug,
            title=module["title"],
            description=module["description"],
            icon=module["icon"],
            topic_count=len(topics),
            flashcard_count=flashcard_count,
            quiz_count=quiz_count
        ))

    return result


@router.get("/modules/{module_slug}", response_model=StudyflowModuleDetail)
async def get_module(module_slug: str):
    """Hämta en modul med alla topics"""
    modules = get_modules()

    if module_slug not in modules:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{module_slug}' not found"
        )

    module = modules[module_slug]
    topics = []

    for topic in module.get("topics", []):
        topics.append(StudyflowTopic(
            id=topic["id"],
            title=topic["title"],
            flashcard_count=len(topic.get("flashcards", [])),
            quiz_count=len(topic.get("multiple_choice", []))
        ))

    return StudyflowModuleDetail(
        slug=module_slug,
        title=module["title"],
        description=module["description"],
        icon=module["icon"],
        topics=topics
    )


@router.get("/modules/{module_slug}/flashcards", response_model=FlashcardsResponse)
async def get_flashcards(
    module_slug: str,
    topics: Optional[str] = None,  # Comma-separated topic IDs
    shuffle: bool = False
):
    """Hämta flashcards för en modul, valfritt filtrerat på topics"""
    modules = get_modules()

    if module_slug not in modules:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{module_slug}' not found"
        )

    module = modules[module_slug]
    topic_filter = set(topics.split(",")) if topics else None

    all_flashcards = []

    for topic in module.get("topics", []):
        topic_id = topic["id"]

        # Skip om inte i filter
        if topic_filter and topic_id not in topic_filter:
            continue

        for i, fc in enumerate(topic.get("flashcards", [])):
            all_flashcards.append(Flashcard(
                id=f"{topic_id}-fc-{i}",
                front=fc["front"],
                back=fc["back"],
                topic_id=topic_id,
                topic_title=topic["title"]
            ))

    if shuffle:
        random.shuffle(all_flashcards)

    return FlashcardsResponse(
        flashcards=all_flashcards,
        total=len(all_flashcards),
        module_title=module["title"]
    )


@router.get("/modules/{module_slug}/quiz", response_model=QuizResponse)
async def get_quiz(
    module_slug: str,
    topics: Optional[str] = None,  # Comma-separated topic IDs
    shuffle: bool = False
):
    """Hämta quiz-frågor för en modul, valfritt filtrerat på topics"""
    modules = get_modules()

    if module_slug not in modules:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{module_slug}' not found"
        )

    module = modules[module_slug]
    topic_filter = set(topics.split(",")) if topics else None

    all_questions = []

    for topic in module.get("topics", []):
        topic_id = topic["id"]

        # Skip om inte i filter
        if topic_filter and topic_id not in topic_filter:
            continue

        for i, q in enumerate(topic.get("multiple_choice", [])):
            all_questions.append(QuizQuestion(
                id=f"{topic_id}-mc-{i}",
                question=q["question"],
                options=q["options"],
                correct=q["correct"],
                explanation=q.get("explanation"),
                topic_id=topic_id,
                topic_title=topic["title"]
            ))

    if shuffle:
        random.shuffle(all_questions)

    return QuizResponse(
        questions=all_questions,
        total=len(all_questions),
        module_title=module["title"]
    )
