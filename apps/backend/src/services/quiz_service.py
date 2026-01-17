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
                logger.error("❌ OpenAI API key not configured (checked OPENAI_KEY and OPENAI_API_KEY)")
                return None
            try:
                _openai_client = OpenAI(api_key=api_key, timeout=30.0)  # 30 second timeout
                logger.info(f"✅ OpenAI client initialized with key from: {'OPENAI_KEY' if os.getenv('OPENAI_KEY') else 'OPENAI_API_KEY'}")
            except Exception as e:
                logger.error(f"❌ Failed to initialize OpenAI client: {e}")
                return None
        except ImportError:
            logger.error("❌ OpenAI package not installed - run: pip install openai")
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
        logger.error("❌ OpenAI client not available - check OPENAI_KEY or OPENAI_API_KEY env var")
        raise ValueError("OpenAI API key not configured")

    # Enhanced prompt with DevOps examples and practical scenarios - SWEDISH
    if quiz_type == "flashcard":
        format_instruction = """Generera flashcards på SVENSKA i detta JSON-format:
{
  "questions": [
    {
      "front": "Fråga eller term (PÅ SVENSKA)",
      "back": "Svar eller definition (PÅ SVENSKA)",
      "hint": "Valfri ledtråd (PÅ SVENSKA)"
    }
  ]
}

Exempel på BRA flashcard:
{
  "front": "Vad gör kommandot 'docker run -d -p 8080:80 nginx'?",
  "back": "Kör nginx-container i bakgrunden (detached mode) och mappar värdport 8080 till containerport 80",
  "hint": "Tänk på -d (detached) och -p (portmappning)"
}

Exempel på DÅLIGT flashcard (för vagt):
{
  "front": "Docker",
  "back": "Containerisering"
}

VIKTIGT: Allt innehåll ska vara på SVENSKA!"""
    else:
        format_instruction = """Generera flervalsfrågor på SVENSKA i detta JSON-format:
{
  "questions": [
    {
      "question": "Frågetexten (PÅ SVENSKA)",
      "options": ["A) Alternativ 1", "B) Alternativ 2", "C) Alternativ 3", "D) Alternativ 4"],
      "correct": "A",
      "explanation": "Förklaring varför detta svar är rätt (PÅ SVENSKA)"
    }
  ]
}

Exempel på BRA flervalsfråga:
{
  "question": "Du ska deploya en Python-app med dependencies. Vilken Dockerfile-lagerordning är MEST effektiv?",
  "options": [
    "A) COPY . . && RUN pip install -r requirements.txt",
    "B) COPY requirements.txt . && RUN pip install -r requirements.txt && COPY . .",
    "C) RUN pip install -r requirements.txt && COPY . .",
    "D) COPY requirements.txt requirements.txt && COPY . . && RUN pip install"
  ],
  "correct": "B",
  "explanation": "Genom att kopiera requirements.txt först kan Docker cacha pip install-lagret. Om endast kod ändras återanvänder Docker det cachade pip install-lagret, vilket gör ombyggnader snabbare."
}

VIKTIGT:
- Det korrekta svaret ska slumpmässigt fördelas över A, B, C, D - gör INTE alltid A till rätt svar
- Variera positionen för det korrekta svaret för varje fråga
- Gör felaktiga svar rimliga men tydligt felaktiga
- Fokusera på praktiska DevOps-scenarion, inte bara definitioner
- ALLT innehåll (frågor, svar, förklaringar) ska vara på SVENSKA!"""

    focus_text = f"\nFocus specifically on: {focus_area}" if focus_area else ""

    # Add unique variation instruction when generating fresh (not cached) - SWEDISH
    # ALWAYS add variation seed to ensure unique questions every time
    # Generate timestamp-based seed for maximum uniqueness
    import time
    timestamp = int(time.time() * 1000)  # millisecond precision
    random_seed = random.randint(1000, 9999)
    unique_id = str(uuid.uuid4())[:8]

    variation_seed = f"""

🔥 KRITISKT: Generera HELT NYA och UNIKA frågor för denna session!

Session Identifiers:
- Unique ID: {unique_id}
- Random Seed: {random_seed}
- Timestamp: {timestamp}

Instruktioner för UNIKA frågor:
1. UPPREPA ALDRIG frågor från tidigare sessions
2. Välj OLIKA koncept än du normalt skulle välja
3. Utforska OVANLIGA aspekter av innehållet
4. Använd VARIERANDE scenarion och exempel
5. Var KREATIV och UNDVIK uppenbara frågor
6. Fokusera på PRAKTISKA edge cases och verkliga situationer

Om du har genererat frågor för denna modul tidigare:
- Välj HELT ANDRA topics från innehållet
- Använd OLIKA kommandon och verktyg
- Skapa NYA scenarion som du inte använt förut

Skriv ALLT på SVENSKA!"""

    # Determine difficulty-specific instructions - SWEDISH
    difficulty_instructions = {
        "beginner": """Nybörjarnivå frågor ska:
- Testa grundläggande koncept och definitioner
- Använda enkelt, tydligt språk
- Fokusera på "vad" och "när" frågor
- Exempel: "Vilket kommando listar körande containers?" (docker ps)""",
        "intermediate": """Mellannivå frågor ska:
- Testa praktisk tillämpning och felsökning
- Kräva förståelse för hur saker fungerar tillsammans
- Fokusera på "hur" och "varför" frågor
- Inkludera verkliga scenarion
- Exempel: "Din Docker-container kan inte ansluta till databasen. Vad är den mest troliga orsaken?" (nätverkskonfiguration)""",
        "advanced": """Avancerad nivå frågor ska:
- Testa djup förståelse och specialfall
- Kräva kunskap om best practices och avvägningar
- Fokusera på "vad händer om" och optimeringsscenarier
- Inkludera komplexa flerstegsproblem
- Exempel: "Du behöver skala en stateless webbapp för att hantera 10x trafik. Vilken approach minimerar latens?" (horisontell skalning med load balancer)"""
    }

    # Increase content limit from 4000 to 8000 chars for better context
    content_preview = content[:8000]
    if len(content) > 8000:
        content_preview += "\n\n[... content truncated for token limits ...]"

    # Enhanced system prompt with DevOps expertise - SWEDISH
    system_prompt = """Du är en expert DevOps-instruktör med 10+ års erfarenhet av att undervisa Linux, Docker, Kubernetes, CI/CD och molninfrastruktur.

VIKTIGT: Generera ALLT innehåll på SVENSKA. Alla frågor, svar, förklaringar och hints ska vara på svenska.

Dina quiz-frågor ska:
1. Testa PRAKTISK förståelse, inte bara memorering
2. Reflektera VERKLIGA scenarion som DevOps-ingenjörer möter dagligen
3. Inkludera rimliga felaktiga svar som testar förståelse av vanliga misstag
4. Ge tydliga, handlingsbara förklaringar som hjälper studenter lära sig
5. Fokusera på koncept som är viktiga i produktionsmiljöer

Returnera ENDAST giltig JSON, ingen markdown-formatering, ingen extra text."""

    # Build enhanced user prompt - SWEDISH
    difficulty_swedish = {"beginner": "nybörjar", "intermediate": "mellan", "advanced": "avancerad"}.get(difficulty, "mellan")
    difficulty_guide = difficulty_instructions.get(difficulty, difficulty_instructions["intermediate"])

    prompt = f"""Du skapar quiz-innehåll på {difficulty_swedish}nivå för DevOps-modulen: "{module_title}"

VIKTIGT: Generera ALLT innehåll på SVENSKA - frågor, svar, förklaringar, hints.

{difficulty_guide}

Baserat på detta modulinnehåll:
{content_preview}

Generera exakt {count} UNIKA och OLIKA {quiz_type} frågor.{focus_text}{variation_seed}

{format_instruction}

Kvalitetsriktlinjer:
- Varje fråga ska testa ett specifikt, viktigt koncept från innehållet
- Felaktiga svar ska vara rimliga men tydligt felaktiga (inga lurigfrågor)
- Förklaringar ska vara pedagogiska och hjälpa studenter förstå konceptet
- För flerval: Fördela korrekta svar jämnt över A, B, C, D positioner
- För flashcards: Framsidan ska vara specifik, baksidan ska vara heltäckande men koncis
- Undvik frågor som kan besvaras utan att läsa innehållet
- Prioritera frågor om praktisk tillämpning över ren memorering

VIKTIGT: Generera ALLT innehåll på SVENSKA!

Returnera ENDAST giltig JSON, inga markdown-kodblock, ingen extra text före eller efter."""

    try:
        # Higher temperature when not caching (force_new mode) for more variation
        # Lower temperature when caching for consistency
        temperature = 0.95 if not use_cache else 0.75  # More creative when generating fresh

        # Scale max_tokens based on question count
        # MCQ: ~150 tokens per question, Flashcard: ~80 tokens per question
        base_tokens = 200 if quiz_type == "mcq" else 120
        max_tokens = min(count * base_tokens + 500, 16000)  # Cap at 16k

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
    Retrieves ACTUAL node content from the module's tasks OR static question sources.

    Args:
        module_slug: Module slug to get content for OR question source slug
                    (e.g., "linux-247", "manpage-tenta", "omtenta-2", "handson", etc.)

    Returns:
        Combined content string from all nodes/source or None
    """
    import os

    # Normalize slug for matching
    normalized_slug = module_slug.lower().strip()

    # ==============================================================================
    # STATIC QUESTION SOURCES — For AI to generate similar questions
    # ==============================================================================
    # These are the same sources used in Tenta Simulator, but AI generates NEW questions
    # based on the content/style instead of showing static questions

    # Get project root (2 levels up from this file)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    backend_root = os.path.dirname(os.path.dirname(current_dir))
    project_root = os.path.dirname(os.path.dirname(backend_root))

    STATIC_SOURCES = {
        "manpage-tenta": os.path.join(project_root, "ManpageTentan.md"),
        "linux-tenta": None,  # May not exist
        "omtenta-2": os.path.join(project_root, "Omtenta"),  # Directory
        "handson": project_root,  # Root for Handson files
        "linux-commands": None,  # Will use quiz file data instead
    }

    # Check if this is a static source
    if normalized_slug in STATIC_SOURCES:
        source_path = STATIC_SOURCES[normalized_slug]

        if source_path and os.path.exists(source_path):
            try:
                if os.path.isfile(source_path):
                    # Read single markdown file
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    logger.info(f"✅ Loaded static source: {normalized_slug} ({len(content)} chars)")
                    return content[:12000]  # Limit for token budget

                elif os.path.isdir(source_path):
                    # Read all markdown files from directory
                    content_parts = []

                    # Special handling for handson - read Handson*.md files from root
                    if normalized_slug == "handson":
                        for filename in os.listdir(source_path):
                            if filename.startswith('Handson') and filename.endswith('.md'):
                                filepath = os.path.join(source_path, filename)
                                with open(filepath, 'r', encoding='utf-8') as f:
                                    content_parts.append(f"# {filename}\n{f.read()}")
                    else:
                        # For omtenta and others, read all .md files in directory
                        for filename in os.listdir(source_path):
                            if filename.endswith('.md'):
                                filepath = os.path.join(source_path, filename)
                                with open(filepath, 'r', encoding='utf-8') as f:
                                    content_parts.append(f"# {filename}\n{f.read()}")

                    if content_parts:
                        combined = "\n\n".join(content_parts)
                        logger.info(f"✅ Loaded static source: {normalized_slug} ({len(combined)} chars from {len(content_parts)} files)")
                        return combined[:12000]
                    else:
                        logger.warning(f"⚠️  No content found for {normalized_slug}")

            except Exception as e:
                logger.error(f"❌ Failed to load static source {normalized_slug}: {e}")

        # Fallback: use quiz data file content for linux-commands
        if normalized_slug == "linux-commands":
            logger.info(f"ℹ️  Using quiz data fallback for {normalized_slug}")
            return "# Linux Commands Reference\nVanliga Linux-kommandon för terminal och systemadministration."

    # ==============================================================================
    # REGULAR MODULES — From content source
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
