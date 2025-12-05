# 📘 SKILLSMAPS CREATION MANUAL

> **Version:** 1.0
> **Senast uppdaterad:** 2025-12-05 UTC
> **Syfte:** Komplett guide för att skapa nya SkillsMaps i DevOpsHub
> **Kvalitetsstandard:** Premium Bootcamp-content (5000+ chars/nod)

---

## 🚨 KRITISK REGEL: ALDRIG MER MOCK DATA

Alla SkillsMaps **MÅSTE** byggas via backend-first approach:

1. **Backend:** Skapa modul-fil i `modules_v3/` eller `skillsmaps/`
2. **Registrera:** Lägg till i `modules_v3/__init__.py`
3. **Seed:** Kör seed-script eller API-endpoint
4. **Frontend:** Hämtar automatiskt via API (ingen mock data!)

---

## 📂 FILSTRUKTUR

### Enkel modul (~1500 rader)

```bash
apps/backend/src/db/seeds/modules_v3/
└── module_{slug}.py        # All content i en fil
```

### Splittad modul (~3000+ rader, rekommenderat)

```bash
apps/backend/src/db/seeds/skillsmaps/{slug}/
├── __init__.py             # Metadata + importerar blocks
├── block_1_fundamentals.py # Nodes 1-4
├── block_2_intermediate.py # Nodes 5-8
├── block_3_advanced.py     # Nodes 9-12
├── block_4_production.py   # Nodes 13-16
└── block_5_expert.py       # Nodes 17-20
```

---

## 🏗️ STEG 1: SKAPA BACKEND-FIL

### `__init__.py` Mall (Splittad modul)

```python
"""
{Title} SkillsMap - {Description}
Based on roadmap.sh/{roadmap-slug}

Structure:
- Block 1: Fundamentals (4 nodes)
- Block 2: Intermediate (4 nodes)
- Block 3: Advanced (4 nodes)
- Block 4: Production (4 nodes)
- Block 5: Expert (4 nodes)

Total: 20 nodes, ~{hours} hours, {xp} XP
"""

from .block_1_fundamentals import BLOCK_1_NODES
from .block_2_intermediate import BLOCK_2_NODES
from .block_3_advanced import BLOCK_3_NODES
from .block_4_production import BLOCK_4_NODES
from .block_5_expert import BLOCK_5_NODES

SKILLSMAP_METADATA = {
    "id": "{slug}-mastery",
    "slug": "{slug}-mastery",
    "title": "{Title}",
    "description": "{Description på svenska}",
    "icon": "🎯",           # Emoji icon
    "color": "#HEX",        # Hex color for UI
    "difficulty": "intermediate",  # beginner/intermediate/advanced/expert
    "estimated_hours": 25,
    "total_xp": 2000,
    "prerequisites": ["python", "docker"],  # Slug av prerequisite modules
    "tags": ["Tag1", "Tag2", "Tag3"],
}

# Combine all nodes
ALL_NODES = (
    BLOCK_1_NODES + 
    BLOCK_2_NODES + 
    BLOCK_3_NODES + 
    BLOCK_4_NODES + 
    BLOCK_5_NODES
)

# VALIDATION - måste vara exakt 20 nodes!
NODE_COUNT = 20
assert len(ALL_NODES) == NODE_COUNT, f"Expected {NODE_COUNT} nodes, got {len(ALL_NODES)}"
```

### Modul-fil Mall (`module_{slug}.py`)

```python
"""
{Title} Module - DevOpsHub Bootcamp v3
======================================
Premium content med 5000+ chars per task.
"""

MODULE_{SLUG}_MASTERY = {
    "slug": "{slug}-mastery",
    "name": "{Title}",
    "description": "{Description}",
    "track_slug": "devops",  # devops/cloud/containers/platform
    "order_index": 1,
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "tags": ["Tag1", "Tag2"],
    "tasks": [
        # 20 tasks här...
    ]
}
```

---

## 📝 STEG 2: NODE/TASK STRUKTUR

