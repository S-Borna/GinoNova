"""
React SkillsMap - Block 4: Next.js Framework
Nodes 13-16: App Router, Server Components, Data Fetching, Routing
"""

from typing import Any

# ============================================================================
# NODE 13: NEXT.JS INTRODUCTION
# ============================================================================

REACT_NODE_13_NEXTJS_INTRO = {
    "node_id": 13,
    "title": "Next.js Introduction",
    "slug": "nextjs-introduction",
    "description": "Komma igang med Next.js App Router",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "next.js", "app router", "pages router", "file-based routing",
        "project structure", "next.config.js"
    ],
    "content": """
# Next.js Introduction

------------------------------------------------------------

## Vad ar Next.js?

Next.js ar ett React-ramverk for produktion som ger dig allt du behover inbyggt.

```
+-----------------------------------------------------------------+
|                  REACT vs NEXT.JS                                |
+-----------------------------------------------------------------+
|                                                                  |
|  Vanilla React (Vite)              Next.js                      |
|  --------------------              -------                      |
|  - Client-side rendering           - Server + Client rendering  |
|  - Manual routing (react-router)   - File-based routing inbyggt |
|  - Manual code splitting           - Automatisk code splitting  |
|  - Manual SEO                      - Inbyggd SEO & metadata     |
|  - Manual API setup                - API routes inbyggt         |
|  - Manual bildoptimering           - next/image optimering      |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| CI/CD | Next.js har forstaklassigt stod for Vercel, Netlify och containerisering |
| Performance | Inbyggd optimering minskar infrastrukturkostnader |
| SSR/SSG | Server-side rendering ger battre SEO och snabbare initial load |
| Edge Functions | Stod for edge computing nara anvandarna |
| Monitoring | Inbyggt stod for analytics och performance monitoring |

------------------------------------------------------------

## Project Setup

```bash
# Skapa Next.js-projekt
npx create-next-app@latest my-app

# Valj options:
# TypeScript? Yes
# ESLint? Yes
# Tailwind CSS? Yes
# src/ directory? Yes
# App Router? Yes (VIKTIGT!)
# Turbopack? Yes

cd my-app
npm run dev
```

### Projektstruktur (App Router)

```
+-----------------------------------------------------------------+
|                  PROJECT STRUCTURE                               |
+-----------------------------------------------------------------+
|                                                                  |
|  my-app/                                                        |
|  +-- src/                                                       |
|  |   +-- app/                     # App Router                  |
|  |   |   +-- layout.tsx           # Root layout                 |
|  |   |   +-- page.tsx             # Home page (/)               |
|  |   |   +-- globals.css                                        |
|  |   |   +-- about/                                             |
|  |   |   |   +-- page.tsx         # /about                      |
|  |   |   +-- blog/                                              |
|  |   |   |   +-- page.tsx         # /blog                       |
|  |   |   |   +-- [slug]/                                        |
|  |   |   |       +-- page.tsx     # /blog/my-post               |
|  |   |   +-- api/                                               |
|  |   |       +-- hello/                                         |
|  |   |           +-- route.ts     # API: /api/hello             |
|  |   +-- components/                                            |
|  |   +-- lib/                                                   |
|  +-- public/                       # Statiska filer             |
|  +-- next.config.js                                             |
|  +-- package.json                                               |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Root Layout

```tsx
// src/app/layout.tsx
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'My App',
  description: 'Built with Next.js',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <header>
          <nav>Navigation</nav>
        </header>
        <main>{children}</main>
        <footer>Footer</footer>
      </body>
    </html>
  );
}
```

------------------------------------------------------------

## Snabbreferens

| Koncept | Syntax | Anvandning |
|---------|--------|------------|
| Page | `page.tsx` | Definierar en route |
| Layout | `layout.tsx` | Delad layout for barn |
| Loading | `loading.tsx` | Loading UI |
| Error | `error.tsx` | Error boundary |
| Dynamic Route | `[slug]` | Variabel i URL |
| Catch-all | `[...slug]` | Multipla segment |
| Route Group | `(group)` | Organisering utan URL |

------------------------------------------------------------

## File-based Routing

```
+-----------------------------------------------------------------+
|                    FILE -> URL MAPPING                            |
+-----------------------------------------------------------------+
|                                                                  |
|  src/app/page.tsx              ->  /                             |
|  src/app/about/page.tsx        ->  /about                        |
|  src/app/blog/page.tsx         ->  /blog                         |
|  src/app/blog/[slug]/page.tsx  ->  /blog/my-post (dynamisk)      |
|  src/app/shop/[...slug]/page.tsx -> /shop/a/b/c (catch-all)      |
|                                                                  |
+-----------------------------------------------------------------+
```

### Dynamiska Routes

```tsx
// src/app/blog/[slug]/page.tsx
interface BlogPostProps {
  params: { slug: string };
}

export default function BlogPost({ params }: BlogPostProps) {
  return <h1>Blog Post: {params.slug}</h1>;
}

// URL: /blog/hello-world -> params.slug = "hello-world"
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| 404 page not found | Fil heter inte page.tsx | Byt namn till page.tsx |
| Layout renderas inte | Saknar layout.tsx i app/ | Skapa root layout.tsx |
| Metadata visas inte | metadata exporteras inte | Lagg till export const metadata |
| Hydration mismatch | Server/client renderar olika | Se till att initialt innehall matchar |
| Module not found | Fel import-path | Kontrollera src/ och alias i tsconfig |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| App Router | Moderna routing-systemet fran Next.js 13+ |
| File-based | Filstruktur = URL-struktur automatiskt |
| Layout | Delade komponenter mellan routes |
| Metadata | Inbyggt SEO-stod |
| Dynamiska routes | [slug] for variabla URL-segment |

### Kom ihag
- Next.js ar React-ramverket for produktion
- App Router ar den rekommenderade routern
- Varje page.tsx blir en route
- layout.tsx delas mellan barn-routes
- Metadata exporteras for SEO
""",
}


