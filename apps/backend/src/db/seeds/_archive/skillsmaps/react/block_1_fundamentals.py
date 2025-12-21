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
    "title": "React Introduktion och Setup",
    "slug": "react-introduction",
    "description": "Forsta React och satt upp din utvecklingsmiljo",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 80,
    "topics_covered": [
        "react", "vite", "create-react-app", "jsx", "virtual dom",
        "component", "rendering", "npm", "yarn", "pnpm"
    ],
    "content": """# React Introduktion och Setup

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor React ar viktigt |
|----------|------------------------|
| **Dashboard-byggande** | Manga DevOps-verktyg har React-baserade UI |
| **Intern tooling** | Bygg admin-paneler och monitoring-dashboards |
| **Full-stack forstaelse** | Forsta frontend for battre API-design |
| **CI/CD pipelines** | Bygg och testa React-appar i pipelines |

Du maste forsta:

- **Vad React ar** - for att kunna deploya och konfigurera React-appar
- **Hur komponenter fungerar** - for att forsta applikationsstruktur
- **Build-processen** - for att optimera CI/CD pipelines

------------------------------------------------------------

## Vad ar React?

React ar ett **deklarativt** UI-bibliotek fran Meta (Facebook). Istallet for att saga *hur* UI ska uppdateras, beskriver du *vad* du vill se.

```
+-----------------------------------------------------------------+
|                    IMPERATIV vs DEKLARATIV                       |
+-----------------------------------------------------------------+
|                                                                  |
|  IMPERATIV (vanilla JS):              DEKLARATIV (React):       |
|  ---------------------                --------------------      |
|  const btn = document.                function Counter() {      |
|    createElement('button');             const [count, setCount] |
|  btn.textContent = count;               = useState(0);          |
|  btn.onclick = () => {                  return (                |
|    count++;                               <button onClick={      |
|    btn.textContent = count;                () => setCount(c+1)  |
|  };                                       }>                     |
|  document.body.appendChild(btn);           {count}               |
|                                          </button>               |
|                                        );                        |
|                                       }                          |
|                                                                  |
|  Problem: Manuell DOM-manipulation     Losning: React hanterar  |
|  blir komplex och buggig               DOM automatiskt          |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Virtual DOM

React anvander en **Virtual DOM** for effektiva uppdateringar:

```
+-----------------------------------------------------------------+
|                     REACT RENDERING CYCLE                        |
+-----------------------------------------------------------------+
|                                                                  |
|  1. State andras                                                 |
|     |                                                            |
|     ▼                                                            |
|  2. React skapar ny Virtual DOM                                  |
|     |                                                            |
|     ▼                                                            |
|  3. Diffing: Jamfor gammal vs ny Virtual DOM                     |
|     |                                                            |
|     ▼                                                            |
|  4. Reconciliation: Berakna minimala andringar                   |
|     |                                                            |
|     ▼                                                            |
|  5. Commit: Uppdatera bara det som andrats i riktiga DOM         |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Kommandon och Installation

| Kommando | Beskrivning |
|----------|-------------|
| `npm create vite@latest` | Skapa nytt React-projekt med Vite |
| `npx create-next-app@latest` | Skapa Next.js-app (fullstack) |
| `npm install` | Installera dependencies |
| `npm run dev` | Starta utvecklingsserver |
| `npm run build` | Bygg for produktion |

### Vite Setup (Rekommenderat)

```bash
# Skapa nytt React-projekt med Vite
npm create vite@latest my-react-app -- --template react-ts

# Navigera och installera
cd my-react-app
npm install

# Starta utvecklingsserver
npm run dev
# Output: Local: http://localhost:5173/
```

### Next.js Setup (Fullstack)

```bash
# Skapa Next.js-app (App Router)
npx create-next-app@latest my-nextjs-app
# Valj: TypeScript, ESLint, Tailwind CSS, App Router

cd my-nextjs-app
npm run dev
# Output: Local: http://localhost:3000/
```

------------------------------------------------------------

## Projektstruktur

```
+-----------------------------------------------------------------+
|                    VITE REACT PROJEKTSTRUKTUR                    |
+-----------------------------------------------------------------+
|                                                                  |
|  my-react-app/                                                   |
|  +-- public/                  # Statiska filer                   |
|  |   +-- vite.svg                                                |
|  +-- src/                     # Kallkod                          |
|  |   +-- assets/              # Bilder, fonts                    |
|  |   +-- App.tsx              # Huvudkomponent                   |
|  |   +-- App.css              # Komponent-styles                 |
|  |   +-- main.tsx             # Entry point                      |
|  |   +-- index.css            # Global CSS                       |
|  +-- index.html               # HTML template                    |
|  +-- package.json             # Dependencies                     |
|  +-- tsconfig.json            # TypeScript config                |
|  +-- vite.config.ts           # Vite config                      |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Praktiskt Exempel

```tsx
// src/App.tsx - Din forsta React-komponent
function App() {
  return (
    <div className="app">
      <h1>Hello, React!</h1>
      <p>Welcome to your first React application.</p>
    </div>
  );
}

export default App;
```

```tsx
// src/main.tsx - Entry point
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

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **React** | Deklarativt UI-bibliotek fran Meta |
| **JSX** | JavaScript XML - HTML-liknande syntax i JS |
| **Virtual DOM** | In-memory representation av UI |
| **Component** | Ateranvandbar UI-byggblock |
| **Vite** | Modern, snabb build-tool for React |
| **Next.js** | React-framework med SSR och routing |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Cannot find module 'react'` | Dependencies ej installerade | `npm install` |
| `Port 5173 already in use` | Annan process anvander porten | `npm run dev -- --port 3001` |
| `JSX element has no corresponding closing tag` | Obalanserade taggar | Kontrollera JSX-syntax |
| `'React' must be in scope` | Gammal React-version | Uppgradera eller lagg till `import React` |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Deklarativt** | Beskriv vad du vill se, inte hur |
| **Komponentbaserat** | Bygg UI av ateranvandbara delar |
| **Virtual DOM** | Effektiv rendering genom diffing |
| **Vite/Next.js** | Moderna verktyg for React-utveckling |

**Kom ihag:**

- React ar ett bibliotek, inte ett framework
- Komponenter ar funktioner som returnerar JSX
- Virtual DOM gor React snabbt
- Vite ar det moderna valet for nya projekt
""",
}


