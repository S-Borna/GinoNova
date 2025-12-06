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

> *"Tests give you confidence to ship. Without tests, every deploy is a gamble."*

---

## 🎯 Why This Matters

Tester är inte optional i professionell utveckling:
- Fånga buggar innan produktion
- Dokumentera förväntad funktionalitet
- Möjliggör säker refactoring
- CI/CD kräver tester

---

## 🧠 Testing Library Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│           TESTING LIBRARY GUIDING PRINCIPLE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  "The more your tests resemble the way your software is used,   │
│   the more confidence they can give you."                       │
│                                                                  │
│  ✅ Testa BETEENDEn, inte implementation                        │
│  ✅ Query elements som användare ser dem                         │
│  ❌ Testa inte interna state-variabler                          │
│  ❌ Testa inte implementation detaljer                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Setup

```bash
# Redan inkluderat i Next.js, för Vite:
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

---

## 💻 Basic Component Test

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
  it('renders children', () => {
    render(<Button onClick={() => {}}>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('calls onClick when clicked', async () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    await userEvent.click(screen.getByRole('button'));
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button onClick={() => {}} disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

---

## 💻 Testing Forms

```tsx
// src/components/LoginForm.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  it('submits with email and password', async () => {
    const handleSubmit = vi.fn();
    render(<LoginForm onSubmit={handleSubmit} />);
    
    await userEvent.type(screen.getByLabelText(/email/i), 'test@example.com');
    await userEvent.type(screen.getByLabelText(/password/i), 'password123');
    await userEvent.click(screen.getByRole('button', { name: /submit/i }));
    
    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123',
      });
    });
  });

  it('shows validation error for invalid email', async () => {
    render(<LoginForm onSubmit={() => {}} />);
    
    await userEvent.type(screen.getByLabelText(/email/i), 'invalid');
    await userEvent.click(screen.getByRole('button', { name: /submit/i }));
    
    expect(await screen.findByText(/invalid email/i)).toBeInTheDocument();
  });
});
```

---

## 💻 Mocking

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

it('fetches and displays users', async () => {
  render(<UserList />);
  
  expect(await screen.findByText('John')).toBeInTheDocument();
});

// Mocka moduler
vi.mock('../lib/api', () => ({
  getUsers: vi.fn(() => Promise.resolve([{ id: 1, name: 'John' }])),
}));
```

---

## ✅ Sammanfattning

- **Testing Library** - testa beteende, inte implementation
- **userEvent** för realistisk användarinteraktion
- **findBy** för asynkrona element
- **Mock** externa beroenden (fetch, API)
- **screen.getByRole** föredras över getByTestId
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

> *"Choose the right tool for the job. Sometimes Context is enough, sometimes you need more."*

---

## 🎯 When to Use What

```
┌─────────────────────────────────────────────────────────────────┐
│                STATE MANAGEMENT CHOICES                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Local State (useState)                                         │
│  └─ Component-specific, enkelt                                  │
│                                                                  │
│  Context API                                                    │
│  └─ Tema, auth, settings (sällan uppdateras)                   │
│                                                                  │
│  Zustand ⭐                                                      │
│  └─ Global state, enkel API, liten bundle                       │
│                                                                  │
│  Jotai                                                          │
│  └─ Atomic state, finkorning, React Suspense                    │
│                                                                  │
│  Redux Toolkit                                                  │
│  └─ Complex apps, time-travel debugging, middleware             │
│                                                                  │
│  TanStack Query                                                 │
│  └─ Server state (API-data, caching, syncing)                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Zustand (Rekommenderat)

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
      name: 'app-storage',  // localStorage key
    }
  )
);

// Användning i komponenter
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

---

## 💻 Jotai (Atomic)

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

// Användning
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

---

## 💻 Redux Toolkit

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

// Användning
function Profile() {
  const user = useSelector((state) => state.user.data);
  const dispatch = useDispatch();
  
  useEffect(() => {
    dispatch(fetchUser('123'));
  }, []);
  
  return <div>{user?.name}</div>;
}
```

---

## ✅ Sammanfattning

- **Zustand** - enkel, minimal, bra default-val
- **Jotai** - atomic state, React-native
- **Redux Toolkit** - komplex app, middleware, devtools
- **Välj baserat på komplexitet** - inte "bara för att"
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

> *"A feature isn't done until it's in production."*

---

## 🎯 Deployment Options

```
┌─────────────────────────────────────────────────────────────────┐
│                  DEPLOYMENT PLATFORMS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Vercel (Rekommenderat för Next.js)                             │
│  └─ Git push = deploy, preview URLs, edge functions             │
│                                                                  │
│  Netlify                                                        │
│  └─ Bra för statiska sites, edge functions                      │
│                                                                  │
│  AWS Amplify                                                    │
│  └─ AWS integration, CI/CD                                      │
│                                                                  │
│  Docker + Railway/Fly.io                                        │
│  └─ Full kontroll, containers                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Vercel Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Deploy to production
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

---

## 💻 Environment Variables

```bash
# .env.local (lokal utveckling - ALDRIG commit!)
DATABASE_URL=postgresql://localhost:5432/mydb
NEXT_PUBLIC_API_URL=http://localhost:3000/api

