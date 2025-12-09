"""
React SkillsMap - Block 2: State & Effects
Nodes 5-8: useState, useEffect, Forms, Custom Hooks
"""

from typing import Any

# ============================================================================
# NODE 5: useState - LOCAL STATE
# ============================================================================

REACT_NODE_05_USESTATE = {
    "node_id": 5,
    "title": "useState - Local State",
    "slug": "use-state",
    "description": "Hantera komponentens lokala state med useState",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "useState", "state", "setter function", "immutability",
        "object state", "array state", "functional updates"
    ],
    "content": """
# useState - Local State

State ar det som gor React-appar interaktiva. Utan state ar komponenter statiska.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Dashboard state** | Realtidsdata som uppdateras kontinuerligt |
| **Form handling** | Konfigurationsformular for deployment |
| **UI state** | Modals, alerts, loading states i operations UI |
| **Filter state** | Filtrera loggar, metrics, och alerts |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## State vs Props

```
┌─────────────────────────────────────────────────────────────────┐
│                      STATE vs PROPS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PROPS                          STATE                           │
│  ─────                          ─────                           │
│  Kommer fran parent             Ags av komponenten sjalv        │
│  Read-only                      Kan andras via setter           │
│  Kan inte andras                Triggar re-render vid andring   │
│  Flodar nedat                   Privat till komponenten         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## useState Hook

```tsx
import { useState } from 'react';

function Counter() {
  // useState returnerar [varde, setterFunktion]
  const [count, setCount] = useState(0);  // 0 ar initial value

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Functional Updates

Nar ny state beror pa foregaende state, anvand functional update:

```tsx
function Counter() {
  const [count, setCount] = useState(0);

  // FEL: Om du klickar snabbt kanske inte alla klick raknas
  const incrementBad = () => setCount(count + 1);

  // RATT: Functional update garanterar senaste varde
  const incrementGood = () => setCount(prev => prev + 1);

  // Anvandbart for batch-operationer
  const addThree = () => {
    setCount(prev => prev + 1);
    setCount(prev => prev + 1);
    setCount(prev => prev + 1);
  };

  return (
    <button onClick={addThree}>Add 3 (count: {count})</button>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Object State

```tsx
interface User {
  name: string;
  email: string;
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
  };
}

function UserSettings() {
  const [user, setUser] = useState<User>({
    name: '',
    email: '',
    preferences: {
      theme: 'light',
      notifications: true
    }
  });

  // FEL: Mutera aldrig state direkt
  const badUpdate = () => {
    user.name = 'New Name';  // Detta triggar INTE re-render!
  };

  // RATT: Skapa nytt objekt med spread
  const updateName = (name: string) => {
    setUser({ ...user, name });
  };

  // Uppdatera nested property
  const toggleNotifications = () => {
    setUser({
      ...user,
      preferences: {
        ...user.preferences,
        notifications: !user.preferences.notifications
      }
    });
  };

  return (
    <form>
      <input
        value={user.name}
        onChange={(e) => updateName(e.target.value)}
      />
    </form>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Array State

```tsx
interface Task {
  id: string;
  title: string;
  completed: boolean;
}

function TaskList() {
  const [tasks, setTasks] = useState<Task[]>([]);

  // ADD - Lagg till i slutet
  const addTask = (title: string) => {
    const newTask: Task = {
      id: crypto.randomUUID(),
      title,
      completed: false
    };
    setTasks([...tasks, newTask]);
  };

  // REMOVE - Filtrera bort
  const removeTask = (id: string) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  // UPDATE - Map och uppdatera specifik
  const toggleTask = (id: string) => {
    setTasks(tasks.map(task =>
      task.id === id
        ? { ...task, completed: !task.completed }
        : task
    ));
  };

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => toggleTask(task.id)}
          />
          {task.title}
          <button onClick={() => removeTask(task.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Koncept | Beskrivning |
|---------|-------------|
| **useState** | Hook som returnerar [value, setter] |
| **Initial value** | Argument till useState |
| **Setter function** | Uppdaterar state och triggar re-render |
| **Functional update** | `prev => prev + 1` for state baserat pa previous |
| **Immutability** | Skapa nya objekt/arrayer, mutera aldrig |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| State uppdateras inte direkt | State ar asynkront | Anvand useEffect for att reagera pa andring |
| Stale closure | Gammal closure fangar initialt varde | Anvand functional update `prev => prev + 1` |
| Re-render sker inte | Mutering av state | Skapa nytt objekt med spread |
| For manga re-renders | useState i loop | Flytta useState till top level |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Immutability** | Mutera aldrig state, skapa nya objekt/arrayer |
| **Functional updates** | Anvand nar ny state beror pa previous |
| **Lazy initial state** | Anvand funktion for dyra berakningar |
| **Batching** | React batchar flera setters i samma event |

**Kom ihag:**

- useState returnerar [value, setter]
- Functional updates garanterar senaste varde
- Mutera aldrig state direkt - skapa nya objekt
- State-uppdateringar ar asynkrona och batchas
""",
}


