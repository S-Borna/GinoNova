"""
Ansible Mastery - V3 Premium Module
===========================================
Configuration Management & Automation

20 Premium tasks with V3 pedagogical structure
"""

# Import from skillsmaps folder
from ..skillsmaps.ansible import ANSIBLE_SKILLSMAP_ALL_NODES, ANSIBLE_SKILLSMAP_INFO


def convert_ansible_node_to_v3_task(node: dict, idx: int) -> dict:
    """Convert skillsmap node to V3 task format."""
    return {
        "id": f"ansible-task-{idx + 1}",
        "title": node["title"],
        "slug": node["slug"],
        "description": f"Lär dig {node['title'].lower()} för Ansible automation",
        "xp_reward": node.get("xp_reward", 100),
        "estimated_minutes": node.get("estimated_minutes", 45),
        "order_index": idx + 1,
        "prerequisites": [f"ansible-task-{p}" for p in node.get("prerequisites", [])] if node.get("prerequisites") else [],
        "content": node.get("content", ""),
        "content_type": "markdown",
        "quality_tier": "premium"
    }


# Convert all nodes to V3 tasks
ANSIBLE_V3_TASKS = [
    convert_ansible_node_to_v3_task(node, idx)
    for idx, node in enumerate(ANSIBLE_SKILLSMAP_ALL_NODES)
]


MODULE_ANSIBLE_MASTERY = {
    "track_slug": "platform-engineering",
    "order_index": 6,
    "name": "Ansible Mastery",
    "slug": "ansible-mastery",
    "title": "Ansible Mastery",
    "description": "Bemästra Ansible för automatiserad infrastrukturhantering, konfigurationshantering och deployment. Från grundläggande playbooks till avancerade roller och produktionsmönster.",
    "icon": "📦",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "total_xp": sum(t.get("xp_reward", 100) for t in ANSIBLE_V3_TASKS),
    "prerequisites": ["linux-mastery"],
    "skills": ANSIBLE_SKILLSMAP_INFO.get("skills", ["Ansible", "YAML", "Automation", "Configuration Management"]),
    "tasks": ANSIBLE_V3_TASKS,
    "labs": [
        {
            "id": "ansible-lab-1",
            "title": "Bygg ditt första Ansible-projekt",
            "description": "Skapa en komplett Ansible-struktur med inventory, playbook och roles",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 200
        },
        {
            "id": "ansible-lab-2",
            "title": "Multi-Server Deployment",
            "description": "Automatisera deployment till flera servrar med rolling updates",
            "difficulty": "advanced",
            "estimated_minutes": 90,
            "xp_reward": 300
        }
    ]
}


# Validation
assert len(MODULE_ANSIBLE_MASTERY["tasks"]) == 20, f"Expected 20 tasks, got {len(MODULE_ANSIBLE_MASTERY['tasks'])}"
print(f"✅ Ansible Mastery V3: {len(MODULE_ANSIBLE_MASTERY['tasks'])} Premium tasks loaded")
