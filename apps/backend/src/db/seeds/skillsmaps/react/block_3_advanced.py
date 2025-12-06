"""
React SkillsMap - Block 3: Advanced Patterns
Nodes 9-12: Context, useReducer, Performance, Patterns
"""

from typing import Any

# ============================================================================
# NODE 9: CONTEXT API - GLOBAL STATE
# ============================================================================

REACT_NODE_09_CONTEXT = {
    "node_id": 9,
    "title": "Context API - Global State",
    "slug": "context-api",
    "description": "Dela state globalt utan prop drilling",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "createContext", "useContext", "Provider", "Consumer",
        "theme context", "auth context", "prop drilling"
    ],
    "content": """
# Context API - Global State

> *"Context provides a way to pass data through the component tree without having to pass props down manually at every level."*

---

## 🎯 Why This Matters

Prop drilling blir snabbt ohållbart i stora appar. Context löser detta genom att göra data tillgänglig för alla komponenter i ett träd.

---

## 🧠 Core Concepts

### Creating Context

```tsx
import { createContext, useContext, useState, ReactNode } from 'react';

// 1. Create context with default value
interface ThemeContextType {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | null>(null);

// 2. Create Provider component
function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// 3. Create custom hook for consumption
function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// 4. Use in components
function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();

  return (
    <button onClick={toggleTheme}>
      Current: {theme} (Click to toggle)
    </button>
  );
}

// 5. Wrap app with Provider
function App() {
  return (
    <ThemeProvider>
      <Header />
      <Main />
      <Footer />
    </ThemeProvider>
  );
}
```

### Auth Context (Real World Example)

```tsx
interface User {
  id: string;
  name: string;
  email: string;
}

interface AuthContextType {
  user: User | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | null>(null);

function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Check session on mount
  useEffect(() => {
    checkAuth().then(setUser).finally(() => setIsLoading(false));
  }, []);

  const login = async (email: string, password: string) => {
    const user = await loginAPI(email, password);
    setUser(user);
  };

  const logout = () => {
    logoutAPI();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{
      user,
      isLoading,
      login,
      logout,
      isAuthenticated: !!user
    }}>
      {children}
    </AuthContext.Provider>
  );
}

function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}

// Protected Route component
function ProtectedRoute({ children }: { children: ReactNode }) {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) return <LoadingSpinner />;
  if (!isAuthenticated) return <Navigate to="/login" />;

  return <>{children}</>;
}
```

---

## 💻 Multiple Contexts

```tsx
// Combine multiple providers
function AppProviders({ children }: { children: ReactNode }) {
  return (
    <AuthProvider>
      <ThemeProvider>
        <NotificationProvider>
          {children}
        </NotificationProvider>
      </ThemeProvider>
    </AuthProvider>
  );
}

function App() {
  return (
    <AppProviders>
      <Router>
        <Routes />
      </Router>
    </AppProviders>
  );
}
```

---

## ⚠️ Vanliga Problem

### Problem: Unnecessary re-renders

```tsx
// ❌ Alla consumers re-renderas vid varje state-ändring
function BadProvider({ children }) {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');

  // Nytt objekt varje render = alla consumers re-renderas
  return (
    <AppContext.Provider value={{ user, setUser, theme, setTheme }}>
      {children}
    </AppContext.Provider>
  );
}

// ✅ Memoize value eller splitta contexts
function GoodProvider({ children }) {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');

  const value = useMemo(
    () => ({ user, setUser, theme, setTheme }),
    [user, theme]
  );

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
}
```

---

## ✅ Sammanfattning

- **Context** eliminerar prop drilling
- **createContext + Provider + useContext** trion
- **Custom hook** för säker consumption
- **Splitta contexts** för att undvika onödiga re-renders
- **Memoize value** om context har flera värden
""",
}


# ============================================================================
# NODE 10: useReducer - COMPLEX STATE
# ============================================================================