# ============================================================================
# NODE 14: SERVER COMPONENTS
# ============================================================================

REACT_NODE_14_RSC = {
    "node_id": 14,
    "title": "React Server Components",
    "slug": "server-components",
    "description": "Forsta Server vs Client Components",
    "difficulty": "advanced",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "server components", "client components", "use client",
        "streaming", "suspense", "async components"
    ],
    "content": """
# React Server Components

------------------------------------------------------------

## Vad ar Server Components?

Server Components lat dig rendera komponenter pa servern utan att skicka JavaScript till klienten.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Bundle Size | Drastiskt mindre JS att ladda - snabbare sidor |
| Server Load | Mer rendering pa server, planera kapacitet |
| Caching | RSC kan cachas effektivt pa CDN |
| Monitoring | Behover overvaka bade server och client metrics |
| Deployment | Kraver Node.js runtime, inte statiskt |

------------------------------------------------------------

## Server vs Client Components

```
+-----------------------------------------------------------------+
|              SERVER vs CLIENT COMPONENTS                         |
+-----------------------------------------------------------------+
|                                                                  |
|  SERVER COMPONENTS (default)      CLIENT COMPONENTS              |
|  ----------------------          ------------------------------  |
|  - Kors pa servern                - Kors i browsern              |
|  - Ingen JS till client           - JS skickas till client       |
|  - Kan fetcha data direkt         - Anvander hooks (useState)    |
|  - Kan accessa backend direkt     - Hanterar interaktivitet      |
|  - Snabbare initial load          - Event handlers               |
|  - Battre SEO                     - Browser APIs                 |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Snabbreferens

| Typ | Direktiv | Anvandning |
|-----|----------|------------|
| Server Component | (default) | Data fetching, statiskt innehall |
| Client Component | 'use client' | Hooks, events, interaktivitet |
| Async Component | async function | Direkt await i komponenten |
| Suspense | `<Suspense>` | Loading states for streaming |
| Mixed | Kombinera | Server wrapper med Client children |

------------------------------------------------------------

## Server Component Exempel

```tsx
// src/app/users/page.tsx
// Ingen 'use client' = Server Component

async function getUsers() {
  const res = await fetch('https://api.example.com/users', {
    cache: 'no-store'
  });
  return res.json();
}

export default async function UsersPage() {
  const users = await getUsers();  // Direkt async

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

------------------------------------------------------------

## Client Component Exempel

```tsx
// src/components/Counter.tsx
'use client';

import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Increment
      </button>
    </div>
  );
}
```

------------------------------------------------------------

## Kombinera Server + Client

```tsx
// src/app/dashboard/page.tsx (Server Component)
import { Counter } from '@/components/Counter';

async function getData() {
  return fetch('/api/stats').then(r => r.json());
}

export default async function Dashboard() {
  const stats = await getData();  // Server

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Total users: {stats.users}</p>
      <Counter />  {/* Client Component */}
    </div>
  );
}
```

------------------------------------------------------------

## Streaming med Suspense

```tsx
import { Suspense } from 'react';

async function SlowComponent() {
  const data = await slowFetch();
  return <div>{data}</div>;
}

export default function Page() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<p>Laddar...</p>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| useState i Server Component | Hooks fungerar inte pa server | Lagg till 'use client' |
| async i Client Component | Client components kan inte vara async | Flytta data fetching till server |
| Importing Client in Server | Fungerar - men hela tradet blir client | Var specifik med 'use client' |
| Hydration mismatch | Server/client renderar olika | Anvand useEffect for client-only kod |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Server Components | Default i App Router - ingen JS till client |
| Client Components | 'use client' for hooks och interaktivitet |
| Async Components | Fetcha data direkt med await |
| Suspense | Streaming och loading states |
| Kombinera | Server for data, Client for interaktion |

### Kom ihag
- Server Components ar default i Next.js 13+
- Lagg till 'use client' endast nar du behover hooks
- Haller JavaScript-bundle minimal
- Suspense mojliggor progressiv rendering
- Kombinera bada for optimal prestanda
""",
}


