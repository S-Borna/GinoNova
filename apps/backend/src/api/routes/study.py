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
from typing import List, Optional, Literal
import random

from src.db.seeds.study_data import STUDY_DATA_REGISTRY, get_all_study_modules

router = APIRouter(prefix="/study", tags=["study"])


# === Schemas ===

class Flashcard(BaseModel):
    id: str
    front: str
    back: str
    difficulty: Literal["easy", "medium", "hard"]


class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct: int  # Index of correct answer (0-3)
    explanation: Optional[str] = None
    difficulty: Literal["easy", "medium", "hard"]


class StudyNode(BaseModel):
    id: int
    title: str
    slug: str


class StudyModule(BaseModel):
    slug: str
    title: str
    description: str
    icon: str
    node_count: int
    flashcard_count: int
    quiz_count: int
    nodes: List[StudyNode]


class FlashcardsResponse(BaseModel):
    flashcards: List[Flashcard]
    total: int
    module_slug: str
    module_title: str
    difficulty: Optional[str] = None


class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
    total: int
    module_slug: str
    module_title: str
    difficulty: Optional[str] = None


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


def get_flashcards_for_module(module_slug: str, difficulty: Optional[str] = None) -> List[dict]:
    """Hämta flashcards från study_data"""
    study_data = STUDY_DATA_REGISTRY.get(module_slug)
    if not study_data:
        return []

    flashcards_data = study_data.get("flashcards", {})
    result = []

    difficulties = [difficulty] if difficulty else ["easy", "medium", "hard"]

    for diff in difficulties:
        cards = flashcards_data.get(diff, [])
        for i, card in enumerate(cards):
            result.append({
                "id": f"{module_slug}-fc-{diff}-{i}",
                "front": card["front"],
                "back": card["back"],
                "difficulty": diff
            })

    return result


def get_quiz_for_module(module_slug: str, difficulty: Optional[str] = None) -> List[dict]:
    """Hämta quiz-frågor från study_data"""
    study_data = STUDY_DATA_REGISTRY.get(module_slug)
    if not study_data:
        return []

    quiz_data = study_data.get("quiz", {})
    result = []

    difficulties = [difficulty] if difficulty else ["easy", "medium", "hard"]

    for diff in difficulties:
        questions = quiz_data.get(diff, [])
        for i, q in enumerate(questions):
            result.append({
                "id": f"{module_slug}-quiz-{diff}-{i}",
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"],
                "explanation": q.get("explanation"),
                "difficulty": diff
            })

    return result


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

        # Hämta nodes
        nodes = [
            StudyNode(id=n["id"], title=n["title"], slug=n["slug"])
            for n in study_data.get("nodes", [])
        ]

        result.append(StudyModule(
            slug=study_data.get("module_slug", module_slug),
            title=study_data.get("module_title", "Unknown"),
            description=study_data.get("module_description", ""),
            icon=study_data.get("icon", "BookOpen"),
            node_count=len(nodes),
            flashcard_count=flashcard_count,
            quiz_count=quiz_count,
            nodes=nodes
        ))

    return result


@router.get("/modules/{module_slug}", response_model=StudyModule)
async def get_study_module(module_slug: str):
    """Hämta detaljer för en specifik modul"""
    study_data = STUDY_DATA_REGISTRY.get(module_slug)

    if not study_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte"
        )

    flashcard_count = sum(
        len(study_data.get("flashcards", {}).get(diff, []))
        for diff in ["easy", "medium", "hard"]
    )
    quiz_count = sum(
        len(study_data.get("quiz", {}).get(diff, []))
        for diff in ["easy", "medium", "hard"]
    )

    nodes = [
        StudyNode(id=n["id"], title=n["title"], slug=n["slug"])
        for n in study_data.get("nodes", [])
    ]

    return StudyModule(
        slug=study_data.get("module_slug", module_slug),
        title=study_data.get("module_title", "Unknown"),
        description=study_data.get("module_description", ""),
        icon=study_data.get("icon", "BookOpen"),
        node_count=len(nodes),
        flashcard_count=flashcard_count,
        quiz_count=quiz_count,
        nodes=nodes
    )


@router.get("/modules/{module_slug}/flashcards", response_model=FlashcardsResponse)
async def get_flashcards(
    module_slug: str,
    difficulty: Optional[Literal["easy", "medium", "hard"]] = Query(
        None, description="Filtrera på svårighetsgrad"
    ),
    shuffle: bool = Query(True, description="Slumpa ordningen på kort"),
    limit: Optional[int] = Query(None, description="Max antal kort att returnera")
):
    """
    Hämta flashcards för en modul.

    - **difficulty**: easy, medium, eller hard (alla om ej angiven)
    - **shuffle**: Slumpa ordningen (default: true)
    - **limit**: Begränsa antal kort
    """
    study_data = STUDY_DATA_REGISTRY.get(module_slug)

    if not study_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte"
        )

    flashcards = get_flashcards_for_module(module_slug, difficulty)

    # Slumpa ordningen
    if shuffle:
        random.shuffle(flashcards)

    # Begränsa antal
    if limit and limit > 0:
        flashcards = flashcards[:limit]

    return FlashcardsResponse(
        flashcards=[Flashcard(**fc) for fc in flashcards],
        total=len(flashcards),
        module_slug=module_slug,
        module_title=study_data.get("module_title", "Unknown"),
        difficulty=difficulty
    )


@router.get("/modules/{module_slug}/quiz", response_model=QuizResponse)
async def get_quiz(
    module_slug: str,
    difficulty: Optional[Literal["easy", "medium", "hard"]] = Query(
        None, description="Filtrera på svårighetsgrad"
    ),
    shuffle: bool = Query(True, description="Slumpa ordningen på frågor"),
    shuffle_options: bool = Query(True, description="Slumpa svarsalternativens ordning"),
    limit: Optional[int] = Query(None, description="Max antal frågor att returnera")
):
    """
    Hämta quiz-frågor för en modul.

    - **difficulty**: easy, medium, eller hard (alla om ej angiven)
    - **shuffle**: Slumpa frågeordningen (default: true)
    - **shuffle_options**: Slumpa svarsalternativ så rätt svar inte alltid är A (default: true)
    - **limit**: Begränsa antal frågor
    """
    study_data = STUDY_DATA_REGISTRY.get(module_slug)

    if not study_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modul '{module_slug}' hittades inte"
        )

    questions = get_quiz_for_module(module_slug, difficulty)

    # Slumpa svarsalternativens ordning för varje fråga
    if shuffle_options:
        questions = [shuffle_quiz_options(q) for q in questions]

    # Slumpa frågeordningen
    if shuffle:
        random.shuffle(questions)

    # Begränsa antal
    if limit and limit > 0:
        questions = questions[:limit]

    return QuizResponse(
        questions=[QuizQuestion(**q) for q in questions],
        total=len(questions),
        module_slug=module_slug,
        module_title=study_data.get("module_title", "Unknown"),
        difficulty=difficulty
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
