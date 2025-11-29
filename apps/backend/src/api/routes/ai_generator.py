"""
AI Content Generator API Routes
Phase 17 - AI Content Generation Engine

Endpoints for:
- Generating tasks, modules, quizzes, and packs
- Managing generation requests
- Reviewing and approving generated content
"""
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Response, HTTPException, status

from ...schemas.ai_generator import (
    GenerationType, GenerationStatus,
    GenerationInputs, GenerationRequestCreate, GenerationRequestPublic, GenerationRequestInDB,
    GeneratedTask, GeneratedModule, GeneratedQuiz, GeneratedPack,
    GeneratedContentPublic, GeneratedContentInDB,
    GeneratorStatusResponse, GenerationResultResponse,
)


router = APIRouter(prefix="/ai/generator", tags=["ai-generator"])

PHASE_VERSION = "17.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# IN-MEMORY STORAGE
# ==============================================================================

_generation_requests: dict[UUID, GenerationRequestInDB] = {}
_generated_content: dict[UUID, GeneratedContentInDB] = {}


# ==============================================================================
# AI GENERATION LOGIC (Mock for now - integrate with OpenAI later)
# ==============================================================================

def _generate_task_content(inputs: GenerationInputs) -> GeneratedTask:
    """Generate a task based on inputs"""
    topic = inputs.topic
    difficulty = inputs.difficulty
    
    # Mock generation - in production, this calls OpenAI
    content_markdown = f"""# {topic}

## Introduction

In this task, you'll learn about **{topic}** - a fundamental concept in DevOps.

## Learning Objectives

By the end of this task, you will be able to:
- Understand the core concepts of {topic}
- Apply {topic} in real-world scenarios
- Troubleshoot common issues related to {topic}

## Prerequisites

Before starting, make sure you have:
- Basic understanding of Linux/Unix
- Access to a terminal
- Docker installed (optional)

## The Basics

{topic} is essential for modern DevOps workflows. Let's break it down:

### Key Concepts

1. **Concept One**: The foundation of {topic}
2. **Concept Two**: How {topic} integrates with other tools
3. **Concept Three**: Best practices for {topic}

## Hands-On Practice

Let's put this into practice:

```bash
# Example command for {topic}
echo "Learning {topic}!"
```

## Common Mistakes

- Mistake 1: Not understanding the basics first
- Mistake 2: Skipping the documentation
- Mistake 3: Not practicing in a safe environment

## Summary

You've learned the fundamentals of {topic}. Keep practicing!

---

*💡 Tip: Practice makes perfect. Try these commands in your own environment.*
"""

    hints = [
        f"Start by understanding what {topic} does at a high level",
        "Read the official documentation before diving in",
        "Practice in a sandbox environment first",
    ]
    
    code_examples = [
        {
            "language": "bash",
            "code": f"# Basic {topic} example\necho 'Hello {topic}'",
            "explanation": f"A simple example demonstrating {topic}",
        },
        {
            "language": "yaml",
            "code": f"# {topic} configuration\nname: {topic.lower().replace(' ', '-')}\nenabled: true",
            "explanation": f"Configuration file for {topic}",
        },
    ]
    
    quiz_questions = [
        {
            "type": "quiz",
            "question": f"What is the primary purpose of {topic}?",
            "options": [
                {"text": "Option A: To automate tasks", "is_correct": True, "feedback": "Correct!"},
                {"text": "Option B: To slow down processes", "is_correct": False, "feedback": "Not quite."},
                {"text": "Option C: To remove automation", "is_correct": False, "feedback": "Think again."},
            ],
            "explanation": f"{topic} is primarily used to automate and streamline DevOps workflows.",
        },
    ]
    
    xp_map = {"beginner": 20, "intermediate": 30, "advanced": 50}
    time_map = {"beginner": 10, "intermediate": 20, "advanced": 35}
    
    return GeneratedTask(
        title=topic,
        description=f"Learn the fundamentals of {topic} and how to apply it in DevOps workflows.",
        content_markdown=content_markdown,
        difficulty="easy" if difficulty == "beginner" else ("hard" if difficulty == "advanced" else "medium"),
        estimated_minutes=time_map.get(difficulty, 20),
        xp_reward=xp_map.get(difficulty, 30),
        tags=[topic.lower().replace(" ", "-"), "devops", difficulty],
        code_examples=code_examples if inputs.include_examples else [],
        hints=hints if inputs.include_hints else [],
        quiz_questions=quiz_questions,
        solution_markdown=f"## Solution\n\nThe key to mastering {topic} is practice and understanding the underlying concepts.",
    )


