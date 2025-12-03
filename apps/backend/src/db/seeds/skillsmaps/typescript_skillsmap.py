"""
TypeScript SkillsMap — Type-Safe JavaScript for DevOps
======================================================

20 nodes covering TypeScript from basics to advanced patterns.
Akhilesh-style pedagogy: Hook → Concept → Code → Pro Tips → Hands-on

Block 1 (1-2): Introduction & Annotations
Block 2 (3-4): Basic Types & Inference
Block 3 (5-6): Interfaces & Type Aliases
Block 4 (7-8): Union/Intersection & Functions
Block 5 (9-10): Generics & Utility Types
Block 6 (11-12): Classes & Modules
Block 7 (13-14): Declaration Files & Advanced
Block 8 (15-16): Decorators & Namespaces
Block 9 (17-18): Config & Testing
Block 10 (19-20): DevOps Capstone
"""

from typing import Any

# ============================================================================
# BLOCK 1: INTRODUCTION & ANNOTATIONS (Nodes 1-2)
# ============================================================================

TS_NODE_01_INTRODUCTION = {
    "id": "ts-01-introduction",
    "title": "TypeScript Introduction",
    "description": "Understand TypeScript's value and set up your environment",
    "content": """
# TypeScript Introduction

> *"TypeScript is JavaScript that scales. Catch bugs before runtime, not after deployment."*

---

## 🎯 Why This Matters

In DevOps, reliability is everything:
- **Catch bugs at compile time** — Not at 3 AM in production
- **Self-documenting code** — Types ARE documentation
- **Better tooling** — Autocomplete, refactoring, navigation
- **Team scale** — Multiple engineers, one codebase

TypeScript powers:
- VS Code (written in TypeScript)
- Most modern CLI tools
- AWS CDK, Pulumi
- All major frontend frameworks

---

## 🧠 Core Concepts

### What is TypeScript?

```typescript
// TypeScript = JavaScript + Types
// It compiles to plain JavaScript

// JavaScript (runtime error)
function greet(name) {
    return name.toUpperCase();
}
greet(42); // Runtime error!

// TypeScript (compile-time error)
function greetSafe(name: string): string {
    return name.toUpperCase();
}
greetSafe(42); // ❌ Error: Argument of type 'number' is not assignable
```

### TypeScript vs JavaScript

| Feature | JavaScript | TypeScript |
|---------|------------|------------|
| Type checking | Runtime | Compile-time |
| Error detection | Late | Early |
| IDE support | Basic | Excellent |
| Refactoring | Risky | Safe |
| Learning curve | Lower | Slightly higher |

---

## ⚡ Quick Setup

### Installation

```bash
# Install TypeScript globally
npm install -g typescript

# Check version
tsc --version

# Initialize a project
mkdir my-ts-project && cd my-ts-project
npm init -y
npm install typescript --save-dev

# Create tsconfig.json
npx tsc --init
```

### Your First TypeScript File

```typescript
// hello.ts
const message: string = "Hello, DevOps!";
console.log(message);

// Compile to JavaScript
// tsc hello.ts

// Run the output
// node hello.js
```

### tsconfig.json Basics

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

---

## 🔧 Development Workflow

```bash
# Watch mode (auto-compile on save)
tsc --watch

# Run TypeScript directly (development)
npx ts-node src/index.ts

# Or use tsx (faster)
npx tsx src/index.ts
```

---

## 🔥 Pro Tips

### 1. Use Strict Mode
```json
// tsconfig.json
{ "compilerOptions": { "strict": true } }
```

### 2. Install ts-node for Scripts
```bash
npm install -D ts-node @types/node
```

---

## 🛠️ Hands-on Exercise

Create a TypeScript project:
1. Initialize npm and TypeScript
2. Configure tsconfig.json with strict mode
3. Create src/index.ts with typed variables
4. Compile and run

---

## 📚 Resources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- [TypeScript Playground](https://www.typescriptlang.org/play)
""",
    "xp_reward": 150,
    "estimated_time": "40 minutes",
    "difficulty": "beginner",
    "order_index": 1,
    "tags": ["typescript", "setup", "introduction", "configuration"],
}

TS_NODE_02_TYPE_ANNOTATIONS = {
    "id": "ts-02-type-annotations",
    "title": "Type Annotations",
    "description": "Learn to annotate variables, functions, and parameters",
    "content": """
# Type Annotations

> *"Explicit types are documentation that the compiler enforces."*

---

## 🎯 Why This Matters

Type annotations:
- Make code self-documenting
- Enable IDE autocomplete
- Catch errors before runtime
- Communicate intent to other developers

---

## 🧠 Core Concepts

### Variable Annotations

```typescript
// Syntax: let variableName: type = value;

// Primitives
let serviceName: string = "api-gateway";
let port: number = 8080;
let isHealthy: boolean = true;

// Arrays
let hosts: string[] = ["host1", "host2", "host3"];
let ports: number[] = [80, 443, 8080];
let mixed: (string | number)[] = ["host", 8080];

// Alternative array syntax
let servers: Array<string> = ["srv1", "srv2"];
```

### Function Annotations

```typescript
// Parameter and return type annotations
function deployService(name: string, replicas: number): boolean {
    console.log(`Deploying ${name} with ${replicas} replicas`);
    return true;
}

// Arrow functions
const getPort = (service: string): number => {
    const ports: Record<string, number> = {
        api: 3000,
        web: 80,
        db: 5432
    };
    return ports[service] || 8080;
};

// Void return type (no return value)
function logEvent(event: string): void {
    console.log(`[${new Date().toISOString()}] ${event}`);
}

// Optional parameters
function configure(host: string, port?: number): void {
    console.log(`Host: ${host}, Port: ${port ?? 3000}`);
}

// Default parameters
function connect(url: string, timeout: number = 5000): void {
    console.log(`Connecting to ${url} (timeout: ${timeout}ms)`);
}
```

### Object Annotations

```typescript
// Inline object type
let server: { host: string; port: number; ssl: boolean } = {
    host: "localhost",
    port: 443,
    ssl: true
};

// Optional properties
let config: {
    name: string;
    version: string;
    debug?: boolean;  // Optional
} = {
    name: "my-service",
    version: "1.0.0"
};

// Readonly properties
let constants: {
    readonly API_VERSION: string;
    readonly MAX_RETRIES: number;
} = {
    API_VERSION: "v2",
    MAX_RETRIES: 3
};

constants.API_VERSION = "v3"; // ❌ Error: Cannot assign to readonly
```

---

## ⚡ Special Types

### Any, Unknown, Never

```typescript
// any - Opt out of type checking (avoid!)
let legacy: any = "could be anything";
legacy = 42;
legacy.nonexistent(); // No error, but will crash

// unknown - Type-safe any
let input: unknown = getUserInput();
// input.toUpperCase(); // ❌ Error
if (typeof input === "string") {
    input.toUpperCase(); // ✅ OK after type guard
}

// never - Function never returns
function throwError(message: string): never {
    throw new Error(message);
}

function infiniteLoop(): never {
    while (true) {}
}
```

### Tuple Types

```typescript
// Fixed-length array with specific types
let serverInfo: [string, number] = ["localhost", 8080];

// Named tuples (TypeScript 4.0+)
let endpoint: [host: string, port: number, ssl: boolean] =
    ["api.example.com", 443, true];

// Destructuring
const [host, port, ssl] = endpoint;
```

---

## 🔧 Type Assertions

```typescript
// When you know more than TypeScript
const input = document.getElementById("config") as HTMLInputElement;
const value = input.value;

// Alternative syntax
const element = <HTMLInputElement>document.getElementById("config");

// Non-null assertion (use carefully!)
function getConfig(): string | undefined {
    return process.env.CONFIG;
}
const config = getConfig()!; // Assert it's not undefined
```

---

## 🔥 Pro Tips

### 1. Let TypeScript Infer When Obvious
```typescript
// ❌ Redundant
const name: string = "api";

// ✅ Let it infer
const name = "api"; // TypeScript knows it's string
```

### 2. Use const for Literal Types
```typescript
let status = "active";      // type: string
const status2 = "active";   // type: "active" (literal)

const config = {
    port: 3000,
    host: "localhost"
} as const; // All properties readonly
```

---

## 🛠️ Hands-on Exercise

Create typed functions:
1. `healthCheck(url: string): Promise<boolean>`
2. `parseConfig(json: string): { host: string; port: number }`
3. `formatLog(level: string, message: string, timestamp?: Date): string`

---

## 📚 Resources

- [TypeScript: Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
""",
    "xp_reward": 175,
    "estimated_time": "45 minutes",
    "difficulty": "beginner",
    "order_index": 2,
    "tags": ["typescript", "types", "annotations", "functions"],
}


# ============================================================================
# BLOCK 2: BASIC TYPES & INFERENCE (Nodes 3-4)
# ============================================================================

TS_NODE_03_BASIC_TYPES = {
    "id": "ts-03-basic-types",
    "title": "Basic Types Deep Dive",
    "description": "Master all primitive and built-in types",
    "content": """
# Basic Types Deep Dive

> *"Know your types like you know your infrastructure."*

---

## 🎯 Why This Matters

Understanding TypeScript's type system lets you:
- Model any data structure
- Prevent entire categories of bugs
- Write more expressive code

---

## 🧠 Primitive Types

### String, Number, Boolean

```typescript
// String - text data
const serviceName: string = "api-gateway";
const multiLine: string = `
    Service: ${serviceName}
    Status: Active
`;

// Number - integers and floats
const port: number = 8080;
const pi: number = 3.14159;
const hex: number = 0xff;
const binary: number = 0b1010;

// Boolean - true/false
const isEnabled: boolean = true;
const hasSSL: boolean = port === 443;
```

### Null and Undefined

```typescript
// undefined - variable declared but not assigned
let config: string | undefined;
console.log(config); // undefined

// null - intentional absence of value
let connection: DatabaseConnection | null = null;

// strictNullChecks (recommended)
function getUser(id: string): User | null {
    // Return null if not found
    return users.get(id) ?? null;
}
```

### Symbol and BigInt

```typescript
// Symbol - unique identifiers
const id1 = Symbol("id");
const id2 = Symbol("id");
console.log(id1 === id2); // false - always unique

// BigInt - large integers
const bigNumber: bigint = 9007199254740991n;
const anotherBig: bigint = BigInt("12345678901234567890");
```

---

## ⚡ Object Types

### Object Literal Types

```typescript
// Define object shape inline
const server: {
    host: string;
    port: number;
    ssl: boolean;
    metadata?: Record<string, string>;
} = {
    host: "localhost",
    port: 443,
    ssl: true
};

// Nested objects
const deployment: {
    name: string;
    spec: {
        replicas: number;
        containers: { image: string; ports: number[] }[];
    };
} = {
    name: "api",
    spec: {
        replicas: 3,
        containers: [
            { image: "api:v1", ports: [8080] }
        ]
    }
};
```

### Array Types

```typescript
// Two equivalent syntaxes
const hosts: string[] = ["h1", "h2", "h3"];
const ports: Array<number> = [80, 443, 8080];

// Multi-dimensional arrays
const matrix: number[][] = [
    [1, 2, 3],
    [4, 5, 6]
];

// Array of objects
const services: { name: string; port: number }[] = [
    { name: "api", port: 3000 },
    { name: "web", port: 80 }
];
```

### Tuple Types

```typescript
// Fixed-length, typed arrays
type HostPort = [string, number];
const server: HostPort = ["localhost", 8080];

// Rest elements in tuples
type LogEntry = [Date, string, ...string[]];
const log: LogEntry = [new Date(), "ERROR", "Connection", "failed"];

// Optional tuple elements
type Config = [string, number?];
const minimal: Config = ["host"];
const full: Config = ["host", 8080];
```

---

## 🔧 Enum Types

```typescript
// Numeric enum (default)
enum Status {
    Pending,    // 0
    Active,     // 1
    Completed,  // 2
    Failed      // 3
}

const taskStatus: Status = Status.Active;
console.log(Status[1]); // "Active" - reverse mapping

// String enum (recommended for DevOps)
enum LogLevel {
    Debug = "DEBUG",
    Info = "INFO",
    Warn = "WARN",
    Error = "ERROR"
}

function log(level: LogLevel, message: string): void {
    console.log(`[${level}] ${message}`);
}

log(LogLevel.Error, "Connection failed");

// Const enum (inlined at compile time)
const enum HttpMethod {
    GET = "GET",
    POST = "POST",
    PUT = "PUT",
    DELETE = "DELETE"
}
```

---

## 🏗️ Literal Types

```typescript
// String literals
type Environment = "development" | "staging" | "production";
const env: Environment = "production";

// Number literals
type DiceRoll = 1 | 2 | 3 | 4 | 5 | 6;
const roll: DiceRoll = 4;

// Boolean literal
type Success = true;
const result: Success = true;

// Template literal types (TS 4.1+)
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";
type Endpoint = `/api/${string}`;
type Route = `${HttpMethod} ${Endpoint}`;

const route: Route = "GET /api/users";
```

---

## 🔥 Pro Tips

### 1. Prefer String Enums Over Numeric
```typescript
// ✅ String enum - readable in logs
enum Status { Active = "ACTIVE" }

// ❌ Numeric - "1" in logs is confusing
enum Status { Active = 1 }
```

### 2. Use as const for Immutable Literals
```typescript
const config = {
    port: 3000,
    host: "localhost"
} as const;
// type: { readonly port: 3000; readonly host: "localhost" }
```

---

## 🛠️ Hands-on Exercise

Create types for:
1. Log levels enum (DEBUG, INFO, WARN, ERROR)
2. HTTP response tuple: [status: number, body: string, headers: object]
3. Server config with optional SSL settings

---

## 📚 Resources

- [TypeScript Handbook: Basic Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
""",
    "xp_reward": 175,
    "estimated_time": "45 minutes",
    "difficulty": "beginner",
    "order_index": 3,
    "tags": ["typescript", "types", "primitives", "enums"],
}

