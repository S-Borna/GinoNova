# =============================================================================
# SYSTEM DESIGN SKILLSMAP
# =============================================================================
# 20 noder uppdelade i 5 block för hanterbarhet
# Total: ~3500 rader
# =============================================================================

from .block_1_fundamentals import SYSTEM_DESIGN_BLOCK_1
from .block_2_infrastructure import SYSTEM_DESIGN_BLOCK_2
from .block_3_data import SYSTEM_DESIGN_BLOCK_3
from .block_4_architecture import SYSTEM_DESIGN_BLOCK_4
from .block_5_advanced import SYSTEM_DESIGN_BLOCK_5

SYSTEM_DESIGN_NODES = (
    SYSTEM_DESIGN_BLOCK_1 +
    SYSTEM_DESIGN_BLOCK_2 +
    SYSTEM_DESIGN_BLOCK_3 +
    SYSTEM_DESIGN_BLOCK_4 +
    SYSTEM_DESIGN_BLOCK_5
)

SYSTEM_DESIGN_METADATA = {
    "id": "system-design",
    "title": "System Design",
    "description": "Designa skalbara, robusta och högpresterande system",
    "icon": "🏗️",
    "category": "architecture",
    "difficulty": "advanced",
    "estimated_hours": 35,
    "total_xp": 3100,
    "prerequisites": ["sql", "linux"],
}

# Validera att vi har alla 20 noder
assert len(SYSTEM_DESIGN_NODES) == 20, f"Expected 20 nodes, got {len(SYSTEM_DESIGN_NODES)}"
