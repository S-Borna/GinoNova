"""
React SkillsMap - Block 1: Fundamentals
Nodes 1-4: Introduction, JSX, Components, Props
"""

from typing import Any

# ============================================================================
# NODE 1: REACT INTRODUCTION & SETUP
# ============================================================================

REACT_NODE_01_INTRODUCTION = {
    "node_id": 1,
    "title": "React Introduction & Setup",
    "slug": "react-introduction",
    "description": "Förstå React och sätt upp din utvecklingsmiljö",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 80,
    "topics_covered": [
        "react", "vite", "create-react-app", "jsx", "virtual dom",
        "component", "rendering", "npm", "yarn", "pnpm"
    ],
    "content": """
# React Introduction & Setup

> *"React changed how we think about UI. Instead of manipulating the DOM, we describe what we want to see."*

---

## 🎯 Why This Matters

React är världens mest populära frontend-bibliotek:

- **Facebook, Instagram, Netflix, Airbnb** använder React
- **95% av Fortune 500** har React i sin tech stack
- **Job market:** React-utvecklare är efterfrågade och välbetalda
- **Ekosystem:** Next.js, React Native, Remix - alla bygger på React

Som utvecklare kommer du att:
- Bygga interaktiva användargränssnitt
- Skapa återanvändbara komponenter
- Hantera komplex applikationsstate
- Optimera prestanda för miljontals användare

---

## 🧠 Core Concepts

### Vad är React?

React är ett **deklarativt** UI-bibliotek. Istället för att säga *hur* UI ska uppdateras, beskriver du *vad* du vill se:

```
┌─────────────────────────────────────────────────────────────────┐
│                    IMPERATIV vs DEKLARATIV                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IMPERATIV (vanilla JS):              DEKLARATIV (React):       │
│  ─────────────────────                ────────────────────      │
│  const btn = document.                function Counter() {      │
│    createElement('button');             const [count, setCount] │
│  btn.textContent = count;               = useState(0);         │
│  btn.onclick = () => {                  return (               │
│    count++;                               <button onClick={     │
│    btn.textContent = count;                () => setCount(c+1) │
│  };                                       }>                    │
│  document.body.appendChild(btn);           {count}              │
│                                          </button>              │
│                                        );                       │
│                                       }                         │
└─────────────────────────────────────────────────────────────────┘
```

### Virtual DOM

React använder en **Virtual DOM** för effektiva uppdateringar:

```
┌─────────────────────────────────────────────────────────────────┐
│                     REACT RENDERING CYCLE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. State ändras                                                │
│     │                                                           │
│     ▼                                                           │
│  2. React skapar ny Virtual DOM                                 │
│     │                                                           │
│     ▼                                                           │
│  3. Diffing: Jämför gammal vs ny Virtual DOM                    │
│     │                                                           │
│     ▼                                                           │
│  4. Reconciliation: Beräkna minimala ändringar                  │
│     │                                                           │
│     ▼                                                           │
│  5. Commit: Uppdatera bara det som ändrats i riktiga DOM        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Setup & Installation

### Alternativ 1: Vite (Rekommenderat 2024+)

```bash
# Skapa nytt React-projekt med Vite
npm create vite@latest my-react-app -- --template react-ts

# Navigera och installera
cd my-react-app
npm install

# Starta utvecklingsserver
npm run dev
```

### Alternativ 2: Next.js (Fullstack)

```bash
# Skapa Next.js-app (App Router)
npx create-next-app@latest my-nextjs-app

# Välj options:
# ✔ TypeScript? Yes
# ✔ ESLint? Yes
# ✔ Tailwind CSS? Yes
# ✔ src/ directory? Yes
# ✔ App Router? Yes

cd my-nextjs-app
npm run dev
```

### Projektstruktur (Vite)

```bash
my-react-app/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   │   └── react.svg
│   ├── App.tsx           # Huvudkomponent
│   ├── App.css           # Styles
│   ├── main.tsx          # Entry point
│   └── index.css         # Global CSS
├── index.html            # HTML template
├── package.json
├── tsconfig.json
└── vite.config.ts
```

### Din första React-komponent

```tsx
// src/App.tsx
function App() {
  return (
    <div className="app">
      <h1>Hello, React! 🚀</h1>
      <p>Welcome to your first React application.</p>
    </div>
  );
}

export default App;
```

### Entry Point

```tsx
// src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

---

## ⚠️ Vanliga Problem

### Problem 1: "Cannot find module 'react'"

```bash
# Lösning: Installera dependencies
npm install

# Eller specifikt
npm install react react-dom
```

### Problem 2: Port redan upptagen

```bash
# Vite: Ändra port i vite.config.ts
export default defineConfig({
  server: {
    port: 3001
  }
});

# Eller använd --port flag
npm run dev -- --port 3001
```

### Problem 3: TypeScript errors

```bash
# Se till att tsconfig.json har rätt jsx setting
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "strict": true
  }
}
```

---

## 🎮 Praktisk Övning

**Uppgift:** Sätt upp ett React-projekt och skapa en välkomstkomponent.

1. Skapa projekt med Vite:
   ```bash
   npm create vite@latest devops-dashboard -- --template react-ts
   cd devops-dashboard
   npm install
   ```

2. Modifiera `src/App.tsx`:
   ```tsx
   function App() {
     const features = ['CI/CD', 'Docker', 'Kubernetes', 'Terraform'];
     
     return (
       <div className="dashboard">
         <h1>DevOps Dashboard 🛠️</h1>
         <ul>
           {features.map(f => <li key={f}>{f}</li>)}
         </ul>
       </div>
     );
   }
   
   export default App;
   ```

3. Starta och verifiera:
   ```bash
   npm run dev
   # Öppna http://localhost:5173
   ```

---

## ✅ Sammanfattning

- React är ett **deklarativt** UI-bibliotek för att bygga komponentbaserade gränssnitt
- **Virtual DOM** möjliggör effektiva UI-uppdateringar
- **Vite** är det moderna valet för React-projekt
- **Next.js** lägger till server-rendering och routing
- React använder **JSX** - JavaScript med HTML-liknande syntax
""",
}