TS_NODE_04_TYPE_INFERENCE = {
    "id": "ts-04-type-inference",
    "title": "Type Inference",
    "description": "Let TypeScript figure out types automatically",
    "content": """
# Type Inference

> *"The best type annotation is the one you don't have to write."*

---

## 🎯 Why This Matters

TypeScript's inference:
- Reduces boilerplate code
- Makes refactoring safer
- Keeps code readable
- Still provides full type safety

---

## 🧠 Core Concepts

### Variable Inference

```typescript
// TypeScript infers from initialization
let name = "api-gateway";     // string
let port = 8080;              // number
let isActive = true;          // boolean

// const gets literal types
const env = "production";     // type: "production" (not string!)
const maxRetries = 3;         // type: 3 (not number!)

// Arrays
const hosts = ["h1", "h2"];   // string[]
const mixed = [1, "two"];     // (string | number)[]

// Objects
const config = {
    host: "localhost",
    port: 3000
};
// type: { host: string; port: number }
```

### Function Return Inference

```typescript
// Return type inferred
function add(a: number, b: number) {
    return a + b;  // Returns number
}

// Complex inference
function getServerConfig() {
    return {
        host: "localhost",
        port: process.env.PORT ? parseInt(process.env.PORT) : 3000,
        ssl: false
    };
}
// Return type: { host: string; port: number; ssl: boolean }

// Conditional return inference
function parseValue(input: string) {
    if (input === "true") return true;
    if (input === "false") return false;
    return input;
}
// Return type: string | boolean
```

### Contextual Typing

```typescript
// TypeScript infers from context
const numbers = [1, 2, 3, 4, 5];

// 'n' is inferred as number from array type
const doubled = numbers.map(n => n * 2);

// Event handlers
document.addEventListener("click", event => {
    // 'event' is MouseEvent
    console.log(event.clientX, event.clientY);
});

// Array methods
const servers = [
    { name: "api", port: 3000 },
    { name: "web", port: 80 }
];

// 's' is inferred as { name: string; port: number }
const names = servers.map(s => s.name);
```

---

## ⚡ Best Common Type

```typescript
// TypeScript finds the "best common type"
const items = [1, 2, null];  // (number | null)[]

// Mixed array
const mixed = [1, "two", { three: 3 }];
// type: (string | number | { three: number })[]

// Empty array needs annotation
const empty: string[] = [];  // Would be never[] without annotation
```

---

## 🔧 Control Flow Analysis

```typescript
// TypeScript tracks types through code flow
function processValue(value: string | number) {
    // value is string | number here

    if (typeof value === "string") {
        // value is string here
        return value.toUpperCase();
    }

    // value is number here
    return value.toFixed(2);
}

// Truthiness narrowing
function printValue(value: string | null | undefined) {
    if (value) {
        // value is string (null/undefined excluded)
        console.log(value.length);
    }
}

// Equality narrowing
function compare(a: string | number, b: string | boolean) {
    if (a === b) {
        // Both must be string (only common type)
        console.log(a.toUpperCase());
    }
}
```

---

## 🏗️ When to Annotate vs Infer

```typescript
// ✅ Let inference work
const port = 3000;
const hosts = ["h1", "h2"];
const config = { host: "localhost" };

// ✅ Annotate function parameters
function deploy(service: string, replicas: number) {
    // ...
}

// ✅ Annotate public API return types
function getConfig(): ServerConfig {
    return { host: "localhost", port: 3000 };
}

// ✅ Annotate when inference is wrong
const ids: string[] = [];  // Not never[]

// ✅ Annotate complex types
const handlers: Map<string, (data: unknown) => void> = new Map();
```

---

## 🔥 Pro Tips

### 1. Hover for Inferred Types
In VS Code, hover over variables to see inferred types.

### 2. Use satisfies for Validation
```typescript
// Validate type while preserving inference
const config = {
    port: 3000,
    host: "localhost"
} satisfies { port: number; host: string };
// config.port is still type 3000, not number
```

### 3. Return Type for Complex Functions
```typescript
// Explicit return type documents intent
async function fetchUsers(): Promise<User[]> {
    const response = await fetch("/api/users");
    return response.json();
}
```

---

## 🛠️ Hands-on Exercise

Practice inference:
1. Create variables and check inferred types
2. Write functions without return type annotations
3. Use control flow narrowing with type guards

---

## 📚 Resources

- [TypeScript: Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html)
""",
    "xp_reward": 175,
    "estimated_time": "40 minutes",
    "difficulty": "beginner",
    "order_index": 4,
    "tags": ["typescript", "inference", "types", "narrowing"],
}


# ============================================================================
# BLOCK 3: INTERFACES & TYPE ALIASES (Nodes 5-6)
# ============================================================================

