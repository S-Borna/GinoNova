"""
Study API Routes - Flashcards och Quiz från modulinnehåll
=============================================================

Dynamiskt genererat från modulernas noder.
Hämtar Key Takeaways, Kom ihåg-punkter och kommandotabeller.

SECURITY: All endpoints require authentication to prevent content scraping.
"""
from fastapi import APIRouter, HTTPException, status, Query
from pydantic import BaseModel
from typing import List, Optional
import random

# Ny generator som primär källa
from src.services.study_generator import (
    get_v3_study_data,
    get_v3_study_modules,
    get_module_icon,
)
from src.core.deps import CurrentUser

# Fallback registry - tom om ingen study_data finns
STUDY_DATA_REGISTRY = {}

def get_all_study_modules():
    """Fallback för study modules."""
    return []

router = APIRouter(prefix="/study", tags=["study"])


# === Schemas ===

class Flashcard(BaseModel):
    id: str
    front: str
    back: str
    module_slug: str
    lesson_title: str  # Maps to difficulty for backwards compatibility


class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct: int  # Index of correct answer (0-3)
    explanation: Optional[str] = None
    module_slug: str
    lesson_title: str  # Maps to difficulty for backwards compatibility


class StudyLesson(BaseModel):
    """Backwards compatible - maps to difficulty levels"""
    id: str
    title: str
    flashcard_count: int
    quiz_count: int


class StudyModule(BaseModel):
    slug: str
    title: str
    description: str
    icon: str
    lesson_count: int
    flashcard_count: int
    quiz_count: int


class StudyModuleDetail(BaseModel):
    slug: str
    title: str
    description: str
    icon: str
    lessons: List[StudyLesson]


class FlashcardsResponse(BaseModel):
    flashcards: List[Flashcard]
    total: int


class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
    total: int


# === Helper Functions ===

def shuffle_quiz_options(question: dict) -> dict:
    """
    Slumpa ordningen på svarsalternativ OCH uppdatera correct index.
    Så att rätt svar inte alltid är samma bokstav.
    """
    options = question["options"].copy()
    correct_answer = options[question["correct"]]

    # Skapa index-mapping och shuffla
    indices = list(range(len(options)))
    random.shuffle(indices)

    # Bygg nya options i shufflad ordning
    new_options = [options[i] for i in indices]

    # Hitta var rätt svar hamnade
    new_correct = new_options.index(correct_answer)

    return {
        **question,
        "options": new_options,
        "correct": new_correct
    }


def get_flashcards_for_module(module_slug: str) -> List[dict]:
    """
    Hämta flashcards - försök V3 först, fallback till statisk data.
    """
    # Försök V3-genererad data först
    v3_data = get_v3_study_data(module_slug)
    if v3_data and v3_data.get("flashcards"):
        flashcards_data = v3_data["flashcards"]
        result = []

        difficulty_titles = {
            "easy": "Grundläggande",
            "medium": "Medel",
            "hard": "Avancerad"
        }

        for diff in ["easy", "medium", "hard"]:
            cards = flashcards_data.get(diff, [])
            for i, card in enumerate(cards):
                result.append({
                    "id": f"{module_slug}-fc-{diff}-{i}",
                    "front": card.get("front", ""),
                    "back": card.get("back", ""),
                    "module_slug": module_slug,
                    "lesson_title": difficulty_titles[diff],
                    "source": card.get("source", "V3 Content")
                })

        if result:  # Om vi fick ut något, returnera det
            return result

    # Fallback till statisk study_data
    study_data = STUDY_DATA_REGISTRY.get(module_slug)
    if not study_data:
        return []

    flashcards_data = study_data.get("flashcards", {})
    result = []

    difficulty_titles = {
        "easy": "Grundläggande",
        "medium": "Medel",
        "hard": "Avancerad"
    }

    for diff in ["easy", "medium", "hard"]:
        cards = flashcards_data.get(diff, [])
        for i, card in enumerate(cards):
            result.append({
                "id": f"{module_slug}-fc-{diff}-{i}",
                "front": card["front"],
                "back": card["back"],
                "module_slug": module_slug,
                "lesson_title": difficulty_titles[diff]
            })

    return result