# ============================================================================
# NODE 6: useEffect - SIDE EFFECTS
# ============================================================================

REACT_NODE_06_USEEFFECT = {
    "node_id": 6,
    "title": "useEffect - Side Effects",
    "slug": "use-effect",
    "description": "Hantera side effects som API-anrop och subscriptions",
    "difficulty": "intermediate",
    "estimated_minutes": 75,
    "xp_reward": 120,
    "topics_covered": [
        "useEffect", "side effects", "cleanup", "dependencies",
        "data fetching", "subscriptions", "event listeners"
    ],
    "content": """
# useEffect - Side Effects

useEffect hanterar kod som kor efter rendering - API-anrop, subscriptions, DOM-manipulation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Data fetching** | Hamta metrics, loggar, deployment status |
| **WebSocket** | Realtidsuppdateringar fran servrar |
| **Polling** | Periodisk kontroll av system health |
| **Cleanup** | Forhindra memory leaks vid unmount |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pure vs Side Effects

```
┌─────────────────────────────────────────────────────────────────┐
│                      PURE vs SIDE EFFECTS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PURE RENDER                        SIDE EFFECTS                │
│  ───────────                        ────────────                │
│  Berakna JSX fran props/state       API-anrop                   │
│  Deterministiskt                    DOM-manipulation            │
│  Inga externa beroenden             Event listeners             │
│  Samma input = samma output         Timers/intervals            │
│                                     LocalStorage                │
│                                     WebSocket connections        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## useEffect Syntax

```tsx
import { useEffect } from 'react';

function Component() {
  useEffect(() => {
    // Din side effect-kod har
    console.log('Effect kors');

    // Cleanup function (valfri)
    return () => {
      console.log('Cleanup kors');
    };
  }, [/* dependencies */]);
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dependency Array

```tsx
// Kors efter VARJE render
useEffect(() => {
  console.log('Kors varje gang');
});

// Kors bara vid MOUNT (och cleanup vid UNMOUNT)
useEffect(() => {
  console.log('Kors en gang');
  return () => console.log('Cleanup vid unmount');
}, []);

// Kors nar specifika varden ANDRAS
useEffect(() => {
  console.log('userId andrades till:', userId);
}, [userId]);

// Flera dependencies
useEffect(() => {
  console.log('userId eller filter andrades');
}, [userId, filter]);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Data Fetching

```tsx
interface User {
  id: string;
  name: string;
  email: string;
}

function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

    const controller = new AbortController();

    async function fetchUser() {
      try {
        const response = await fetch(`/api/users/${userId}`, {
          signal: controller.signal
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user');
        }

        const data = await response.json();
        setUser(data);
      } catch (err) {
        if (err instanceof Error && err.name !== 'AbortError') {
          setError(err.message);
        }
      } finally {
        setLoading(false);
      }
    }

    fetchUser();

    // Cleanup: Avbryt pagaende request om userId andras
    return () => controller.abort();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event Listeners

```tsx
function WindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    function handleResize() {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    }

    window.addEventListener('resize', handleResize);

    // CLEANUP: Ta bort listener vid unmount
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return <p>Window: {size.width} x {size.height}</p>;
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## WebSocket Subscription

```tsx
function LiveStatus({ serverId }: { serverId: string }) {
  const [status, setStatus] = useState<'online' | 'offline'>('offline');

  useEffect(() => {
    const ws = new WebSocket(`wss://api.example.com/status/${serverId}`);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setStatus(data.status);
    };

    ws.onerror = () => setStatus('offline');

    // CLEANUP: Stang anslutning
    return () => {
      ws.close();
    };
  }, [serverId]);

  return (
    <span className={status === 'online' ? 'green' : 'red'}>
      Server: {status}
    </span>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Dependency Array | Beteende |
|------------------|----------|
| **Ingen array** | Kors efter varje render |
| **Tom array []** | Kors bara vid mount |
| **[dep1, dep2]** | Kors nar dep1 eller dep2 andras |

| Cleanup Pattern | Anvandning |
|-----------------|------------|
| **return () => {}** | Kors vid unmount eller innan nasta effect |
| **AbortController** | Avbryt pagaende fetch |
| **clearInterval** | Stoppa timers |
| **ws.close()** | Stang WebSocket |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Infinite loop | Saknar dependency array | Lagg till tom array [] |
| Missing dependency | ESLint varning | Inkludera alla dependencies |
| Memory leak | Cleanup missas | Returnera cleanup-funktion |
| Stale data | Race condition | Anvand AbortController |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Dependency array** | Styr nar effect kors |
| **Cleanup function** | Stada upp listeners, timers, subscriptions |
| **Tom array** | [] = kors bara vid mount |
| **AbortController** | Avbryt fetch-requests vid unmount |

**Kom ihag:**

- useEffect for kod som kors efter render
- Alltid cleanup for subscriptions och listeners
- Tom array [] = kors bara en gang
- Inkludera alla dependencies i arrayen
""",
}