TS_NODE_05_INTERFACES = {
    "id": "ts-05-interfaces",
    "title": "Interfaces",
    "description": "Define object shapes and contracts",
    "content": """
# Interfaces

> *"Interfaces define contracts. Code to the contract, not the implementation."*

---

## 🎯 Why This Matters

Interfaces are the backbone of TypeScript:
- Define object shapes
- Enable duck typing
- Support extension/inheritance
- Document API contracts

---

## 🧠 Core Concepts

### Basic Interface

```typescript
interface Server {
    host: string;
    port: number;
    ssl: boolean;
}

const apiServer: Server = {
    host: "api.example.com",
    port: 443,
    ssl: true
};

// Missing property = error
const badServer: Server = {
    host: "localhost",
    port: 8080
    // ❌ Error: Property 'ssl' is missing
};
```

### Optional & Readonly Properties

```typescript
interface Config {
    readonly name: string;        // Can't be changed
    version: string;
    debug?: boolean;              // Optional
    readonly apiKey?: string;     // Optional + readonly
}

const config: Config = {
    name: "my-service",
    version: "1.0.0"
};

config.version = "1.0.1";  // ✅ OK
config.name = "other";     // ❌ Error: readonly
```

### Method Signatures

```typescript
interface Logger {
    // Method signature
    log(message: string): void;

    // Function property (equivalent)
    error: (message: string, code?: number) => void;

    // Optional method
    debug?(message: string): void;
}

const consoleLogger: Logger = {
    log(message) {
        console.log(`[LOG] ${message}`);
    },
    error(message, code) {
        console.error(`[ERROR ${code ?? 500}] ${message}`);
    }
};
```

---

## ⚡ Interface Extension

```typescript
interface BaseService {
    name: string;
    version: string;
}

interface HttpService extends BaseService {
    port: number;
    protocol: "http" | "https";
}

interface DatabaseService extends BaseService {
    connectionString: string;
    poolSize: number;
}

// Multiple inheritance
interface FullService extends HttpService, DatabaseService {
    healthEndpoint: string;
}

const service: HttpService = {
    name: "api",
    version: "1.0.0",
    port: 3000,
    protocol: "https"
};
```

### Declaration Merging

```typescript
// Same interface can be declared multiple times
interface Window {
    customProperty: string;
}

// TypeScript merges them automatically
// Now Window has customProperty + all standard properties
```

---

## 🔧 Index Signatures

```typescript
// Allow any string keys
interface StringMap {
    [key: string]: string;
}

const env: StringMap = {
    NODE_ENV: "production",
    API_KEY: "secret123",
    LOG_LEVEL: "info"
};

// Mixed with defined properties
interface Config {
    name: string;
    version: string;
    [key: string]: string;  // Additional properties
}

// Numeric index
interface StringArray {
    [index: number]: string;
}

const arr: StringArray = ["a", "b", "c"];
```

---

## 🏗️ Function Interfaces

```typescript
// Interface for function type
interface Comparator<T> {
    (a: T, b: T): number;
}

const numberSort: Comparator<number> = (a, b) => a - b;
const stringSort: Comparator<string> = (a, b) => a.localeCompare(b);

// Callable with properties
interface Logger {
    (message: string): void;
    level: string;
    setLevel(level: string): void;
}

function createLogger(): Logger {
    const logger = ((message: string) => {
        console.log(`[${logger.level}] ${message}`);
    }) as Logger;

    logger.level = "INFO";
    logger.setLevel = (level) => { logger.level = level; };

    return logger;
}
```

---

## 🔥 Pro Tips

### 1. Use Interfaces for Objects
```typescript
// ✅ Interfaces for object shapes
interface User { name: string; }

// ✅ Type aliases for unions/primitives
type Status = "active" | "inactive";
```

### 2. Prefer Readonly
```typescript
interface ImmutableConfig {
    readonly host: string;
    readonly port: number;
}
```

---

## 🛠️ Hands-on Exercise

Create interfaces for:
1. `ServiceConfig` with name, port, optional healthPath
2. `LoggerInterface` with log, error, warn methods
3. `CacheStore<T>` with get, set, delete operations

---

## 📚 Resources

- [TypeScript: Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 5,
    "tags": ["typescript", "interfaces", "objects", "contracts"],
}

TS_NODE_06_TYPE_ALIASES = {
    "id": "ts-06-type-aliases",
    "title": "Type Aliases",
    "description": "Create reusable type definitions",
    "content": """
# Type Aliases

> *"Name your types for clarity. Complex types deserve names."*

---

## 🎯 Why This Matters

Type aliases let you:
- Name complex types
- Create union/intersection types
- Build reusable type definitions
- Document domain concepts

---

## 🧠 Core Concepts

### Basic Type Alias

```typescript
// Alias for primitive
type UserId = string;
type Port = number;
type IsActive = boolean;

// Alias for object
type Server = {
    host: string;
    port: Port;
    active: IsActive;
};

// Alias for function
type Handler = (event: Event) => void;
type Callback<T> = (error: Error | null, result: T) => void;

// Usage
const serverId: UserId = "srv-123";
const apiPort: Port = 3000;
```

### Union Types

```typescript
// Union = one of several types
type Status = "pending" | "active" | "completed" | "failed";
type StringOrNumber = string | number;
type MaybeUser = User | null | undefined;

function setStatus(status: Status): void {
    console.log(`Status: ${status}`);
}

setStatus("active");     // ✅
setStatus("unknown");    // ❌ Error

// Discriminated unions
type Result<T> =
    | { success: true; data: T }
    | { success: false; error: string };

function handleResult(result: Result<User>) {
    if (result.success) {
        console.log(result.data.name);  // TypeScript knows data exists
    } else {
        console.error(result.error);     // TypeScript knows error exists
    }
}
```

### Intersection Types

```typescript
// Intersection = combine multiple types
type Timestamps = {
    createdAt: Date;
    updatedAt: Date;
};

type Identifiable = {
    id: string;
};

type Entity = Timestamps & Identifiable;

// Same as:
// {
//     id: string;
//     createdAt: Date;
//     updatedAt: Date;
// }

type Service = {
    name: string;
    port: number;
} & Timestamps & Identifiable;
```

---

## ⚡ Advanced Patterns

### Conditional Types

```typescript
// Type depends on condition
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;  // false

// Extract/Exclude
type NonNull<T> = T extends null | undefined ? never : T;
type StringOrNull = string | null;
type JustString = NonNull<StringOrNull>;  // string
```

### Template Literal Types

```typescript
// Build string types
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";
type ApiVersion = "v1" | "v2";
type Endpoint = `/${ApiVersion}/${string}`;

type Route = `${HttpMethod} ${Endpoint}`;
const route: Route = "GET /v1/users";  // ✅
const bad: Route = "PATCH /v1/users";  // ❌

// Generate property names
type EventName = "click" | "focus" | "blur";
type EventHandler = `on${Capitalize<EventName>}`;
// "onClick" | "onFocus" | "onBlur"
```

### Mapped Types

```typescript
// Transform existing types
type Readonly<T> = {
    readonly [K in keyof T]: T[K];
};

type Partial<T> = {
    [K in keyof T]?: T[K];
};

type Required<T> = {
    [K in keyof T]-?: T[K];  // Remove optional
};

// Usage
interface Config {
    host: string;
    port: number;
}

type ReadonlyConfig = Readonly<Config>;
type PartialConfig = Partial<Config>;
```

---

## 🔧 Type vs Interface

```typescript
// Interfaces: better for objects, can extend
interface User {
    name: string;
}
interface Admin extends User {
    role: string;
}

// Type aliases: better for unions, primitives, complex types
type Status = "active" | "inactive";
type StringOrNumber = string | number;
type Config = User & { settings: object };

// Interfaces merge, types don't
interface Window {
    myProp: string;
}
// Adds myProp to Window

// type Window = { myProp: string };
// ❌ Error: Duplicate identifier
```

---

## 🏗️ Practical Patterns

```typescript
// API Response wrapper
type ApiResponse<T> = {
    data: T;
    status: number;
    message: string;
    timestamp: Date;
};

// Partial update
type UpdateUser = Partial<User> & { id: string };

// Pick specific properties
type UserSummary = Pick<User, "id" | "name">;

// Omit properties
type PublicUser = Omit<User, "password" | "email">;

// Record type
type ServiceRegistry = Record<string, {
    url: string;
    healthy: boolean;
}>;
```

---

## 🔥 Pro Tips

### 1. Use Descriptive Names
```typescript
// ✅ Good - clear intent
type UserId = string;
type Port = number;

// ❌ Bad - generic
type S = string;
```

### 2. Export Reusable Types
```typescript
// types.ts
export type Status = "active" | "inactive";
export type Handler<T> = (data: T) => void;
```

---

## 🛠️ Hands-on Exercise

Create type aliases:
1. `HttpResponse<T>` with data, status, headers
2. `DeploymentStatus` union of states
3. `ServiceConfig` intersection of base + optional fields

---

## 📚 Resources

- [TypeScript: Type Aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 6,
    "tags": ["typescript", "types", "aliases", "unions", "intersections"],
}


# ============================================================================
# BLOCK 4: UNION/INTERSECTION & FUNCTIONS (Nodes 7-8)
# ============================================================================

TS_NODE_07_UNION_INTERSECTION = {
    "id": "ts-07-union-intersection",
    "title": "Union & Intersection Types",
    "description": "Combine types for flexible, precise modeling",
    "content": """
# Union & Intersection Types

> *"Union for 'or', intersection for 'and'. Model reality precisely."*

---

## 🎯 Why This Matters

Union and intersection types let you:
- Model real-world complexity
- Create flexible APIs
- Implement discriminated unions
- Build type-safe state machines

---

## 🧠 Union Types (OR)

### Basic Unions

```typescript
// Value can be one of several types
type StringOrNumber = string | number;
let id: StringOrNumber = "abc123";
id = 42;  // Also valid

// Literal unions
type Status = "pending" | "active" | "completed";
type LogLevel = "debug" | "info" | "warn" | "error";

// Nullable types
type MaybeString = string | null;
type OptionalNumber = number | undefined;
```

### Discriminated Unions

```typescript
// Each variant has a "discriminant" property
type Success<T> = {
    kind: "success";
    data: T;
};

type Failure = {
    kind: "failure";
    error: string;
    code: number;
};

type Result<T> = Success<T> | Failure;

function handleResult<T>(result: Result<T>): void {
    switch (result.kind) {
        case "success":
            console.log("Data:", result.data);
            break;
        case "failure":
            console.error(`Error ${result.code}: ${result.error}`);
            break;
    }
}

// State machine example
type ConnectionState =
    | { status: "disconnected" }
    | { status: "connecting"; attempt: number }
    | { status: "connected"; socket: WebSocket }
    | { status: "error"; message: string };

function render(state: ConnectionState): string {
    switch (state.status) {
        case "disconnected":
            return "Click to connect";
        case "connecting":
            return `Connecting (attempt ${state.attempt})...`;
        case "connected":
            return "Connected!";
        case "error":
            return `Error: ${state.message}`;
    }
}
```

---

## ⚡ Intersection Types (AND)

### Basic Intersections

```typescript
// Combine multiple types
type Timestamps = {
    createdAt: Date;
    updatedAt: Date;
};

type Identifiable = {
    id: string;
};

type Nameable = {
    name: string;
};

// Entity has ALL properties
type Entity = Timestamps & Identifiable & Nameable;

const user: Entity = {
    id: "user-123",
    name: "John",
    createdAt: new Date(),
    updatedAt: new Date()
};
```

### Mixing with Interfaces

```typescript
interface BaseConfig {
    host: string;
    port: number;
}

interface SSLConfig {
    ssl: boolean;
    cert?: string;
}

type SecureConfig = BaseConfig & SSLConfig;

const config: SecureConfig = {
    host: "localhost",
    port: 443,
    ssl: true,
    cert: "/path/to/cert.pem"
};
```

---

## 🔧 Type Narrowing

```typescript
// typeof guard
function process(value: string | number): string {
    if (typeof value === "string") {
        return value.toUpperCase();
    }
    return value.toFixed(2);
}

// in guard
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function move(animal: Fish | Bird): void {
    if ("swim" in animal) {
        animal.swim();
    } else {
        animal.fly();
    }
}

// instanceof guard
function formatDate(date: Date | string): string {
    if (date instanceof Date) {
        return date.toISOString();
    }
    return new Date(date).toISOString();
}

// Custom type guard
function isSuccess<T>(result: Result<T>): result is Success<T> {
    return result.kind === "success";
}

const result: Result<User> = await fetchUser();
if (isSuccess(result)) {
    console.log(result.data.name);  // TypeScript knows it's Success
}
```

---

## 🏗️ Practical Patterns

```typescript
// API Error Handling
type ApiError =
    | { type: "network"; message: string }
    | { type: "validation"; fields: string[] }
    | { type: "auth"; reason: "expired" | "invalid" };

function handleError(error: ApiError): void {
    switch (error.type) {
        case "network":
            console.log("Network error:", error.message);
            break;
        case "validation":
            console.log("Invalid fields:", error.fields.join(", "));
            break;
        case "auth":
            if (error.reason === "expired") {
                refreshToken();
            }
            break;
    }
}

// Builder Pattern
type Builder<T> = T & {
    build(): T;
};

// Exhaustive check
function assertNever(x: never): never {
    throw new Error(`Unexpected value: ${x}`);
}

function handleStatus(status: Status): void {
    switch (status) {
        case "pending": return;
        case "active": return;
        case "completed": return;
        default:
            assertNever(status);  // Error if case missing
    }
}
```

---

## 🔥 Pro Tips

### 1. Use Discriminated Unions for State
```typescript
type LoadingState<T> =
    | { status: "idle" }
    | { status: "loading" }
    | { status: "success"; data: T }
    | { status: "error"; error: Error };
```

### 2. Prefer Narrowing Over Casting
```typescript
// ❌ Type assertion (unsafe)
const value = data as User;

// ✅ Type guard (safe)
if (isUser(data)) { /* data is User */ }
```

---

## 🛠️ Hands-on Exercise

Create:
1. `HttpResult` discriminated union (success/error)
2. Type guard `isHttpError()`
3. Exhaustive switch handler

---

## 📚 Resources

- [TypeScript: Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 7,
    "tags": ["typescript", "unions", "intersections", "narrowing"],
}

TS_NODE_08_FUNCTIONS = {
    "id": "ts-08-functions",
    "title": "Function Types",
    "description": "Master function signatures, overloads, and advanced patterns",
    "content": """
# Function Types

> *"Functions are first-class citizens. Type them like it."*

---

## 🎯 Why This Matters

Proper function typing:
- Documents expected inputs/outputs
- Enables better autocomplete
- Catches argument errors early
- Supports advanced patterns

---

## 🧠 Core Concepts

### Basic Function Types

```typescript
// Function declaration
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Function type alias
type MathOp = (a: number, b: number) => number;
const divide: MathOp = (a, b) => a / b;

// Function interface
interface Calculator {
    (a: number, b: number): number;
}
```

### Optional & Default Parameters

```typescript
// Optional parameter
function greet(name: string, greeting?: string): string {
    return `${greeting ?? "Hello"}, ${name}!`;
}

greet("World");           // "Hello, World!"
greet("World", "Hi");     // "Hi, World!"

// Default parameter
function connect(host: string, port: number = 3000): void {
    console.log(`Connecting to ${host}:${port}`);
}

// Rest parameters
function sum(...numbers: number[]): number {
    return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3, 4, 5);  // 15
```

### Generic Functions

```typescript
// Type parameter
function identity<T>(value: T): T {
    return value;
}

const str = identity("hello");  // string
const num = identity(42);       // number

// Multiple type parameters
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second];
}

// Constrained generics
function getLength<T extends { length: number }>(item: T): number {
    return item.length;
}

getLength("hello");     // 5
getLength([1, 2, 3]);   // 3
getLength({ length: 10 }); // 10
```

---

## ⚡ Function Overloads

```typescript
// Multiple signatures for same function
function process(input: string): string;
function process(input: number): number;
function process(input: string | number): string | number {
    if (typeof input === "string") {
        return input.toUpperCase();
    }
    return input * 2;
}

const str = process("hello");  // string
const num = process(21);       // number

// Overloads with different parameters
function createElement(tag: "div"): HTMLDivElement;
function createElement(tag: "span"): HTMLSpanElement;
function createElement(tag: "canvas"): HTMLCanvasElement;
function createElement(tag: string): HTMLElement {
    return document.createElement(tag);
}

const div = createElement("div");  // HTMLDivElement
```

---

## 🔧 Callbacks & Higher-Order Functions

```typescript
// Callback type
type Callback<T> = (error: Error | null, result: T) => void;

function fetchData(url: string, callback: Callback<string>): void {
    // Simulated async operation
    setTimeout(() => {
        callback(null, `Data from ${url}`);
    }, 1000);
}

// Higher-order function
function withRetry<T>(
    fn: () => Promise<T>,
    retries: number = 3
): () => Promise<T> {
    return async () => {
        let lastError: Error | undefined;
        for (let i = 0; i < retries; i++) {
            try {
                return await fn();
            } catch (err) {
                lastError = err as Error;
            }
        }
        throw lastError;
    };
}

// Function that returns function
function createMultiplier(factor: number): (n: number) => number {
    return (n) => n * factor;
}

const double = createMultiplier(2);
double(5);  // 10
```

---

## 🏗️ This Type

```typescript
// Explicit this type
interface Button {
    label: string;
    onClick(this: Button): void;
}

const button: Button = {
    label: "Submit",
    onClick() {
        console.log(`Clicked: ${this.label}`);
    }
};

// This parameter in callbacks
function addClickHandler(
    el: HTMLElement,
    handler: (this: HTMLElement, event: MouseEvent) => void
): void {
    el.addEventListener("click", handler);
}
```

---

## 🔥 Pro Tips

### 1. Use Readonly for Input Arrays
```typescript
function process(items: readonly string[]): void {
    // items.push("x");  // ❌ Error
}
```

### 2. Return Type Inference
```typescript
// Let TS infer simple returns
const add = (a: number, b: number) => a + b;

// Explicit for public APIs
export function fetchUser(id: string): Promise<User> {
    // ...
}
```

### 3. Void vs Undefined
```typescript
// void = return value ignored
type Logger = (msg: string) => void;

// undefined = must return undefined
type Getter = () => undefined;
```

---

## 🛠️ Hands-on Exercise

Create:
1. Generic `retry<T>(fn, times)` function
2. Overloaded `parse()` for string/number
3. Higher-order `debounce` function

---

## 📚 Resources

- [TypeScript: Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html)
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 8,
    "tags": ["typescript", "functions", "generics", "overloads"],
}


# ============================================================================
# BLOCK 5: GENERICS & UTILITY TYPES (Nodes 9-10)
# ============================================================================

TS_NODE_09_GENERICS = {
    "id": "ts-09-generics",
    "title": "Generics",
    "description": "Create reusable, type-safe components",
    "content": """
# Generics

> *"Write once, use with any type. That's the power of generics."*

---

## 🎯 Why This Matters

Generics enable:
- Reusable components with type safety
- Type inference for better DX
- Constraints for specific behavior
- Foundation for utility types

---

## 🧠 Core Concepts

### Basic Generics

```typescript
// Generic function
function identity<T>(value: T): T {
    return value;
}

// Type inferred from argument
const str = identity("hello");  // string
const num = identity(42);       // number

// Explicit type
const explicit = identity<string>("world");

// Generic array function
function firstElement<T>(arr: T[]): T | undefined {
    return arr[0];
}

const first = firstElement([1, 2, 3]);  // number | undefined
```

### Generic Interfaces & Types

```typescript
// Generic interface
interface Container<T> {
    value: T;
    getValue(): T;
    setValue(value: T): void;
}

// Generic type alias
type Result<T> = {
    success: boolean;
    data: T;
    error?: string;
};

// Generic class
class Box<T> {
    constructor(private value: T) {}

    get(): T {
        return this.value;
    }

    set(value: T): void {
        this.value = value;
    }
}

const stringBox = new Box("hello");
const numberBox = new Box(42);
```

---

## ⚡ Generic Constraints

```typescript
// Constraint with extends
function getLength<T extends { length: number }>(item: T): number {
    return item.length;
}

getLength("hello");      // ✅ string has length
getLength([1, 2, 3]);    // ✅ array has length
getLength({ length: 5 }); // ✅ object has length
// getLength(42);         // ❌ number has no length

// Constraint with interface
interface Printable {
    print(): string;
}

function printItem<T extends Printable>(item: T): void {
    console.log(item.print());
}

// keyof constraint
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

const user = { name: "John", age: 30 };
const name = getProperty(user, "name");  // string
const age = getProperty(user, "age");    // number
// getProperty(user, "email");  // ❌ Error
```

### Multiple Type Parameters

```typescript
// Two type parameters
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second];
}

const result = pair("hello", 42);  // [string, number]

// Map function
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
    return arr.map(fn);
}

const numbers = [1, 2, 3];
const strings = map(numbers, n => n.toString());  // string[]
```

---

## 🔧 Default Type Parameters

```typescript
// Default type
interface Response<T = unknown> {
    data: T;
    status: number;
}

const generic: Response = { data: "anything", status: 200 };
const typed: Response<User> = { data: user, status: 200 };

// Multiple defaults
type ApiResult<T = unknown, E = Error> = {
    data?: T;
    error?: E;
};
```

---

## 🏗️ Practical Patterns

```typescript
// Generic API client
class ApiClient<T> {
    constructor(private baseUrl: string) {}

    async get(endpoint: string): Promise<T> {
        const response = await fetch(`${this.baseUrl}${endpoint}`);
        return response.json();
    }

    async post(endpoint: string, data: Partial<T>): Promise<T> {
        const response = await fetch(`${this.baseUrl}${endpoint}`, {
            method: "POST",
            body: JSON.stringify(data)
        });
        return response.json();
    }
}

const userApi = new ApiClient<User>("/api/users");
const users = await userApi.get("/");

// Generic cache
class Cache<T> {
    private store = new Map<string, { value: T; expiry: number }>();

    set(key: string, value: T, ttl: number): void {
        this.store.set(key, { value, expiry: Date.now() + ttl });
    }

    get(key: string): T | undefined {
        const item = this.store.get(key);
        if (!item || item.expiry < Date.now()) return undefined;
        return item.value;
    }
}
```

---

## 🔥 Pro Tips

### 1. Use Descriptive Type Names
```typescript
// ✅ Descriptive
function merge<TSource, TTarget>(source: TSource, target: TTarget)

// ❌ Cryptic
function merge<S, T>(source: S, target: T)
```

### 2. Prefer Inference
```typescript
// Let TS infer when possible
const result = identity("hello");  // ✅
const result = identity<string>("hello");  // Unnecessary
```

---

## 🛠️ Hands-on Exercise

Create:
1. Generic `Stack<T>` with push/pop
2. Generic `Result<T, E>` type
3. Constrained `stringify<T extends object>()`

---

## 📚 Resources

- [TypeScript: Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
""",
    "xp_reward": 225,
    "estimated_time": "55 minutes",
    "difficulty": "intermediate",
    "order_index": 9,
    "tags": ["typescript", "generics", "constraints", "reusability"],
}

TS_NODE_10_UTILITY_TYPES = {
    "id": "ts-10-utility-types",
    "title": "Utility Types",
    "description": "Transform types with built-in utilities",
    "content": """
# Utility Types

> *"Don't repeat type definitions. Transform them."*

---

## 🎯 Why This Matters

Utility types:
- Reduce code duplication
- Create derived types easily
- Enable powerful transformations
- Built into TypeScript

---

## 🧠 Property Modifiers

### Partial & Required

```typescript
interface User {
    id: string;
    name: string;
    email: string;
    age?: number;
}

// All properties optional
type PartialUser = Partial<User>;
// { id?: string; name?: string; email?: string; age?: number }

// All properties required
type RequiredUser = Required<User>;
// { id: string; name: string; email: string; age: number }

// Use case: Update function
function updateUser(id: string, updates: Partial<User>): User {
    const user = getUser(id);
    return { ...user, ...updates };
}

updateUser("123", { name: "New Name" });  // Only update name
```

### Readonly

```typescript
// All properties readonly
type ImmutableUser = Readonly<User>;

const user: ImmutableUser = {
    id: "123",
    name: "John",
    email: "john@example.com"
};

// user.name = "Jane";  // ❌ Error

// Deep readonly (custom)
type DeepReadonly<T> = {
    readonly [K in keyof T]: T[K] extends object
        ? DeepReadonly<T[K]>
        : T[K];
};
```

---

## ⚡ Property Selection

### Pick & Omit

```typescript
interface Service {
    id: string;
    name: string;
    port: number;
    host: string;
    ssl: boolean;
    apiKey: string;
}

// Pick specific properties
type ServiceSummary = Pick<Service, "id" | "name" | "port">;
// { id: string; name: string; port: number }

// Omit specific properties
type PublicService = Omit<Service, "apiKey">;
// { id: string; name: string; port: number; host: string; ssl: boolean }

// Combine them
type ServiceEndpoint = Pick<Service, "host" | "port" | "ssl">;
```

---

## 🔧 Record & Map Types

### Record

```typescript
// Create object type with specific keys
type ServiceStatus = Record<string, "healthy" | "unhealthy" | "unknown">;

const status: ServiceStatus = {
    api: "healthy",
    db: "healthy",
    cache: "unknown"
};

// Literal keys
type HttpCodes = Record<200 | 404 | 500, string>;
const messages: HttpCodes = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
};

// Enum keys
enum Service { Api, Web, Worker }
type ServiceConfig = Record<Service, { port: number }>;
```

---

## 🏗️ Extraction Types

### Extract & Exclude

```typescript
type AllStatus = "pending" | "active" | "completed" | "failed" | "cancelled";

// Extract matching types
type ActiveStatus = Extract<AllStatus, "active" | "pending">;
// "active" | "pending"

// Exclude matching types
type FinalStatus = Exclude<AllStatus, "pending" | "active">;
// "completed" | "failed" | "cancelled"

// With objects
type Animal = { type: "cat"; meow: () => void } | { type: "dog"; bark: () => void };
type Dog = Extract<Animal, { type: "dog" }>;
```

### NonNullable

```typescript
type MaybeString = string | null | undefined;
type DefiniteString = NonNullable<MaybeString>;
// string

// Useful for filtering
const items: (string | null)[] = ["a", null, "b", null, "c"];
const filtered: string[] = items.filter((x): x is string => x !== null);
```

---

## ⚙️ Function Types

### Parameters & ReturnType

```typescript
function createService(name: string, port: number, ssl: boolean): Service {
    return { id: crypto.randomUUID(), name, port, host: "localhost", ssl, apiKey: "" };
}

// Get parameter types as tuple
type CreateParams = Parameters<typeof createService>;
// [string, number, boolean]

// Get return type
type CreateResult = ReturnType<typeof createService>;
// Service

// Async function return type
async function fetchUser(id: string): Promise<User> { /* ... */ }
type FetchResult = Awaited<ReturnType<typeof fetchUser>>;
// User (unwrapped from Promise)
```

### ConstructorParameters

```typescript
class Logger {
    constructor(public name: string, public level: "debug" | "info") {}
}

type LoggerParams = ConstructorParameters<typeof Logger>;
// [string, "debug" | "info"]
```

---

## 🔥 Advanced Combinations

```typescript
// Create update type
type Updateable<T> = Partial<Omit<T, "id" | "createdAt">>;

interface User {
    id: string;
    name: string;
    email: string;
    createdAt: Date;
}

type UserUpdate = Updateable<User>;
// { name?: string; email?: string }

// Required with defaults
type WithDefaults<T, D extends keyof T> =
    Omit<T, D> & Required<Pick<T, D>>;

// Strict partial (at least one property)
type AtLeastOne<T> = {
    [K in keyof T]: Pick<T, K> & Partial<Omit<T, K>>;
}[keyof T];
```

---

## 🔥 Pro Tips

### 1. Chain Utilities
```typescript
type CleanUser = Readonly<Required<Omit<User, "password">>>;
```

### 2. Create Custom Utilities
```typescript
type Nullable<T> = T | null;
type Optional<T> = T | undefined;
type Maybe<T> = T | null | undefined;
```

---

## 🛠️ Hands-on Exercise

Create:
1. `UpdateDTO<T>` = Partial without id/timestamps
2. `ServiceRegistry` using Record
3. `SafeConfig` = Readonly + Required

---

## 📚 Resources

- [TypeScript: Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
""",
    "xp_reward": 225,
    "estimated_time": "55 minutes",
    "difficulty": "intermediate",
    "order_index": 10,
    "tags": ["typescript", "utility-types", "partial", "pick", "omit"],
}


# ============================================================================
# BLOCK 6: CLASSES & MODULES (Nodes 11-12)
# ============================================================================

TS_NODE_11_CLASSES = {
    "id": "ts-11-classes",
    "title": "Classes in TypeScript",
    "description": "Object-oriented programming with type safety",
    "content": """
# Classes in TypeScript

> *"Classes with types = self-documenting, maintainable code."*

---

## 🎯 Why This Matters

TypeScript classes provide:
- Type-safe OOP
- Access modifiers (public, private, protected)
- Abstract classes and interfaces
- Better tooling support

---

## 🧠 Core Concepts

### Basic Class

```typescript
class Service {
    // Properties with types
    name: string;
    port: number;
    private apiKey: string;

    // Constructor
    constructor(name: string, port: number, apiKey: string) {
        this.name = name;
        this.port = port;
        this.apiKey = apiKey;
    }

    // Methods
    getUrl(): string {
        return `http://${this.name}:${this.port}`;
    }

    // Private method
    private authenticate(): boolean {
        return this.apiKey.length > 0;
    }
}

const api = new Service("api", 3000, "secret");
console.log(api.getUrl());  // http://api:3000
// api.apiKey;  // ❌ Error: private
```

### Parameter Properties (Shorthand)

```typescript
// Shorthand: declare and assign in constructor
class Service {
    constructor(
        public name: string,
        public port: number,
        private apiKey: string,
        readonly id: string = crypto.randomUUID()
    ) {}

    getUrl(): string {
        return `http://${this.name}:${this.port}`;
    }
}

// Equivalent to previous example but much shorter!
```

---

## ⚡ Access Modifiers

```typescript
class DatabaseConnection {
    public host: string;           // Accessible everywhere
    protected port: number;        // Accessible in class and subclasses
    private password: string;      // Only in this class
    readonly connectionId: string; // Cannot be modified after init

    constructor(host: string, port: number, password: string) {
        this.host = host;
        this.port = port;
        this.password = password;
        this.connectionId = crypto.randomUUID();
    }
}

class PostgresConnection extends DatabaseConnection {
    getConnectionString(): string {
        // Can access public and protected
        return `postgres://${this.host}:${this.port}`;
        // this.password;  // ❌ Cannot access private
    }
}
```

---

## 🔧 Inheritance & Interfaces

```typescript
// Interface implementation
interface Startable {
    start(): Promise<void>;
    stop(): Promise<void>;
    isRunning(): boolean;
}

class Server implements Startable {
    private running = false;

    async start(): Promise<void> {
        this.running = true;
        console.log("Server started");
    }

    async stop(): Promise<void> {
        this.running = false;
        console.log("Server stopped");
    }

    isRunning(): boolean {
        return this.running;
    }
}

// Class inheritance
class HttpServer extends Server {
    constructor(public port: number) {
        super();  // Call parent constructor
    }

    async start(): Promise<void> {
        await super.start();
        console.log(`Listening on port ${this.port}`);
    }
}
```

### Abstract Classes

```typescript
abstract class BaseLogger {
    abstract log(message: string): void;
    abstract error(message: string): void;

    // Concrete method
    info(message: string): void {
        this.log(`[INFO] ${message}`);
    }

    warn(message: string): void {
        this.log(`[WARN] ${message}`);
    }
}

class ConsoleLogger extends BaseLogger {
    log(message: string): void {
        console.log(message);
    }

    error(message: string): void {
        console.error(`[ERROR] ${message}`);
    }
}

// const logger = new BaseLogger();  // ❌ Cannot instantiate abstract
const logger = new ConsoleLogger();
logger.info("Starting...");
```

---

## 🏗️ Static Members & Getters/Setters

```typescript
class Config {
    private static instance: Config;
    private _port: number = 3000;

    // Singleton pattern
    static getInstance(): Config {
        if (!Config.instance) {
            Config.instance = new Config();
        }
        return Config.instance;
    }

    // Static property
    static readonly VERSION = "1.0.0";

    // Getter
    get port(): number {
        return this._port;
    }

    // Setter with validation
    set port(value: number) {
        if (value < 1 || value > 65535) {
            throw new Error("Invalid port");
        }
        this._port = value;
    }
}

const config = Config.getInstance();
config.port = 8080;
console.log(Config.VERSION);
```

---

## 🔥 Pro Tips

### 1. Use readonly for Immutability
```typescript
class User {
    readonly id: string;
    constructor(public name: string) {
        this.id = crypto.randomUUID();
    }
}
```

### 2. Prefer Composition Over Inheritance
```typescript
class Service {
    constructor(
        private logger: Logger,
        private cache: Cache
    ) {}
}
```

---

## 🛠️ Hands-on Exercise

Create:
1. `Logger` abstract class with implementations
2. `Cache<T>` class with get/set/delete
3. `ServiceManager` singleton

---

## 📚 Resources

- [TypeScript: Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 11,
    "tags": ["typescript", "classes", "oop", "inheritance"],
}

TS_NODE_12_MODULES = {
    "id": "ts-12-modules",
    "title": "Modules & Namespaces",
    "description": "Organize code with ES modules and TypeScript features",
    "content": """
# Modules & Namespaces

> *"Good architecture starts with good module organization."*

---

## 🎯 Why This Matters

Modules enable:
- Code organization
- Encapsulation
- Reusability
- Clear dependencies

---

## 🧠 ES Modules

### Named Exports

```typescript
// utils.ts
export function formatDate(date: Date): string {
    return date.toISOString();
}

export const VERSION = "1.0.0";

export interface Config {
    host: string;
    port: number;
}

export class Logger {
    log(msg: string): void {
        console.log(msg);
    }
}

// main.ts
import { formatDate, VERSION, Config, Logger } from "./utils";

const logger = new Logger();
logger.log(formatDate(new Date()));
```

### Default Exports

```typescript
// service.ts
export default class ApiService {
    constructor(private baseUrl: string) {}

    async get<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${this.baseUrl}${endpoint}`);
        return response.json();
    }
}

