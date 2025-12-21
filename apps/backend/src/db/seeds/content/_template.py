"""
Module Template — Kopiera denna för att skapa nya moduler
=========================================================

Användning:
1. Kopiera denna fil till t.ex. `linux.py`
2. Fyll i MODULE med dina värden
3. Importera i __init__.py:
   from .linux import MODULE as LINUX_MODULE
   ALL_MODULES = [LINUX_MODULE]
"""

MODULE = {
    # ==========================================================================
    # METADATA
    # ==========================================================================
    "name": "Module Name",                    # Visas på sidan
    "slug": "module-slug",                    # URL-vänligt ID (unikt!)
    "description": "En beskrivning av modulen som visas på kortet.",

    # Track (valfritt - för gruppering)
    "track_slug": "foundation",               # foundation, cloud-infrastructure, etc.

    # Ordning och svårighet
    "order_index": 1,                         # Sorteringsordning
    "difficulty": "intermediate",             # beginner, intermediate, advanced, expert
    "estimated_hours": 20,                    # Uppskattad tid att slutföra

    # Förkunskaper (lista med modul-slugs)
    "prerequisites": [],                      # ["linux-mastery", "git-github-mastery"]

    # Visuellt
    "icon": "🐧",                             # Emoji för modulen
    "color": "#FCC624",                       # Hex färg för kortet

    # ==========================================================================
    # TASKS (Nodes) — Lektionerna i modulen
    # ==========================================================================
    "tasks": [
        {
            "title": "Task 1: Introduction",
            "slug": "introduction",           # URL-vänligt (valfritt)
            "description": "Kort beskrivning som syns i listan",

            # Svårighet och tid
            "difficulty": "easy",             # easy, medium, hard
            "estimated_minutes": 30,
            "xp_reward": 100,

            # Innehåll — Markdown
            "content": """# Introduktion

Välkommen till denna modul! Här lär du dig grunderna.

## Vad du kommer lära dig

- Punkt 1
- Punkt 2
- Punkt 3

## Teori

Lorem ipsum dolor sit amet...

```bash
# Exempel på kod
echo "Hello World"
```

## Sammanfattning

Du har nu lärt dig grunderna!
""",

            # Interaktiva block (valfritt - för quiz, terminal, etc.)
            "content_blocks": None,

            # Krav för att slutföra (valfritt)
            "requirements": None,
        },

        {
            "title": "Task 2: Hands-on Practice",
            "slug": "hands-on-practice",
            "description": "Praktisk övning",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 150,
            "content": """# Praktisk övning

Nu ska vi öva på det du lärt dig!

## Övning 1

Gör detta...

## Övning 2

Gör sedan detta...
""",
            "content_blocks": None,
            "requirements": None,
        },

        # Lägg till fler tasks här...
    ],

    # ==========================================================================
    # LABS (Valfritt) — Större praktiska övningar
    # ==========================================================================
    "labs": [
        # {
        #     "title": "Lab: Build Something",
        #     "slug": "lab-build-something",
        #     "hours": 2.0,
        # },
    ],

    # ==========================================================================
    # PROJECT (Valfritt) — Avslutande projekt
    # ==========================================================================
    "project": None,
    # Eller:
    # "project": {
    #     "title": "Final Project",
    #     "slug": "final-project",
    #     "description": "Bygg något coolt!",
    #     "deliverables": ["Deliverable 1", "Deliverable 2"],
    #     "xp_reward": 500,
    #     "estimated_hours": 5.0,
    # },
}
