"""
React SkillsMap - Block 5: Production & Testing
Nodes 17-20: Testing, Deployment, State Management, Capstone
"""

from typing import Any

# ============================================================================
# NODE 17: TESTING REACT APPS
# ============================================================================

REACT_NODE_17_TESTING = {
    "node_id": 17,
    "title": "Testing React Apps",
    "slug": "react-testing",
    "description": "Testa React-komponenter med Jest och Testing Library",
    "difficulty": "intermediate",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "jest", "react testing library", "unit tests", "integration tests",
        "mocking", "snapshot testing", "coverage"
    ],
    "content": """
# Testing React Apps

------------------------------------------------------------

## Vad ar React Testing?

Tester ger dig sjalvfortroende att deploya. Utan tester ar varje deploy ett hasardspel.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| CI/CD | Tester ar gateway for deployment pipelines |
| Kvalitet | Fanga buggar innan produktion |
| Dokumentation | Tester dokumenterar forvantad funktionalitet |
| Refactoring | Mojliggor sakra kodandringar |
| Coverage | Metrics for testning av kodbasen |

------------------------------------------------------------

## Testing Library Philosophy

```
+-----------------------------------------------------------------+
|           TESTING LIBRARY GUIDING PRINCIPLE                      |
+-----------------------------------------------------------------+
|                                                                  |
|  Ju mer dina tester liknar hur din mjukvara anvands,            |
|  desto mer sjalvfortroende ger de dig.                          |
|                                                                  |
|  - Testa BETEENDE, inte implementation                          |
|  - Query element som anvandare ser dem                          |
|  - Testa INTE interna state-variabler                           |
|  - Testa INTE implementation detaljer                           |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Snabbreferens

| Query | Anvandning | Async |
|-------|------------|-------|
| getBy | Element finns, failar annars | Nej |
| queryBy | Element kanske finns | Nej |
| findBy | Vanta pa element | Ja |
| getByRole | Accessibility role | Nej |
| getByLabelText | Form labels | Nej |
| getByText | Textinnehall | Nej |

------------------------------------------------------------

## Setup

```bash
# For Vite-projekt:
npm install -D @testing-library/react @testing-library/jest-dom @testing-library/user-event vitest jsdom
```

```tsx
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './src/test/setup.ts',
  },
});

// src/test/setup.ts
import '@testing-library/jest-dom';
```

------------------------------------------------------------

## Komponent Test Exempel

```tsx
// src/components/Button.tsx
interface ButtonProps {
  onClick: () => void;
  children: React.ReactNode;
  disabled?: boolean;
}

export function Button({ onClick, children, disabled }: ButtonProps) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {children}
    </button>
  );
}

// src/components/Button.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button', () => {
  it('renderar children', () => {
    render(<Button onClick={() => {}}>Klicka mig</Button>);
    expect(screen.getByText('Klicka mig')).toBeInTheDocument();
  });

  it('anropar onClick vid klick', async () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Klicka mig</Button>);

    await userEvent.click(screen.getByRole('button'));

    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('ar disabled nar disabled prop ar true', () => {
    render(<Button onClick={() => {}} disabled>Klicka mig</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

------------------------------------------------------------

## Testa Formular

```tsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  it('submittar med email och losenord', async () => {
    const handleSubmit = vi.fn();
    render(<LoginForm onSubmit={handleSubmit} />);

    await userEvent.type(screen.getByLabelText(/email/i), 'test@example.com');
    await userEvent.type(screen.getByLabelText(/losenord/i), 'password123');
    await userEvent.click(screen.getByRole('button', { name: /skicka/i }));

    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123',
      });
    });
  });

  it('visar valideringsfel for ogiltig email', async () => {
    render(<LoginForm onSubmit={() => {}} />);

    await userEvent.type(screen.getByLabelText(/email/i), 'ogiltig');
    await userEvent.click(screen.getByRole('button', { name: /skicka/i }));

    expect(await screen.findByText(/ogiltig email/i)).toBeInTheDocument();
  });
});
```

------------------------------------------------------------

## Mocking

```tsx
// Mocka fetch
beforeEach(() => {
  vi.spyOn(global, 'fetch').mockResolvedValue({
    ok: true,
    json: () => Promise.resolve({ users: [{ id: 1, name: 'John' }] }),
  } as Response);
});

afterEach(() => {
  vi.restoreAllMocks();
});

it('hamtar och visar anvandare', async () => {
  render(<UserList />);

  expect(await screen.findByText('John')).toBeInTheDocument();
});

// Mocka moduler
vi.mock('../lib/api', () => ({
  getUsers: vi.fn(() => Promise.resolve([{ id: 1, name: 'John' }])),
}));
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Element not found | Element finns inte an | Anvand findBy for async |
| act() warning | State uppdateras utanfor act | Wrappa i waitFor |
| Mock fungerar inte | Fel mock-path | Kontrollera relativa paths |
| Test timeout | Async operation tar for lang tid | Oka timeout eller mocka |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Testing Library | Testa beteende, inte implementation |
| userEvent | Realistisk anvandarinteraktion |
| findBy | For asynkrona element |
| Mock | Isolera externa beroenden |
| getByRole | Foredras over getByTestId |

### Kom ihag
- Tester ar obligatoriska i professionell utveckling
- Testa vad komponenten GOR, inte hur
- Anvand findBy for element som laddas asynkront
- Mocka externa API:er for snabba, stabila tester
- getByRole forbattrar bade tester och accessibility

## Sammanfattning

- **Testing Library** - testa beteende, inte implementation
- **userEvent** for realistisk anvandarinteraktion
- **findBy** for asynkrona element
- **Mock** externa beroenden (fetch, API)
- **screen.getByRole** foredras over getByTestId
""",
}


