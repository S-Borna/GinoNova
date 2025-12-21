"""
C# & .NET SkillsMap — Backend Development with Microsoft Stack
==============================================================

20 nodes covering C# from fundamentals to production-ready ASP.NET Core apps.
Akhilesh-style pedagogy: Hook -> Concept -> Code -> Pro Tips -> Hands-on Task

Block 1 (Nodes 1-4): C# Fundamentals
Block 2 (Nodes 5-8): Object-Oriented Programming
Block 3 (Nodes 9-12): ASP.NET Core Basics
Block 4 (Nodes 13-16): Data Access & APIs
Block 5 (Nodes 17-20): Production & DevOps

Total: 20 nodes, ~35 hours, 2200 XP
"""

from .block_1_fundamentals import BLOCK_1_NODES
from .block_2_oop import BLOCK_2_NODES
from .block_3_aspnet import BLOCK_3_NODES
from .block_4_data import BLOCK_4_NODES
from .block_5_production import BLOCK_5_NODES

SKILLSMAP_METADATA = {
    "id": "dotnet-mastery",
    "slug": "dotnet-mastery",
    "title": "C# & .NET Mastery",
    "description": "Bygg robusta backend-applikationer med C# och ASP.NET Core - från syntax till produktion",
    "icon": "🟣",
    "color": "#512BD4",
    "difficulty": "intermediate",
    "estimated_hours": 35,
    "total_xp": 2200,
    "prerequisites": ["programming-basics"],
    "tags": ["C#", ".NET", "ASP.NET Core", "Backend", "Entity Framework", "API", "Microsoft"],
}

# Combine all nodes
ALL_NODES = BLOCK_1_NODES + BLOCK_2_NODES + BLOCK_3_NODES + BLOCK_4_NODES + BLOCK_5_NODES

def get_node_count():
    return len(ALL_NODES)

def get_total_xp():
    return sum(node.get("xp_reward", 100) for node in ALL_NODES)