REACT_NODE_10_USEREDUCER = {
    "node_id": 10,
    "title": "useReducer - Complex State",
    "slug": "use-reducer",
    "description": "Hantera komplex state logic med reducer pattern",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "useReducer", "reducer", "dispatch", "actions",
        "state machine", "immer", "redux pattern"
    ],
    "content": """
# useReducer - Complex State

> *"useReducer is usually preferable to useState when you have complex state logic."*

---

## 🎯 Why This Matters

När state-logik blir komplex (flera relaterade värden, komplexa uppdateringar), blir useReducer mer läsbart och testbart än många useState-calls.

---

## 🧠 Core Concepts

### useReducer vs useState

```
┌─────────────────────────────────────────────────────────────────┐
│                  useState vs useReducer                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  useState                         useReducer                    │
│  ────────                         ──────────                    │
│  • Enkelt state                  • Komplex state                │
│  • Få uppdateringar              • Många relaterade ändringar   │
│  • Inline logic OK               • Logic bör vara testbar       │
│  • Enskilda värden               • State machine patterns       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Basic useReducer

```tsx
// Types
interface State {
  count: number;
  step: number;
}

type Action =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'reset' }
  | { type: 'setStep'; payload: number };

// Reducer function (pure!)
function counterReducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'decrement':
      return { ...state, count: state.count - state.step };
    case 'reset':
      return { ...state, count: 0 };
    case 'setStep':
      return { ...state, step: action.payload };
    default:
      return state;
  }
}

// Component
function Counter() {
  const [state, dispatch] = useReducer(counterReducer, {
    count: 0,
    step: 1
  });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
      <input
        type="number"
        value={state.step}
        onChange={(e) => dispatch({
          type: 'setStep',
          payload: Number(e.target.value)
        })}
      />
    </div>
  );
}
```

### Todo App with useReducer

```tsx
interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

interface TodoState {
  todos: Todo[];
  filter: 'all' | 'active' | 'completed';
}

type TodoAction =
  | { type: 'ADD_TODO'; payload: string }
  | { type: 'TOGGLE_TODO'; payload: string }
  | { type: 'DELETE_TODO'; payload: string }
  | { type: 'SET_FILTER'; payload: TodoState['filter'] }
  | { type: 'CLEAR_COMPLETED' };

function todoReducer(state: TodoState, action: TodoAction): TodoState {
  switch (action.type) {
    case 'ADD_TODO':
      return {
        ...state,
        todos: [
          ...state.todos,
          { id: crypto.randomUUID(), text: action.payload, completed: false }
        ]
      };

    case 'TOGGLE_TODO':
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload
            ? { ...todo, completed: !todo.completed }
            : todo
        )
      };

    case 'DELETE_TODO':
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.payload)
      };

    case 'SET_FILTER':
      return { ...state, filter: action.payload };

    case 'CLEAR_COMPLETED':
      return {
        ...state,
        todos: state.todos.filter(todo => !todo.completed)
      };

    default:
      return state;
  }
}

function TodoApp() {
  const [state, dispatch] = useReducer(todoReducer, {
    todos: [],
    filter: 'all'
  });

  const filteredTodos = state.todos.filter(todo => {
    if (state.filter === 'active') return !todo.completed;
    if (state.filter === 'completed') return todo.completed;
    return true;
  });

  return (
    <div>
      <AddTodoForm onAdd={(text) => dispatch({ type: 'ADD_TODO', payload: text })} />

      <FilterButtons
        current={state.filter}
        onChange={(filter) => dispatch({ type: 'SET_FILTER', payload: filter })}
      />

      <TodoList
        todos={filteredTodos}
        onToggle={(id) => dispatch({ type: 'TOGGLE_TODO', payload: id })}
        onDelete={(id) => dispatch({ type: 'DELETE_TODO', payload: id })}
      />

      <button onClick={() => dispatch({ type: 'CLEAR_COMPLETED' })}>
        Clear completed
      </button>
    </div>
  );
}
```

---

## 💻 useReducer + Context

```tsx
// Global state med useReducer + Context
const TodoContext = createContext<{
  state: TodoState;
  dispatch: React.Dispatch<TodoAction>;
} | null>(null);

function TodoProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(todoReducer, initialState);

  return (
    <TodoContext.Provider value={{ state, dispatch }}>
      {children}
    </TodoContext.Provider>
  );
}

function useTodos() {
  const context = useContext(TodoContext);
  if (!context) throw new Error('useTodos must be used within TodoProvider');
  return context;
}

// Nu kan vilken komponent som helst använda
function DeepNestedComponent() {
  const { state, dispatch } = useTodos();
  // ...
}
```

---

## ✅ Sammanfattning

- **useReducer** för komplex eller relaterad state
- **Reducer** är en pure function: (state, action) => newState
- **dispatch** skickar actions till reducern
- **Actions** beskriver vad som hände (type + payload)
- **Kombinera med Context** för global state
""",
}


# ============================================================================
# NODE 11: PERFORMANCE - MEMO, USEMEMO, USECALLBACK
# ============================================================================

