# DevOpsHub - Fas-filer för Migration

Dessa filer löser identifierade problem och lägger till ny funktionalitet.

## 📁 Filstruktur

```
phase-files/
├── fas1/                          # Kritiska bugfixar
│   ├── LearningCodeBlock.tsx      # Fixar [object Object] bug
│   ├── ContentBlockRenderer.tsx   # Korrekt rendering av alla block-typer
│   ├── SessionHistory.tsx         # Balanserad Recent Sessions layout
│   ├── search.py                  # Backend search API
│   └── SearchBar.tsx              # Frontend search komponent
│
├── fas2/                          # Task Layout & Navigation
│   ├── ModuleLayout.tsx           # Sidebar med task-lista
│   └── TaskDetailPage.tsx         # Förbättrad task-vy
│
├── fas3/                          # Terminal Integration
│   └── TerminalEmulator.tsx       # Interaktiv terminal
│
├── fas4/                          # Database Persistence
│   ├── redis_client.py            # Redis caching
│   ├── database.py                # PostgreSQL config
│   └── main.py                    # Uppdaterad FastAPI app
│
└── fas5/                          # Advanced Content
    └── bootcamp_v4_content.py     # 60+ Senior DevOps moduler
```

---

## 🚀 Installation

### Fas 1: Kritiska Bugfixar

```bash
# Frontend komponenter
cp fas1/LearningCodeBlock.tsx apps/frontend/src/components/learning/
cp fas1/ContentBlockRenderer.tsx apps/frontend/src/components/learning/
cp fas1/SessionHistory.tsx apps/frontend/src/components/studyflow/
cp fas1/SearchBar.tsx apps/frontend/src/components/layout/

# Backend search
cp fas1/search.py apps/backend/src/api/routes/

# Registrera search router i main.py:
# from .api.routes.search import router as search_router
# app.include_router(search_router, prefix="/api", tags=["Search"])
```

### Fas 2: Task Layout

```bash
# Skapa layout-fil
mkdir -p apps/frontend/src/app/\(app\)/modules/\[id\]
cp fas2/ModuleLayout.tsx apps/frontend/src/app/\(app\)/modules/\[id\]/layout.tsx

# Skapa task page
mkdir -p apps/frontend/src/app/\(app\)/modules/\[id\]/tasks/\[taskId\]
cp fas2/TaskDetailPage.tsx apps/frontend/src/app/\(app\)/modules/\[id\]/tasks/\[taskId\]/page.tsx
```

### Fas 3: Terminal Integration

```bash
cp fas3/TerminalEmulator.tsx apps/frontend/src/components/content/
```

### Fas 4: Database Persistence

```bash
# Backend filer
cp fas4/redis_client.py apps/backend/src/db/
cp fas4/database.py apps/backend/src/db/
cp fas4/main.py apps/backend/src/

# Installera dependencies
cd apps/backend
pip install psycopg2-binary asyncpg redis
# eller lägg till i pyproject.toml:
# psycopg2-binary = "^2.9.9"
# asyncpg = "^0.29.0"  
# redis = "^5.0.0"
```

### Fas 5: Bootcamp v4.0 Content

```bash
cp fas5/bootcamp_v4_content.py apps/backend/src/db/seeds/

# Importera och kör seed i main.py eller separat script:
# from .db.seeds.bootcamp_v4_content import seed_v4_content
# seed_v4_content(db_session)
```

---

## ✅ Verifikation

Efter installation, verifiera:

```bash
# 1. Frontend bygger utan fel
cd apps/frontend && npm run build

# 2. Backend startar korrekt
cd apps/backend && python -m src.main

# 3. Search fungerar
curl http://localhost:8000/api/search?q=linux

# 4. Health check
curl http://localhost:8000/health
```

---

## 🔧 Railway Environment Variables

Säkerställ att dessa finns i Railway:

```env
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
FRONTEND_URL=https://saasprojekt.netlify.app
```

---

## 📝 Git Commits

Föreslagna commits:

```bash
git add apps/frontend/src/components/learning/
git commit -m "fix(content): resolve [object Object] rendering in code blocks"

git add apps/frontend/src/components/layout/SearchBar.tsx apps/backend/src/api/routes/search.py
git commit -m "feat(search): implement functional search across modules and tasks"

git add apps/frontend/src/app/\(app\)/modules/
git commit -m "feat(layout): add sidebar navigation for task pages"

git add apps/backend/src/db/redis_client.py apps/backend/src/db/database.py
git commit -m "feat(db): add PostgreSQL and Redis persistence"

git add apps/backend/src/db/seeds/bootcamp_v4_content.py
git commit -m "feat(content): add Bootcamp v4.0 Senior DevOps curriculum"
```

---

## 🎯 Nästa Steg

1. **Verifiera bugfixar** - Kör frontend lokalt och testa
2. **Testa search** - Sök efter moduler och tasks
3. **Konfigurera Railway** - Lägg till DATABASE_URL och REDIS_URL
4. **Seed v4.0 content** - Kör seed-scriptet
5. **Deploy** - Push till main för automatisk deploy