# ============================================================================
# NODE 15: DATA FETCHING
# ============================================================================

REACT_NODE_15_DATA_FETCHING = {
    "node_id": 15,
    "title": "Data Fetching in Next.js",
    "slug": "nextjs-data-fetching",
    "description": "Olika satt att hamta data i Next.js",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "fetch", "caching", "revalidation", "server actions",
        "static generation", "ISR", "dynamic rendering"
    ],
    "content": """
# Data Fetching in Next.js

------------------------------------------------------------

## Vad ar Data Fetching i Next.js?

Next.js utvidgar fetch med kraftfulla caching- och revalideringsfunktioner.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Caching | Minskar API-anrop och serverbelastning |
| ISR | Incremental Static Regeneration - balans mellan statiskt och dynamiskt |
| CDN | Statisk data kan distribueras globalt |
| Monitoring | Spara latency och cache hit rates |
| Kostnader | Ratt strategi minskar infrastrukturkostnader |

------------------------------------------------------------

## Snabbreferens

| Strategi | Cache Option | Anvandning |
|----------|--------------|------------|
| Static | `cache: 'force-cache'` | Data som aldrig andras |
| Dynamic | `cache: 'no-store'` | Alltid farsk data |
| ISR | `next: { revalidate: 60 }` | Revalidera efter N sekunder |
| On-demand | `revalidatePath()` | Manuell revalidering |

------------------------------------------------------------

## Fetching i Server Components

```tsx
// Static Data (cachad for alltid)
async function getStaticData() {
  const res = await fetch('https://api.example.com/posts', {
    cache: 'force-cache'  // Default - statiskt
  });
  return res.json();
}

// Dynamic Data (no cache)
async function getDynamicData() {
  const res = await fetch('https://api.example.com/posts', {
    cache: 'no-store'  // Alltid färsk data
  });
  return res.json();
}

// Revalidate every 60 seconds (ISR)
async function getRevalidatedData() {
  const res = await fetch('https://api.example.com/posts', {
    next: { revalidate: 60 }  // Revalidera efter 60 sek
  });
  return res.json();
}
```

### Direct Database Access

```tsx
// src/app/users/page.tsx
import { db } from '@/lib/db';

export default async function UsersPage() {
  // Direkt databas-query i Server Component!
  const users = await db.user.findMany();

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

---

## 💻 Server Actions

Mutate data utan API routes:

------------------------------------------------------------

## Server Actions

Mutera data utan API routes:

```tsx
// src/app/actions.ts
'use server';

import { db } from '@/lib/db';
import { revalidatePath } from 'next/cache';

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string;
  const content = formData.get('content') as string;

  await db.post.create({
    data: { title, content }
  });

  revalidatePath('/posts');
}

// src/app/posts/new/page.tsx
import { createPost } from '../actions';

export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" placeholder="Titel" required />
      <textarea name="content" placeholder="Innehall" required />
      <button type="submit">Skapa Post</button>
    </form>
  );
}
```

------------------------------------------------------------

## useFormState for Feedback

```tsx
'use client';

import { useFormState, useFormStatus } from 'react-dom';
import { createPost } from '../actions';

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Skapar...' : 'Skapa Post'}
    </button>
  );
}

export default function NewPostForm() {
  const [state, action] = useFormState(createPost, { error: null });

  return (
    <form action={action}>
      {state.error && <p className="error">{state.error}</p>}
      <input name="title" required />
      <textarea name="content" required />
      <SubmitButton />
    </form>
  );
}
```

------------------------------------------------------------

## Loading och Error States

```tsx
// src/app/posts/loading.tsx
export default function Loading() {
  return <div>Laddar inlagg...</div>;
}

// src/app/posts/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Nagot gick fel!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Forsok igen</button>
    </div>
  );
}
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Stale data efter mutation | Glom revalidatePath | Lagg till revalidatePath('/path') |
| Cache uppdateras inte | Fel cache-strategi | Anvand no-store for dynamisk data |
| Server Action fungerar inte | Saknar 'use server' | Lagg till 'use server' i filen |
| Form submittar ej | action ar inte async | Kontrollera Server Action signaturen |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| force-cache | Statisk data, cachad permanent |
| no-store | Dynamisk data, hamtas varje gang |
| revalidate | ISR - uppdateras efter N sekunder |
| Server Actions | Mutera data utan API routes |
| loading.tsx | Automatisk loading UI |

### Kom ihag
- Valj caching-strategi baserat pa data-behov
- ISR ar bra for innehall som uppdateras sallsynt
- Server Actions forenklar data mutations
- loading.tsx och error.tsx ger automatiska UI states
- revalidatePath() for manuell cache-invalidering
""",
}


