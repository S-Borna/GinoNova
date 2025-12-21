# =============================================================================
# KUBERNETES MASTERY V3 - MAIN EXPORT
# 20 noder uppdelade i 10 filer | Linux Mastery Standard
# =============================================================================

"""
KUBERNETES SKILLSMAP V3
=======================
Komplett Kubernetes-modul med 20 noder fördelade på 10 filer.
Varje nod följer Linux Mastery-standarden med ~10,000+ chars/node.

STRUKTUR:
- Block 1: Fundamentals (Noder 1-4)
- Block 2: Services & Networking (Noder 5-8)
- Block 3: Advanced Workloads (Noder 9-12)
- Block 4: Helm & Advanced (Noder 13-16)
- Block 5: Production (Noder 17-20)
"""

# Block 1 - Fundamentals
from .block_1_fundamentals_part1 import NODE_1, NODE_2, BLOCK_1_PART_1_NODES
from .block_1_fundamentals_part2 import NODE_3, NODE_4, BLOCK_1_PART_2_NODES

# Block 2 - Services & Networking
from .block_2_services_part1 import NODE_5, NODE_6, BLOCK_2_PART_1_NODES
from .block_2_services_part2 import NODE_7, NODE_8, BLOCK_2_PART_2_NODES

# Block 3 - Advanced Workloads
from .block_3_workloads_part1 import NODE_9, NODE_10, BLOCK_3_PART_1_NODES
from .block_3_workloads_part2 import NODE_11, NODE_12, BLOCK_3_PART_2_NODES

# Block 4 - Helm & Advanced
from .block_4_helm_part1 import NODE_13, NODE_14, BLOCK_4_PART_1_NODES
from .block_4_helm_part2 import NODE_15, NODE_16, BLOCK_4_PART_2_NODES

# Block 5 - Production
from .block_5_production_part1 import NODE_17, NODE_18, BLOCK_5_PART_1_NODES
from .block_5_production_part2 import NODE_19, NODE_20, BLOCK_5_PART_2_NODES

# =============================================================================
# AGGREGATED EXPORTS
# =============================================================================

# All nodes in order
KUBERNETES_NODES = [
    NODE_1, NODE_2, NODE_3, NODE_4,      # Block 1: Fundamentals
    NODE_5, NODE_6, NODE_7, NODE_8,      # Block 2: Services
    NODE_9, NODE_10, NODE_11, NODE_12,   # Block 3: Workloads
    NODE_13, NODE_14, NODE_15, NODE_16,  # Block 4: Helm
    NODE_17, NODE_18, NODE_19, NODE_20   # Block 5: Production
]

# Block groupings
BLOCK_1_NODES = BLOCK_1_PART_1_NODES + BLOCK_1_PART_2_NODES
BLOCK_2_NODES = BLOCK_2_PART_1_NODES + BLOCK_2_PART_2_NODES
BLOCK_3_NODES = BLOCK_3_PART_1_NODES + BLOCK_3_PART_2_NODES
BLOCK_4_NODES = BLOCK_4_PART_1_NODES + BLOCK_4_PART_2_NODES
BLOCK_5_NODES = BLOCK_5_PART_1_NODES + BLOCK_5_PART_2_NODES

# =============================================================================
# SKILLSMAP METADATA
# =============================================================================

KUBERNETES_SKILLSMAP = {
    "id": "kubernetes_mastery_v3",
    "title": "Kubernetes Mastery",
    "slug": "kubernetes-mastery",
    "description": """
    Komplett Kubernetes-utbildning från grundläggande koncept till production-ready deployments.

    20 djupgående moduler som täcker:
    • Core concepts: Pods, Deployments, Services
    • Networking: Ingress, Network Policies
    • Storage: Volumes, ConfigMaps, Secrets
    • Workloads: StatefulSets, DaemonSets, Jobs
    • Package Management: Helm Charts
    • Production: Autoscaling, Probes, Observability
    """,
    "icon": "☸️",
    "color": "#326CE5",
    "category": "container_orchestration",
    "difficulty": "intermediate",
    "estimated_hours": 40,
    "total_xp": sum(node.get("xp_reward", 100) for node in KUBERNETES_NODES),
    "prerequisites": ["docker_fundamentals", "linux_basics"],
    "blocks": [
        {
            "id": "block_1",
            "title": "Kubernetes Fundamentals",
            "description": "Core concepts och grundläggande operationer",
            "nodes": BLOCK_1_NODES
        },
        {
            "id": "block_2",
            "title": "Services & Networking",
            "description": "Service discovery, ingress och konfiguration",
            "nodes": BLOCK_2_NODES
        },
        {
            "id": "block_3",
            "title": "Advanced Workloads",
            "description": "StatefulSets, Jobs, DaemonSets och RBAC",
            "nodes": BLOCK_3_NODES
        },
        {
            "id": "block_4",
            "title": "Helm & Advanced Features",
            "description": "Package management och avancerade features",
            "nodes": BLOCK_4_NODES
        },
        {
            "id": "block_5",
            "title": "Production Operations",
            "description": "Production-ready practices och observability",
            "nodes": BLOCK_5_NODES
        }
    ],
    "nodes": KUBERNETES_NODES
}

# =============================================================================
# VALIDATION
# =============================================================================

def validate_kubernetes_module():
    """Validera att alla noder är korrekt konfigurerade."""
    errors = []

    # Check node count
    if len(KUBERNETES_NODES) != 20:
        errors.append(f"Expected 20 nodes, got {len(KUBERNETES_NODES)}")

    # Check each node
    for i, node in enumerate(KUBERNETES_NODES, 1):
        node_id = node.get("id", f"unknown_{i}")

        # Required fields
        required = ["id", "title", "slug", "content", "xp_reward"]
        for field in required:
            if field not in node:
                errors.append(f"Node {node_id}: Missing required field '{field}'")

        # Content length
        content = node.get("content", "")
        if len(content) < 5000:
            errors.append(f"Node {node_id}: Content too short ({len(content)} chars, min 5000)")

    return errors

def get_module_stats():
    """Returnera statistik om modulen."""
    total_chars = sum(len(node.get("content", "")) for node in KUBERNETES_NODES)
    total_xp = sum(node.get("xp_reward", 0) for node in KUBERNETES_NODES)
    total_minutes = sum(node.get("estimated_minutes", 0) for node in KUBERNETES_NODES)

    return {
        "total_nodes": len(KUBERNETES_NODES),
        "total_chars": total_chars,
        "avg_chars_per_node": total_chars // len(KUBERNETES_NODES) if KUBERNETES_NODES else 0,
        "total_xp": total_xp,
        "total_minutes": total_minutes,
        "total_hours": total_minutes / 60
    }

# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("KUBERNETES MASTERY V3 - MODULE VALIDATION")
    print("=" * 60)

    # Validate
    errors = validate_kubernetes_module()
    if errors:
        print("\n❌ VALIDATION ERRORS:")
        for error in errors:
            print(f"   • {error}")
    else:
        print("\n✅ All validations passed!")

    # Stats
    stats = get_module_stats()
    print("\n📊 MODULE STATISTICS:")
    print(f"   • Total nodes: {stats['total_nodes']}")
    print(f"   • Total chars: {stats['total_chars']:,}")
    print(f"   • Avg chars/node: {stats['avg_chars_per_node']:,}")
    print(f"   • Total XP: {stats['total_xp']}")
    print(f"   • Estimated hours: {stats['total_hours']:.1f}")

    print("\n" + "=" * 60)
