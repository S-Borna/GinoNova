"""
Dallas Dynamic FAQ - Läser automatiskt från ALL_V3_MODULES.
Ingen GPT-kostnad - endast lokala svar från plattformens faktiska innehåll.

Version: 2.0 - Dynamisk (läser från moduler automatiskt)
"""

from typing import Optional, List, Tuple, Dict, Any
import re
from functools import lru_cache


def get_all_modules() -> List[Dict[str, Any]]:
    """Hämta alla moduler från v3 systemet."""
    try:
        from ..db.seeds.modules_v3 import ALL_V3_MODULES
        return ALL_V3_MODULES
    except ImportError:
        return []


def normalize_text(text: str) -> str:
    """Normalize text for matching."""
    text = text.lower().strip()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text


def extract_keywords_from_module(module: Dict[str, Any]) -> List[str]:
    """Extrahera sökbara keywords från en modul."""
    keywords = []

    # Namn och slug
    name = module.get("name", "").lower()
    slug = module.get("slug", "").lower()
    keywords.extend(name.split())
    keywords.extend(slug.replace("-", " ").split())

    # Tags
    tags = module.get("tags", [])
    keywords.extend([t.lower() for t in tags])

    # Prerequisites
    prereqs = module.get("prerequisites", [])
    keywords.extend([p.lower() for p in prereqs])

    # Extrahera från tasks
    for task in module.get("tasks", [])[:5]:  # Första 5 tasks för keywords
        title = task.get("title", "").lower()
        keywords.extend(title.split()[:3])  # Första 3 ord per task

    # Ta bort common words
    stop_words = {"the", "a", "an", "and", "or", "for", "to", "in", "on", "with", "är", "och", "för", "med", "på"}
    keywords = [k for k in keywords if k not in stop_words and len(k) > 2]

    return list(set(keywords))


def extract_topics_from_module(module: Dict[str, Any]) -> List[str]:
    """Extrahera topics från tasks för bättre svar."""
    topics = []
    for task in module.get("tasks", []):
        topics.append(task.get("title", ""))
    return topics[:10]  # Max 10 topics i svaret


@lru_cache(maxsize=1)
def build_module_index() -> Dict[str, Dict[str, Any]]:
    """
    Bygger ett index över alla moduler för snabb sökning.
    Cached för prestanda.
    """
    modules = get_all_modules()
    index = {}

    for module in modules:
        slug = module.get("slug", "")
        keywords = extract_keywords_from_module(module)

        index[slug] = {
            "module": module,
            "keywords": keywords,
            "name": module.get("name", ""),
            "description": module.get("description", ""),
            "topics": extract_topics_from_module(module),
        }

    return index


def find_matching_modules(query: str) -> List[Tuple[Dict[str, Any], float]]:
    """
    Hitta moduler som matchar en fråga.
    Returnerar lista av (module_info, score) sorterad efter relevans.
    """
    query_normalized = normalize_text(query)
    query_words = set(query_normalized.split())

    index = build_module_index()
    matches = []

    for slug, info in index.items():
        score = 0.0

        # Exakt match på namn eller slug (högst score)
        if slug in query_normalized or info["name"].lower() in query_normalized:
            score += 1.0

        # Keyword matches
        keyword_matches = sum(1 for kw in info["keywords"] if kw in query_normalized)
        if keyword_matches > 0:
            score += 0.3 * min(keyword_matches / max(len(info["keywords"]), 1), 1.0)

        # Word overlap med query
        for kw in info["keywords"]:
            if kw in query_words:
                score += 0.2

        if score > 0.1:
            matches.append((info, score))

    # Sortera efter score (högst först)
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:3]  # Max 3 träffar


