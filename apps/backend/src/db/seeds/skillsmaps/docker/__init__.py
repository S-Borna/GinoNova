# =============================================================================
# DOCKER SKILLSMAP V3 - ULTRA-PREMIUM BOOTCAMP-QUALITY CONTENT
# =============================================================================
# 20 noder med fullständigt pedagogiskt innehåll (~10,000-15,000 chars/nod)
# Strukturen: Intro -> Koncept -> ASCII-diagram -> Praktik -> Övningar
# Uppgraderad till Linux Mastery-standard
# =============================================================================

# Block 1: Container Fundamentals (Nodes 1-4)
from .block_1_fundamentals_part1 import BLOCK_1_PART_1_NODES
from .block_1_fundamentals_part2 import BLOCK_1_PART_2_NODES

# Block 2: Volumes & Networking (Nodes 5-8)
from .block_2_volumes_part1 import BLOCK_2_PART_1_NODES
from .block_2_volumes_part2 import BLOCK_2_PART_2_NODES

# Block 3: Best Practices & Security (Nodes 9-12)
from .block_3_bestpractices_part1 import BLOCK_3_PART_1_NODES
from .block_3_bestpractices_part2 import BLOCK_3_PART_2_NODES

# Block 4: CI/CD & Optimization (Nodes 13-16)
from .block_4_cicd_part1 import BLOCK_4_PART_1_NODES
from .block_4_cicd_part2 import BLOCK_4_PART_2_NODES

# Block 5: Production & Scale (Nodes 17-20)
from .block_5_production_part1 import BLOCK_5_PART_1_NODES
from .block_5_production_part2 import BLOCK_5_PART_2_NODES

SKILLSMAP_METADATA = {
    "name": "Docker Mastery V3",
    "slug": "docker-mastery",
    "description": "Behärska containerisering från grunden till produktion. Premium bootcamp-kvalitet med djupgående teori, ASCII-diagram, praktiska övningar och enterprise-patterns.",
    "icon": "🐳",
    "color": "#2496ED",
    "track_id": "skillsmaps",
    "total_nodes": 20,
    "estimated_hours": 40,
    "difficulty": "intermediate-advanced",
    "prerequisites": ["linux-fundamentals"],
    "skills": [
        "Docker", "Containers", "Images", "Dockerfile", "Multi-stage Builds",
        "Volumes", "Networking", "Docker Compose", "Security", "Registry",
        "CI/CD", "Debugging", "Optimization", "Health Checks", "Swarm",
        "Production Patterns", "Monitoring", "Logging", "Scale"
    ],
    "certification_available": True,
    "version": "3.0",
    "quality_standard": "linux-mastery-equivalent",
    "avg_chars_per_node": 12000,
}

# Combine all nodes in correct order
ALL_NODES = (
    BLOCK_1_PART_1_NODES +   # Nodes 1-2: Docker Introduction, Working with Images
    BLOCK_1_PART_2_NODES +   # Nodes 3-4: Dockerfile Mastery, Container Lifecycle
    BLOCK_2_PART_1_NODES +   # Nodes 5-6: Docker Volumes, Docker Networking
    BLOCK_2_PART_2_NODES +   # Nodes 7-8: Docker Compose Basics, Advanced Compose
    BLOCK_3_PART_1_NODES +   # Nodes 9-10: Best Practices, Multi-stage Builds
    BLOCK_3_PART_2_NODES +   # Nodes 11-12: Security Hardening, Registry Management
    BLOCK_4_PART_1_NODES +   # Nodes 13-14: CI/CD Integration, Debugging
    BLOCK_4_PART_2_NODES +   # Nodes 15-16: Build Optimization, Health Checks
    BLOCK_5_PART_1_NODES +   # Nodes 17-18: Docker Swarm, Production Patterns
    BLOCK_5_PART_2_NODES     # Nodes 19-20: Monitoring/Logging, Scale & Performance
)

__all__ = [
    "ALL_NODES",
    "SKILLSMAP_METADATA",
    "get_all_nodes",
    "get_node_count",
    "get_total_xp",
    "get_node_by_id",
    "get_node_by_slug",
    "validate_module",
]

def get_all_nodes():
    """Return all nodes in the Docker skillsmap."""
    return ALL_NODES

def get_node_count():
    """Return total number of nodes."""
    return len(ALL_NODES)

def get_total_xp():
    """Calculate total XP available in this skillsmap."""
    return sum(node.get("xp_reward", 100) for node in ALL_NODES)

def get_node_by_id(node_id: str):
    """Find a specific node by its ID."""
    for node in ALL_NODES:
        if node.get("id") == node_id:
            return node
    return None

def get_node_by_slug(slug: str):
    """Find a specific node by its slug."""
    for node in ALL_NODES:
        if node.get("slug") == slug:
            return node
    return None

def validate_module():
    """Validate the Docker module meets quality standards."""
    total_chars = sum(len(node.get("content", "")) for node in ALL_NODES)
    avg_chars = total_chars // len(ALL_NODES) if ALL_NODES else 0

    return {
        "module": "Docker Mastery V3",
        "total_nodes": len(ALL_NODES),
        "total_characters": total_chars,
        "average_chars_per_node": avg_chars,
        "meets_standard": avg_chars >= 5918,  # Linux Mastery minimum
        "quality_rating": "PREMIUM" if avg_chars >= 10000 else "STANDARD",
    }
