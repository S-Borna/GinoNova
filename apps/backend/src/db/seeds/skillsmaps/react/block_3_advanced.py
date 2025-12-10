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

Context gor data tillganglig for alla komponenter i ett trad utan prop drilling.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Auth context** | Anvandarsession for hela appen |
| **Theme context** | Dark/light mode globalt |
| **Config context** | Miljovariabler och feature flags |
| **Notification** | Global toast/alert system |

------------------------------------------------------------

## Creating Context

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

------------------------------------------------------------

## Auth Context

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

------------------------------------------------------------

## Multiple Contexts

```tsx
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

------------------------------------------------------------

## Snabbreferens

| Koncept | Beskrivning |
|---------|-------------|
| **createContext** | Skapar context med default value |
| **Provider** | Ger value till alla children |
| **useContext** | Konsumerar context value |
| **Custom hook** | useTheme, useAuth for saker consumption |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Context is undefined | Saknar Provider | Wrap med Provider |
| Alla re-renderas | Nytt value-objekt varje render | useMemo pa value |
| Hook utanfor Provider | Komponent inte wrapped | Lagg till Provider hogre upp |
| Default value null | Saknar check | Kasta error i custom hook |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Eliminera prop drilling** | Data tillganglig overallt |
| **createContext + Provider** | Trion for context |
| **Custom hook** | Saker consumption med error handling |
| **Splitta contexts** | Undvik onodig re-renders |

**Kom ihag:**

- Context eliminerar prop drilling
- createContext + Provider + useContext
- Custom hook for saker consumption
- Memoize value for att undvika re-renders
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

useReducer ar att foredra framfor useState nar du har komplex state-logik.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Form state** | Komplexa formular med manga falt |
| **Workflow state** | Multi-step deployment wizards |
| **Data tables** | Sorting, filtering, pagination |
| **State machines** | Pipeline status transitions |

------------------------------------------------------------

## useState vs useReducer

```
+-----------------------------------------------------------------+
|                  useState vs useReducer                          |
+-----------------------------------------------------------------+
|                                                                  |
|  useState                         useReducer                    |
|  --------                         ----------                    |
|  Enkelt state                     Komplex state                 |
|  Fa uppdateringar                 Manga relaterade andringar    |
|  Inline logic OK                  Logic bor vara testbar        |
|  Enskilda varden                  State machine patterns        |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Basic useReducer

```tsx
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

------------------------------------------------------------

## Todo App med useReducer

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
  | { type: 'SET_FILTER'; payload: TodoState['filter'] };

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

    default:
      return state;
  }
}
```

------------------------------------------------------------

## useReducer + Context

```tsx
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

// Nu kan vilken komponent som helst anvanda
function DeepNestedComponent() {
  const { state, dispatch } = useTodos();
  // ...
}
```

------------------------------------------------------------

## Snabbreferens

| Koncept | Beskrivning |
|---------|-------------|
| **Reducer** | Pure function: (state, action) => newState |
| **Action** | Objekt med type och optional payload |
| **dispatch** | Funktion som skickar action till reducer |
| **Initial state** | Startvardet for state |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| State muteras | Direkt mutation i reducer | Returnera alltid nytt objekt |
| Action ignoreras | Saknar case i switch | Lagg till case eller default |
| Undefined state | Fel initial state | Kontrollera initial value |
| Type error | Fel action type | Anvand TypeScript discriminated unions |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Komplex state** | useReducer for relaterade state-andringar |
| **Pure reducer** | (state, action) => newState utan side effects |
| **dispatch** | Skickar actions till reducern |
| **Context combo** | useReducer + Context for global state |

**Kom ihag:**

- useReducer for komplex eller relaterad state
- Reducer ar en pure function
- dispatch skickar actions till reducern
- Kombinera med Context for global state
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

React ar snabbt som default, men vid skala behovs forstaelse for memoization och optimering.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Stora listor** | Loggar, metrics, events |
| **Dashboards** | Manga widgets med olika data |
| **Real-time** | Frekventa uppdateringar utan lag |
| **Code splitting** | Snabbare initial load |

------------------------------------------------------------

## React.memo

Forhindrar re-render om props inte andrats:

```tsx
// Utan memo: re-renderas varje gang parent renderas
function ExpensiveList({ items }: { items: Item[] }) {
  console.log('ExpensiveList rendered');
  return (
    <ul>
      {items.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
}

// Med memo: re-renderas bara om items andras
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
  return prevProps.items.length === nextProps.items.length;
});
```

------------------------------------------------------------

## useMemo

Cacha dyra berakningar:

```tsx
function Dashboard({ users, filter }: { users: User[]; filter: string }) {
  // FEL: Beraknas varje render
  const filteredUsers = users.filter(u =>
    u.name.toLowerCase().includes(filter.toLowerCase())
  );

  // RATT: Cacha resultat, berakna bara nar dependencies andras
  const filteredUsers = useMemo(() => {
    console.log('Filtering users...');
    return users.filter(u =>
      u.name.toLowerCase().includes(filter.toLowerCase())
    );
  }, [users, filter]);

  return <UserList users={filteredUsers} />;
}
```

------------------------------------------------------------

## useCallback

