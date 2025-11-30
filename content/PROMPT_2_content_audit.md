# PROMPT 2: Content Audit — Kartlägg Generiskt Innehåll

## KONTEXT

DevOpsHub har 359 tasks i v3.0 och 500+ i v4.0.
Misstänkt: De flesta har generiskt placeholder-innehåll.

## UPPDRAG

Skapa en komplett inventering av innehållskvalitet för ALLA tasks.

## STEG 1: Exportera alla tasks

```python
# Skapa script: audit_content.py
import json
from pathlib import Path

# Anslut till databas eller läs seed-filer
# Exportera alla tasks med följande fält:
# - id
# - title
# - module_slug
# - content_preview (första 200 tecken)
# - has_code_blocks (bool)
# - code_block_count (int)
# - word_count (int)
```

## STEG 2: Identifiera generiska mönster

Sök efter dessa placeholder-fraser:

```python
GENERIC_PATTERNS = [
    "This lesson will teach you the fundamentals",
    "Follow along with the examples below",
    "Understanding the basics",
    "Practical applications", 
    "Best practices",
    "You've learned the core concepts",
    "Practice these skills to reinforce",
    "Concept 1:",
    "Concept 2:",
    "Concept 3:",
    "[object Object]",
    "Lorem ipsum",
    "TODO",
    "PLACEHOLDER",
]

def is_generic(content: str) -> bool:
    return any(pattern.lower() in content.lower() for pattern in GENERIC_PATTERNS)
```

## STEG 3: Kategorisera varje task

```python
class ContentQuality:
    EMPTY = "empty"           # Ingen content
    GENERIC = "generic"       # Placeholder-text
    PARTIAL = "partial"       # Har något innehåll men ofullständigt
    COMPLETE = "complete"     # Fullt pedagogiskt innehåll
```

## STEG 4: Generera rapport

Output-fil: `content_audit_report.json`

```json
{
  "summary": {
    "total_tasks": 359,
    "empty": 0,
    "generic": 340,
    "partial": 15,
    "complete": 4
  },
  "by_module": {
    "environment-setup": {
      "total": 17,
      "generic": 16,
      "needs_rewrite": ["task-1", "task-2", ...]
    }
  },
  "tasks": [
    {
      "id": "uuid",
      "title": "Create personal dotfiles repository",
      "module": "environment-setup",
      "quality": "generic",
      "issues": ["generic_intro", "placeholder_concepts", "no_real_code"],
      "priority": "high"
    }
  ]
}
```

## STEG 5: Prioritera omskrivningar

### Prioritet 1 (Kritisk) — Track 1 Foundation
Dessa är första intryck för nya användare:
- Module 01: Environment Setup (17 tasks)
- Module 02: Linux Mastery
- Module 03: Shell Scripting

### Prioritet 2 (Hög) — Mest använda
- Module 04: Git Workflows
- Module 10: Docker Fundamentals
- Module 12: Kubernetes Core

### Prioritet 3 (Medel) — Resten av v3.0
Alla övriga moduler i ordning

### Prioritet 4 (Låg) — v4.0
Avancerat innehåll, kan vänta

## FÖRVÄNTAD OUTPUT

1. `content_audit_report.json` — Fullständig inventering
2. `rewrite_queue.md` — Prioriterad lista för omskrivning
3. Uppdaterat Command Center med audit-resultat

## SUCCESS CRITERIA

- [ ] Varje task har en kvalitetsbedömning
- [ ] Prioriterad kö för omskrivningar finns
- [ ] Tydlig bild av arbetsmängd (hur många tasks behöver skrivas om)

## COMMIT MESSAGE

```
docs(audit): complete content quality audit

- Audited all 359 v3.0 tasks
- Identified X generic/placeholder tasks
- Created prioritized rewrite queue
- Added quality metrics to Command Center
```

## NÄSTA STEG

Med audit klar, fortsätt med PROMPT_3_content_template.md för att börja skriva om innehåll.
