"""
Quiz Service - AI-powered quiz generation using OpenAI GPT-4o-mini
Now with ASYNC support to prevent blocking the server.

Improvements:
- ASYNC OpenAI calls - doesn't block other requests
- Parallel batch generation for large quiz counts (100 questions = 5x20 parallel)
- Enhanced prompts with DevOps examples and practical scenarios
- Redis caching to reduce API costs by 80-90%
"""
import os
import json
import logging
import hashlib
import random
import uuid
import asyncio
from typing import Optional, List, Literal
from datetime import datetime

logger = logging.getLogger(__name__)

# Lazy-loaded OpenAI clients (sync and async)
_openai_client = None
_async_openai_client = None


def _get_client():
    """Get sync OpenAI client (legacy, avoid using)."""
    global _openai_client
    if _openai_client is None:
        try:
            from openai import OpenAI
            api_key = os.getenv("OPENAI_KEY") or os.getenv("OPENAI_API_KEY")
            if not api_key:
                logger.error("❌ OpenAI API key not configured")
                return None
            _openai_client = OpenAI(api_key=api_key, timeout=30.0)
            logger.info("✅ Sync OpenAI client initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize OpenAI client: {e}")
            return None
    return _openai_client


def _get_async_client():
    """Get async OpenAI client for non-blocking requests."""
    global _async_openai_client
    if _async_openai_client is None:
        try:
            from openai import AsyncOpenAI
            api_key = os.getenv("OPENAI_KEY") or os.getenv("OPENAI_API_KEY")
            if not api_key:
                logger.error("❌ OpenAI API key not configured")
                return None
            _async_openai_client = AsyncOpenAI(api_key=api_key, timeout=60.0)
            logger.info("✅ Async OpenAI client initialized")
        except Exception as e:
            logger.error(f"❌ Failed to initialize async OpenAI client: {e}")
            return None
    return _async_openai_client


