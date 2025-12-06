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

> *"State is how React remembers things between renders."*

---

## 🎯 Why This Matters

State är det som gör React-appar interaktiva. Utan state är komponenter statiska - de kan inte svara på användarinput eller uppdatera sig själva.

---

## 🧠 Core Concepts

### Vad är State?

State är data som kan ändras över tid och påverkar vad som renderas:

```
┌─────────────────────────────────────────────────────────────────┐
│                      STATE vs PROPS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PROPS                          STATE                           │
│  ─────                          ─────                           │
│  • Kommer från parent          • Ägs av komponenten själv       │
│  • Read-only                   • Kan ändras via setter          │
│  • Kan inte ändras             • Triggar re-render vid ändring  │
│  • Flödar nedåt                • Privat till komponenten        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### useState Hook

```tsx
import { useState } from 'react';

function Counter() {
  // useState returnerar [värde, setterFunktion]
  const [count, setCount] = useState(0);  // 0 är initial value

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

### Functional Updates

När ny state beror på föregående state, använd functional update:

```tsx
function Counter() {
  const [count, setCount] = useState(0);

  // ❌ Problem: Om du klickar snabbt kanske inte alla klick räknas
  const incrementBad = () => setCount(count + 1);

  // ✅ Lösning: Functional update garanterar senaste värde
  const incrementGood = () => setCount(prev => prev + 1);

  // Användbart för batch-operationer
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

### Object State

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

  // ❌ FEL: Mutera aldrig state direkt
  const badUpdate = () => {
    user.name = 'New Name';  // Detta triggar INTE re-render!
  };

  // ✅ RÄTT: Skapa nytt objekt med spread
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
      <label>
        <input
          type="checkbox"
          checked={user.preferences.notifications}
          onChange={toggleNotifications}
        />
        Enable notifications
      </label>
    </form>
  );
}
```

### Array State

```tsx
interface Task {
  id: string;
  title: string;
  completed: boolean;
}

function TaskList() {
  const [tasks, setTasks] = useState<Task[]>([]);

  // ADD - Lägg till i slutet
  const addTask = (title: string) => {
    const newTask: Task = {
      id: crypto.randomUUID(),
      title,
      completed: false
    };
    setTasks([...tasks, newTask]);  // Spread + new item
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

  // REORDER - Sortera
  const sortByCompleted = () => {
    setTasks([...tasks].sort((a, b) =>
      Number(a.completed) - Number(b.completed)
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

---

## 💻 State Management Patterns

### Multiple State Variables vs Object

```tsx
// Option 1: Separata state-variabler (ofta bättre)
function Form() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState(0);

  // Fördel: Enkelt att uppdatera individuellt
  // Nackdel: Många useState-calls
}

// Option 2: Object state (för relaterad data)
function Form() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: 0
  });

  const updateField = (field: string, value: string | number) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  // Fördel: All relaterad data tillsammans
  // Nackdel: Måste alltid spread'a
}
```

### Lazy Initial State

```tsx
// ❌ Körs varje render (onödigt)
const [items, setItems] = useState(
  JSON.parse(localStorage.getItem('items') || '[]')
);

// ✅ Körs bara första gången (lazy)
const [items, setItems] = useState(() => {
  const saved = localStorage.getItem('items');
  return saved ? JSON.parse(saved) : [];
});
```

---

## ⚠️ Vanliga Problem

### Problem 1: State uppdateras inte direkt

```tsx
function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
    console.log(count);  // Fortfarande 0! State uppdateras inte synkront
  };

  // State är nytt nästa render, inte direkt efter setCount
}
```

### Problem 2: Stale closure

```tsx
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      // ❌ count är alltid 0 (stale closure)
      setCount(count + 1);
    }, 1000);

    return () => clearInterval(id);
  }, []);  // Tom dependency array = count fångas vid mount

  // ✅ Lösning: Functional update
  useEffect(() => {
    const id = setInterval(() => {
      setCount(prev => prev + 1);  // Alltid senaste värdet
    }, 1000);
    return () => clearInterval(id);
  }, []);
}
```

---

## 🎮 Praktisk Övning

Bygg en shopping cart:

```tsx
interface Product {
  id: string;
  name: string;
  price: number;
}

interface CartItem extends Product {
  quantity: number;
}

