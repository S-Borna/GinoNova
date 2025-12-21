"""
MLOps SkillsMap - Machine Learning Operations
Based on roadmap.sh/mlops

Structure:
- Block 1: Fundamentals (Programming, Version Control, Cloud)
- Block 2: Data Engineering (Pipelines, Lakes, Ingestion)
- Block 3: ML Fundamentals (Training, Models, Experiments)
- Block 4: MLOps Core (CI/CD, Orchestration, Serving)
- Block 5: Production (Monitoring, Scaling, Best Practices)

Total: 20 nodes, ~35 hours, 2200 XP
"""

from .block_1_fundamentals import BLOCK_1_NODES
from .block_2_data_engineering import BLOCK_2_NODES
from .block_3_ml_fundamentals import BLOCK_3_NODES
from .block_4_infrastructure import BLOCK_4_NODES
from .block_5_advanced import BLOCK_5_NODES

SKILLSMAP_METADATA = {
    "id": "mlops",
    "slug": "mlops",
    "title": "MLOps",
    "description": "Machine Learning Operations - från experiment till produktion med ML-pipelines, modellhantering och observability",
    "icon": "🤖",
    "color": "#FF6F00",
    "difficulty": "advanced",
    "estimated_hours": 35,
    "total_xp": 2200,
    "prerequisites": ["python", "docker", "linux"],
    "tags": ["ML", "AI", "DevOps", "Data Science", "Pipelines"],
}

# Combine all nodes
ALL_NODES = BLOCK_1_NODES + BLOCK_2_NODES + BLOCK_3_NODES + BLOCK_4_NODES + BLOCK_5_NODES

# Validate node count
NODE_COUNT = 20
assert len(ALL_NODES) == NODE_COUNT, f"Expected {NODE_COUNT} nodes, got {len(ALL_NODES)}"
