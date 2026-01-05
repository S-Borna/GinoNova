# DevOpsHub - Komplett Projektöversikt

> **Senast uppdaterad:** 2026-01-05
> **Version:** v1.0.0
> **Status:** Production (med teknisk skuld)

---

## 📋 Innehållsförteckning

1. [Vad är detta?](#vad-är-detta)
2. [Tech Stack](#tech-stack)
3. [Projektstruktur](#projektstruktur)
4. [Arkitektur](#arkitektur)
5. [Funktioner & Features](#funktioner--features)
6. [Kom igång (Setup)](#kom-igång-setup)
7. [Databas & Modeller](#databas--modeller)
8. [API-dokumentation](#api-dokumentation)
9. [Aktuella Problem](#aktuella-problem)
10. [Rekommendationer för Städning](#rekommendationer-för-städning)
11. [Förbättringsförslag](#förbättringsförslag)

---

## 🎯 Vad är detta?

**DevOpsHub** är en interaktiv e-learningplattform fokuserad på DevOps, Linux och systemadministration.

### Huvudsyfte
- Strukturerad utbildning genom moduler, uppgifter och labb
- Interaktiva studieverktyg (flashcards, quiz, tentasimulator)
- AI-driven inlärningsassistent ("Dallas")
- Spårning av framsteg och gamification
- Visualisering av färdighetsvägar (skillsmaps)
- Community och sociala funktioner

### Target Audience
- DevOps-studenter och nybörjare
- Systemadministratörer som vill lära sig mer
- Personer som förbereder sig för DevOps-certifieringar
- Team som vill standardisera DevOps-kunskaper

---

## 🛠 Tech Stack

### Frontend
```
Framework:     Next.js 16.1.0 (App Router, React 18)
Language:      TypeScript (strict mode)
Styling:       Tailwind CSS 4.1.17
UI Library:    Radix UI (accessibility)
Icons:         Lucide React
Animations:    Framer Motion
State:         TanStack Query v5 + React Context
Auth:          NextAuth v4 (Google, GitHub, Discord OAuth)
```

**Specialfunktioner:**
- `xterm.js` - Terminal emulator för labs
- `react-markdown` - Content rendering
- `canvas-confetti` - Gamification effekter
- `highlight.js` - Syntax highlighting

### Backend
```
Framework:     FastAPI 0.111.0
Language:      Python 3.11
Database:      PostgreSQL (SQLAlchemy 2.0.44)
ORM:           SQLAlchemy + Alembic migrations
Async:         asyncpg
Cache:         Redis 5.0.0
Auth:          JWT (python-jose + bcrypt)
AI:            OpenAI API 1.0.0+
Payment:       Stripe 7.0.0+
Dep Mgmt:      Poetry
```

### Infrastructure & Deployment
```
Frontend:      Netlify (med Next.js plugin)
Backend:       Railway.app (Docker)
Database:      PostgreSQL (Railway managed)
Cache:         Redis (Railway managed)
CI/CD:         Docker-based builds
Monitoring:    Health check endpoints
```

### Utvecklingsverktyg
```
Monorepo:      Turborepo
Versionskontroll: Git + GitHub
Linting:       ESLint, Prettier
Pre-commit:    Hooks för validering
Testing:       Jest (minimal coverage)
```

---

## 📁 Projektstruktur

```
saas-project/
├── apps/
│   ├── backend/              # Python FastAPI server
│   │   ├── src/
│   │   │   ├── api/          # API routes (30+ moduler)
│   │   │   ├── core/         # Configuration, JWT, deps
│   │   │   ├── db/           # Models, repositories, seeds
│   │   │   ├── schemas/      # Pydantic models (23+ filer)
│   │   │   ├── services/     # Business logic
│   │   │   └── main.py       # App entry point
│   │   ├── alembic/          # Database migrations
│   │   ├── tests/            # Backend tests (minimal)
│   │   ├── pyproject.toml    # Poetry dependencies
│   │   └── Dockerfile        # Production container
│   │
│   ├── frontend/             # Next.js React app
│   │   ├── src/
│   │   │   ├── app/          # Next.js App Router
│   │   │   │   ├── (app)/    # Protected routes
│   │   │   │   ├── (auth)/   # Auth pages
│   │   │   │   └── api/      # Next.js API routes
│   │   │   ├── components/   # React components (27 UI + features)
│   │   │   ├── lib/          # Utilities, API client
│   │   │   ├── hooks/        # Custom hooks
│   │   │   ├── contexts/     # React contexts
│   │   │   ├── providers/    # Providers
│   │   │   └── types/        # TypeScript types
│   │   ├── public/           # Static assets
│   │   ├── next.config.js    # Next.js config
│   │   ├── tailwind.config.js
│   │   └── package.json
│   │
│   └── workers/              # Background jobs (minimal setup)
│
├── packages/
│   ├── shared/
│   │   ├── python/           # Shared Python utilities
│   │   └── ts/               # Shared TypeScript types
│   └── ui/                   # Design system components
│
├── content/                  # Content management (not in use)
├── docs/                     # Documentation (extensive phase docs)
├── infra/                    # Infrastructure as code
├── phases/                   # Development phase tracking
│
├── turbo.json                # Turborepo config
├── package.json              # Root workspace config
└── tsconfig.json             # Root TypeScript config
```

### Viktiga Kataloger att Förstå

#### `/apps/backend/src/api/routes/`
Här finns alla API endpoints:
- `auth.py` - Autentisering (login, register, OAuth)
- `modules.py` - Learning modules
- `tasks.py` - Tasks/lessons
- `progress.py` - Progress tracking
- `studyflow.py` - Study sessions
- `ai.py` - AI services
- `admin.py` - Admin functions
- `study.py` - Flashcards/quizzes
- `dallas.py` - AI assistant
- Plus 20+ andra specialiserade routes

#### `/apps/frontend/src/app/(app)/`
Huvudapplikationens skyddade routes:
- `dashboard/` - User dashboard
- `modules/` - Learning modules
- `study/` - Study tools (flashcards, quiz, tenta)
- `studyflow/` - Study sessions
- `admin/` - Admin panel
- `skillpath/` - Skill visualization
- `community/` - Community features
- `profile/` - User profiles

#### `/apps/backend/src/db/`
Databaslag:
- `models.py` - SQLAlchemy models (alla tabeller)
- `*_repository.py` - Data access layer (repository pattern)
- `seeds/` - Seed data för modules, tasks, content

---

## 🏗 Arkitektur

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Next.js)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  App Router  │  │  Components  │  │   Contexts   │  │
│  │  (Pages)     │  │  (UI Logic)  │  │  (State)     │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                  │                  │          │
│         └──────────────────┴──────────────────┘          │
│                            │                             │
└────────────────────────────┼─────────────────────────────┘
                             │ HTTP/REST API
                             │
┌────────────────────────────┼─────────────────────────────┐
│                            ▼                             │
│                   BACKEND (FastAPI)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ API Routes   │→ │  Services    │→ │ Repositories │  │
│  │ (Endpoints)  │  │ (Logic)      │  │ (Data)       │  │
│  └──────────────┘  └──────────────┘  └──────┬───────┘  │
│                                              │          │
└──────────────────────────────────────────────┼──────────┘
                                               │
                     ┌─────────────────────────┼──────────┐
                     │                         ▼          │
                     │  ┌──────────────────────────────┐  │
                     │  │   PostgreSQL Database        │  │
                     │  │   (Source of Truth)          │  │
                     │  └──────────────────────────────┘  │
                     │                                    │
                     │  ┌──────────────────────────────┐  │
                     │  │   Redis Cache                │  │
                     │  │   (Sessions, Rate Limiting)  │  │
                     │  └──────────────────────────────┘  │
                     │                                    │
                     │         DATA LAYER                 │
                     └────────────────────────────────────┘

External Services:
- OpenAI API (AI features)
- Stripe API (payments)
- NextAuth Providers (Google, GitHub, Discord)
```

### Design Patterns

**Backend:**
- **Repository Pattern** - Data access abstraction
- **Service Layer** - Business logic separation
- **Dependency Injection** - FastAPI dependencies
- **Schema Validation** - Pydantic models

**Frontend:**
- **Component Composition** - Reusable UI components
- **Custom Hooks** - Shared logic extraction
- **Context API** - Global state management
- **Server State** - TanStack Query for API data

### Data Flow Example: User Submits Task

```
1. User clicks "Mark Complete" i frontend
   ↓
2. Frontend component anropar useMutation hook
   ↓
3. TanStack Query gör POST till /api/progress
   ↓
4. Backend route /progress.py tar emot request
   ↓
5. progress_service.py uppdaterar business logic
   ↓
6. progress_repository.py sparar till PostgreSQL
   ↓
7. Response returneras med uppdaterad progress
   ↓
8. TanStack Query invaliderar cache
   ↓
9. UI uppdateras automatiskt med ny data
```

---

## ⚡ Funktioner & Features

### 🎓 Core Learning Features

#### 1. Module System
- **15 moduler** över 4 tracks (Bootcamp v3.0)
- Progressiv svårighetsgrad (Basics → Advanced)
- Prerequisites tracking
- Estimerad completion time
- **Tracks:**
  - Track 1: Linux & Terminal Basics
  - Track 2: DevOps Fundamentals
  - Track 3: Deployment & Cloud
  - Track 4: Advanced DevOps

#### 2. Interactive Content (ILE - Interactive Learning Engine)
- **Tasks** med rich content blocks:
  - Markdown text
  - Code snippets med syntax highlighting
  - Embedded terminals (xterm.js)
  - Videos och bilder
  - Quizzes inline
- **Labs** - Hands-on övningar
- **Projects** - Module-level projekt
- Content blocks system för flexibel content

#### 3. Study Tools

**Flashcards:**
- Genererade från module content
- Spaced repetition (implicit)
- Progress tracking per deck
- Kategoriserade efter module

**Quiz System:**
- Multiple choice questions
- AI-genererade frågor
- Instant feedback
- Score tracking

**Exam Simulator (Tenta Simulator):**
- Simulerar riktiga tentor
- Tidsbegränsade sessioner
- Randomiserade frågor
- Detaljerad feedback
- Review mode efter completion

**Study Sessions (Studyflow):**
- Fokuserade learning sessions
- Timer och break reminders
- Session statistics
- Progress visualization

#### 4. AI Features ("Dallas")

- **AI Chat Assistant:**
  - Kontextmedveten hjälp
  - Förklaringar av koncept
  - Code review
  - Debugging hjälp

- **Content Analysis:**
  - Difficulty analysis
  - Study recommendations
  - Next step suggestions
  - Summary generation

- **Usage Tracking:**
  - AI usage logs
  - Cost tracking
  - Rate limiting

#### 5. Gamification System

**XP & Levels:**
- XP för completed tasks
- Level progression system
- XP multipliers för streaks

**Streaks:**
- Daily login streaks
- Study session streaks
- Streak freeze (premium feature)

**Badges & Certificates:**
- Achievement badges
- Module completion certificates
- Skill-based badges

**Progress Visualization:**
- Skillpath board
- Module completion charts
- Activity heatmaps

#### 6. Social Features

- **Community Section:**
  - User discussions
  - Question/answer forum
  - Resource sharing

- **User Profiles:**
  - Public achievements
  - Activity feed
  - Skill visualization

- **Notifications:**
  - Achievement notifications
  - Streak reminders
  - Community updates

#### 7. Admin Features

**User Management:**
- User list med filters
- Permission control per user
- Force logout users
- Ban/unban users
- Toggle admin status
- Delete users

**Analytics Dashboard:**
- User statistics
- Module completion rates
- AI usage metrics
- Revenue tracking (Stripe)

**Content Management:**
- Module editing
- Task management
- Content seeding

**System Control:**
- Lockdown mode (restrict to allowed emails)
- Feature flags
- System health monitoring

### 🔐 Authentication & Security

**Authentication Methods:**
1. **Traditional:** Email/password med bcrypt hashing
2. **OAuth:** Google, GitHub, Discord

**Security Features:**
- JWT token-based auth
- Session management
- Password strength requirements
- Lockdown mode för restricted access
- Rate limiting (TODO: ej implementerad)
- CORS protection

**User Permissions:**
Granular feature flags:
- `ai_quiz_access` - AI quiz features
- `premium_modules_access` - Premium content
- `study_room_access` - Study room features
- `skillpath_access` - Skillpath visualization

---

## 🚀 Kom igång (Setup)

### Prerequisites

```bash
# Required
- Node.js 18+ och npm/pnpm
- Python 3.11+
- PostgreSQL 14+
- Redis 7+ (optional för local dev)

# Rekommenderat
- Docker & Docker Compose
- Git
- VS Code med TypeScript/Python extensions
```

### 1. Clone Repository

```bash
git clone <repo-url>
cd saas-project
```

### 2. Install Dependencies

**Root & Frontend:**
```bash
# Installera alla workspace dependencies
npm install
# eller
pnpm install
```

**Backend:**
```bash
cd apps/backend

# Med Poetry (rekommenderat)
poetry install

# Eller med pip
pip install -r requirements.txt
```

### 3. Environment Variables

**Backend** (`apps/backend/.env`):
```env
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/devopshub

# Redis (optional för local dev)
REDIS_URL=redis://localhost:6379

# Security
JWT_SECRET=din-jwt-secret-här-minst-32-tecken
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API
API_ORIGINS=http://localhost:3000,http://localhost:3001

# OpenAI (för AI features)
OPENAI_API_KEY=sk-...

# Stripe (för payments)
STRIPE_API_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Lockdown (optional)
LOCKDOWN_MODE=false
ALLOWED_EMAILS=email@example.com,email2@example.com

# Environment
RAILWAY_ENV=development
```

**Frontend** (`apps/frontend/.env.local`):
```env
# Backend API
NEXT_PUBLIC_API_URL=http://localhost:8000

# NextAuth
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=din-nextauth-secret-minst-32-tecken

# OAuth Providers
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret

DISCORD_CLIENT_ID=your-discord-client-id
DISCORD_CLIENT_SECRET=your-discord-client-secret
```

### 4. Setup Database

```bash
cd apps/backend

# Kör migrations
poetry run alembic upgrade head

# Seed initial data (moduler, tasks, etc.)
poetry run python -m src.db.seeds.seed_all
```

### 5. Start Development Servers

**Option 1: Turborepo (båda samtidigt)**
```bash
# Från root
npm run dev
```

**Option 2: Separat (för debugging)**

Terminal 1 - Backend:
```bash
cd apps/backend
poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Terminal 2 - Frontend:
```bash
cd apps/frontend
npm run dev
```

### 6. Access Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs (FastAPI auto-docs)

### 7. Create Admin User

```bash
cd apps/backend

# Använd Python REPL eller skapa script
poetry run python

>>> from src.db.database import get_db_sync
>>> from src.db.models import User
>>> from passlib.context import CryptContext
>>>
>>> pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
>>> db = next(get_db_sync())
>>>
>>> admin = User(
...     email="admin@example.com",
...     username="admin",
...     hashed_password=pwd_context.hash("secure_password"),
...     is_admin=True,
...     email_verified=True
... )
>>> db.add(admin)
>>> db.commit()
```

---

## 🗄 Databas & Modeller

### Database Schema

**Core Tables:**

#### `users` - User Accounts
```python
id: UUID (PK)
email: String (unique)
username: String (unique, optional)
hashed_password: String (optional för OAuth)
is_admin: Boolean
email_verified: Boolean
oauth_provider: String (google/github/discord)
oauth_id: String
avatar_url: String
created_at: DateTime
last_activity_at: DateTime

# Permissions
ai_quiz_access: Boolean
premium_modules_access: Boolean
study_room_access: Boolean
skillpath_access: Boolean

# Gamification
xp: Integer
level: Integer
current_streak: Integer
longest_streak: Integer
```

#### `tracks` - Learning Tracks
```python
id: UUID (PK)
title: String
description: Text
order_index: Integer
created_at: DateTime
```

#### `modules` - Learning Modules
```python
id: UUID (PK)
track_id: UUID (FK → tracks)
title: String
slug: String (unique)
description: Text
difficulty: String (beginner/intermediate/advanced)
order_index: Integer
estimated_hours: Float
is_premium: Boolean
prerequisites: JSON (list of module IDs)
```

#### `tasks` - Individual Lessons
```python
id: UUID (PK)
module_id: UUID (FK → modules)
title: String
slug: String
description: Text
content_blocks: JSON (ILE content)
difficulty: String
order_index: Integer
estimated_minutes: Integer
xp_reward: Integer
tier: Integer (1-3, för hierarki)
parent_task_id: UUID (FK → tasks, för nesting)
```

#### `labs` - Hands-on Labs
```python
id: UUID (PK)
module_id: UUID (FK → modules)
title: String
description: Text
setup_instructions: Text
tasks: JSON
verification_script: Text
difficulty: String
estimated_minutes: Integer
```

#### `projects` - Module Projects
```python
id: UUID (PK)
module_id: UUID (FK → modules)
title: String
description: Text
requirements: JSON
resources: JSON
difficulty: String
estimated_hours: Float
```

#### `progress` - User Progress Tracking
```python
id: UUID (PK)
user_id: UUID (FK → users)
task_id: UUID (FK → tasks)
module_id: UUID (FK → modules)
status: String (not_started/in_progress/completed)
completed_at: DateTime
time_spent_minutes: Integer
```

#### `studyflow_sessions` - Study Sessions
```python
id: UUID (PK)
user_id: UUID (FK → users)
task_id: UUID (FK → tasks, optional)
started_at: DateTime
ended_at: DateTime
duration_minutes: Integer
focus_score: Float
notes: Text
```

#### `bookmarks` - User Bookmarks
```python
id: UUID (PK)
user_id: UUID (FK → users)
task_id: UUID (FK → tasks)
notes: Text
created_at: DateTime
```

#### `ai_usage_logs` - AI Usage Tracking
```python
id: UUID (PK)
user_id: UUID (FK → users)
feature: String (dallas/quiz/summary/etc)
prompt_tokens: Integer
completion_tokens: Integer
total_cost: Float
created_at: DateTime
```

**Additional Tables:**
- `flashcard_decks` - Flashcard collections
- `flashcards` - Individual flashcards
- `flashcard_progress` - User flashcard progress
- `quiz_attempts` - Quiz attempt history
- `badges` - Achievement badges
- `user_badges` - User badge associations
- `certificates` - Module certificates
- `notifications` - User notifications
- `study_notes` - User study notes

### Migrations

Location: `/apps/backend/alembic/versions/`

**Migration History:**
1. `001_initial_tables.py` - Core tables
2. `002_add_task_tier_parent.py` - Task hierarchy
3. `003_add_bookmarks.py` - Bookmark system
4. `004_add_oauth_fields.py` - OAuth support
5. `005_add_user_permissions.py` - Permission system
6. `006_add_ai_usage_logs.py` - AI tracking

**Running Migrations:**
```bash
# Upgrade to latest
alembic upgrade head

# Downgrade one version
alembic downgrade -1

# Create new migration
alembic revision --autogenerate -m "description"
```

---

## 📡 API-dokumentation

### Base URL
```
Development: http://localhost:8000
Production:  https://api.ginonova.com (eller Railway URL)
```

### Authentication

**All authenticated requests:**
```http
Authorization: Bearer <jwt_token>
```

### Main API Routes

#### Authentication
```
POST   /api/auth/register          - Register new user
POST   /api/auth/login             - Login (email/password)
POST   /api/auth/oauth/google      - Google OAuth
POST   /api/auth/oauth/github      - GitHub OAuth
POST   /api/auth/oauth/discord     - Discord OAuth
GET    /api/auth/me                - Get current user
PUT    /api/auth/me                - Update current user
POST   /api/auth/logout            - Logout
```

#### Modules & Content
```
GET    /api/tracks                 - List all tracks
GET    /api/tracks/{id}            - Get track details

GET    /api/modules                - List all modules
GET    /api/modules/{id}           - Get module details
GET    /api/modules/{id}/tasks     - Get module tasks
GET    /api/modules/{id}/labs      - Get module labs
GET    /api/modules/{id}/project   - Get module project

GET    /api/tasks/{id}             - Get task details
POST   /api/tasks/{id}/complete    - Mark task complete
```

#### Progress
```
GET    /api/progress               - Get user progress
GET    /api/progress/module/{id}   - Get module progress
POST   /api/progress/task/{id}     - Update task progress
GET    /api/progress/stats         - Get progress statistics
```

#### Study Tools
```
GET    /api/study/flashcards       - Get flashcard decks
GET    /api/study/flashcards/{id}  - Get deck cards
POST   /api/study/flashcards/progress - Update card progress

GET    /api/study/quizzes          - Get available quizzes
POST   /api/study/quizzes/{id}/start - Start quiz attempt
POST   /api/study/quizzes/{id}/submit - Submit quiz answers

POST   /api/tenta/generate         - Generate exam questions
POST   /api/tenta/submit           - Submit exam attempt
```

#### Studyflow
```
GET    /api/studyflow/sessions     - Get user sessions
POST   /api/studyflow/start        - Start study session
POST   /api/studyflow/{id}/end     - End study session
GET    /api/studyflow/stats        - Get study statistics
```

#### AI (Dallas)
```
POST   /api/dallas/chat            - Chat with AI assistant
POST   /api/ai/analyze-difficulty  - Analyze content difficulty
POST   /api/ai/generate-summary    - Generate content summary
POST   /api/ai/recommend-next      - Get next step recommendations
```

#### Analytics & Gamification
```
GET    /api/analytics/overview     - Dashboard analytics
GET    /api/analytics/skillpath    - Skillpath data
GET    /api/badges                 - Get available badges
GET    /api/badges/user            - Get user badges
GET    /api/certificates           - Get user certificates
```

#### Bookmarks & Notes
```
GET    /api/bookmarks              - Get user bookmarks
POST   /api/bookmarks              - Create bookmark
DELETE /api/bookmarks/{id}         - Delete bookmark

GET    /api/notes                  - Get study notes
POST   /api/notes                  - Create note
PUT    /api/notes/{id}             - Update note
DELETE /api/notes/{id}             - Delete note
```

#### Admin
```
GET    /api/admin/users            - List all users
GET    /api/admin/users/{id}       - Get user details
PUT    /api/admin/users/{id}       - Update user
DELETE /api/admin/users/{id}       - Delete user
POST   /api/admin/users/{id}/ban   - Ban user
POST   /api/admin/users/{id}/force-logout - Force logout
POST   /api/admin/users/{id}/toggle-admin - Toggle admin

GET    /api/admin/analytics        - System analytics
GET    /api/admin/ai-usage         - AI usage logs
```

#### Notifications
```
GET    /api/notifications          - Get user notifications
PUT    /api/notifications/{id}/read - Mark as read
DELETE /api/notifications/{id}     - Delete notification
```

#### Search
```
GET    /api/search?q=query         - Global search
GET    /api/search/tasks?q=query   - Search tasks
GET    /api/search/modules?q=query - Search modules
```

#### Health & System
```
GET    /health                     - Health check
GET    /api/system/stats           - System statistics
```

### Request/Response Examples

**Login:**
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'

# Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "username": "user",
    "is_admin": false
  }
}
```

**Get Modules:**
```bash
curl -X GET http://localhost:8000/api/modules \
  -H "Authorization: Bearer <token>"

# Response:
[
  {
    "id": "uuid",
    "title": "Linux Basics",
    "slug": "linux-basics",
    "description": "Introduction to Linux...",
    "difficulty": "beginner",
    "estimated_hours": 8.0,
    "is_premium": false,
    "tasks_count": 12,
    "completed_tasks": 5
  },
  ...
]
```

---

## ⚠️ Aktuella Problem

### 🔴 Kritiska Problem

#### 1. Enorma Filer (>900 rader)

**Problem:** 7 filer är >900 rader, svåra att underhålla och testa.

| Fil | Rader | Problem |
|-----|-------|---------|
| `study/tenta-simulator/page.tsx` | 1,191 | Monolitisk exam simulator |
| `study/page.tsx` | 1,175 | All study tools i en fil |
| `SkillpathBoard.tsx` | 1,118 | Komplex visualization |
| `quiz/page.tsx` | 1,011 | Quiz logic + UI |
| `studyflow/page.tsx` | 975 | Session management |
| `modules/[id]/tasks/[taskId]/page.tsx` | 940 | Task viewer |
| `dashboard/page.tsx` | 926 | Dashboard widgets |

**Lösning:**
```
Exempel: study/page.tsx (1,175 rader) → Split till:
- components/study/FlashcardSection.tsx (200 rader)
- components/study/QuizSection.tsx (200 rader)
- components/study/TentaSection.tsx (200 rader)
- components/study/StudyStats.tsx (150 rader)
- hooks/useStudyData.ts (100 rader)
- app/study/page.tsx (150 rader - layout only)
```

#### 2. Föråldrad README

**Problem:** README säger "Baseline Strong Mode scaffold. No features implemented yet."

**Realitet:** 30,000+ rader kod, 15 moduler, AI features, payment integration.

**Lösning:** Ersätt med riktig dokumentation (denna fil är en start).

#### 3. Massivt Archive (12MB)

**Problem:** `/apps/backend/src/db/seeds/_archive/` innehåller:
- Gamla deprecated skillsmaps
- Tidigare versioner av moduler
- Oanvänd study data
- `doe25_tentaplugg_OLD.py` (182KB)

**Lösning:**
- Radera arkivet (om ej behövs)
- Eller flytta till separat archive repo
- Spara disk space och reducera repo size

#### 4. Minimal Test Coverage

**Problem:** Endast 4 test-filer i hela projektet.

**Nuvarande tester:**
- `/apps/backend/tests/test_*.py` (4 filer, minimal coverage)
- Frontend: Jest setup men inga tester

**Lösning:**
```bash
# Backend (pytest)
tests/
  test_auth.py          # Auth flows
  test_modules.py       # Module CRUD
  test_progress.py      # Progress tracking
  test_ai.py            # AI services
  test_admin.py         # Admin functions

# Frontend (Jest + Testing Library)
__tests__/
  components/
    ui/Button.test.tsx
    learning/TaskCard.test.tsx
  hooks/
    useAuth.test.ts
  pages/
    dashboard.test.tsx

# Target: >70% coverage
```

#### 5. Security Issues

**a) CORS Origins Hardcoded:**
```python
# apps/backend/src/main.py
origins = [
    "http://localhost:3000",
    "https://ginonova.com",
    "https://www.ginonova.com",
    # ... hardcoded lista
]
```
**Fix:** Använd environment variable.

**b) Production Dockerfile kör dev mode:**
```dockerfile
# apps/frontend/Dockerfile
CMD ["npm", "run", "dev"]  # ❌ Fel!
```
**Fix:** Ändra till `CMD ["npm", "run", "start"]`

**c) Saknar Rate Limiting:**
```python
# TODO kommentarer överallt:
# TODO Phase 2: Add rate limiting middleware
```
**Fix:** Implementera SlowAPI eller FastAPI rate limiter.

### 🟡 Medelsvåra Problem

#### 6. TODO-kommentarer (82 filer)

**Problem:** 82 filer med TODO/FIXME kommentarer.

**Exempel:**
```python
# TODO Phase 2: Add rate limiting middleware
# TODO: Add validation
# FIXME: Handle edge case
# NOTE: This is a workaround
```

**Lösning:**
1. Samla alla TODOs: `grep -r "TODO\|FIXME" apps/`
2. Skapa GitHub issues
3. Prioritera och implementera
4. Ta bort TODO eller ersätt med issue-referens

#### 7. Inkonsistent Error Handling

**Problem:** Vissa routes har comprehensive error handling, andra basic try-catch.

**Exempel:**
```python
# God error handling
try:
    result = await service.do_thing()
except SpecificError as e:
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:
    logger.error(f"Unexpected: {e}")
    raise HTTPException(status_code=500, detail="Internal error")

# Dålig error handling
try:
    result = await service.do_thing()
except Exception:
    pass  # ❌ Swallows errors
```

**Lösning:** Standardisera error handling med middleware.

#### 8. Saknar API Documentation

**Problem:** FastAPI auto-docs ej konfigurerade ordentligt.

**Nuvarande:** `/docs` endpoint finns men minimal description.

**Lösning:**
```python
# main.py
app = FastAPI(
    title="DevOpsHub API",
    description="E-learning platform API för DevOps education",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {"name": "auth", "description": "Authentication operations"},
        {"name": "modules", "description": "Learning modules"},
        # ... etc
    ]
)

# I varje route:
@router.post("/login", tags=["auth"], summary="Login user")
async def login(credentials: LoginSchema):
    """
    Login user with email and password.

    Returns JWT access token.
    """
    ...
```

### 🟠 Mindre Problem

#### 9. Duplicate Code Patterns

**Problem:** Liknande patterns upprepas.

**Exempel:**
- Flera fetch wrappers istället för en API client
- Samma skeleton loaders i olika pages
- Repetitiv form validation

**Lösning:**
```typescript
// lib/api-client.ts - Single source of truth
class ApiClient {
  async get<T>(url: string): Promise<T> { ... }
  async post<T>(url: string, data: any): Promise<T> { ... }
  // ...
}

// components/ui/SkeletonLoader.tsx - Reusable
export function SkeletonLoader({ type }: { type: 'card' | 'list' | 'table' }) {
  // ...
}
```

#### 10. Deprecated Files

**Problem:** Backup och gamla filer ligger kvar.

**Exempel:**
- `/apps/frontend/_backup_design_v1/`
- `/apps/backend/Dockerfile.deprecated`
- `doe25_tentaplugg_OLD.py`

**Lösning:** Radera eller flytta till archive repo.

---

## 🧹 Rekommendationer för Städning

### Immediate Actions (Gör nu)

#### 1. Radera Archive & Backups
```bash
# Ta backup först (om osäker)
tar -czf archive_backup_$(date +%Y%m%d).tar.gz apps/backend/src/db/seeds/_archive/

# Radera
rm -rf apps/backend/src/db/seeds/_archive/
rm -rf apps/frontend/_backup_design_v1/
rm apps/backend/Dockerfile.deprecated
rm apps/backend/src/db/seeds/doe25_tentaplugg_OLD.py

# Commit
git add .
git commit -m "🧹 Clean up: Remove archived and deprecated files"
```

**Vinst:** -12MB repo size, renare struktur.

#### 2. Uppdatera README.md
```bash
# Ersätt nuvarande README med kortversion av denna doc
cat > README.md << 'EOF'
# DevOpsHub

Interactive e-learning platform för DevOps, Linux och systemadministration.

## Quick Start

Se [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md) för komplett dokumentation.

### Development
```bash
npm install
npm run dev
```

### Documentation
- [Projektöversikt](./PROJECT_OVERVIEW.md)
- [Setup Guide](./PROJECT_OVERVIEW.md#kom-igång-setup)
- [API Docs](http://localhost:8000/docs)

## Tech Stack
- Frontend: Next.js 16, TypeScript, Tailwind
- Backend: FastAPI, Python 3.11, PostgreSQL
- Deployment: Netlify + Railway

EOF

git add README.md
git commit -m "📝 Update README with accurate information"
```

#### 3. Fix Security Issues

**a) CORS Environment Variable:**
```python
# apps/backend/src/core/settings.py
class Settings(BaseSettings):
    # ...
    API_ORIGINS: str = "http://localhost:3000"  # Comma-separated

# apps/backend/src/main.py
from src.core.settings import settings

origins = settings.API_ORIGINS.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # ...
)
```

**b) Fix Production Dockerfile:**
```dockerfile
# apps/frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "start"]  # ✅ Production mode
```

**c) Add Rate Limiting:**
```bash
cd apps/backend
poetry add slowapi
```

```python
# apps/backend/src/main.py
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# I routes:
@router.post("/login")
@limiter.limit("5/minute")  # Max 5 login attempts per minute
async def login(request: Request, ...):
    ...
```

### Medium-term Actions (Nästa sprint)

#### 4. Refactor Large Files

**Prioritet 1: `study/page.tsx` (1,175 rader)**

**Före:**
```
app/study/page.tsx (1,175 rader)
- Flashcard section
- Quiz section
- Tenta section
- Stats section
- All logic inline
```

**Efter:**
```
app/study/
  page.tsx (150 rader - layout only)

components/study/
  FlashcardSection.tsx (200 rader)
  QuizSection.tsx (200 rader)
  TentaSection.tsx (200 rader)
  StudyStats.tsx (150 rader)

hooks/
  useFlashcards.ts (100 rader)
  useQuizzes.ts (100 rader)
  useStudyStats.ts (75 rader)
```

**Implementation:**
```bash
# 1. Skapa nya component files
mkdir -p apps/frontend/src/components/study
mkdir -p apps/frontend/src/hooks/study

# 2. Extrahera en section i taget (iterativt)
# 3. Testa efter varje extraktion
# 4. Commit efter varje lyckad refactor
```

#### 5. Standardisera Error Handling

**Skapa Error Middleware:**
```python
# apps/backend/src/core/errors.py
from fastapi import Request, status
from fastapi.responses import JSONResponse
from typing import Dict, Any

class AppException(Exception):
    def __init__(
        self,
        status_code: int,
        detail: str,
        error_code: str = None
    ):
        self.status_code = status_code
        self.detail = detail
        self.error_code = error_code

class ValidationError(AppException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            error_code="VALIDATION_ERROR"
        )

class NotFoundError(AppException):
    def __init__(self, resource: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} not found",
            error_code="NOT_FOUND"
        )

# Exception handler
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.error_code or "ERROR",
            "detail": exc.detail,
            "path": str(request.url)
        }
    )

# main.py
app.add_exception_handler(AppException, app_exception_handler)
```

**Använd i routes:**
```python
# Före
@router.get("/{id}")
async def get_module(id: str):
    try:
        module = await module_service.get(id)
        if not module:
            raise HTTPException(status_code=404, detail="Not found")
        return module
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Efter
@router.get("/{id}")
async def get_module(id: str):
    module = await module_service.get(id)
    if not module:
        raise NotFoundError("Module")
    return module
```

#### 6. Add Comprehensive Tests

**Setup Test Infrastructure:**
```bash
# Backend
cd apps/backend
poetry add --group dev pytest pytest-asyncio pytest-cov httpx

# Frontend
cd apps/frontend
npm install --save-dev @testing-library/react @testing-library/jest-dom jest-environment-jsdom
```

**Test Structure:**
```
apps/backend/tests/
  conftest.py              # Test fixtures
  test_auth.py             # Auth tests
  test_modules.py          # Module tests
  test_progress.py         # Progress tests
  test_admin.py            # Admin tests
  integration/
    test_user_flow.py      # E2E user flows

apps/frontend/__tests__/
  setup.ts                 # Jest setup
  components/
    ui/Button.test.tsx
  hooks/
    useAuth.test.ts
  pages/
    dashboard.test.tsx
```

**Example Test:**
```python
# apps/backend/tests/test_auth.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    response = await client.post("/api/auth/register", json={
        "email": "test@example.com",
        "password": "SecurePass123!",
        "username": "testuser"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "access_token" in data

@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient):
    response = await client.post("/api/auth/login", json={
        "email": "test@example.com",
        "password": "WrongPassword"
    })
    assert response.status_code == 401
```

### Long-term Actions (Nästa kvartal)

#### 7. Implement Monitoring & Logging

**Add Structured Logging:**
```python
# apps/backend/src/core/logging.py
import logging
import sys
from loguru import logger

# Remove default handler
logger.remove()

# Add custom handler
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
    level="INFO",
    serialize=True  # JSON output
)

# Add file handler
logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="1 day",
    retention="30 days",
    level="DEBUG"
)
```

**Add Error Monitoring (Sentry):**
```python
import sentry_sdk

sentry_sdk.init(
    dsn="your-sentry-dsn",
    traces_sample_rate=1.0,
    environment=settings.RAILWAY_ENV or "development"
)
```

#### 8. Performance Optimization

**Database Indexing:**
```python
# alembic migration
def upgrade():
    op.create_index('idx_progress_user_id', 'progress', ['user_id'])
    op.create_index('idx_progress_task_id', 'progress', ['task_id'])
    op.create_index('idx_tasks_module_id', 'tasks', ['module_id'])
    op.create_index('idx_modules_track_id', 'modules', ['track_id'])
```

**Query Optimization:**
```python
# Använd eager loading
from sqlalchemy.orm import selectinload

modules = await db.execute(
    select(Module)
    .options(selectinload(Module.tasks))  # Avoid N+1 queries
    .where(Module.track_id == track_id)
)
```

**Frontend Code Splitting:**
```typescript
// app/admin/page.tsx
import dynamic from 'next/dynamic'

const AdminDashboard = dynamic(() => import('@/components/admin/Dashboard'), {
  loading: () => <SkeletonLoader />,
  ssr: false
})
```

#### 9. Documentation

**Setup Automated API Docs:**
```python
# main.py - Already has FastAPI, just enhance
app = FastAPI(
    title="DevOpsHub API",
    description=open("API_DESCRIPTION.md").read(),
    version="1.0.0",
    contact={
        "name": "DevOpsHub Team",
        "email": "support@ginonova.com"
    },
    license_info={
        "name": "Proprietary"
    }
)
```

**Component Documentation (Storybook):**
```bash
cd apps/frontend
npx storybook init
```

---

## 🚀 Förbättringsförslag

### Architecture Improvements

#### 1. Implement Caching Strategy

**Problem:** Ingen konsistent caching strategy.

**Lösning:**
```python
# Cache layers
1. Redis - Session data, rate limiting
2. PostgreSQL - Source of truth
3. Frontend - TanStack Query (stale-while-revalidate)

# Implementation
from functools import lru_cache
from aiocache import cached
from aiocache.serializers import JsonSerializer

@cached(ttl=300, serializer=JsonSerializer())  # 5 min cache
async def get_all_modules():
    return await module_repository.get_all()
```

#### 2. Event-Driven Architecture (Optional)

**För skalbarhet:**
```python
# apps/backend/src/events/
events.py         # Event definitions
handlers.py       # Event handlers
publisher.py      # Publish events

# Exempel: User completes task
await event_publisher.publish(
    "task.completed",
    {
        "user_id": user_id,
        "task_id": task_id,
        "xp_earned": xp
    }
)

# Handlers listen:
# - Update progress
# - Award XP
# - Check badges
# - Send notifications
# - Update analytics
```

#### 3. API Versioning

**Förbered för breaking changes:**
```python
# apps/backend/src/api/
v1/
  routes/
    modules.py
    tasks.py
v2/  # Future version
  routes/
    modules.py

# main.py
app.include_router(api_v1_router, prefix="/api/v1")
app.include_router(api_v2_router, prefix="/api/v2")
```

### Feature Improvements

#### 4. Real-time Features

**WebSocket support:**
```python
# Live study sessions
# Real-time notifications
# Collaborative features

from fastapi import WebSocket

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    # Handle real-time communication
```

#### 5. Content Management System (CMS)

**Problem:** Content hårdkodat i seeds.

**Lösning:**
```
Admin CMS för:
- Module creation
- Task editing
- Content block management
- WYSIWYG editor
- Preview before publish
- Version control
```

#### 6. Analytics Dashboard

**Utöka analytics:**
```
User Analytics:
- Learning patterns
- Time of day analysis
- Difficulty vs completion rate
- Drop-off points

Module Analytics:
- Popular modules
- Completion rates
- Average time per task
- User feedback

Business Analytics:
- Revenue tracking
- Conversion funnel
- Retention metrics
- Churn prediction
```

### Developer Experience

#### 7. Development Containers

**devcontainer.json:**
```json
{
  "name": "DevOpsHub",
  "dockerComposeFile": "docker-compose.dev.yml",
  "service": "app",
  "workspaceFolder": "/workspace",
  "extensions": [
    "dbaeumer.vscode-eslint",
    "ms-python.python",
    "bradlc.vscode-tailwindcss"
  ]
}
```

#### 8. Pre-commit Hooks

**Already configured, enhance:**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=1000']

  - repo: https://github.com/psf/black
    hooks:
      - id: black

  - repo: local
    hooks:
      - id: tests
        name: run tests
        entry: npm run test
        language: system
        pass_filenames: false
```

#### 9. CI/CD Pipeline

**GitHub Actions:**
```yaml
# .github/workflows/ci.yml
name: CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm run test

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        run: npm run build

  deploy:
    needs: [test, build]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

---

## 📊 Metrics & Goals

### Current State
```
Lines of Code:     ~30,000+
Test Coverage:     <10%
Files:             500+
Large Files (>900): 7
TODO Comments:     82 files
Archive Size:      12MB
Documentation:     Minimal
```

### Target State (3 månader)
```
Lines of Code:     ~25,000 (after refactor)
Test Coverage:     >70%
Files:             450 (after cleanup)
Large Files (>900): 0
TODO Comments:     0 (converted to issues)
Archive Size:      0MB
Documentation:     Comprehensive
```

### Success Metrics
- [ ] All files <500 rader
- [ ] Test coverage >70%
- [ ] All TODOs resolved eller converterade till issues
- [ ] API documentation complete
- [ ] Setup guide tested av ny utvecklare
- [ ] <2 minuter från clone till running app
- [ ] Zero security warnings
- [ ] Automated CI/CD pipeline

---

## 🎯 Action Plan - Prioriterad Lista

### Sprint 1 (Vecka 1-2): Cleanup
- [x] Skapa denna dokumentation
- [ ] Radera archive & deprecated files
- [ ] Uppdatera README.md
- [ ] Fix security issues (CORS, Dockerfile, rate limiting)
- [ ] Samla alla TODOs i GitHub issues

### Sprint 2 (Vecka 3-4): Refactoring
- [ ] Refactor study/page.tsx
- [ ] Refactor tenta-simulator/page.tsx
- [ ] Refactor dashboard/page.tsx
- [ ] Standardisera error handling
- [ ] Implementera logging

### Sprint 3 (Vecka 5-6): Testing
- [ ] Setup test infrastructure
- [ ] Backend tests (auth, modules, progress)
- [ ] Frontend tests (components, hooks)
- [ ] Integration tests
- [ ] Aim for 50% coverage

### Sprint 4 (Vecka 7-8): Documentation & DevEx
- [ ] Complete API documentation
- [ ] Setup Storybook
- [ ] Improve pre-commit hooks
- [ ] CI/CD pipeline
- [ ] Developer onboarding guide

### Sprint 5+ (Vecka 9+): Optimization
- [ ] Performance optimization
- [ ] Database indexing
- [ ] Caching strategy
- [ ] Monitoring (Sentry)
- [ ] Analytics dashboard

---

## 🤝 Contributing

### Code Style

**TypeScript/React:**
```typescript
// Använd functional components
export function MyComponent({ prop }: Props) {
  // Custom hooks först
  const { data } = useMyData()

  // Event handlers
  const handleClick = () => {}

  // Return JSX
  return <div>...</div>
}

// Filename: PascalCase för components
// MyComponent.tsx

// Filename: camelCase för utilities
// myUtility.ts
```

**Python:**
```python
# Använd async/await
async def my_function() -> ReturnType:
    """Docstring describing function."""
    result = await some_async_operation()
    return result

# Filename: snake_case
# my_module.py

# Class names: PascalCase
class MyClass:
    pass
```

### Git Workflow
```bash
# Feature branch
git checkout -b feature/my-feature

# Commits
git commit -m "feat: Add new feature"
git commit -m "fix: Fix bug"
git commit -m "docs: Update documentation"
git commit -m "refactor: Refactor code"
git commit -m "test: Add tests"

# Conventional commits format
```

---

## 📞 Support & Resources

### Documentation
- [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md) - This file
- [API Docs](http://localhost:8000/docs) - FastAPI auto-docs
- `/docs/phases/` - Development phase documentation

### External Resources
- [Next.js Docs](https://nextjs.org/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [TanStack Query](https://tanstack.com/query/latest)

### Team Contact
- **Tech Lead:** [Fill in]
- **Backend:** [Fill in]
- **Frontend:** [Fill in]

---

## 📝 Changelog

### 2026-01-05
- ✨ Initial PROJECT_OVERVIEW.md created
- 📊 Comprehensive codebase analysis completed
- 🎯 Action plan defined

---

## 🎓 Slutsats

**DevOpsHub är en ambitiös och feature-rik plattform** med solid arkitektur men visar tecken på snabb utveckling med ackumulerad teknisk skuld.

### Styrkor ✅
- Modern tech stack (Next.js 16, FastAPI, PostgreSQL)
- Ren arkitektur (repository pattern, service layer)
- Omfattande funktioner (learning, AI, gamification)
- Deployment setup (Netlify, Railway)
- God separation of concerns

### Svagheter ⚠️
- Stora filer (>1000 rader)
- Låg test coverage (<10%)
- Inkonsistenta patterns
- Föråldrad dokumentation
- Security gaps (rate limiting, etc.)

### Rekommendation 🎯
**Fokusera på refactoring och testing innan nya features.**
Plattformen fungerar men underhåll kommer bli svårare utan städning.

**Nästa Steg:**
1. Radera archive (12MB)
2. Refactor stora filer
3. Lägg till tester
4. Uppdatera dokumentation
5. Fix security issues

**Risk Level:** 🟡 Medium
Plattformen är deployed och fungerar, men behöver refactoring för långsiktig hållbarhet.

---

*Dokumentation genererad: 2026-01-05*
*Version: 1.0.0*
*Författare: Claude Code Analysis*