def _generate_module_content(inputs: GenerationInputs) -> GeneratedModule:
    """Generate a module with tasks"""
    topic = inputs.topic
    num_tasks = inputs.num_tasks or 6
    
    # Generate tasks
    task_topics = [
        f"Introduction to {topic}",
        f"Setting up {topic}",
        f"{topic} Configuration",
        f"{topic} Best Practices",
        f"Advanced {topic}",
        f"Troubleshooting {topic}",
        f"{topic} in Production",
        f"{topic} Security",
    ][:num_tasks]
    
    tasks = []
    for i, task_topic in enumerate(task_topics):
        task_inputs = GenerationInputs(
            topic=task_topic,
            difficulty=inputs.difficulty,
            num_tasks=None,
            num_questions=None,
            include_examples=inputs.include_examples,
            include_hints=inputs.include_hints,
        )
        task = _generate_task_content(task_inputs)
        tasks.append(task)
    
    slug = topic.lower().replace(" ", "-").replace("_", "-")
    
    return GeneratedModule(
        name=topic,
        slug=slug,
        description=f"Master {topic} from beginner to advanced. This module covers everything you need to know.",
        difficulty=inputs.difficulty,
        estimated_hours=round(sum(t.estimated_minutes for t in tasks) / 60, 1),
        learning_objectives=[
            f"Understand the fundamentals of {topic}",
            f"Configure and set up {topic}",
            f"Apply {topic} best practices",
            f"Troubleshoot common {topic} issues",
        ],
        prerequisites=inputs.learning_goals[:3] if inputs.learning_goals else [],
        tags=[slug, "devops", inputs.difficulty],
        tasks=tasks,
        summary_markdown=f"## Module Summary\n\nIn this module, you learned everything about {topic}.",
    )


def _generate_quiz_content(inputs: GenerationInputs) -> GeneratedQuiz:
    """Generate a quiz"""
    topic = inputs.topic
    num_questions = inputs.num_questions or 5
    
    questions = []
    for i in range(num_questions):
        questions.append({
            "type": "quiz",
            "question": f"Question {i+1}: What is an important aspect of {topic}?",
            "options": [
                {"text": "Correct answer about " + topic, "is_correct": True, "feedback": "Well done!"},
                {"text": "Wrong answer 1", "is_correct": False, "feedback": "Not quite right."},
                {"text": "Wrong answer 2", "is_correct": False, "feedback": "Try again."},
                {"text": "Wrong answer 3", "is_correct": False, "feedback": "Think about it more."},
            ],
            "explanation": f"This question tests your understanding of {topic}.",
            "xp_bonus": 5,
        })
    
    return GeneratedQuiz(
        title=f"{topic} Quiz",
        description=f"Test your knowledge of {topic}",
        difficulty=inputs.difficulty,
        questions=questions,
        passing_score=70,
        time_limit_minutes=num_questions * 2,
    )