def _randomize_mcq_options(questions: List[dict]) -> List[dict]:
    """
    Randomisera svarsalternativens position för MCQ-frågor.
    Säkerställer att rätt svar inte alltid är på samma position.
    """
    letters = ['A', 'B', 'C', 'D']

    for q in questions:
        if 'options' not in q or 'correct' not in q:
            continue

        options = q['options']
        if len(options) != 4:
            continue

        # Hitta index för rätt svar
        correct_letter = q['correct'].strip().upper()
        if correct_letter not in letters:
            continue
        correct_idx = letters.index(correct_letter)

        # Ta bort bokstavsprefixet från options (om det finns)
        clean_options = []
        for opt in options:
            # Ta bort "A) ", "B) ", etc.
            if len(opt) > 3 and opt[0] in letters and opt[1] == ')':
                clean_options.append(opt[3:].strip())
            elif len(opt) > 2 and opt[0] in letters and opt[1] == '.':
                clean_options.append(opt[2:].strip())
            else:
                clean_options.append(opt)

        # Spara rätt svar
        correct_answer = clean_options[correct_idx]

        # Slumpa ordningen
        random.shuffle(clean_options)

        # Hitta nya positionen för rätt svar
        new_correct_idx = clean_options.index(correct_answer)
        new_correct_letter = letters[new_correct_idx]

        # Uppdatera med nya bokstavsprefixer
        q['options'] = [f"{letters[i]}) {clean_options[i]}" for i in range(4)]
        q['correct'] = new_correct_letter

    return questions


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
        logger.error("❌ OpenAI client not available - check OPENAI_KEY or OPENAI_API_KEY env var")
        raise ValueError("OpenAI API key not configured")

    # Enhanced prompt with DevOps examples and practical scenarios - ENGLISH
    if quiz_type == "flashcard":
        format_instruction = """Generate flashcards in ENGLISH in this JSON format:
{
  "questions": [
    {
      "front": "Question or term (IN ENGLISH)",
      "back": "Answer or definition (IN ENGLISH)",
      "hint": "Optional hint (IN ENGLISH)"
    }
  ]
}

Example of a GOOD flashcard:
{
  "front": "What does the command 'docker run -d -p 8080:80 nginx' do?",
  "back": "Runs nginx container in detached mode (background) and maps host port 8080 to container port 80",
  "hint": "Think about -d (detached) and -p (port mapping)"
}

Example of a BAD flashcard (too vague):
{
  "front": "Docker",
  "back": "Containerization"
}

IMPORTANT: All content must be in ENGLISH!"""
    else:
        format_instruction = """Generate multiple choice questions in ENGLISH in this JSON format:
{
  "questions": [
    {
      "question": "The question text (IN ENGLISH)",
      "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
      "correct": "A",
      "explanation": "Explanation of why this answer is correct (IN ENGLISH)"
    }
  ]
}

CRITICAL FOR ANSWER DISTRIBUTION:
- Distribute correct answers EVENLY across A, B, C, D
- If generating 20 questions, approximately 5 should have A correct, 5 B, 5 C, 5 D
- NEVER have more than 30% of answers on the same letter
- Actively vary where the correct answer is placed

⚠️ CRITICAL FOR ANSWER LENGTH - AVOID REVEALING THE CORRECT ANSWER:
- ALL four answer options MUST be APPROXIMATELY THE SAME LENGTH (max 20% difference)
- The correct answer must NOT be more detailed or longer than incorrect ones
- If the correct answer is short (e.g., "docker ps"), make incorrect answers equally short
- If the correct answer needs to be long, make ALL options equally long and detailed
- Incorrect answers should be EQUALLY CONVINCING as the correct one
- Avoid having only the correct answer include examples or details

Example of a GOOD multiple choice question:
{
  "question": "You need to deploy a Python app with dependencies. Which Dockerfile layer order is MOST efficient?",
  "options": [
    "A) COPY . . && RUN pip install -r requirements.txt",
    "B) COPY requirements.txt . && RUN pip install -r requirements.txt && COPY . .",
    "C) RUN pip install -r requirements.txt && COPY . .",
    "D) COPY requirements.txt requirements.txt && COPY . . && RUN pip install"
  ],
  "correct": "B",
  "explanation": "By copying requirements.txt first, Docker can cache the pip install layer."
}

IMPORTANT:
- Generate EXACTLY the number of questions requested - no fewer!
- Distribute correct answers EVENLY (25% A, 25% B, 25% C, 25% D)
- Make incorrect answers plausible but clearly wrong
- ALL content must be in ENGLISH!"""

    focus_text = f"\nFocus specifically on: {focus_area}" if focus_area else ""

    # Add unique variation instruction when generating fresh (not cached) - SWEDISH
    # ALWAYS add variation seed to ensure unique questions every time
    # Generate timestamp-based seed for maximum uniqueness
    import time
    timestamp = int(time.time() * 1000)  # millisecond precision
    random_seed = random.randint(1000, 9999)
    unique_id = str(uuid.uuid4())[:8]

    variation_seed = f"""

🔥 CRITICAL: Generate COMPLETELY NEW and UNIQUE questions for this session!

Session Identifiers:
- Unique ID: {unique_id}
- Random Seed: {random_seed}
- Timestamp: {timestamp}
- Difficulty Level: {difficulty.upper()}

⚠️ DIFFICULTY ENFORCEMENT:
The selected difficulty is "{difficulty.upper()}". You MUST:
- Generate questions ONLY appropriate for {difficulty.upper()} level
- Questions for BEGINNER must be simpler than INTERMEDIATE
- Questions for INTERMEDIATE must be simpler than ADVANCED
- A question suitable for BEGINNER should NEVER appear in ADVANCED quiz
- The same topic can appear across difficulties but with VERY different complexity

Instructions for UNIQUE questions:
1. NEVER repeat questions from previous sessions
2. Choose DIFFERENT concepts than you normally would
3. Explore UNUSUAL aspects of the content
4. Use VARYING scenarios and examples
5. Be CREATIVE and AVOID obvious questions
6. Focus on PRACTICAL edge cases and real-world situations
7. ⚠️ NEVER have duplicate questions within the same quiz - each question MUST be different
8. ⚠️ Ensure ALL questions match the {difficulty.upper()} difficulty level STRICTLY

If you have generated questions for this module before:
- Choose COMPLETELY DIFFERENT topics from the content
- Use DIFFERENT commands and tools
- Create NEW scenarios you haven't used before

Write EVERYTHING in ENGLISH!"""

    # Determine difficulty-specific instructions - ENGLISH
    # These are VERY different to ensure distinct question sets per difficulty
    difficulty_instructions = {
        "beginner": """🟢 BEGINNER LEVEL - STRICTLY FOLLOW THESE RULES:

Question characteristics:
- Test BASIC concepts, definitions, and simple facts
- Use simple, clear, straightforward language
- Focus on "what is" and "which command" questions
- Single-step problems only - NO multi-step reasoning
- Test recognition and recall, NOT analysis

Topic restrictions for BEGINNER:
- Basic command syntax (ls, cd, pwd, cat, echo)
- Simple file operations (create, copy, move, delete)
- Basic concepts (what is a container, what is a process)
- Definition questions (what does X mean)

⚠️ FORBIDDEN for beginner level:
- Troubleshooting scenarios
- "Best practice" questions
- Performance optimization
- Security implications
- Multi-step procedures
- Edge cases or exceptions

Example GOOD beginner question:
"Which command displays the current working directory?"
A) pwd  B) cwd  C) dir  D) path

Example BAD beginner question (too complex):
"Your Docker container fails to start. What should you check first?" """,

        "intermediate": """🟡 INTERMEDIATE LEVEL - STRICTLY FOLLOW THESE RULES:

Question characteristics:
- Test practical application and basic troubleshooting
- Require understanding of how components work together
- Focus on "how to" and "why does" questions
- Include realistic workplace scenarios
- Test understanding, NOT just recall

Topic restrictions for INTERMEDIATE:
- Command combinations and pipelines
- Basic troubleshooting (why doesn't X work)
- Configuration and setup procedures
- Comparing similar tools/approaches
- Understanding output and logs

⚠️ FORBIDDEN for intermediate level:
- Simple definition questions (those are beginner)
- Complex optimization scenarios (those are advanced)
- Multi-system architecture decisions
- Security hardening beyond basics

Example GOOD intermediate question:
"Your colleague runs 'docker ps' but doesn't see their container. It was running yesterday. What is the most likely explanation?"
A) Container crashed  B) Docker daemon stopped  C) Container was deleted  D) Network issue

Example BAD intermediate question (too simple):
"What command lists files?" """,

        "advanced": """🔴 ADVANCED LEVEL - STRICTLY FOLLOW THESE RULES:

Question characteristics:
- Test deep understanding, edge cases, and expert knowledge
- Require knowledge of best practices and trade-offs
- Focus on "what if", optimization, and architecture decisions
- Include complex multi-step problems
- Test analysis and synthesis, NOT just understanding

Topic restrictions for ADVANCED:
- Performance tuning and optimization
- Security hardening and best practices
- Architecture decisions and trade-offs
- Edge cases and failure scenarios
- Production-grade configurations
- Debugging complex issues

⚠️ FORBIDDEN for advanced level:
- Simple "what is" questions (those are beginner)
- Basic troubleshooting (that's intermediate)
- Questions answerable by reading documentation once

Example GOOD advanced question:
"You're designing a CI/CD pipeline for a microservices app with 50 services. Which strategy minimizes deployment risk while maximizing deployment frequency?"
A) Blue-green with canary  B) Rolling updates only  C) Big-bang releases  D) Feature flags only

Example BAD advanced question (too simple):
"What does the -d flag do in docker run?" """
    }

    # Increase content limit from 4000 to 8000 chars for better context
    content_preview = content[:8000]
    if len(content) > 8000:
        content_preview += "\n\n[... content truncated for token limits ...]"

    # Enhanced system prompt with DevOps expertise - ENGLISH
    system_prompt = """You are an expert DevOps instructor creating quiz questions.

🚨 ABSOLUTE RULE #1: BASE ALL QUESTIONS ON THE PROVIDED CONTENT ONLY!
- You MUST generate questions EXCLUSIVELY from the module content provided below
- NEVER invent topics, commands, or concepts not mentioned in the content
- If the content is about Docker, ask about Docker - NOT about Kubernetes unless mentioned
- If the content is about file permissions, ask about permissions - NOT about networking unless mentioned
- Every question MUST be directly traceable to something in the provided content

🚨 ABSOLUTE RULE #2: GENERATE IN ENGLISH ONLY!
- All questions, answers, explanations must be in English

Your quiz questions should:
1. Test understanding of concepts ACTUALLY PRESENT in the provided content
2. Use examples and scenarios that relate to the module's specific topics
3. Include plausible incorrect answers based on common mistakes for THAT topic
4. Provide explanations that reference the module content

Return ONLY valid JSON, no markdown formatting, no extra text."""

    # Build enhanced user prompt - ENGLISH
    difficulty_label = {"beginner": "beginner", "intermediate": "intermediate", "advanced": "advanced"}.get(difficulty, "intermediate")
    difficulty_guide = difficulty_instructions.get(difficulty, difficulty_instructions["intermediate"])

    prompt = f"""You are creating {difficulty_label} level quiz content for the DevOps module: "{module_title}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 CONTENT-BASED GENERATION - READ THIS CAREFULLY!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The module content below is your ONLY source of truth. You MUST:

✅ REQUIRED:
- Generate questions ONLY about topics explicitly mentioned in the content
- Use commands, tools, and concepts that appear in the content
- Reference scenarios and examples similar to those in the content
- Match the technical domain of the content (if it's about SSH, ask about SSH)

❌ FORBIDDEN:
- Inventing topics not present in the content
- Asking about tools/commands not mentioned in the content
- Assuming the content covers general DevOps when it's specific
- Adding your own "common knowledge" that isn't in the provided text

DIFFICULTY LEVEL: {difficulty_label.upper()}
Apply this difficulty to the content topics - don't change WHAT you ask about, 
change HOW COMPLEX the questions are about those same topics.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 MODULE CONTENT (YOUR ONLY SOURCE):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{content_preview}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{difficulty_guide}

⚠️ CRITICAL: Generate EXACTLY {count} questions - no fewer, no more!
⚠️ CRITICAL: ALL questions must be about topics IN THE CONTENT ABOVE!

{format_instruction}

Quality guidelines:
- Each question MUST test a concept that appears in the module content above
- If a topic isn't in the content, DO NOT ask about it
- Incorrect answers should be plausible alternatives within the content's domain
- Explanations should ideally reference the module content
- ⚠️ ALL answer options must be EQUAL LENGTH

IMPORTANT:
1. Generate EXACTLY {count} questions (this is a REQUIREMENT)
2. ALL content in ENGLISH!
3. ⚠️ ONLY ask about topics from the provided module content!
{focus_text}{variation_seed}

Return ONLY valid JSON, no markdown code blocks, no extra text."""

    try:
        # Higher temperature when not caching (force_new mode) for more variation
        temperature = 0.95 if not use_cache else 0.8

        # Scale max_tokens based on question count - INCREASED for more questions
        # MCQ: ~250 tokens per question, Flashcard: ~150 tokens per question
        base_tokens = 300 if quiz_type == "mcq" else 180
        max_tokens = min(count * base_tokens + 1000, 16000)  # Cap at 16k

        logger.info(f"🎲 Generating {count} questions with temperature={temperature}, max_tokens={max_tokens}")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=120.0,  # 2 minute timeout for large requests
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

        # POST-PROCESSING: Randomisera svarsalternativ för MCQ
        if quiz_type == "mcq" and "questions" in result:
            result["questions"] = _randomize_mcq_options(result["questions"])
            logger.info(f"🔀 Randomized answer positions for {len(result['questions'])} questions")

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


