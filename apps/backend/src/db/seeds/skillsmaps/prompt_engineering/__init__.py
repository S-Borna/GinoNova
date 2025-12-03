# =============================================================================
# PROMPT ENGINEERING SKILLSMAP
# =============================================================================
# 20 noder uppdelade i 5 block för hanterbarhet
# Källa: roadmap.sh/prompt-engineering (46 topics)
# =============================================================================

from .block_1_fundamentals import PROMPT_BLOCK_1
from .block_2_configuration import PROMPT_BLOCK_2
from .block_3_techniques import PROMPT_BLOCK_3
from .block_4_advanced import PROMPT_BLOCK_4
from .block_5_applications import PROMPT_BLOCK_5

PROMPT_ENGINEERING_NODES = (
    PROMPT_BLOCK_1 +
    PROMPT_BLOCK_2 +
    PROMPT_BLOCK_3 +
    PROMPT_BLOCK_4 +
    PROMPT_BLOCK_5
)

PROMPT_ENGINEERING_METADATA = {
    "id": "prompt-engineering",
    "title": "Prompt Engineering",
    "description": "Bemästra konsten att kommunicera med AI-modeller effektivt",
    "icon": "🧠",
    "category": "ai",
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "total_xp": 2800,
    "prerequisites": [],
}

# Validera att vi har alla 20 noder
assert len(PROMPT_ENGINEERING_NODES) == 20, f"Expected 20 nodes, got {len(PROMPT_ENGINEERING_NODES)}"
