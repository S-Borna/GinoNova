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
    "description": "Komma igång med Next.js App Router",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "next.js", "app router", "pages router", "file-based routing",
        "project structure", "next.config.js"
    ],
    "content": """
# Next.js Introduction

> *"Next.js is React framework for production - with everything you need built-in."*

---

## 🎯 Why Next.js?

Next.js löser problem som vanilla React inte hanterar:

```
┌─────────────────────────────────────────────────────────────────┐
│                  REACT vs NEXT.JS                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Vanilla React (Vite)              Next.js                      │
│  ────────────────────              ───────                      │
│  • Client-side rendering          • Server + Client rendering   │
│  • Manual routing (react-router)  • File-based routing built-in│
│  • Manual code splitting          • Automatic code splitting    │
│  • Manual SEO                     • Built-in SEO & metadata     │
│  • Manual API setup               • API routes built-in         │
│  • Manual image optimization      • next/image optimization     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧠 Project Setup

```bash
# Skapa Next.js-projekt
npx create-next-app@latest my-app

# Välj options:
# ✔ TypeScript? Yes
# ✔ ESLint? Yes
# ✔ Tailwind CSS? Yes
# ✔ src/ directory? Yes
# ✔ App Router? Yes (VIKTIGT!)
# ✔ Turbopack? Yes

cd my-app
npm run dev
```

### Project Structure (App Router)

```bash
my-app/
├── src/
│   ├── app/                    # App Router
│   │   ├── layout.tsx          # Root layout
│   │   ├── page.tsx            # Home page (/)
│   │   ├── globals.css
│   │   ├── about/
│   │   │   └── page.tsx        # /about
│   │   ├── blog/
│   │   │   ├── page.tsx        # /blog
│   │   │   └── [slug]/
│   │   │       └── page.tsx    # /blog/my-post
│   │   └── api/
│   │       └── hello/
│   │           └── route.ts    # API: /api/hello
│   ├── components/
│   └── lib/
├── public/                      # Static files
├── next.config.js
└── package.json
```

### Root Layout

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

### Page Component

```tsx
// src/app/page.tsx
export default function HomePage() {
  return (
    <div>
      <h1>Welcome to Next.js!</h1>
      <p>This is the home page.</p>
    </div>
  );
}

// src/app/about/page.tsx
export default function AboutPage() {
  return (
    <div>
      <h1>About Us</h1>
      <p>Learn more about our company.</p>
    </div>
  );
}
```

---

## 💻 File-based Routing

```
┌─────────────────────────────────────────────────────────────────┐
│                    FILE → URL MAPPING                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  src/app/page.tsx              →  /                             │
│  src/app/about/page.tsx        →  /about                        │
│  src/app/blog/page.tsx         →  /blog                         │
│  src/app/blog/[slug]/page.tsx  →  /blog/my-post (dynamic)       │
│  src/app/shop/[...slug]/page.tsx → /shop/a/b/c (catch-all)      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Dynamic Routes

```tsx
// src/app/blog/[slug]/page.tsx
interface BlogPostProps {
  params: { slug: string };
}

export default function BlogPost({ params }: BlogPostProps) {
  return <h1>Blog Post: {params.slug}</h1>;
}

// URL: /blog/hello-world → params.slug = "hello-world"
```

---

## ✅ Sammanfattning

- **Next.js** är React-ramverket för produktion
- **App Router** är den moderna routern (från Next.js 13+)
- **File-based routing** - filstruktur = URL-struktur
- **Layouts** delas mellan sidor
- **Metadata** för SEO built-in
""",
}


# ============================================================================
# NODE 14: SERVER COMPONENTS
# ============================================================================