# .env.production
NEXT_PUBLIC_API_URL=https://api.myapp.com
```

```tsx
// Använda env variables
// NEXT_PUBLIC_ prefix = tillgänglig i browser
const apiUrl = process.env.NEXT_PUBLIC_API_URL;

// Server-only (utan NEXT_PUBLIC_)
const dbUrl = process.env.DATABASE_URL;  // Endast i Server Components
```

---

## 💻 Docker Deployment

```dockerfile
# Dockerfile
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
  output: 'standalone',  // För Docker
};
```

---

## 💻 Production Checklist

```
┌─────────────────────────────────────────────────────────────────┐
│              PRODUCTION CHECKLIST                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✅ Environment variables konfigurerade                         │
│  ✅ HTTPS aktiverat                                              │
│  ✅ Error tracking (Sentry)                                     │
│  ✅ Analytics (Vercel Analytics, Plausible)                     │
│  ✅ Performance monitoring                                      │
│  ✅ Logging                                                     │
│  ✅ Security headers                                            │
│  ✅ Rate limiting                                               │
│  ✅ Database backups                                            │
│  ✅ CI/CD pipeline                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Sammanfattning

- **Vercel** är bästa valet för Next.js
- **Environment variables** för konfiguration
- **Docker** för full kontroll och portabilitet
- **Monitoring & logging** är kritiskt i produktion
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

> *"Time to put everything together. Build something real."*

---

## 🎯 Project Overview

Bygg en **DevOps Dashboard** med:
- Authentication (NextAuth.js)
- Database (Prisma + PostgreSQL)
- Real-time updates
- Charts och visualiseringar
- Deploy till Vercel

---

## 🧠 Tech Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                      TECH STACK                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Frontend: Next.js 14, React 18, TypeScript                     │
│  Styling: Tailwind CSS, shadcn/ui                               │
│  State: Zustand + TanStack Query                                │
│  Database: PostgreSQL + Prisma                                  │
│  Auth: NextAuth.js                                              │
│  Charts: Recharts                                               │
│  Forms: React Hook Form + Zod                                   │
│  Testing: Vitest + Testing Library                              │
│  Deploy: Vercel                                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Project Structure

```bash
devops-dashboard/
├── src/
│   ├── app/
│   │   ├── (auth)/
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── (dashboard)/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── deployments/page.tsx
│   │   │   ├── servers/page.tsx
│   │   │   └── settings/page.tsx
│   │   ├── api/
│   │   │   ├── auth/[...nextauth]/route.ts
│   │   │   ├── deployments/route.ts
│   │   │   └── servers/route.ts
│   │   └── layout.tsx
│   ├── components/
│   │   ├── ui/
│   │   ├── charts/
│   │   └── forms/
│   ├── lib/
│   │   ├── db.ts
│   │   └── auth.ts
│   └── stores/
│       └── useStore.ts
├── prisma/
│   └── schema.prisma
└── tests/
```

---

## 💻 Database Schema

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

enum Role {
  USER
  ADMIN
}

enum ServerStatus {
  ONLINE
  OFFLINE
  MAINTENANCE
}

enum DeploymentStatus {
  PENDING
  BUILDING
  DEPLOYED
  FAILED
}
```

---

## 💻 Key Features to Implement

### 1. Authentication

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
        // Validate and return user
      },
    }),
  ],
});
```

### 2. Dashboard Page

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

### 3. Real-time Updates

```tsx
// hooks/useServerStatus.ts
import { useQuery } from '@tanstack/react-query';

export function useServerStatus() {
  return useQuery({
    queryKey: ['servers'],
    queryFn: () => fetch('/api/servers').then(r => r.json()),
    refetchInterval: 5000,  // Poll every 5 seconds
  });
}
```

---

## 🎮 Implementation Steps

1. **Setup Project**
   - `npx create-next-app@latest devops-dashboard`
   - Install dependencies
   - Setup Prisma + PostgreSQL

2. **Build Authentication**
   - Configure NextAuth
   - Create login/register forms
   - Protected routes

3. **Create Dashboard UI**
   - Layout with sidebar
   - Stats cards
   - Charts (Recharts)

4. **Implement API Routes**
   - CRUD for deployments
   - Server management
   - User settings

5. **Add Real-time Features**
   - Server status polling
   - Deployment progress
   - Notifications

6. **Testing**
   - Unit tests för komponenter
   - Integration tests för forms
   - E2E tests med Playwright

7. **Deploy**
   - Setup Vercel project
   - Configure env variables
   - Deploy och monitor

---

## ✅ Sammanfattning

Du har nu lärt dig allt du behöver för att bygga produktionsklara React/Next.js-applikationer:

- ⚛️ React fundamentals (components, state, effects)
- 🪝 Hooks och custom hooks
- 📦 State management
- 🚀 Next.js (App Router, RSC, data fetching)
- 🧪 Testing
- 🌐 Deployment

**Grattis! Du är redo att bygga professionella React-applikationer!** 🎉
""",
}


# Export all nodes from Block 5
BLOCK_5_NODES = [
    REACT_NODE_17_TESTING,
    REACT_NODE_18_STATE_MANAGEMENT,
    REACT_NODE_19_DEPLOYMENT,
    REACT_NODE_20_CAPSTONE,
]