### Obligatoriska fält per node

| Fält | Typ | Beskrivning | Krav |
|------|-----|-------------|------|
| `id` | string | Unik identifierare | `{slug}-{number}` |
| `slug` | string | URL-säker identifierare | `{topic-name}` |
| `title` | string | Visningsnamn | Max 60 tecken |
| `order_index` | int | Ordning 1-20 | Unikt per modul |
| `estimated_minutes` | int | Tid i minuter | 20-60 |
| `xp_reward` | int | XP belöning | 50-150 |
| `difficulty` | string | Svårighetsgrad | easy/medium/hard |
| `node_type` | string | Typ av node | concept/practice/challenge/quiz/project |
| `prerequisites` | list | ID:n av tidigare nodes | `[]` eller `["id1"]` |
| `content` | string | Pedagogiskt innehåll | **MIN 5000 tecken!** |

### Node Mall

```python
{
    "id": "mlops-01",
    "slug": "introduction-to-mlops",
    "title": "Introduction to MLOps",
    "order_index": 1,
    "estimated_minutes": 30,
    "xp_reward": 100,
    "difficulty": "easy",
    "node_type": "concept",
    "prerequisites": [],
    "content": """# Introduction to MLOps

## Varför detta är viktigt

[HOOK - Varför bryr vi oss? Verkligt problem som löses]

MLOps löser ett kritiskt problem i ML-projekt: 87% av ML-modeller 
når aldrig produktion. Utan MLOps hamnar modeller i "notebook-helvetet"...

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Förstå skillnaden mellan ML-development och ML-production
- ✅ Identifiera MLOps maturity levels (0-2)
- ✅ Välja rätt verktyg för din organisations behov
- ✅ Designa en grundläggande ML-pipeline

## Kärnkoncept

### ML Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                      ML LIFECYCLE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │   Data   │──▶│  Train   │──▶│  Deploy  │──▶│ Monitor  │     │
│  │ Ingest   │   │  Model   │   │  Model   │   │  & Retrain│     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│       │              │              │              │             │
│       ▼              ▼              ▼              ▼             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              VERSION CONTROL & EXPERIMENT TRACKING        │  │
│  │              (MLflow, DVC, Weights & Biases)              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### MLOps vs DevOps

| Aspekt | DevOps | MLOps |
|--------|--------|-------|
| **Artefakt** | Code | Code + Data + Model |
| **Testning** | Unit/Integration | + Data validation, Model validation |
| **Deployment** | Application | Model serving |
| **Monitoring** | App metrics | + Data drift, Model drift |
| **Versioning** | Code | Code + Data + Model + Experiments |

## Steg-för-steg: Setup MLflow

### 1. Installation

```bash
# Installera MLflow
pip install mlflow

# Starta tracking server
mlflow server --host 0.0.0.0 --port 5000
```

### 2. Logga experiment

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sätt experiment
mlflow.set_experiment("my-ml-project")

# Starta run
with mlflow.start_run():
    # Logga parametrar
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    
    # Träna modell
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)
    
    # Logga metrics
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    mlflow.log_metric("accuracy", accuracy)
    
    # Logga modell
    mlflow.sklearn.log_model(model, "model")
    
    print(f"Accuracy: {accuracy:.4f}")
```

### 3. Verifiera

```bash
# Öppna MLflow UI
open http://localhost:5000

# Lista experiment via CLI
mlflow experiments list
```

## Vanliga problem

### Problem 1: "MLflow server startar inte"
```bash
# Lösning: Kontrollera att port 5000 är ledig
lsof -i :5000
# Döda process om upptagen
kill -9 <PID>
```

### Problem 2: "Kan inte hitta experiment"
```python
# Lösning: Sätt tracking URI explicit
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("my-experiment")
```

## Praktisk övning

**Uppgift:** Skapa ett komplett MLflow experiment

1. Installera MLflow
2. Starta tracking server
3. Skapa ett experiment med 3 runs (olika hyperparameters)
4. Jämför runs i MLflow UI
5. Exportera bästa modellen