# =============================================================================
# ASYNC QUIZ GENERATION - Non-blocking with parallel batches
# =============================================================================

async def _generate_batch_async(
    client,
    system_prompt: str,
    user_prompt: str,
    batch_count: int,
    quiz_type: str,
    temperature: float,
    batch_id: int
) -> Optional[dict]:
    """Generate a single batch of questions asynchronously."""
    try:
        base_tokens = 300 if quiz_type == "mcq" else 180
        max_tokens = min(batch_count * base_tokens + 500, 4096)

        logger.info(f"🎲 Batch {batch_id}: Generating {batch_count} questions...")

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        result_text = response.choices[0].message.content.strip()

        # Clean markdown formatting
        if result_text.startswith("```"):
            result_text = result_text.split("```")[1]
            if result_text.startswith("json"):
                result_text = result_text[4:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]

        result = json.loads(result_text.strip())
        questions = result.get("questions", [])

        logger.info(f"✅ Batch {batch_id}: Got {len(questions)} questions")

        # Return usage info for cost tracking
        return {
            "questions": questions,
            "usage": response.usage
        }

    except Exception as e:
        logger.error(f"❌ Batch {batch_id} failed: {e}")
        return None


async def generate_quiz_async(
    module_title: str,
    content: str,
    quiz_type: Literal["flashcard", "mcq"] = "mcq",
    count: int = 10,
    difficulty: Literal["beginner", "intermediate", "advanced"] = "intermediate",
    focus_area: Optional[str] = None,
    use_cache: bool = True
) -> Optional[dict]:
    """
    ASYNC quiz generation with parallel batches for large counts.

    For 100 questions: Runs 5 parallel batches of 20 questions each.
    Result: ~15-20 seconds instead of 2-3 minutes.
    """
    import time
    start_time = time.time()

    # Check cache first
    if use_cache:
        from ..db.redis_client import cache_get, cache_set
        cache_key = _generate_cache_key(module_title, content, quiz_type, count, difficulty, focus_area)
        cached_result = cache_get(cache_key)
        if cached_result:
            logger.info(f"✅ Quiz cache hit for {module_title}")
            return cached_result

    client = _get_async_client()
    if not client:
        logger.error("❌ Async OpenAI client not available")
        raise ValueError("OpenAI API key not configured")

    # Determine batch strategy
    # For large counts, split into parallel batches
    BATCH_SIZE = 20  # Optimal for speed vs quality

    if count <= BATCH_SIZE:
        batches = [count]
    else:
        # Split into batches of BATCH_SIZE
        num_full_batches = count // BATCH_SIZE
        remainder = count % BATCH_SIZE
        batches = [BATCH_SIZE] * num_full_batches
        if remainder > 0:
            batches.append(remainder)

    logger.info(f"🚀 Generating {count} questions in {len(batches)} parallel batches: {batches}")

    # Build prompts
    temperature = 0.95 if not use_cache else 0.8

    # System prompt (shared)
    system_prompt = _build_system_prompt()

    # Content preview
    content_preview = content[:8000]

    # Create batch tasks
    tasks = []
    for i, batch_count in enumerate(batches):
        # Each batch gets a unique seed for variety
        unique_seed = f"{uuid.uuid4().hex[:8]}_{i}"
        user_prompt = _build_user_prompt(
            module_title=module_title,
            content=content_preview,
            quiz_type=quiz_type,
            count=batch_count,
            difficulty=difficulty,
            focus_area=focus_area,
            unique_seed=unique_seed,
            batch_number=i + 1,
            total_batches=len(batches)
        )

        task = _generate_batch_async(
            client=client,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            batch_count=batch_count,
            quiz_type=quiz_type,
            temperature=temperature,
            batch_id=i + 1
        )
        tasks.append(task)

    # Run all batches in parallel
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Combine results
    all_questions = []
    total_prompt_tokens = 0
    total_completion_tokens = 0

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            logger.error(f"Batch {i+1} raised exception: {result}")
            continue
        if result is None:
            logger.warning(f"Batch {i+1} returned None")
            continue

        questions = result.get("questions", [])
        all_questions.extend(questions)

        if result.get("usage"):
            total_prompt_tokens += result["usage"].prompt_tokens
            total_completion_tokens += result["usage"].completion_tokens

    if not all_questions:
        logger.error("❌ All batches failed - no questions generated")
        return None

    # =========================================================================
    # ENSURE EXACT QUESTION COUNT - Retry for missing questions
    # =========================================================================
    retry_count = 0
    max_retries = 3

    while len(all_questions) < count and retry_count < max_retries:
        missing = count - len(all_questions)
        logger.warning(f"⚠️ Got {len(all_questions)}/{count} questions, generating {missing} more (retry {retry_count + 1})")

        # Generate missing questions in a single batch
        unique_seed = f"{uuid.uuid4().hex[:8]}_retry_{retry_count}"
        retry_prompt = _build_user_prompt(
            module_title=module_title,
            content=content_preview,
            quiz_type=quiz_type,
            count=missing,
            difficulty=difficulty,
            focus_area=focus_area,
            unique_seed=unique_seed,
            batch_number=1,
            total_batches=1
        )

        retry_result = await _generate_batch_async(
            client=client,
            system_prompt=system_prompt,
            user_prompt=retry_prompt,
            batch_count=missing,
            quiz_type=quiz_type,
            temperature=0.9,  # Higher temp for variety
            batch_id=999  # Special batch ID for retry
        )

        if retry_result and retry_result.get("questions"):
            all_questions.extend(retry_result["questions"])
            if retry_result.get("usage"):
                total_prompt_tokens += retry_result["usage"].prompt_tokens
                total_completion_tokens += retry_result["usage"].completion_tokens
            logger.info(f"✅ Retry got {len(retry_result['questions'])} questions, total now: {len(all_questions)}")

        retry_count += 1

    # Trim to exact count if we got too many
    if len(all_questions) > count:
        logger.info(f"📏 Trimming from {len(all_questions)} to {count} questions")
        all_questions = all_questions[:count]

    logger.info(f"📊 Final question count: {len(all_questions)}/{count}")

    # Randomize MCQ options
    if quiz_type == "mcq":
        all_questions = _randomize_mcq_options(all_questions)

    # Shuffle all questions for variety
    random.shuffle(all_questions)

    final_result = {"questions": all_questions}

    # Log timing and cost
    elapsed = time.time() - start_time
    cost = (total_prompt_tokens / 1_000_000 * 0.15) + (total_completion_tokens / 1_000_000 * 0.60)
    logger.info(f"⚡ Generated {len(all_questions)} questions in {elapsed:.1f}s (${cost:.4f})")

    # Log AI usage
    try:
        from ..services.ai_usage_service import log_ai_usage
        log_ai_usage(
            feature="ai_quiz",
            model="gpt-4o-mini",
            prompt_tokens=total_prompt_tokens,
            completion_tokens=total_completion_tokens,
            request_type=f"{quiz_type}_{difficulty}_async"
        )
    except Exception as e:
        logger.debug(f"Failed to log AI usage: {e}")

    # Cache result
    if use_cache:
        from ..db.redis_client import cache_set
        cache_set(cache_key, final_result, ttl=86400)

    return final_result