# ============================================================================
# NODE 2: JSX - JAVASCRIPT XML
# ============================================================================

REACT_NODE_02_JSX = {
    "node_id": 2,
    "title": "JSX - JavaScript XML",
    "slug": "jsx-syntax",
    "description": "Beharска JSX-syntax och dynamiska uttryck",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "jsx", "expressions", "attributes", "children", "fragments",
        "conditional rendering", "lists", "keys", "className"
    ],
    "content": """# JSX - JavaScript XML

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor JSX ar viktigt |
|----------|----------------------|
| **Dashboard-UI** | Skapa dynamiska vyer for monitoring |
| **Konfiguration** | Rendera listor av servrar, containers |
| **Statusvisning** | Villkorlig rendering baserat pa status |
| **Formuler** | Bygg admin-verktyg och input-forms |

Du maste forsta:

- **JSX-syntax** - grundlaggande for all React-utveckling
- **Expressions** - for att visa dynamisk data
- **Listor och keys** - for att rendera collections effektivt

------------------------------------------------------------

## Vad ar JSX?

JSX ar en syntaxextension for JavaScript som later dig skriva HTML-liknande kod:

```
+-----------------------------------------------------------------+
|                    JSX TRANSFORMATION                            |
+-----------------------------------------------------------------+
|                                                                  |
|  JSX (vad du skriver):                                           |
|  ---------------------                                           |
|  const element = <h1>Hello, World!</h1>;                         |
|                                                                  |
|                        |                                         |
|                        ▼  (kompileras av Babel/TypeScript)       |
|                                                                  |
|  JavaScript (vad som kors):                                      |
|  --------------------------                                      |
|  const element = React.createElement('h1', null, 'Hello!');      |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## JSX Syntax

| Syntax | Beskrivning | Exempel |
|--------|-------------|---------|
| `{expression}` | JavaScript-uttryck | `{name}`, `{2 + 2}` |
| `className` | CSS-klass (inte class) | `className="btn"` |
| `onClick` | Event handler (camelCase) | `onClick={handler}` |
| `style={{}}` | Inline styles som objekt | `style={{color: 'red'}}` |
| `<></>` | Fragment (ingen wrapper) | Returnera flera element |
| `key` | Unik identifierare i listor | `key={item.id}` |

------------------------------------------------------------

## Praktiska Exempel

### Expressions i JSX

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

### Attribut i JSX

```tsx
function StyledButton() {
  return (
    <button
      className="btn-primary"
      onClick={() => alert('Clicked!')}
      disabled={false}
      style={{
        backgroundColor: 'blue',
        fontSize: '16px'
      }}
    >
      Click me
    </button>
  );
}
```

### Villkorlig Rendering

```tsx
function UserStatus({ isLoggedIn }: { isLoggedIn: boolean }) {
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

// AND-operator for enkel villkor
function Notifications({ count }: { count: number }) {
  return (
    <div>
      {count > 0 && <span className="badge">{count}</span>}
    </div>
  );
}
```

### Listor och Keys

```tsx
interface Server {
  id: string;
  name: string;
  status: 'online' | 'offline';
}

function ServerList({ servers }: { servers: Server[] }) {
  return (
    <ul>
      {servers.map(server => (
        <li key={server.id}>
          {server.status === 'online' ? 'ON' : 'OFF'} {server.name}
        </li>
      ))}
    </ul>
  );
}
```

### Fragments

```tsx
function Profile() {
  return (
    <>
      <h1>User Profile</h1>
      <p>Details here</p>
    </>
  );
}

// Med key i listor
import { Fragment } from 'react';

function DefinitionList({ items }) {
  return items.map(item => (
    <Fragment key={item.id}>
      <dt>{item.title}</dt>
      <dd>{item.description}</dd>
    </Fragment>
  ));
}
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **JSX** | JavaScript XML - HTML-liknande syntax |
| **Expression** | JavaScript-kod inom `{}` |
| **className** | CSS-klass i JSX (inte class) |
| **Fragment** | `<>...</>` for multipla element |
| **key** | Unik ID for list-element |
| **Ternary** | `condition ? true : false` for villkor |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Adjacent JSX elements must be wrapped` | Flera root-element | Wrappa i `<>...</>` eller `<div>` |
| `class is not valid` | Fel attributnamn | Anvand `className` |
| `Each child should have unique key` | Saknar key i lista | Lagg till `key={uniqueId}` |
| `Objects are not valid as React child` | Renderar objekt direkt | Konvertera till string eller mappa |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **JSX = JavaScript** | Kompileras till React.createElement() |
| **Expressions** | Anvand `{}` for dynamisk data |
| **className** | Inte class - React-specifikt |
| **Keys** | Obligatoriskt i listor for performance |

**Kom ihag:**

- JSX ar inte HTML - det ar JavaScript
- Alla attribut ar camelCase (onClick, className)
- Alltid unika keys i listor - aldrig index om listan andras
- Fragments sparar onodiga DOM-noder
""",
}


