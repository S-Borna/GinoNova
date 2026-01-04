"""
Quiz Service - AI-powered quiz generation using OpenAI GPT-4o-mini
Lazy-loads OpenAI client to avoid crashes if API key is missing.

Improvements:
- Enhanced prompts with DevOps examples and practical scenarios
- Increased content limit (8000-12000 chars)
- Optimized temperature (0.7-0.8) for consistent quality
- Increased max_tokens (3000-4000) for better explanations
- Redis caching to reduce API costs by 80-90%
"""
import os
import json
import logging
import hashlib
import random
import uuid
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


def _generate_cache_key(
    module_title: str,
    content: str,
    quiz_type: str,
    count: int,
    difficulty: str,
    focus_area: Optional[str] = None
) -> str:
    """Generate a cache key for quiz generation."""
    # Create hash from parameters (excluding content hash for exact match)
    key_parts = [
        module_title,
        quiz_type,
        str(count),
        difficulty,
        focus_area or "",
        # Hash first 1000 chars of content for cache key (not full content)
        hashlib.md5(content[:1000].encode()).hexdigest()[:16]
    ]
    key_string = "|".join(key_parts)
    return f"quiz:{hashlib.md5(key_string.encode()).hexdigest()}"


def generate_quiz(
    module_title: str,
    content: str,
    quiz_type: Literal["flashcard", "mcq"] = "mcq",
    count: int = 10,
    difficulty: Literal["beginner", "intermediate", "advanced"] = "intermediate",
    focus_area: Optional[str] = None,
    use_cache: bool = True
) -> Optional[dict]:
    """
    Generate quiz questions using OpenAI GPT-4o-mini with enhanced prompts and caching.

    Args:
        module_title: Title of the module
        content: Module content to generate questions from
        quiz_type: "flashcard" or "mcq"
        count: Number of questions (1-20)
        difficulty: Question difficulty level
        focus_area: Optional specific topic to focus on
        use_cache: Whether to use Redis cache (default: True)

    Returns:
        Dict with questions list or None if generation fails
    """
    # Check cache first
    if use_cache:
        from ..db.redis_client import cache_get, cache_set
        cache_key = _generate_cache_key(module_title, content, quiz_type, count, difficulty, focus_area)
        cached_result = cache_get(cache_key)
        if cached_result:
            logger.info(f"✅ Quiz cache hit for {module_title} ({quiz_type}, {difficulty})")
            return cached_result

    client = _get_client()
    if not client:
        return None

    # Enhanced prompt with DevOps examples and practical scenarios
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
}

Example of GOOD flashcard:
{
  "front": "What does 'docker run -d -p 8080:80 nginx' do?",
  "back": "Runs nginx container in detached mode, mapping host port 8080 to container port 80",
  "hint": "Think about -d (detached) and -p (port mapping)"
}