# ============================================================================
# NODE 2: JSX - JAVASCRIPT XML
# ============================================================================

REACT_NODE_02_JSX = {
    "node_id": 2,
    "title": "JSX - JavaScript XML",
    "slug": "jsx-syntax",
    "description": "Behärska JSX-syntax och dynamiska uttryck",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "jsx", "expressions", "attributes", "children", "fragments",
        "conditional rendering", "lists", "keys", "className"
    ],
    "content": """
# JSX - JavaScript XML

> *"JSX is just syntax sugar. Under the hood, it's all JavaScript."*

---

## 🎯 Why This Matters

JSX är hjärtat av React. Det låter dig skriva UI på ett intuitivt sätt som kombinerar HTML och JavaScript. Varje React-utvecklare måste behärska JSX.

---

## 🧠 Core Concepts

### Vad är JSX?

JSX är en syntaxextension för JavaScript som låter dig skriva HTML-liknande kod:

```tsx
// JSX
const element = <h1>Hello, World!</h1>;

// Kompileras till (av Babel/TypeScript):
const element = React.createElement('h1', null, 'Hello, World!');
```

### JSX Expressions

Du kan använda JavaScript-uttryck inom `{}`:

```tsx
function Greeting() {
  const name = "DevOps Engineer";
  const time = new Date().getHours();
  
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>Current hour: {time}</p>
      <p>2 + 2 = {2 + 2}</p>
      <p>Uppercase: {name.toUpperCase()}</p>
    </div>
  );
}
```

### JSX Attributes

Attribut i JSX använder camelCase:

```tsx
function StyledButton() {
  return (
    <button
      className="btn-primary"      // inte "class"!
      onClick={() => alert('Hi')}  // inte "onclick"
      disabled={false}
      tabIndex={0}
      style={{ 
        backgroundColor: 'blue',   // CSS i JS = camelCase
        fontSize: '16px' 
      }}
    >
      Click me
    </button>
  );
}
```

### Conditional Rendering

```tsx
function UserStatus({ isLoggedIn }: { isLoggedIn: boolean }) {
  // Ternary operator
  return (
    <div>
      {isLoggedIn ? (
        <p>Welcome back!</p>
      ) : (
        <p>Please sign in</p>
      )}
    </div>
  );
}

// && operator (om true, visa)
function Notifications({ count }: { count: number }) {
  return (
    <div>
      {count > 0 && <span className="badge">{count}</span>}
    </div>
  );
}
```

### Lists & Keys

```tsx
interface Task {
  id: string;
  title: string;
  completed: boolean;
}

function TaskList({ tasks }: { tasks: Task[] }) {
  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>  {/* Key är obligatoriskt! */}
          {task.completed ? '✅' : '⬜'} {task.title}
        </li>
      ))}
    </ul>
  );
}
```

### Fragments

När du behöver returnera flera element utan en wrapper:

```tsx
function Profile() {
  return (
    <>
      <h1>User Profile</h1>
      <p>Details here</p>
    </>
  );
}

// Eller med explicit Fragment (för key i lists)
import { Fragment } from 'react';

function Items({ items }) {
  return items.map(item => (
    <Fragment key={item.id}>
      <dt>{item.title}</dt>
      <dd>{item.description}</dd>
    </Fragment>
  ));
}
```

---

## 💻 Advanced JSX Patterns

### Spread Attributes

```tsx
interface ButtonProps {
  variant: 'primary' | 'secondary';
  size: 'sm' | 'md' | 'lg';
}

function Button({ variant, size, ...rest }: ButtonProps & React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button 
      className={`btn btn-${variant} btn-${size}`}
      {...rest}  // Spread alla andra props (onClick, disabled, etc.)
    />
  );
}

// Användning
<Button variant="primary" size="md" onClick={() => {}} disabled>
  Submit
</Button>
```

### Dynamic Tag Names

```tsx
type HeadingLevel = 1 | 2 | 3 | 4 | 5 | 6;

function Heading({ level, children }: { level: HeadingLevel; children: React.ReactNode }) {
  const Tag = `h${level}` as keyof JSX.IntrinsicElements;
  return <Tag>{children}</Tag>;
}

// Användning
<Heading level={1}>Main Title</Heading>
<Heading level={2}>Subtitle</Heading>
```

---

## ⚠️ Vanliga Problem

### Problem 1: Adjacent JSX elements

```tsx
// ❌ FEL - Måste ha en wrapper
function Bad() {
  return (
    <h1>Title</h1>
    <p>Content</p>
  );
}

// ✅ RÄTT - Använd Fragment
function Good() {
  return (
    <>
      <h1>Title</h1>
      <p>Content</p>
    </>
  );
}
```

### Problem 2: class vs className

```tsx
// ❌ FEL
<div class="container">

// ✅ RÄTT
<div className="container">
```

### Problem 3: Keys in lists

```tsx
// ❌ FEL - Använd inte index som key om listan kan ändras
{items.map((item, index) => (
  <li key={index}>{item}</li>
))}

// ✅ RÄTT - Använd unikt ID
{items.map(item => (
  <li key={item.id}>{item.title}</li>
))}
```

---

## 🎮 Praktisk Övning

**Uppgift:** Bygg en enkel profil-komponent med JSX.

```tsx
interface User {
  name: string;
  role: string;
  avatar: string;
  skills: string[];
  isOnline: boolean;
}

function ProfileCard({ user }: { user: User }) {
  return (
    <article className="profile-card">
      <img 
        src={user.avatar} 
        alt={`${user.name}'s avatar`}
        className="avatar"
      />
      <h2>{user.name}</h2>
      <p className="role">{user.role}</p>
      
      {user.isOnline && (
        <span className="status online">● Online</span>
      )}
      
      <h3>Skills</h3>
      <ul className="skills">
        {user.skills.map(skill => (
          <li key={skill} className="skill-tag">
            {skill}
          </li>
        ))}
      </ul>
    </article>
  );
}

// Användning
const devOpsEngineer: User = {
  name: "Alex",
  role: "Senior DevOps Engineer",
  avatar: "/avatar.png",
  skills: ["Docker", "Kubernetes", "Terraform", "AWS"],
  isOnline: true
};

<ProfileCard user={devOpsEngineer} />
```

---

## ✅ Sammanfattning

- **JSX** är syntax sugar som kompileras till `React.createElement()`
- Använd `{}` för JavaScript-uttryck
- **className** istället för class, **camelCase** för attribut
- **Key** är obligatoriskt i listor för Reacts diffing-algoritm
- **Fragments** (`<>...</>`) för att gruppera utan extra DOM-element
- **Conditional rendering** med ternary (`? :`) eller `&&`
""",
}


