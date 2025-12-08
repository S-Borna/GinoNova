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
            # Check OPENAI_KEY first (Railway config), then OPENAI_API_KEY
            api_key = os.getenv("OPENAI_KEY") or os.getenv("OPENAI_API_KEY")
            if not api_key:
                logger.warning("OpenAI API key not configured (checked OPENAI_KEY and OPENAI_API_KEY)")
                return None
            _openai_client = OpenAI(api_key=api_key)
            logger.info(f"OpenAI client initialized with key from: {'OPENAI_KEY' if os.getenv('OPENAI_KEY') else 'OPENAI_API_KEY'}")
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
}

IMPORTANT: The correct answer should be randomly distributed across A, B, C, D - do NOT always make A the correct answer. Vary the position of the correct answer for each question."""

    focus_text = f"\nFocus specifically on: {focus_area}" if focus_area else ""

    # Add unique seed for variation
    import random
    random_seed = random.randint(1000, 9999)

    prompt = f"""You are a DevOps expert creating {difficulty}-level quiz content for the module "{module_title}".
Session ID: {random_seed} (use this to ensure unique questions each time)

Based on this content:
{content[:4000]}

Generate exactly {count} UNIQUE and DIFFERENT {quiz_type} questions.{focus_text}

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
            temperature=0.9,
            max_tokens=2000,
            seed=random_seed
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


def get_module_content_for_quiz(module_slug: str) -> Optional[str]:
    """
    Get module content suitable for quiz generation.
    Retrieves ACTUAL node content from the module's tasks.

    Args:
        module_slug: Module slug to get content for

    Returns:
        Combined content string from all nodes or None
    """
    from src.db.seeds.modules import ALL_MODULES

    # Find the module by slug
    module_data = None
    for mod in ALL_MODULES:
        if mod.get("slug", "").lower() == module_slug.lower():
            module_data = mod
            break

    if not module_data:
        return None

    # Build content string from all node contents
    content_parts = [
        f"# Module: {module_data.get('name', module_slug)}",
        f"Description: {module_data.get('description', 'DevOps learning module')}",
        "",
    ]

    # Extract content from each task/node
    tasks = module_data.get("tasks", [])
    for i, task in enumerate(tasks, 1):
        title = task.get("title", f"Node {i}")
        node_content = task.get("content", "")

        # Add node title and first ~2000 chars of content to avoid token limits
        content_parts.append(f"\n## Node {i}: {title}")
        if node_content:
            # Truncate each node to ~2000 chars to fit within limits
            content_parts.append(node_content[:2000])

    # Return combined content (limit total to ~12000 chars for API)
    combined = "\n".join(content_parts)
    return combined[:12000]
