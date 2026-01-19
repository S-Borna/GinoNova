# GinoNova - Komplett Projektöversikt

> **Senast uppdaterad:** 2026-01-19
> **Version:** v2.6.0
> **Status:** Production
> **URL:** <https://ginonova.com> | <https://api.ginonova.com>

---

## 📋 Innehållsförteckning

1. [Vad är detta?](#vad-är-detta)
2. [Tech Stack](#tech-stack)
3. [Projektstruktur](#projektstruktur)
4. [Alla Features](#alla-features)
5. [Admin Dashboard](#admin-dashboard)
6. [Quiz & Tenta System](#quiz--tenta-system)
7. [Content Management](#content-management)
8. [Databas & Modeller](#databas--modeller)
9. [API Endpoints](#api-endpoints)
10. [Deployment](#deployment)
11. [Vanliga Uppgifter](#vanliga-uppgifter)

---

## 🎯 Vad är detta?

**GinoNova** är en interaktiv e-learningplattform för DevOps, Linux och systemadministration.

### Huvudfunktioner

- **Camp DevOps** - Strukturerade utbildningsmoduler med uppgifter och labs
- **Tenta Simulator** - Realistisk tentaövning med 770+ frågor från DOE25, Omtenta 2.0, Manpage-tenta
- **AI Quiz** - Dynamiskt genererade frågor via OpenAI baserat på modulinnehåll
- **Flashcards** - Interaktiva flashcards för alla moduler
- **Dallas AI** - AI-assistent som svarar på DevOps-frågor
- **SkillsMaps** - Visuella kunskapskartor med lärandevägar
- **FastTrack** - Snabbkurser för specifika verktyg (Docker, Git, etc.)
- **Admin Dashboard** - Realtidsövervakning av användare, broadcast, analytics

### Layout & Design (v2.6.0)

- **TopBar** - Fixed full-width header med GinoNova logo, "Skapad med ❤️" quote, Spotify widget, session timer
- **Sidebar** - Börjar under TopBar vid NAVIGATION-nivå (logo flyttad till TopBar)
- **Logo** - Stor glödande logo (80px) med animerade drop-shadow effekter
- **Spotify Widget** - Centrerad i TopBar med Play-knapp, visar nu spelande låt via Last.fm

---

## 🛠 Tech Stack

### Frontend

```
Framework:     Next.js 16.1.0 (App Router)
Language:      TypeScript
Styling:       Tailwind CSS 4.x
UI:            Radix UI + Lucide Icons
Animations:    Framer Motion
State:         React Context + localStorage
Auth:          NextAuth v4 (Google, GitHub, Discord)
```

### Backend

```
Framework:     FastAPI 0.111
Language:      Python 3.11
Database:      PostgreSQL (SQLAlchemy 2.0)
Migrations:    Alembic
Auth:          JWT (python-jose + bcrypt)
AI:            OpenAI API (GPT-4o-mini)
Workers:       4 Uvicorn workers på Railway
```

### Infrastructure

```
Frontend:      Netlify
Backend:       Railway.app (4 workers)
Database:      PostgreSQL (Railway)
Domain:        ginonova.com / api.ginonova.com
```

---

## 📁 Projektstruktur

```
saas-project/
├── apps/
│   ├── backend/               # FastAPI backend
│   │   ├── src/
│   │   │   ├── api/
│   │   │   │   ├── auth.py           # Auth endpoints (login, register, OAuth)
│   │   │   │   ├── routes/
│   │   │   │   │   ├── admin_v2.py   # 🔥 Admin dashboard (80KB - huvudfil)
│   │   │   │   │   ├── quiz.py       # AI Quiz generation
│   │   │   │   │   ├── study.py      # Study endpoints
│   │   │   │   │   ├── dallas.py     # Dallas AI assistant
│   │   │   │   │   ├── exam_results.py
│   │   │   │   │   └── ...
│   │   │   ├── db/
│   │   │   │   ├── models.py         # SQLAlchemy models
│   │   │   │   ├── database.py       # DB connection
│   │   │   │   └── seeds/            # Content seeding
│   │   │   └── services/
│   │   │       └── quiz_service.py   # AI quiz generation logic
│   │   └── alembic/versions/         # DB migrations (001-011)
│   │
│   ├── frontend/              # Next.js frontend
│   │   ├── src/
│   │   │   ├── app/
│   │   │   │   ├── (app)/            # Authenticated pages
│   │   │   │   │   ├── admin/        # Admin pages
│   │   │   │   │   ├── study/        # Study pages
│   │   │   │   │   ├── dashboard/
│   │   │   │   │   └── ...
│   │   │   │   └── (auth)/           # Login/Register
│   │   │   ├── components/
│   │   │   │   ├── admin/            # Admin components
│   │   │   │   ├── study/            # Study components
│   │   │   │   ├── broadcast/        # Broadcast system
│   │   │   │   ├── ai/               # Dallas AI
│   │   │   │   └── ...
│   │   │   ├── data/                 # 84 datafiler med quiz/flashcards
│   │   │   │   ├── doe25-*.ts        # DOE25 material
│   │   │   │   ├── exam-nod*.ts      # Omtenta 2.0 (10 noder)
│   │   │   │   ├── manpage-*.ts      # Manpage-tenta
│   │   │   │   ├── linux-commands-*.ts
│   │   │   │   └── handson-*.ts
│   │   │   ├── hooks/
│   │   │   │   └── useActivityTracker.tsx  # Real-time tracking
│   │   │   └── lib/
│   │   │       └── auth.ts           # Auth utilities
│   │
│   └── workers/               # Background workers (om används)
│
├── content-source/            # Markdown-innehåll för moduler
│   └── modules/
│       ├── Docker/
│       ├── Linux/
│       └── linux-tentaplugg/
│
└── docs/                      # Dokumentation
```

---

## 🚀 Alla Features

### Användarfunktioner

| Feature | Beskrivning | Sida |
|---------|-------------|------|
| **Dashboard** | Översikt med streak, XP, progress | `/dashboard` |
| **Camp DevOps** | Strukturerade moduler | `/learn` |
| **Study Room** | Quiz + Flashcards per modul | `/study` |
| **Tenta Simulator** | 770+ frågor, tidsbegränsad tenta | `/study/tenta-simulator` |
| **AI Quiz** | AI-genererade frågor från OpenAI | `/quiz` |
| **Omtenta 2.0** | 10 noder med flashcards | `/study/omtenta-v2` |
| **FastTrack** | Snabbkurser för verktyg | `/fasttrack` |
| **SkillsMaps** | Visuella kunskapskartor | `/skillsmaps` |
| **Tutorials** | Guider och howtos | `/tutorials` |
| **Community** | Forum/diskussioner | `/community` |
| **Certificates** | Kurscertifikat | `/certificates` |
| **Profile** | Användarinställningar | `/profile` |
| **Dallas AI** | AI-assistent (floating widget) | Alla sidor |

### Admin Features (endast för admin)

| Feature | Beskrivning | Sida |
|---------|-------------|------|
| **Dashboard** | Stats, senaste aktivitet | `/admin` |
| **User Management** | Lista, redigera, banna användare | `/admin/users` |
| **Live Activity** | Realtidsövervakning av användare | `/admin/users/live` |
| **Broadcast** | Skicka meddelanden till alla | `/admin/broadcast` |
| **Analytics** | Grafer, heatmaps, tillväxt | `/admin/analytics` |
| **AI Usage** | OpenAI-kostnader per användare | `/admin/ai-usage` |
| **Exam Stats** | Tentaresultat och statistik | `/admin/exam-stats` |
| **Inbox** | Meddelanden från användare | Widget i TopBar |

---

## 👑 Admin Dashboard

### Realtidsfunktioner (polling var 3-5 sek)

1. **Activity Flash** - Toast-notifikationer för login/logout/exam/quiz
2. **Live Activity Monitor** - Se var varje användare är just nu
3. **Admin Online Status** - Visa om admin är online (grön prick)
4. **Broadcast System** - Skicka meddelanden som visas för alla
5. **User Messages** - Ta emot meddelanden från användare

### Endpoints i `admin_v2.py`

```
GET  /api/admin/v2/stats/overview          - Dashboard stats
GET  /api/admin/v2/users                   - Lista användare
GET  /api/admin/v2/users/live-activity     - Realtidsaktivitet
POST /api/admin/v2/broadcast               - Skicka broadcast
GET  /api/admin/v2/activity-flash          - Hämta nya events
POST /api/admin/v2/users/activity          - Spåra användaraktivitet
GET  /api/admin/v2/contact/messages        - User→Admin meddelanden
POST /api/admin/v2/status/heartbeat        - Admin heartbeat
```

### Datalagring

| Data | Lagring | Anledning |
|------|---------|-----------|
| Activity Log | PostgreSQL | Multi-worker support |
| Broadcast Messages | In-memory | Temporära meddelanden |
| User Messages | In-memory | Max 50, rensas vid restart |
| Live Activity | In-memory | Realtid per worker |

---

## 📝 Quiz & Tenta System

### Frågebanker (84 datafiler)

| Källa | Antal frågor | Typ | Fil |
|-------|--------------|-----|-----|
| DOE25 | ~200 | MCQ + Open | `doe25-*.ts` |
| Omtenta 2.0 | ~300 | MCQ + VG | `exam-nod*.ts` |
| Manpage-tenta | ~100 | MCQ | `manpage-tenta-quiz.ts` |
| Linux Commands | ~100 | MCQ | `linux-commands-*.ts` |
| Hands-on Labs | ~70 | MCQ | `handson-*.ts` |
| **Totalt** | **~770** | | |

### Tenta Simulator (`/study/tenta-simulator`)

- Välj källor: DOE25, Omtenta, Manpage, Linux Commands, Hands-on
- Välj antal frågor och tidsgräns
- G/VG-nivå per fråga
- Resultat sparas i `exam_results` tabell
- Admin ser alla resultat i `/admin/exam-stats`

### AI Quiz (`/quiz`)

- Genererar NYA frågor via OpenAI GPT-4o-mini
- Baserat på modulinnehåll/stilar
- Välj modul, typ (MCQ/TF/Open), antal, svårighetsgrad
- Loggas i `ai_usage_logs` tabell
- Cost tracking i admin dashboard

---

## 📚 Content Management

### Hur lägga till nytt innehåll

#### 1. Quiz-frågor (statiska)

Skapa fil i `apps/frontend/src/data/`:

```typescript
// my-new-quiz.ts
export interface QuizQuestion {
  id: string
  question: string
  options: string[]
  correctAnswer: number
  explanation?: string
  difficulty: 'G' | 'VG'
}

export const MY_NEW_QUIZ: QuizQuestion[] = [
  {
    id: 'q1',
    question: 'Vad gör kommandot ls?',
    options: ['Listar filer', 'Tar bort filer', 'Skapar filer', 'Kopierar filer'],
    correctAnswer: 0,
    explanation: 'ls listar innehållet i en katalog',
    difficulty: 'G'
  }
]
```

#### 2. Flashcards

```typescript
// my-flashcards.ts
export interface Flashcard {
  id: string
  front: string
  back: string
  category?: string
}

export const MY_FLASHCARDS: Flashcard[] = [
  {
    id: 'f1',
    front: 'Vad är en process?',
    back: 'Ett körande program i minnet',
    category: 'Linux Basics'
  }
]
```

#### 3. Camp DevOps-moduler

Markdown-filer i `content-source/modules/`:

```markdown
---
title: Min Nya Modul
slug: min-nya-modul
description: Beskrivning
order: 5
---

# Innehåll här
```

Seeda sedan till databasen med `apps/backend/src/db/seeds/`.

### Importera i Tenta Simulator

Uppdatera `apps/frontend/src/app/(app)/study/tenta-simulator/page.tsx`:

```typescript
import { MY_NEW_QUIZ } from '@/data/my-new-quiz'

// Lägg till i questionSources
const sources = {
  // ...existing
  'my-new': MY_NEW_QUIZ
}
```

---

## 🗄 Databas & Modeller

### Tabeller (13 st)

| Tabell | Beskrivning |
|--------|-------------|
| `users` | Användardata, auth, permissions |
| `tracks` | Utbildningsspår (DevOps, Linux) |
| `modules` | Moduler inom spår |
| `tasks` | Uppgifter inom moduler |
| `labs` | Hands-on labs |
| `projects` | Capstone-projekt |
| `progress` | Användarens framsteg |
| `studyflow_sessions` | Studiesessioner |
| `task_block_progress` | Detaljerad progress |
| `bookmarks` | Sparade moduler |
| `ai_usage_logs` | OpenAI API-anrop |
| `exam_results` | Tentaresultat |
| `activity_logs` | Admin activity flash (NY) |

### Migrations

```bash
cd apps/backend
alembic upgrade head          # Kör alla migrations
alembic revision -m "name"    # Skapa ny migration
```

---

## 🔌 API Endpoints

### Auth (`/api/auth/`)

```
POST /register     - Registrera ny användare
POST /login        - Logga in (email/password)
POST /logout       - Logga ut (loggar aktivitet)
GET  /me           - Hämta nuvarande användare
POST /oauth        - OAuth login (Google/GitHub/Discord)
```

### Study (`/api/study/`)

```
GET  /modules              - Lista moduler
GET  /modules/{slug}       - Hämta modul
GET  /progress             - Användarens progress
POST /progress             - Uppdatera progress
```

### Quiz (`/api/quiz/`)

```
POST /generate             - Generera AI Quiz
GET  /modules              - Tillgängliga quiz-moduler
```

### Admin (`/api/admin/v2/`)

Se [Admin Dashboard](#admin-dashboard) ovan.

---

## 🚀 Deployment

### Frontend (Netlify)

Automatisk deploy vid push till `main`:

```bash
git push origin main        # Triggar Netlify build
```

Build command: `npm run build`
Publish directory: `.next`

### Backend (Railway)

Automatisk deploy vid push:

```bash
git push origin main        # Triggar Railway build
```

**Efter schema-ändringar:**

```bash
# SSH till Railway eller kör lokalt mot prod-DB
alembic upgrade head
```

### Manuell deploy

```bash
# Build frontend
npm run --prefix apps/frontend build

# Test backend
cd apps/backend
python -m pytest

# Push
git add -A
git commit -m "description"
git push
```

---

## 🔧 Vanliga Uppgifter

### Starta lokalt

```bash
# Backend (port 8000)
cd apps/backend
python3 -m uvicorn src.main:app --reload --port 8000

# Frontend (port 3000)
cd apps/frontend
npm run dev
```

### Lägg till ny quiz-källa

1. Skapa datafil i `apps/frontend/src/data/`
2. Importera i Tenta Simulator page
3. Lägg till i `questionSources` objekt
4. Commita och pusha

### Lägg till ny admin-endpoint

1. Editera `apps/backend/src/api/routes/admin_v2.py`
2. Lägg till `@router.get/post/etc` decorator
3. Implementera funktion
4. Testa lokalt
5. Pusha (auto-deploy)

### Fixa database-problem

```bash
# Reset migration
alembic downgrade -1
alembic upgrade head

# Skapa ny migration efter model-ändringar
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Debug production

```bash
# Kolla Railway logs
railway logs

# Testa endpoint
curl https://api.ginonova.com/api/auth/status
```

---

## 📊 Statistik

- **Frontend pages:** 40+
- **Backend routes:** 80+
- **Quiz frågor:** 770+
- **Datafiler:** 84
- **DB tabeller:** 13
- **Migrations:** 11
- **Total kodrader:** ~50,000+

---

## 🔑 Viktiga Filer

| Fil | Syfte |
|-----|-------|
| `apps/backend/src/api/routes/admin_v2.py` | Hela admin-systemet (80KB) |
| `apps/backend/src/api/auth.py` | Autentisering |
| `apps/backend/src/db/models.py` | Alla DB-modeller |
| `apps/frontend/src/components/layout/TopBar.tsx` | Fixed TopBar med logo, Spotify, quote |
| `apps/frontend/src/components/layout/Sidebar.tsx` | Sidebar (börjar under TopBar) |
| `apps/frontend/src/components/spotify/SpotifyTopBarWidget.tsx` | Spotify widget med Play-knapp |
| `apps/frontend/src/components/auth/AuthProvider.tsx` | Auth context |
| `apps/frontend/src/hooks/useActivityTracker.tsx` | Realtidsspårning |
| `apps/frontend/src/components/broadcast/UserBroadcast.tsx` | Broadcast UI |
| `apps/frontend/src/app/(app)/study/tenta-simulator/page.tsx` | Tenta |

---

## 👤 Admin-konto

Email: `said.ebadi@hotmail.com` (hårdkodad som admin i flera ställen)

---

*Dokumentation uppdaterad 2026-01-19*
