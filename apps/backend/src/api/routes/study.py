"""
Study API Routes - Static flashcards and quiz from V2 nodes
No AI required - pulls questions directly from module content.
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
import random

router = APIRouter(prefix="/study", tags=["study"])


# === Schemas ===

class Flashcard(BaseModel):
    id: str
    front: str
    back: str
    module_slug: str
    lesson_title: str


class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct: int
    explanation: Optional[str] = None
    module_slug: str
    lesson_title: str


class StudyModule(BaseModel):
    slug: str
    title: str
    description: str
    icon: str
    lesson_count: int
    flashcard_count: int
    quiz_count: int


class StudyLesson(BaseModel):
    id: str
    title: str
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


# === Data Sources ===
# Import V2 nodes to extract quiz content

def get_linux_v2_data():
    """Get Linux V2 nodes with quiz data"""
    from src.db.seeds.skillsmaps.linux.node_1_process_v2 import LINUX_NODE_1_PROCESS_V2
    from src.db.seeds.skillsmaps.linux.node_2_filesystem_v2 import LINUX_NODE_2_FILESYSTEM_V2
    from src.db.seeds.skillsmaps.linux.node_3_fileops_v2 import LINUX_NODE_3_FILEOPS_V2
    from src.db.seeds.skillsmaps.linux.node_4_permissions_v2 import LINUX_NODE_4_PERMISSIONS_V2
    from src.db.seeds.skillsmaps.linux.node_5_textproc_v2 import LINUX_NODE_5_TEXTPROC_V2

    return [
        LINUX_NODE_1_PROCESS_V2,
        LINUX_NODE_2_FILESYSTEM_V2,
        LINUX_NODE_3_FILEOPS_V2,
        LINUX_NODE_4_PERMISSIONS_V2,
        LINUX_NODE_5_TEXTPROC_V2,
    ]


def get_docker_v2_data():
    """Get Docker V2 nodes with quiz data"""
    try:
        from src.db.seeds.skillsmaps.docker.nodes_v2 import ALL_DOCKER_V2_NODES
        return ALL_DOCKER_V2_NODES
    except ImportError:
        return []


def extract_flashcards_from_node(node: dict, module_slug: str) -> List[Flashcard]:
    """Extract flashcards from a V2 node"""
    flashcards = []
    lesson_title = node.get("title", "Unknown")

    for section in node.get("sections", []):
        if section.get("type") == "quiz":
            content = section.get("content", {})
            questions = content.get("questions", {})

            for i, fc in enumerate(questions.get("flashcards", [])):
                flashcards.append(Flashcard(
                    id=f"{module_slug}-{node.get('node_id', 0)}-fc-{i}",
                    front=fc.get("front", ""),
                    back=fc.get("back", ""),
                    module_slug=module_slug,
                    lesson_title=lesson_title
                ))

    return flashcards


def extract_quiz_from_node(node: dict, module_slug: str) -> List[QuizQuestion]:
    """Extract multiple choice questions from a V2 node"""
    questions = []
    lesson_title = node.get("title", "Unknown")

    for section in node.get("sections", []):
        if section.get("type") == "quiz":
            content = section.get("content", {})
            quiz_questions = content.get("questions", {})

            for i, q in enumerate(quiz_questions.get("multiple_choice", [])):
                questions.append(QuizQuestion(
                    id=f"{module_slug}-{node.get('node_id', 0)}-mc-{i}",
                    question=q.get("question", ""),
                    options=q.get("options", []),
                    correct=q.get("correct", 0),
                    explanation=q.get("explanation"),
                    module_slug=module_slug,
                    lesson_title=lesson_title
                ))

    return questions


# === Module Registry ===

STUDY_MODULES = {
    "linux-mastery": {
        "slug": "linux-mastery",
        "title": "Linux Mastery",
        "description": "Komplett Linux-kurs på svenska för DevOps",
        "icon": "Terminal",
        "get_data": get_linux_v2_data
    },
    "docker-containers": {
        "slug": "docker-containers",
        "title": "Docker & Containers",
        "description": "Container-teknologi och Docker för DevOps",
        "icon": "Box",
        "get_data": get_docker_v2_data
    },
}


# === Endpoints ===

@router.get("/modules", response_model=List[StudyModule])
async def list_study_modules():
    """Get all modules available for study with flashcards/quiz"""
    result = []

    for slug, module_info in STUDY_MODULES.items():
        try:
            nodes = module_info["get_data"]()

            flashcard_count = 0
            quiz_count = 0

            for node in nodes:
                flashcard_count += len(extract_flashcards_from_node(node, slug))
                quiz_count += len(extract_quiz_from_node(node, slug))

            result.append(StudyModule(
                slug=slug,
                title=module_info["title"],
                description=module_info["description"],
                icon=module_info["icon"],
                lesson_count=len(nodes),
                flashcard_count=flashcard_count,
                quiz_count=quiz_count
            ))
        except Exception as e:
            print(f"Error loading module {slug}: {e}")
            continue

    return result


@router.get("/modules/{module_slug}", response_model=StudyModuleDetail)
async def get_study_module(module_slug: str):
    """Get module details with lessons"""
    if module_slug not in STUDY_MODULES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{module_slug}' not found"
        )

    module_info = STUDY_MODULES[module_slug]
    nodes = module_info["get_data"]()

    lessons = []
    for node in nodes:
        flashcards = extract_flashcards_from_node(node, module_slug)
        quiz_questions = extract_quiz_from_node(node, module_slug)

        lessons.append(StudyLesson(
            id=f"{module_slug}-{node.get('node_id', 0)}",
            title=node.get("title", "Unknown"),
            flashcard_count=len(flashcards),
            quiz_count=len(quiz_questions)
        ))

    return StudyModuleDetail(
        slug=module_slug,
        title=module_info["title"],
        description=module_info["description"],
        icon=module_info["icon"],
        lessons=lessons
    )


@router.get("/modules/{module_slug}/flashcards", response_model=FlashcardsResponse)
async def get_flashcards(
    module_slug: str,
    lessons: Optional[str] = None,  # Comma-separated lesson IDs
    shuffle: bool = False
):
    """Get flashcards for a module, optionally filtered by lessons"""
    if module_slug not in STUDY_MODULES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{module_slug}' not found"
        )

    module_info = STUDY_MODULES[module_slug]
    nodes = module_info["get_data"]()

    # Parse lesson filter
    lesson_filter = None
    if lessons:
        lesson_filter = set(lessons.split(","))

    all_flashcards = []
    for node in nodes:
        lesson_id = f"{module_slug}-{node.get('node_id', 0)}"

        # Skip if not in filter
        if lesson_filter and lesson_id not in lesson_filter:
            continue

        flashcards = extract_flashcards_from_node(node, module_slug)
        all_flashcards.extend(flashcards)

    # Shuffle if requested
    if shuffle:
        random.shuffle(all_flashcards)

    return FlashcardsResponse(
        flashcards=all_flashcards,
        total=len(all_flashcards)
    )


@router.get("/modules/{module_slug}/quiz", response_model=QuizResponse)
async def get_quiz(
    module_slug: str,
    lessons: Optional[str] = None,  # Comma-separated lesson IDs
    shuffle: bool = False
):
    """Get quiz questions for a module, optionally filtered by lessons"""
    if module_slug not in STUDY_MODULES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module '{module_slug}' not found"
        )

    module_info = STUDY_MODULES[module_slug]
    nodes = module_info["get_data"]()

    # Parse lesson filter
    lesson_filter = None
    if lessons:
        lesson_filter = set(lessons.split(","))

    all_questions = []
    for node in nodes:
        lesson_id = f"{module_slug}-{node.get('node_id', 0)}"

        # Skip if not in filter
        if lesson_filter and lesson_id not in lesson_filter:
            continue

        questions = extract_quiz_from_node(node, module_slug)
        all_questions.extend(questions)

    # Shuffle if requested
    if shuffle:
        random.shuffle(all_questions)

    return QuizResponse(
        questions=all_questions,
        total=len(all_questions)
    )
