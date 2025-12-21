"""
AI Agents SkillsMap - Design, Build and Ship AI Agents
Based on roadmap.sh/ai-agents

Structure (10 blocks x 2 nodes = 20 total):
- Block 01: LLM Fundamentals (nodes 1-2)
- Block 02: Model Mechanics (nodes 3-4)
- Block 03: Agent Basics (nodes 5-6)
- Block 04: Agent Loop (nodes 7-8)
- Block 05: Tools & Actions (nodes 9-10)
- Block 06: Frameworks (nodes 11-12)
- Block 07: Memory & State (nodes 13-14)
- Block 08: Multi-Agent (nodes 15-16)
- Block 09: Production (nodes 17-18)
- Block 10: Advanced (nodes 19-20)

Total: 20 nodes, ~30 hours, 2400 XP
"""

from .block_01_llm_fundamentals import BLOCK_01_NODES
from .block_02_model_mechanics import BLOCK_02_NODES
from .block_03_agent_basics import BLOCK_03_NODES
from .block_04_agent_loop import BLOCK_04_NODES
from .block_05_tools_actions import BLOCK_05_NODES
from .block_06_frameworks import BLOCK_06_NODES
from .block_07_memory_state import BLOCK_07_NODES
from .block_08_multi_agent import BLOCK_08_NODES
from .block_09_production import BLOCK_09_NODES
from .block_10_advanced import BLOCK_10_NODES

SKILLSMAP_METADATA = {
    "id": "ai-agents",
    "slug": "ai-agents",
    "title": "AI Agents",
    "description": "Designa, bygg och deploya AI-agenter - från LLM-grunder till autonoma system med verktygsanvändning och multi-agent arkitekturer",
    "icon": "🤖",
    "color": "#7C3AED",
    "difficulty": "advanced",
    "estimated_hours": 30,
    "total_xp": 2400,
    "prerequisites": ["python", "prompt-engineering"],
    "tags": ["AI", "LLM", "Agents", "Automation", "OpenAI", "LangChain"],
}

# Combine all nodes
ALL_NODES = (
    BLOCK_01_NODES +
    BLOCK_02_NODES +
    BLOCK_03_NODES +
    BLOCK_04_NODES +
    BLOCK_05_NODES +
    BLOCK_06_NODES +
    BLOCK_07_NODES +
    BLOCK_08_NODES +
    BLOCK_09_NODES +
    BLOCK_10_NODES
)

# Validate node count
NODE_COUNT = 20
assert len(ALL_NODES) == NODE_COUNT, f"Expected {NODE_COUNT} nodes, got {len(ALL_NODES)}"