def _build_system_prompt() -> str:
    """Build the system prompt for quiz generation."""
    return """You are an expert DevOps instructor creating quiz questions.

🚨 ABSOLUTE RULE #1: BASE ALL QUESTIONS ON THE PROVIDED CONTENT ONLY!
- You MUST generate questions EXCLUSIVELY from the module content provided
- NEVER invent topics, commands, or concepts not mentioned in the content
- If the content is about Docker, ask about Docker - NOT about Kubernetes unless mentioned
- Every question MUST be directly traceable to something in the provided content

🚨 ABSOLUTE RULE #2: GENERATE IN ENGLISH ONLY!
- All questions, answers, explanations must be in English

Return ONLY valid JSON, no markdown formatting, no extra text."""


def _build_user_prompt(
    module_title: str,
    content: str,
    quiz_type: str,
    count: int,
    difficulty: str,
    focus_area: Optional[str],
    unique_seed: str,
    batch_number: int = 1,
    total_batches: int = 1
) -> str:
    """Build the user prompt for quiz generation."""

    if quiz_type == "flashcard":
        format_instruction = """Generate flashcards in ENGLISH in this JSON format:
{
  "questions": [
    {
      "front": "Question or term (IN ENGLISH)",
      "back": "Answer or definition (IN ENGLISH)",
      "hint": "Optional hint (IN ENGLISH)"
    }
  ]
}"""
    else:
        format_instruction = """Generate multiple choice questions in ENGLISH in this JSON format:
{
  "questions": [
    {
      "question": "The question text (IN ENGLISH)",
      "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
      "correct": "A",
      "explanation": "Explanation of why this answer is correct (IN ENGLISH)"
    }
  ]
}

CRITICAL:
- Distribute correct answers EVENLY across A, B, C, D
- ALL answer options should be APPROXIMATELY THE SAME LENGTH"""

    difficulty_label = {"beginner": "beginner", "intermediate": "intermediate", "advanced": "advanced"}.get(difficulty, "intermediate")
    focus_text = f"\nFocus specifically on: {focus_area}" if focus_area else ""

    batch_instruction = ""
    if total_batches > 1:
        batch_instruction = f"""

🔀 BATCH {batch_number} of {total_batches}
Unique seed: {unique_seed}
Generate UNIQUE questions that DO NOT overlap with other batches.
Focus on DIFFERENT aspects of the content for this batch."""

    # Add difficulty-specific instructions for async batch generation
    difficulty_guide = ""
    if difficulty == "beginner":
        difficulty_guide = """
🟢 BEGINNER LEVEL - Apply to the content topics:
- Simple "what is" and "which command" questions about topics IN THE CONTENT
- NO troubleshooting, NO optimization"""
    elif difficulty == "intermediate":
        difficulty_guide = """
🟡 INTERMEDIATE LEVEL - Apply to the content topics:
- Practical application and basic troubleshooting about topics IN THE CONTENT
- "How to" and "why does" questions"""
    else:  # advanced
        difficulty_guide = """
🔴 ADVANCED LEVEL - Apply to the content topics:
- Deep understanding, edge cases, optimization about topics IN THE CONTENT
- Architecture decisions and trade-offs"""

    return f"""You are creating {difficulty_label.upper()} level quiz content for the DevOps module: "{module_title}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 CONTENT-BASED GENERATION REQUIRED!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ ONLY ask about topics explicitly in the content below
❌ NEVER invent topics not present in the content
{difficulty_guide}

📚 MODULE CONTENT (YOUR ONLY SOURCE):
{content}

⚠️ CRITICAL: Generate EXACTLY {count} questions from THE CONTENT ABOVE!
⚠️ Apply {difficulty_label.upper()} difficulty to these content topics!

{format_instruction}
{focus_text}{batch_instruction}

Return ONLY valid JSON."""