def generate_module_response(module_info: Dict[str, Any]) -> str:
    """Generera ett svar baserat på en modul."""
    module = module_info["module"]
    name = module.get("name", "Unknown")
    slug = module.get("slug", "")
    description = module.get("description", "")
    difficulty = module.get("difficulty", "intermediate")
    hours = module.get("estimated_hours", 10)
    topics = module_info.get("topics", [])

    # Bygg svaret
    response = f"""**{name}** täcks i vårt innehåll!

📖 {description if description else f'Lär dig {name} från grunden.'}

**Detaljer:**
• Svårighetsgrad: {difficulty.capitalize()}
• Uppskattad tid: {hours} timmar
• Antal topics: {len(module.get('tasks', []))}

"""

    if topics:
        response += "**Topics som täcks:**\n"
        for i, topic in enumerate(topics[:8], 1):
            response += f"• {topic}\n"
        if len(topics) > 8:
            response += f"• ...och {len(topics) - 8} till!\n"

    response += f"\nGå till: **SkillsMaps → {name}** eller sök på '{slug}' i Camp DevOps."

    return response


# =============================================================================
# STATISKA FAQ ENTRIES (plattformsfrågor som inte relaterar till specifika moduler)
# =============================================================================

STATIC_FAQ: List[Tuple[List[str], List[str], str]] = [
    (
        ["devopshub", "plattform", "vad är", "hur funkar", "sida", "sidan", "hub"],
        ["vad är devopshub", "hur funkar sidan", "vad kan jag göra här", "vad är detta"],
        """**DevOpsHub** är en lärplattform för tech! 🚀

Här kan du lära dig:
• **DevOps** - Linux, Docker, Kubernetes, CI/CD, Terraform
• **Cloud** - AWS, Azure, GCP
• **Programmering** - Python, JavaScript, TypeScript, Go, Java, C#
• **Data & AI** - SQL, MLOps, AI Agents, Prompt Engineering
• **Arkitektur** - System Design, Microservices

**Hur du börjar:**
1. Gå till **Camp DevOps** för strukturerade moduler
2. Utforska **SkillsMaps** för djupa lärvägar
3. Använd **Studyflow** för fokuserade sessioner

Välj ett ämne som intresserar dig och börja lära!"""
    ),

    (
        ["camp", "moduler", "bootcamp", "kurser"],
        ["vad är camp", "vilka moduler finns", "hur funkar moduler"],
        """**Camp** innehåller strukturerade lärmoduler med tasks.

Varje modul har:
• Teori och koncept
• Kodexempel
• Praktiska övningar
• XP-belöningar

Slutför tasks för att samla XP och se din progress!"""
    ),

    (
        ["skillsmap", "skillsmaps", "lärväg", "nodes", "nod"],
        ["vad är skillsmaps", "hur funkar skillsmaps"],
        """**SkillsMaps** är djupa lärvägar med 20 nodes per ämne.

Varje node innehåller:
• Detaljerad teori (~5000+ tecken)
• ASCII-visualiseringar
• Kodexempel med förklaringar
• Praktiska övningar
• Pro tips

Perfekt för djupinlärning av ett ämne!"""
    ),

    (
        ["xp", "poäng", "level", "nivå", "progress"],
        ["hur får jag xp", "vad är xp", "poängsystem"],
        """**XP-systemet** belönar ditt lärande!

• Slutför tasks → Få XP
• Svara rätt på quiz → Bonus XP
• Håll streaks → Extra belöningar

Se din progress på Dashboard!"""
    ),

    (
        ["dallas", "du", "vem", "assistent"],
        ["vem är du", "vad är dallas"],
        """Jag är **Dallas** 🐺 - din guide!

Jag kan hjälpa dig:
• Hitta rätt modul eller SkillsMap
• Förklara vad som finns på plattformen
• Svara på frågor om innehållet

Ställ en fråga så guidar jag dig rätt!"""
    ),

    (
        ["börja", "start", "nybörjare", "var börjar jag", "ny"],
        ["var börjar jag", "hur startar jag", "ny här"],
        """Välkommen! 🎉 Här är tips baserat på din inriktning:

**DevOps/Infra:**
1. Linux Mastery → Grunden
2. Docker → Containers
3. Kubernetes → Orchestration
4. CI/CD → Automation

**Backend-utvecklare:**
1. Python/Node.js/Go → Välj ett språk
2. SQL → Databaser
3. System Design → Arkitektur

**Frontend/Fullstack:**
1. JavaScript/TypeScript → Grund
2. React/Next.js → Framework
3. Node.js → Backend basics

**Cloud:**
1. AWS eller Azure → Välj en
2. Terraform → Infrastructure as Code

Gå till **Camp** och välj din första modul!"""
    ),

    (
        ["hjälp", "support", "problem", "funkar inte"],
        ["hjälp", "support", "problem"],
        """Behöver du hjälp? 🤝

• **Hitta innehåll** - Fråga mig om specifika ämnen
• **Tekniska problem** - Prova ladda om sidan
• **Frågor** - Beskriv vad du letar efter

Jag kan hjälpa dig hitta rätt modul!"""
    ),
]