function ShoppingCart() {
  const [cart, setCart] = useState<CartItem[]>([]);

  const addToCart = (product: Product) => {
    setCart(prev => {
      const existing = prev.find(item => item.id === product.id);
      if (existing) {
        return prev.map(item =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }
      return [...prev, { ...product, quantity: 1 }];
    });
  };

  const removeFromCart = (productId: string) => {
    setCart(prev => prev.filter(item => item.id !== productId));
  };

  const updateQuantity = (productId: string, quantity: number) => {
    if (quantity <= 0) {
      removeFromCart(productId);
      return;
    }
    setCart(prev =>
      prev.map(item =>
        item.id === productId ? { ...item, quantity } : item
      )
    );
  };

  const total = cart.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <div>
      <h2>Shopping Cart</h2>
      {cart.map(item => (
        <div key={item.id} className="cart-item">
          <span>{item.name}</span>
          <input
            type="number"
            value={item.quantity}
            onChange={(e) => updateQuantity(item.id, Number(e.target.value))}
            min={0}
          />
          <span>${(item.price * item.quantity).toFixed(2)}</span>
          <button onClick={() => removeFromCart(item.id)}>Remove</button>
        </div>
      ))}
      <p className="total">Total: ${total.toFixed(2)}</p>
    </div>
  );
}
```

---

## ✅ Sammanfattning

- **useState** returnerar `[value, setter]`
- **Functional updates** (`prev => prev + 1`) för state som beror på föregående
- **Immutability** - mutera aldrig state, skapa nya objekt/arrayer
- **Lazy initial state** med function för dyra beräkningar
- State-uppdateringar är **asynkrona** och batch'as
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

> *"Effects let you run code after rendering, outside React's pure render phase."*

---

## 🎯 Why This Matters

De flesta React-appar behöver göra mer än att bara rendera UI:
- Hämta data från API:er
- Sätta upp event listeners
- Manipulera DOM direkt
- Synka med externa system

useEffect är hur du hanterar dessa "side effects".

---

## 🧠 Core Concepts

### Vad är en Side Effect?

```
┌─────────────────────────────────────────────────────────────────┐
│                      PURE vs SIDE EFFECTS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PURE RENDER (Reacts jobb)          SIDE EFFECTS (useEffect)   │
│  ─────────────────────────          ────────────────────────   │
│  • Beräkna JSX från props/state    • API-anrop                 │
│  • Deterministiskt                 • DOM-manipulation          │
│  • Inga externa beroenden          • Event listeners           │
│  • Samma input = samma output      • Timers/intervals          │
│                                    • LocalStorage              │
│                                    • WebSocket connections      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### useEffect Syntax

```tsx
import { useEffect } from 'react';

function Component() {
  useEffect(() => {
    // Din side effect-kod här
    console.log('Effect körs');

    // Cleanup function (valfri)
    return () => {
      console.log('Cleanup körs');
    };
  }, [/* dependencies */]);
}
```

### Dependency Array

```tsx
// Körs efter VARJE render
useEffect(() => {
  console.log('Körs varje gång');
});

// Körs bara vid MOUNT (och cleanup vid UNMOUNT)
useEffect(() => {
  console.log('Körs en gång');
  return () => console.log('Cleanup vid unmount');
}, []);

// Körs när specifika värden ÄNDRAS
useEffect(() => {
  console.log('userId ändrades till:', userId);
}, [userId]);

// Flera dependencies
useEffect(() => {
  console.log('userId eller filter ändrades');
}, [userId, filter]);
```

### Data Fetching

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
    // Reset state när userId ändras
    setLoading(true);
    setError(null);

    // AbortController för att kunna avbryta fetch
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

    // Cleanup: Avbryt pågående request om userId ändras
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