def get_quiz_for_module(module_slug: str) -> List[dict]:
    """
    Hämta quiz-frågor - försök V3 först, fallback till statisk data.
    """
    # Försök V3-genererad data först
    v3_data = get_v3_study_data(module_slug)
    if v3_data and v3_data.get("quiz"):
        quiz_data = v3_data["quiz"]
        result = []

        difficulty_titles = {
            "easy": "Grundläggande",
            "medium": "Medel",
            "hard": "Avancerad"
        }

        for diff in ["easy", "medium", "hard"]:
            questions = quiz_data.get(diff, [])
            for i, q in enumerate(questions):
                result.append({
                    "id": f"{module_slug}-quiz-{diff}-{i}",
                    "question": q.get("question", ""),
                    "options": q.get("options", []),
                    "correct": q.get("correct", 0),
                    "explanation": q.get("explanation"),
                    "module_slug": module_slug,
                    "lesson_title": difficulty_titles[diff],
                    "source": q.get("source", "V3 Content")
                })

        if result:  # Om vi fick ut något, returnera det
            return result

    # Fallback till statisk study_data
    study_data = STUDY_DATA_REGISTRY.get(module_slug)
    if not study_data:
        return []

    quiz_data = study_data.get("quiz", {})
    result = []

    difficulty_titles = {
        "easy": "Grundläggande",
        "medium": "Medel",
        "hard": "Avancerad"
    }

    for diff in ["easy", "medium", "hard"]:
        questions = quiz_data.get(diff, [])
        for i, q in enumerate(questions):
            result.append({
                "id": f"{module_slug}-quiz-{diff}-{i}",
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"],
                "explanation": q.get("explanation"),
                "module_slug": module_slug,
                "lesson_title": difficulty_titles[diff]
            })

    return result


def get_lessons_for_module(module_slug: str) -> List[dict]:
    """Skapa 'lessons' från difficulty levels - V3 först, sedan fallback"""
    # Försök V3 först
    v3_data = get_v3_study_data(module_slug)
    if v3_data:
        flashcards_data = v3_data.get("flashcards", {})
        quiz_data = v3_data.get("quiz", {})
    else:
        # Fallback till statisk data
        study_data = STUDY_DATA_REGISTRY.get(module_slug)
        if not study_data:
            return []
        flashcards_data = study_data.get("flashcards", {})
        quiz_data = study_data.get("quiz", {})

    lessons = []
    difficulty_map = [
        ("easy", "Grundläggande"),
        ("medium", "Medel"),
        ("hard", "Avancerad")
    ]

    for diff, title in difficulty_map:
        fc_count = len(flashcards_data.get(diff, []))
        quiz_count = len(quiz_data.get(diff, []))

        lessons.append({
            "id": f"{module_slug}-{diff}",
            "title": title,
            "flashcard_count": fc_count,
            "quiz_count": quiz_count
        })

    return lessons


# === Endpoints ===

