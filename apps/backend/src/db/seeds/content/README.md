# Content System — DevOpsHub

> **Single Source of Truth** för allt innehåll på sidan.

## 📁 Struktur

```
src/db/seeds/
├── content/                 # ← ENDA källan för content
│   ├── __init__.py         # API: get_all_modules(), get_tracks()
│   ├── _template.py        # Mall för nya moduler
│   └── [dina_moduler.py]   # Lägg moduler här
│
└── _archive/               # Gammalt content (arkiverat, ej aktivt)
    ├── bootcamp_v3_data.py
    ├── modules/
    ├── modules_v3/
    └── ...
```

## 🚀 Snabbstart: Lägg till en modul

### 1. Kopiera mallen

```bash
cp content/_template.py content/linux.py
```

### 2. Editera din modul

```python
# content/linux.py
MODULE = {
    "name": "Linux Mastery",
    "slug": "linux-mastery",
    "description": "Lär dig Linux från grunden",
    "track_slug": "foundation",
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "tasks": [
        {
            "title": "Filesystem Hierarchy",
            "content": "# Introduktion...",
            "difficulty": "easy",
            "xp_reward": 100,
        },
        # ... fler tasks
    ]
}
```

### 3. Importera i **init**.py

```python
# content/__init__.py
from .linux import MODULE as LINUX_MODULE

ALL_MODULES = [LINUX_MODULE]
```

### 4. Starta om backend

```bash
cd apps/backend
python -m uvicorn src.main:app --reload
```

Modulen syns nu på sidan! 🎉

---

## 📖 API Reference

### `get_all_modules() → list[dict]`

Returnerar alla moduler. Tom lista = ingen content på sidan.

### `get_module_by_slug(slug: str) → dict | None`

Hämta en specifik modul.

### `get_tracks() → list[dict]`

Returnerar alla tracks (kategorier).

### `get_bootcamp_summary() → dict`

Sammanfattning: antal moduler, tasks, tracks.

---

## 📦 Modul-schema

```python
MODULE = {
    # Metadata
    "name": str,              # Visas på sidan
    "slug": str,              # URL-ID (unikt!)
    "description": str,
    "track_slug": str,        # foundation, cloud-infrastructure, etc.
    "order_index": int,
    "difficulty": str,        # beginner, intermediate, advanced, expert
    "estimated_hours": float,
    "prerequisites": list,    # ["linux-mastery"]
    "icon": str,              # Emoji
    "color": str,             # Hex

    # Tasks (nodes)
    "tasks": [
        {
            "title": str,
            "slug": str,      # Valfritt
            "description": str,
            "content": str,   # Markdown
            "difficulty": str,  # easy, medium, hard
            "estimated_minutes": int,
            "xp_reward": int,
            "content_blocks": list,  # Valfritt (quiz, terminal)
            "requirements": list,    # Valfritt
        }
    ],

    # Valfritt
    "labs": [...],
    "project": {...},
}
```

---

## 🔧 Återanvända gammalt content

Vill du använda content från arkivet?

```python
# content/__init__.py

# Importera från arkivet
import sys
sys.path.insert(0, str(Path(__file__).parent / "_archive"))
from _archive.modules.linux import MODULE as LINUX_MODULE

ALL_MODULES = [LINUX_MODULE]
```

---

## ❓ FAQ

**Q: Varför syns inte min modul?**
A:

1. Kolla att du importerat den i `__init__.py`
2. Kolla att den ligger i `ALL_MODULES`-listan
3. Starta om backend

**Q: Hur tar jag bort en modul?**
A: Ta bort den från `ALL_MODULES` i `__init__.py`

**Q: Var är det gamla innehållet?**
A: Arkiverat i `_archive/`. Kan importeras om du vill.