# ============================================================================
# NODE 18: STATE MANAGEMENT
# ============================================================================

REACT_NODE_18_STATE_MANAGEMENT = {
    "node_id": 18,
    "title": "State Management Libraries",
    "slug": "state-management",
    "description": "Zustand, Jotai, och Redux Toolkit",
    "difficulty": "advanced",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "zustand", "jotai", "redux toolkit", "global state",
        "state persistence", "devtools"
    ],
    "content": """
# State Management Libraries

------------------------------------------------------------

## Vad ar State Management?

Valj ratt verktyg for jobbet. Ibland racker Context, ibland behover du mer.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Performance | Ratt state-losning paverkar rendering och bundle size |
| Debugging | Devtools mojliggor time-travel debugging |
| Persistence | State kan sparas for offline-stod |
| Testing | Isolerat state forenklar testning |
| Scalability | Ratt arkitektur skalar med teamet |

------------------------------------------------------------

## Snabbreferens

| Losning | Anvandning | Bundle Size |
|---------|------------|-------------|
| useState | Komponent-lokal | 0 (inbyggt) |
| Context | Tema, auth, settings | 0 (inbyggt) |
| Zustand | Global state, enkel | ~1KB |
| Jotai | Atomic state | ~2KB |
| Redux Toolkit | Komplex app | ~11KB |
| TanStack Query | Server state | ~12KB |

------------------------------------------------------------

## State Management Val

```
+-----------------------------------------------------------------+
|                STATE MANAGEMENT CHOICES                          |
+-----------------------------------------------------------------+
|                                                                  |
|  Local State (useState)                                         |
|  +- Komponent-specifikt, enkelt                                 |
|                                                                  |
|  Context API                                                    |
|  +- Tema, auth, settings (sallan uppdateras)                    |
|                                                                  |
|  Zustand (Rekommenderat)                                        |
|  +- Global state, enkel API, liten bundle                       |
|                                                                  |
|  Jotai                                                          |
|  +- Atomic state, finkorning, React Suspense                    |
|                                                                  |
|  Redux Toolkit                                                  |
|  +- Komplex app, time-travel debugging, middleware              |
|                                                                  |
|  TanStack Query                                                 |
|  +- Server state (API-data, caching, syncing)                   |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Zustand (Rekommenderat)

```tsx
// stores/useStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface User {
  id: string;
  name: string;
}

interface AppState {
  user: User | null;
  theme: 'light' | 'dark';
  setUser: (user: User | null) => void;
  toggleTheme: () => void;
}

export const useStore = create<AppState>()(
  persist(
    (set) => ({
      user: null,
      theme: 'light',
      setUser: (user) => set({ user }),
      toggleTheme: () => set((state) => ({
        theme: state.theme === 'light' ? 'dark' : 'light'
      })),
    }),
    {
      name: 'app-storage',
    }
  )
);

// Anvandning i komponenter
function Profile() {
  const user = useStore((state) => state.user);
  const setUser = useStore((state) => state.setUser);

  return <div>{user?.name}</div>;
}

function ThemeToggle() {
  const { theme, toggleTheme } = useStore();
  return <button onClick={toggleTheme}>{theme}</button>;
}
```

------------------------------------------------------------

## Jotai (Atomic)

```tsx
// atoms/user.ts
import { atom } from 'jotai';
import { atomWithStorage } from 'jotai/utils';

// Basic atom
export const countAtom = atom(0);

// Derived atom
export const doubleCountAtom = atom((get) => get(countAtom) * 2);

// Writable derived
export const countWithValidation = atom(
  (get) => get(countAtom),
  (get, set, newValue: number) => {
    if (newValue >= 0) {
      set(countAtom, newValue);
    }
  }
);

// Persisted atom
export const themeAtom = atomWithStorage('theme', 'light');

// Anvandning
function Counter() {
  const [count, setCount] = useAtom(countAtom);
  const doubleCount = useAtomValue(doubleCountAtom);

  return (
    <div>
      <p>Count: {count}</p>
      <p>Double: {doubleCount}</p>
      <button onClick={() => setCount(c => c + 1)}>+</button>
    </div>
  );
}
```

------------------------------------------------------------

## Redux Toolkit

```tsx
// store/slices/userSlice.ts
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUser = createAsyncThunk(
  'user/fetch',
  async (userId: string) => {
    const response = await fetch(`/api/users/${userId}`);
    return response.json();
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    data: null,
    loading: false,
    error: null,
  },
  reducers: {
    logout: (state) => {
      state.data = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.data = action.payload;
        state.loading = false;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.error = action.error.message;
        state.loading = false;
      });
  },
});

// store/index.ts
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './slices/userSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

// Anvandning
function Profile() {
  const user = useSelector((state) => state.user.data);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUser('123'));
  }, []);

  return <div>{user?.name}</div>;
}
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Re-renders for mycket | Hela store selekteras | Selektera bara det du behover |
| State persisteras inte | Saknar persist middleware | Lagg till persist i Zustand/Jotai |
| Redux boilerplate | For mycket kod | Anvand Redux Toolkit createSlice |
| Circular dependency | Store importerar components | Separera store-logik |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Zustand | Enkel, minimal, bra default-val |
| Jotai | Atomic state, React-native |
| Redux Toolkit | Komplex app, middleware, devtools |
| Val | Basera pa komplexitet, inte hype |
| Server State | TanStack Query for API-data |

### Kom ihag
- Borja med useState och Context
- Zustand ar basta default for global state
- Redux Toolkit for stora team och komplex logik
- TanStack Query for server state
- Over-engineera inte state management
""",
}