def _generate_pack_content(inputs: GenerationInputs) -> GeneratedPack:
    """Generate a marketplace pack"""
    topic = inputs.topic
    
    # Generate modules for the pack
    module_topics = [
        f"{topic} Fundamentals",
        f"Advanced {topic}",
        f"{topic} in Production",
    ]
    
    modules = []
    for mod_topic in module_topics:
        mod_inputs = GenerationInputs(
            topic=mod_topic,
            difficulty=inputs.difficulty,
            num_tasks=4,
            num_questions=None,
            include_examples=inputs.include_examples,
            include_hints=inputs.include_hints,
        )
        module = _generate_module_content(mod_inputs)
        modules.append(module)
    
    total_hours = sum(m.estimated_hours for m in modules)
    
    return GeneratedPack(
        title=f"{topic} Mastery Pack",
        description=f"Complete {topic} training from fundamentals to production-ready skills.",
        short_description=f"Master {topic} with this comprehensive pack",
        difficulty=inputs.difficulty,
        estimated_hours=total_hours,
        tags=[topic.lower().replace(" ", "-"), "pack", inputs.difficulty],
        modules=modules,
        suggested_price_cents=4999 if inputs.difficulty == "advanced" else 2999,
    )


# ==============================================================================
# API ENDPOINTS
# ==============================================================================

@router.get("/status", response_model=GeneratorStatusResponse)
def generator_status(response: Response):
    """Get AI generator status"""
    add_phase_header(response)
    
    pending = len([r for r in _generation_requests.values() if r.status == "pending"])
    total = len(_generated_content)
    
    return GeneratorStatusResponse(
        status="operational",
        phase=PHASE_VERSION,
        capabilities=[
            "generate_task",
            "generate_module",
            "generate_quiz",
            "generate_pack",
            "generate_hints",
            "generate_examples",
        ],
        pending_requests=pending,
        total_generated=total,
    )


@router.post("/task", response_model=GenerationResultResponse, status_code=status.HTTP_201_CREATED)
def generate_task(data: GenerationRequestCreate, response: Response):
    """Generate a new task"""
    add_phase_header(response)
    
    if data.type != "task":
        data.type = "task"
    
    # Create request
    request = GenerationRequestInDB(
        id=uuid4(),
        type="task",
        inputs=data.inputs,
        status="generating",
    )
    _generation_requests[request.id] = request
    
    try:
        # Generate content
        task = _generate_task_content(data.inputs)
        
        # Store generated content
        content = GeneratedContentInDB(
            id=uuid4(),
            request_id=request.id,
            type="task",
            status="completed",
            output_json=task.model_dump(),
            task=task,
        )
        _generated_content[content.id] = content
        
        # Update request
        request.status = "completed"
        request.completed_at = datetime.utcnow()
        
        return GenerationResultResponse(
            request=GenerationRequestPublic(**request.model_dump()),
            content=GeneratedContentPublic(**content.model_dump()),
        )
    except Exception as e:
        request.status = "failed"
        request.error_message = str(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Generation failed: {str(e)}"
        )


@router.post("/module", response_model=GenerationResultResponse, status_code=status.HTTP_201_CREATED)
def generate_module(data: GenerationRequestCreate, response: Response):
    """Generate a new module with tasks"""
    add_phase_header(response)
    
    if data.type != "module":
        data.type = "module"
    
    request = GenerationRequestInDB(
        id=uuid4(),
        type="module",
        inputs=data.inputs,
        status="generating",
    )
    _generation_requests[request.id] = request
    
    try:
        module = _generate_module_content(data.inputs)
        
        content = GeneratedContentInDB(
            id=uuid4(),
            request_id=request.id,
            type="module",
            status="completed",
            output_json=module.model_dump(),
            module=module,
        )
        _generated_content[content.id] = content
        
        request.status = "completed"
        request.completed_at = datetime.utcnow()
        
        return GenerationResultResponse(
            request=GenerationRequestPublic(**request.model_dump()),
            content=GeneratedContentPublic(**content.model_dump()),
        )
    except Exception as e:
        request.status = "failed"
        request.error_message = str(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Generation failed: {str(e)}"
        )


