"""
Tentaplugg Linux - Study Data (Uppdaterad v2.0)
================================================

Flashcards för DOE25 Linux-tentan.
Nu med 25 noder i 4 moduler!

STRUKTUR:
- MODUL 0: Linux Grunder (2 noder)
- MODUL 1: BASH (11 noder)
- MODUL 2: LINUX SYSTEM (8 noder)
- MODUL 3: DEVOPS (4 noder)

TOTALT: 25 noder, 250+ flashcards
"""

# Importera flashcards från huvudmodulen
from ..content.doe25_tentaplugg import ALL_FLASHCARDS

TENTAPLUGG_LINUX_STUDY = {
    "module_slug": "tentaplugg-linux",
    "module_title": "Tentaplugg Linux",
    "module_description": "Komplett tentaförberedelse för DOE25 Linux-kursen - 25 noder i 4 moduler",
    "icon": "GraduationCap",
    "flashcards": ALL_FLASHCARDS,
}

# =============================================================================
# EXPORTERA
# =============================================================================
__all__ = ["TENTAPLUGG_LINUX_STUDY"]
