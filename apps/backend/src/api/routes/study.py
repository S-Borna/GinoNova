"""
Study API Routes - Flashcards och Quiz från dedikerad study_data
================================================================

9 färdiga moduler med:
- 90 flashcards per modul (30 easy, 30 medium, 30 hard)
- 60 quiz-frågor per modul (20 easy, 20 medium, 20 hard)
- Slumpning av frågor OCH svarspositioner
"""
from fastapi import APIRouter, HTTPException, status, Query
from pydantic import BaseModel
from typing import List, Optional
import random

from src.db.seeds.study_data import STUDY_DATA_REGISTRY, get_all_study_modules

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
    """Hämta flashcards från study_data med bakåtkompatibla fält"""
    study_data = STUDY_DATA_REGISTRY.get(module_slug)
    if not study_data:
        return []

    flashcards_data = study_data.get("flashcards", {})
    result = []

    # Difficulty levels map to "lessons" for backwards compatibility
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
    """Hämta quiz-frågor från study_data med bakåtkompatibla fält"""
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
    """Skapa 'lessons' från difficulty levels för bakåtkompatibilitet"""
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
async def list_study_modules():
    """
    Lista alla 9 färdiga moduler med studydata.
    Returnerar antal flashcards och quiz per modul.
    """
    result = []

    for module_slug in get_all_study_modules():
        study_data = STUDY_DATA_REGISTRY.get(module_slug)
        if not study_data:
            continue

        # Räkna flashcards och quiz
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
            lesson_count=3,  # easy, medium, hard
            flashcard_count=flashcard_count,
            quiz_count=quiz_count
        ))

    return result


@router.get("/modules/{module_slug}", response_model=StudyModuleDetail)
async def get_study_module(module_slug: str):
    """Hämta detaljer för en specifik modul med lessons"""
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
    lessons: Optional[str] = Query(None, description="Kommaseparerade lesson IDs"),
    shuffle: bool = Query(True, description="Slumpa ordningen på kort")
):
    """
    Hämta flashcards för en modul.

    - **lessons**: Filtrera på lesson IDs (kommaseparerade)
    - **shuffle**: Slumpa ordningen (default: true)
    """
    study_data = STUDY_DATA_REGISTRY.get(module_slug)

    if not study_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte"
        )

    flashcards = get_flashcards_for_module(module_slug)

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
    lessons: Optional[str] = Query(None, description="Kommaseparerade lesson IDs"),
    shuffle: bool = Query(True, description="Slumpa ordningen på frågor"),
    shuffle_options: bool = Query(True, description="Slumpa svarsalternativens ordning")
):
    """
    Hämta quiz-frågor för en modul.

    - **lessons**: Filtrera på lesson IDs (kommaseparerade)
    - **shuffle**: Slumpa frågeordningen (default: true)
    - **shuffle_options**: Slumpa svarsalternativ så rätt svar inte alltid är A (default: true)
    """
    study_data = STUDY_DATA_REGISTRY.get(module_slug)

    if not study_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte"
        )

    questions = get_quiz_for_module(module_slug)

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
    """
    stats = {
        "total_modules": len(get_all_study_modules()),
        "total_flashcards": 0,
        "total_quiz_questions": 0,
        "modules": []
    }

    for module_slug in get_all_study_modules():
        study_data = STUDY_DATA_REGISTRY.get(module_slug)
        if not study_data:
            continue

        fc_easy = len(study_data.get("flashcards", {}).get("easy", []))
        fc_medium = len(study_data.get("flashcards", {}).get("medium", []))
        fc_hard = len(study_data.get("flashcards", {}).get("hard", []))
        fc_total = fc_easy + fc_medium + fc_hard

        quiz_easy = len(study_data.get("quiz", {}).get("easy", []))
        quiz_medium = len(study_data.get("quiz", {}).get("medium", []))
        quiz_hard = len(study_data.get("quiz", {}).get("hard", []))
        quiz_total = quiz_easy + quiz_medium + quiz_hard

        stats["total_flashcards"] += fc_total
        stats["total_quiz_questions"] += quiz_total

        stats["modules"].append({
            "slug": module_slug,
            "title": study_data.get("module_title", "Unknown"),
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