# ============================================================================
# NODE 3: COMPONENTS - BUILDING BLOCKS
# ============================================================================

REACT_NODE_03_COMPONENTS = {
    "node_id": 3,
    "title": "Komponenter - Byggstenar",
    "slug": "react-components",
    "description": "Forsta och skapa React-komponenter",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "function components", "class components", "component composition",
        "reusability", "separation of concerns", "component tree"
    ],
    "content": """# Komponenter - Byggstenar

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor komponenter ar viktiga |
|----------|------------------------------|
| **Dashboard-moduler** | Ateranvand samma kort for olika metrics |
| **Status-widgets** | Samma komponent for olika tjanster |
| **Formulerhantering** | Generiska input-komponenter |
| **Navigation** | Konsistent UI over hela appen |

Du maste forsta:

- **Komponent-tanket** - bryt ner UI i ateranvandbara delar
- **Composition** - bygg komplext fran enkelt
- **Separation of concerns** - varje komponent gor en sak

------------------------------------------------------------

## Vad ar en komponent?

En komponent ar en funktion som returnerar JSX:

```
+-----------------------------------------------------------------+
|                    KOMPONENT-ANATOMI                             |
+-----------------------------------------------------------------+
|                                                                  |
|  function Button({ label, onClick }) {  // Props (input)         |
|    const [clicked, setClicked] = useState(false);  // State      |
|                                                                  |
|    const handleClick = () => {  // Event handler                 |
|      setClicked(true);                                           |
|      onClick?.();                                                |
|    };                                                            |
|                                                                  |
|    return (                    // JSX (output)                   |
|      <button onClick={handleClick}>                              |
|        {label}                                                   |
|      </button>                                                   |
|    );                                                            |
|  }                                                               |
|                                                                  |
|  INPUT: Props (data fran parent)                                 |
|  INTERN: State (lokal data)                                      |
|  OUTPUT: JSX (UI att rendera)                                    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Komponent-typer

| Typ | Beskrivning | Anvandning |
|-----|-------------|------------|
| **Function Component** | Funktion som returnerar JSX | Standard idag |
| **Presentation** | Endast UI, ingen logik | Knappar, kort, text |
| **Container** | Logik och datahamtning | Sidor, wrappers |
| **Compound** | Flexibla sub-komponenter | Card.Header, Card.Body |

------------------------------------------------------------

## Praktiska Exempel

### Enkel komponent

```tsx
// Enkel funktion
function Greeting() {
  return <h1>Hello!</h1>;
}

// Arrow function
const Greeting = () => <h1>Hello!</h1>;

// Med TypeScript
interface GreetingProps {
  name: string;
}

function Greeting({ name }: GreetingProps) {
  return <h1>Hello, {name}!</h1>;
}
```

### Komponent-komposition

```tsx
// Sma, fokuserade komponenter
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

// Sammansatt komponent
function UserCard({ user }: { user: User }) {
  return (
    <article className="user-card">
      <Avatar src={user.avatar} alt={user.name} />
      <UserInfo name={user.name} role={user.role} />
    </article>
  );
}
```

### Komponent-hierarki

```
+-----------------------------------------------------------------+
|                     KOMPONENT-TRAD                               |
+-----------------------------------------------------------------+
|                                                                  |
|                          App                                     |
|                           |                                      |
|         +-----------------+-----------------+                    |
|         |                 |                 |                    |
|      Header            Main             Footer                   |
|         |                 |                                      |
|    +----+----+      +----+----+                                  |
|    |         |      |         |                                  |
|   Logo    NavBar  Sidebar   Content                              |
|              |                 |                                 |
|         +----+----+       ServerList                             |
|         |         |           |                                  |
|      NavItem  NavItem    ServerCard                              |
|                              |                                   |
|                         +----+----+                              |
|                         |         |                              |
|                      Status    Actions                           |
|                                                                  |
+-----------------------------------------------------------------+
```

### Container vs Presentation

```tsx
// Presentation (dumb) - endast UI
function ServerCard({ server, onRestart }: {
  server: Server;
  onRestart: (id: string) => void
}) {
  return (
    <div className="server-card">
      <span>{server.status === 'online' ? 'ON' : 'OFF'}</span>
      <h3>{server.name}</h3>
      <button onClick={() => onRestart(server.id)}>Restart</button>
    </div>
  );
}

// Container (smart) - logik och data
function ServerListContainer() {
  const [servers, setServers] = useState<Server[]>([]);

  useEffect(() => {
    fetchServers().then(setServers);
  }, []);

  const handleRestart = async (id: string) => {
    await restartServer(id);
    setServers(prev => prev.map(s =>
      s.id === id ? { ...s, status: 'restarting' } : s
    ));
  };

  return (
    <div className="server-list">
      {servers.map(server => (
        <ServerCard
          key={server.id}
          server={server}
          onRestart={handleRestart}
        />
      ))}
    </div>
  );
}
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Component** | Ateranvandbar UI-funktion |
| **Props** | Input-data fran parent |
| **State** | Intern, foranderlig data |
| **Composition** | Bygga komplext fran enkelt |
| **PascalCase** | Komponentnamn borjar med stor bokstav |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `button is not defined` | Komponent med liten bokstav | Anvand `Button` (PascalCase) |
| `Nothing was returned from render` | Inget return-varde | Returnera JSX eller null |
| `Too many re-renders` | State-uppdatering i render | Flytta till useEffect |
| `Cannot read property of undefined` | Props saknas | Lagg till default-varden |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Ateranvandbarhet** | Skriv komponenter som kan anvandas pa flera stallen |
| **Single Responsibility** | Varje komponent gor EN sak |
| **Composition** | Bygg komplext genom att kombinera enkelt |
| **PascalCase** | Alltid stor bokstav for komponentnamn |

**Kom ihag:**

- Function components ar standard - undvik class components
- Bryt ner stora komponenter i mindre
- Props gar nedat, callbacks gar uppat
- Testa komponenter isolerat
""",
}


