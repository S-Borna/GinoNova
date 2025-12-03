# =============================================================================
# NODE.JS SKILLSMAP
# =============================================================================
# 20 noder uppdelade i 5 block för hanterbarhet
# Total: ~3500 rader
# =============================================================================

from .block_1_fundamentals import NODEJS_BLOCK_1
from .block_2_async import NODEJS_BLOCK_2
from .block_3_backend import NODEJS_BLOCK_3
from .block_4_advanced import NODEJS_BLOCK_4
from .block_5_production import NODEJS_BLOCK_5

NODEJS_NODES = (
    NODEJS_BLOCK_1 +
    NODEJS_BLOCK_2 +
    NODEJS_BLOCK_3 +
    NODEJS_BLOCK_4 +
    NODEJS_BLOCK_5
)

NODEJS_METADATA = {
    "id": "nodejs",
    "title": "Node.js",
    "description": "Bygg skalbara server-side applikationer med JavaScript",
    "icon": "🟢",
    "category": "backend",
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "total_xp": 2900,
    "prerequisites": ["javascript"],
}

# Validera att vi har alla 20 noder
assert len(NODEJS_NODES) == 20, f"Expected 20 nodes, got {len(NODEJS_NODES)}"