REACT_NODE_14_RSC = {
    "node_id": 14,
    "title": "React Server Components",
    "slug": "server-components",
    "description": "Förstå Server vs Client Components",
    "difficulty": "advanced",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "server components", "client components", "use client",
        "streaming", "suspense", "async components"
    ],
    "content": """
# React Server Components

> *"Server Components let you render components on the server - no JavaScript sent to the client."*

---

## 🎯 Why This Matters

Server Components är en paradigmskift - de reducerar JavaScript-bundle drastiskt och gör data fetching enklare.

---

## 🧠 Server vs Client Components

```
┌─────────────────────────────────────────────────────────────────┐
│              SERVER vs CLIENT COMPONENTS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SERVER COMPONENTS (default)      CLIENT COMPONENTS ('use client')│
│  ──────────────────────          ──────────────────────────────│
│  • Körs på servern               • Körs i browsern              │
│  • Ingen JS till client          • JS skickas till client       │
│  • Kan fetcha data direkt        • Använder hooks (useState)    │
│  • Kan accessa backend direkt    • Hanterar interaktivitet      │
│  • Snabbare initial load         • Event handlers               │
│  • Bättre SEO                    • Browser APIs                 │
│                                                                  │
│  ✅ Använd för:                  ✅ Använd för:                 │
│  • Statiskt content              • Interaktiva formulär         │
│  • Data fetching                 • useState, useEffect          │
│  • Markdown rendering            • onClick, onChange            │
│  • Databas-queries               • Animations                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Server Component (Default)

```tsx
// src/app/users/page.tsx
// Ingen 'use client' = Server Component

async function getUsers() {
  const res = await fetch('https://api.example.com/users', {
    cache: 'no-store' // eller 'force-cache'
  });
  return res.json();
}

export default async function UsersPage() {
  const users = await getUsers();  // Direkt async!
  
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

### Client Component

```tsx
// src/components/Counter.tsx
'use client';  // ← Gör detta till Client Component

import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);  // hooks fungerar här
  
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

### Combining Server + Client

```tsx
// src/app/dashboard/page.tsx (Server Component)
import { Counter } from '@/components/Counter';

async function getData() {
  // Server-side fetch
  return fetch('/api/stats').then(r => r.json());
}

export default async function Dashboard() {
  const stats = await getData();  // Server
  
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Total users: {stats.users}</p>  {/* Server rendered */}
      <Counter />  {/* Client Component för interaktivitet */}
    </div>
  );
}
```

---

## 💻 Streaming with Suspense

```tsx
import { Suspense } from 'react';

async function SlowComponent() {
  const data = await slowFetch();  // Tar 3 sekunder
  return <div>{data}</div>;
}

export default function Page() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<p>Loading stats...</p>}>
        <SlowComponent />  {/* Streamas när redo */}
      </Suspense>
    </div>
  );
}
```

---

## ⚠️ Vanliga Problem

```tsx
// ❌ FEL: useState i Server Component
export default function Page() {
  const [count, setCount] = useState(0);  // ERROR!
  return <div>{count}</div>;
}

// ✅ RÄTT: Markera som Client Component
'use client';
export default function Page() {
  const [count, setCount] = useState(0);  // OK!
  return <div>{count}</div>;
}
```

---

## ✅ Sammanfattning

- **Server Components** (default) - körs på servern, ingen JS till client
- **Client Components** (`'use client'`) - för interaktivitet och hooks
- **Async components** - fetcha data direkt i komponenten
- **Suspense** - streaming och loading states
- **Kombinera** server och client där det passar bäst
""",
}


# ============================================================================
# NODE 15: DATA FETCHING
# ============================================================================