# ============================================================================
# NODE 16: ROUTING & NAVIGATION
# ============================================================================

REACT_NODE_16_ROUTING = {
    "node_id": 16,
    "title": "Routing & Navigation",
    "slug": "nextjs-routing",
    "description": "Avancerad routing i Next.js",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "dynamic routes", "catch-all routes", "parallel routes",
        "intercepting routes", "middleware", "Link", "useRouter"
    ],
    "content": """
# Routing & Navigation

------------------------------------------------------------

## Vad ar Routing i Next.js?

Next.js routing ar filsystemsbaserat - dina mappar definierar dina URL:er.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| URL Design | Rena URLs forbattrar SEO och anvandbarhet |
| Auth | Middleware skyddar routes pa edge |
| Performance | Link prefetchar for snabb navigation |
| Redirects | Hanteras i middleware eller config |
| A/B Testing | Middleware mojliggor route-baserad testing |

------------------------------------------------------------

## Snabbreferens

| Pattern | Syntax | Exempel URL |
|---------|--------|-------------|
| Static | `page.tsx` | /about |
| Dynamic | `[slug]` | /blog/hello-world |
| Catch-all | `[...slug]` | /docs/a/b/c |
| Optional | `[[...slug]]` | / eller /a/b |
| Group | `(group)` | (paverkar inte URL) |
| Parallel | `@modal` | Renderas parallellt |

------------------------------------------------------------

## Routing Conventions

```
+-----------------------------------------------------------------+
|                    ROUTING CONVENTIONS                           |
+-----------------------------------------------------------------+
|                                                                  |
|  Fil/Mapp                        URL                            |
|  --------                        ---                            |
|  app/page.tsx                    /                              |
|  app/about/page.tsx              /about                         |
|  app/blog/[slug]/page.tsx        /blog/:slug                    |
|  app/shop/[...slug]/page.tsx     /shop/*                        |
|  app/[[...slug]]/page.tsx        / eller /*                     |
|  app/(group)/page.tsx            / (gruppering utan URL)        |
|  app/@modal/page.tsx             Parallel route                 |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Dynamiska Routes

```tsx
// app/blog/[slug]/page.tsx
interface Props {
  params: { slug: string };
}

export default function BlogPost({ params }: Props) {
  return <h1>Post: {params.slug}</h1>;
}

// Generate static params for SSG
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map(post => ({ slug: post.slug }));
}
```

------------------------------------------------------------

## Catch-all Routes

```tsx
// app/docs/[...slug]/page.tsx
interface Props {
  params: { slug: string[] };
}

export default function DocsPage({ params }: Props) {
  // /docs/getting-started -> slug = ['getting-started']
  // /docs/api/users -> slug = ['api', 'users']

  return <h1>Docs: {params.slug.join('/')}</h1>;
}
```

------------------------------------------------------------

## Navigation med Link

```tsx
import Link from 'next/link';

export function Navigation() {
  return (
    <nav>
      <Link href="/">Hem</Link>
      <Link href="/about">Om oss</Link>
      <Link href="/blog/hello-world">Blogginlagg</Link>

      {/* Prefetch avstangd */}
      <Link href="/heavy-page" prefetch={false}>
        Tung Sida
      </Link>

      {/* Ersatt historik */}
      <Link href="/new-page" replace>
        Ersatt Nuvarande
      </Link>
    </nav>
  );
}
```

------------------------------------------------------------

## useRouter (Client Components)

```tsx
'use client';

import { useRouter, usePathname, useSearchParams } from 'next/navigation';

export function SearchForm() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const handleSearch = (query: string) => {
    const params = new URLSearchParams(searchParams);
    params.set('q', query);
    router.push(`${pathname}?${params.toString()}`);
  };

  return (
    <input
      defaultValue={searchParams.get('q') ?? ''}
      onChange={(e) => handleSearch(e.target.value)}
    />
  );
}
```

------------------------------------------------------------

## Server Redirect

```tsx
import { redirect } from 'next/navigation';

export default async function ProtectedPage() {
  const session = await getSession();

  if (!session) {
    redirect('/login');
  }

  return <div>Skyddat innehall</div>;
}
```

------------------------------------------------------------

## Middleware

```tsx
// middleware.ts (i root)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  const response = NextResponse.next();
  response.headers.set('x-custom-header', 'my-value');

  return response;
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Link prefetchar for mycket | Default beteende | Satt prefetch={false} |
| useRouter i Server Component | Hook fungerar inte pa server | Anvand redirect() istallet |
| Middleware kors inte | Fel plats eller matcher | Lagg middleware.ts i root |
| Dynamisk route matchar inte | Fel mappstruktur | Kontrollera [slug] syntax |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| File-based | Mappar = URL-segment automatiskt |
| [slug] | Dynamiska routes med parametrar |
| [...slug] | Catch-all for multipla segment |
| Link | Client-side navigation med prefetch |
| Middleware | Edge-baserad auth och redirects |

### Kom ihag
- Filsystemet definierar URL-strukturen
- Link-komponenten ger snabb navigation
- useRouter for programmatisk navigation i client
- redirect() for server-side redirects
- Middleware kors pa edge for bast prestanda
""",
}


# Export all nodes from Block 4
BLOCK_4_NODES = [
    REACT_NODE_13_NEXTJS_INTRO,
    REACT_NODE_14_RSC,
    REACT_NODE_15_DATA_FETCHING,
    REACT_NODE_16_ROUTING,
]