# ============================================================================
# NODE 7: FORMS - USER INPUT
# ============================================================================

REACT_NODE_07_FORMS = {
    "node_id": 7,
    "title": "Forms - User Input",
    "slug": "react-forms",
    "description": "Hantera formular och anvandarinput i React",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "controlled components", "uncontrolled components", "form submission",
        "validation", "react-hook-form", "zod", "formik"
    ],
    "content": """
# Forms - User Input

Formular ar det primara sattet anvandare interagerar med webbapplikationer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **Config forms** | Deployment-konfiguration, env variables |
| **Search/filter** | Filtrera loggar, metrics, alerts |
| **Settings** | System-installningar, user preferences |
| **Validation** | Forhindra felaktiga konfigurationer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Controlled vs Uncontrolled

```
┌─────────────────────────────────────────────────────────────────┐
│              CONTROLLED vs UNCONTROLLED                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CONTROLLED                       UNCONTROLLED                  │
│  ──────────                       ────────────                  │
│  React styr vardet               DOM styr vardet                │
│  value + onChange                ref + defaultValue             │
│  Fullstandig kontroll            Enklare for enkla formular     │
│  Kan validera i realtid          Mindre kod                     │
│  Mer kod                         Svarare att kontrollera        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Controlled Component

```tsx
function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Login:', { email, password });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Uncontrolled Component

```tsx
function LoginFormUncontrolled() {
  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Login:', {
      email: emailRef.current?.value,
      password: passwordRef.current?.value
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        ref={emailRef}
        defaultValue=""
        placeholder="Email"
      />
      <input
        type="password"
        ref={passwordRef}
        defaultValue=""
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Form with Validation

```tsx
interface FormData {
  name: string;
  email: string;
  password: string;
}

interface FormErrors {
  name?: string;
  email?: string;
  password?: string;
}

function RegistrationForm() {
  const [formData, setFormData] = useState<FormData>({
    name: '',
    email: '',
    password: ''
  });
  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validate = (): boolean => {
    const newErrors: FormErrors = {};

    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    }

    if (!formData.email.includes('@')) {
      newErrors.email = 'Valid email is required';
    }

    if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (field: keyof FormData) => (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setFormData(prev => ({ ...prev, [field]: e.target.value }));
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: undefined }));
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validate()) return;

    setIsSubmitting(true);
    try {
      await registerUser(formData);
    } catch (err) {
      setErrors({ email: 'Email already exists' });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <input
          value={formData.name}
          onChange={handleChange('name')}
          placeholder="Name"
        />
        {errors.name && <span className="error">{errors.name}</span>}
      </div>

      <div>
        <input
          type="email"
          value={formData.email}
          onChange={handleChange('email')}
          placeholder="Email"
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>

      <div>
        <input
          type="password"
          value={formData.password}
          onChange={handleChange('password')}
          placeholder="Password"
        />
        {errors.password && <span className="error">{errors.password}</span>}
      </div>

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Registering...' : 'Register'}
      </button>
    </form>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## React Hook Form + Zod

```tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const schema = z.object({
  name: z.string().min(1, 'Name is required'),
  email: z.string().email('Invalid email'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
});

type FormData = z.infer<typeof schema>;

function RegistrationForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting }
  } = useForm<FormData>({
    resolver: zodResolver(schema)
  });

  const onSubmit = async (data: FormData) => {
    await registerUser(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <input {...register('name')} placeholder="Name" />
        {errors.name && <span>{errors.name.message}</span>}
      </div>

      <div>
        <input {...register('email')} type="email" placeholder="Email" />
        {errors.email && <span>{errors.email.message}</span>}
      </div>

      <div>
        <input {...register('password')} type="password" placeholder="Password" />
        {errors.password && <span>{errors.password.message}</span>}
      </div>

      <button type="submit" disabled={isSubmitting}>
        Register
      </button>
    </form>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Koncept | Beskrivning |
|---------|-------------|
| **Controlled** | React styr vardet via state |
| **Uncontrolled** | DOM styr, React laser via ref |
| **preventDefault** | Stoppa default form submission |
| **register** | React Hook Form for input binding |
| **zodResolver** | Schema-baserad validering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Sidan laddas om | preventDefault saknas | Lagg till e.preventDefault() |
| Checkbox fungerar inte | value istallet for checked | Anvand checked={isChecked} |
| Input uppdateras inte | Saknar onChange | Lagg till onChange handler |
| Validering triggas inte | Fel form event | Anvand onSubmit pa form-taggen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Controlled** | React styr vardet via state och onChange |
| **preventDefault** | Alltid i onSubmit for att stoppa page reload |
| **React Hook Form** | Rekommenderat for produktionsformular |
| **Zod** | Schema-baserad validering med TypeScript |

**Kom ihag:**

- Controlled components ger full kontroll over input
- Alltid e.preventDefault() i onSubmit
- React Hook Form + Zod for produktionsformular
- Validera bade client och server-side
""",
}