```python
# Din kod här:
import mlflow

# TODO: Implementera enligt stegen ovan
```

## Sammanfattning

- ✅ MLOps = DevOps + Data + Models
- ✅ Maturity levels: Manual → Pipeline → CI/CD
- ✅ Verktyg: MLflow, DVC, Kubeflow, etc.
- ✅ Experiment tracking är grundläggande

## Nästa steg

Nu när du förstår MLOps-grunden, fortsätt till:
- **Node 2:** Version Control for ML (DVC)
- **Node 3:** Data Pipelines

---
*Tips: Bookmark denna sida för referens under resten av kursen.*
"""
}
```

---

## ✅ STEG 3: KVALITETSKRAV (PREMIUM CONTENT)

### Obligatoriska element per node

| Element | Beskrivning | Krav |
|---------|-------------|------|
| **Hook** | Varför är detta viktigt? | Första stycket |
| **Learning objectives** | Vad lär man sig? | 3-5 bullet points |
| **ASCII diagram** | Visualisering av koncept | MIN 1 per node |
| **Kod med förklaringar** | Praktiska exempel | 2-3 kodblock |
| **Steg-för-steg** | Konkreta instruktioner | Numrerade steg |
| **Vanliga problem** | Troubleshooting | 2-3 vanliga fel |
| **Praktisk övning** | Hands-on task | 1 övning |
| **Sammanfattning** | Key takeaways | 4-5 bullet points |
| **Nästa steg** | Vad kommer sen? | Länk till nästa node |

### Teckenräkning

| Kvalitet | Tecken | Godkänt |
|----------|--------|---------|
| 🔴 Minimal | < 2000 | ❌ NEJ |
| 🟠 Basic | 2000-4000 | ❌ NEJ |
| 🟡 Standard | 4000-5000 | ⚠️ Gränsen |
| 🟢 Premium | 5000-10000 | ✅ BRA |
| 🏆 Elite | 10000+ | ✅ UTMÄRKT |

**Snittlängd i V3:** ~14,643 tecken/node

### Språkstil

- **Rubriker:** Svenska
- **Kod:** Engelska (variabler, kommandon, kommentarer)
- **Förklaringar:** Svenska med tekniska termer på engelska
- **Ton:** Professionell men vänlig, som en erfaren mentor

---

## 🔄 STEG 4: REGISTRERA MODUL

### I `modules_v3/__init__.py`

```python
# Lägg till import
from .module_{slug} import MODULE_{SLUG}_MASTERY
# ELLER för splittad modul:
from .{slug} import MODULE_{SLUG}_MASTERY

# Lägg till i ALL_V3_MODULES
ALL_V3_MODULES = [
    # ... existing modules ...
    MODULE_{SLUG}_MASTERY,  # NY
]
```

---

## 🎨 STEG 5: FRONTEND METADATA

### I `apps/frontend/src/lib/skillsmaps.ts`

```typescript
const SKILLSMAP_METADATA: Record<string, SkillsMapMeta> = {
    // ... existing ...
    "{slug}-mastery": {
        icon: "🎯",
        color: "#HEX",
        tags: ["Tag1", "Tag2", "Tag3"]
    },
}
```

---

## 🚀 STEG 6: SEEDING (AUTOMATISK)

### Lokal utveckling

Moduler laddas automatiskt när backend startar via `modules_v3/__init__.py`.

### Production (Railway)

Använd seed-scriptet:

```bash
# Från apps/backend/
DATABASE_URL=postgresql://... python scripts/seed_tasks_to_prod.py
```

Eller via API:

```bash
curl -X POST https://api.devopshub.com/api/admin/dev/seed-v3
```

---

## 📊 STEG 7: UPPDATERA ROADMAP REGISTRY

### I `Endgame/MASTER_ROADMAP_REGISTRY.md`

Flytta från "⏳ NÄSTA" till "✅ KLARA":

```markdown
| # | SkillsMap | Noder | Fil | Status |
|---|-----------|-------|-----|--------|
| 19 | **{Title}** | 20 | `{slug}/` | ✅ LIVE |
```

---

## ✅ CHECKLISTA FÖRE PUSH

```markdown
## Pre-Push Checklist för {SkillsMap Name}

### Backend
- [ ] 20 nodes skapade
- [ ] Alla nodes har 5000+ tecken content
- [ ] Alla obligatoriska fält finns
- [ ] `order_index` 1-20 är unika
- [ ] `prerequisites` är korrekta
- [ ] Import i `modules_v3/__init__.py`
- [ ] Lagt till i `ALL_V3_MODULES`
- [ ] Python syntax validerad (`python -c "from src.db.seeds.modules_v3 import *"`)

### Frontend  
- [ ] Metadata i `skillsmaps.ts`
- [ ] Icon vald (emoji)
- [ ] Color vald (hex)
- [ ] Tags definierade

### Dokumentation
- [ ] MASTER_ROADMAP_REGISTRY.md uppdaterad
- [ ] EXPANSION_LOG.md uppdaterad
- [ ] command_center.md uppdaterad

### Verifiering
- [ ] `npm run build` lyckas
- [ ] Backend startar utan fel
- [ ] API returnerar modul via `/api/modules/slug/{slug}`
- [ ] Tasks returneras via `/api/tasks/module/slug/{slug}`
```

---

## 🔧 AUTOMATISK SEEDING VID PUSH

### GitHub Actions Workflow

Skapa `.github/workflows/seed-on-push.yml`:

```yaml
name: Auto-seed SkillsMaps

on:
  push:
    branches: [main]
    paths:
      - 'apps/backend/src/db/seeds/modules_v3/**'
      - 'apps/backend/src/db/seeds/skillsmaps/**'

jobs:
  seed:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: |
          cd apps/backend
          pip install -r requirements.txt
          
      - name: Run seed script
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
        run: |
          cd apps/backend
          python scripts/seed_tasks_to_prod.py
```

---

## 📋 EXEMPEL: SKAPA AI AGENTS SKILLSMAP

```bash
# 1. Skapa mapp
mkdir -p apps/backend/src/db/seeds/skillsmaps/ai_agents

# 2. Skapa filer
touch apps/backend/src/db/seeds/skillsmaps/ai_agents/__init__.py
touch apps/backend/src/db/seeds/skillsmaps/ai_agents/block_1_fundamentals.py
# ... etc

# 3. Skriv content (se mallar ovan)

# 4. Registrera i modules_v3/__init__.py
# from .ai_agents import MODULE_AI_AGENTS_MASTERY
# ALL_V3_MODULES.append(MODULE_AI_AGENTS_MASTERY)

# 5. Validera
cd apps/backend
python -c "from src.db.seeds.skillsmaps.ai_agents import ALL_NODES; print(f'{len(ALL_NODES)} nodes')"

# 6. Lägg till frontend metadata i skillsmaps.ts

# 7. Uppdatera docs

# 8. Commit & push
git add -A
git commit -m "feat(skillsmaps): Add AI Agents SkillsMap - 20 premium nodes"
git push origin main
```

---

## 🎯 NÄSTA SKILLSMAPS ATT BYGGA

| # | SkillsMap | Källa | Prio | Status |
|---|-----------|-------|------|--------|
| 19 | **AI Agents** | roadmap.sh/ai-agents | P1 🔥 | ⏳ NÄSTA |
| 20 | DSA | roadmap.sh/datastructures-and-algorithms | P1 | ⏳ |
| 21 | GraphQL | roadmap.sh/graphql | P1 | ⏳ |
| 22 | MongoDB | roadmap.sh/mongodb | P1 | ⏳ |
| 23 | Redis | roadmap.sh/redis | P1 | ⏳ |

---

*Denna manual är den ENDA källan till sanning för SkillsMaps-skapande.*