def get_module_content_for_quiz(module_slug: str) -> Optional[str]:
    """
    Get module content suitable for quiz generation.
    """
    # Normalize slug for matching
    normalized_slug = module_slug.lower().strip()
    logger.info(f"🔍 get_module_content_for_quiz: '{normalized_slug}'")

    # ==============================================================================
    # FRÅGEKÄLLOR — Inbyggd content (fungerar på produktion)
    # ==============================================================================
    QUESTION_SOURCES = {
        "manpage-tenta": """# Manpage Tenta - Linux/Unix Kommandoreferens
Omfattande quiz om Linux-kommandon och systemadministration.

## Pipes & Redirection
- | (pipe): Skickar output från ett kommando som input till nästa
- > : Skriver över fil med output
- >> : Lägger till output i slutet av fil
- < : Tar input från fil
- 2> : Redirectar stderr
- 2>&1 : Kombinerar stderr med stdout

## Filhantering
- ls: Lista filer (-l för detaljer, -a för dolda)
- cp: Kopiera filer (-r för mappar)
- mv: Flytta/byt namn
- rm: Ta bort (-r för mappar, -f för force)
- mkdir: Skapa mapp (-p för nested)
- touch: Skapa tom fil eller uppdatera timestamp
- cat, less, head, tail: Visa filinnehåll
- find: Sök filer (-name, -type, -exec)
- grep: Sök i text (-r rekursivt, -i case-insensitive)

## Permissions
- chmod: Ändra rättigheter (755, 644, u+x)
- chown: Ändra ägare (user:group)
- chgrp: Ändra grupp
- rwx = read(4), write(2), execute(1)

## Processer
- ps: Visa processer (aux för alla)
- top/htop: Realtidsövervakning
- kill: Avsluta process (-9 för force)
- bg/fg: Bakgrund/förgrund
- nohup: Kör även efter logout
- & : Kör i bakgrunden

## Nätverk
- ip addr / ifconfig: Visa nätverkskonfiguration
- ping: Testa anslutning
- netstat / ss: Visa anslutningar
- curl/wget: Hämta från URL
- ssh: Säker fjärranslutning
- scp: Säker filkopiering

## Systemd
- systemctl start/stop/restart/status
- journalctl: Visa loggar
- enable/disable: Autostart vid boot

## Pakethantering
- apt update/upgrade/install (Debian/Ubuntu)
- yum/dnf install (RHEL/Fedora)
- pacman -S (Arch)
""",

        "omtenta-2": """# Omtenta 2.0 - DevOps & Linux
Examensfrågor för Linux och DevOps-kursen.

## Filsystem & Struktur
- /etc: Konfigurationsfiler
- /var: Variabel data (loggar, databaser)
- /home: Användarkataloger
- /tmp: Temporära filer
- /usr: Användarprogram
- /bin, /sbin: Systemkommandon
- Inodes, filsystem (ext4, xfs), mount

## Användarhantering
- useradd, usermod, userdel
- groupadd, groupmod
- passwd: Ändra lösenord
- /etc/passwd, /etc/shadow, /etc/group
- sudo, su: Privilegier

## Nätverk & Subnetting
- IP-adresser, subnätmasker
- CIDR-notation (/24 = 255.255.255.0)
- Gateway, DNS
- Portar (22=SSH, 80=HTTP, 443=HTTPS)
- TCP vs UDP

## Brandvägg
- ufw (Ubuntu): allow, deny, status
- firewalld (RHEL): --add-port, --add-service
- iptables: INPUT, OUTPUT, FORWARD

## SSH
- ssh-keygen: Skapa nycklar
- ssh-copy-id: Kopiera publik nyckel
- ~/.ssh/authorized_keys
- ~/.ssh/config: Alias

## Docker
- docker run, build, pull, push
- docker ps, images, logs
- Dockerfile: FROM, RUN, COPY, CMD
- docker-compose up/down
- Volumes, networks

## Scripting
- Variabler: VAR=value, $VAR
- if/else, for, while
- Funktioner
- Exit codes: $?
- Arguments: $1, $2, $@, $#
""",

        "handson": """# Hands-On Labs - Praktiska Övningar

## Lab 1: Onboarding
- Grundläggande terminalnavigation
- Filhantering med ls, cd, pwd, mkdir
- Skapa och redigera filer
- Bash-grunderna

## Lab 2: Användarhantering
- Skapa användare med useradd
- Hantera grupper
- Konfigurera sudo-rättigheter
- /etc/passwd och /etc/shadow

## Lab 3: SSH & Säkerhet
- Generera SSH-nycklar
- Konfigurera SSH-server
- Publik nyckelautentisering
- SSH config och alias

## Lab 4: Brandvägg
- UFW-konfiguration på Ubuntu
- Öppna/stänga portar
- Tillåta specifika IP-adresser
- Logga brandväggshändelser

## Lab 5: Pakethantering
- apt update && apt upgrade
- Installera och ta bort paket
- Hantera repositories
- dpkg för .deb-filer

## Lab 6: Subnetting
- Beräkna subnät
- CIDR-notation
- Network/broadcast-adresser
- Antal hosts per subnät

## Lab 7: Docker
- Installera Docker
- Köra containers
- Bygga images med Dockerfile
- Docker Compose för multi-container
""",

        "linux-commands": """# Linux Kommandon - Referens

## Navigering
- pwd: Visa aktuell katalog
- cd: Byt katalog (cd -, cd ~, cd ..)
- ls: Lista innehåll (-la för allt)

## Filoperationer
- cat: Visa innehåll
- less/more: Bläddra i filer
- head/tail: Visa början/slut (-n antal, -f följ)
- cp: Kopiera (-r rekursivt)
- mv: Flytta/byt namn
- rm: Ta bort (-rf för mappar)
- mkdir: Skapa mapp (-p för nested)

## Sökning
- find: Sök filer (-name, -type f/d, -exec)
- grep: Sök text (-r, -i, -v, -n)
- locate: Snabbsökning (kräver updatedb)
- which/whereis: Hitta kommandon

## Textbearbetning
- sed: Stream editor (s/old/new/g)
- awk: Kolumnbearbetning
- cut: Klipp ut delar (-d delimiter, -f fält)
- sort: Sortera (-n numeriskt, -r omvänt)
- uniq: Ta bort dubbletter (-c räkna)
- wc: Räkna (-l rader, -w ord, -c tecken)

## System
- uname -a: Systeminfo
- df -h: Diskutrymme
- du -sh: Mappstorlek
- free -h: Minnesanvändning
- uptime: Drifttid
- whoami: Aktuell användare
- id: Användar-/grupp-ID

## Processer
- ps aux: Alla processer
- top/htop: Realtid
- kill PID: Avsluta
- killall name: Avsluta alla med namn
- jobs, bg, fg: Jobbkontroll

## Arkiv
- tar -czvf: Skapa .tar.gz
- tar -xzvf: Extrahera .tar.gz
- zip/unzip: ZIP-filer
- gzip/gunzip: Komprimera
""",

        "tenta-floden": """# Tenta Flöden - Scenario & Flow Questions (40 frågor)
Scenario-baserade och sekvensbaserade frågor från Linux Tenta.

## Linux Philosophy
- Everything in Linux is treated as a file (devices, sockets, etc.)
- Unix philosophy: Do one thing well, combine tools with pipes
- "Write programs that do one thing and do it well"

## Block Storage & Encryption
- Setup order: partition → LUKS encrypt → filesystem
- LUKS (Linux Unified Key Setup) for disk encryption
- cryptsetup for managing encrypted volumes
- /dev/mapper for encrypted device mapping

## Subnetting & Networking
- CIDR notation: /27 = 32 addresses, 30 usable hosts
- Network address (first) and broadcast (last) are reserved
- 2^(32-prefix) = total addresses
- localhost (127.0.0.1) only accessible locally by definition
- Subnetting calculations with host bits

## SSH & Remote Access
- ssh-keygen for generating key pairs
- ~/.ssh/authorized_keys for public keys
- SSH config file for aliases and settings
- Port forwarding and tunneling

## User Administration
- useradd, usermod, userdel for user management
- /etc/passwd, /etc/shadow, /etc/group
- UID/GID management
- sudo and privilege escalation

## Process Management
- ps aux for process listing
- kill, killall for process termination
- nice/renice for priority adjustment
- Background processes with & and nohup
""",

        "manpage-floden": """# Manpage Flöden - Scenario & Flow Questions (150 frågor)
Scenario-baserade praktiska frågor baserat på Linux manpage-tentan.

## Linux Grundläggande (30 frågor)
- ls -a: Visa dolda filer
- man: Visa manual sidor
- head/tail: Visa filens början/slut
- grep: Sök text i filer
- wc -l: Räkna rader
- du: Visa diskutrymme
- touch: Skapa tomma filer
- pwd: Visa aktuell katalog
- clear: Rensa terminal
- cat: Visa filinnehåll
- date: Visa datum/tid
- which: Hitta binärfiler
- whoami: Visa användarnamn
- env/printenv: Visa miljövariabler
- hostname: Visa servernamn

## Textbearbetning
- diff: Jämför filer
- sort: Sortera rader
- uniq: Ta bort dubbletter
- tail -f: Följ loggfil i realtid
- cut -d: Extrahera kolumner med delimiter
- awk: Avancerad textbearbetning
- sed: Stream editor för texttransformationer

## Fil & Kataloghantering (30 frågor)
- mkdir -p: Skapa nästlade kataloger
- rmdir: Ta bort tomma kataloger
- rm -r: Ta bort kataloger rekursivt
- cp -r: Kopiera rekursivt
- mv: Flytta/byt namn
- ln -s: Skapa symboliska länkar
- find -name: Sök efter filnamn
- locate: Snabbsökning via databas
- tree: Visa katalogstruktur
- ls -l: Visa detaljer med storlek
- find -mtime: Sök efter ändringsdatum
- find -size: Sök efter storlek
- find -exec: Utför kommando på resultat

## Docker (20 frågor)
- docker ps: Lista körande containers
- docker ps -a: Inkludera stoppade
- docker logs: Visa container-loggar
- docker exec -it: Interaktiv shell
- docker images: Lista images
- docker build: Bygg image
- docker run -d: Detached mode
- docker run -p: Port mapping
- docker-compose: Multi-container apps
- Dockerfile: FROM, RUN, COPY, CMD, ENTRYPOINT
- docker volume: Persistent lagring
- docker network: Container-nätverk

## Permissions (10 frågor)
- chmod: Ändra rättigheter
- chown: Ändra ägare
- Numerisk notation: 755, 644
- Symbolisk: u+x, g-w, o=r
- SUID, SGID, sticky bit

## Git (10 frågor)
- git status: Visa ändringar
- git add: Stage ändringar
- git commit: Spara ändringar
- git push/pull: Synka med remote
- git branch: Hantera branches
- git merge: Slå ihop branches
- git log: Visa historik
"""
    }

    # Kolla om det är en frågekälla
    if normalized_slug in QUESTION_SOURCES:
        content = QUESTION_SOURCES[normalized_slug]
        logger.info(f"✅ Loaded question source: {normalized_slug} ({len(content)} chars)")
        return content

    # ==============================================================================
    # MODULER — Från content source
    # ==============================================================================
    from src.db.seeds.content import get_all_modules
    ALL_MODULES = get_all_modules()

    # Find the module by slug (with multiple matching strategies)
    module_data = None
    for mod in ALL_MODULES:
        mod_slug = mod.get("slug", "").lower().strip()
        # Exact match
        if mod_slug == normalized_slug:
            module_data = mod
            break
        # Partial match (for variations like "doe25-tenta" vs "doe25")
        if normalized_slug in mod_slug or mod_slug in normalized_slug:
            module_data = mod
            break

    if not module_data:
        logger.warning(f"Module not found for quiz: {module_slug}. Available: {[m.get('slug') for m in ALL_MODULES]}")
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
