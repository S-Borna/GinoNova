"""
ULTIMATE Modules - Clean Architecture
======================================

Denna mapp innehåller ENDAST moduler som är fullt uppgraderade till ULTIMATE-format.

ULTIMATE-format inkluderar:
- LÄRANDEMÅL
- INTRODUKTION
- TEORI (med ASCII-diagram)
- STEG-FÖR-STEG GUIDE
- PRAKTISKA EXEMPEL
- BÄSTA PRAXIS
- VANLIGA FALLGROPAR
- ÖVNINGAR
- KOPPLINGAR
- SAMMANFATTNING
- NYCKELKOMMANDON
- REFERENSER

Moduler här:
- linux_ultimate.py      - Linux Mastery (20 noder)
- docker_ultimate.py     - Docker Mastery (20 noder)
- cicd_ultimate.py       - CI/CD Mastery (20 noder)

Framtida planering:
- kubernetes_ultimate.py
- terraform_ultimate.py
- ansible_ultimate.py
- aws_ultimate.py
- azure_ultimate.py
- git_github_ultimate.py
- bash_ultimate.py
"""

# Import när moduler är klara
# from .linux_ultimate import MODULE as LINUX_ULTIMATE
# from .docker_ultimate import MODULE as DOCKER_ULTIMATE
# from .cicd_ultimate import MODULE as CICD_ULTIMATE

ALL_ULTIMATE_MODULES = []

def get_ultimate_modules():
    """Returnerar alla ULTIMATE-moduler."""
    return ALL_ULTIMATE_MODULES

def get_ultimate_count():
    """Antal ULTIMATE-moduler."""
    return len(ALL_ULTIMATE_MODULES)