@router.get("/modules", response_model=List[StudyModule])
async def list_study_modules(current_user: CurrentUser):
    """
    Lista alla moduler med studydata.
    Prioriterar V3-genererat innehåll, fallback till statisk data.

    **Authentication required**: Must be logged in to view study modules.

    Args:
        current_user: Authenticated user (injected)

    Returns:
        List of available study modules

    Raises:
        401: If not authenticated
    """
    result = []

    # Hämta alla tillgängliga moduler (kombinera V3 och statisk)
    all_slugs = set(get_v3_study_modules()) | set(get_all_study_modules())

    for module_slug in sorted(all_slugs):
        # Försök V3 först
        v3_data = get_v3_study_data(module_slug)

        if v3_data:
            flashcard_count = sum(
                len(v3_data.get("flashcards", {}).get(diff, []))
                for diff in ["easy", "medium", "hard"]
            )
            quiz_count = sum(
                len(v3_data.get("quiz", {}).get(diff, []))
                for diff in ["easy", "medium", "hard"]
            )

            result.append(StudyModule(
                slug=module_slug,
                title=v3_data.get("module_title", module_slug),
                description=v3_data.get("module_description", ""),
                icon=get_module_icon(module_slug),
                lesson_count=3,
                flashcard_count=flashcard_count,
                quiz_count=quiz_count
            ))
        else:
            # Fallback till statisk data
            study_data = STUDY_DATA_REGISTRY.get(module_slug)
            if not study_data:
                continue

            flashcard_count = sum(
                len(study_data.get("flashcards", {}).get(diff, []))
                for diff in ["easy", "medium", "hard"]
            )
            quiz_count = sum(
                len(study_data.get("quiz", {}).get(diff, []))
                for diff in ["easy", "medium", "hard"]
            )

            result.append(StudyModule(
                slug=study_data.get("module_slug", module_slug),
                title=study_data.get("module_title", "Unknown"),
                description=study_data.get("module_description", ""),
                icon=study_data.get("icon", "BookOpen"),
                lesson_count=3,
                flashcard_count=flashcard_count,
                quiz_count=quiz_count
            ))

    return result


@router.get("/modules/{module_slug}", response_model=StudyModuleDetail)
async def get_study_module(module_slug: str, current_user: CurrentUser):
    """
    Hämta detaljer för en specifik modul med lessons.

    **Authentication required**: Must be logged in to view module details.

    Args:
        module_slug: Module identifier
        current_user: Authenticated user (injected)

    Returns:
        Module details with lessons

    Raises:
        401: If not authenticated
        404: If module not found
    """
    # Försök V3 först
    v3_data = get_v3_study_data(module_slug)

    if v3_data:
        lessons = [StudyLesson(**lesson) for lesson in get_lessons_for_module(module_slug)]
        return StudyModuleDetail(
            slug=module_slug,
            title=v3_data.get("module_title", module_slug),
            description=v3_data.get("module_description", ""),
            icon=get_module_icon(module_slug),
            lessons=lessons
        )

    # Fallback till statisk data
    study_data = STUDY_DATA_REGISTRY.get(module_slug)

    if not study_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte"
        )

    lessons = [StudyLesson(**lesson) for lesson in get_lessons_for_module(module_slug)]

    return StudyModuleDetail(
        slug=study_data.get("module_slug", module_slug),
        title=study_data.get("module_title", "Unknown"),
        description=study_data.get("module_description", ""),
        icon=study_data.get("icon", "BookOpen"),
        lessons=lessons
    )


@router.get("/modules/{module_slug}/flashcards", response_model=FlashcardsResponse)
async def get_flashcards(
    module_slug: str,
    current_user: CurrentUser,
    lessons: Optional[str] = Query(None, description="Kommaseparerade lesson IDs"),
    shuffle: bool = Query(True, description="Slumpa ordningen på kort")
):
    """
    Hämta flashcards för en modul.
    Prioriterar V3-genererat innehåll från modulnoder.

    **Authentication required**: Must be logged in to access flashcards.
    This prevents unauthorized scraping of educational content.

    Args:
        module_slug: Module identifier
        current_user: Authenticated user (injected)
        lessons: Filtrera på lesson IDs (kommaseparerade)
        shuffle: Slumpa ordningen (default: true)

    Returns:
        Flashcards for the module

    Raises:
        401: If not authenticated
        404: If module not found or has no flashcards
    """
    flashcards = get_flashcards_for_module(module_slug)

    if not flashcards:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte eller har inga flashcards"
        )

    # Filtrera på lessons om angivet
    if lessons:
        lesson_ids = [lid.strip() for lid in lessons.split(",")]
        flashcards = [fc for fc in flashcards if any(lid in fc["id"] for lid in lesson_ids)]

    # Slumpa ordningen
    if shuffle:
        random.shuffle(flashcards)

    return FlashcardsResponse(
        flashcards=[Flashcard(**fc) for fc in flashcards],
        total=len(flashcards)
    )