// main.ts
import ApiService from "./service";
// or with alias
import Api from "./service";

const api = new Api("https://api.example.com");
```

### Re-exports

```typescript
// index.ts (barrel file)
export { Logger } from "./logger";
export { Config } from "./config";
export { ApiService as Api } from "./api";
export * from "./utils";
export * as helpers from "./helpers";

// Usage
import { Logger, Config, Api } from "./lib";
```

---

## ⚡ Import Types

```typescript
// Type-only imports (erased at runtime)
import type { User, Config } from "./types";

// Mixed import
import { createUser, type User } from "./users";

// Import for side effects only
import "./polyfills";

// Dynamic import
async function loadModule() {
    const { heavyFunction } = await import("./heavy-module");
    return heavyFunction();
}
```

---

## 🔧 Module Resolution

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "node",  // or "bundler" for modern
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"],
      "@utils/*": ["utils/*"],
      "@services/*": ["services/*"]
    }
  }
}

// Now you can import:
import { Logger } from "@/logger";
import { formatDate } from "@utils/date";
import { ApiService } from "@services/api";
```

---

## 🏗️ Project Structure

```bash
src/
├── index.ts              # Entry point
├── types/
│   ├── index.ts          # Barrel export
│   ├── user.ts
│   └── config.ts
├── services/
│   ├── index.ts
│   ├── api.service.ts
│   └── cache.service.ts
├── utils/
│   ├── index.ts
│   ├── date.ts
│   └── string.ts
└── config/
    ├── index.ts
    └── database.ts
```