REACT_NODE_11_PERFORMANCE = {
    "node_id": 11,
    "title": "Performance Optimization",
    "slug": "react-performance",
    "description": "Optimera React-appar med memoization",
    "difficulty": "advanced",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "React.memo", "useMemo", "useCallback", "profiling",
        "virtualization", "code splitting", "lazy loading"
    ],
    "content": """
# Performance Optimization

> *"Premature optimization is the root of all evil. But when you need it, know your tools."*

---

## 🎯 Why This Matters

React är snabbt som default, men vid skala behöver du förstå hur du undviker onödiga re-renders och optimerar tunga beräkningar.

---

## 🧠 Core Concepts

### React.memo

Förhindrar re-render om props inte ändrats:

```tsx
// Utan memo: re-renderas varje gång parent renderas
function ExpensiveList({ items }: { items: Item[] }) {
  console.log('ExpensiveList rendered');
  return (
    <ul>
      {items.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
}

// Med memo: re-renderas bara om items ändras
const MemoizedList = React.memo(function ExpensiveList({ items }: { items: Item[] }) {
  console.log('MemoizedList rendered');
  return (
    <ul>
      {items.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
});

// Custom comparison
const MemoizedWithCompare = React.memo(ExpensiveList, (prevProps, nextProps) => {
  // Return true om props är "lika" (skip re-render)
  return prevProps.items.length === nextProps.items.length;
});
```

### useMemo

Cacha dyra beräkningar:

```tsx
function Dashboard({ users, filter }: { users: User[]; filter: string }) {
  // ❌ Beräknas varje render
  const filteredUsers = users.filter(u =>
    u.name.toLowerCase().includes(filter.toLowerCase())
  );

  // ✅ Cacha resultat, beräkna bara när dependencies ändras
  const filteredUsers = useMemo(() => {
    console.log('Filtering users...');
    return users.filter(u =>
      u.name.toLowerCase().includes(filter.toLowerCase())
    );
  }, [users, filter]);

  return <UserList users={filteredUsers} />;
}
```

### useCallback

Cacha funktioner (viktigt för memo'd children):

```tsx
function Parent() {
  const [count, setCount] = useState(0);

  // ❌ Ny funktion varje render → Child re-renderas
  const handleClick = () => {
    console.log('clicked');
  };

  // ✅ Samma funktionsreferens mellan renders
  const handleClick = useCallback(() => {
    console.log('clicked');
  }, []);

  return (
    <>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      <MemoizedChild onClick={handleClick} />
    </>
  );
}

const MemoizedChild = React.memo(function Child({ onClick }: { onClick: () => void }) {
  console.log('Child rendered');
  return <button onClick={onClick}>Child Button</button>;
});
```

### När ska man använda dem?

```
┌─────────────────────────────────────────────────────────────────┐
│              OPTIMIZATION DECISION TREE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Använd React.memo när:                                         │
│  • Komponenten renderas ofta med samma props                    │
│  • Komponenten är "tung" (många children, komplex render)       │
│  • Parent re-renderas ofta av andra anledningar                 │
│                                                                  │
│  Använd useMemo när:                                            │
│  • Beräkningen är dyr (filtering, sorting, mapping stora arr)   │
│  • Resultatet används i dependency array för andra hooks        │
│  • Du skapar objekt/arrayer som skickas till memo'd children    │
│                                                                  │
│  Använd useCallback när:                                        │
│  • Funktionen skickas till memo'd children                      │
│  • Funktionen är dependency för useEffect                       │
│                                                                  │
│  ANVÄND INTE för:                                               │
│  • Enkla komponenter                                            │
│  • Simpla beräkningar                                           │
│  • "Just in case" - mätning först!                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Code Splitting

```tsx
import { lazy, Suspense } from 'react';

// Lazy load tung komponent
const HeavyChart = lazy(() => import('./HeavyChart'));
const AdminPanel = lazy(() => import('./AdminPanel'));

function App() {
  const { isAdmin } = useAuth();

  return (
    <div>
      <Suspense fallback={<ChartSkeleton />}>
        <HeavyChart />
      </Suspense>

      {isAdmin && (
        <Suspense fallback={<Loading />}>
          <AdminPanel />
        </Suspense>
      )}
    </div>
  );
}
```

---

## ✅ Sammanfattning

- **React.memo** - förhindrar re-render om props inte ändras
- **useMemo** - cachar dyra beräkningar
- **useCallback** - cachar funktioner
- **Mät först** med React DevTools Profiler
- **Lazy/Suspense** för code splitting
""",
}


# ============================================================================
# NODE 12: ADVANCED PATTERNS
# ============================================================================