@router.get("/modules/{module_slug}/quiz", response_model=QuizResponse)
async def get_quiz(
    module_slug: str,
    current_user: CurrentUser,
    lessons: Optional[str] = Query(None, description="Kommaseparerade lesson IDs"),
    shuffle: bool = Query(True, description="Slumpa ordningen på frågor"),
    shuffle_options: bool = Query(True, description="Slumpa svarsalternativens ordning")
):
    """
    Hämta quiz-frågor för en modul.
    Prioriterar V3-genererat innehåll från modulnoder.

    **Authentication required**: Must be logged in to access quiz questions.
    This prevents unauthorized scraping of educational content.

    Args:
        module_slug: Module identifier
        current_user: Authenticated user (injected)
        lessons: Filtrera på lesson IDs (kommaseparerade)
        shuffle: Slumpa frågeordningen (default: true)
        shuffle_options: Slumpa svarsalternativ så rätt svar inte alltid är A (default: true)

    Returns:
        Quiz questions for the module

    Raises:
        401: If not authenticated
        404: If module not found or has no quiz questions
    """
    questions = get_quiz_for_module(module_slug)

    if not questions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte eller har inga quiz-frågor"
        )

    # Filtrera på lessons om angivet
    if lessons:
        lesson_ids = [lid.strip() for lid in lessons.split(",")]
        questions = [q for q in questions if any(lid in q["id"] for lid in lesson_ids)]

    # Slumpa svarsalternativens ordning för varje fråga
    if shuffle_options:
        questions = [shuffle_quiz_options(q) for q in questions]

    # Slumpa frågeordningen
    if shuffle:
        random.shuffle(questions)

    return QuizResponse(
        questions=[QuizQuestion(**q) for q in questions],
        total=len(questions)
    )


# === Stats Endpoint ===

@router.get("/stats")
async def get_study_stats():
    """
    Hämta statistik för Studyroom.
    Visar totalt antal flashcards och quiz per modul.
    Prioriterar V3-genererat innehåll.
    """
    all_slugs = set(get_v3_study_modules()) | set(get_all_study_modules())

    stats = {
        "total_modules": len(all_slugs),
        "total_flashcards": 0,
        "total_quiz_questions": 0,
        "modules": [],
        "source": "v3_module_content"
    }

    for module_slug in sorted(all_slugs):
        # Försök V3 först
        v3_data = get_v3_study_data(module_slug)

        if v3_data:
            fc_data = v3_data.get("flashcards", {})
            quiz_data = v3_data.get("quiz", {})
            title = v3_data.get("module_title", module_slug)
        else:
            # Fallback till statisk data
            study_data = STUDY_DATA_REGISTRY.get(module_slug)
            if not study_data:
                continue
            fc_data = study_data.get("flashcards", {})
            quiz_data = study_data.get("quiz", {})
            title = study_data.get("module_title", "Unknown")

        fc_easy = len(fc_data.get("easy", []))
        fc_medium = len(fc_data.get("medium", []))
        fc_hard = len(fc_data.get("hard", []))
        fc_total = fc_easy + fc_medium + fc_hard

        quiz_easy = len(quiz_data.get("easy", []))
        quiz_medium = len(quiz_data.get("medium", []))
        quiz_hard = len(quiz_data.get("hard", []))
        quiz_total = quiz_easy + quiz_medium + quiz_hard

        stats["total_flashcards"] += fc_total
        stats["total_quiz_questions"] += quiz_total

        stats["modules"].append({
            "slug": module_slug,
            "title": title,
            "source": "v3" if v3_data else "static",
            "flashcards": {
                "easy": fc_easy,
                "medium": fc_medium,
                "hard": fc_hard,
                "total": fc_total
            },
            "quiz": {
                "easy": quiz_easy,
                "medium": quiz_medium,
                "hard": quiz_hard,
                "total": quiz_total
            }
        })

    return stats