```typescript
// types/index.ts
export * from "./user";
export * from "./config";

// services/index.ts
export { ApiService } from "./api.service";
export { CacheService } from "./cache.service";

// Entry point
import { User, Config } from "./types";
import { ApiService, CacheService } from "./services";
```

---

## 📦 Declaration Files

```typescript
// global.d.ts - Ambient declarations
declare const API_URL: string;
declare const DEBUG: boolean;

// Extend existing types
declare global {
    interface Window {
        analytics: AnalyticsService;
    }
}

// Module augmentation
declare module "express" {
    interface Request {
        user?: User;
    }
}
```

---

## 🔥 Pro Tips

### 1. Use Barrel Files
```typescript
// Don't: import from deep paths
import { User } from "./types/entities/user";

// Do: import from barrel
import { User } from "./types";
```

### 2. Avoid Circular Dependencies
```typescript
// types.ts - shared types, no imports from other modules
// This file should be dependency-free
```

### 3. Use type-only Imports
```typescript
// Smaller bundles, clearer intent
import type { Config } from "./config";
```

---

## 🛠️ Hands-on Exercise

Create project structure:
1. `types/` folder with User, Config
2. `services/` with ApiService, Logger
3. `utils/` with helpers
4. Barrel exports for each folder

---

## 📚 Resources