REACT_NODE_12_PATTERNS = {
    "node_id": 12,
    "title": "Advanced Patterns",
    "slug": "advanced-patterns",
    "description": "Kraftfulla React-patterns för skalbarhet",
    "difficulty": "advanced",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "render props", "higher-order components", "compound components",
        "controlled/uncontrolled", "state initializers", "portals"
    ],
    "content": """
# Advanced Patterns

> *"Patterns are proven solutions to recurring problems."*

---

## 🎯 Why This Matters

Dessa patterns löser vanliga problem i större React-appar och gör din kod mer flexibel och återanvändbar.

---

## 🧠 Compound Components

Komponenter som arbetar tillsammans med implicit state-delning:

```tsx
// Användning (slutresultat)
<Tabs defaultValue="tab1">
  <Tabs.List>
    <Tabs.Trigger value="tab1">Tab 1</Tabs.Trigger>
    <Tabs.Trigger value="tab2">Tab 2</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="tab1">Content 1</Tabs.Content>
  <Tabs.Content value="tab2">Content 2</Tabs.Content>
</Tabs>

// Implementation
interface TabsContextType {
  activeTab: string;
  setActiveTab: (value: string) => void;
}

const TabsContext = createContext<TabsContextType | null>(null);

function Tabs({ defaultValue, children }: { defaultValue: string; children: ReactNode }) {
  const [activeTab, setActiveTab] = useState(defaultValue);

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

Tabs.List = function TabsList({ children }: { children: ReactNode }) {
  return <div className="tabs-list">{children}</div>;
};

Tabs.Trigger = function TabsTrigger({ value, children }: { value: string; children: ReactNode }) {
  const { activeTab, setActiveTab } = useContext(TabsContext)!;

  return (
    <button
      className={activeTab === value ? 'active' : ''}
      onClick={() => setActiveTab(value)}
    >
      {children}
    </button>
  );
};

Tabs.Content = function TabsContent({ value, children }: { value: string; children: ReactNode }) {
  const { activeTab } = useContext(TabsContext)!;

  if (activeTab !== value) return null;
  return <div className="tabs-content">{children}</div>;
};
```

---

## 💻 Render Props

Dela logik via en funktion som prop:

```tsx
interface MousePosition {
  x: number;
  y: number;
}

interface MouseTrackerProps {
  render: (position: MousePosition) => ReactNode;
}

function MouseTracker({ render }: MouseTrackerProps) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleMove = (e: MouseEvent) => {
      setPosition({ x: e.clientX, y: e.clientY });
    };

    window.addEventListener('mousemove', handleMove);
    return () => window.removeEventListener('mousemove', handleMove);
  }, []);

  return <>{render(position)}</>;
}

// Användning
<MouseTracker
  render={({ x, y }) => (
    <div>Mouse: {x}, {y}</div>
  )}
/>
```

---

## 💻 Higher-Order Components (HOC)

Funktion som tar en komponent och returnerar en ny:

```tsx
function withAuth<P extends object>(
  WrappedComponent: ComponentType<P>
) {
  return function WithAuthComponent(props: P) {
    const { isAuthenticated, isLoading } = useAuth();

    if (isLoading) return <LoadingSpinner />;
    if (!isAuthenticated) return <Navigate to="/login" />;

    return <WrappedComponent {...props} />;
  };
}

// Användning
const ProtectedDashboard = withAuth(Dashboard);

function App() {
  return <ProtectedDashboard />;
}
```

---

## 💻 Portals

Rendera utanför parent DOM-hierarkin:

```tsx
import { createPortal } from 'react-dom';

function Modal({ children, onClose }: { children: ReactNode; onClose: () => void }) {
  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <button onClick={onClose}>×</button>
        {children}
      </div>
    </div>,
    document.getElementById('modal-root')!
  );
}

// Användning
function App() {
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <button onClick={() => setShowModal(true)}>Open</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <h2>Modal Content</h2>
        </Modal>
      )}
    </div>
  );
}
```

---

## ✅ Sammanfattning

- **Compound Components** - flexibel API med implicit state
- **Render Props** - dela logik via render function
- **HOC** - återanvändbar komponent-logik (legacy, föredra hooks)
- **Portals** - rendera utanför DOM-hierarkin
""",
}


# Export all nodes from Block 3
BLOCK_3_NODES = [
    REACT_NODE_09_CONTEXT,
    REACT_NODE_10_USEREDUCER,
    REACT_NODE_11_PERFORMANCE,
    REACT_NODE_12_PATTERNS,
]
