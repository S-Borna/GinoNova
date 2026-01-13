"""
Content Source — Single Source of Truth
========================================

Detta är DEN ENDA platsen där moduler och tasks definieras.
Allt content som ska visas på sidan kommer härifrån.

Struktur:
- ALL_MODULES: Lista med alla moduler
- Varje modul har: name, slug, description, tasks[], etc.
- Varje task har: title, content, difficulty, xp_reward, etc.

Användning:
-----------
# Lägg till modul direkt:
ALL_MODULES = [
    {
        "name": "Linux Mastery",
        "slug": "linux-mastery",
        ...
    }
]

# Eller importera från separata filer:
from .linux import MODULE as LINUX_MODULE
ALL_MODULES = [LINUX_MODULE]

API:
----
- get_all_modules() → Lista med alla moduler
- get_module_by_slug(slug) → En specifik modul eller None
- get_total_modules() → Antal moduler
- get_total_tasks() → Totalt antal tasks
"""

from typing import Optional

# =============================================================================
# IMPORT MODULES
# =============================================================================
from .linux_247 import MODULE as LINUX_247_MODULE
from .doe25_tentaplugg import MODULE as DOE25_TENTAPLUGG_MODULE
from .hands_on import MODULE as HANDS_ON_MODULE
from .kubernetes_fundamentals import MODULE as KUBERNETES_MODULE
from .prompt_engineering_devops import MODULE as PROMPT_ENGINEERING_MODULE
from .cicd_pipelines_advanced import MODULE as CICD_ADVANCED_MODULE
from .cloud_aws_fundamentals import MODULE as AWS_FUNDAMENTALS_MODULE
from .cloud_azure_fundamentals import MODULE as AZURE_FUNDAMENTALS_MODULE
from .cloud_gcp_fundamentals import MODULE as GCP_FUNDAMENTALS_MODULE
from .cloud_multicloud_architecture import MODULE as MULTICLOUD_MODULE
from .terraform_iac import MODULE as TERRAFORM_MODULE
from .python_for_devops import MODULE as PYTHON_DEVOPS_MODULE
from .config_ansible_automation import MODULE as ANSIBLE_MODULE

# =============================================================================
# ALL MODULES — Lista med alla moduler som ska visas
# =============================================================================
ALL_MODULES: list[dict] = [
    # Existing modules
    LINUX_247_MODULE,
    DOE25_TENTAPLUGG_MODULE,
    HANDS_ON_MODULE,

    # Core DevOps Skills (Job-ready content)
    KUBERNETES_MODULE,
    CICD_ADVANCED_MODULE,

    # Cloud Platforms
    AWS_FUNDAMENTALS_MODULE,
    AZURE_FUNDAMENTALS_MODULE,
    GCP_FUNDAMENTALS_MODULE,
    MULTICLOUD_MODULE,

    # Infrastructure as Code
    TERRAFORM_MODULE,

    # Configuration Management
    ANSIBLE_MODULE,

    # Tools & Languages
    PYTHON_DEVOPS_MODULE,
    PROMPT_ENGINEERING_MODULE,
]


# =============================================================================
# API FUNCTIONS — Används av backend för att hämta content
# =============================================================================


def get_all_modules() -> list[dict]:
    """
    Returnerar alla moduler.

    Returns:
        Lista med moduler. Tom lista = inga moduler visas på sidan.
    """
    return ALL_MODULES


def get_camp_devops_modules() -> list[dict]:
    """
    Returnerar Camp DevOps moduler (DevOps-fokuserade).
    Filtrera på track_slug om du vill separera.
    """
    return [
        m
        for m in ALL_MODULES
        if m.get("track_slug")
        in [
            "foundation",
            "cloud-infrastructure",
            "containers-orchestration",
            "platform-engineering",
        ]
    ]


def get_module_by_slug(slug: str) -> Optional[dict]:
    """
    Hämta en specifik modul via dess slug.

    Args:
        slug: Modulens unika identifierare (t.ex. "linux-mastery")

    Returns:
        Modul-dict om hittad, annars None.
    """
    for module in ALL_MODULES:
        if module.get("slug") == slug:
            return module
    return None


def get_total_modules() -> int:
    """Returnerar totalt antal moduler."""
    return len(ALL_MODULES)


def get_total_tasks() -> int:
    """Returnerar totalt antal tasks över alla moduler."""
    return sum(len(m.get("tasks", [])) for m in ALL_MODULES)


def get_bootcamp_summary() -> dict:
    """
    Returnerar en sammanfattning av innehållet.
    Används av seeding för att veta om data behöver seedas.
    """
    return {
        "modules": get_total_modules(),
        "tasks": get_total_tasks(),
        "tracks": len(
            set(m.get("track_slug") for m in ALL_MODULES if m.get("track_slug"))
        ),
    }


# =============================================================================
# TRACKS — Definieras här om du vill ha dem
# =============================================================================

TRACKS: list[dict] = [
    {
        "name": "Foundation",
        "slug": "foundation",
        "description": "Bygg din grund med Linux, Git, och scripting",
        "color": "#6366f1",
        "icon": "🏗️",
        "order_index": 1,
    },
    {
        "name": "Cloud & Infrastructure",
        "slug": "cloud-infrastructure",
        "description": "AWS, Terraform, och molnarkitektur",
        "color": "#8b5cf6",
        "icon": "☁️",
        "order_index": 2,
    },
    {
        "name": "Containers & Orchestration",
        "slug": "containers-orchestration",
        "description": "Docker och Kubernetes",
        "color": "#06b6d4",
        "icon": "🐳",
        "order_index": 3,
    },
    {
        "name": "Platform Engineering",
        "slug": "platform-engineering",
        "description": "CI/CD, GitOps, och SRE",
        "color": "#f97316",
        "icon": "🚀",
        "order_index": 4,
    },
]


def get_tracks() -> list[dict]:
    """Returnerar alla tracks."""
    return TRACKS