- [TypeScript: Modules](https://www.typescriptlang.org/docs/handbook/2/modules.html)
""",
    "xp_reward": 200,
    "estimated_time": "45 minutes",
    "difficulty": "intermediate",
    "order_index": 12,
    "tags": ["typescript", "modules", "imports", "exports", "organization"],
}


# ============================================================================
# BLOCK 7: ADVANCED TYPES & TYPE GUARDS (Nodes 13-14)
# ============================================================================

TS_NODE_13_ADVANCED_TYPES = {
    "id": "ts-13-advanced-types",
    "title": "Advanced Types",
    "description": "Master conditional types, mapped types, and template literals",
    "content": """
# Advanced Types

> *"Advanced types let you express complex relationships with precision."*

---

## 🎯 Why This Matters

Advanced types enable:
- Complex type transformations
- Conditional logic at type level
- Better library design
- Type-safe APIs

---

## 🧠 Conditional Types

```typescript
// T extends U ? X : Y
type IsString<T> = T extends string ? true : false;

type A = IsString<"hello">;  // true
type B = IsString<42>;       // false

// Practical example
type ApiResponse<T> = T extends void
    ? { success: boolean }
    : { success: boolean; data: T };

type EmptyResponse = ApiResponse<void>;   // { success: boolean }
type UserResponse = ApiResponse<User>;    // { success: boolean; data: User }

// Infer keyword
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type ArrayElement<T> = T extends (infer E)[] ? E : never;

type Func = () => string;
type FuncReturn = ReturnType<Func>;  // string

type Arr = number[];
type Elem = ArrayElement<Arr>;  // number
```

---

## ⚡ Mapped Types

```typescript
// Transform all properties
type Readonly<T> = {
    readonly [K in keyof T]: T[K];
};

type Optional<T> = {
    [K in keyof T]?: T[K];
};

// Modify property names
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

interface User {
    name: string;
    age: number;
}

type UserGetters = Getters<User>;
// { getName: () => string; getAge: () => number }

// Filter properties
type OnlyStrings<T> = {
    [K in keyof T as T[K] extends string ? K : never]: T[K];
};

type StringProps = OnlyStrings<User>;  // { name: string }
```

---

## 🔧 Template Literal Types

```typescript
// String manipulation at type level
type EventName = "click" | "focus" | "blur";
type Handler = `on${Capitalize<EventName>}`;
// "onClick" | "onFocus" | "onBlur"

// HTTP routes
type Method = "GET" | "POST" | "PUT" | "DELETE";
type Route = `/${string}`;
type Endpoint = `${Method} ${Route}`;

const endpoint: Endpoint = "GET /api/users";  // ✅

// Intrinsic string types
type Upper = Uppercase<"hello">;    // "HELLO"
type Lower = Lowercase<"HELLO">;    // "hello"
type Cap = Capitalize<"hello">;     // "Hello"
type Uncap = Uncapitalize<"Hello">; // "hello"

// Dynamic property access
type PropPath<T, K extends keyof T> =
    K extends string ? `${K}.${string & keyof T[K]}` : never;
```

---

## 🏗️ Recursive Types

```typescript
// JSON type
type Json =
    | string
    | number
    | boolean
    | null
    | Json[]
    | { [key: string]: Json };

// Deep partial
type DeepPartial<T> = T extends object
    ? { [K in keyof T]?: DeepPartial<T[K]> }
    : T;

// Deep readonly
type DeepReadonly<T> = T extends object
    ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
    : T;

// Flatten nested object paths
type Paths<T> = T extends object
    ? { [K in keyof T]: K extends string
        ? T[K] extends object
            ? K | `${K}.${Paths<T[K]>}`
            : K
        : never
    }[keyof T]
    : never;
```

---

## 🔥 Pro Tips

### 1. Use Distributive Conditionals
```typescript
type ToArray<T> = T extends any ? T[] : never;
type Result = ToArray<string | number>;  // string[] | number[]
```

### 2. Avoid Over-Engineering
```typescript
// Simple is often better
type Simple = { name: string };
// vs complex mapped type for same result
```

---

## 🛠️ Hands-on Exercise

Create:
1. `DeepRequired<T>` utility
2. `PathValue<T, Path>` type
3. `EventMap` with template literals

---

## 📚 Resources

- [TypeScript: Advanced Types](https://www.typescriptlang.org/docs/handbook/2/types-from-types.html)
""",
    "xp_reward": 250,
    "estimated_time": "60 minutes",
    "difficulty": "advanced",
    "order_index": 13,
    "tags": ["typescript", "advanced", "conditional", "mapped-types"],
}

TS_NODE_14_TYPE_GUARDS = {
    "id": "ts-14-type-guards",
    "title": "Type Guards & Narrowing",
    "description": "Runtime checks that inform the type system",
    "content": """
# Type Guards & Narrowing

> *"Tell TypeScript what you know at runtime."*

---

## 🎯 Why This Matters

Type guards:
- Safely handle union types
- Enable runtime validation
- Provide type-safe APIs
- Bridge runtime and compile time

---

## 🧠 Built-in Narrowing

```typescript
// typeof guard
function process(value: string | number): string {
    if (typeof value === "string") {
        return value.toUpperCase();  // TypeScript knows it's string
    }
    return value.toFixed(2);  // TypeScript knows it's number
}

// instanceof guard
function formatError(error: Error | string): string {
    if (error instanceof Error) {
        return error.message;
    }
    return error;
}

// in guard
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function move(animal: Fish | Bird): void {
    if ("swim" in animal) {
        animal.swim();
    } else {
        animal.fly();
    }
}

// Truthiness narrowing
function printValue(value: string | null | undefined): void {
    if (value) {
        console.log(value.length);  // string
    }
}
```

---

## ⚡ Custom Type Guards

```typescript
// User-defined type guard
interface User {
    type: "user";
    name: string;
    email: string;
}

interface Admin {
    type: "admin";
    name: string;
    permissions: string[];
}

type Account = User | Admin;

// Type predicate: paramName is Type
function isAdmin(account: Account): account is Admin {
    return account.type === "admin";
}

function getPermissions(account: Account): string[] {
    if (isAdmin(account)) {
        return account.permissions;  // TypeScript knows it's Admin
    }
    return [];
}

// Guard with assertion
function assertIsString(value: unknown): asserts value is string {
    if (typeof value !== "string") {
        throw new Error("Value must be a string");
    }
}

function processInput(value: unknown): void {
    assertIsString(value);
    console.log(value.toUpperCase());  // value is string after assertion
}
```

---

## 🔧 Discriminated Union Guards

```typescript
// Pattern: discriminant property
type Result<T> =
    | { status: "success"; data: T }
    | { status: "error"; error: string }
    | { status: "loading" };

function handleResult<T>(result: Result<T>): void {
    switch (result.status) {
        case "success":
            console.log("Data:", result.data);
            break;
        case "error":
            console.error("Error:", result.error);
            break;
        case "loading":
            console.log("Loading...");
            break;
    }
}

// Exhaustive checking
function assertNever(x: never): never {
    throw new Error(`Unexpected value: ${x}`);
}

function handleStatus(result: Result<User>): void {
    switch (result.status) {
        case "success": return;
        case "error": return;
        case "loading": return;
        default:
            assertNever(result);  // Error if case missing
    }
}
```

---

## 🏗️ Advanced Guards

```typescript
// Array type guards
function isStringArray(value: unknown): value is string[] {
    return Array.isArray(value) && value.every(item => typeof item === "string");
}

// Object validation guard
interface Config {
    host: string;
    port: number;
    ssl?: boolean;
}

function isConfig(value: unknown): value is Config {
    if (typeof value !== "object" || value === null) return false;

    const obj = value as Record<string, unknown>;

    return (
        typeof obj.host === "string" &&
        typeof obj.port === "number" &&
        (obj.ssl === undefined || typeof obj.ssl === "boolean")
    );
}

// Generic guard factory
function createGuard<T>(
    validate: (value: unknown) => boolean
): (value: unknown) => value is T {
    return (value): value is T => validate(value);
}

const isNumber = createGuard<number>(v => typeof v === "number");
```

---

## 🔥 Pro Tips

### 1. Narrow Early
```typescript
function process(data: unknown): void {
    if (!isValidData(data)) {
        throw new Error("Invalid data");
    }
    // data is now typed correctly
}
```

### 2. Use Branded Types with Guards
```typescript
type UserId = string & { __brand: "UserId" };

function isUserId(value: string): value is UserId {
    return /^usr_[a-z0-9]+$/.test(value);
}
```

---

## 🛠️ Hands-on Exercise

Create:
1. `isNonEmpty<T>()` array guard
2. `isApiResponse<T>()` with schema validation
3. Exhaustive status handler

---

## 📚 Resources

- [TypeScript: Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
""",
    "xp_reward": 225,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 14,
    "tags": ["typescript", "type-guards", "narrowing", "validation"],
}


# ============================================================================
# BLOCK 8: DECORATORS & CONFIG (Nodes 15-16)
# ============================================================================

TS_NODE_15_DECORATORS = {
    "id": "ts-15-decorators",
    "title": "Decorators",
    "description": "Metaprogramming with TypeScript decorators",
    "content": """
# Decorators

> *"Decorators add behavior without changing code. AOP for TypeScript."*

---

## 🎯 Why This Matters

Decorators enable:
- Cross-cutting concerns (logging, auth)
- Metadata attachment
- Framework integration (NestJS, Angular)
- Clean, declarative code

---

## 🧠 Core Concepts

### Enable Decorators

```json
// tsconfig.json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

### Class Decorators

```typescript
// Simple class decorator
function Logger(constructor: Function) {
    console.log(`Creating: ${constructor.name}`);
}

@Logger
class Service {
    constructor() {
        console.log("Service instantiated");
    }
}

// Decorator factory (with parameters)
function LoggerFactory(prefix: string) {
    return function(constructor: Function) {
        console.log(`${prefix}: ${constructor.name}`);
    };
}

@LoggerFactory("API")
class ApiService {}
```

### Method Decorators

```typescript
function Log(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    const original = descriptor.value;

    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey} with:`, args);
        const result = original.apply(this, args);
        console.log(`Result:`, result);
        return result;
    };

    return descriptor;
}

class Calculator {
    @Log
    add(a: number, b: number): number {
        return a + b;
    }
}

const calc = new Calculator();
calc.add(2, 3);
// Calling add with: [2, 3]
// Result: 5
```

---

## ⚡ Property Decorators

```typescript
function Required(target: any, propertyKey: string) {
    let value: any;

    const getter = () => value;
    const setter = (newValue: any) => {
        if (newValue === undefined || newValue === null) {
            throw new Error(`${propertyKey} is required`);
        }
        value = newValue;
    };

    Object.defineProperty(target, propertyKey, {
        get: getter,
        set: setter
    });
}

class Config {
    @Required
    apiKey!: string;
}
```

### Parameter Decorators

```typescript
function Validate(
    target: any,
    propertyKey: string,
    parameterIndex: number
) {
    const existingParams = Reflect.getMetadata("validate", target, propertyKey) || [];
    existingParams.push(parameterIndex);
    Reflect.defineMetadata("validate", existingParams, target, propertyKey);
}

class UserService {
    createUser(@Validate name: string) {
        // ...
    }
}
```

---

## 🔧 Practical Patterns

```typescript
// Timing decorator
function Timed(
    target: any,
    key: string,
    descriptor: PropertyDescriptor
) {
    const original = descriptor.value;

    descriptor.value = async function(...args: any[]) {
        const start = performance.now();
        const result = await original.apply(this, args);
        const end = performance.now();
        console.log(`${key} took ${(end - start).toFixed(2)}ms`);
        return result;
    };

    return descriptor;
}

// Retry decorator
function Retry(attempts: number = 3) {
    return function(
        target: any,
        key: string,
        descriptor: PropertyDescriptor
    ) {
        const original = descriptor.value;

        descriptor.value = async function(...args: any[]) {
            for (let i = 0; i < attempts; i++) {
                try {
                    return await original.apply(this, args);
                } catch (e) {
                    if (i === attempts - 1) throw e;
                    await new Promise(r => setTimeout(r, 1000 * (i + 1)));
                }
            }
        };

        return descriptor;
    };
}

class ApiClient {
    @Timed
    @Retry(3)
    async fetchData(url: string): Promise<any> {
        const response = await fetch(url);
        return response.json();
    }
}
```

---

## 🔥 Pro Tips

### 1. Decorator Order
```typescript
// Decorators execute bottom-up
@First   // Executes second
@Second  // Executes first
class MyClass {}
```

### 2. Use Reflect Metadata
```typescript
import "reflect-metadata";

function Type(type: string) {
    return Reflect.metadata("design:type", type);
}
```

---

## 🛠️ Hands-on Exercise

Create decorators:
1. `@Memoize` for caching
2. `@Deprecated(message)`
3. `@Auth(role)` access control

---

## 📚 Resources

- [TypeScript: Decorators](https://www.typescriptlang.org/docs/handbook/decorators.html)
""",
    "xp_reward": 225,
    "estimated_time": "55 minutes",
    "difficulty": "advanced",
    "order_index": 15,
    "tags": ["typescript", "decorators", "metaprogramming", "aop"],
}

TS_NODE_16_CONFIGURATION = {
    "id": "ts-16-configuration",
    "title": "TypeScript Configuration",
    "description": "Master tsconfig.json and compiler options",
    "content": """
# TypeScript Configuration

> *"tsconfig.json is your TypeScript control center."*

---

## 🎯 Why This Matters

Proper configuration:
- Ensures consistent behavior
- Enables/disables features
- Optimizes output
- Matches your target environment

---

## 🧠 tsconfig.json Structure

```json
{
  "compilerOptions": {
    // ... compiler settings
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"],
  "extends": "./tsconfig.base.json"
}
```

### Essential Options

```json
{
  "compilerOptions": {
    // Language & Environment
    "target": "ES2022",           // Output JS version
    "lib": ["ES2022", "DOM"],     // Available APIs
    "module": "NodeNext",         // Module system
    "moduleResolution": "NodeNext",

    // Strictness
    "strict": true,               // Enable all strict checks
    "noImplicitAny": true,        // Error on implicit any
    "strictNullChecks": true,     // Null/undefined checking
    "noUnusedLocals": true,       // Error on unused variables
    "noUnusedParameters": true,   // Error on unused params

    // Output
    "outDir": "./dist",           // Output directory
    "rootDir": "./src",           // Source root
    "declaration": true,          // Generate .d.ts files
    "sourceMap": true,            // Generate source maps

    // Interop
    "esModuleInterop": true,      // CommonJS/ES module interop
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,

    // Paths
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"],
      "@utils/*": ["utils/*"]
    }
  }
}
```

---

## ⚡ Common Configurations

### Node.js Backend

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Library Package

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "strict": true,
    "moduleResolution": "node"
  },
  "include": ["src"],
  "exclude": ["**/*.test.ts"]
}
```

---

## 🔧 Strict Mode Options

```json
{
  "compilerOptions": {
    // "strict": true enables all of these:
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "useUnknownInCatchVariables": true,
    "alwaysStrict": true
  }
}
```

---

## 🏗️ Project References

```json
// tsconfig.json (root)
{
  "files": [],
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/api" },
    { "path": "./packages/web" }
  ]
}

// packages/core/tsconfig.json
{
  "compilerOptions": {
    "composite": true,  // Required for references
    "outDir": "./dist"
  }
}

// packages/api/tsconfig.json
{
  "compilerOptions": {
    "composite": true
  },
  "references": [
    { "path": "../core" }
  ]
}
```

Build with: `tsc --build`

---

## 🔥 Pro Tips

### 1. Start Strict
```json
{ "compilerOptions": { "strict": true } }
```

### 2. Use extends
```json
{
  "extends": "@tsconfig/node20/tsconfig.json"
}
```

### 3. skipLibCheck for Speed
```json
{ "compilerOptions": { "skipLibCheck": true } }
```

---

## 🛠️ Hands-on Exercise

Create configs for:
1. Node.js API project
2. Shared library package
3. Monorepo with references

---

## 📚 Resources

- [TSConfig Reference](https://www.typescriptlang.org/tsconfig)
""",
    "xp_reward": 200,
    "estimated_time": "45 minutes",
    "difficulty": "intermediate",
    "order_index": 16,
    "tags": ["typescript", "tsconfig", "configuration", "compiler"],
}


# ============================================================================
# BLOCK 9: ERROR HANDLING & TESTING (Nodes 17-18)
# ============================================================================

TS_NODE_17_ERROR_HANDLING = {
    "id": "ts-17-error-handling",
    "title": "Type-Safe Error Handling",
    "description": "Handle errors with full type safety in TypeScript",
    "content": """
# Type-Safe Error Handling

> *"In TypeScript, errors become values you can reason about, not surprises at runtime."*

---

## 🎯 Why This Matters

DevOps reliability requires predictable error handling:
- **Caught errors are `unknown`** in strict mode
- **Custom errors carry context** for debugging
- **Result pattern** makes errors explicit in return types

---

## 💡 Core Concepts

### Problem: Unknown Catch Type

```typescript
try {
  await deployToK8s();
} catch (error) {
  // error is `unknown` in strict mode!
  // console.log(error.message); // ❌ Error
}
```

### Solution: Type Guards

```typescript
function isError(value: unknown): value is Error {
  return value instanceof Error;
}

try {
  await deployToK8s();
} catch (error) {
  if (isError(error)) {
    console.log(error.message); // ✅ Safe
    console.log(error.stack);
  } else {
    console.log('Unknown error:', String(error));
  }
}
```

---

## 🔧 Custom Error Classes

```typescript
class DevOpsError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean = false,
    public readonly context?: Record<string, unknown>
  ) {
    super(message);
    this.name = 'DevOpsError';
    Error.captureStackTrace(this, DevOpsError);
  }
}

