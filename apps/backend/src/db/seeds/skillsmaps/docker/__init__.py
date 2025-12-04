# =============================================================================
# DOCKER SKILLSMAP - PREMIUM BOOTCAMP-QUALITY CONTENT
# =============================================================================
# 20 noder med fullständigt pedagogiskt innehåll
# Strukturen: Intro → Koncept → Praktik → Deep-dive → Övningar
# =============================================================================

from .fundamentals import NODES as FUNDAMENTALS_NODES
from .images import NODES as IMAGES_NODES
from .networking import NODES as NETWORKING_NODES
from .compose import NODES as COMPOSE_NODES
from .production import NODES as PRODUCTION_NODES

SKILLSMAP_METADATA = {
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "description": "Behärska containerisering från grunden till produktion. Lär dig bygga, köra och orkestrera containers som ett proffs.",
    "icon": "🐳",
    "color": "#2496ED",
    "track_id": "skillsmaps",
    "total_nodes": 20,
    "estimated_hours": 25,
    "difficulty": "intermediate",
    "prerequisites": ["linux-fundamentals"],
    "skills": ["Docker", "Containers", "Images", "Compose", "Networking", "Security", "Production"],
    "certification_available": True,
}

ALL_NODES = (
    FUNDAMENTALS_NODES +
    IMAGES_NODES +
    NETWORKING_NODES +
    COMPOSE_NODES +
    PRODUCTION_NODES
)

def get_all_nodes():
    return ALL_NODES

def get_node_count():
    return len(ALL_NODES)

def get_total_xp():
    return sum(node.get("xp_reward", 100) for node in ALL_NODES)