# ============================================================================
# NODE 3: COMPONENTS - BUILDING BLOCKS
# ============================================================================

REACT_NODE_03_COMPONENTS = {
    "node_id": 3,
    "title": "Components - Building Blocks",
    "slug": "react-components",
    "description": "Förstå och skapa React-komponenter",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "function components", "class components", "component composition",
        "reusability", "separation of concerns", "component tree"
    ],
    "content": """
# Components - Building Blocks

> *"Components let you split the UI into independent, reusable pieces."*

---

## 🎯 Why This Matters

Komponenter är Reacts DNA. En modern React-app består av hundratals komponenter som arbetar tillsammans. Att designa bra komponenter är nyckeln till underhållbar kod.

---

## 🧠 Core Concepts

### Vad är en komponent?

En komponent är en funktion som returnerar JSX:

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPONENT ANATOMY                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  function Button({ label, onClick }) {  // Props (input)        │
│    const [clicked, setClicked] = useState(false);  // State     │
│                                                                  │
│    const handleClick = () => {  // Event handler                │
│      setClicked(true);                                          │
│      onClick?.();                                                │
│    };                                                           │
│                                                                  │
│    return (                    // JSX (output)                  │
│      <button onClick={handleClick}>                             │
│        {label}                                                  │
│      </button>                                                  │
│    );                                                           │
│  }                                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Function Components

Moderna React använder nästan uteslutande function components:

```tsx
// Simple component
function Greeting() {
  return <h1>Hello!</h1>;
}

// Arrow function variant
const Greeting = () => <h1>Hello!</h1>;

// With TypeScript types
interface GreetingProps {
  name: string;
}

function Greeting({ name }: GreetingProps) {
  return <h1>Hello, {name}!</h1>;
}
```

### Component Composition

Bygg komplexa UI genom att kombinera enkla komponenter:

```tsx
// Small, focused components
function Avatar({ src, alt }: { src: string; alt: string }) {
  return <img src={src} alt={alt} className="avatar" />;
}

function UserInfo({ name, role }: { name: string; role: string }) {
  return (
    <div className="user-info">
      <h3>{name}</h3>
      <p>{role}</p>
    </div>
  );
}

// Composed component
function UserCard({ user }: { user: User }) {
  return (
    <article className="user-card">
      <Avatar src={user.avatar} alt={user.name} />
      <UserInfo name={user.name} role={user.role} />
    </article>
  );
}

// Page-level composition
function TeamPage({ members }: { members: User[] }) {
  return (
    <main>
      <h1>Our Team</h1>
      <div className="team-grid">
        {members.map(member => (
          <UserCard key={member.id} user={member} />
        ))}
      </div>
    </main>
  );
}
```

### Component Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                     COMPONENT TREE EXAMPLE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                          App                                     │
│                           │                                      │
│         ┌─────────────────┼─────────────────┐                   │
│         │                 │                 │                    │
│      Header            Main             Footer                   │
│         │                 │                                      │
│    ┌────┴────┐      ┌────┴────┐                                 │
│    │         │      │         │                                  │
│   Logo    NavBar  Sidebar   Content                             │
│              │                 │                                 │
│         ┌────┴────┐       ArticleList                           │
│         │         │           │                                  │
│      NavItem  NavItem    ArticleCard                            │
│                              │                                   │
│                         ┌────┴────┐                              │
│                         │         │                              │
│                       Title    Summary                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Component Patterns

### Container vs Presentation

```tsx
// Presentation component (dumb) - bara UI
function TaskItem({ task, onToggle }: { 
  task: Task; 
  onToggle: (id: string) => void 
}) {
  return (
    <li onClick={() => onToggle(task.id)}>
      {task.completed ? '✅' : '⬜'} {task.title}
    </li>
  );
}

// Container component (smart) - logik och data
function TaskListContainer() {
  const [tasks, setTasks] = useState<Task[]>([]);
  
  useEffect(() => {
    fetchTasks().then(setTasks);
  }, []);
  
  const handleToggle = (id: string) => {
    setTasks(tasks.map(t => 
      t.id === id ? { ...t, completed: !t.completed } : t
    ));
  };
  
  return (
    <ul>
      {tasks.map(task => (
        <TaskItem key={task.id} task={task} onToggle={handleToggle} />
      ))}
    </ul>
  );
}
```

### Compound Components

```tsx
// Flexible card with compound components
function Card({ children }: { children: React.ReactNode }) {
  return <div className="card">{children}</div>;
}

Card.Header = function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="card-header">{children}</div>;
};

Card.Body = function CardBody({ children }: { children: React.ReactNode }) {
  return <div className="card-body">{children}</div>;
};

Card.Footer = function CardFooter({ children }: { children: React.ReactNode }) {
  return <div className="card-footer">{children}</div>;
};

// Användning - flexibel struktur
<Card>
  <Card.Header>
    <h2>Server Status</h2>
  </Card.Header>
  <Card.Body>
    <p>All systems operational</p>
  </Card.Body>
  <Card.Footer>
    <button>View Details</button>
  </Card.Footer>
</Card>
```

---

## ⚠️ Vanliga Problem

### Problem 1: Components måste börja med stor bokstav

```tsx
// ❌ FEL - lowercase tolkas som HTML-element
function button() {
  return <button>Click</button>;
}
<button />  // Renderar <button></button>, inte komponenten!

// ✅ RÄTT
function Button() {
  return <button>Click</button>;
}
<Button />
```

### Problem 2: Render måste returnera ett element

```tsx
// ❌ FEL
function Bad() {
  // Returnerar inget
}

// ✅ RÄTT
function Good() {
  return null;  // OK att returnera null
}
```

---

## 🎮 Praktisk Övning

Bygg en DevOps Dashboard med komponenter:

```tsx
// components/MetricCard.tsx
interface MetricCardProps {
  title: string;
  value: string | number;
  trend?: 'up' | 'down' | 'stable';
  icon: string;
}

function MetricCard({ title, value, trend, icon }: MetricCardProps) {
  const trendColors = {
    up: 'text-green-500',
    down: 'text-red-500',
    stable: 'text-gray-500'
  };

  return (
    <div className="metric-card">
      <span className="icon">{icon}</span>
      <h3>{title}</h3>
      <p className="value">{value}</p>
      {trend && (
        <span className={trendColors[trend]}>
          {trend === 'up' ? '↑' : trend === 'down' ? '↓' : '→'}
        </span>
      )}
    </div>
  );
}

// components/Dashboard.tsx
function Dashboard() {
  const metrics = [
    { title: 'Deployments', value: 142, trend: 'up' as const, icon: '🚀' },
    { title: 'Uptime', value: '99.9%', trend: 'stable' as const, icon: '✅' },
    { title: 'Errors', value: 3, trend: 'down' as const, icon: '❌' },
    { title: 'Build Time', value: '2m 34s', trend: 'up' as const, icon: '⏱️' },
  ];

  return (
    <main className="dashboard">
      <h1>DevOps Dashboard</h1>
      <div className="metrics-grid">
        {metrics.map(metric => (
          <MetricCard key={metric.title} {...metric} />
        ))}
      </div>
    </main>
  );
}
```

---

## ✅ Sammanfattning

- **Komponenter** är återanvändbara UI-bygglodsar
- Använd **function components** (inte class components)
- **Composition** > Inheritance - bygg komplext från enkelt
- Följ **Single Responsibility Principle** - en komponent gör en sak
- **PascalCase** för komponentnamn
""",
}


