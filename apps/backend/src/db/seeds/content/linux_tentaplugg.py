"""
Tentaplugg Linux Parafraserade - 10 djupgående noder för komplett tentaförberedelse
DOE25 Linux/Unix Server samt Bash Programmering | Parafraserat innehåll

STRUKTUR:
- Linux Filsystem & Navigering (1 nod)
- Rättigheter & Säkerhet (1 nod)
- Processhantering (1 nod)
- Nätverk & Server (1 nod)
- SSH & Säker kommunikation (1 nod)
- Bash Skriptprogrammering (1 nod)
- Bash Verktyg (1 nod)
- Docker Grunder (1 nod)
- Docker Nätverk & Lagring (1 nod)
- Docker Compose & IaC (1 nod)
"""

# =============================================================================
# IMPORTS från individuella nod-filer
# =============================================================================

from .nod_filsystem_grunder import FILSYSTEM_GRUNDER_NODE
from .nod_rattigheter_sakerhet import RATTIGHETER_SAKERHET_NODE
from .nod_processhantering import PROCESSHANTERING_NODE
from .nod_natverk_server import NATVERK_SERVER_NODE
from .nod_ssh_kommunikation import SSH_KOMMUNIKATION_NODE
from .nod_bash_skript import BASH_SKRIPT_NODE
from .nod_bash_verktyg import BASH_VERKTYG_NODE
from .nod_docker_isolering import DOCKER_ISOLERING_NODE
from .nod_docker_natverk_lagring import DOCKER_NATVERK_LAGRING_NODE
from .nod_docker_compose_iac import DOCKER_COMPOSE_NODE


# =============================================================================
# BYGG MODULEN
# =============================================================================

def _update_order_index(node, index):
    """Uppdatera order_index för en nod"""
    node_copy = node.copy()
    node_copy["order_index"] = index
    return node_copy


MODULE = {
    "id": "linux-tentaplugg",
    "slug": "linux-tentaplugg",
    "title": "Linux Tentaplugg",
    "description": "10 djupgående noder: Linux Filsystem, Rättigheter, Processhantering, Nätverk, SSH, Bash Skript & Verktyg, samt Docker & Compose.",
    "icon": "📚",
    "difficulty": "intermediate",
    "estimated_hours": 12,
    "order_index": 2,
    "exam_date": "2026-01-07",
    "groups": [
        {
            "id": "linux-system",
            "title": "Linux System",
            "subtitle": "Filsystem, Rättigheter & Processer",
            "icon": "Server",
            "color": "from-cyan-500 to-blue-500",
            "bgGlow": "rgba(6, 182, 212, 0.2)",
            "taskIds": [
                "filsystem-grunder",
                "rattigheter-sakerhet",
                "processhantering"
            ]
        },
        {
            "id": "natverk-ssh",
            "title": "Nätverk & SSH",
            "subtitle": "Kommunikation & Säkerhet",
            "icon": "Network",
            "color": "from-green-500 to-emerald-500",
            "bgGlow": "rgba(16, 185, 129, 0.2)",
            "taskIds": [
                "natverk-server",
                "ssh-kommunikation"
            ]
        },
        {
            "id": "bash-scripting",
            "title": "Bash Scripting",
            "subtitle": "Skript & Verktyg",
            "icon": "Terminal",
            "color": "from-orange-500 to-amber-500",
            "bgGlow": "rgba(245, 158, 11, 0.2)",
            "taskIds": [
                "bash-skript",
                "bash-verktyg"
            ]
        },
        {
            "id": "docker-devops",
            "title": "Docker & DevOps",
            "subtitle": "Containrar & Infrastructure as Code",
            "icon": "Container",
            "color": "from-purple-500 to-violet-500",
            "bgGlow": "rgba(139, 92, 246, 0.2)",
            "taskIds": [
                "docker-isolering-images",
                "docker-natverk-lagring",
                "docker-compose-iac"
            ]
        }
    ],
    "tasks": [
        # =====================================================================
        # LINUX SYSTEM (3 noder)
        # =====================================================================
        _update_order_index(FILSYSTEM_GRUNDER_NODE, 1),
        _update_order_index(RATTIGHETER_SAKERHET_NODE, 2),
        _update_order_index(PROCESSHANTERING_NODE, 3),

        # =====================================================================
        # NÄTVERK & SSH (2 noder)
        # =====================================================================
        _update_order_index(NATVERK_SERVER_NODE, 4),
        _update_order_index(SSH_KOMMUNIKATION_NODE, 5),

        # =====================================================================
        # BASH SCRIPTING (2 noder)
        # =====================================================================
        _update_order_index(BASH_SKRIPT_NODE, 6),
        _update_order_index(BASH_VERKTYG_NODE, 7),

        # =====================================================================
        # DOCKER & DEVOPS (3 noder)
        # =====================================================================
        _update_order_index(DOCKER_ISOLERING_NODE, 8),
        _update_order_index(DOCKER_NATVERK_LAGRING_NODE, 9),
        _update_order_index(DOCKER_COMPOSE_NODE, 10),
    ],
}


# =============================================================================
# EXPORTERA
# =============================================================================

__all__ = ["MODULE"]
