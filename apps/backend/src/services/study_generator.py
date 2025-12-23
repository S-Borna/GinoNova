"""
Study Generator - Dynamiskt generera flashcards och quiz från modulinnehåll
==============================================================================

Hämtar innehåll från modulernas noder (tasks) och extraherar:
- Key Takeaways -> Flashcards
- Kom ihåg-punkter -> Flashcards
- Kodexempel -> Quiz-frågor
- Tabeller -> Quiz-frågor

Detta ersätter statisk study_data med dynamiskt innehåll från moduler.
"""
import re
from typing import List, Dict, Optional, Any
from src.db.seeds.content import get_all_modules

# Hämta moduler vid import
ALL_MODULES = get_all_modules()

# Import manuellt skapad studydata för tentaplugg-moduler
try:
    from src.db.seeds.study_data.tentaplugg_linux_study import TENTAPLUGG_LINUX_STUDY
    MANUAL_STUDY_DATA = {
        "tentaplugg-linux": TENTAPLUGG_LINUX_STUDY
    }
except ImportError:
    MANUAL_STUDY_DATA = {}


# =============================================================================
# MODULE REGISTRY - Mappar slug till modul-data
# =============================================================================

def get_module_registry() -> Dict[str, dict]:
    """Bygg en registry av alla moduler med slug som nyckel"""
    registry = {}
    for module in ALL_MODULES:
        slug = module.get("slug", "")
        if slug:
            registry[slug] = module
    return registry


MODULE_REGISTRY = get_module_registry()


def get_all_v3_modules() -> List[str]:
    """Returnera alla modul-slugs som har V3-formaterat innehåll"""
    # Endast de 9 refaktorerade modulerna har V3-format
    v3_slugs = [
        "linux-mastery",
        "docker-mastery",
        "kubernetes-mastery",
        "git-github-mastery",
        "bash-mastery",
        "terraform-mastery",
        "ansible-mastery",
        "cicd-mastery",
        "aws-mastery",
    ]
    # Lägg till manuellt skapade studydata-moduler
    manual_slugs = list(MANUAL_STUDY_DATA.keys())
    all_slugs = [slug for slug in v3_slugs if slug in MODULE_REGISTRY]
    all_slugs.extend(manual_slugs)
    return all_slugs


# =============================================================================
# CONTENT EXTRACTION - Extrahera flashcards och quiz från nod-innehåll
# =============================================================================

def extract_key_takeaways(content: str) -> List[Dict[str, str]]:
    """
    Extrahera Key Takeaways-tabellen från nodinnehåll.
    V3-format: | Koncept | Detalj |
    """
    flashcards = []

    # Hitta Key Takeaways-sektionen
    takeaway_pattern = r'## Key Takeaways\s*\n\s*\|[^\n]+\|\s*\n\s*\|[-\s|]+\|\s*\n((?:\|[^\n]+\|\s*\n)+)'
    match = re.search(takeaway_pattern, content)

    if match:
        table_rows = match.group(1)
        # Parsa varje rad: | Koncept | Detalj |
        row_pattern = r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
        for row_match in re.finditer(row_pattern, table_rows):
            koncept = row_match.group(1).strip()
            detalj = row_match.group(2).strip()
            if koncept and detalj and koncept != "Koncept":
                flashcards.append({
                    "front": koncept,
                    "back": detalj
                })

    return flashcards


def extract_kom_ihag(content: str) -> List[Dict[str, str]]:
    """
    Extrahera Kom ihåg-punkterna från nodinnehåll.
    V3-format: ## Kom ihag\n- punkt1\n- punkt2
    """
    flashcards = []

    # Hitta Kom ihag-sektionen
    kom_ihag_pattern = r'## Kom ihag\s*\n((?:- [^\n]+\n?)+)'
    match = re.search(kom_ihag_pattern, content)

    if match:
        bullets = match.group(1)
        # Parsa varje punkt
        for line in bullets.strip().split('\n'):
            line = line.strip()
            if line.startswith('- '):
                punkt = line[2:].strip()
                if punkt:
                    # Skapa flashcard med första delen som front
                    # Om det finns ett kolon, dela där
                    if ':' in punkt:
                        parts = punkt.split(':', 1)
                        flashcards.append({
                            "front": parts[0].strip(),
                            "back": parts[1].strip()
                        })
                    else:
                        # Annars använd punkten som back, skapa generisk front
                        flashcards.append({
                            "front": "Kom ihåg",
                            "back": punkt
                        })

    return flashcards