# ============================================================================
# NODE 4: PROPS - COMPONENT COMMUNICATION
# ============================================================================

REACT_NODE_04_PROPS = {
    "node_id": 4,
    "title": "Props - Komponentkommunikation",
    "slug": "react-props",
    "description": "Dataflode med props och prop-monster",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "props", "children", "default props", "prop types",
        "typescript interfaces", "destructuring", "prop drilling"
    ],
    "content": """# Props - Komponentkommunikation

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor props ar viktigt |
|----------|------------------------|
| **Konfigurerbara komponenter** | Samma komponent, olika data |
| **Dataflode** | Forsta hur applikationer hangar ihop |
| **Callback-monster** | Child-to-parent kommunikation |
| **Ateranvandbarhet** | Generiska komponenter for olika use cases |

Du maste forsta:

- **Unidirectional data flow** - data gar nedat
- **Callbacks** - events gar uppat
- **Prop drilling** - och hur man undviker det

------------------------------------------------------------

## Dataflode i React

```
+-----------------------------------------------------------------+
|                    UNIDIRECTIONAL DATA FLOW                      |
+-----------------------------------------------------------------+
|                                                                  |
|                        Parent                                    |
|                     [state: servers]                             |
|                          |                                       |
|              props       |       callback                        |
|              (data)      ▼       (events)                        |
|         +----------------+----------------+                      |
|         |                                 |                      |
|         ▼                                 ▼                      |
|      Child A                          Child B                    |
|   <ServerList                     <AddServerForm                 |
|     servers={servers}               onAdd={handleAdd}            |
|   />                              />                             |
|                                                                  |
|  Data flodar NEDAT via props                                     |
|  Events flodar UPPAT via callbacks                               |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Props-typer

| Prop-typ | Beskrivning | Exempel |
|----------|-------------|---------|
| **Primitiv** | String, number, boolean | `name="Server1"` |
| **Objekt** | Komplexa datastrukturer | `server={serverObj}` |
| **Array** | Listor av data | `items={[1,2,3]}` |
| **Funktion** | Callbacks | `onClick={handler}` |
| **Children** | Nested JSX | `<Card>content</Card>` |
| **Optional** | Med `?` i TypeScript | `title?: string` |

------------------------------------------------------------

## Praktiska Exempel

### Grundlaggande Props

```tsx
interface ServerCardProps {
  name: string;
  status: 'online' | 'offline';
  ip?: string;  // Optional
}

function ServerCard({ name, status, ip }: ServerCardProps) {
  return (
    <div className="server-card">
      <h3>{name}</h3>
      <span className={status}>{status.toUpperCase()}</span>
      {ip && <p>IP: {ip}</p>}
    </div>
  );
}

// Anvandning
<ServerCard name="web-01" status="online" ip="192.168.1.1" />
<ServerCard name="db-01" status="offline" />
```

### Children Prop

```tsx
interface CardProps {
  title: string;
  children: React.ReactNode;
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

// Anvandning - allt mellan taggarna blir children
<Card title="Server Status">
  <p>All systems operational</p>
  <ul>
    <li>API: Online</li>
    <li>Database: Online</li>
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
  variant = 'primary',
  size = 'md'
}: ButtonProps) {
  return (
    <button className={`btn btn-${variant} btn-${size}`}>
      {label}
    </button>
  );
}

// Alla dessa fungerar
<Button label="Submit" />
<Button label="Cancel" variant="secondary" />
<Button label="Delete" variant="danger" size="sm" />
```

### Callback Props

```tsx
interface SearchProps {
  onSearch: (query: string) => void;
  placeholder?: string;
}

function SearchInput({ onSearch, placeholder = "Sok..." }: SearchProps) {
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
      <button type="submit">Sok</button>
    </form>
  );
}

// Parent
function App() {
  const handleSearch = (query: string) => {
    console.log('Soker efter:', query);
  };

  return <SearchInput onSearch={handleSearch} />;
}
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
      {error && <span className="error-msg">{error}</span>}
    </div>
  );
}

// Alla standard input-attribut fungerar
<Input
  label="Email"
  type="email"
  required
  placeholder="Enter email"
  error="Invalid format"
/>
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Props** | Read-only data fran parent |
| **Children** | Speciell prop for nested content |
| **Callback** | Funktion som prop for events |
| **Destructuring** | `{ name, age }` istallet for `props.name` |
| **Spread** | `{...props}` for att vidarebefordra alla props |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Cannot assign to props` | Forsok att mutera props | Props ar read-only, anvand callback |
| `undefined is not a function` | Callback saknas | Lagg till optional chaining `onClick?.()` |
| `Prop drilling hell` | For manga nivaer | Anvand Context eller state management |
| `Type error on props` | Fel prop-typ | Kontrollera TypeScript interface |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Unidirectional** | Data nedat, events uppat |
| **Immutable** | Mutera aldrig props |
| **TypeScript** | Definiera props med interfaces |
| **Defaults** | Anvand default-varden for optional props |

**Kom ihag:**

- Props ar som funktionsargument - read-only
- Children ar en speciell prop for nested JSX
- Callbacks later children kommunicera med parents
- Undvik prop drilling med Context eller composition
""",
}


# Export all nodes from Block 1
BLOCK_1_NODES = [
    REACT_NODE_01_INTRODUCTION,
    REACT_NODE_02_JSX,
    REACT_NODE_03_COMPONENTS,
    REACT_NODE_04_PROPS,
]