class DeploymentError extends DevOpsError {
  constructor(
    message: string,
    public readonly environment: 'dev' | 'staging' | 'prod',
    public readonly service: string
  ) {
    super(message, 'DEPLOYMENT_FAILED', true, { environment, service });
  }
}

class ConfigurationError extends DevOpsError {
  constructor(
    message: string,
    public readonly configKey: string
  ) {
    super(message, 'CONFIG_ERROR', false, { configKey });
  }
}

// Usage with type narrowing
async function deploy(service: string, env: string) {
  try {
    await performDeployment(service, env);
  } catch (error) {
    if (error instanceof DeploymentError) {
      // Full access to typed properties
      console.log(`Failed: ${error.service} to ${error.environment}`);
      if (error.retryable) {
        await scheduleRetry(error.service);
      }
    } else if (error instanceof ConfigurationError) {
      console.log(`Bad config: ${error.configKey}`);
    } else if (error instanceof Error) {
      console.log(`Generic error: ${error.message}`);
    }
  }
}
```

---

## 🎯 Result Pattern

```typescript
// Make errors explicit in the type system
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

// Wrap async operations
async function safeAsync<T>(
  fn: () => Promise<T>
): Promise<Result<T>> {
  try {
    const data = await fn();
    return { success: true, data };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error
        ? error
        : new Error(String(error))
    };
  }
}

// Use with explicit handling
const result = await safeAsync(() => fetchPods('default'));

if (result.success) {
  // TypeScript knows data exists
  result.data.forEach(pod => console.log(pod.name));
} else {
  // TypeScript knows error exists
  console.error('Failed:', result.error.message);
}

// Chain Results
function map<T, U, E>(
  result: Result<T, E>,
  fn: (value: T) => U
): Result<U, E> {
  if (result.success) {
    return { success: true, data: fn(result.data) };
  }
  return result;
}

const podNames = map(result, pods =>
  pods.map(p => p.name)
);
```

---

## 🔥 Pro Tips

### 1. Assert Functions
```typescript
function assertDefined<T>(
  value: T | undefined,
  message: string
): asserts value is T {
  if (value === undefined) {
    throw new Error(message);
  }
}

const config = process.env.API_KEY;
assertDefined(config, 'API_KEY is required');
// config is string here, not string | undefined
```

### 2. Never Return Type
```typescript
function fail(message: string): never {
  throw new Error(message);
}

function getEnvOrFail(key: string): string {
  return process.env[key] ?? fail(`Missing ${key}`);
}
```

---

## 🛠️ Hands-on Exercise

Build a deployment service with:
1. Custom error hierarchy
2. Result pattern for all operations
3. Proper error context and retry logic

---

## 📚 Resources

- [TypeScript Error Handling](https://typescript.tv/errors/)
- [Result Pattern](https://github.com/badrap/result)
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "advanced",
    "order_index": 17,
    "tags": ["typescript", "errors", "result-pattern", "type-guards"],
}

TS_NODE_18_TESTING = {
    "id": "ts-18-testing",
    "title": "Testing TypeScript",
    "description": "Write type-safe tests with Jest and Vitest",
    "content": """
# Testing TypeScript

> *"Types catch bugs at compile time, tests catch bugs at runtime—use both."*

---

## 🎯 Why This Matters

TypeScript + testing = double safety net:
- **Type errors** caught before tests run
- **Runtime behavior** verified by tests
- **Mocks with full type safety**
- **Refactoring confidence**

---

## 💡 Jest Configuration

### jest.config.ts

```typescript
import type { Config } from 'jest';

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/*.test.ts', '**/*.spec.ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/index.ts',
  ],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
  setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
};

export default config;
```

### tsconfig for tests

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "types": ["jest", "node"]
  },
  "include": ["src/**/*.test.ts", "jest.setup.ts"]
}
```

---

## 🔧 Typed Test Utilities

```typescript
// src/test-utils/factories.ts
import { Pod, Container, Deployment } from '../types';

export function createMockPod(overrides?: Partial<Pod>): Pod {
  return {
    name: 'test-pod',
    namespace: 'default',
    status: 'Running',
    containers: [createMockContainer()],
    labels: {},
    annotations: {},
    createdAt: new Date(),
    ...overrides,
  };
}

export function createMockContainer(
  overrides?: Partial<Container>
): Container {
  return {
    name: 'main',
    image: 'nginx:latest',
    ready: true,
    restartCount: 0,
    ...overrides,
  };
}

export function createMockDeployment(
  overrides?: Partial<Deployment>
): Deployment {
  return {
    name: 'test-deployment',
    namespace: 'default',
    replicas: 3,
    availableReplicas: 3,
    ...overrides,
  };
}
```

---

## 🎯 Unit Tests

```typescript
// src/services/kubernetes.test.ts
import { KubernetesService } from './kubernetes';
import { createMockPod } from '../test-utils/factories';

describe('KubernetesService', () => {
  let service: KubernetesService;

  beforeEach(() => {
    service = new KubernetesService({
      context: 'test-cluster',
      namespace: 'default',
    });
  });

  describe('filterRunningPods', () => {
    it('should return only running pods', () => {
      const pods = [
        createMockPod({ status: 'Running' }),
        createMockPod({ status: 'Pending' }),
        createMockPod({ status: 'Running' }),
      ];

      const result = service.filterRunningPods(pods);

      expect(result).toHaveLength(2);
      expect(result.every(p => p.status === 'Running')).toBe(true);
    });

    it('should return empty array for no running pods', () => {
      const pods = [
        createMockPod({ status: 'Pending' }),
        createMockPod({ status: 'Failed' }),
      ];

      expect(service.filterRunningPods(pods)).toEqual([]);
    });
  });

  describe('getPodsByLabel', () => {
    it('should filter by label selector', () => {
      const pods = [
        createMockPod({ labels: { app: 'api' } }),
        createMockPod({ labels: { app: 'web' } }),
        createMockPod({ labels: { app: 'api', tier: 'backend' } }),
      ];

      const result = service.getPodsByLabel(pods, { app: 'api' });

      expect(result).toHaveLength(2);
    });
  });
});
```

---

## 🔧 Mocking with Types

```typescript
// Typed mocks with jest.mocked
import { ApiClient } from '../api-client';

jest.mock('../api-client');

const mockedClient = jest.mocked(ApiClient);

describe('DeploymentService', () => {
  beforeEach(() => {
    mockedClient.mockClear();
  });

  it('should fetch deployments', async () => {
    const mockDeployments = [
      createMockDeployment({ name: 'api' }),
      createMockDeployment({ name: 'web' }),
    ];

    mockedClient.prototype.getDeployments.mockResolvedValue(
      mockDeployments
    );

    const service = new DeploymentService(new ApiClient());
    const result = await service.listDeployments('default');

    expect(result).toEqual(mockDeployments);
    expect(mockedClient.prototype.getDeployments)
      .toHaveBeenCalledWith('default');
  });

  it('should handle API errors', async () => {
    mockedClient.prototype.getDeployments.mockRejectedValue(
      new Error('Network error')
    );

    const service = new DeploymentService(new ApiClient());

    await expect(service.listDeployments('default'))
      .rejects.toThrow('Network error');
  });
});
```

---

## 🎯 Integration Tests

```typescript
// src/integration/deploy.integration.test.ts
import { setupTestCluster, teardownTestCluster } from './helpers';

describe('Deployment Integration', () => {
  beforeAll(async () => {
    await setupTestCluster();
  });

  afterAll(async () => {
    await teardownTestCluster();
  });

  it('should deploy and verify', async () => {
    const deployment = await deployService({
      name: 'test-app',
      image: 'nginx:latest',
      replicas: 2,
    });

    expect(deployment.status).toBe('deployed');

    const pods = await listPods({ labelSelector: 'app=test-app' });
    expect(pods.length).toBeGreaterThanOrEqual(2);
  });
});
```

---

## 🔥 Pro Tips

### 1. Type-Safe Spies
```typescript
const spy = jest.spyOn(service, 'deploy');
// spy has full type inference
```

### 2. Custom Matchers
```typescript
expect.extend({
  toBeRunning(pod: Pod) {
    return {
      pass: pod.status === 'Running',
      message: () => `Expected pod to be running`,
    };
  },
});
```

---

## 🛠️ Hands-on Exercise

Create a test suite for a Kubernetes service:
1. Factory functions for all types
2. Unit tests with mocks
3. Custom matchers for assertions
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "advanced",
    "order_index": 18,
    "tags": ["typescript", "testing", "jest", "mocking"],
}


# ============================================================================
# BLOCK 10: DEVOPS INTEGRATION & CAPSTONE (Nodes 19-20)
# ============================================================================

TS_NODE_19_DEVOPS_INTEGRATION = {
    "id": "ts-19-devops-integration",
    "title": "TypeScript in DevOps Workflows",
    "description": "Integrate TypeScript into CI/CD and DevOps tooling",
    "content": """
# TypeScript in DevOps Workflows

> *"TypeScript transforms DevOps scripts from brittle hacks into reliable automation."*

---

## 🎯 Why This Matters

TypeScript excels in DevOps scenarios:
- **CLI tools** with type-safe arguments
- **CI/CD configs** generated with validation
- **Infrastructure code** with compile-time checks
- **API clients** for services and providers

---

## 💡 Building CLI Tools

### Using Commander

```typescript
// src/cli/index.ts
import { Command } from 'commander';
import { version } from '../../package.json';

interface DeployOptions {
  environment: 'dev' | 'staging' | 'prod';
  dryRun: boolean;
  force: boolean;
  timeout: number;
}

const program = new Command();

program
  .name('devops-cli')
  .description('Type-safe DevOps automation')
  .version(version);

program
  .command('deploy <service>')
  .description('Deploy a service')
  .option('-e, --environment <env>', 'Target environment', 'dev')
  .option('-d, --dry-run', 'Simulate deployment', false)
  .option('-f, --force', 'Skip confirmations', false)
  .option('-t, --timeout <seconds>', 'Timeout in seconds', '300')
  .action(async (service: string, opts: DeployOptions) => {
    console.log(`Deploying ${service} to ${opts.environment}...`);

    if (opts.dryRun) {
      console.log('DRY RUN - no changes will be made');
    }

    await runDeployment(service, {
      environment: opts.environment,
      dryRun: opts.dryRun,
      force: opts.force,
      timeout: parseInt(String(opts.timeout)),
    });
  });

program
  .command('status')
  .description('Check deployment status')
  .option('-n, --namespace <ns>', 'Kubernetes namespace', 'default')
  .action(async (opts) => {
    const status = await getClusterStatus(opts.namespace);
    console.table(status);
  });

program.parse();
```

---

## 🔧 GitHub Actions Generator

```typescript
// src/generators/github-actions.ts

interface WorkflowStep {
  name: string;
  uses?: string;
  run?: string;
  with?: Record<string, string>;
  env?: Record<string, string>;
  if?: string;
}

interface WorkflowJob {
  'runs-on': string;
  needs?: string[];
  if?: string;
  steps: WorkflowStep[];
  environment?: string;
}

interface Workflow {
  name: string;
  on: {
    push?: { branches: string[]; paths?: string[] };
    pull_request?: { branches: string[] };
    workflow_dispatch?: {};
  };
  env?: Record<string, string>;
  jobs: Record<string, WorkflowJob>;
}

function createCIWorkflow(config: {
  nodeVersion: string;
  testCommand: string;
  buildCommand: string;
  deployBranch: string;
}): Workflow {
  return {
    name: 'CI/CD Pipeline',
    on: {
      push: { branches: ['main', config.deployBranch] },
      pull_request: { branches: ['main'] },
    },
    env: {
      NODE_VERSION: config.nodeVersion,
    },
    jobs: {
      test: {
        'runs-on': 'ubuntu-latest',
        steps: [
          { name: 'Checkout', uses: 'actions/checkout@v4' },
          {
            name: 'Setup Node.js',
            uses: 'actions/setup-node@v4',
            with: { 'node-version': '${{ env.NODE_VERSION }}' },
          },
          { name: 'Install dependencies', run: 'npm ci' },
          { name: 'Run tests', run: config.testCommand },
          { name: 'Build', run: config.buildCommand },
        ],
      },
      deploy: {
        'runs-on': 'ubuntu-latest',
        needs: ['test'],
        if: `github.ref == 'refs/heads/${config.deployBranch}'`,
        environment: 'production',
        steps: [
          { name: 'Checkout', uses: 'actions/checkout@v4' },
          { name: 'Deploy', run: 'npm run deploy' },
        ],
      },
    },
  };
}

// Usage
const workflow = createCIWorkflow({
  nodeVersion: '20',
  testCommand: 'npm test',
  buildCommand: 'npm run build',
  deployBranch: 'main',
});

// Convert to YAML
import * as yaml from 'yaml';
console.log(yaml.stringify(workflow));
```

---

## 🎯 Config Validation

```typescript
// src/config/schema.ts
import { z } from 'zod';

const EnvironmentSchema = z.enum(['dev', 'staging', 'prod']);

const ServiceConfigSchema = z.object({
  name: z.string().min(1),
  image: z.string().regex(/^[\\w.-]+\\/[\\w.-]+:[\\w.-]+$/),
  replicas: z.number().int().min(1).max(100),
  resources: z.object({
    cpu: z.string().regex(/^\\d+m$/),
    memory: z.string().regex(/^\\d+Mi$/),
  }),
  env: z.record(z.string()).optional(),
});

const DeploymentConfigSchema = z.object({
  version: z.literal('1.0'),
  environment: EnvironmentSchema,
  services: z.array(ServiceConfigSchema),
});

type DeploymentConfig = z.infer<typeof DeploymentConfigSchema>;

// Validate config file
function loadConfig(path: string): DeploymentConfig {
  const raw = JSON.parse(fs.readFileSync(path, 'utf-8'));
  const result = DeploymentConfigSchema.safeParse(raw);

  if (!result.success) {
    console.error('Invalid config:');
    result.error.issues.forEach(issue => {
      console.error(`  ${issue.path.join('.')}: ${issue.message}`);
    });
    process.exit(1);
  }

  return result.data;
}
```

---

## 🔥 Pro Tips

### 1. Type-Safe ENV
```typescript
const EnvSchema = z.object({
  API_KEY: z.string(),
  DEBUG: z.coerce.boolean().default(false),
});

const env = EnvSchema.parse(process.env);
```

### 2. Generated Types
```bash
# Generate types from OpenAPI spec
npx openapi-typescript api-spec.yaml -o types/api.ts
```

---

## 🛠️ Hands-on Exercise

Build a CLI tool that:
1. Generates GitHub Actions workflows
2. Validates deployment configs
3. Has typed commands and options
""",
    "xp_reward": 250,
    "estimated_time": "60 minutes",
    "difficulty": "advanced",
    "order_index": 19,
    "tags": ["typescript", "devops", "cli", "automation"],
}