# ============================================================================
# NODE 19: DEPLOYMENT & PRODUCTION
# ============================================================================

REACT_NODE_19_DEPLOYMENT = {
    "node_id": 19,
    "title": "Deployment & Production",
    "slug": "react-deployment",
    "description": "Deploy React/Next.js appar till produktion",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "vercel", "netlify", "docker", "environment variables",
        "CI/CD", "monitoring", "analytics"
    ],
    "content": """
# Deployment & Production

------------------------------------------------------------

## Vad ar Deployment?

En feature ar inte klar forrn den ar i produktion.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| CI/CD | Automatiserade deployments minskar risk |
| Environment | Hantera config mellan miljoer |
| Monitoring | Overvaka prestanda och fel |
| Scaling | Hantera trafik och last |
| Rollback | Snabb atergag vid problem |

------------------------------------------------------------

## Snabbreferens

| Platform | Bast for | Kostnad |
|----------|---------|---------|
| Vercel | Next.js | Free tier |
| Netlify | Statiska sites | Free tier |
| AWS Amplify | AWS-integration | Pay-as-you-go |
| Railway | Full-stack | Free tier |
| Docker | Full kontroll | Varierar |

------------------------------------------------------------

## Deployment Platforms

```
+-----------------------------------------------------------------+
|                  DEPLOYMENT PLATFORMS                            |
+-----------------------------------------------------------------+
|                                                                  |
|  Vercel (Rekommenderat for Next.js)                             |
|  +- Git push = deploy, preview URLs, edge functions             |
|                                                                  |
|  Netlify                                                        |
|  +- Bra for statiska sites, edge functions                      |
|                                                                  |
|  AWS Amplify                                                    |
|  +- AWS integration, CI/CD                                      |
|                                                                  |
|  Docker + Railway/Fly.io                                        |
|  +- Full kontroll, containers                                   |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Vercel Deployment

```bash
# Installera Vercel CLI
npm i -g vercel

# Deploy
vercel

# Deploy till produktion
vercel --prod
```

### vercel.json

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "regions": ["arn1"],
  "env": {
    "DATABASE_URL": "@database-url"
  }
}
```

------------------------------------------------------------

## Environment Variables

```bash
# .env.local (lokal utveckling - ALDRIG committa!)
DATABASE_URL=postgresql://localhost:5432/mydb
NEXT_PUBLIC_API_URL=http://localhost:3000/api

# .env.production
NEXT_PUBLIC_API_URL=https://api.myapp.com
```

```tsx
// Anvanda env variables
// NEXT_PUBLIC_ prefix = tillganglig i browser
const apiUrl = process.env.NEXT_PUBLIC_API_URL;

// Server-only (utan NEXT_PUBLIC_)
const dbUrl = process.env.DATABASE_URL;
```

------------------------------------------------------------

## Docker Deployment

```dockerfile
FROM node:20-alpine AS base

FROM base AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM base AS runner
WORKDIR /app
ENV NODE_ENV production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT 3000

CMD ["node", "server.js"]
```

```js
// next.config.js
module.exports = {
  output: 'standalone',
};
```

------------------------------------------------------------

## Production Checklist

```
+-----------------------------------------------------------------+
|              PRODUCTION CHECKLIST                                |
+-----------------------------------------------------------------+
|                                                                  |
|  - Environment variables konfigurerade                          |
|  - HTTPS aktiverat                                              |
|  - Error tracking (Sentry)                                      |
|  - Analytics (Vercel Analytics, Plausible)                      |
|  - Performance monitoring                                       |
|  - Logging                                                      |
|  - Security headers                                             |
|  - Rate limiting                                                |
|  - Database backups                                             |
|  - CI/CD pipeline                                               |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Build failar | Saknade env vars | Konfigurera i Vercel/Netlify |
| 500 error | Server-side fel | Kontrollera logs och error tracking |
| Slow load | Stora bundles | Analysera med next/bundle-analyzer |
| CORS errors | Fel API-konfiguration | Konfigurera headers i middleware |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Vercel | Basta valet for Next.js |
| Env vars | Separera config fran kod |
| Docker | Portabilitet och full kontroll |
| Monitoring | Kritiskt i produktion |
| CI/CD | Automatisera deployments |

### Kom ihag
- Commita aldrig hemligheter till git
- Anvand preview deployments for code review
- Satt upp monitoring fran dag ett
- Ha en rollback-plan
- Testa i staging innan produktion
""",
}