# ============================================================================
# NODE 8: CUSTOM HOOKS
# ============================================================================

REACT_NODE_08_CUSTOM_HOOKS = {
    "node_id": 8,
    "title": "Custom Hooks - Reusable Logic",
    "slug": "custom-hooks",
    "description": "Skapa egna hooks for ateranvandbar logik",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "custom hooks", "composition", "state logic reuse",
        "hook rules", "testing hooks"
    ],
    "content": """
# Custom Hooks - Reusable Logic

Custom hooks later dig extrahera komponentlogik till ateranvandbara funktioner.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Betydelse |
|--------|-----------|
| **useFetch** | Ateranvandbar data-hamtning for alla API:er |
| **usePolling** | Periodisk uppdatering av metrics/status |
| **useWebSocket** | Realtidsanslutningar for monitoring |
| **useLocalStorage** | Persistent state for user preferences |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar en Custom Hook?

En custom hook ar en funktion som:
1. Borjar med use prefix
2. Kan anvanda andra hooks
3. Returnerar data och/eller funktioner

```tsx
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);

  const increment = () => setCount(c => c + 1);
  const decrement = () => setCount(c => c - 1);
  const reset = () => setCount(initialValue);

  return { count, increment, decrement, reset };
}

// Anvandning
function Counter() {
  const { count, increment, decrement, reset } = useCounter(10);

  return (
    <div>
      <p>{count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## useLocalStorage

```tsx
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function
        ? value(storedValue)
        : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  };

  return [storedValue, setValue] as const;
}

// Anvandning
function Settings() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');

  return (
    <select value={theme} onChange={e => setTheme(e.target.value)}>
      <option value="light">Light</option>
      <option value="dark">Dark</option>
    </select>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## useFetch

```tsx
interface UseFetchResult<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
  refetch: () => void;
}

function useFetch<T>(url: string): UseFetchResult<T> {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Fetch failed');
      const json = await response.json();
      setData(json);
    } catch (err) {
      setError(err instanceof Error ? err : new Error('Unknown error'));
    } finally {
      setLoading(false);
    }
  }, [url]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
}

// Anvandning
function UserList() {
  const { data: users, loading, error, refetch } = useFetch<User[]>('/api/users');

  if (loading) return <Spinner />;
  if (error) return <Error message={error.message} onRetry={refetch} />;

  return (
    <ul>
      {users?.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## useDebounce

```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// Anvandning
function SearchBox() {
  const [query, setQuery] = useState('');
  const debouncedQuery = useDebounce(query, 300);

  const { data: results } = useFetch<Result[]>(
    `/api/search?q=${debouncedQuery}`
  );

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <ResultList results={results} />
    </div>
  );
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hook Rules

```
┌─────────────────────────────────────────────────────────────────┐
│                       RULES OF HOOKS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Anropa hooks pa TOP LEVEL                                   │
│     Aldrig i loops, conditions, eller nested functions          │
│                                                                  │
│  2. Anropa hooks bara fran REACT FUNCTIONS                      │
│     React function components eller custom hooks                 │
│                                                                  │
│  3. Custom hooks borjar alltid med "use"                        │
│     useCounter, useFetch, useLocalStorage                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Hook | Anvandning |
|------|------------|
| **useLocalStorage** | Persistent state i localStorage |
| **useFetch** | Data fetching med loading/error |
| **useDebounce** | Fordrojd uppdatering av varde |
| **useMediaQuery** | Responsiv design baserat pa skarmstorlek |
| **useOnClickOutside** | Detektera klick utanfor element |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Invalid hook call | Hook i condition/loop | Flytta till top level |
| Hook inte definierad | Saknar use prefix | Lagg till use i namnet |
| Oandlig loop | useEffect saknar deps | Lagg till dependencies |
| Stale closure | Gammal referens | Anvand useCallback |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **use prefix** | Custom hooks borjar alltid med use |
| **Ateranvandbar logik** | Extrahera stateful logic till hooks |
| **Hook rules** | Alltid top-level, bara i React functions |
| **Composition** | Bygg komplexa hooks fran enkla |

**Kom ihag:**

- Custom hooks borjar med use och kan anvanda andra hooks
- Ateranvand stateful logic utan att kopiera kod
- Folj hook rules - alltid top-level
- Komponera hooks - bygg komplexa fran enkla
""",
}


# Export all nodes from Block 2
BLOCK_2_NODES = [
    REACT_NODE_05_USESTATE,
    REACT_NODE_06_USEEFFECT,
    REACT_NODE_07_FORMS,
    REACT_NODE_08_CUSTOM_HOOKS,
]
