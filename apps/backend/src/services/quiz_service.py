"""
Quiz Service - AI-powered quiz generation using OpenAI GPT-4o-mini
Lazy-loads OpenAI client to avoid crashes if API key is missing.
"""
import os
import json
import logging
from typing import Optional, List, Literal
from datetime import datetime

logger = logging.getLogger(__name__)

# Lazy-loaded OpenAI client
_openai_client = None


def _get_client():
    """Get OpenAI client, lazy-loaded to avoid import-time crashes."""
    global _openai_client
    if _openai_client is None:
        try:
            from openai import OpenAI
            api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY")
            if not api_key:
                logger.warning("OpenAI API key not configured")
                return None
            _openai_client = OpenAI(api_key=api_key)
        except ImportError:
            logger.error("OpenAI package not installed")
            return None
    return _openai_client


def generate_quiz(
    module_title: str,
    content: str,
    quiz_type: Literal["flashcard", "mcq"] = "mcq",
    count: int = 10,
    difficulty: Literal["beginner", "intermediate", "advanced"] = "intermediate",
    focus_area: Optional[str] = None
) -> Optional[dict]:
    """
    Generate quiz questions using OpenAI GPT-4o-mini.

    Args:
        module_title: Title of the module
        content: Module content to generate questions from
        quiz_type: "flashcard" or "mcq"
        count: Number of questions (1-20)
        difficulty: Question difficulty level
        focus_area: Optional specific topic to focus on

    Returns:
        Dict with questions list or None if generation fails
    """
    client = _get_client()
    if not client:
        return None

    # Build the prompt
    if quiz_type == "flashcard":
        format_instruction = """Generate flashcards in this JSON format:
{
  "questions": [
    {
      "front": "Question or term",
      "back": "Answer or definition",
      "hint": "Optional hint"
    }
  ]
}"""
    else:
        format_instruction = """Generate multiple choice questions in this JSON format:
{
  "questions": [
    {
      "question": "The question text",
      "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
      "correct": "A",
      "explanation": "Why this answer is correct"
    }
  ]
}"""

    focus_text = f"\nFocus specifically on: {focus_area}" if focus_area else ""

    prompt = f"""You are a DevOps expert creating {difficulty}-level quiz content for the module "{module_title}".

Based on this content:
{content[:4000]}

Generate exactly {count} {quiz_type} questions.{focus_text}

{format_instruction}

Important:
- Questions should test practical understanding, not just memorization
- For {difficulty} level: {"basic concepts and definitions" if difficulty == "beginner" else "practical application and troubleshooting" if difficulty == "intermediate" else "advanced scenarios and edge cases"}
- Return ONLY valid JSON, no markdown or extra text"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a DevOps training expert. Return only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        result_text = response.choices[0].message.content.strip()

        # Clean up potential markdown formatting
        if result_text.startswith("```"):
            result_text = result_text.split("```")[1]
            if result_text.startswith("json"):
                result_text = result_text[4:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]

        return json.loads(result_text.strip())

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse quiz response: {e}")
        return None
    except Exception as e:
        logger.error(f"Quiz generation failed: {e}")
        return None


def get_module_content_for_quiz(db, module_slug: str) -> Optional[str]:
    """
    Get module content suitable for quiz generation.

    Args:
        db: Database session
        module_slug: Module slug to get content for

    Returns:
        Combined content string or None
    """
    from src.db.models import Module, Task

    module = db.query(Module).filter(Module.slug == module_slug).first()
    if not module:
        return None

    # Get tasks for this module
    tasks = db.query(Task).filter(Task.module_id == module.id).limit(20).all()

    # Build content string
    content_parts = [
        f"Module: {module.title}",
        f"Description: {module.description or 'N/A'}",
        "",
        "Tasks:"
    ]

    for task in tasks:
        content_parts.append(f"- {task.title}: {task.description or 'N/A'}")
        if task.content:
            content_parts.append(f"  Content: {task.content[:500]}")

    return "\n".join(content_parts)