REACT_NODE_15_DATA_FETCHING = {
    "node_id": 15,
    "title": "Data Fetching in Next.js",
    "slug": "nextjs-data-fetching",
    "description": "Olika sätt att hämta data i Next.js",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "fetch", "caching", "revalidation", "server actions",
        "static generation", "ISR", "dynamic rendering"
    ],
    "content": """
# Data Fetching in Next.js

> *"Next.js extends fetch with caching and revalidation superpowers."*

---

## 🎯 Why This Matters

Rätt data-fetching strategi påverkar prestanda, SEO, och användarupplevelse dramatiskt.

---

## 🧠 Fetching in Server Components

```tsx
// Static Data (cached forever)
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
  
  revalidatePath('/posts');  // Uppdatera cache
}

// src/app/posts/new/page.tsx
import { createPost } from '../actions';

export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" placeholder="Title" required />
      <textarea name="content" placeholder="Content" required />
      <button type="submit">Create Post</button>
    </form>
  );
}
```

### Server Action with useFormState

```tsx
'use client';

import { useFormState, useFormStatus } from 'react-dom';
import { createPost } from '../actions';

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Creating...' : 'Create Post'}
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

---

## 💻 Loading & Error States

```tsx
// src/app/posts/loading.tsx
export default function Loading() {
  return <div>Loading posts...</div>;
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
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

---

## ✅ Sammanfattning

- **cache: 'force-cache'** - statisk data (default)
- **cache: 'no-store'** - dynamisk data
- **next: { revalidate: N }** - ISR (Incremental Static Regeneration)
- **Server Actions** - mutate data utan API routes
- **loading.tsx/error.tsx** - automatiska loading/error states
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

> *"Next.js routing is file-system based - your folders define your URLs."*

---

## 🎯 File-based Routing Deep Dive

```
┌─────────────────────────────────────────────────────────────────┐
│                    ROUTING CONVENTIONS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Fil/Mapp                        URL                            │
│  ────────                        ───                            │
│  app/page.tsx                    /                              │
│  app/about/page.tsx              /about                         │
│  app/blog/[slug]/page.tsx        /blog/:slug                    │
│  app/shop/[...slug]/page.tsx     /shop/*                        │
│  app/[[...slug]]/page.tsx        / eller /*                     │
│  app/(group)/page.tsx            / (gruppering utan URL)        │
│  app/@modal/page.tsx             Parallel route                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Dynamic Routes

```tsx
// app/blog/[slug]/page.tsx
interface Props {
  params: { slug: string };
}

export default function BlogPost({ params }: Props) {
  return <h1>Post: {params.slug}</h1>;
}

// Generate static params för SSG
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map(post => ({ slug: post.slug }));
}
```

### Catch-all Routes

```tsx
// app/docs/[...slug]/page.tsx
interface Props {
  params: { slug: string[] };
}

export default function DocsPage({ params }: Props) {
  // /docs/getting-started → slug = ['getting-started']
  // /docs/api/users → slug = ['api', 'users']
  
  return <h1>Docs: {params.slug.join('/')}</h1>;
}
```

---

## 💻 Navigation

### Link Component

```tsx
import Link from 'next/link';

export function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/blog/hello-world">Blog Post</Link>
      
      {/* Prefetch disabled */}
      <Link href="/heavy-page" prefetch={false}>
        Heavy Page
      </Link>
      
      {/* Replace history */}
      <Link href="/new-page" replace>
        Replace Current
      </Link>
    </nav>
  );
}
```

### useRouter (Client Components)

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

### redirect (Server)

```tsx
import { redirect } from 'next/navigation';

export default async function ProtectedPage() {
  const session = await getSession();
  
  if (!session) {
    redirect('/login');  // Server-side redirect
  }
  
  return <div>Protected content</div>;
}
```

---

## 💻 Middleware

```tsx
// middleware.ts (i root)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Auth check
  const token = request.cookies.get('token');
  
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  // Add headers
  const response = NextResponse.next();
  response.headers.set('x-custom-header', 'my-value');
  
  return response;
}

// Matcha specifika paths
export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
```

---

## ✅ Sammanfattning

- **File-based routing** - mappar = URL-segment
- **Dynamic routes** `[slug]` för variabla segment
- **Catch-all** `[...slug]` för multipla segment
- **Link** för client-side navigation med prefetching
- **useRouter** för programmatisk navigation
- **Middleware** för auth, redirects, headers
""",
}


# Export all nodes from Block 4
BLOCK_4_NODES = [
    REACT_NODE_13_NEXTJS_INTRO,
    REACT_NODE_14_RSC,
    REACT_NODE_15_DATA_FETCHING,
    REACT_NODE_16_ROUTING,
]