def extract_commands_table(content: str) -> List[Dict[str, Any]]:
    """
    Extrahera kommandotabeller för quiz-frågor.
    V3-format: | Kommando | Beskrivning |
    """
    quiz_questions = []

    # Hitta tabeller med kommandon
    table_pattern = r'\|[^\n]*[Kk]ommando[^\n]*\|\s*\n\s*\|[-\s|]+\|\s*\n((?:\|[^\n]+\|\s*\n)+)'

    for match in re.finditer(table_pattern, content):
        table_rows = match.group(1)
        row_pattern = r'\|\s*`?([^|`]+?)`?\s*\|\s*([^|]+?)\s*\|'

        commands = []
        for row_match in re.finditer(row_pattern, table_rows):
            cmd = row_match.group(1).strip()
            desc = row_match.group(2).strip()
            if cmd and desc and not cmd.startswith('-'):
                commands.append({"cmd": cmd, "desc": desc})

        # Skapa quiz-frågor från kommandona
        for i, cmd_data in enumerate(commands[:10]):  # Max 10 per tabell
            # Hitta 3 felaktiga alternativ
            wrong_options = [c["desc"] for c in commands if c["cmd"] != cmd_data["cmd"]][:3]

            if len(wrong_options) >= 3:
                options = [cmd_data["desc"]] + wrong_options
                # Blanda inte här - det görs vid servering
                quiz_questions.append({
                    "question": f"Vad gör kommandot: {cmd_data['cmd']}?",
                    "options": options,
                    "correct": 0,  # Rätt svar är alltid första (blandas senare)
                    "explanation": f"{cmd_data['cmd']} - {cmd_data['desc']}"
                })

    return quiz_questions


def extract_concept_table(content: str, title: str) -> List[Dict[str, Any]]:
    """
    Extrahera koncept-tabeller för quiz-frågor.
    """
    quiz_questions = []

    # Hitta "Varfor viktigt for DevOps?"-tabellen
    pattern = r'## Varfor viktigt for DevOps\?\s*\n\s*\|[^\n]+\|\s*\n\s*\|[-\s|]+\|\s*\n((?:\|[^\n]+\|\s*\n)+)'
    match = re.search(pattern, content)

    if match:
        table_rows = match.group(1)
        row_pattern = r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'

        concepts = []
        for row_match in re.finditer(row_pattern, table_rows):
            problem = row_match.group(1).strip()
            consequence = row_match.group(2).strip()
            if problem and consequence:
                concepts.append({"problem": problem, "consequence": consequence})

        # Skapa quiz-frågor
        for concept in concepts[:5]:  # Max 5 per nod
            wrong = [c["consequence"] for c in concepts if c["problem"] != concept["problem"]][:3]

            if len(wrong) >= 3:
                quiz_questions.append({
                    "question": f"I {title}: Vad är konsekvensen av '{concept['problem']}'?",
                    "options": [concept["consequence"]] + wrong,
                    "correct": 0,
                    "explanation": f"{concept['problem']} -> {concept['consequence']}"
                })

    return quiz_questions


# =============================================================================
# GENERATE STUDY DATA - Huvudfunktion för att generera studydata
# =============================================================================