# ============================================================================
# NODE 20: CAPSTONE PROJECT
# ============================================================================

REACT_NODE_20_CAPSTONE = {
    "node_id": 20,
    "title": "Capstone: Full-Stack Dashboard",
    "slug": "react-capstone",
    "description": "Bygg en komplett dashboard-applikation",
    "difficulty": "advanced",
    "estimated_minutes": 180,
    "xp_reward": 200,
    "topics_covered": [
        "full-stack", "authentication", "database", "api routes",
        "real-time", "deployment"
    ],
    "content": """
# Capstone: Full-Stack Dashboard

------------------------------------------------------------

## Projektbeskrivning

Dags att satta ihop allt. Bygg nagot riktigt.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Integration | Praktisk erfarenhet av fullstack-utveckling |
| Deployment | End-to-end deployment pipeline |
| Monitoring | Bygg dashboard for overvakning |
| Best Practices | Tillampning av produktionsklar kod |
| Portfolio | Konkret projekt att visa upp |

------------------------------------------------------------

## Snabbreferens

| Steg | Uppgift | Tid |
|------|---------|-----|
| 1 | Setup projekt | 30 min |
| 2 | Auth implementation | 45 min |
| 3 | Dashboard UI | 45 min |
| 4 | API routes | 30 min |
| 5 | Real-time features | 20 min |
| 6 | Deployment | 10 min |

------------------------------------------------------------

## Project Overview

Bygg en DevOps Dashboard med:
- Authentication (NextAuth.js)
- Database (Prisma + PostgreSQL)
- Real-time updates
- Charts och visualiseringar
- Deploy till Vercel

------------------------------------------------------------

## Tech Stack

```
+-----------------------------------------------------------------+
|                      TECH STACK                                  |
+-----------------------------------------------------------------+
|                                                                  |
|  Frontend: Next.js 14, React 18, TypeScript                     |
|  Styling: Tailwind CSS, shadcn/ui                               |
|  State: Zustand + TanStack Query                                |
|  Database: PostgreSQL + Prisma                                  |
|  Auth: NextAuth.js                                              |
|  Charts: Recharts                                               |
|  Forms: React Hook Form + Zod                                   |
|  Testing: Vitest + Testing Library                              |
|  Deploy: Vercel                                                 |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Projektstruktur

```
devops-dashboard/
+-- src/
|   +-- app/
|   |   +-- (auth)/
|   |   |   +-- login/page.tsx
|   |   |   +-- register/page.tsx
|   |   +-- (dashboard)/
|   |   |   +-- layout.tsx
|   |   |   +-- page.tsx
|   |   |   +-- deployments/page.tsx
|   |   |   +-- servers/page.tsx
|   |   |   +-- settings/page.tsx
|   |   +-- api/
|   |   |   +-- auth/[...nextauth]/route.ts
|   |   |   +-- deployments/route.ts
|   |   |   +-- servers/route.ts
|   |   +-- layout.tsx
|   +-- components/
|   |   +-- ui/
|   |   +-- charts/
|   |   +-- forms/
|   +-- lib/
|   |   +-- db.ts
|   |   +-- auth.ts
|   +-- stores/
|       +-- useStore.ts
+-- prisma/
|   +-- schema.prisma
+-- tests/
```

------------------------------------------------------------

## Database Schema

```prisma
// prisma/schema.prisma
model User {
  id            String       @id @default(cuid())
  email         String       @unique
  name          String?
  password      String
  role          Role         @default(USER)
  deployments   Deployment[]
  createdAt     DateTime     @default(now())
}

model Server {
  id          String       @id @default(cuid())
  name        String
  ip          String
  status      ServerStatus @default(ONLINE)
  cpu         Float        @default(0)
  memory      Float        @default(0)
  deployments Deployment[]
}

model Deployment {
  id        String           @id @default(cuid())
  name      String
  status    DeploymentStatus @default(PENDING)
  server    Server           @relation(fields: [serverId], references: [id])
  serverId  String
  user      User             @relation(fields: [userId], references: [id])
  userId    String
  createdAt DateTime         @default(now())
}

enum Role { USER ADMIN }
enum ServerStatus { ONLINE OFFLINE MAINTENANCE }
enum DeploymentStatus { PENDING BUILDING DEPLOYED FAILED }
```

------------------------------------------------------------

## Authentication

```tsx
// lib/auth.ts
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { PrismaAdapter } from '@auth/prisma-adapter';
import { db } from './db';

export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: PrismaAdapter(db),
  providers: [
    CredentialsProvider({
      async authorize(credentials) {
        // Validera och returnera anvandare
      },
    }),
  ],
});
```

------------------------------------------------------------

## Dashboard Page

```tsx
// app/(dashboard)/page.tsx
import { DeploymentChart } from '@/components/charts/DeploymentChart';
import { ServerGrid } from '@/components/ServerGrid';
import { StatsCards } from '@/components/StatsCards';

export default async function DashboardPage() {
  const stats = await getStats();
  const servers = await getServers();
  const deployments = await getRecentDeployments();

  return (
    <div className="space-y-6">
      <h1>Dashboard</h1>
      <StatsCards stats={stats} />
      <div className="grid grid-cols-2 gap-6">
        <DeploymentChart data={deployments} />
        <ServerGrid servers={servers} />
      </div>
    </div>
  );
}
```

------------------------------------------------------------

## Real-time Updates

```tsx
// hooks/useServerStatus.ts
import { useQuery } from '@tanstack/react-query';

export function useServerStatus() {
  return useQuery({
    queryKey: ['servers'],
    queryFn: () => fetch('/api/servers').then(r => r.json()),
    refetchInterval: 5000,
  });
}
```

------------------------------------------------------------

## Implementation Steps

1. Setup Project
   - npx create-next-app@latest devops-dashboard
   - Installera dependencies
   - Setup Prisma + PostgreSQL

2. Build Authentication
   - Konfigurera NextAuth
   - Skapa login/register formuler
   - Skyddade routes

3. Create Dashboard UI
   - Layout med sidebar
   - Stats cards
   - Charts (Recharts)

4. Implement API Routes
   - CRUD for deployments
   - Server management
   - User settings

5. Add Real-time Features
   - Server status polling
   - Deployment progress
   - Notifikationer

6. Testing och Deployment
   - Unit tests for komponenter
   - Integration tests
   - Deploy till Vercel

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Auth failar | Session-konfiguration | Kontrollera NextAuth setup |
| Prisma fel | Schema mismatch | Kor prisma db push |
| Charts renderar inte | Data-format | Validera data-strukturen |
| Build failar | TypeScript errors | Fixa typer innan deploy |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Full-stack | Next.js hanterar bade frontend och backend |
| Auth | NextAuth ger sakerhet med minimal setup |
| Database | Prisma forenklar databasoperationer |
| Real-time | TanStack Query med polling |
| Deployment | Vercel for somlost deploy |

### Kom ihag
- Borja enkelt och bygg ut gradvis
- Testa varje del innan du gar vidare
- Anvand TypeScript for sakerhet
- Deploya tidigt for att hitta problem
- Dokumentera ditt arbete

------------------------------------------------------------

## Grattis!

Du har nu lart dig allt du behover for att bygga produktionsklara React/Next.js-applikationer:

- React fundamentals (components, state, effects)
- Hooks och custom hooks
- State management
- Next.js (App Router, RSC, data fetching)
- Testing
- Deployment

Du ar redo att bygga professionella React-applikationer!
""",
}


# Export all nodes from Block 5
BLOCK_5_NODES = [
    REACT_NODE_17_TESTING,
    REACT_NODE_18_STATE_MANAGEMENT,
    REACT_NODE_19_DEPLOYMENT,
    REACT_NODE_20_CAPSTONE,
]