Cacha funktioner (viktigt for memo'd children):

```tsx
function Parent() {
  const [count, setCount] = useState(0);

  // FEL: Ny funktion varje render -> Child re-renderas
  const handleClick = () => {
    console.log('clicked');
  };

  // RATT: Samma funktionsreferens mellan renders
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

------------------------------------------------------------

## Nar ska du anvanda dem?

```
+-----------------------------------------------------------------+
|              OPTIMIZATION DECISION TREE                          |
+-----------------------------------------------------------------+
|                                                                  |
|  Anvand React.memo nar:                                         |
|  - Komponenten renderas ofta med samma props                    |
|  - Komponenten ar tung (manga children, komplex render)         |
|  - Parent re-renderas ofta av andra anledningar                 |
|                                                                  |
|  Anvand useMemo nar:                                            |
|  - Berakningen ar dyr (filtering, sorting stora arrayer)        |
|  - Resultatet anvands i dependency array for andra hooks        |
|  - Du skapar objekt/arrayer som skickas till memo'd children    |
|                                                                  |
|  Anvand useCallback nar:                                        |
|  - Funktionen skickas till memo'd children                      |
|  - Funktionen ar dependency for useEffect                       |
|                                                                  |
|  ANVAND INTE for:                                               |
|  - Enkla komponenter                                            |
|  - Simpla berakningar                                           |
|  - "Just in case" - matning forst!                              |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Code Splitting

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

------------------------------------------------------------

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| **React.memo** | Forhindra re-render om props inte andras |
| **useMemo** | Cacha dyra berakningar |
| **useCallback** | Cacha funktioner |
| **lazy/Suspense** | Code splitting |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Memo hjalper inte | Ny funktion/objekt som prop | Anvand useCallback/useMemo |
| Over-optimization | Memoize allt | Mat forst med Profiler |
| Stale data | Tom dependency array | Lagg till alla dependencies |
| Ingen effekt | Prop andras faktiskt | Kontrollera vad som andras |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **React.memo** | Wrap komponenter som far samma props ofta |
| **useMemo** | Cacha dyra berakningar |
| **useCallback** | Cacha funktioner for memo'd children |
| **Mat forst** | Anvand React DevTools Profiler |

**Kom ihag:**

- React.memo forhindrar re-render om props inte andras
- useMemo cachar dyra berakningar
- useCallback cachar funktioner
- Mat forst med React DevTools Profiler
""",
}


# ============================================================================
# NODE 12: ADVANCED PATTERNS
# ============================================================================

REACT_NODE_12_PATTERNS = {
    "node_id": 12,
    "title": "Advanced Patterns",
    "slug": "advanced-patterns",
    "description": "Kraftfulla React-patterns for skalbarhet",
    "difficulty": "advanced",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "render props", "higher-order components", "compound components",
        "controlled/uncontrolled", "state initializers", "portals"
    ],
    "content": """
# Advanced Patterns

Dessa patterns loser vanliga problem i storre React-appar och gor din kod mer flexibel.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Compound Components** | Flexibla UI-komponenter for dashboards |
| **Render Props** | Delbar logik for data fetching |
| **HOC** | Ateranvandbar auth/permission logic |
| **Portals** | Modals, tooltips, notifications |

------------------------------------------------------------

## Compound Components

Komponenter som arbetar tillsammans med implicit state-delning:

```tsx
// Anvandning
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

------------------------------------------------------------

## Higher-Order Components (HOC)

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

// Anvandning
const ProtectedDashboard = withAuth(Dashboard);

function App() {
  return <ProtectedDashboard />;
}
```

------------------------------------------------------------

## Portals

Rendera utanfor parent DOM-hierarkin:

```tsx
import { createPortal } from 'react-dom';

function Modal({ children, onClose }: { children: ReactNode; onClose: () => void }) {
  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <button onClick={onClose}>x</button>
        {children}
      </div>
    </div>,
    document.getElementById('modal-root')!
  );
}

// Anvandning
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

------------------------------------------------------------

## Snabbreferens

| Pattern | Anvandning |
|---------|------------|
| **Compound Components** | Flexibel API med implicit state |
| **HOC** | Ateranvandbar komponent-logik |
| **Render Props** | Dela logik via render function |
| **Portals** | Rendera utanfor DOM-hierarkin |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Context undefined | Komponent utanfor Provider | Wrap med Provider |
| HOC namn saknas | displayName inte satt | Lagg till displayName |
| Portal renderas inte | modal-root saknas | Lagg till div i HTML |
| Render prop re-renders | Inline function | useCallback eller flytta ut |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Compound Components** | Flexibel API med implicit state |
| **HOC** | Legacy pattern, foredra hooks |
| **Portals** | Modals, tooltips utanfor parent |
| **Render Props** | Dela logik, delvis ersatt av hooks |

**Kom ihag:**

- Compound Components for flexibel API med implicit state
- HOC for ateranvandbar komponent-logik (legacy)
- Portals for att rendera utanfor DOM-hierarkin
- Render Props delvis ersatt av custom hooks
""",
}


# Export all nodes from Block 3
BLOCK_3_NODES = [
    REACT_NODE_09_CONTEXT,
    REACT_NODE_10_USEREDUCER,
    REACT_NODE_11_PERFORMANCE,
    REACT_NODE_12_PATTERNS,
]