def generate_study_data_for_module(module_slug: str) -> Optional[Dict[str, Any]]:
    """
    Generera flashcards och quiz från en moduls V3-innehåll.

    Returns:
        Dict med module_slug, flashcards, quiz eller None om modulen inte finns
    """
    module = MODULE_REGISTRY.get(module_slug)
    if not module:
        return None

    tasks = module.get("tasks", [])
    if not tasks:
        return None

    all_flashcards = {"easy": [], "medium": [], "hard": []}
    all_quiz = {"easy": [], "medium": [], "hard": []}

    for i, task in enumerate(tasks):
        content = task.get("content", "")
        title = task.get("title", f"Node {i+1}")
        difficulty = task.get("difficulty", "intermediate")

        # Mappa difficulty till easy/medium/hard
        diff_map = {
            "easy": "easy",
            "beginner": "easy",
            "intermediate": "medium",
            "medium": "medium",
            "advanced": "hard",
            "hard": "hard"
        }
        diff_key = diff_map.get(difficulty, "medium")

        # Extrahera flashcards
        takeaways = extract_key_takeaways(content)
        kom_ihag = extract_kom_ihag(content)

        for fc in takeaways:
            fc["source"] = title
            all_flashcards[diff_key].append(fc)

        for fc in kom_ihag:
            fc["source"] = title
            all_flashcards[diff_key].append(fc)

        # Extrahera quiz
        cmd_quiz = extract_commands_table(content)
        concept_quiz = extract_concept_table(content, title)

        for q in cmd_quiz:
            q["source"] = title
            all_quiz[diff_key].append(q)

        for q in concept_quiz:
            q["source"] = title
            all_quiz[diff_key].append(q)

    return {
        "module_slug": module_slug,
        "module_title": module.get("name", module_slug),
        "module_description": module.get("description", ""),
        "icon": module.get("icon", "📚").replace("🐳", "Box").replace("🐧", "Terminal").replace("☸️", "Layers"),
        "flashcards": all_flashcards,
        "quiz": all_quiz,
        "generated_from": "v3_module_content"
    }


def get_v3_study_data(module_slug: str) -> Optional[Dict[str, Any]]:
    """
    Hämta studydata för en modul.
    Prioriterar manuellt skapad studydata, annars genererar dynamiskt.
    """
    # Kolla först om vi har manuellt skapad studydata
    if module_slug in MANUAL_STUDY_DATA:
        manual_data = MANUAL_STUDY_DATA[module_slug]
        # Transformera till format som study.py förväntar sig
        return {
            "module_slug": manual_data.get("module_slug", module_slug),
            "module_title": manual_data.get("module_title", module_slug),
            "module_description": manual_data.get("module_description", ""),
            "icon": manual_data.get("icon", "BookOpen"),
            "flashcards": _transform_manual_flashcards(manual_data),
            "quiz": _transform_manual_quiz(manual_data),
            "nodes": manual_data.get("nodes", {}),
            "source": "manual_study_data"
        }

    # Annars generera dynamiskt från V3-modulinnehåll
    return generate_study_data_for_module(module_slug)


def _transform_manual_flashcards(data: Dict) -> Dict[str, List]:
    """Transformerar manuellt skapade flashcards till rätt format"""
    all_flashcards = {"easy": [], "medium": [], "hard": []}

    nodes = data.get("nodes", {})
    for node_slug, node_data in nodes.items():
        flashcards = node_data.get("flashcards", {})
        title = node_data.get("title", node_slug)

        for difficulty in ["easy", "medium", "hard"]:
            for fc in flashcards.get(difficulty, []):
                all_flashcards[difficulty].append({
                    "front": fc.get("front", ""),
                    "back": fc.get("back", ""),
                    "source": title
                })

    return all_flashcards


def _transform_manual_quiz(data: Dict) -> Dict[str, List]:
    """Transformerar manuellt skapade quiz till rätt format"""
    all_quiz = {"easy": [], "medium": [], "hard": []}

    nodes = data.get("nodes", {})
    for node_slug, node_data in nodes.items():
        quiz = node_data.get("quiz", {})
        title = node_data.get("title", node_slug)

        for difficulty in ["easy", "medium", "hard"]:
            for q in quiz.get(difficulty, []):
                all_quiz[difficulty].append({
                    "question": q.get("question", ""),
                    "options": q.get("options", []),
                    "correct": q.get("correct", 0),
                    "explanation": q.get("explanation", ""),
                    "source": title
                })

    return all_quiz


def get_v3_study_modules() -> List[str]:
    """Returnera alla tillgängliga V3-moduler"""
    return get_all_v3_modules()


# =============================================================================
# ICON MAPPING
# =============================================================================

ICON_MAP = {
    "linux-mastery": "Terminal",
    "docker-mastery": "Box",
    "kubernetes-mastery": "Layers",
    "git-github-mastery": "GitBranch",
    "bash-mastery": "Code",
    "terraform-mastery": "Cloud",
    "ansible-mastery": "Server",
    "cicd-mastery": "GitBranch",
    "aws-mastery": "Cloud",
    "tentaplugg-linux": "GraduationCap",
}


def get_module_icon(module_slug: str) -> str:
    """Hämta ikon för en modul"""
    return ICON_MAP.get(module_slug, "BookOpen")