Example of BAD flashcard (too vague):
{
  "front": "Docker",
  "back": "Containerization"
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

Example of GOOD MCQ:
{
  "question": "You need to deploy a Python app with dependencies. Which Dockerfile layer order is MOST efficient?",
  "options": [
    "A) COPY . . && RUN pip install -r requirements.txt",
    "B) COPY requirements.txt . && RUN pip install -r requirements.txt && COPY . .",
    "C) RUN pip install -r requirements.txt && COPY . .",
    "D) COPY requirements.txt requirements.txt && COPY . . && RUN pip install"
  ],
  "correct": "B",
  "explanation": "Copying requirements.txt first allows Docker to cache the pip install layer. If only code changes, Docker reuses the cached pip install layer, making rebuilds faster."
}

IMPORTANT: 
- The correct answer should be randomly distributed across A, B, C, D - do NOT always make A the correct answer
- Vary the position of the correct answer for each question
- Make wrong answers plausible but clearly incorrect
- Focus on practical DevOps scenarios, not just definitions"""

    focus_text = f"\nFocus specifically on: {focus_area}" if focus_area else ""
    
    # Add unique variation instruction when generating fresh (not cached)
    variation_seed = ""
    if not use_cache:
        # Generate random seed for variation
        random_seed = random.randint(1000, 9999)
        unique_id = str(uuid.uuid4())[:8]
        variation_seed = f"""

IMPORTANT: Generate COMPLETELY NEW and UNIQUE questions for this session.
Session ID: {unique_id}-{random_seed}
Do NOT repeat questions from previous generations.
Pick DIFFERENT concepts and scenarios than you would normally choose.
Be creative and explore less obvious aspects of the content."""

    # Determine difficulty-specific instructions
    difficulty_instructions = {
        "beginner": """Beginner level questions should:
- Test basic concepts and definitions
- Use simple, clear language
- Focus on "what" and "when" questions
- Example: "What command lists running containers?" (docker ps)""",
        "intermediate": """Intermediate level questions should:
- Test practical application and troubleshooting
- Require understanding of how things work together
- Focus on "how" and "why" questions
- Include real-world scenarios
- Example: "Your Docker container can't connect to a database. What's the most likely cause?" (network configuration)""",
        "advanced": """Advanced level questions should:
- Test deep understanding and edge cases
- Require knowledge of best practices and trade-offs
- Focus on "what if" and optimization scenarios
- Include complex multi-step problems
- Example: "You need to scale a stateless web app to handle 10x traffic. Which approach minimizes latency?" (horizontal scaling with load balancer)"""
    }

    # Increase content limit from 4000 to 8000 chars for better context
    content_preview = content[:8000]
    if len(content) > 8000:
        content_preview += "\n\n[... content truncated for token limits ...]"

    # Enhanced system prompt with DevOps expertise
    system_prompt = """You are an expert DevOps instructor with 10+ years of experience teaching Linux, Docker, Kubernetes, CI/CD, and cloud infrastructure.

Your quiz questions should:
1. Test PRACTICAL understanding, not just memorization
2. Reflect REAL-WORLD scenarios that DevOps engineers face daily
3. Include plausible wrong answers that test understanding of common mistakes
4. Provide clear, actionable explanations that help students learn
5. Focus on concepts that matter in production environments

Return ONLY valid JSON, no markdown formatting, no extra text."""

    # Build enhanced user prompt
    prompt = f"""You are creating {difficulty}-level quiz content for the DevOps module: "{module_title}"

{difficulty_instructions.get(difficulty, difficulty_instructions["intermediate"])}

Based on this module content:
{content_preview}

Generate exactly {count} UNIQUE and DIFFERENT {quiz_type} questions.{focus_text}{variation_seed}

{format_instruction}

Quality Guidelines:
- Each question should test a specific, important concept from the content
- Wrong answers should be plausible but clearly incorrect (not trick questions)
- Explanations should be educational and help students understand the concept
- For MCQ: Distribute correct answers evenly across A, B, C, D positions
- For flashcards: Front should be specific, back should be comprehensive but concise
- Avoid questions that can be answered without reading the content
- Prioritize questions about practical application over pure memorization

Return ONLY valid JSON, no markdown code blocks, no explanatory text before or after."""

    try:
        # Higher temperature when not caching (force_new mode) for more variation
        # Lower temperature when caching for consistency
        temperature = 0.95 if not use_cache else 0.75  # More creative when generating fresh
        max_tokens = 3500 if quiz_type == "mcq" else 2500  # MCQ needs more tokens for explanations
        
        logger.info(f"🎲 Generating quiz with temperature={temperature}, use_cache={use_cache}")
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        result_text = response.choices[0].message.content.strip()

        # Clean up potential markdown formatting
        if result_text.startswith("```"):
            result_text = result_text.split("```")[1]
            if result_text.startswith("json"):
                result_text = result_text[4:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]

        result = json.loads(result_text.strip())
        
        # Log AI usage for cost tracking
        try:
            from ..services.ai_usage_service import log_ai_usage
            usage_info = response.usage
            log_ai_usage(
                feature="ai_quiz",
                model="gpt-4o-mini",
                prompt_tokens=usage_info.prompt_tokens,
                completion_tokens=usage_info.completion_tokens,
                request_type=f"{quiz_type}_{difficulty}"
            )
            cost = (usage_info.prompt_tokens / 1_000_000 * 0.15) + (usage_info.completion_tokens / 1_000_000 * 0.60)
            logger.info(f"💰 Quiz generated: {usage_info.total_tokens} tokens, ${cost:.4f}")
        except Exception as e:
            logger.debug(f"Failed to log AI usage: {e}")
        
        # Cache the result (24 hours TTL for quiz content)
        if use_cache:
            from ..db.redis_client import cache_set
            cache_set(cache_key, result, ttl=86400)  # 24 hours
            logger.info(f"💾 Quiz cached for {module_title} ({quiz_type}, {difficulty})")

        return result

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse quiz response: {e}")
        logger.debug(f"Response text: {result_text[:500]}")
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
    from src.db.seeds.content import get_all_modules
    ALL_MODULES = get_all_modules()

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
    
    # Calculate per-node limit based on total desired (8000-12000 chars)
    # Distribute more evenly across nodes
    total_desired = 10000  # Increased from 4000 to 10000
    per_node_limit = max(1500, total_desired // max(len(tasks), 1))
    
    for i, task in enumerate(tasks, 1):
        title = task.get("title", f"Node {i}")
        node_content = task.get("content", "")

        # Add node title and content (increased limit per node)
        content_parts.append(f"\n## Node {i}: {title}")
        if node_content:
            # Include more content per node for better context
            # Prioritize beginning of content (usually most important)
            if len(node_content) > per_node_limit:
                # Take first part and a sample from middle/end
                first_part = node_content[:per_node_limit - 500]
                # Try to get a representative sample
                middle_sample = node_content[len(node_content)//2:len(node_content)//2 + 200]
                content_parts.append(f"{first_part}\n[...]\n{middle_sample}")
            else:
                content_parts.append(node_content)

    # Return combined content (increased limit to 10000 chars for better context)
    combined = "\n".join(content_parts)
    # Ensure we don't exceed token limits (roughly 1 char = 0.25 tokens, so 10000 chars ≈ 2500 tokens)
    return combined[:10000]


def clear_quiz_cache(module_slug: Optional[str] = None) -> int:
    """
    Clear quiz cache for a specific module or all modules.
    
    Args:
        module_slug: Optional module slug to clear cache for. If None, clears all quiz cache.
    
    Returns:
        Number of keys deleted
    """
    from ..db.redis_client import get_redis_client
    
    client = get_redis_client()
    if not client:
        return 0
    
    try:
        if module_slug:
            # Clear cache for specific module (pattern matching)
            pattern = f"quiz:*{module_slug}*"
            keys = client.keys(pattern)
        else:
            # Clear all quiz cache
            keys = client.keys("quiz:*")
        
        if keys:
            deleted = client.delete(*keys)
            logger.info(f"🗑️  Cleared {deleted} quiz cache entries")
            return deleted
        return 0
    except Exception as e:
        logger.error(f"Failed to clear quiz cache: {e}")
        return 0