# ============================================================================
# NODE 4: PROPS - COMPONENT COMMUNICATION
# ============================================================================

REACT_NODE_04_PROPS = {
    "node_id": 4,
    "title": "Props - Component Communication",
    "slug": "react-props",
    "description": "Data flow med props och prop patterns",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "props", "children", "default props", "prop types",
        "typescript interfaces", "destructuring", "prop drilling"
    ],
    "content": """
# Props - Component Communication

> *"Props are how data flows down the component tree. They're React's main mechanism for composition."*

---

## 🎯 Why This Matters

Props (properties) är hur komponenter kommunicerar. Att förstå props är fundamentalt för att bygga React-appar.

---

## 🧠 Core Concepts

### Data Flow i React

React har **unidirectional data flow** - data flödar nedåt:

```
┌─────────────────────────────────────────────────────────────────┐
│                    UNIDIRECTIONAL DATA FLOW                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                        Parent                                    │
│                     [state: user]                                │
│                          │                                       │
│                    props │                                       │
│                          ▼                                       │
│         ┌────────────────┴────────────────┐                     │
│         │                                 │                      │
│         ▼                                 ▼                      │
│      Child A                          Child B                    │
│   <Avatar user={user} />          <Profile user={user} />       │
│                                                                  │
│  ⚠️ Children kan INTE ändra parent's state direkt!              │
│  ✅ Istället: Parent skickar callback functions via props       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Basic Props

```tsx
// Definiera props med TypeScript interface
interface WelcomeProps {
  name: string;
  age?: number;  // Optional prop
}

function Welcome({ name, age }: WelcomeProps) {
  return (
    <div>
      <h1>Welcome, {name}!</h1>
      {age && <p>You are {age} years old</p>}
    </div>
  );
}

// Användning
<Welcome name="Alex" />
<Welcome name="Sam" age={28} />
```

### Children Prop

`children` är en speciell prop för nested content:

```tsx
interface CardProps {
  title: string;
  children: React.ReactNode;  // Accepterar JSX
}

function Card({ title, children }: CardProps) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <div className="card-content">
        {children}
      </div>
    </div>
  );
}

// Användning - allt mellan öppnings/stängningstaggen blir children
<Card title="Server Status">
  <p>All systems operational</p>
  <ul>
    <li>API: ✅</li>
    <li>Database: ✅</li>
    <li>Cache: ✅</li>
  </ul>
</Card>
```

### Default Props

```tsx
interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
}

function Button({ 
  label, 
  variant = 'primary',  // Default value
  size = 'md' 
}: ButtonProps) {
  return (
    <button className={`btn btn-${variant} btn-${size}`}>
      {label}
    </button>
  );
}

// Alla dessa är giltiga
<Button label="Submit" />
<Button label="Cancel" variant="secondary" />
<Button label="Delete" variant="danger" size="sm" />
```

### Callback Props

Skicka funktioner för child-to-parent communication:

```tsx
interface SearchProps {
  onSearch: (query: string) => void;
  placeholder?: string;
}

function SearchInput({ onSearch, placeholder = "Search..." }: SearchProps) {
  const [value, setValue] = useState('');
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(value);  // Anropa parent's funktion
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder={placeholder}
      />
      <button type="submit">Search</button>
    </form>
  );
}

// Parent component
function App() {
  const handleSearch = (query: string) => {
    console.log('Searching for:', query);
    // Gör API-anrop etc.
  };
  
  return <SearchInput onSearch={handleSearch} />;
}
```

---

## 💻 Advanced Patterns

### Render Props

```tsx
interface DataFetcherProps<T> {
  url: string;
  render: (data: T | null, loading: boolean, error: Error | null) => React.ReactNode;
}

function DataFetcher<T>({ url, render }: DataFetcherProps<T>) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  
  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);
  
  return <>{render(data, loading, error)}</>;
}

// Användning
<DataFetcher<User[]> 
  url="/api/users"
  render={(users, loading, error) => {
    if (loading) return <Spinner />;
    if (error) return <Error message={error.message} />;
    return <UserList users={users!} />;
  }}
/>
```

### Props Spreading

```tsx
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
}

function Input({ label, error, ...inputProps }: InputProps) {
  return (
    <div className="form-field">
      <label>{label}</label>
      <input {...inputProps} className={error ? 'error' : ''} />
      {error && <span className="error-message">{error}</span>}
    </div>
  );
}

// Alla standard input-attribut fungerar
<Input 
  label="Email"
  type="email"
  required
  placeholder="Enter email"
  error="Invalid email format"
/>
```

---

## ⚠️ Vanliga Problem

### Problem 1: Props är read-only

```tsx
// ❌ FEL - Mutera aldrig props
function Bad({ user }: { user: User }) {
  user.name = "Changed";  // ALDRIG göra detta!
  return <p>{user.name}</p>;
}

// ✅ RÄTT - Be parent uppdatera via callback
function Good({ user, onUpdate }: { user: User; onUpdate: (u: User) => void }) {
  const handleChange = () => {
    onUpdate({ ...user, name: "Changed" });
  };
  return <button onClick={handleChange}>Change Name</button>;
}
```

### Problem 2: Prop Drilling

```tsx
// ❌ Problem: Skicka props genom många nivåer
<App user={user}>
  <Layout user={user}>
    <Sidebar user={user}>
      <UserMenu user={user} />  // Äntligen används!
    </Sidebar>
  </Layout>
</App>

// ✅ Lösning: Context (nästa modul) eller composition
<App>
  <Layout sidebar={<Sidebar><UserMenu user={user} /></Sidebar>}>
    <MainContent />
  </Layout>
</App>
```

---

## 🎮 Praktisk Övning

Bygg ett flexibelt Alert-system:

```tsx
interface AlertProps {
  type: 'success' | 'warning' | 'error' | 'info';
  title: string;
  message?: string;
  onDismiss?: () => void;
  children?: React.ReactNode;
}

function Alert({ type, title, message, onDismiss, children }: AlertProps) {
  const icons = {
    success: '✅',
    warning: '⚠️',
    error: '❌',
    info: 'ℹ️'
  };
  
  const colors = {
    success: 'bg-green-100 border-green-500',
    warning: 'bg-yellow-100 border-yellow-500',
    error: 'bg-red-100 border-red-500',
    info: 'bg-blue-100 border-blue-500'
  };
  
  return (
    <div className={`alert ${colors[type]}`} role="alert">
      <span className="alert-icon">{icons[type]}</span>
      <div className="alert-content">
        <strong>{title}</strong>
        {message && <p>{message}</p>}
        {children}
      </div>
      {onDismiss && (
        <button onClick={onDismiss} className="alert-dismiss">
          ×
        </button>
      )}
    </div>
  );
}

// Användning
<Alert 
  type="success" 
  title="Deployment Complete!"
  message="Version 2.3.1 is now live"
  onDismiss={() => setShowAlert(false)}
/>

<Alert type="error" title="Build Failed">
  <ul>
    <li>TypeScript error in src/App.tsx</li>
    <li>Missing dependency: react-query</li>
  </ul>
</Alert>
```

---

## ✅ Sammanfattning

- **Props** flödar nedåt (parent → child)
- **children** är en speciell prop för nested JSX
- **Default values** med `=` i destructuring
- **Callback props** för child → parent communication
- **Props är immutable** - mutera aldrig!
- Undvik **prop drilling** med Context eller composition
""",
}


# Export all nodes from Block 1
BLOCK_1_NODES = [
    REACT_NODE_01_INTRODUCTION,
    REACT_NODE_02_JSX,
    REACT_NODE_03_COMPONENTS,
    REACT_NODE_04_PROPS,
]