def find_static_match(query: str) -> Tuple[Optional[str], float]:
    """Sök i statiska FAQ entries."""
    query_normalized = normalize_text(query)
    query_words = set(query_normalized.split())

    best_answer = None
    best_score = 0.0

    for keywords, patterns, answer in STATIC_FAQ:
        score = 0.0

        # Keyword matches
        keyword_matches = sum(1 for kw in keywords if kw in query_normalized)
        if keyword_matches > 0:
            score += 0.4 * min(keyword_matches / len(keywords), 1.0)

        # Pattern matches
        for pattern in patterns:
            pattern_normalized = normalize_text(pattern)
            pattern_words = set(pattern_normalized.split())
            overlap = len(query_words & pattern_words)
            if overlap > 0:
                pattern_score = overlap / max(len(pattern_words), len(query_words))
                score = max(score, 0.5 + 0.5 * pattern_score)

        if score > best_score:
            best_score = score
            best_answer = answer

    return best_answer, best_score


def get_available_modules_summary() -> str:
    """Generera en sammanfattning av alla tillgängliga moduler."""
    modules = get_all_modules()

    if not modules:
        return "Inga moduler laddade."

    # Gruppera efter "track" eller kategori
    summary = f"**{len(modules)} moduler tillgängliga:**\n\n"

    for module in sorted(modules, key=lambda m: m.get("name", "")):
        name = module.get("name", "Unknown")
        tasks = len(module.get("tasks", []))
        summary += f"• **{name}** ({tasks} tasks)\n"

    return summary


# =============================================================================
# HUVUDFUNKTION
# =============================================================================

NO_MATCH_RESPONSE = """Jag hittade tyvärr inget svar på din fråga. 🤔

**Tips:**
• Prova att omformulera frågan
• Fråga om specifika teknologier (Docker, Python, AWS, etc.)
• Utforska modulerna i Camp eller SkillsMaps

Jag kan hjälpa dig hitta rätt modul om du berättar vad du vill lära dig!"""


def get_dallas_response(query: str) -> dict:
    """
    Dynamisk Dallas-respons som läser från moduler.

    Prioritetsordning:
    1. Exakt modul-match (högst)
    2. Statiska FAQ (plattformsfrågor)
    3. Modul-keyword match
    4. Fallback
    """

    # 1. Kolla om det är en fråga om "alla moduler" eller "lista"
    if any(word in query.lower() for word in ["alla moduler", "vilka moduler", "lista", "vad finns"]):
        return {
            "response": get_available_modules_summary(),
            "confidence": 0.9,
            "source": "module_list"
        }

    # 2. Sök i moduler
    module_matches = find_matching_modules(query)

    # 3. Sök i statiska FAQ
    static_answer, static_score = find_static_match(query)

    # 4. Bestäm bästa svaret
    if module_matches:
        best_module, module_score = module_matches[0]

        # Om modulmatch är stark, använd den
        if module_score > 0.5 or (module_score > static_score):
            response = generate_module_response(best_module)

            # Lägg till relaterade moduler om det finns fler
            if len(module_matches) > 1:
                response += "\n\n**Relaterade ämnen:**\n"
                for info, _ in module_matches[1:3]:
                    response += f"• {info['name']}\n"

            return {
                "response": response,
                "confidence": min(module_score, 1.0),
                "source": "dynamic_module"
            }

    # 5. Använd statisk FAQ om score är tillräcklig
    if static_answer and static_score >= 0.25:
        return {
            "response": static_answer,
            "confidence": static_score,
            "source": "static_faq"
        }

    # 6. Fallback
    return {
        "response": NO_MATCH_RESPONSE,
        "confidence": 0.0,
        "source": "no_match"
    }


def clear_cache():
    """Rensa cache (anropas vid moduluppdateringar)."""
    build_module_index.cache_clear()