### Event Listeners

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

    // Lägg till listener
    window.addEventListener('resize', handleResize);

    // CLEANUP: Ta bort listener vid unmount
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);  // Tom array = körs bara vid mount/unmount

  return <p>Window: {size.width} x {size.height}</p>;
}
```

### Subscriptions

```tsx
function LiveStatus({ serverId }: { serverId: string }) {
  const [status, setStatus] = useState<'online' | 'offline'>('offline');

  useEffect(() => {
    // Skapa WebSocket-anslutning
    const ws = new WebSocket(`wss://api.example.com/status/${serverId}`);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setStatus(data.status);
    };

    ws.onerror = () => setStatus('offline');

    // CLEANUP: Stäng anslutning
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

---

## 💻 Advanced Patterns

### Sync med Local Storage

```tsx
function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    const saved = localStorage.getItem(key);
    return saved ? JSON.parse(saved) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}

// Användning
function Settings() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');
  // theme sparas automatiskt till localStorage
}
```

### Document Title

```tsx
function useDocumentTitle(title: string) {
  useEffect(() => {
    const previousTitle = document.title;
    document.title = title;

    return () => {
      document.title = previousTitle;
    };
  }, [title]);
}

// Användning
function ProfilePage({ user }: { user: User }) {
  useDocumentTitle(`${user.name} - Profile`);
  return <div>...</div>;
}
```

---

## ⚠️ Vanliga Problem

### Problem 1: Infinite loop

```tsx
// ❌ INFINITE LOOP!
function Bad() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(setData);
  });  // SAKNAR dependency array!
}

// ✅ RÄTT
function Good() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(setData);
  }, []);  // Tom array = körs bara en gång
}
```

### Problem 2: Missing dependencies

```tsx
// ❌ ESLint varnar: Missing dependency 'userId'
useEffect(() => {
  fetchUser(userId);
}, []);

// ✅ Inkludera alla dependencies
useEffect(() => {
  fetchUser(userId);
}, [userId]);
```

### Problem 3: Cleanup missas

```tsx
// ❌ Memory leak - interval fortsätter efter unmount
useEffect(() => {
  setInterval(() => {
    setCount(c => c + 1);
  }, 1000);
}, []);

// ✅ Cleanup stoppar interval
useEffect(() => {
  const id = setInterval(() => {
    setCount(c => c + 1);
  }, 1000);

  return () => clearInterval(id);
}, []);
```

---

## 🎮 Praktisk Övning

Bygg en real-time search med debouncing:

```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  // Debounce search query med 300ms delay
  const debouncedQuery = useDebounce(query, 300);

  useEffect(() => {
    if (!debouncedQuery) {
      setResults([]);
      return;
    }

    const controller = new AbortController();
    setLoading(true);

    fetch(`/api/search?q=${encodeURIComponent(debouncedQuery)}`, {
      signal: controller.signal
    })
      .then(res => res.json())
      .then(setResults)
      .catch(() => {})
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [debouncedQuery]);

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      {loading && <p>Searching...</p>}
      <ul>
        {results.map((result, i) => (
          <li key={i}>{result}</li>
        ))}
      </ul>
    </div>
  );
}
```

---

## ✅ Sammanfattning

- **useEffect** för kod som körs efter render
- **Dependency array** styr när effect körs
- **Cleanup function** för att städa upp (listeners, timers, subscriptions)
- **Tom array** `[]` = körs bara vid mount
- **Alltid cleanup** för subscriptions och listeners
- Använd **AbortController** för fetch-requests
""",
}


# ============================================================================
# NODE 7: FORMS - USER INPUT
# ============================================================================

REACT_NODE_07_FORMS = {
    "node_id": 7,
    "title": "Forms - User Input",
    "slug": "react-forms",
    "description": "Hantera formulär och användarinput i React",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "controlled components", "uncontrolled components", "form submission",
        "validation", "react-hook-form", "zod", "formik"
    ],
    "content": """
# Forms - User Input

> *"Forms are the primary way users interact with web applications."*

---

## 🎯 Why This Matters

Formulär finns överallt - login, registrering, checkout, settings. Att hantera forms korrekt i React är en kärnkompetens.

---

## 🧠 Core Concepts

### Controlled vs Uncontrolled Components

```
┌─────────────────────────────────────────────────────────────────┐
│              CONTROLLED vs UNCONTROLLED                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CONTROLLED                       UNCONTROLLED                  │
│  ──────────                       ────────────                  │
│  • React styr värdet             • DOM styr värdet              │
│  • value + onChange              • ref + defaultValue           │
│  • Fullständig kontroll          • Enklare för enkla formulär   │
│  • Kan validera i realtid        • Mindre kod                   │
│  • Mer kod                       • Svårare att kontrollera      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Controlled Component

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

### Uncontrolled Component

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

### Form with Validation

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
    // Clear error when user starts typing
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
      // Success!
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

---

## 💻 React Hook Form (Recommended)

```tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

// Schema with Zod
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

---

## ⚠️ Vanliga Problem

### Problem 1: preventDefault glöms

```tsx
// ❌ Sidan laddas om!
const handleSubmit = () => {
  console.log('Submitting...');
};

// ✅ Förhindra default form submission
const handleSubmit = (e: React.FormEvent) => {
  e.preventDefault();
  console.log('Submitting...');
};
```

### Problem 2: Checkbox/Radio controlled

```tsx
// ❌ FEL - value istället för checked
<input type="checkbox" value={isChecked} />

// ✅ RÄTT - checked för boolean inputs
<input
  type="checkbox"
  checked={isChecked}
  onChange={(e) => setIsChecked(e.target.checked)}
/>
```

---

## 🎮 Praktisk Övning

Bygg ett komplett kontaktformulär:

```tsx
const contactSchema = z.object({
  name: z.string().min(2, 'Name too short'),
  email: z.string().email('Invalid email'),
  subject: z.enum(['support', 'sales', 'general']),
  message: z.string().min(10, 'Message too short').max(1000),
  priority: z.enum(['low', 'medium', 'high']),
  subscribe: z.boolean().default(false),
});

type ContactForm = z.infer<typeof contactSchema>;

function ContactPage() {
  const { register, handleSubmit, formState: { errors, isSubmitting } } =
    useForm<ContactForm>({
      resolver: zodResolver(contactSchema),
      defaultValues: {
        subject: 'general',
        priority: 'medium',
        subscribe: false,
      }
    });

  const onSubmit = async (data: ContactForm) => {
    await fetch('/api/contact', {
      method: 'POST',
      body: JSON.stringify(data),
    });
    alert('Message sent!');
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <Input {...register('name')} error={errors.name?.message} label="Name" />
      <Input {...register('email')} error={errors.email?.message} label="Email" type="email" />

      <Select {...register('subject')} label="Subject">
        <option value="support">Support</option>
        <option value="sales">Sales</option>
        <option value="general">General</option>
      </Select>

      <Textarea {...register('message')} error={errors.message?.message} label="Message" />

      <RadioGroup {...register('priority')} label="Priority">
        <Radio value="low">Low</Radio>
        <Radio value="medium">Medium</Radio>
        <Radio value="high">High</Radio>
      </RadioGroup>

      <Checkbox {...register('subscribe')} label="Subscribe to newsletter" />

      <Button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Sending...' : 'Send Message'}
      </Button>
    </form>
  );
}
```

---

## ✅ Sammanfattning

- **Controlled components** - React styr värdet via state
- **Uncontrolled components** - DOM styr, React läser via ref
- **Alltid `e.preventDefault()`** i onSubmit
- **React Hook Form + Zod** för produktionsformulär
- **Validera både client och server-side**
""",
}


# ============================================================================
# NODE 8: CUSTOM HOOKS
# ============================================================================

REACT_NODE_08_CUSTOM_HOOKS = {
    "node_id": 8,
    "title": "Custom Hooks - Reusable Logic",
    "slug": "custom-hooks",
    "description": "Skapa egna hooks för återanvändbar logik",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "custom hooks", "composition", "state logic reuse",
        "hook rules", "testing hooks"
    ],
    "content": """
# Custom Hooks - Reusable Logic

> *"Custom hooks let you extract component logic into reusable functions."*

---

## 🎯 Why This Matters

Custom hooks är ett av Reacts mest kraftfulla patterns. De låter dig:
- Återanvända stateful logic mellan komponenter
- Hålla komponenter rena och läsbara
- Bygga ett bibliotek av återanvändbara verktyg

---

## 🧠 Core Concepts

### Vad är en Custom Hook?

En custom hook är en funktion som:
1. Börjar med `use` prefix
2. Kan använda andra hooks
3. Returnerar data och/eller funktioner

```tsx
// Custom hook
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);

  const increment = () => setCount(c => c + 1);
  const decrement = () => setCount(c => c - 1);
  const reset = () => setCount(initialValue);

  return { count, increment, decrement, reset };
}

// Användning
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

### useLocalStorage

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

// Användning
function Settings() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');
  const [language, setLanguage] = useLocalStorage('language', 'en');

  return (
    <div>
      <select value={theme} onChange={e => setTheme(e.target.value)}>
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </div>
  );
}
```

### useFetch

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

// Användning
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

### useDebounce

```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// Användning
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

### useMediaQuery

```tsx
function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState(false);

  useEffect(() => {
    const media = window.matchMedia(query);
    setMatches(media.matches);

    const listener = (e: MediaQueryListEvent) => setMatches(e.matches);
    media.addEventListener('change', listener);

    return () => media.removeEventListener('change', listener);
  }, [query]);

  return matches;
}

// Användning
function ResponsiveNav() {
  const isMobile = useMediaQuery('(max-width: 768px)');

  return isMobile ? <MobileMenu /> : <DesktopNav />;
}
```

### useOnClickOutside

```tsx
function useOnClickOutside(
  ref: RefObject<HTMLElement>,
  handler: () => void
) {
  useEffect(() => {
    const listener = (event: MouseEvent | TouchEvent) => {
      if (!ref.current || ref.current.contains(event.target as Node)) {
        return;
      }
      handler();
    };

    document.addEventListener('mousedown', listener);
    document.addEventListener('touchstart', listener);

    return () => {
      document.removeEventListener('mousedown', listener);
      document.removeEventListener('touchstart', listener);
    };
  }, [ref, handler]);
}

// Användning
function Dropdown() {
  const [isOpen, setIsOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useOnClickOutside(ref, () => setIsOpen(false));

  return (
    <div ref={ref}>
      <button onClick={() => setIsOpen(true)}>Open</button>
      {isOpen && <DropdownMenu />}
    </div>
  );
}
```

---

## 💻 Hook Rules

```
┌─────────────────────────────────────────────────────────────────┐
│                       RULES OF HOOKS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. ✅ Anropa hooks på TOP LEVEL                                │
│     Aldrig i loops, conditions, eller nested functions          │
│                                                                  │
│  2. ✅ Anropa hooks bara från REACT FUNCTIONS                   │
│     React function components eller custom hooks                 │
│                                                                  │
│  3. ✅ Custom hooks börjar alltid med "use"                     │
│     useCounter, useFetch, useLocalStorage                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```tsx
// ❌ FEL - Hook i condition
function Bad({ shouldFetch }) {
  if (shouldFetch) {
    const data = useFetch('/api/data');  // ALDRIG!
  }
}

// ✅ RÄTT - Alltid anropa, villkora användningen
function Good({ shouldFetch }) {
  const data = useFetch(shouldFetch ? '/api/data' : null);
}
```

---

## 🎮 Praktisk Övning

Bygg ett useToggle hook-bibliotek:

```tsx
// hooks/useToggle.ts
function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  const toggle = useCallback(() => setValue(v => !v), []);
  const setTrue = useCallback(() => setValue(true), []);
  const setFalse = useCallback(() => setValue(false), []);

  return { value, toggle, setTrue, setFalse };
}

// hooks/useBoolean.ts (utökad version)
function useBoolean(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  const callbacks = useMemo(() => ({
    toggle: () => setValue(v => !v),
    on: () => setValue(true),
    off: () => setValue(false),
    set: setValue,
  }), []);

  return [value, callbacks] as const;
}

// Användning
function Modal() {
  const [isOpen, { on: open, off: close }] = useBoolean(false);

  return (
    <>
      <button onClick={open}>Open Modal</button>
      {isOpen && (
        <Dialog onClose={close}>
          <p>Modal content</p>
        </Dialog>
      )}
    </>
  );
}
```

---

## ✅ Sammanfattning

- **Custom hooks** börjar med `use` och kan använda andra hooks
- **Återanvänd stateful logic** utan att kopiera kod
- **Följ hook rules** - alltid top-level, bara i React functions
- **Komponera hooks** - bygg komplexa hooks från enkla
- **Testa hooks** med @testing-library/react-hooks
""",
}


# Export all nodes from Block 2
BLOCK_2_NODES = [
    REACT_NODE_05_USESTATE,
    REACT_NODE_06_USEEFFECT,
    REACT_NODE_07_FORMS,
    REACT_NODE_08_CUSTOM_HOOKS,
]