@router.post("/quiz", response_model=GenerationResultResponse, status_code=status.HTTP_201_CREATED)
def generate_quiz(data: GenerationRequestCreate, response: Response):
    """Generate a quiz"""
    add_phase_header(response)
    
    if data.type != "quiz":
        data.type = "quiz"
    
    request = GenerationRequestInDB(
        id=uuid4(),
        type="quiz",
        inputs=data.inputs,
        status="generating",
    )
    _generation_requests[request.id] = request
    
    try:
        quiz = _generate_quiz_content(data.inputs)
        
        content = GeneratedContentInDB(
            id=uuid4(),
            request_id=request.id,
            type="quiz",
            status="completed",
            output_json=quiz.model_dump(),
            quiz=quiz,
        )
        _generated_content[content.id] = content
        
        request.status = "completed"
        request.completed_at = datetime.utcnow()
        
        return GenerationResultResponse(
            request=GenerationRequestPublic(**request.model_dump()),
            content=GeneratedContentPublic(**content.model_dump()),
        )
    except Exception as e:
        request.status = "failed"
        request.error_message = str(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Generation failed: {str(e)}"
        )


@router.post("/pack", response_model=GenerationResultResponse, status_code=status.HTTP_201_CREATED)
def generate_pack(data: GenerationRequestCreate, response: Response):
    """Generate a marketplace pack"""
    add_phase_header(response)
    
    if data.type != "pack":
        data.type = "pack"
    
    request = GenerationRequestInDB(
        id=uuid4(),
        type="pack",
        inputs=data.inputs,
        status="generating",
    )
    _generation_requests[request.id] = request
    
    try:
        pack = _generate_pack_content(data.inputs)
        
        content = GeneratedContentInDB(
            id=uuid4(),
            request_id=request.id,
            type="pack",
            status="completed",
            output_json=pack.model_dump(),
            pack=pack,
        )
        _generated_content[content.id] = content
        
        request.status = "completed"
        request.completed_at = datetime.utcnow()
        
        return GenerationResultResponse(
            request=GenerationRequestPublic(**request.model_dump()),
            content=GeneratedContentPublic(**content.model_dump()),
        )
    except Exception as e:
        request.status = "failed"
        request.error_message = str(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Generation failed: {str(e)}"
        )


@router.get("/results", response_model=List[GenerationResultResponse])
def list_generated_content(
    type: Optional[GenerationType] = None,
    status: Optional[GenerationStatus] = None,
    limit: int = 20,
    response: Optional[Response] = None,
):
    """List generated content"""
    if response:
        add_phase_header(response)
    
    results = []
    
    for content in _generated_content.values():
        if type and content.type != type:
            continue
        if status and content.status != status:
            continue
        
        request = _generation_requests.get(content.request_id)
        if request:
            results.append(GenerationResultResponse(
                request=GenerationRequestPublic(**request.model_dump()),
                content=GeneratedContentPublic(**content.model_dump()),
            ))
    
    # Sort by created_at desc
    results.sort(key=lambda r: r.request.created_at, reverse=True)
    
    return results[:limit]


@router.get("/result/{content_id}", response_model=GenerationResultResponse)
def get_generated_content(content_id: UUID, response: Response):
    """Get specific generated content"""
    add_phase_header(response)
    
    content = _generated_content.get(content_id)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Generated content not found"
        )
    
    request = _generation_requests.get(content.request_id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Generation request not found"
        )
    
    return GenerationResultResponse(
        request=GenerationRequestPublic(**request.model_dump()),
        content=GeneratedContentPublic(**content.model_dump()),
    )


@router.post("/result/{content_id}/approve", response_model=GeneratedContentPublic)
def approve_content(content_id: UUID, response: Response):
    """Approve generated content for publishing"""
    add_phase_header(response)
    
    content = _generated_content.get(content_id)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Generated content not found"
        )
    
    content.status = "approved"
    content.approved_at = datetime.utcnow()
    # content.approved_by = current_user.id  # TODO: Get from auth
    
    return GeneratedContentPublic(**content.model_dump())


@router.post("/result/{content_id}/reject", response_model=GeneratedContentPublic)
def reject_content(content_id: UUID, response: Response):
    """Reject generated content"""
    add_phase_header(response)
    
    content = _generated_content.get(content_id)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Generated content not found"
        )
    
    content.status = "rejected"
    
    return GeneratedContentPublic(**content.model_dump())
