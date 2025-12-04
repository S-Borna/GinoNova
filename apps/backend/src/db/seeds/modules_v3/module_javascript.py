"""
Javascript - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: advanced-specialty
Tasks: 20
Estimated Hours: 10.0
"""

MODULE_JAVASCRIPT = {
    "track_slug": "advanced-specialty",
    "order_index": 100,
    "name": "Javascript",
    "slug": "javascript",
    "description": """Master Javascript from fundamentals to production""",
    "difficulty": "intermediate",
    "estimated_hours": 10.0,
    "prerequisites": [],
    "tasks": [
            {
                "title": "JavaScript Introduction & Setup",
                "difficulty": "easy",
                "estimated_minutes": 30,
                "xp_reward": 150,
                "content": r"""
# JavaScript Introduction & Setup

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"JavaScript runs the web. And increasingly, the server, mobile, and everything in between."*

---

## 🎯 Why This Matters

JavaScript is everywhere:
- **Frontend:** Every website uses it
- **Backend:** Node.js powers millions of servers
- **DevOps:** npm scripts, automation, infrastructure tools
- **Cloud:** AWS Lambda, serverless functions

As a DevOps engineer, you'll encounter JavaScript in:
- CI/CD pipelines
- Infrastructure tooling
- Monitoring dashboards
- Automation scripts

---

## 🧠 Core Concepts

### What is JavaScript?

JavaScript is a:
- **Dynamic** language (types determined at runtime)
- **Interpreted** language (no compilation step)
- **Multi-paradigm** (OOP, functional, procedural)
- **Single-threaded** with async capabilities

```javascript
// Your first JavaScript
console.log("Hello, DevOps!");

// Variables
let name = "DevOps Hub";
const version = "1.0.0";

// Functions
function greet(user) {
    return `Welcome, ${user}!`;
}

console.log(greet("Engineer"));
```

### Running JavaScript

```bash
# In browser (F12 → Console)
# In Node.js
node script.js

# Interactive REPL
node
> 2 + 2
4
> .exit

# Run inline
node -e "console.log('Hello')"
```

### Development Environment

```bash
# Install Node.js (includes npm)
# macOS
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version   # v20.x.x
npm --version    # 10.x.x
```

### Project Setup

```bash
# Create new project
mkdir my-project && cd my-project

# Initialize package.json
npm init -y

# Project structure
my-project/
├── package.json
├── src/
│   └── index.js
├── test/
│   └── index.test.js
└── README.md
```

### package.json Basics

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "type": "module",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "node --watch src/index.js",
    "test": "node --test test/"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

---

## 💻 Essential Commands

```bash
# Run scripts from package.json
npm start
npm run dev
npm test

# Install packages
npm install lodash         # Production dependency
npm install -D jest        # Dev dependency
npm install -g typescript  # Global install

# Show installed packages
npm list
npm list -g --depth=0
```

---

## 🔥 Pro Tips

### 1. Use Node.js 20+ Features
```javascript
// Native test runner
node --test test/

// Watch mode (auto-reload)
node --watch src/index.js
```

### 2. ES Modules by Default
```json
// package.json
{
  "type": "module"
}
```

### 3. Use npx for One-off Commands
```bash
npx create-react-app my-app
npx prettier --write .
```

---

## ⚠️ Common Pitfalls

| Mistake | Problem | Solution |
|---------|---------|----------|
| Wrong Node version | Incompatible syntax | Use `nvm` to manage versions |
| Missing `type: module` | Import/export errors | Add to package.json |
| `npm install` in wrong dir | Wrong dependencies | Check you're in project root |

---

## 🛠️ Hands-on Exercise

### Task: Create a DevOps CLI Tool

1. Initialize a new npm project
2. Create `src/index.js` with:
   - Command-line argument parsing
   - A `greet` function
   - Version display
3. Add npm scripts for run and dev
4. Test with `npm start -- --help`

---

## 📚 Deep Dive Resources

- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Node.js Documentation](https://nodejs.org/docs/latest/api/)
- [JavaScript.info](https://javascript.info/)
"""
            },
            {
                "title": "Variables & Data Types",
                "difficulty": "easy",
                "estimated_minutes": 30,
                "xp_reward": 175,
                "content": r"""
# Variables & Data Types

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Understanding types in JavaScript means understanding why things sometimes go hilariously wrong."*

---

## 🎯 Why This Matters

JavaScript's dynamic typing is powerful but dangerous:
- Variables can hold any type
- Types can change at runtime
- Implicit coercion causes bugs

Mastering types prevents countless bugs.

---

## 🧠 Core Concepts

### Variable Declarations

```javascript
// const - can't be reassigned (use by default)
const API_URL = "https://api.example.com";
// API_URL = "other"; // Error!

// let - can be reassigned (when needed)
let count = 0;
count = 1;  // OK

// var - avoid (function-scoped, hoisted)
var old = "legacy";  // Don't use in modern JS
```

### Primitive Types

```javascript
// String
const name = "DevOps";
const template = `Hello, ${name}!`;  // Template literal

// Number (integers and floats)
const count = 42;
const price = 19.99;
const big = 1e6;  // 1000000

// BigInt (for very large numbers)
const huge = 9007199254740991n;

// Boolean
const isActive = true;
const isComplete = false;

// undefined (declared but no value)
let data;
console.log(data);  // undefined

// null (intentionally empty)
const result = null;

// Symbol (unique identifiers)
const id = Symbol("id");
```

### Type Checking

```javascript
// typeof operator
typeof "hello"     // "string"
typeof 42          // "number"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object" (historical bug!)
typeof {}          // "object"
typeof []          // "object" (arrays are objects)
typeof function(){} // "function"

// Better checks
Array.isArray([1, 2, 3])  // true
Number.isInteger(42)       // true
Number.isNaN(NaN)          // true
```

### Type Coercion

```javascript
// Implicit coercion (avoid!)
"5" + 3           // "53" (string concatenation)
"5" - 3           // 2 (numeric subtraction)
"5" * "2"         // 10
true + true       // 2
[] + []           // ""
[] + {}           // "[object Object]"
{} + []           // 0

// Explicit conversion (preferred)
Number("42")      // 42
String(42)        // "42"
Boolean(1)        // true
parseInt("42px")  // 42
parseFloat("3.14") // 3.14
```

### Truthy & Falsy

```javascript
// Falsy values (evaluate to false)
false
0
-0
0n
""
null
undefined
NaN

// Everything else is truthy
"0"    // truthy (non-empty string)
[]     // truthy (empty array)
{}     // truthy (empty object)

// Use in conditions
if (value) {
    // value is truthy
}

// Explicit boolean conversion
Boolean("hello")  // true
!!""              // false (double negation trick)
```

### Template Literals

```javascript
const name = "DevOps";
const count = 5;

// Basic interpolation
const msg = `Hello, ${name}!`;

// Expressions
const result = `Total: ${count * 10}`;

// Multi-line strings
const html = `
<div>
    <h1>${name}</h1>
    <p>Count: ${count}</p>
</div>
`;

// Tagged templates (advanced)
function highlight(strings, ...values) {
    return strings.reduce((acc, str, i) =>
        acc + str + (values[i] ? `<mark>${values[i]}</mark>` : ""), "");
}

const output = highlight`Hello ${name}!`;  // Hello <mark>DevOps</mark>!
```

---

## 💻 Essential Patterns

```javascript
// Default values
const port = process.env.PORT || 3000;
const name = config.name ?? "default";  // Nullish coalescing

// Type guards
function processValue(value) {
    if (typeof value === "string") {
        return value.toUpperCase();
    }
    if (typeof value === "number") {
        return value * 2;
    }
    return value;
}

// Safe property access
const user = { profile: { name: "John" } };
const name = user?.profile?.name;  // "John"
const age = user?.profile?.age ?? 0;  // 0
```

---

## 🔥 Pro Tips

### 1. Always Use const by Default
```javascript
const config = { port: 3000 };  // Object can be mutated
config.port = 8080;  // OK
// config = {};  // Error
```

### 2. Use Strict Equality
```javascript
// ❌ Loose equality (coerces types)
"5" == 5   // true

// ✅ Strict equality (no coercion)
"5" === 5  // false
```

### 3. Use Optional Chaining
```javascript
const email = user?.contact?.email ?? "N/A";
```

---

## 🛠️ Hands-on Exercise

### Task: Type Validator

Create functions that:
1. Check if value is a valid port number (1-65535)
2. Safely parse JSON with fallback
3. Convert various inputs to boolean
4. Handle null/undefined gracefully

---

## 📚 Deep Dive Resources

- [MDN: JavaScript Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [JavaScript Type Coercion Explained](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/)
"""
            },
            {
                "title": "Operators & Expressions",
                "difficulty": "easy",
                "estimated_minutes": 30,
                "xp_reward": 175,
                "content": r"""
# Operators & Expressions

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"JavaScript operators are intuitive... until they're not."*

---

## 🎯 Why This Matters

Operators are the building blocks of logic:
- Calculate values
- Compare data
- Control flow
- Transform data

Understanding operators prevents subtle bugs.

---

## 🧠 Core Concepts

### Arithmetic Operators

```javascript
// Basic math
10 + 5    // 15 (addition)
10 - 5    // 5  (subtraction)
10 * 5    // 50 (multiplication)
10 / 5    // 2  (division)
10 % 3    // 1  (modulo/remainder)
10 ** 2   // 100 (exponentiation)

// Increment/Decrement
let count = 0;
count++;  // 1 (post-increment)
++count;  // 2 (pre-increment)
count--;  // 1 (post-decrement)

// Assignment operators
let x = 10;
x += 5;   // x = x + 5 = 15
x -= 3;   // x = x - 3 = 12
x *= 2;   // x = x * 2 = 24
x /= 4;   // x = x / 4 = 6
x **= 2;  // x = x ** 2 = 36
```

### Comparison Operators

```javascript
// Equality
5 == "5"   // true  (loose, coerces types)
5 === "5"  // false (strict, no coercion)
5 != "5"   // false (loose inequality)
5 !== "5"  // true  (strict inequality)

// Relational
5 > 3      // true
5 >= 5     // true
3 < 5      // true
3 <= 3     // true

// String comparison (lexicographic)
"apple" < "banana"  // true
"10" < "9"          // true (string comparison!)
```

### Logical Operators

```javascript
// AND - returns first falsy or last value
true && true    // true
true && false   // false
"hello" && 42   // 42
null && "test"  // null

// OR - returns first truthy or last value
true || false   // true
false || "default"  // "default"
null || undefined || "fallback"  // "fallback"

// NOT - inverts truthiness
!true           // false
!0              // true
!!"hello"       // true (double negation = boolean)

// Nullish Coalescing (??) - only null/undefined
null ?? "default"      // "default"
undefined ?? "default" // "default"
0 ?? "default"         // 0 (not null/undefined)
"" ?? "default"        // "" (not null/undefined)
```

### Short-Circuit Evaluation

```javascript
// AND short-circuits on first falsy
const result = condition && expensiveOperation();

// OR short-circuits on first truthy
const value = cached || fetchFromDatabase();

// Practical patterns
const config = userConfig && userConfig.settings;
const port = process.env.PORT || 3000;
const name = data?.name ?? "Anonymous";
```

### Ternary Operator

```javascript
// condition ? valueIfTrue : valueIfFalse
const status = isActive ? "active" : "inactive";

// Nested (avoid excessive nesting)
const level = score > 90 ? "A"
            : score > 80 ? "B"
            : score > 70 ? "C"
            : "F";

// With nullish
const display = value != null ? value : "N/A";
```

### Optional Chaining (?.)

```javascript
const user = {
    profile: {
        email: "test@example.com"
    }
};

// Safe property access
user?.profile?.email        // "test@example.com"
user?.settings?.theme       // undefined (no error)

// With method calls
user?.getProfile?.()        // undefined if no method

// With arrays
const first = arr?.[0];

// Combining with nullish coalescing
const theme = user?.settings?.theme ?? "dark";
```

### Spread & Rest Operators

```javascript
// Spread - expand elements
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];  // [1, 2, 3, 4, 5]

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };  // { a: 1, b: 2, c: 3 }

// Rest - collect elements
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3, 4);  // 10

// Destructuring with rest
const [first, ...rest] = [1, 2, 3, 4];
// first = 1, rest = [2, 3, 4]

const { name, ...others } = { name: "John", age: 30, city: "NYC" };
// name = "John", others = { age: 30, city: "NYC" }
```

---

## 💻 Essential Patterns

```javascript
// Toggle boolean
let isOpen = false;
isOpen = !isOpen;  // true

// Clamp value
const clamped = Math.min(Math.max(value, min), max);

// Default object values
const config = { ...defaults, ...userConfig };

// Conditional object properties
const user = {
    name: "John",
    ...(isAdmin && { role: "admin" }),
};
```

---

## 🔥 Pro Tips

### 1. Use ?? for Defaults (Not ||)
```javascript
// ❌ || treats 0 and "" as falsy
const count = data.count || 10;  // 10 if count is 0

// ✅ ?? only replaces null/undefined
const count = data.count ?? 10;  // 0 if count is 0
```

### 2. Chain Optional Access
```javascript
const city = user?.address?.city ?? "Unknown";
```

### 3. Merge Objects Safely
```javascript
const merged = { ...defaults, ...overrides };
```

---

## 🛠️ Hands-on Exercise

### Task: Config Merger

Create a function that:
1. Merges default config with user config
2. Uses nullish coalescing for missing values
3. Validates numeric ranges with clamping
4. Returns frozen (immutable) result

---

## 📚 Deep Dive Resources

- [MDN: Expressions and Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)
- [JavaScript Operators Explained](https://javascript.info/operators)
"""
            },
            {
                "title": "Conditionals — if, switch, and Patterns",
                "difficulty": "easy",
                "estimated_minutes": 30,
                "xp_reward": 175,
                "content": r"""
# Conditionals — if, switch, and Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Code that can't make decisions is just a calculator."*

---

## 🎯 Why This Matters

Every program needs to:
- Validate input
- Handle different cases
- Respond to conditions
- Branch logic

Clean conditionals = readable code.

---

## 🧠 Core Concepts

### if / else if / else

```javascript
const status = "active";

if (status === "active") {
    console.log("User is active");
} else if (status === "pending") {
    console.log("User is pending");
} else {
    console.log("Unknown status");
}

// Single line (no braces for one statement)
if (isValid) doSomething();

// Block form (always recommended)
if (isValid) {
    doSomething();
}
```

### Ternary Operator

```javascript
// Simple condition
const message = isLoggedIn ? "Welcome back!" : "Please log in";

// Nested (use sparingly)
const access = isAdmin
    ? "full"
    : isUser
        ? "limited"
        : "none";

// In template literals
console.log(`Status: ${isActive ? "Active" : "Inactive"}`);
```

### switch Statement

```javascript
const action = "deploy";

switch (action) {
    case "build":
        console.log("Building...");
        break;
    case "test":
        console.log("Testing...");
        break;
    case "deploy":
        console.log("Deploying...");
        break;
    default:
        console.log("Unknown action");
}

// Fall-through (intentional)
switch (day) {
    case "Saturday":
    case "Sunday":
        console.log("Weekend!");
        break;
    default:
        console.log("Weekday");
}

// Return in switch (no break needed)
function getColor(status) {
    switch (status) {
        case "success": return "green";
        case "warning": return "yellow";
        case "error": return "red";
        default: return "gray";
    }
}
```

### Object Lookup Pattern

```javascript
// Instead of switch/if-else chain
const statusColors = {
    success: "green",
    warning: "yellow",
    error: "red",
    default: "gray"
};

const color = statusColors[status] ?? statusColors.default;

// With functions
const actions = {
    build: () => runBuild(),
    test: () => runTests(),
    deploy: () => runDeploy()
};

actions[action]?.() ?? console.log("Unknown action");
```

### Guard Clauses

```javascript
// ❌ Nested conditions (pyramid of doom)
function processUser(user) {
    if (user) {
        if (user.isActive) {
            if (user.hasPermission) {
                // finally do something
            }
        }
    }
}

// ✅ Guard clauses (early return)
function processUser(user) {
    if (!user) return;
    if (!user.isActive) return;
    if (!user.hasPermission) return;

    // do something
}
```

### Nullish Checks

```javascript
// Check for null/undefined
if (value == null) {  // matches null AND undefined
    console.log("Value is null or undefined");
}

// Check for existence
if (value != null) {
    console.log("Value exists");
}

// With optional chaining
if (user?.profile?.email) {
    sendEmail(user.profile.email);
}
```

---

## 💻 Essential Patterns

```javascript
// Default assignment
const port = config.port ?? 3000;

// Conditional execution
isAdmin && deleteUser(id);

// Feature flags
const features = {
    darkMode: true,
    betaFeatures: false
};

if (features.darkMode) {
    enableDarkMode();
}

// Type-based handling
function process(value) {
    if (typeof value === "string") return value.trim();
    if (typeof value === "number") return value.toFixed(2);
    if (Array.isArray(value)) return value.length;
    return null;
}
```

---

## 🔥 Pro Tips

### 1. Use Object Maps for Many Cases
```javascript
const handlers = {
    GET: handleGet,
    POST: handlePost,
    PUT: handlePut,
    DELETE: handleDelete
};

handlers[method]?.(request);
```

### 2. Early Returns Keep Code Flat
```javascript
function validate(data) {
    if (!data) return { error: "No data" };
    if (!data.name) return { error: "Name required" };
    return { success: true };
}
```

---

## 🛠️ Hands-on Exercise

### Task: HTTP Router

Create a simple router that:
1. Matches method (GET, POST, etc.)
2. Matches path patterns
3. Returns appropriate handlers
4. Uses object lookup instead of switch

---

## 📚 Deep Dive Resources

- [MDN: Control Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
"""
            },
            {
                "title": "Loops — Iteration Patterns",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 200,
                "content": r"""
# Loops — Iteration Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Modern JavaScript prefers functional iteration, but knowing all forms makes you versatile."*

---

## 🎯 Why This Matters

Iteration is everywhere:
- Process arrays of data
- Handle API responses
- Transform collections
- Repeat operations

Choosing the right loop = cleaner code.

---

## 🧠 Core Concepts

### Traditional for Loop

```javascript
// Basic for
for (let i = 0; i < 5; i++) {
    console.log(i);  // 0, 1, 2, 3, 4
}

// Reverse iteration
for (let i = array.length - 1; i >= 0; i--) {
    console.log(array[i]);
}

// With step
for (let i = 0; i < 100; i += 10) {
    console.log(i);  // 0, 10, 20, ...
}
```

### for...of (Iterables)

```javascript
const servers = ["web01", "web02", "db01"];

// Iterate values
for (const server of servers) {
    console.log(server);
}

// With index (using entries)
for (const [index, server] of servers.entries()) {
    console.log(`${index}: ${server}`);
}

// Strings are iterable
for (const char of "hello") {
    console.log(char);
}

// Maps
const map = new Map([["a", 1], ["b", 2]]);
for (const [key, value] of map) {
    console.log(`${key}: ${value}`);
}
```

### for...in (Object Properties)

```javascript
const config = { host: "localhost", port: 3000 };

// Iterate keys
for (const key in config) {
    console.log(`${key}: ${config[key]}`);
}

// ⚠️ Includes inherited properties!
// Use hasOwnProperty or Object.keys instead
for (const key in config) {
    if (config.hasOwnProperty(key)) {
        console.log(key);
    }
}
```

### while / do...while

```javascript
// while - check first
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

// do...while - execute at least once
let attempts = 0;
do {
    console.log(`Attempt ${attempts + 1}`);
    attempts++;
} while (attempts < 3 && !success);
```

### Array Methods (Functional)

```javascript
const numbers = [1, 2, 3, 4, 5];

// forEach - side effects, no return
numbers.forEach((n, i) => console.log(`${i}: ${n}`));

// map - transform each element
const doubled = numbers.map(n => n * 2);  // [2, 4, 6, 8, 10]

// filter - keep matching elements
const even = numbers.filter(n => n % 2 === 0);  // [2, 4]

// find - first match
const found = numbers.find(n => n > 3);  // 4

// findIndex - index of first match
const index = numbers.findIndex(n => n > 3);  // 3

// some - any match?
const hasLarge = numbers.some(n => n > 4);  // true

// every - all match?
const allPositive = numbers.every(n => n > 0);  // true

// reduce - accumulate
const sum = numbers.reduce((acc, n) => acc + n, 0);  // 15
```

### Loop Control

```javascript
// break - exit loop
for (const item of items) {
    if (item === target) {
        console.log("Found!");
        break;
    }
}

// continue - skip iteration
for (const file of files) {
    if (file.startsWith(".")) {
        continue;  // Skip hidden files
    }
    process(file);
}

// Labels (rarely needed)
outer: for (const row of matrix) {
    for (const cell of row) {
        if (cell === target) {
            break outer;  // Exit both loops
        }
    }
}
```

---

## 💻 Essential Patterns

```javascript
// Transform API response
const users = response.data.map(user => ({
    id: user.id,
    name: `${user.firstName} ${user.lastName}`,
    email: user.email.toLowerCase()
}));

// Filter and transform
const activeAdmins = users
    .filter(u => u.isActive && u.role === "admin")
    .map(u => u.name);

// Group by property
const byStatus = items.reduce((acc, item) => {
    const key = item.status;
    acc[key] = acc[key] || [];
    acc[key].push(item);
    return acc;
}, {});

// Async iteration
for await (const chunk of stream) {
    process(chunk);
}
```

---

## 🔥 Pro Tips

### 1. Prefer Array Methods Over Loops
```javascript
// ❌ Imperative
const results = [];
for (const item of items) {
    if (item.active) {
        results.push(item.name);
    }
}

// ✅ Functional
const results = items
    .filter(item => item.active)
    .map(item => item.name);
```

### 2. Use for...of for Simple Iteration
```javascript
for (const item of items) {
    // Clean and readable
}
```

### 3. Chain Array Methods
```javascript
const result = data
    .filter(Boolean)        // Remove falsy
    .map(transform)         // Transform
    .sort((a, b) => a - b); // Sort
```

---

## 🛠️ Hands-on Exercise

### Task: Log Processor

Process log entries to:
1. Filter by log level (ERROR, WARN)
2. Extract timestamps and messages
3. Group by hour
4. Count occurrences

---

## 📚 Deep Dive Resources

- [MDN: Loops and Iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
- [Array Methods Visualized](https://arrayexplorer.netlify.app/)
"""
            },
            {
                "title": "Functions — Declaration to Arrow",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 225,
                "content": r"""
# Functions — Declaration to Arrow

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Functions are first-class citizens in JavaScript. Treat them like the VIPs they are."*

---

## 🎯 Why This Matters

Functions are the building blocks:
- Organize code
- Enable reuse
- Create abstractions
- Enable functional programming

JavaScript has multiple function syntaxes — know them all.

---

## 🧠 Core Concepts

### Function Declaration

```javascript
// Declaration (hoisted)
function greet(name) {
    return `Hello, ${name}!`;
}

// Can be called before declaration (hoisting)
sayHi();  // Works!

function sayHi() {
    console.log("Hi!");
}
```

### Function Expression

```javascript
// Expression (not hoisted)
const greet = function(name) {
    return `Hello, ${name}!`;
};

// Named function expression (useful for recursion/debugging)
const factorial = function fact(n) {
    return n <= 1 ? 1 : n * fact(n - 1);
};
```

### Arrow Functions

```javascript
// Arrow syntax
const greet = (name) => {
    return `Hello, ${name}!`;
};

// Implicit return (no braces)
const greet = (name) => `Hello, ${name}!`;

// Single parameter (no parentheses)
const double = n => n * 2;

// No parameters
const getRandom = () => Math.random();

// Return object (wrap in parentheses)
const createUser = (name) => ({ name, id: Date.now() });

// ⚠️ Arrow functions don't have their own 'this'
const obj = {
    name: "Object",
    regular: function() { return this.name; },  // "Object"
    arrow: () => this.name  // undefined (or global)
};
```

### Parameters

```javascript
// Default parameters
function connect(host = "localhost", port = 3000) {
    return `${host}:${port}`;
}

connect();              // "localhost:3000"
connect("db.local");    // "db.local:3000"

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3, 4);  // 10

// Destructured parameters
function createUser({ name, email, role = "user" }) {
    return { name, email, role };
}

createUser({ name: "John", email: "john@example.com" });
```

### Higher-Order Functions

```javascript
// Function that returns a function
function createMultiplier(factor) {
    return (number) => number * factor;
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

double(5);  // 10
triple(5);  // 15

// Function that takes a function
function withLogging(fn) {
    return (...args) => {
        console.log(`Calling with: ${args}`);
        const result = fn(...args);
        console.log(`Result: ${result}`);
        return result;
    };
}

const loggedAdd = withLogging((a, b) => a + b);
loggedAdd(2, 3);  // Logs and returns 5
```

### Closures

```javascript
// Functions remember their scope
function createCounter() {
    let count = 0;
    return {
        increment: () => ++count,
        decrement: () => --count,
        get: () => count
    };
}

const counter = createCounter();
counter.increment();  // 1
counter.increment();  // 2
counter.get();        // 2

// Practical closure: private state
function createCache() {
    const cache = new Map();
    return {
        get: (key) => cache.get(key),
        set: (key, value) => cache.set(key, value),
        has: (key) => cache.has(key)
    };
}
```

### IIFE (Immediately Invoked)

```javascript
// Execute immediately
(function() {
    const secret = "hidden";
    console.log("IIFE executed");
})();

// Arrow IIFE
(() => {
    console.log("Arrow IIFE");
})();

// With parameters
((name) => {
    console.log(`Hello, ${name}!`);
})("World");
```

---

## 💻 Essential Patterns

```javascript
// Currying
const add = (a) => (b) => a + b;
const add5 = add(5);
add5(3);  // 8

// Composition
const compose = (...fns) => (x) =>
    fns.reduceRight((acc, fn) => fn(acc), x);

const processName = compose(
    s => s.trim(),
    s => s.toLowerCase(),
    s => s.replace(/\s+/g, "-")
);

processName("  Hello World  ");  // "hello-world"

// Memoization
function memoize(fn) {
    const cache = new Map();
    return (...args) => {
        const key = JSON.stringify(args);
        if (!cache.has(key)) {
            cache.set(key, fn(...args));
        }
        return cache.get(key);
    };
}

const memoizedFetch = memoize(fetchData);
```

---

## 🔥 Pro Tips

### 1. Use Arrow Functions for Callbacks
```javascript
const doubled = numbers.map(n => n * 2);
```

### 2. Use Regular Functions for Methods
```javascript
const obj = {
    name: "Object",
    getName() {  // Shorthand method
        return this.name;
    }
};
```

### 3. Destructure for Clarity
```javascript
const processUser = ({ name, email }) => {
    // Clear what the function expects
};
```

---

## 🛠️ Hands-on Exercise

### Task: Function Utilities

Create:
1. `pipe` - compose functions left to right
2. `debounce` - delay execution
3. `throttle` - limit execution rate
4. `retry` - retry failed operations

---

## 📚 Deep Dive Resources

- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [JavaScript Closures Explained](https://javascript.info/closure)
"""
            },
            {
                "title": "Arrays — The Swiss Army Knife",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 225,
                "content": r"""
# Arrays — The Swiss Army Knife

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Arrays are the workhorse of JavaScript data manipulation."*

---

## 🎯 Why This Matters

Arrays are everywhere:
- API responses
- Log entries
- Configuration lists
- User collections

Master arrays = master JavaScript.

---

## 🧠 Core Concepts

### Array Creation

```javascript
// Literal notation (preferred)
const servers = ["web01", "web02", "db01"];

// Constructor (rarely needed)
const arr = new Array(3);  // [empty × 3]
const filled = Array(3).fill(0);  // [0, 0, 0]

// Array.from - convert iterables
Array.from("hello");  // ["h", "e", "l", "l", "o"]
Array.from({ length: 5 }, (_, i) => i);  // [0, 1, 2, 3, 4]

// Array.of - create from arguments
Array.of(1, 2, 3);  // [1, 2, 3]
```

### Accessing Elements

```javascript
const arr = ["a", "b", "c", "d", "e"];

arr[0]      // "a"
arr[arr.length - 1]  // "e" (last)
arr.at(-1)  // "e" (ES2022)
arr.at(-2)  // "d"

// Destructuring
const [first, second, ...rest] = arr;
// first = "a", second = "b", rest = ["c", "d", "e"]

// Skip elements
const [, , third] = arr;  // third = "c"
```

### Modifying Arrays

```javascript
const arr = [1, 2, 3];

// Add elements
arr.push(4);       // [1, 2, 3, 4] - end
arr.unshift(0);    // [0, 1, 2, 3, 4] - start

// Remove elements
arr.pop();         // [0, 1, 2, 3] - removes last
arr.shift();       // [1, 2, 3] - removes first

// Splice - add/remove at position
const months = ["Jan", "March", "April"];
months.splice(1, 0, "Feb");  // Insert at index 1
// ["Jan", "Feb", "March", "April"]

months.splice(2, 1);  // Remove 1 element at index 2
// ["Jan", "Feb", "April"]

months.splice(2, 1, "March");  // Replace at index 2
// ["Jan", "Feb", "March"]
```

### Non-Mutating Methods

```javascript
const arr = [1, 2, 3, 4, 5];

// slice - extract portion (doesn't modify)
arr.slice(1, 3)    // [2, 3]
arr.slice(-2)      // [4, 5]
arr.slice()        // [1, 2, 3, 4, 5] (copy)

// concat - combine arrays
arr.concat([6, 7])  // [1, 2, 3, 4, 5, 6, 7]

// spread operator (preferred for concat)
[...arr, 6, 7]      // [1, 2, 3, 4, 5, 6, 7]
[0, ...arr]         // [0, 1, 2, 3, 4, 5]
```

### Searching

```javascript
const fruits = ["apple", "banana", "cherry", "banana"];

// indexOf / lastIndexOf
fruits.indexOf("banana")      // 1
fruits.lastIndexOf("banana")  // 3
fruits.indexOf("grape")       // -1

// includes (ES7)
fruits.includes("apple")  // true

// find / findIndex
const users = [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" }
];

users.find(u => u.id === 2)       // { id: 2, name: "Jane" }
users.findIndex(u => u.id === 2)  // 1
```

### Transforming

```javascript
const numbers = [1, 2, 3, 4, 5];

// map - transform each element
const doubled = numbers.map(n => n * 2);  // [2, 4, 6, 8, 10]

// filter - keep matching
const even = numbers.filter(n => n % 2 === 0);  // [2, 4]

// reduce - accumulate
const sum = numbers.reduce((acc, n) => acc + n, 0);  // 15

// flat - flatten nested arrays
[[1, 2], [3, 4]].flat()  // [1, 2, 3, 4]
[[1, [2, 3]], [[4]]].flat(2)  // [1, 2, 3, 4]

// flatMap - map + flat
const arr = [1, 2, 3];
arr.flatMap(n => [n, n * 2]);  // [1, 2, 2, 4, 3, 6]
```

### Sorting

```javascript
// Default sort (string comparison!)
[10, 2, 30].sort()  // [10, 2, 30] - wrong!

// Numeric sort
[10, 2, 30].sort((a, b) => a - b)  // [2, 10, 30]

// Descending
[10, 2, 30].sort((a, b) => b - a)  // [30, 10, 2]

// Object sort
users.sort((a, b) => a.name.localeCompare(b.name));

// toSorted (ES2023) - non-mutating
const sorted = arr.toSorted((a, b) => a - b);
```

---

## 💻 Essential Patterns

```javascript
// Remove duplicates
const unique = [...new Set(array)];

// Group by property
const grouped = items.reduce((acc, item) => {
    const key = item.category;
    (acc[key] ??= []).push(item);
    return acc;
}, {});

// Chunk array
function chunk(arr, size) {
    return Array.from({ length: Math.ceil(arr.length / size) },
        (_, i) => arr.slice(i * size, i * size + size));
}

// Partition (split by condition)
const [pass, fail] = items.reduce(
    ([p, f], item) => condition(item) ? [[...p, item], f] : [p, [...f, item]],
    [[], []]
);
```

---

## 🔥 Pro Tips

### 1. Prefer Immutable Methods
```javascript
// ✅ Creates new array
const newArr = [...arr, newItem];

// ❌ Mutates original
arr.push(newItem);
```

### 2. Chain Methods
```javascript
const result = data
    .filter(Boolean)
    .map(transform)
    .sort(compare);
```

---

## 🛠️ Hands-on Exercise

### Task: Data Pipeline

Build functions:
1. `dedupe` - remove duplicates
2. `groupBy` - group by property
3. `chunk` - split into chunks
4. `partition` - split by condition

---

## 📚 Deep Dive Resources

- [MDN: Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
"""
            },
            {
                "title": "Objects — Key-Value Mastery",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 225,
                "content": r"""
# Objects — Key-Value Mastery

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"In JavaScript, almost everything is an object. Understanding them is non-negotiable."*

---

## 🎯 Why This Matters

Objects are fundamental:
- Config files
- API responses
- State management
- Data modeling

---

## 🧠 Core Concepts

### Object Creation

```javascript
// Object literal (most common)
const server = {
    host: "localhost",
    port: 3000,
    isRunning: true
};

// Shorthand properties (ES6)
const host = "localhost";
const port = 3000;
const server = { host, port };  // Same as { host: host, port: port }

// Computed property names
const key = "status";
const obj = {
    [key]: "active",
    [`${key}Code`]: 200
};

// Object.create
const proto = { greet() { return `Hello, ${this.name}`; } };
const user = Object.create(proto);
user.name = "John";
```

### Accessing Properties

```javascript
const config = {
    database: {
        host: "localhost",
        port: 5432
    }
};

// Dot notation
config.database.host  // "localhost"

// Bracket notation (dynamic keys)
const key = "host";
config.database[key]  // "localhost"

// Optional chaining
config.database?.credentials?.password  // undefined

// Destructuring
const { host, port } = config.database;

// Nested destructuring
const { database: { host, port } } = config;

// With defaults
const { timeout = 5000 } = config;

// Rename while destructuring
const { host: dbHost } = config.database;
```

### Modifying Objects

```javascript
const user = { name: "John" };

// Add/update properties
user.email = "john@example.com";
user["age"] = 30;

// Delete property
delete user.age;

// Spread operator (shallow copy)
const updated = { ...user, role: "admin" };

// Object.assign (older pattern)
const merged = Object.assign({}, user, { role: "admin" });
```

### Object Methods

```javascript
const config = { host: "localhost", port: 3000 };

// Get keys
Object.keys(config)    // ["host", "port"]

// Get values
Object.values(config)  // ["localhost", 3000]

// Get entries
Object.entries(config) // [["host", "localhost"], ["port", 3000]]

// From entries
Object.fromEntries([["a", 1], ["b", 2]])  // { a: 1, b: 2 }

// Check property existence
"host" in config                // true
config.hasOwnProperty("host")   // true

// Freeze (immutable)
Object.freeze(config);
config.port = 8080;  // Silently fails (or throws in strict)

// Seal (can modify, can't add/delete)
Object.seal(config);
```

### Object Iteration

```javascript
const obj = { a: 1, b: 2, c: 3 };

// for...in (all enumerable, including inherited)
for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(`${key}: ${obj[key]}`);
    }
}

// Object.keys (preferred)
for (const key of Object.keys(obj)) {
    console.log(`${key}: ${obj[key]}`);
}

// Object.entries (most useful)
for (const [key, value] of Object.entries(obj)) {
    console.log(`${key}: ${value}`);
}

// Transform with entries
const doubled = Object.fromEntries(
    Object.entries(obj).map(([k, v]) => [k, v * 2])
);
```

### Getters & Setters

```javascript
const user = {
    firstName: "John",
    lastName: "Doe",

    // Getter
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },

    // Setter
    set fullName(value) {
        const [first, last] = value.split(" ");
        this.firstName = first;
        this.lastName = last;
    }
};

user.fullName;            // "John Doe"
user.fullName = "Jane Smith";
user.firstName;           // "Jane"
```

---

## 💻 Essential Patterns

```javascript
// Deep clone (simple)
const clone = JSON.parse(JSON.stringify(obj));

// Deep clone (with structuredClone - modern)
const clone = structuredClone(obj);

// Merge with defaults
const config = { ...defaults, ...userConfig };

// Pick properties
const pick = (obj, keys) =>
    Object.fromEntries(keys.map(k => [k, obj[k]]));

// Omit properties
const omit = (obj, keys) =>
    Object.fromEntries(
        Object.entries(obj).filter(([k]) => !keys.includes(k))
    );
```

---

## 🔥 Pro Tips

### 1. Use Optional Chaining
```javascript
const city = user?.address?.city ?? "Unknown";
```

### 2. Prefer Spread for Immutability
```javascript
const updated = { ...obj, newProp: value };
```

---

## 🛠️ Hands-on Exercise

### Task: Config Manager

Create functions:
1. `deepMerge` - recursively merge objects
2. `pick` - select specific properties
3. `omit` - exclude properties
4. `flatten` - flatten nested object to dot notation

---

## 📚 Deep Dive Resources

- [MDN: Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
"""
            },
            {
                "title": "Destructuring & Spread",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 200,
                "content": r"""
# Destructuring & Spread

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Destructuring makes your code shorter and more expressive. Master it."*

---

## 🎯 Why This Matters

Destructuring:
- Cleaner variable assignment
- Better function parameters
- Easy data extraction
- Swap values elegantly

---

## 🧠 Core Concepts

### Array Destructuring

```javascript
const coords = [10, 20, 30];

// Basic
const [x, y, z] = coords;  // x=10, y=20, z=30

// Skip elements
const [first, , third] = coords;  // first=10, third=30

// Rest pattern
const [head, ...tail] = coords;  // head=10, tail=[20, 30]

// Default values
const [a, b, c, d = 0] = coords;  // d=0

// Nested arrays
const matrix = [[1, 2], [3, 4]];
const [[a, b], [c, d]] = matrix;

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];  // a=2, b=1
```

### Object Destructuring

```javascript
const user = {
    name: "John",
    email: "john@example.com",
    role: "admin"
};

// Basic
const { name, email } = user;

// Rename variables
const { name: userName, email: userEmail } = user;

// Default values
const { name, age = 30 } = user;  // age=30

// Rest pattern
const { name, ...rest } = user;  // rest = { email, role }

// Nested objects
const config = {
    server: { host: "localhost", port: 3000 }
};
const { server: { host, port } } = config;
```

### Function Parameters

```javascript
// Object destructuring in params
function createUser({ name, email, role = "user" }) {
    return { id: Date.now(), name, email, role };
}

createUser({ name: "John", email: "john@test.com" });

// Array destructuring in params
function processCoords([x, y]) {
    return { x, y };
}

// With defaults for entire param
function connect({ host = "localhost", port = 3000 } = {}) {
    return `${host}:${port}`;
}

connect();  // "localhost:3000"
connect({ port: 8080 });  // "localhost:8080"
```

### Spread Operator

```javascript
// Array spread
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// Insert in middle
const inserted = [1, ...arr1, 2];  // [1, 1, 2, 3, 2]

// Copy array
const copy = [...arr1];

// Convert iterable to array
const chars = [..."hello"];  // ["h", "e", "l", "l", "o"]

// Object spread
const defaults = { theme: "dark", lang: "en" };
const userPrefs = { lang: "sv" };
const settings = { ...defaults, ...userPrefs };
// { theme: "dark", lang: "sv" }

// Conditional properties
const user = {
    name: "John",
    ...(isAdmin && { role: "admin" })
};

// Function arguments
const numbers = [1, 2, 3];
Math.max(...numbers);  // 3
```

### Rest Parameters

```javascript
// Collect remaining arguments
function sum(first, ...rest) {
    return rest.reduce((acc, n) => acc + n, first);
}

sum(1, 2, 3, 4);  // 10

// Combine with destructuring
function processItems([first, ...rest], options = {}) {
    console.log(`First: ${first}, Rest: ${rest.length} items`);
}
```

### Advanced Patterns

```javascript
// Rename + default
const { name: userName = "Anonymous" } = user;

// Computed property names
const key = "name";
const { [key]: value } = user;  // value = user.name

// Mixed destructuring
const {
    user: { name, email },
    posts: [firstPost, ...otherPosts]
} = apiResponse;

// Destructure in loops
for (const { name, email } of users) {
    console.log(`${name}: ${email}`);
}

// Parameter parsing
const parseUrl = (url) => {
    const { protocol, hostname, port } = new URL(url);
    return { protocol, hostname, port };
};
```

---

## 💻 Essential Patterns

```javascript
// Extract and transform
const users = [{ name: "John", age: 30 }, { name: "Jane", age: 25 }];
const names = users.map(({ name }) => name);

// Combine objects immutably
const updatedUser = { ...user, updatedAt: Date.now() };

// Remove property
const { password, ...safeUser } = user;

// Module imports
import { useState, useEffect } from "react";
```

---

## 🔥 Pro Tips

### 1. Default Objects in Params
```javascript
function api({ method = "GET", body } = {}) {
    // Works even with no arguments
}
```

### 2. Quick Object Property Extraction
```javascript
const { name, email } = await fetchUser(id);
```

---

## 🛠️ Hands-on Exercise

### Task: API Response Handler

Create a function that:
1. Destructures nested API response
2. Extracts user + first 3 posts
3. Renames fields for UI
4. Adds default values for missing data

---

## 📚 Deep Dive Resources

- [MDN: Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
"""
            },
            {
                "title": "ES6+ Modern Features",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 225,
                "content": r"""
# ES6+ Modern Features

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Modern JavaScript isn't just syntactic sugar — it's a productivity revolution."*

---

## 🎯 Why This Matters

ES6+ features:
- Cleaner syntax
- New data structures
- Better iteration
- Enhanced functionality

Write less, do more.

---

## 🧠 Core Concepts

### Template Literals

```javascript
const name = "DevOps";
const version = "1.0";

// Basic interpolation
const msg = `Hello, ${name}!`;

// Multi-line strings
const html = `
    <div class="card">
        <h1>${name}</h1>
        <p>Version: ${version}</p>
    </div>
`;

// Expressions
const total = `Total: ${items.reduce((a, b) => a + b, 0)}`;

// Tagged templates
function sql(strings, ...values) {
    return { query: strings.join("?"), values };
}

const id = 5;
const query = sql`SELECT * FROM users WHERE id = ${id}`;
// { query: "SELECT * FROM users WHERE id = ?", values: [5] }
```

### Symbol

```javascript
// Create unique identifier
const id = Symbol("id");
const id2 = Symbol("id");
id === id2;  // false (always unique)

// Use as property key (private-like)
const user = {
    name: "John",
    [id]: 12345
};

Object.keys(user);  // ["name"] (symbols hidden)
Object.getOwnPropertySymbols(user);  // [Symbol(id)]

// Well-known symbols
Symbol.iterator
Symbol.toStringTag
Symbol.asyncIterator

// Global symbol registry
const globalId = Symbol.for("app.id");
const sameId = Symbol.for("app.id");
globalId === sameId;  // true
```

### Map & Set

```javascript
// Map - key-value with any key type
const map = new Map();
map.set("string", "value");
map.set(42, "number key");
map.set({ key: "obj" }, "object key");

map.get("string");   // "value"
map.has(42);         // true
map.size;            // 3
map.delete(42);

// Map from entries
const map2 = new Map([
    ["a", 1],
    ["b", 2]
]);

// Iteration
for (const [key, value] of map2) {
    console.log(`${key}: ${value}`);
}

// Set - unique values
const set = new Set([1, 2, 2, 3, 3, 3]);
set;  // Set(3) {1, 2, 3}

set.add(4);
set.has(2);     // true
set.delete(2);
set.size;       // 3

// Convert to array
[...set];  // [1, 3, 4]

// Deduplicate array
const unique = [...new Set(array)];
```

### WeakMap & WeakSet

```javascript
// WeakMap - keys are weakly held (garbage collected)
const wm = new WeakMap();
let obj = { data: "important" };
wm.set(obj, "metadata");

obj = null;  // Now key can be garbage collected

// Use case: private data
const privateData = new WeakMap();

class User {
    constructor(name) {
        privateData.set(this, { name });
    }

    getName() {
        return privateData.get(this).name;
    }
}
```

### Iterators & Generators

```javascript
// Custom iterator
const range = {
    start: 1,
    end: 5,
    [Symbol.iterator]() {
        let current = this.start;
        const end = this.end;
        return {
            next() {
                if (current <= end) {
                    return { value: current++, done: false };
                }
                return { done: true };
            }
        };
    }
};

[...range];  // [1, 2, 3, 4, 5]

// Generator function
function* range(start, end) {
    for (let i = start; i <= end; i++) {
        yield i;
    }
}

[...range(1, 5)];  // [1, 2, 3, 4, 5]

// Infinite generator
function* infiniteIds() {
    let id = 1;
    while (true) {
        yield id++;
    }
}

const gen = infiniteIds();
gen.next().value;  // 1
gen.next().value;  // 2
```

### Proxy & Reflect

```javascript
// Proxy - intercept operations
const target = { name: "John", age: 30 };

const proxy = new Proxy(target, {
    get(obj, prop) {
        console.log(`Getting ${prop}`);
        return obj[prop];
    },
    set(obj, prop, value) {
        console.log(`Setting ${prop} = ${value}`);
        obj[prop] = value;
        return true;
    }
});

proxy.name;      // Logs "Getting name", returns "John"
proxy.age = 31;  // Logs "Setting age = 31"

// Validation proxy
const validator = {
    set(obj, prop, value) {
        if (prop === "age" && typeof value !== "number") {
            throw new TypeError("Age must be a number");
        }
        obj[prop] = value;
        return true;
    }
};
```

---

## 💻 Essential Patterns

```javascript
// Config with defaults (Map)
const defaults = new Map([
    ["timeout", 5000],
    ["retries", 3]
]);

const config = new Map([...defaults, ...userConfig]);

// Unique ID generator
const createIdGenerator = function* (prefix) {
    let id = 0;
    while (true) {
        yield `${prefix}-${++id}`;
    }
};

const userIds = createIdGenerator("user");
```

---

## 🔥 Pro Tips

### 1. Use Map for Dynamic Keys
```javascript
const cache = new Map();
cache.set(functionRef, result);  // Functions as keys!
```

### 2. Use Set for Membership Tests
```javascript
const allowedRoles = new Set(["admin", "moderator"]);
if (allowedRoles.has(user.role)) { ... }
```

---

## 🛠️ Hands-on Exercise

### Task: Feature Flag System

Build with:
1. Map for flag storage
2. Proxy for access logging
3. Generator for flag IDs
4. Set for enabled flags

---

## 📚 Deep Dive Resources

- [MDN: ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
"""
            },
            {
                "title": "Classes — OOP in JavaScript",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 225,
                "content": r"""
# Classes — OOP in JavaScript

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Classes are syntactic sugar over prototypes — delicious, productive sugar."*

---

## 🎯 Why This Matters

Classes provide:
- Clear structure
- Encapsulation
- Inheritance
- Familiar OOP patterns

Essential for larger applications.

---

## 🧠 Core Concepts

### Class Declaration

```javascript
class User {
    // Constructor
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    // Instance method
    greet() {
        return `Hello, I'm ${this.name}`;
    }

    // Getter
    get displayName() {
        return this.name.toUpperCase();
    }

    // Setter
    set displayName(value) {
        this.name = value.toLowerCase();
    }

    // Static method
    static create(data) {
        return new User(data.name, data.email);
    }

    // Static property
    static count = 0;
}

const user = new User("John", "john@example.com");
user.greet();           // "Hello, I'm John"
user.displayName;       // "JOHN"
User.create({ name: "Jane", email: "jane@test.com" });
```

### Private Fields (ES2022)

```javascript
class BankAccount {
    // Private fields (truly private)
    #balance = 0;
    #transactions = [];

    constructor(initialBalance) {
        this.#balance = initialBalance;
    }

    deposit(amount) {
        if (amount <= 0) throw new Error("Invalid amount");
        this.#balance += amount;
        this.#logTransaction("deposit", amount);
    }

    withdraw(amount) {
        if (amount > this.#balance) throw new Error("Insufficient funds");
        this.#balance -= amount;
        this.#logTransaction("withdraw", amount);
    }

    // Private method
    #logTransaction(type, amount) {
        this.#transactions.push({ type, amount, date: new Date() });
    }

    get balance() {
        return this.#balance;
    }
}

const account = new BankAccount(100);
account.deposit(50);
account.balance;     // 150
account.#balance;    // SyntaxError: Private field
```

### Inheritance

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);  // Call parent constructor
        this.breed = breed;
    }

    // Override method
    speak() {
        console.log(`${this.name} barks!`);
    }

    // New method
    fetch() {
        console.log(`${this.name} fetches the ball`);
    }
}

const dog = new Dog("Rex", "German Shepherd");
dog.speak();  // "Rex barks!"
dog.fetch();  // "Rex fetches the ball"

dog instanceof Dog;     // true
dog instanceof Animal;  // true
```

### Abstract Pattern

```javascript
class Component {
    constructor(name) {
        if (new.target === Component) {
            throw new Error("Component is abstract");
        }
        this.name = name;
    }

    // Abstract method (must be implemented)
    render() {
        throw new Error("render() must be implemented");
    }

    // Concrete method (shared)
    mount(container) {
        container.innerHTML = this.render();
    }
}

class Button extends Component {
    constructor(label) {
        super("Button");
        this.label = label;
    }

    render() {
        return `<button>${this.label}</button>`;
    }
}
```

### Mixins

```javascript
// Mixin pattern for multiple inheritance
const TimestampMixin = (Base) => class extends Base {
    getTimestamp() {
        return new Date().toISOString();
    }
};

const SerializableMixin = (Base) => class extends Base {
    toJSON() {
        return JSON.stringify(this);
    }
};

class User {
    constructor(name) {
        this.name = name;
    }
}

// Apply mixins
class EnhancedUser extends SerializableMixin(TimestampMixin(User)) {
    constructor(name) {
        super(name);
    }
}

const user = new EnhancedUser("John");
user.getTimestamp();  // "2025-12-03T..."
user.toJSON();        // '{"name":"John"}'
```

### Static Blocks (ES2022)

```javascript
class Config {
    static settings;

    // Static initialization block
    static {
        try {
            this.settings = JSON.parse(localStorage.getItem("config")) || {};
        } catch {
            this.settings = {};
        }
    }
}
```

---

## 💻 Essential Patterns

```javascript
// Singleton
class Database {
    static #instance;

    constructor() {
        if (Database.#instance) {
            return Database.#instance;
        }
        Database.#instance = this;
    }

    static getInstance() {
        return Database.#instance || new Database();
    }
}

// Factory
class VehicleFactory {
    static create(type) {
        switch (type) {
            case "car": return new Car();
            case "bike": return new Bike();
            default: throw new Error(`Unknown type: ${type}`);
        }
    }
}
```

---

## 🔥 Pro Tips

### 1. Use Private Fields for Encapsulation
```javascript
class User {
    #password;  // Truly private
}
```

### 2. Prefer Composition Over Inheritance
```javascript
class User {
    constructor(logger, validator) {
        this.logger = logger;
        this.validator = validator;
    }
}
```

---

## 🛠️ Hands-on Exercise

### Task: Event System

Create classes:
1. `EventEmitter` base class
2. `Logger` extending EventEmitter
3. `User` with private fields
4. Use mixins for serialization

---

## 📚 Deep Dive Resources

- [MDN: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
"""
            },
            {
                "title": "Modules — import & export",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 200,
                "content": r"""
# Modules — import & export

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Modules turn spaghetti code into a well-organized library."*

---

## 🎯 Why This Matters

Modules enable:
- Code organization
- Dependency management
- Encapsulation
- Reusability

Essential for any project beyond a single file.

---

## 🧠 Core Concepts

### Named Exports

```javascript
// math.js
export const PI = 3.14159;

export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

// Alternative: export at end
const multiply = (a, b) => a * b;
const divide = (a, b) => a / b;

export { multiply, divide };
```

### Named Imports

```javascript
// Import specific exports
import { add, subtract } from "./math.js";

add(2, 3);  // 5

// Rename imports
import { add as sum, PI } from "./math.js";

sum(2, 3);  // 5

// Import all as namespace
import * as math from "./math.js";

math.add(2, 3);  // 5
math.PI;         // 3.14159
```

### Default Exports

```javascript
// logger.js
export default class Logger {
    log(message) {
        console.log(`[LOG] ${message}`);
    }
}

// Alternative
class Logger { ... }
export default Logger;

// Import default
import Logger from "./logger.js";
// Can use any name
import MyLogger from "./logger.js";

// Combine default and named
export default class Logger { ... }
export const LOG_LEVELS = ["debug", "info", "warn", "error"];

import Logger, { LOG_LEVELS } from "./logger.js";
```

### Re-exports

```javascript
// index.js - barrel file
export { User } from "./user.js";
export { Product } from "./product.js";
export * from "./utils.js";

// Rename on re-export
export { User as UserModel } from "./user.js";

// Re-export default as named
export { default as Logger } from "./logger.js";

// Import from barrel
import { User, Product, Logger } from "./models/index.js";
```

### Dynamic Imports

```javascript
// Static import (top of file only)
import { func } from "./module.js";

// Dynamic import (anywhere, returns Promise)
const loadModule = async () => {
    const module = await import("./heavy-module.js");
    module.doSomething();
};

// Conditional import
if (condition) {
    const { feature } = await import("./feature.js");
    feature();
}

// Import with variable path
const modulePath = `./modules/${moduleName}.js`;
const module = await import(modulePath);
```

### Module Patterns

```javascript
// Module with state
// counter.js
let count = 0;

export const increment = () => ++count;
export const decrement = () => --count;
export const getCount = () => count;

// Each import shares the same state
import { increment, getCount } from "./counter.js";

// Configuration module
// config.js
const config = {
    apiUrl: process.env.API_URL,
    timeout: 5000
};

export default Object.freeze(config);
```

### CommonJS (Node.js legacy)

```javascript
// CommonJS (older Node.js pattern)
// math.js
module.exports = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b
};

// Or single export
module.exports = function add(a, b) {
    return a + b;
};

// Import CommonJS
const math = require("./math.js");
const { add } = require("./math.js");
```

### package.json Configuration

```json
{
    "name": "my-package",
    "type": "module",
    "main": "./dist/index.js",
    "exports": {
        ".": "./dist/index.js",
        "./utils": "./dist/utils.js"
    },
    "imports": {
        "#config": "./src/config.js",
        "#utils/*": "./src/utils/*.js"
    }
}
```

---

## 💻 Essential Patterns

```javascript
// Lazy loading
const routes = {
    "/dashboard": () => import("./pages/dashboard.js"),
    "/settings": () => import("./pages/settings.js")
};

async function loadRoute(path) {
    const module = await routes[path]?.();
    return module?.default;
}

// Plugin system
async function loadPlugins(pluginNames) {
    return Promise.all(
        pluginNames.map(name => import(`./plugins/${name}.js`))
    );
}
```

---

## 🔥 Pro Tips

### 1. Use Barrel Files
```javascript
// models/index.js
export * from "./user.js";
export * from "./product.js";
```

### 2. Prefer Named Exports
```javascript
// Easier to refactor and tree-shake
export { User, createUser };
```

### 3. Use Import Maps (Browser)
```html
<script type="importmap">
{
    "imports": {
        "lodash": "/node_modules/lodash-es/lodash.js"
    }
}
</script>
```

---

## 🛠️ Hands-on Exercise

### Task: Plugin Architecture

Create:
1. Core module with plugin interface
2. Multiple plugin modules
3. Dynamic plugin loading
4. Barrel file for exports

---

## 📚 Deep Dive Resources

- [MDN: Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
"""
            },
            {
                "title": "Callbacks & the Event Loop",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 200,
                "content": r"""
# Callbacks & the Event Loop

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"JavaScript is single-threaded but never blocking. Understanding the event loop is understanding JavaScript."*

---

## 🎯 Why This Matters

JavaScript handles:
- User interactions
- Network requests
- File operations
- Timers

All without blocking — thanks to the event loop.

---

## 🧠 Core Concepts

### Single-Threaded Nature

```javascript
// JavaScript runs on ONE thread
// But handles async operations via the event loop

console.log("1");

setTimeout(() => {
    console.log("2");
}, 0);

console.log("3");

// Output: 1, 3, 2
// Even with 0ms delay, setTimeout is async!
```

### The Event Loop

```
┌───────────────────────────┐
│        Call Stack         │
│   (Synchronous Code)      │
└───────────┬───────────────┘
            │
            ▼
┌───────────────────────────┐
│      Web APIs / Node      │
│  (setTimeout, fetch, fs)  │
└───────────┬───────────────┘
            │
            ▼
┌───────────────────────────┐
│     Callback Queue        │
│   (Task Queue / Macrotask)│
└───────────┬───────────────┘
            │
            ▼
┌───────────────────────────┐
│    Microtask Queue        │
│  (Promises, queueMicrotask)│
└───────────────────────────┘

Event Loop: Continuously checks if Call Stack is empty,
then processes Microtasks, then one Macrotask
```

### Callback Pattern

```javascript
// Traditional callback pattern
function fetchUser(id, callback) {
    setTimeout(() => {
        const user = { id, name: "John" };
        callback(null, user);
    }, 100);
}

// Usage
fetchUser(1, (error, user) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(user);
});

// Error-first callback (Node.js convention)
function readFile(path, callback) {
    // callback(error, data)
    if (!path) {
        callback(new Error("Path required"), null);
        return;
    }
    callback(null, "file contents");
}
```

### Callback Hell

```javascript
// ❌ Callback Hell (Pyramid of Doom)
getUser(userId, (err, user) => {
    if (err) return handleError(err);
    getOrders(user.id, (err, orders) => {
        if (err) return handleError(err);
        getOrderDetails(orders[0].id, (err, details) => {
            if (err) return handleError(err);
            processPayment(details, (err, result) => {
                if (err) return handleError(err);
                sendConfirmation(result, (err) => {
                    if (err) return handleError(err);
                    console.log("Done!");
                });
            });
        });
    });
});
```

### Microtasks vs Macrotasks

```javascript
console.log("1 - Sync");

setTimeout(() => console.log("2 - Timeout (Macro)"), 0);

Promise.resolve().then(() => console.log("3 - Promise (Micro)"));

queueMicrotask(() => console.log("4 - Microtask"));

console.log("5 - Sync");

// Output: 1, 5, 3, 4, 2
// Microtasks run before Macrotasks!
```

### Higher-Order Callbacks

```javascript
// Array methods use callbacks
const numbers = [1, 2, 3, 4, 5];

numbers.forEach((n, i) => {
    console.log(`${i}: ${n}`);
});

const doubled = numbers.map(n => n * 2);
const even = numbers.filter(n => n % 2 === 0);

// Event listeners
button.addEventListener("click", (event) => {
    console.log("Clicked!", event.target);
});
```

---

## 💻 Essential Patterns

```javascript
// Named callbacks (better debugging)
function handleUserResponse(err, user) {
    if (err) {
        console.error("Failed to fetch user:", err);
        return;
    }
    displayUser(user);
}

fetchUser(1, handleUserResponse);

// Callback wrapper for error handling
function withErrorHandling(fn) {
    return (err, data) => {
        if (err) {
            console.error(err);
            return;
        }
        fn(data);
    };
}

fetchData(withErrorHandling((data) => {
    console.log(data);
}));
```

---

## 🔥 Pro Tips

### 1. Always Handle Errors
```javascript
operation((err, result) => {
    if (err) {
        // Handle error FIRST
        return;
    }
    // Then process result
});
```

### 2. Understand Event Loop Order
```javascript
// Sync → Microtasks → Macrotasks
```

---

## 🛠️ Hands-on Exercise

### Task: Async Operation Manager

Create functions:
1. Callback-based file reader
2. Error-first pattern
3. Show event loop order with console.log
4. Convert callback to promise

---

## 📚 Deep Dive Resources

- [MDN: Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)
- [JavaScript Event Loop Visualized](https://www.jsv9000.app/)
"""
            },
            {
                "title": "Promises — Better Async",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 250,
                "content": r"""
# Promises — Better Async

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Promises don't eliminate async complexity — they make it manageable."*

---

## 🎯 Why This Matters

Promises provide:
- Cleaner async code
- Better error handling
- Chaining operations
- Foundation for async/await

---

## 🧠 Core Concepts

### Promise States

```javascript
// A Promise has three states:
// 1. pending - initial state
// 2. fulfilled - operation succeeded
// 3. rejected - operation failed

const promise = new Promise((resolve, reject) => {
    // Async operation
    if (success) {
        resolve(value);  // → fulfilled
    } else {
        reject(error);   // → rejected
    }
});
```

### Creating Promises

```javascript
// Basic Promise
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Success!");
    }, 1000);
});

// Promise that may reject
function fetchUser(id) {
    return new Promise((resolve, reject) => {
        if (!id) {
            reject(new Error("ID required"));
            return;
        }
        setTimeout(() => {
            resolve({ id, name: "John" });
        }, 100);
    });
}

// Shorthand for resolved/rejected
Promise.resolve("immediate value");
Promise.reject(new Error("immediate error"));
```

### Consuming Promises

```javascript
// then/catch/finally
fetchUser(1)
    .then(user => {
        console.log(user);
        return user.id;  // Return value for next then
    })
    .then(userId => {
        console.log(`User ID: ${userId}`);
    })
    .catch(error => {
        console.error("Error:", error.message);
    })
    .finally(() => {
        console.log("Cleanup");  // Always runs
    });
```

### Promise Chaining

```javascript
// Chain dependent operations
getUser(userId)
    .then(user => getOrders(user.id))
    .then(orders => getOrderDetails(orders[0].id))
    .then(details => processPayment(details))
    .then(result => sendConfirmation(result))
    .then(() => console.log("Done!"))
    .catch(error => console.error("Failed:", error));

// Transforming data
fetch("/api/users")
    .then(response => response.json())
    .then(users => users.filter(u => u.active))
    .then(activeUsers => activeUsers.map(u => u.name))
    .then(names => console.log(names));
```

### Promise Static Methods

```javascript
// Promise.all - wait for all (fail-fast)
const results = await Promise.all([
    fetch("/api/users"),
    fetch("/api/posts"),
    fetch("/api/comments")
]);

// Promise.allSettled - wait for all (no fail-fast)
const results = await Promise.allSettled([
    fetch("/api/users"),
    fetch("/might-fail")
]);
// [{ status: "fulfilled", value: ... }, { status: "rejected", reason: ... }]

// Promise.race - first to settle (resolve or reject)
const result = await Promise.race([
    fetch("/api/data"),
    new Promise((_, reject) =>
        setTimeout(() => reject(new Error("Timeout")), 5000)
    )
]);

// Promise.any - first to fulfill (ignores rejections)
const fastest = await Promise.any([
    fetch("/mirror1/data"),
    fetch("/mirror2/data"),
    fetch("/mirror3/data")
]);
```

### Error Handling

```javascript
// Catch at the end
promise1
    .then(result => promise2(result))
    .then(result => promise3(result))
    .catch(error => {
        // Catches error from any step
        console.error(error);
    });

// Catch and recover
fetchData()
    .catch(error => {
        console.warn("Fetch failed, using cache");
        return getCachedData();  // Return fallback
    })
    .then(data => {
        // Continues with fallback data
    });

// Re-throwing errors
fetchData()
    .catch(error => {
        if (error.code === "NETWORK_ERROR") {
            throw error;  // Re-throw
        }
        return defaultData;
    });
```

### Promisify Callback Functions

```javascript
// Convert callback to promise
function promisify(fn) {
    return (...args) => {
        return new Promise((resolve, reject) => {
            fn(...args, (error, result) => {
                if (error) reject(error);
                else resolve(result);
            });
        });
    };
}

// Usage
const readFileAsync = promisify(fs.readFile);
const data = await readFileAsync("file.txt");

// Node.js built-in
const { promisify } = require("util");
const readFileAsync = promisify(fs.readFile);
```

---

## 💻 Essential Patterns

```javascript
// Retry pattern
async function retry(fn, attempts = 3, delay = 1000) {
    for (let i = 0; i < attempts; i++) {
        try {
            return await fn();
        } catch (error) {
            if (i === attempts - 1) throw error;
            await new Promise(r => setTimeout(r, delay));
        }
    }
}

// Timeout wrapper
function withTimeout(promise, ms) {
    const timeout = new Promise((_, reject) =>
        setTimeout(() => reject(new Error("Timeout")), ms)
    );
    return Promise.race([promise, timeout]);
}

// Sequential execution
async function sequential(tasks) {
    const results = [];
    for (const task of tasks) {
        results.push(await task());
    }
    return results;
}
```

---

## 🔥 Pro Tips

### 1. Always Return in .then()
```javascript
// ✅ Return for chaining
.then(data => processData(data))

// ❌ Missing return breaks chain
.then(data => { processData(data); })
```

### 2. Use Promise.allSettled for Independent Ops
```javascript
await Promise.allSettled([op1, op2, op3]);
```

---

## 🛠️ Hands-on Exercise

### Task: API Client

Build a Promise-based:
1. HTTP client with timeout
2. Retry logic
3. Response caching
4. Error classification

---

## 📚 Deep Dive Resources

- [MDN: Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
"""
            },
            {
                "title": "Async/Await — Clean Async Code",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 250,
                "content": r"""
# Async/Await — Clean Async Code

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Async/await is the best thing to happen to JavaScript since functions."*

---

## 🎯 Why This Matters

Async/await provides:
- Synchronous-looking async code
- Better error handling with try/catch
- Easier debugging
- Cleaner control flow

---

## 🧠 Core Concepts

### Basic Syntax

```javascript
// async function always returns a Promise
async function fetchUser(id) {
    const response = await fetch(`/api/users/${id}`);
    const user = await response.json();
    return user;
}

// Arrow function
const fetchUser = async (id) => {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
};

// Usage
const user = await fetchUser(1);
console.log(user);
```

### Error Handling

```javascript
// try/catch (recommended)
async function fetchData() {
    try {
        const response = await fetch("/api/data");
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Fetch failed:", error.message);
        throw error;  // Re-throw or return fallback
    }
}

// Catch at call site
try {
    const data = await fetchData();
} catch (error) {
    // Handle error
}

// .catch() still works
const data = await fetchData().catch(err => defaultData);
```

### Sequential vs Parallel

```javascript
// ❌ Sequential (slow)
async function getAll() {
    const users = await fetchUsers();      // Wait...
    const posts = await fetchPosts();      // Then wait...
    const comments = await fetchComments(); // Then wait...
    return { users, posts, comments };
}

// ✅ Parallel (fast)
async function getAll() {
    const [users, posts, comments] = await Promise.all([
        fetchUsers(),
        fetchPosts(),
        fetchComments()
    ]);
    return { users, posts, comments };
}

// Mixed: some parallel, some sequential
async function process() {
    // Fetch in parallel
    const [user, settings] = await Promise.all([
        fetchUser(),
        fetchSettings()
    ]);

    // Then process sequentially (depends on above)
    const enriched = await enrichUser(user, settings);
    return enriched;
}
```

### Loops with Async

```javascript
// Sequential processing
async function processSequential(items) {
    const results = [];
    for (const item of items) {
        const result = await processItem(item);
        results.push(result);
    }
    return results;
}

// Parallel processing
async function processParallel(items) {
    return Promise.all(items.map(item => processItem(item)));
}

// Controlled concurrency
async function processWithLimit(items, limit = 3) {
    const results = [];
    for (let i = 0; i < items.length; i += limit) {
        const batch = items.slice(i, i + limit);
        const batchResults = await Promise.all(
            batch.map(item => processItem(item))
        );
        results.push(...batchResults);
    }
    return results;
}

// ⚠️ forEach doesn't work with await!
// ❌ This doesn't wait
items.forEach(async (item) => {
    await processItem(item);  // Fire and forget!
});

// ✅ Use for...of instead
for (const item of items) {
    await processItem(item);
}
```

### Top-Level Await

```javascript
// In ES modules (type: "module")
// Can use await at top level

const config = await loadConfig();
const db = await connectDatabase(config);

export { db, config };
```

### Async Patterns

```javascript
// IIFE for async in non-module context
(async () => {
    const data = await fetchData();
    console.log(data);
})();

// Async class methods
class DataService {
    async fetchAll() {
        return await fetch("/api/data");
    }

    async *fetchPages() {
        let page = 1;
        while (true) {
            const data = await fetch(`/api/data?page=${page}`);
            if (!data.hasMore) break;
            yield data.items;
            page++;
        }
    }
}

// Async generators
async function* asyncGenerator() {
    yield await Promise.resolve(1);
    yield await Promise.resolve(2);
    yield await Promise.resolve(3);
}

for await (const value of asyncGenerator()) {
    console.log(value);
}
```

### Error Handling Patterns

```javascript
// Wrapper for cleaner error handling
async function to(promise) {
    try {
        const result = await promise;
        return [null, result];
    } catch (error) {
        return [error, null];
    }
}

// Usage
const [error, user] = await to(fetchUser(1));
if (error) {
    console.error(error);
    return;
}
console.log(user);

// Multiple operations with individual error handling
async function fetchAll() {
    const results = await Promise.allSettled([
        fetchUsers(),
        fetchPosts(),
        fetchComments()
    ]);

    return results.map(result => {
        if (result.status === "fulfilled") {
            return result.value;
        }
        console.error("Failed:", result.reason);
        return null;
    });
}
```

---

## 💻 Essential Patterns

```javascript
// Retry with exponential backoff
async function fetchWithRetry(url, options = {}) {
    const { retries = 3, backoff = 1000 } = options;

    for (let i = 0; i < retries; i++) {
        try {
            return await fetch(url);
        } catch (error) {
            if (i === retries - 1) throw error;
            await new Promise(r => setTimeout(r, backoff * (i + 1)));
        }
    }
}

// Debounced async function
function debounceAsync(fn, ms) {
    let timeoutId;
    return async (...args) => {
        clearTimeout(timeoutId);
        return new Promise((resolve) => {
            timeoutId = setTimeout(async () => {
                resolve(await fn(...args));
            }, ms);
        });
    };
}
```

---

## 🔥 Pro Tips

### 1. Don't Mix await and .then()
```javascript
// ✅ Pick one style
const data = await fetch(url);
// OR
fetch(url).then(data => ...);
```

### 2. Use Promise.all for Independence
```javascript
const [a, b, c] = await Promise.all([f1(), f2(), f3()]);
```

---

## 🛠️ Hands-on Exercise

### Task: Data Pipeline

Build async functions:
1. Fetch with retry and timeout
2. Process items with concurrency limit
3. Cache results
4. Handle partial failures gracefully

---

## 📚 Deep Dive Resources

- [MDN: async/await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)
"""
            },
            {
                "title": "Error Handling & Debugging",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 200,
                "content": r"""
# Error Handling & Debugging

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Production code isn't code that works—it's code that fails gracefully."*

---

## 🎯 Why This Matters

In DevOps, errors happen constantly:
- API endpoints fail
- Files don't exist
- Network timeouts
- Invalid configurations
- Permission issues

Proper error handling means:
- **Clear error messages** for debugging
- **Graceful degradation** for users
- **Meaningful logs** for monitoring
- **Recovery strategies** for resilience

---

## 🧠 Core Concepts

### Try/Catch Basics

```javascript
try {
    // Code that might fail
    const config = JSON.parse(configString);
    console.log(config.setting);
} catch (error) {
    // Handle the error
    console.error('Failed to parse config:', error.message);
} finally {
    // Always runs (cleanup)
    console.log('Config loading attempted');
}
```

### Error Object

```javascript
try {
    throw new Error('Something went wrong');
} catch (error) {
    console.log(error.name);     // 'Error'
    console.log(error.message);  // 'Something went wrong'
    console.log(error.stack);    // Full stack trace
}

// Built-in Error Types
// SyntaxError - JSON.parse('invalid')
// TypeError - null.toString()
// ReferenceError - undefinedVar
// RangeError - Array(-1)
```

### Custom Errors

```javascript
// Create custom error classes
class ValidationError extends Error {
    constructor(field, message) {
        super(message);
        this.name = 'ValidationError';
        this.field = field;
    }
}

class NetworkError extends Error {
    constructor(url, statusCode) {
        super(`Request to ${url} failed with ${statusCode}`);
        this.name = 'NetworkError';
        this.statusCode = statusCode;
    }
}

// Usage
function validateConfig(config) {
    if (!config.apiKey) {
        throw new ValidationError('apiKey', 'API key is required');
    }
    if (config.timeout < 0) {
        throw new ValidationError('timeout', 'Timeout must be positive');
    }
    return true;
}

try {
    validateConfig({ timeout: -1 });
} catch (error) {
    if (error instanceof ValidationError) {
        console.error(`Validation failed for ${error.field}: ${error.message}`);
    } else {
        throw error;  // Re-throw unexpected errors
    }
}
```

---

## ⚡ Async Error Handling

### Promises

```javascript
// .catch() for promises
fetchData()
    .then(process)
    .catch(error => {
        console.error('Pipeline failed:', error);
        return fallbackData;  // Recover with default
    });

// Promise rejection
function fetchConfig(url) {
    return new Promise((resolve, reject) => {
        if (!url) {
            reject(new Error('URL is required'));
            return;
        }
        // ... fetch logic
    });
}
```

### Async/Await

```javascript
async function deployService(config) {
    try {
        await validateConfig(config);
        await buildContainer(config);
        await pushToRegistry(config);
        await updateService(config);
        return { success: true };
    } catch (error) {
        // Log and rethrow with context
        console.error('Deployment failed:', error);
        throw new Error(`Deployment of ${config.name} failed: ${error.message}`);
    } finally {
        await cleanupTempFiles();
    }
}

// Granular error handling
async function fetchMultipleAPIs() {
    const results = [];

    for (const api of APIs) {
        try {
            const data = await fetch(api.url);
            results.push({ api: api.name, data, success: true });
        } catch (error) {
            results.push({ api: api.name, error: error.message, success: false });
            // Continue with other APIs
        }
    }

    return results;
}
```

---

## 🔧 Debugging Strategies

### Console Methods

```javascript
// Basic logging
console.log('Info:', data);
console.error('Error:', error);
console.warn('Warning:', message);

// Structured logging
console.table([
    { name: 'prod', status: 'healthy' },
    { name: 'staging', status: 'degraded' }
]);

// Timing
console.time('deployment');
await deploy();
console.timeEnd('deployment');  // deployment: 1234.567ms

// Grouping
console.group('Service Health Check');
console.log('CPU: 45%');
console.log('Memory: 67%');
console.groupEnd();

// Assertions (throws if false)
console.assert(response.status === 200, 'Expected 200 response');

// Stack traces
console.trace('How did we get here?');
```

### Debugging Patterns

```javascript
// Debug flag
const DEBUG = process.env.DEBUG === 'true';

function debug(...args) {
    if (DEBUG) console.log('[DEBUG]', ...args);
}

debug('Processing config:', config);

// Conditional breakpoints (in browser/Node debugger)
// debugger;  // Pauses execution if devtools open

// Inspecting objects
console.dir(complexObject, { depth: null });

// JSON stringify for deep inspection
console.log(JSON.stringify(data, null, 2));
```

---

## 🏗️ Production Error Patterns

### Error Wrapper Function

```javascript
// Wrap async functions for consistent error handling
function withErrorHandling(fn, context = '') {
    return async (...args) => {
        try {
            return await fn(...args);
        } catch (error) {
            const enhancedError = new Error(
                `[${context}] ${error.message}`
            );
            enhancedError.originalError = error;
            throw enhancedError;
        }
    };
}

const safeFetch = withErrorHandling(fetch, 'HTTP');
const safeProcess = withErrorHandling(processData, 'Processing');
```

### Error Logging Service

```javascript
class ErrorLogger {
    constructor(options = {}) {
        this.serviceName = options.serviceName || 'unknown';
        this.environment = process.env.NODE_ENV || 'development';
    }

    log(error, context = {}) {
        const errorReport = {
            timestamp: new Date().toISOString(),
            service: this.serviceName,
            environment: this.environment,
            error: {
                name: error.name,
                message: error.message,
                stack: error.stack
            },
            context
        };

        // In production, send to logging service
        if (this.environment === 'production') {
            // sendToLoggingService(errorReport);
        }

        console.error(JSON.stringify(errorReport, null, 2));
        return errorReport;
    }
}

const logger = new ErrorLogger({ serviceName: 'api-gateway' });

try {
    await processRequest(req);
} catch (error) {
    logger.log(error, { requestId: req.id, userId: req.user?.id });
}
```

---

## 🔥 Pro Tips

### 1. Never Swallow Errors
```javascript
// ❌ Bad - error disappears
try { doSomething(); } catch (e) {}

// ✅ Good - at minimum, log it
try { doSomething(); } catch (e) { console.error(e); }
```

### 2. Add Context When Rethrowing
```javascript
catch (error) {
    throw new Error(`Failed to process ${filename}: ${error.message}`);
}
```

### 3. Use Error Boundaries
```javascript
// Node.js global handlers
process.on('uncaughtException', (error) => {
    logger.log(error, { type: 'uncaughtException' });
    process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
    logger.log(reason, { type: 'unhandledRejection' });
});
```

---

## 🛠️ Hands-on Exercise

### Task: Resilient Data Fetcher

Build a function that:
1. Fetches data from an API with retry logic
2. Uses custom errors (NetworkError, ValidationError)
3. Implements timeout handling
4. Logs all errors with context
5. Returns partial results on partial failure

---

## 📚 Deep Dive Resources

- [MDN: Error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Node.js: Error handling](https://nodejs.org/api/errors.html)
"""
            },
            {
                "title": "JSON & Data Manipulation",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 200,
                "content": r"""
# JSON & Data Manipulation

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"In DevOps, JSON is the lingua franca—configs, APIs, logs, everything speaks JSON."*

---

## 🎯 Why This Matters

JSON is everywhere in DevOps:
- **Configuration files:** package.json, tsconfig.json
- **API responses:** REST APIs return JSON
- **Infrastructure:** Terraform, CloudFormation
- **Logging:** Structured logs in JSON
- **CI/CD:** Pipeline definitions

Master JSON and you master data flow.

---

## 🧠 Core Concepts

### JSON Basics

```javascript
// JSON = JavaScript Object Notation
// Valid JSON types: string, number, boolean, null, array, object

const jsonString = `{
    "name": "api-gateway",
    "version": "2.1.0",
    "enabled": true,
    "replicas": 3,
    "endpoints": ["/api", "/health"],
    "config": null
}`;

// Parse JSON string to object
const config = JSON.parse(jsonString);
console.log(config.name);     // "api-gateway"
console.log(config.replicas); // 3

// Convert object to JSON string
const output = JSON.stringify(config);
console.log(output);
// {"name":"api-gateway","version":"2.1.0",...}

// Pretty print
const pretty = JSON.stringify(config, null, 2);
console.log(pretty);
```

### Parse with Error Handling

```javascript
function safeJsonParse(str, fallback = null) {
    try {
        return JSON.parse(str);
    } catch (error) {
        console.error('JSON parse error:', error.message);
        return fallback;
    }
}

const data = safeJsonParse('{"valid": true}');  // { valid: true }
const bad = safeJsonParse('not json', {});      // {}
```

### Stringify Options

```javascript
const service = {
    name: 'worker',
    password: 'secret123',
    metadata: { region: 'us-east-1' }
};

// Replacer: filter properties
const safe = JSON.stringify(service, ['name', 'metadata'], 2);
// Only includes name and metadata

// Replacer function
const masked = JSON.stringify(service, (key, value) => {
    if (key === 'password') return '***';
    return value;
}, 2);
// {"name":"worker","password":"***","metadata":{"region":"us-east-1"}}

// Space: indentation
JSON.stringify(obj);        // Compact
JSON.stringify(obj, null, 2);   // 2 spaces
JSON.stringify(obj, null, '\t'); // Tabs
```

---

## ⚡ Data Transformation

### Array Methods

```javascript
const services = [
    { name: 'api', status: 'healthy', cpu: 45 },
    { name: 'db', status: 'degraded', cpu: 89 },
    { name: 'cache', status: 'healthy', cpu: 12 },
    { name: 'worker', status: 'down', cpu: 0 }
];

// Filter: select matching items
const healthy = services.filter(s => s.status === 'healthy');
// [{ name: 'api', ... }, { name: 'cache', ... }]

// Map: transform items
const names = services.map(s => s.name);
// ['api', 'db', 'cache', 'worker']

// Find: first match
const database = services.find(s => s.name === 'db');
// { name: 'db', status: 'degraded', cpu: 89 }

// Some/Every: boolean checks
const hasDown = services.some(s => s.status === 'down');     // true
const allHealthy = services.every(s => s.status === 'healthy'); // false

// Reduce: aggregate
const totalCpu = services.reduce((sum, s) => sum + s.cpu, 0);
// 146

// Sort: order items
const byCpu = [...services].sort((a, b) => b.cpu - a.cpu);
// Sorted by CPU descending

// Chain methods
const report = services
    .filter(s => s.status !== 'down')
    .map(s => ({ name: s.name, cpu: s.cpu }))
    .sort((a, b) => b.cpu - a.cpu);
```

### Object Methods

```javascript
const config = {
    apiKey: 'abc123',
    timeout: 5000,
    retries: 3
};

// Keys, values, entries
Object.keys(config);    // ['apiKey', 'timeout', 'retries']
Object.values(config);  // ['abc123', 5000, 3]
Object.entries(config); // [['apiKey', 'abc123'], ['timeout', 5000], ...]

// From entries (reverse of entries)
const pairs = [['a', 1], ['b', 2]];
Object.fromEntries(pairs);  // { a: 1, b: 2 }

// Transform object
const uppercased = Object.fromEntries(
    Object.entries(config).map(([key, val]) => [key.toUpperCase(), val])
);
// { APIKEY: 'abc123', TIMEOUT: 5000, RETRIES: 3 }

// Check if property exists
'apiKey' in config;             // true
config.hasOwnProperty('apiKey'); // true

// Merge objects
const defaults = { timeout: 3000, retries: 1 };
const merged = { ...defaults, ...config };  // config wins
```

---

## 🏗️ Complex Transformations

### Nested Data Processing

```javascript
const deployment = {
    name: 'production',
    clusters: [
        {
            region: 'us-east-1',
            services: [
                { name: 'api', replicas: 3 },
                { name: 'worker', replicas: 5 }
            ]
        },
        {
            region: 'eu-west-1',
            services: [
                { name: 'api', replicas: 2 },
                { name: 'worker', replicas: 3 }
            ]
        }
    ]
};

// Flatten nested arrays
const allServices = deployment.clusters.flatMap(c => c.services);
// [{ name: 'api', replicas: 3 }, { name: 'worker', replicas: 5 }, ...]

// Get unique service names
const uniqueNames = [...new Set(allServices.map(s => s.name))];
// ['api', 'worker']

// Total replicas per service
const replicaCount = allServices.reduce((acc, service) => {
    acc[service.name] = (acc[service.name] || 0) + service.replicas;
    return acc;
}, {});
// { api: 5, worker: 8 }

// Group by region
const byRegion = deployment.clusters.reduce((acc, cluster) => {
    acc[cluster.region] = cluster.services;
    return acc;
}, {});
```

### Deep Clone

```javascript
// Shallow copy (nested objects shared)
const shallow = { ...original };

// Deep clone with JSON (simple but loses functions/dates)
const deep = JSON.parse(JSON.stringify(original));

// Modern deep clone
const clone = structuredClone(original);  // Node 17+, browsers

// Custom deep clone for special types
function deepClone(obj) {
    if (obj === null || typeof obj !== 'object') return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof Array) return obj.map(deepClone);

    return Object.fromEntries(
        Object.entries(obj).map(([key, val]) => [key, deepClone(val)])
    );
}
```

### Config Merging

```javascript
// Deep merge for configs
function deepMerge(target, source) {
    const output = { ...target };

    for (const key of Object.keys(source)) {
        if (source[key] instanceof Object && key in target) {
            output[key] = deepMerge(target[key], source[key]);
        } else {
            output[key] = source[key];
        }
    }

    return output;
}

const defaultConfig = {
    server: { port: 3000, host: 'localhost' },
    db: { pool: 5 }
};

const envConfig = {
    server: { port: 8080 },
    db: { host: 'db.prod.internal' }
};

const finalConfig = deepMerge(defaultConfig, envConfig);
// { server: { port: 8080, host: 'localhost' }, db: { pool: 5, host: 'db.prod.internal' } }
```

---

## 🔧 Practical DevOps Examples

### Parse Log Files

```javascript
// Parse JSON logs (one object per line)
function parseJsonLogs(logContent) {
    return logContent
        .split('\n')
        .filter(line => line.trim())
        .map((line, index) => {
            try {
                return JSON.parse(line);
            } catch {
                console.warn(`Line ${index + 1}: Invalid JSON`);
                return null;
            }
        })
        .filter(Boolean);
}

const logs = parseJsonLogs(logFileContent);
const errors = logs.filter(log => log.level === 'error');
```

### Environment Variable Processing

```javascript
// Convert env vars to config object
function envToConfig(prefix = 'APP_') {
    return Object.fromEntries(
        Object.entries(process.env)
            .filter(([key]) => key.startsWith(prefix))
            .map(([key, value]) => [
                key.replace(prefix, '').toLowerCase(),
                parseEnvValue(value)
            ])
    );
}

function parseEnvValue(value) {
    if (value === 'true') return true;
    if (value === 'false') return false;
    if (!isNaN(value)) return Number(value);
    return value;
}

// APP_PORT=3000, APP_DEBUG=true
// → { port: 3000, debug: true }
```

---

## 🔥 Pro Tips

### 1. Handle Missing Data Gracefully
```javascript
// Optional chaining
const region = deployment?.clusters?.[0]?.region ?? 'default';
```

### 2. Use Map for Object Collections
```javascript
// When you need fast lookups
const serviceMap = new Map(services.map(s => [s.name, s]));
const api = serviceMap.get('api');  // O(1) lookup
```

### 3. Immutable Updates
```javascript
// Never mutate, always create new
const updated = {
    ...config,
    timeout: 10000,
    features: [...config.features, 'newFeature']
};
```

---

## 🛠️ Hands-on Exercise

### Task: Config Manager

Build a ConfigManager class that:
1. Loads JSON config from file
2. Merges with environment variables
3. Validates required fields
4. Provides type-safe getters
5. Supports nested key access (e.g., 'server.port')

---

## 📚 Deep Dive Resources

- [MDN: JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
- [MDN: Array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
"""
            },
            {
                "title": "Fetch API & HTTP Requests",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 250,
                "content": r"""
# Fetch API & HTTP Requests

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"APIs connect everything. Master HTTP requests and you control the flow of data."*

---

## 🎯 Why This Matters

Every DevOps workflow involves HTTP:
- **Monitoring:** Health checks, metrics APIs
- **CI/CD:** Trigger builds, deploy hooks
- **Cloud:** AWS/GCP/Azure APIs
- **Automation:** Slack, PagerDuty, Jira APIs
- **Config:** Pull configs from remote sources

Master Fetch and you master integration.

---

## 🧠 Core Concepts

### Basic Fetch

```javascript
// GET request (default)
const response = await fetch('https://api.example.com/data');
const data = await response.json();

// Check response status
if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
}

console.log(data);
```

### HTTP Methods

```javascript
// POST - Create resource
const createResponse = await fetch('https://api.example.com/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    },
    body: JSON.stringify({
        name: 'DevOps Engineer',
        email: 'devops@example.com'
    })
});

// PUT - Update resource (full replace)
await fetch('https://api.example.com/users/123', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'Updated Name', email: 'new@example.com' })
});

// PATCH - Partial update
await fetch('https://api.example.com/users/123', {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'Patched Name' })
});

// DELETE - Remove resource
await fetch('https://api.example.com/users/123', {
    method: 'DELETE'
});
```

### Response Handling

```javascript
const response = await fetch(url);

// Response properties
console.log(response.ok);         // true if status 200-299
console.log(response.status);     // 200, 404, 500, etc.
console.log(response.statusText); // "OK", "Not Found", etc.
console.log(response.headers.get('Content-Type'));

// Parse response body (pick one)
const json = await response.json();   // JSON → Object
const text = await response.text();   // Plain text
const blob = await response.blob();   // Binary data
const buffer = await response.arrayBuffer();
```

---

## ⚡ Advanced Patterns

### Request Wrapper

```javascript
class HttpClient {
    constructor(baseUrl, defaultHeaders = {}) {
        this.baseUrl = baseUrl;
        this.defaultHeaders = {
            'Content-Type': 'application/json',
            ...defaultHeaders
        };
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseUrl}${endpoint}`;
        const config = {
            ...options,
            headers: {
                ...this.defaultHeaders,
                ...options.headers
            }
        };

        if (options.body && typeof options.body === 'object') {
            config.body = JSON.stringify(options.body);
        }

        const response = await fetch(url, config);

        if (!response.ok) {
            const error = new Error(`HTTP ${response.status}`);
            error.response = response;
            error.status = response.status;
            try {
                error.data = await response.json();
            } catch {}
            throw error;
        }

        const contentType = response.headers.get('Content-Type');
        if (contentType?.includes('application/json')) {
            return response.json();
        }
        return response.text();
    }

    get(endpoint, options) {
        return this.request(endpoint, { ...options, method: 'GET' });
    }

    post(endpoint, body, options) {
        return this.request(endpoint, { ...options, method: 'POST', body });
    }

    put(endpoint, body, options) {
        return this.request(endpoint, { ...options, method: 'PUT', body });
    }

    delete(endpoint, options) {
        return this.request(endpoint, { ...options, method: 'DELETE' });
    }
}

// Usage
const api = new HttpClient('https://api.example.com', {
    'Authorization': 'Bearer ' + process.env.API_TOKEN
});

const users = await api.get('/users');
const newUser = await api.post('/users', { name: 'John' });
```

### Retry with Exponential Backoff

```javascript
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
    let lastError;

    for (let attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            const response = await fetch(url, options);

            // Retry on server errors
            if (response.status >= 500 && attempt < maxRetries) {
                throw new Error(`Server error: ${response.status}`);
            }

            return response;
        } catch (error) {
            lastError = error;

            if (attempt < maxRetries) {
                // Exponential backoff: 1s, 2s, 4s
                const delay = Math.pow(2, attempt) * 1000;
                console.log(`Retry ${attempt + 1}/${maxRetries} in ${delay}ms`);
                await new Promise(r => setTimeout(r, delay));
            }
        }
    }

    throw lastError;
}
```

### Timeout Handling

```javascript
async function fetchWithTimeout(url, options = {}, timeoutMs = 5000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

    try {
        const response = await fetch(url, {
            ...options,
            signal: controller.signal
        });
        return response;
    } catch (error) {
        if (error.name === 'AbortError') {
            throw new Error(`Request timed out after ${timeoutMs}ms`);
        }
        throw error;
    } finally {
        clearTimeout(timeoutId);
    }
}
```

### Concurrent Requests

```javascript
// Parallel requests
const [users, posts, comments] = await Promise.all([
    fetch('/api/users').then(r => r.json()),
    fetch('/api/posts').then(r => r.json()),
    fetch('/api/comments').then(r => r.json())
]);

// With error handling (allSettled)
const results = await Promise.allSettled([
    fetch('/api/service1').then(r => r.json()),
    fetch('/api/service2').then(r => r.json()),
    fetch('/api/service3').then(r => r.json())
]);

const successful = results
    .filter(r => r.status === 'fulfilled')
    .map(r => r.value);

const failed = results
    .filter(r => r.status === 'rejected')
    .map(r => r.reason);
```

---

## 🏗️ DevOps API Examples

### Health Check Client

```javascript
async function checkServiceHealth(services) {
    const checks = services.map(async (service) => {
        const startTime = Date.now();

        try {
            const response = await fetchWithTimeout(
                `${service.url}/health`,
                {},
                service.timeout || 5000
            );

            return {
                name: service.name,
                url: service.url,
                status: response.ok ? 'healthy' : 'unhealthy',
                statusCode: response.status,
                responseTime: Date.now() - startTime
            };
        } catch (error) {
            return {
                name: service.name,
                url: service.url,
                status: 'down',
                error: error.message,
                responseTime: Date.now() - startTime
            };
        }
    });

    return Promise.all(checks);
}

// Usage
const services = [
    { name: 'api', url: 'https://api.example.com' },
    { name: 'auth', url: 'https://auth.example.com' },
    { name: 'db', url: 'https://db.example.com', timeout: 10000 }
];

const healthReport = await checkServiceHealth(services);
console.table(healthReport);
```

### Webhook Sender

```javascript
async function sendWebhook(url, payload, options = {}) {
    const {
        secret,
        retries = 3,
        timeout = 10000
    } = options;

    const headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'DevOpsHub-Webhook/1.0'
    };

    // Add signature if secret provided
    if (secret) {
        const crypto = require('crypto');
        const signature = crypto
            .createHmac('sha256', secret)
            .update(JSON.stringify(payload))
            .digest('hex');
        headers['X-Webhook-Signature'] = `sha256=${signature}`;
    }

    return fetchWithRetry(url, {
        method: 'POST',
        headers,
        body: JSON.stringify(payload)
    }, retries);
}

// Send deployment notification
await sendWebhook('https://hooks.slack.com/services/XXX', {
    text: '🚀 Deployment successful!',
    blocks: [
        { type: 'header', text: { type: 'plain_text', text: 'Deployment Complete' }},
        { type: 'section', text: { type: 'mrkdwn', text: '*Service:* api-gateway\n*Version:* 2.1.0' }}
    ]
}, { retries: 2 });
```

### Rate-Limited API Client

```javascript
class RateLimitedClient {
    constructor(baseUrl, requestsPerSecond = 10) {
        this.baseUrl = baseUrl;
        this.minInterval = 1000 / requestsPerSecond;
        this.lastRequestTime = 0;
        this.queue = [];
        this.processing = false;
    }

    async request(endpoint, options = {}) {
        return new Promise((resolve, reject) => {
            this.queue.push({ endpoint, options, resolve, reject });
            this.processQueue();
        });
    }

    async processQueue() {
        if (this.processing || this.queue.length === 0) return;
        this.processing = true;

        while (this.queue.length > 0) {
            const timeSinceLastRequest = Date.now() - this.lastRequestTime;
            if (timeSinceLastRequest < this.minInterval) {
                await new Promise(r => setTimeout(r, this.minInterval - timeSinceLastRequest));
            }

            const { endpoint, options, resolve, reject } = this.queue.shift();
            this.lastRequestTime = Date.now();

            try {
                const response = await fetch(`${this.baseUrl}${endpoint}`, options);
                resolve(response);
            } catch (error) {
                reject(error);
            }
        }

        this.processing = false;
    }
}
```

---

## 🔥 Pro Tips

### 1. Always Check response.ok
```javascript
// ❌ Bad - 404 returns successfully
const data = await fetch(url).then(r => r.json());

// ✅ Good - throw on error status
const response = await fetch(url);
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const data = await response.json();
```

### 2. Cancel Abandoned Requests
```javascript
const controller = new AbortController();
fetch(url, { signal: controller.signal });
// Later...
controller.abort();  // Cancel if user navigates away
```

### 3. Use Headers for Caching
```javascript
const response = await fetch(url, {
    headers: {
        'If-None-Match': cachedEtag,
        'Cache-Control': 'no-cache'
    }
});
if (response.status === 304) {
    return cachedData;  // Use cache
}
```

---

## 🛠️ Hands-on Exercise

### Task: API Dashboard Fetcher

Build a client that:
1. Fetches data from 5 mock API endpoints in parallel
2. Implements retry with exponential backoff
3. Has request timeout of 5 seconds
4. Aggregates successful and failed responses
5. Returns a summary report with response times

---

## 📚 Deep Dive Resources

- [MDN: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [MDN: AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
"""
            },
            {
                "title": "Node.js Fundamentals",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 250,
                "content": r"""
# Node.js Fundamentals

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"Node.js brought JavaScript to the server. Now it powers your entire infrastructure."*

---

## 🎯 Why This Matters

Node.js is essential for DevOps:
- **CLI Tools:** npm, yarn, ESLint, Prettier
- **Build Systems:** Webpack, Vite, esbuild
- **Automation:** Scripts, webhooks, bots
- **Microservices:** Express, Fastify servers
- **Serverless:** AWS Lambda, Cloud Functions

Understanding Node.js unlocks the JavaScript ecosystem.

---

## 🧠 Core Concepts

### Node.js vs Browser JavaScript

```javascript
// Browser: window, document, DOM
// Node.js: global, process, fs, http, etc.

// Check environment
if (typeof window !== 'undefined') {
    console.log('Running in browser');
} else if (typeof process !== 'undefined') {
    console.log('Running in Node.js');
}
```

### Process Object

```javascript
// Current working directory
console.log(process.cwd());

// Environment variables
console.log(process.env.NODE_ENV);
console.log(process.env.HOME);

// Command line arguments
// node script.js arg1 arg2
console.log(process.argv);
// ['node', '/path/to/script.js', 'arg1', 'arg2']

const args = process.argv.slice(2);  // Just your args
console.log(args);  // ['arg1', 'arg2']

// Exit codes
process.exit(0);   // Success
process.exit(1);   // Error

// Standard streams
process.stdout.write('Output\n');
process.stderr.write('Error\n');

// Process info
console.log(process.pid);       // Process ID
console.log(process.platform);  // 'darwin', 'linux', 'win32'
console.log(process.version);   // Node.js version
```

### File System (fs)

```javascript
const fs = require('fs');
const fsPromises = require('fs/promises');

// ========================================
// SYNCHRONOUS (blocks execution)
// ========================================

// Read file
const content = fs.readFileSync('config.json', 'utf8');
const config = JSON.parse(content);

// Write file
fs.writeFileSync('output.txt', 'Hello, World!');

// Check if exists
if (fs.existsSync('data.json')) {
    console.log('File exists');
}

// ========================================
// ASYNC with Promises (recommended)
// ========================================

async function loadConfig() {
    try {
        const content = await fsPromises.readFile('config.json', 'utf8');
        return JSON.parse(content);
    } catch (error) {
        if (error.code === 'ENOENT') {
            console.log('Config not found, using defaults');
            return {};
        }
        throw error;
    }
}

async function saveData(filename, data) {
    await fsPromises.writeFile(
        filename,
        JSON.stringify(data, null, 2)
    );
}

// ========================================
// Directory operations
// ========================================

// List directory
const files = await fsPromises.readdir('./src');

// With file info
const entries = await fsPromises.readdir('./src', { withFileTypes: true });
const dirs = entries.filter(e => e.isDirectory()).map(e => e.name);
const jsFiles = entries.filter(e => e.isFile() && e.name.endsWith('.js'));

// Create directory (recursive)
await fsPromises.mkdir('./logs/2024/01', { recursive: true });

// Remove file
await fsPromises.unlink('temp.txt');

// Remove directory (recursive)
await fsPromises.rm('./temp', { recursive: true, force: true });

// File stats
const stats = await fsPromises.stat('app.js');
console.log(stats.size);         // File size in bytes
console.log(stats.isFile());     // true
console.log(stats.isDirectory()); // false
console.log(stats.mtime);        // Last modified time
```

### Path Module

```javascript
const path = require('path');

// Join paths (handles separators)
const configPath = path.join(__dirname, 'config', 'app.json');
// /Users/dev/project/config/app.json

// Parse path
const parsed = path.parse('/home/user/docs/file.txt');
// { root: '/', dir: '/home/user/docs', base: 'file.txt', ext: '.txt', name: 'file' }

// Get parts
path.dirname('/home/user/file.txt');   // '/home/user'
path.basename('/home/user/file.txt');  // 'file.txt'
path.extname('/home/user/file.txt');   // '.txt'

// Resolve to absolute path
path.resolve('src', 'app.js');  // /current/working/dir/src/app.js

// Relative path between two paths
path.relative('/data/logs', '/data/app/src');  // '../app/src'

// Platform separator
path.sep;  // '/' on Unix, '\\' on Windows
```

---

## ⚡ Built-in Modules

### Child Process (Run Commands)

```javascript
const { exec, execSync, spawn } = require('child_process');

// Execute command (simple)
exec('ls -la', (error, stdout, stderr) => {
    if (error) {
        console.error('Error:', error.message);
        return;
    }
    console.log('Output:', stdout);
});

// Synchronous (blocks)
try {
    const output = execSync('git status', { encoding: 'utf8' });
    console.log(output);
} catch (error) {
    console.error('Git error:', error.message);
}

// Spawn (better for long-running processes)
const ls = spawn('ls', ['-la', '/home']);

ls.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
    console.log(`Process exited with code ${code}`);
});

// With promises (Node 16+)
const { execSync: execPromise } = require('util').promisify(require('child_process').exec);

async function runCommand(cmd) {
    const { stdout, stderr } = await execPromise(cmd);
    return stdout.trim();
}
```

### OS Module

```javascript
const os = require('os');

console.log(os.platform());   // 'darwin', 'linux', 'win32'
console.log(os.arch());       // 'x64', 'arm64'
console.log(os.cpus().length); // Number of CPU cores
console.log(os.totalmem());   // Total memory in bytes
console.log(os.freemem());    // Free memory
console.log(os.homedir());    // User home directory
console.log(os.tmpdir());     // Temp directory
console.log(os.hostname());   // Computer hostname
console.log(os.networkInterfaces());  // Network interfaces
```

### HTTP Server (Quick)

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    // Health check endpoint
    if (req.url === '/health' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'healthy', timestamp: Date.now() }));
        return;
    }

    // 404 for everything else
    res.writeHead(404);
    res.end('Not Found');
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
    console.log('SIGTERM received, shutting down...');
    server.close(() => {
        console.log('Server closed');
        process.exit(0);
    });
});
```

---

## 🏗️ Module Systems

### CommonJS (CJS)

```javascript
// math.js
function add(a, b) { return a + b; }
function multiply(a, b) { return a * b; }

module.exports = { add, multiply };
// OR
module.exports.add = add;
module.exports.multiply = multiply;

// app.js
const { add, multiply } = require('./math');
const math = require('./math');

console.log(add(2, 3));        // 5
console.log(math.multiply(4, 5)); // 20
```

### ES Modules (ESM)

```javascript
// math.mjs (or .js with "type": "module" in package.json)
export function add(a, b) { return a + b; }
export function multiply(a, b) { return a * b; }
export default { add, multiply };

// app.mjs
import { add, multiply } from './math.mjs';
import math from './math.mjs';

// Dynamic import (both CJS and ESM)
const module = await import('./dynamic-module.mjs');
```

### Package.json

```json
{
    "name": "devops-tool",
    "version": "1.0.0",
    "type": "module",
    "main": "src/index.js",
    "bin": {
        "devops-tool": "./bin/cli.js"
    },
    "scripts": {
        "start": "node src/index.js",
        "dev": "node --watch src/index.js",
        "test": "node --test",
        "build": "esbuild src/index.js --bundle --outfile=dist/bundle.js"
    },
    "dependencies": {
        "chalk": "^5.0.0"
    },
    "devDependencies": {
        "esbuild": "^0.19.0"
    },
    "engines": {
        "node": ">=18.0.0"
    }
}
```

---

## 🔧 Practical Patterns

### Environment Config

```javascript
// config.js
const config = {
    port: parseInt(process.env.PORT || '3000'),
    nodeEnv: process.env.NODE_ENV || 'development',
    apiKey: process.env.API_KEY,
    database: {
        host: process.env.DB_HOST || 'localhost',
        port: parseInt(process.env.DB_PORT || '5432'),
        name: process.env.DB_NAME || 'devops'
    },
    isDev: process.env.NODE_ENV !== 'production'
};

// Validate required vars
const required = ['API_KEY'];
const missing = required.filter(key => !process.env[key]);
if (missing.length > 0) {
    console.error(`Missing environment variables: ${missing.join(', ')}`);
    process.exit(1);
}

module.exports = config;
```

### CLI Tool Pattern

```javascript
#!/usr/bin/env node
// bin/cli.js

const args = process.argv.slice(2);
const command = args[0];
const flags = args.slice(1);

const commands = {
    help: () => {
        console.log(`
Usage: devops-tool <command> [options]

Commands:
  deploy    Deploy the application
  status    Show deployment status
  rollback  Rollback to previous version
  help      Show this help
        `);
    },
    deploy: () => {
        console.log('Deploying...');
        // deployment logic
    },
    status: () => {
        console.log('Checking status...');
    }
};

if (!command || command === 'help') {
    commands.help();
} else if (commands[command]) {
    commands[command](flags);
} else {
    console.error(`Unknown command: ${command}`);
    process.exit(1);
}
```

---

## 🔥 Pro Tips

### 1. Use ESM for New Projects
```json
// package.json
{ "type": "module" }
```

### 2. Handle Uncaught Errors
```javascript
process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
    process.exit(1);
});
```

### 3. Use --watch for Development
```bash
node --watch app.js  # Auto-restart on changes
```

---

## 🛠️ Hands-on Exercise

### Task: File Watcher CLI

Build a CLI tool that:
1. Watches a directory for file changes
2. Runs a command when files change
3. Supports filtering by extension
4. Has configurable debounce
5. Logs changes with timestamps

---

## 📚 Deep Dive Resources

- [Node.js Documentation](https://nodejs.org/docs/latest/api/)
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
"""
            },
            {
                "title": "JavaScript DevOps Capstone",
                "difficulty": "hard",
                "estimated_minutes": 30,
                "xp_reward": 500,
                "content": r"""
# JavaScript DevOps Capstone

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


> *"You've learned the pieces. Now let's build something real."*

---

## 🎯 Project Overview

Build a **DevOps Dashboard CLI** that:
- Monitors multiple services
- Collects and displays metrics
- Sends alerts on failures
- Generates reports
- Can be scheduled as a cron job

This project combines everything:
- **Variables & Types:** Configuration
- **Functions & Classes:** Architecture
- **Async/Await:** API calls
- **Error Handling:** Resilience
- **JSON:** Data processing
- **Fetch API:** HTTP requests
- **Node.js:** File system, CLI

---

## 🏗️ Project Architecture

```
devops-dashboard/
├── package.json
├── .env
├── src/
│   ├── index.js          # Entry point
│   ├── config.js         # Configuration loader
│   ├── services/
│   │   ├── HealthChecker.js
│   │   ├── MetricsCollector.js
│   │   └── AlertSender.js
│   ├── reporters/
│   │   ├── ConsoleReporter.js
│   │   └── JsonReporter.js
│   └── utils/
│       ├── http.js
│       └── logger.js
└── tests/
    └── health.test.js
```

---

## 🧠 Implementation Guide

### 1. Configuration (config.js)

```javascript
import { readFile } from 'fs/promises';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

class Config {
    constructor() {
        this.services = [];
        this.alertWebhook = null;
        this.outputFormat = 'console';
        this.timeout = 5000;
        this.retries = 3;
    }

    async load(configPath) {
        try {
            // Load from file
            const content = await readFile(configPath, 'utf8');
            const fileConfig = JSON.parse(content);
            Object.assign(this, fileConfig);
        } catch (error) {
            if (error.code !== 'ENOENT') throw error;
            console.warn('No config file, using defaults');
        }

        // Override with environment variables
        if (process.env.ALERT_WEBHOOK) {
            this.alertWebhook = process.env.ALERT_WEBHOOK;
        }
        if (process.env.TIMEOUT) {
            this.timeout = parseInt(process.env.TIMEOUT);
        }
        if (process.env.OUTPUT_FORMAT) {
            this.outputFormat = process.env.OUTPUT_FORMAT;
        }

        return this;
    }

    validate() {
        if (!this.services || this.services.length === 0) {
            throw new Error('At least one service must be configured');
        }

        for (const service of this.services) {
            if (!service.name || !service.url) {
                throw new Error('Each service must have name and url');
            }
        }

        return true;
    }
}

export const config = new Config();
export default config;
```

### 2. HTTP Utility (utils/http.js)

```javascript
export class HttpClient {
    constructor(options = {}) {
        this.timeout = options.timeout || 5000;
        this.retries = options.retries || 3;
    }

    async fetch(url, options = {}) {
        const controller = new AbortController();
        const timeoutId = setTimeout(
            () => controller.abort(),
            this.timeout
        );

        let lastError;

        for (let attempt = 0; attempt <= this.retries; attempt++) {
            try {
                const response = await fetch(url, {
                    ...options,
                    signal: controller.signal
                });

                clearTimeout(timeoutId);
                return response;
            } catch (error) {
                lastError = error;

                if (error.name === 'AbortError') {
                    throw new Error(`Request to ${url} timed out`);
                }

                if (attempt < this.retries) {
                    const delay = Math.pow(2, attempt) * 1000;
                    await new Promise(r => setTimeout(r, delay));
                }
            }
        }

        throw lastError;
    }

    async getJson(url) {
        const response = await this.fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    }

    async postJson(url, data) {
        const response = await this.fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json().catch(() => ({}));
    }
}

export const http = new HttpClient();
```

### 3. Health Checker (services/HealthChecker.js)

```javascript
import { http } from '../utils/http.js';

export class HealthChecker {
    constructor(services, options = {}) {
        this.services = services;
        this.timeout = options.timeout || 5000;
    }

    async checkService(service) {
        const startTime = Date.now();

        try {
            const response = await http.fetch(service.url, {
                timeout: service.timeout || this.timeout
            });

            const responseTime = Date.now() - startTime;

            return {
                name: service.name,
                url: service.url,
                status: response.ok ? 'healthy' : 'unhealthy',
                statusCode: response.status,
                responseTime,
                timestamp: new Date().toISOString()
            };
        } catch (error) {
            return {
                name: service.name,
                url: service.url,
                status: 'down',
                error: error.message,
                responseTime: Date.now() - startTime,
                timestamp: new Date().toISOString()
            };
        }
    }

    async checkAll() {
        const results = await Promise.all(
            this.services.map(s => this.checkService(s))
        );

        return {
            timestamp: new Date().toISOString(),
            summary: {
                total: results.length,
                healthy: results.filter(r => r.status === 'healthy').length,
                unhealthy: results.filter(r => r.status === 'unhealthy').length,
                down: results.filter(r => r.status === 'down').length
            },
            services: results
        };
    }
}
```

### 4. Alert Sender (services/AlertSender.js)

```javascript
import { http } from '../utils/http.js';

export class AlertSender {
    constructor(webhookUrl) {
        this.webhookUrl = webhookUrl;
    }

    async send(healthReport) {
        if (!this.webhookUrl) return;

        const failures = healthReport.services.filter(
            s => s.status !== 'healthy'
        );

        if (failures.length === 0) return;

        const message = this.formatMessage(healthReport, failures);

        try {
            await http.postJson(this.webhookUrl, message);
            console.log(`Alert sent for ${failures.length} service(s)`);
        } catch (error) {
            console.error('Failed to send alert:', error.message);
        }
    }

    formatMessage(report, failures) {
        // Slack-compatible message
        return {
            text: `🚨 Service Alert: ${failures.length} service(s) failing`,
            blocks: [
                {
                    type: 'header',
                    text: {
                        type: 'plain_text',
                        text: '🚨 DevOps Dashboard Alert'
                    }
                },
                {
                    type: 'section',
                    text: {
                        type: 'mrkdwn',
                        text: `*${failures.length}* of *${report.summary.total}* services are not healthy`
                    }
                },
                ...failures.map(f => ({
                    type: 'section',
                    text: {
                        type: 'mrkdwn',
                        text: `*${f.name}*: ${f.status}\n${f.error || f.statusCode}`
                    }
                }))
            ]
        };
    }
}
```

### 5. Console Reporter (reporters/ConsoleReporter.js)

```javascript
export class ConsoleReporter {
    report(healthReport) {
        console.log('\n' + '='.repeat(60));
        console.log('DEVOPS DASHBOARD HEALTH REPORT');
        console.log('='.repeat(60));
        console.log(`Timestamp: ${healthReport.timestamp}`);
        console.log('');

        // Summary
        const { summary } = healthReport;
        console.log('SUMMARY:');
        console.log(`  Total Services: ${summary.total}`);
        console.log(`  ✅ Healthy: ${summary.healthy}`);
        console.log(`  ⚠️  Unhealthy: ${summary.unhealthy}`);
        console.log(`  ❌ Down: ${summary.down}`);
        console.log('');

        // Details
        console.log('SERVICE DETAILS:');
        console.log('-'.repeat(60));

        for (const service of healthReport.services) {
            const icon = this.getStatusIcon(service.status);
            console.log(`${icon} ${service.name}`);
            console.log(`   URL: ${service.url}`);
            console.log(`   Status: ${service.status}`);
            console.log(`   Response Time: ${service.responseTime}ms`);
            if (service.error) {
                console.log(`   Error: ${service.error}`);
            }
            console.log('');
        }

        console.log('='.repeat(60));
    }

    getStatusIcon(status) {
        const icons = {
            healthy: '✅',
            unhealthy: '⚠️',
            down: '❌'
        };
        return icons[status] || '❓';
    }
}
```

### 6. Main Entry Point (index.js)

```javascript
#!/usr/bin/env node

import { config } from './config.js';
import { HealthChecker } from './services/HealthChecker.js';
import { AlertSender } from './services/AlertSender.js';
import { ConsoleReporter } from './reporters/ConsoleReporter.js';
import { writeFile } from 'fs/promises';

async function main() {
    try {
        // Parse CLI arguments
        const args = process.argv.slice(2);
        const configPath = args.find(a => a.startsWith('--config='))
            ?.replace('--config=', '') || './config.json';

        // Load and validate config
        await config.load(configPath);
        config.validate();

        console.log(`Checking ${config.services.length} services...\n`);

        // Run health checks
        const checker = new HealthChecker(config.services, {
            timeout: config.timeout
        });
        const report = await checker.checkAll();

        // Output report
        if (config.outputFormat === 'json') {
            console.log(JSON.stringify(report, null, 2));
        } else {
            const reporter = new ConsoleReporter();
            reporter.report(report);
        }

        // Save report to file
        if (config.reportFile) {
            await writeFile(
                config.reportFile,
                JSON.stringify(report, null, 2)
            );
            console.log(`Report saved to ${config.reportFile}`);
        }

        // Send alerts if any failures
        if (config.alertWebhook) {
            const alerter = new AlertSender(config.alertWebhook);
            await alerter.send(report);
        }

        // Exit with error code if any services down
        if (report.summary.down > 0) {
            process.exit(1);
        }

    } catch (error) {
        console.error('Fatal error:', error.message);
        process.exit(1);
    }
}

main();
```

---

## 🚀 Running Your Project

### Configuration File (config.json)

```json
{
    "services": [
        { "name": "API Gateway", "url": "https://api.example.com/health" },
        { "name": "Auth Service", "url": "https://auth.example.com/health" },
        { "name": "Database", "url": "https://db.example.com/health", "timeout": 10000 }
    ],
    "timeout": 5000,
    "retries": 3,
    "outputFormat": "console",
    "reportFile": "./reports/health-report.json"
}
```

### Package.json Scripts

```json
{
    "type": "module",
    "bin": {
        "devops-dashboard": "./src/index.js"
    },
    "scripts": {
        "start": "node src/index.js",
        "check": "node src/index.js --config=./config.json",
        "check:json": "OUTPUT_FORMAT=json node src/index.js"
    }
}
```

### Running

```bash
# Direct run
node src/index.js

# With config
node src/index.js --config=./production.json

# As cron job (every 5 minutes)
# crontab -e
# */5 * * * * cd /path/to/project && node src/index.js >> /var/log/health.log 2>&1
```

---

## 🎯 Extension Challenges

1. **Add Metrics History:** Store health data in JSON file, show trends
2. **Parallel Checks:** Use Promise.allSettled with concurrency limit
3. **Custom Checks:** Support POST endpoints, header auth, body validation
4. **Dashboard Server:** Add Express server with real-time updates
5. **Docker Support:** Containerize and run in Kubernetes

---

## ✅ You've Completed JavaScript for DevOps!

You now have production-ready skills:
- ✅ Modern JavaScript (ES6+)
- ✅ Async programming patterns
- ✅ Error handling strategies
- ✅ HTTP/API integration
- ✅ Node.js CLI development
- ✅ Professional project structure

**Next Steps:**
- Build more automation tools
- Contribute to open-source DevOps projects
- Explore TypeScript for type safety
- Learn testing (Jest, Vitest)

---

## 📚 Resources for Continued Learning

- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [JavaScript Info](https://javascript.info/)
- [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS)

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_JAVASCRIPT


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_JAVASCRIPT["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