TS_NODE_20_CAPSTONE = {
    "id": "ts-20-capstone",
    "title": "TypeScript DevOps Capstone",
    "description": "Build a complete type-safe DevOps automation platform",
    "content": """
# TypeScript DevOps Capstone

> *"You've mastered the pieces—now build the whole system."*

---

## 🎯 Project Overview

Build a **DevOps Automation Platform** that combines all TypeScript concepts:

### Features
1. **Multi-cloud deployments** (K8s, AWS, GCP)
2. **Type-safe configurations**
3. **CLI interface**
4. **Result-based error handling**
5. **Full test coverage**

---

## 💡 Architecture

```typescript
// src/types/core.ts

// Provider abstraction
interface ProviderConfig {
  type: string;
}

interface KubernetesConfig extends ProviderConfig {
  type: 'kubernetes';
  context: string;
  namespace: string;
}

interface AWSConfig extends ProviderConfig {
  type: 'aws';
  region: string;
  profile?: string;
}

// Resource definitions
interface Resource {
  type: string;
  name: string;
  config: Record<string, unknown>;
}

// Deployment configuration
interface DeploymentConfig<T extends ProviderConfig = ProviderConfig> {
  name: string;
  version: string;
  environment: 'dev' | 'staging' | 'prod';
  provider: T;
  resources: Resource[];
  hooks?: DeploymentHooks;
}

interface DeploymentHooks {
  preDeploy?: (config: DeploymentConfig) => Promise<void>;
  postDeploy?: (config: DeploymentConfig, result: DeploymentResult) => Promise<void>;
  onError?: (config: DeploymentConfig, error: Error) => Promise<void>;
}

// Result types
interface DeploymentResult {
  success: boolean;
  deployedResources: string[];
  duration: number;
  outputs: Record<string, unknown>;
}
```

---

## 🔧 Deployment Engine

```typescript
// src/engine/deployer.ts
import { Result } from '../types/result';

abstract class BaseDeployer<T extends ProviderConfig> {
  constructor(protected config: DeploymentConfig<T>) {}

  async deploy(): Promise<Result<DeploymentResult>> {
    const startTime = Date.now();

    // Validate
    const validation = this.validate();
    if (!validation.success) {
      return validation;
    }

    // Pre-deploy hook
    await this.config.hooks?.preDeploy?.(this.config);

    try {
      // Execute deployment
      const result = await this.executeDeployment();

      // Post-deploy hook
      await this.config.hooks?.postDeploy?.(this.config, result);

      return {
        success: true,
        data: {
          ...result,
          duration: Date.now() - startTime,
        },
      };
    } catch (error) {
      const err = error instanceof Error ? error : new Error(String(error));
      await this.config.hooks?.onError?.(this.config, err);
      return { success: false, error: err };
    }
  }

  protected abstract validate(): Result<void>;
  protected abstract executeDeployment(): Promise<DeploymentResult>;
}

// Kubernetes implementation
class KubernetesDeployer extends BaseDeployer<KubernetesConfig> {
  protected validate(): Result<void> {
    if (!this.config.provider.context) {
      return {
        success: false,
        error: new Error('Kubernetes context is required'),
      };
    }
    return { success: true, data: undefined };
  }

  protected async executeDeployment(): Promise<DeploymentResult> {
    const deployed: string[] = [];

    for (const resource of this.config.resources) {
      await this.applyResource(resource);
      deployed.push(resource.name);
    }

    return {
      success: true,
      deployedResources: deployed,
      duration: 0,
      outputs: {
        namespace: this.config.provider.namespace,
      },
    };
  }

  private async applyResource(resource: Resource): Promise<void> {
    // kubectl apply logic
  }
}
```

---

## 🎯 CLI Interface

```typescript
// src/cli/commands/deploy.ts
import { Command } from 'commander';

export const deployCommand = new Command('deploy')
  .description('Deploy resources to a provider')
  .argument('<config>', 'Path to deployment config')
  .option('-e, --environment <env>', 'Override environment')
  .option('-d, --dry-run', 'Preview changes without applying')
  .option('--approve', 'Skip confirmation prompts')
  .action(async (configPath: string, options) => {
    // Load and validate config
    const config = loadConfig(configPath);

    // Override environment if specified
    if (options.environment) {
      config.environment = options.environment;
    }

    // Get appropriate deployer
    const deployer = createDeployer(config);

    // Execute
    if (options.dryRun) {
      console.log('Would deploy:', JSON.stringify(config, null, 2));
      return;
    }

    const result = await deployer.deploy();

    if (result.success) {
      console.log('✅ Deployment succeeded!');
      console.log(`Duration: ${result.data.duration}ms`);
      console.log('Resources:', result.data.deployedResources);
    } else {
      console.error('❌ Deployment failed:', result.error.message);
      process.exit(1);
    }
  });
```

---

## 🔧 Complete Test Suite

```typescript
// src/engine/__tests__/deployer.test.ts
import { KubernetesDeployer } from '../kubernetes-deployer';
import { createMockConfig } from '../../test-utils';

describe('KubernetesDeployer', () => {
  it('should validate config', async () => {
    const config = createMockConfig({
      provider: { type: 'kubernetes', context: '', namespace: 'default' },
    });

    const deployer = new KubernetesDeployer(config);
    const result = await deployer.deploy();

    expect(result.success).toBe(false);
    expect(result.error?.message).toContain('context is required');
  });

  it('should deploy resources in order', async () => {
    const config = createMockConfig({
      resources: [
        { type: 'configmap', name: 'config', config: {} },
        { type: 'deployment', name: 'api', config: {} },
        { type: 'service', name: 'api-svc', config: {} },
      ],
    });

    const deployer = new KubernetesDeployer(config);
    const result = await deployer.deploy();

    expect(result.success).toBe(true);
    expect(result.data?.deployedResources).toEqual([
      'config', 'api', 'api-svc'
    ]);
  });

  it('should call hooks', async () => {
    const preDeploy = jest.fn();
    const postDeploy = jest.fn();

    const config = createMockConfig({
      hooks: { preDeploy, postDeploy },
    });

    await new KubernetesDeployer(config).deploy();

    expect(preDeploy).toHaveBeenCalled();
    expect(postDeploy).toHaveBeenCalled();
  });
});
```

---

## 🚀 Final Project Requirements

Build a platform with:

### 1. Core Types (20%)
- Provider configs (K8s, AWS)
- Resource definitions
- Deployment configs
- Result types

### 2. Deployment Engine (30%)
- Base deployer class
- Provider implementations
- Hook system
- Error handling

### 3. CLI Tool (25%)
- deploy command
- status command
- validate command
- generate command

### 4. Tests (25%)
- Unit tests for all components
- Integration tests
- Factory functions

---

## 🎯 Success Criteria

✅ Full type safety - no `any`
✅ Result pattern for all async ops
✅ Custom error types
✅ 80%+ test coverage
✅ Working CLI

---

## 🏆 Congratulations!

You've mastered TypeScript for DevOps:
- Type-safe configurations
- Generic abstractions
- Error handling patterns
- Testing strategies
- CLI development

**You're ready to build production DevOps tools!**
""",
    "xp_reward": 300,
    "estimated_time": "90 minutes",
    "difficulty": "advanced",
    "order_index": 20,
    "tags": ["typescript", "capstone", "devops", "project"],
}


# ============================================================================
# SKILLSMAP DEFINITION (Complete - All 10 Blocks)
# ============================================================================

def get_typescript_skillsmap() -> dict[str, Any]:
    """Return the TypeScript SkillsMap definition."""
    return {
        "id": "typescript",
        "name": "TypeScript for DevOps",
        "slug": "typescript",
        "description": "Master type-safe JavaScript for robust DevOps tooling",
        "icon": "typescript",
        "color": "#3178C6",  # TypeScript blue
        "estimated_hours": 20,
        "difficulty": "intermediate",
        "prerequisites": ["javascript"],
        "tags": ["typescript", "javascript", "types", "devops"],
        "nodes": [
            # Block 1: Noder 1-2
            TS_NODE_01_INTRODUCTION,
            TS_NODE_02_TYPE_ANNOTATIONS,
            # Block 2: Noder 3-4
            TS_NODE_03_BASIC_TYPES,
            TS_NODE_04_TYPE_INFERENCE,
            # Block 3: Noder 5-6
            TS_NODE_05_INTERFACES,
            TS_NODE_06_TYPE_ALIASES,
            # Block 4: Noder 7-8
            TS_NODE_07_UNION_INTERSECTION,
            TS_NODE_08_FUNCTIONS,
            # Block 5: Noder 9-10
            TS_NODE_09_GENERICS,
            TS_NODE_10_UTILITY_TYPES,
            # Block 6: Noder 11-12
            TS_NODE_11_CLASSES,
            TS_NODE_12_MODULES,
            # Block 7: Noder 13-14
            TS_NODE_13_ADVANCED_TYPES,
            TS_NODE_14_TYPE_GUARDS,
            # Block 8: Noder 15-16
            TS_NODE_15_DECORATORS,
            TS_NODE_16_CONFIGURATION,
            # Block 9: Noder 17-18
            TS_NODE_17_ERROR_HANDLING,
            TS_NODE_18_TESTING,
            # Block 10: Noder 19-20
            TS_NODE_19_DEVOPS_INTEGRATION,
            TS_NODE_20_CAPSTONE,
        ],
    }


# Export for seeding
TYPESCRIPT_SKILLSMAP = get_typescript_skillsmap()
