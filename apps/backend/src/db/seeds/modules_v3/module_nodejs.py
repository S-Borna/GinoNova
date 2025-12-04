"""
Nodejs - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: advanced-specialty
Tasks: 20
Estimated Hours: 10.0
"""

MODULE_NODEJS = {
    "track_slug": "advanced-specialty",
    "order_index": 100,
    "name": "Nodejs",
    "slug": "nodejs",
    "description": """Master Nodejs from fundamentals to production""",
    "difficulty": "intermediate",
    "estimated_hours": 10.0,
    "prerequisites": [],
    "tasks": [
            {
                "title": "Introduction to Node.js",
                "difficulty": "easy",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""
# Introduction to Node.js

JavaScript på servern.

## Vad är Node.js?

```yaml
Definition:
  - JavaScript runtime byggd på V8
  - Server-side JavaScript
  - Event-driven, non-blocking I/O

Historia:
  - 2009: Ryan Dahl skapar Node.js
  - 2010: npm lanseras
  - 2015: io.js merge, Node.js Foundation
  - 2019: OpenJS Foundation
```

## Varför Node.js?

```yaml
Fördelar:
  - Ett språk (JS) frontend + backend
  - Hög concurrency (event loop)
  - Stort ekosystem (npm)
  - Snabb utveckling
  - JSON native
  - Real-time applikationer

Use Cases:
  - REST APIs
  - Real-time apps (chat, gaming)
  - Streaming
  - Microservices
  - CLI tools
  - Build tools
```

## Node.js vs Browser

```javascript
// Browser-only
window, document, DOM, localStorage

// Node.js-only
process, fs, http, path, os, crypto

// Båda har
console, setTimeout, JSON, fetch (Node 18+)

// Global object
// Browser: window
// Node.js: global (eller globalThis)
```

## Installation

```bash
# macOS med Homebrew
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Windows - ladda ner från nodejs.org

# Version manager (rekommenderat)
# nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 20
nvm use 20

# Verifiera
node --version
npm --version
```

## Hello World

```javascript
// hello.js
console.log('Hello, Node.js!');

// Kör
// $ node hello.js
```

## REPL (Read-Eval-Print Loop)

```bash
$ node
> console.log('Hello')
Hello
undefined
> 2 + 2
4
> const name = 'Node'
undefined
> `Hello ${name}`
'Hello Node'
> .exit
```

## Process Object

```javascript
// process - global objekt i Node.js

// Aktuell Node version
console.log(process.version);
// v20.10.0

// Miljövariabler
console.log(process.env.NODE_ENV);
// development

// Aktuell working directory
console.log(process.cwd());
// /Users/dev/myapp

// Kommandoradsargument
console.log(process.argv);
// ['node', 'app.js', '--port', '3000']

// Exit programmet
process.exit(0);  // Success
process.exit(1);  // Error
```

## Node.js Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Node.js Application                   │
├─────────────────────────────────────────────────────────┤
│                     Node.js APIs                         │
│         (http, fs, path, crypto, events, etc.)          │
├─────────────────────────────────────────────────────────┤
│                    Node.js Bindings                      │
├──────────────────────────┬──────────────────────────────┤
│           V8             │           libuv              │
│    (JavaScript Engine)   │    (Async I/O, Event Loop)   │
└──────────────────────────┴──────────────────────────────┘
```

| Komponent | Funktion |
|-----------|----------|
| V8 | Kompilerar JS till maskinkod |
| libuv | Event loop, async I/O |
| Node APIs | Inbyggda moduler |
| npm | Pakethanterare |

**Nästa steg:** Node 2 - Modules

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Modules: CommonJS & ESM",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 125,
                "content": r"""
# Modules: CommonJS & ESM

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


Organisera kod i återanvändbara moduler.

## CommonJS (CJS)

```javascript
// math.js - Exportera
function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

module.exports = { add, multiply };

// Alternativt
exports.add = add;
exports.multiply = multiply;

// app.js - Importera
const math = require('./math');
console.log(math.add(2, 3));  // 5

// Destructuring
const { add, multiply } = require('./math');
console.log(add(2, 3));  // 5
```

## ES Modules (ESM)

```javascript
// math.mjs (eller .js med "type": "module" i package.json)
export function add(a, b) {
  return a + b;
}

export function multiply(a, b) {
  return a * b;
}

// Default export
export default class Calculator {
  // ...
}

// app.mjs - Importera
import { add, multiply } from './math.mjs';
import Calculator from './math.mjs';

// Importera allt
import * as math from './math.mjs';
math.add(2, 3);
```

## Aktivera ESM

```json
// package.json - för hela projektet
{
  "name": "my-app",
  "type": "module"
}
```

```javascript
// Eller använd .mjs extension
// file.mjs = ESM
// file.cjs = CommonJS
```

## CJS vs ESM

```yaml
CommonJS:
  Syntax: require() / module.exports
  Loading: Synchronous
  When: Runtime
  Default i: Node.js (legacy)

ESM:
  Syntax: import / export
  Loading: Asynchronous
  When: Compile time (statisk)
  Default i: Browser, modern Node

Rekommendation:
  - Nya projekt: ESM
  - Legacy: CJS
```

## Inbyggda Moduler

```javascript
// Importera inbyggda moduler
const fs = require('fs');           // CJS
import fs from 'fs';                 // ESM
import fs from 'node:fs';            // Explicit (rekommenderat)

// Vanliga inbyggda moduler
import fs from 'node:fs';            // Filsystem
import path from 'node:path';        // Sökvägar
import http from 'node:http';        // HTTP server/client
import https from 'node:https';      // HTTPS
import crypto from 'node:crypto';    // Kryptering
import os from 'node:os';            // Operativsystem
import events from 'node:events';    // Event emitter
import url from 'node:url';          // URL parsing
import util from 'node:util';        // Utilities
```

## __dirname och __filename

```javascript
// CommonJS - direkt tillgängliga
console.log(__dirname);   // /Users/dev/myapp
console.log(__filename);  // /Users/dev/myapp/app.js

// ESM - kräver workaround
import { fileURLToPath } from 'node:url';
import { dirname } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Eller med import.meta
console.log(import.meta.url);
// file:///Users/dev/myapp/app.js
```

## Dynamic Import

```javascript
// Dynamisk import (fungerar i både CJS och ESM)
async function loadModule() {
  const module = await import('./dynamic-module.js');
  module.doSomething();
}

// Villkorlig import
if (process.env.NODE_ENV === 'development') {
  const devTools = await import('./dev-tools.js');
}
```

## Module Resolution

```javascript
// Node.js letar i ordning:
// 1. Core modules (fs, path, etc.)
// 2. node_modules i current directory
// 3. node_modules i parent directories
// 4. Global node_modules

require('fs');           // Core module
require('express');      // node_modules/express
require('./utils');      // Relativ sökväg
require('/abs/path');    // Absolut sökväg
```

| Format | Extension | Import | Export |
|--------|-----------|--------|--------|
| CommonJS | .js/.cjs | require() | module.exports |
| ESM | .mjs/.js | import | export |

**Nästa steg:** Node 3 - npm

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "npm & Package Management",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# npm & Package Management

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


Node Package Manager.

## npm Basics

```bash
# Initiera projekt
npm init              # Interaktivt
npm init -y           # Med defaults

# Installera paket
npm install express           # Lokalt (dependencies)
npm install -D jest           # DevDependencies
npm install -g nodemon        # Globalt

# Kortform
npm i express
npm i -D jest
npm i -g nodemon

# Ta bort paket
npm uninstall express
npm un express

# Uppdatera
npm update                    # Alla paket
npm update express            # Specifikt paket
```

## package.json

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My awesome app",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "build": "tsc",
    "lint": "eslint ."
  },
  "keywords": ["nodejs", "api"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^8.0.0"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "nodemon": "^3.0.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

## Semantic Versioning

```yaml
Format: MAJOR.MINOR.PATCH
Exempel: 4.18.2

MAJOR: Breaking changes (4.x.x → 5.0.0)
MINOR: New features, backward compatible (4.18.x → 4.19.0)
PATCH: Bug fixes (4.18.2 → 4.18.3)

Ranges i package.json:
  "^4.18.2": 4.18.2 - 4.x.x (MINOR + PATCH)
  "~4.18.2": 4.18.2 - 4.18.x (Endast PATCH)
  "4.18.2": Exakt version
  ">=4.18.2": 4.18.2 eller högre
  "*": Senaste version (farligt!)
```

## npm Scripts

```json
{
  "scripts": {
    "start": "node dist/index.js",
    "dev": "nodemon --watch src src/index.ts",
    "test": "jest --coverage",
    "test:watch": "jest --watch",
    "lint": "eslint src/**/*.ts",
    "lint:fix": "eslint src/**/*.ts --fix",
    "build": "tsc",
    "prebuild": "npm run lint",
    "postbuild": "echo 'Build complete!'",
    "docker:build": "docker build -t myapp .",
    "docker:run": "docker run -p 3000:3000 myapp"
  }
}
```

```bash
# Köra scripts
npm run dev
npm run test
npm start          # "start" behöver inte "run"
npm test           # "test" behöver inte "run"

# Med argument
npm run test -- --watch
```

## package-lock.json

```yaml
Syfte:
  - Låser exakta versioner
  - Reproducerbara builds
  - Snabbare installation

Viktigt:
  - Committa till git
  - Genereras automatiskt
  - Uppdateras vid npm install
```

## npm vs Alternativ

```yaml
npm:
  - Standard med Node.js
  - Störst registry

yarn:
  - Snabbare (parallel downloads)
  - Workspaces
  - yarn add, yarn remove

pnpm:
  - Effektivt disk usage
  - Symlinks till global store
  - pnpm add, pnpm remove
```

## Workspaces (Monorepo)

```json
// package.json (root)
{
  "name": "my-monorepo",
  "workspaces": [
    "packages/*"
  ]
}

// Struktur
// my-monorepo/
// ├── package.json
// ├── packages/
// │   ├── api/
// │   │   └── package.json
// │   ├── web/
// │   │   └── package.json
// │   └── shared/
// │       └── package.json
```

```bash
# Installera dependencies för alla workspaces
npm install

# Köra script i specifik workspace
npm run test -w packages/api

# Köra i alla workspaces
npm run test --workspaces
```

## npx

```bash
# Köra paket utan global installation
npx create-react-app my-app
npx typescript --init
npx jest

# Köra specifik version
npx node@18 app.js

# Köra lokal binary
npx eslint .
```

| Kommando | Beskrivning |
|----------|-------------|
| npm init | Skapa package.json |
| npm install | Installera dependencies |
| npm run | Köra script |
| npm publish | Publicera paket |
| npx | Köra paket |

**Nästa steg:** Node 4 - Error Handling

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Error Handling",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Error Handling

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


Hantera fel korrekt i Node.js.

## Error Types

```javascript
// JavaScript Errors
new Error('Something went wrong');
new TypeError('Expected string');
new RangeError('Out of range');
new SyntaxError('Invalid syntax');
new ReferenceError('Variable not defined');

// Node.js System Errors
// ENOENT: File not found
// ECONNREFUSED: Connection refused
// EPERM: Permission denied
// EADDRINUSE: Port in use
```

## Try-Catch

```javascript
// Synchronous errors
try {
  const data = JSON.parse(invalidJson);
} catch (error) {
  console.error('Parse error:', error.message);
} finally {
  // Körs alltid
  cleanup();
}

// Error properties
try {
  throw new Error('Something failed');
} catch (error) {
  console.log(error.name);     // 'Error'
  console.log(error.message);  // 'Something failed'
  console.log(error.stack);    // Stack trace
}
```

## Custom Errors

```javascript
// Custom Error class
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
    this.statusCode = 400;
  }
}

class NotFoundError extends Error {
  constructor(resource) {
    super(`${resource} not found`);
    this.name = 'NotFoundError';
    this.statusCode = 404;
  }
}

// Användning
function validateUser(user) {
  if (!user.email) {
    throw new ValidationError('Email required', 'email');
  }
}

try {
  validateUser({});
} catch (error) {
  if (error instanceof ValidationError) {
    console.log(`Validation failed: ${error.field}`);
  }
}
```

## Async Error Handling

```javascript
// Callbacks (error-first pattern)
fs.readFile('file.txt', (error, data) => {
  if (error) {
    console.error('Failed to read:', error.message);
    return;
  }
  console.log(data.toString());
});

// Promises
readFileAsync('file.txt')
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error.message));

// Async/await
async function readFile() {
  try {
    const data = await readFileAsync('file.txt');
    return data;
  } catch (error) {
    console.error('Error:', error.message);
    throw error;  // Re-throw om needed
  }
}
```

## Uncaught Exceptions

```javascript
// Fånga uncaught exceptions (sista utväg)
process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
  // Logga, cleanup, sedan exit
  process.exit(1);
});

// Unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
  // Node 15+ kastar som exception
});

// OBS: Dessa är sista utväg!
// Applikationen är i undefined state
// Best practice: graceful shutdown
```

## Graceful Shutdown

```javascript
let server;

// Starta server
server = app.listen(3000);

// Graceful shutdown
function shutdown() {
  console.log('Shutting down gracefully...');

  server.close(() => {
    console.log('HTTP server closed');

    // Stäng database connections
    mongoose.connection.close(false, () => {
      console.log('MongoDB closed');
      process.exit(0);
    });
  });

  // Force close efter timeout
  setTimeout(() => {
    console.error('Forced shutdown');
    process.exit(1);
  }, 10000);
}

process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
```

## Error Handling Middleware (Express)

```javascript
// Error handling middleware
app.use((error, req, res, next) => {
  console.error(error.stack);

  // Custom errors
  if (error instanceof ValidationError) {
    return res.status(400).json({
      error: 'Validation Error',
      message: error.message,
      field: error.field
    });
  }

  if (error instanceof NotFoundError) {
    return res.status(404).json({
      error: 'Not Found',
      message: error.message
    });
  }

  // Default error
  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'production'
      ? 'Something went wrong'
      : error.message
  });
});

// Async wrapper
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) throw new NotFoundError('User');
  res.json(user);
}));
```

| Error Type | Hantering |
|------------|-----------|
| Sync | try-catch |
| Callback | error-first pattern |
| Promise | .catch() |
| Async/await | try-catch |
| Uncaught | process.on('uncaughtException') |

**Nästa steg:** Node 5 - Event Loop

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Event Loop",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 160,
                "content": r"""
# Event Loop

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


Hjärtat av Node.js async-modell.

## Vad är Event Loop?

```yaml
Definition:
  - Hanterar async operations
  - Single-threaded men non-blocking
  - Köar callbacks för exekvering

Varför viktigt:
  - Hög concurrency
  - Effektiv I/O
  - Responsiv applikation
```

## Event Loop Phases

```
   ┌───────────────────────────┐
┌─►│           timers          │ (setTimeout, setInterval)
│  └─────────────┬─────────────┘
│  ┌─────────────▼─────────────┐
│  │     pending callbacks     │ (I/O callbacks)
│  └─────────────┬─────────────┘
│  ┌─────────────▼─────────────┐
│  │       idle, prepare       │ (internal)
│  └─────────────┬─────────────┘
│  ┌─────────────▼─────────────┐
│  │           poll            │ (I/O, network)
│  └─────────────┬─────────────┘
│  ┌─────────────▼─────────────┐
│  │           check           │ (setImmediate)
│  └─────────────┬─────────────┘
│  ┌─────────────▼─────────────┐
│  │      close callbacks      │ (socket.on('close'))
│  └─────────────┬─────────────┘
└──────────────◄─┘
```

## Exekveringsordning

```javascript
console.log('1: Script start');

setTimeout(() => {
  console.log('2: setTimeout');
}, 0);

setImmediate(() => {
  console.log('3: setImmediate');
});

Promise.resolve().then(() => {
  console.log('4: Promise');
});

process.nextTick(() => {
  console.log('5: nextTick');
});

console.log('6: Script end');

// Output:
// 1: Script start
// 6: Script end
// 5: nextTick       (microtask queue)
// 4: Promise        (microtask queue)
// 2: setTimeout     (timers phase) *
// 3: setImmediate   (check phase) *
// * ordning kan variera
```

## Microtasks vs Macrotasks

```javascript
// Microtasks (körs först)
process.nextTick(() => console.log('nextTick'));
Promise.resolve().then(() => console.log('Promise'));
queueMicrotask(() => console.log('queueMicrotask'));

// Macrotasks (körs i faser)
setTimeout(() => console.log('setTimeout'));
setInterval(() => console.log('setInterval'));
setImmediate(() => console.log('setImmediate'));
// I/O callbacks

// Prioritet:
// 1. nextTick (högst)
// 2. Microtasks (Promises)
// 3. Macrotasks (timers, I/O)
```

## process.nextTick

```javascript
// Körs direkt efter current operation
// Innan event loop fortsätter

function asyncOperation(callback) {
  // Garantera async
  process.nextTick(() => {
    callback(null, 'result');
  });
}

// Användning
asyncOperation((err, result) => {
  console.log(result);
});
console.log('After call');  // Loggas först!

// OBS: För många nextTick kan blockera I/O
// Använd setImmediate för CPU-intensivt
```

## setImmediate vs setTimeout

```javascript
// setImmediate: check phase
// setTimeout(..., 0): timers phase

// I main script: ordning odefinierad
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
// Kan vara antingen ordning

// I I/O callback: setImmediate alltid först
const fs = require('fs');

fs.readFile('file.txt', () => {
  setTimeout(() => console.log('timeout'), 0);
  setImmediate(() => console.log('immediate'));
  // Alltid: immediate först, sedan timeout
});
```

## Blocking Event Loop

```javascript
// DÅLIGT: Blockerar event loop
app.get('/compute', (req, res) => {
  const result = heavyComputation();  // Blockerar!
  res.json({ result });
});

// BÄTTRE: Dela upp arbetet
function computeInChunks(data, callback) {
  const chunks = splitIntoChunks(data);
  let index = 0;

  function processNext() {
    if (index < chunks.length) {
      processChunk(chunks[index]);
      index++;
      setImmediate(processNext);  // Yield till event loop
    } else {
      callback();
    }
  }

  processNext();
}

// BÄST: Worker threads för CPU-intensivt
const { Worker } = require('worker_threads');
```

## Monitoring Event Loop

```javascript
// Mät event loop lag
let lastCheck = Date.now();

setInterval(() => {
  const now = Date.now();
  const lag = now - lastCheck - 1000;

  if (lag > 100) {
    console.warn(`Event loop lag: ${lag}ms`);
  }

  lastCheck = now;
}, 1000);

// Eller använd paket
const blocked = require('blocked-at');

blocked((time, stack) => {
  console.log(`Blocked for ${time}ms`);
  console.log(stack);
});
```

| Funktion | Queue | När |
|----------|-------|-----|
| process.nextTick | Microtask | Direkt |
| Promise.then | Microtask | Direkt |
| setTimeout | Timers | Timers phase |
| setImmediate | Check | Check phase |
| I/O callbacks | Poll | Poll phase |

**Nästa steg:** Node 6 - Async/Await

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Promises & Async/Await",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Promises & Async/Await

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


Modern asynkron programmering.

## Callbacks (Legacy)

```javascript
// Callback hell
fs.readFile('file1.txt', (err, data1) => {
  if (err) return handleError(err);

  fs.readFile('file2.txt', (err, data2) => {
    if (err) return handleError(err);

    fs.writeFile('output.txt', data1 + data2, (err) => {
      if (err) return handleError(err);
      console.log('Done!');
    });
  });
});
```

## Promises

```javascript
// Skapa Promise
function readFileAsync(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

// Använd Promise
readFileAsync('file.txt')
  .then(data => console.log(data.toString()))
  .catch(err => console.error(err))
  .finally(() => console.log('Cleanup'));

// Chaining
readFileAsync('file1.txt')
  .then(data1 => {
    return readFileAsync('file2.txt')
      .then(data2 => data1 + data2);
  })
  .then(combined => console.log(combined))
  .catch(err => console.error(err));
```

## Promise Utilities

```javascript
// Promise.all - alla måste lyckas
const results = await Promise.all([
  fetchUser(1),
  fetchUser(2),
  fetchUser(3)
]);
// [user1, user2, user3]

// Promise.allSettled - alla, oavsett resultat
const results = await Promise.allSettled([
  fetchUser(1),
  fetchUser(999)  // Finns ej
]);
// [
//   { status: 'fulfilled', value: user1 },
//   { status: 'rejected', reason: Error }
// ]

// Promise.race - första som blir klar
const result = await Promise.race([
  fetch(primaryUrl),
  fetch(backupUrl)
]);

// Promise.any - första som lyckas
const result = await Promise.any([
  fetch(url1),
  fetch(url2)  // Om url1 failar
]);
```

## Async/Await

```javascript
// Async function returnerar alltid Promise
async function fetchData() {
  return 'data';  // Wrappas i Promise
}

// Await pausar exekvering
async function processFiles() {
  try {
    const data1 = await readFileAsync('file1.txt');
    const data2 = await readFileAsync('file2.txt');

    await writeFileAsync('output.txt', data1 + data2);
    console.log('Done!');
  } catch (error) {
    console.error('Error:', error);
  }
}

// Parallel execution
async function parallel() {
  const [user, posts, comments] = await Promise.all([
    fetchUser(1),
    fetchPosts(1),
    fetchComments(1)
  ]);

  return { user, posts, comments };
}
```

## Common Patterns

```javascript
// Sequential (en åt gången)
async function sequential(ids) {
  const results = [];
  for (const id of ids) {
    const result = await fetchItem(id);
    results.push(result);
  }
  return results;
}

// Parallel (alla samtidigt)
async function parallel(ids) {
  const promises = ids.map(id => fetchItem(id));
  return await Promise.all(promises);
}

// Controlled concurrency
async function withConcurrency(ids, limit = 5) {
  const results = [];
  const chunks = chunk(ids, limit);

  for (const batch of chunks) {
    const batchResults = await Promise.all(
      batch.map(id => fetchItem(id))
    );
    results.push(...batchResults);
  }

  return results;
}

// Med p-limit
import pLimit from 'p-limit';

const limit = pLimit(5);

const results = await Promise.all(
  ids.map(id => limit(() => fetchItem(id)))
);
```

## Error Handling

```javascript
// Try-catch med async/await
async function handleErrors() {
  try {
    const result = await riskyOperation();
    return result;
  } catch (error) {
    console.error('Failed:', error);
    throw error;  // Re-throw
  }
}

// Per-promise error handling
async function multipleOperations() {
  const results = await Promise.allSettled([
    operation1(),
    operation2(),
    operation3()
  ]);

  const successes = results
    .filter(r => r.status === 'fulfilled')
    .map(r => r.value);

  const failures = results
    .filter(r => r.status === 'rejected')
    .map(r => r.reason);

  return { successes, failures };
}

// Retry pattern
async function withRetry(fn, retries = 3, delay = 1000) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(r => setTimeout(r, delay * (i + 1)));
    }
  }
}
```

## Promisify

```javascript
import { promisify } from 'node:util';
import fs from 'node:fs';

// Konvertera callback till Promise
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

// Användning
const data = await readFile('file.txt');

// Eller använd fs/promises
import { readFile, writeFile } from 'node:fs/promises';

const data = await readFile('file.txt');
```

| Pattern | Use Case |
|---------|----------|
| Sequential | Dependent operations |
| Promise.all | Independent, all required |
| Promise.allSettled | Independent, partial OK |
| Promise.race | First response wins |
| Promise.any | First success wins |

**Nästa steg:** Node 7 - Event Emitter

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Event Emitter",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Event Emitter

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


Event-driven arkitektur i Node.js.

## Basics

```javascript
import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// Lyssna på event
emitter.on('message', (data) => {
  console.log('Received:', data);
});

// Emit event
emitter.emit('message', 'Hello World');
// Output: Received: Hello World

// Flera argument
emitter.on('user', (name, age) => {
  console.log(`${name} is ${age} years old`);
});

emitter.emit('user', 'Alice', 30);
```

## Event Methods

```javascript
const emitter = new EventEmitter();

// on() - Lyssna (alias: addListener)
emitter.on('event', handler);

// once() - Lyssna en gång
emitter.once('connect', () => {
  console.log('Connected!');
});

// off() - Sluta lyssna (alias: removeListener)
emitter.off('event', handler);

// removeAllListeners()
emitter.removeAllListeners('event');
emitter.removeAllListeners();  // Alla events

// Antal lyssnare
emitter.listenerCount('event');

// Lista lyssnare
emitter.listeners('event');
```

## Custom Event Emitter

```javascript
import { EventEmitter } from 'node:events';

class Database extends EventEmitter {
  constructor() {
    super();
    this.connected = false;
  }

  async connect() {
    // Simulate connection
    await new Promise(r => setTimeout(r, 1000));
    this.connected = true;
    this.emit('connected');
  }

  async query(sql) {
    if (!this.connected) {
      throw new Error('Not connected');
    }

    this.emit('query', sql);
    const result = await this.executeQuery(sql);
    this.emit('result', result);

    return result;
  }

  disconnect() {
    this.connected = false;
    this.emit('disconnected');
  }
}

// Användning
const db = new Database();

db.on('connected', () => console.log('DB connected!'));
db.on('query', (sql) => console.log('Executing:', sql));
db.on('disconnected', () => console.log('DB disconnected'));

await db.connect();
await db.query('SELECT * FROM users');
db.disconnect();
```

## Error Events

```javascript
const emitter = new EventEmitter();

// Om ingen lyssnare: kraschar processen
emitter.emit('error', new Error('Something failed'));

// Lägg alltid till error handler
emitter.on('error', (error) => {
  console.error('Error occurred:', error.message);
});

emitter.emit('error', new Error('Something failed'));
// Hanteras nu säkert
```

## Async Events

```javascript
import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// Async listener
emitter.on('process', async (data) => {
  await processData(data);
  console.log('Processing complete');
});

// Await inte automatiskt!
emitter.emit('process', myData);
console.log('After emit');  // Loggas direkt

// För att vänta på async listeners
import { once } from 'node:events';

const emitter = new EventEmitter();

// Vänta på specifikt event
setTimeout(() => emitter.emit('ready', 'data'), 1000);

const [data] = await once(emitter, 'ready');
console.log('Received:', data);
```

## Event Emitter i Streams

```javascript
import { createReadStream } from 'node:fs';

const stream = createReadStream('largefile.txt');

stream.on('data', (chunk) => {
  console.log('Chunk:', chunk.length);
});

stream.on('end', () => {
  console.log('File read complete');
});

stream.on('error', (err) => {
  console.error('Error:', err);
});

// HTTP Server events
import { createServer } from 'node:http';

const server = createServer();

server.on('request', (req, res) => {
  res.end('Hello World');
});

server.on('listening', () => {
  console.log('Server started');
});

server.on('error', (err) => {
  console.error('Server error:', err);
});

server.listen(3000);
```

## Best Practices

```javascript
// Sätt max listeners (default: 10)
emitter.setMaxListeners(20);

// Warning vid för många
// (MaxListenersExceededWarning)

// Rensa listeners för att undvika memory leaks
class MyClass extends EventEmitter {
  constructor() {
    super();
    this.handler = this.handleEvent.bind(this);
    this.on('event', this.handler);
  }

  handleEvent(data) {
    console.log('Event:', data);
  }

  cleanup() {
    this.off('event', this.handler);
    this.removeAllListeners();
  }
}

// prepend listener (körs först)
emitter.prependListener('event', handler);
emitter.prependOnceListener('event', handler);
```

| Method | Beskrivning |
|--------|-------------|
| on() | Lägg till listener |
| once() | Lyssna en gång |
| emit() | Trigga event |
| off() | Ta bort listener |
| removeAllListeners() | Ta bort alla |

**Nästa steg:** Node 8 - Streams

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Streams & Buffers",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 160,
                "content": r"""
# Streams & Buffers

Effektiv hantering av stora datamängder.

## Varför Streams?

```javascript
// DÅLIGT: Läser hela filen i minnet
import { readFile } from 'node:fs/promises';

const data = await readFile('huge-file.csv');
// 2GB fil = 2GB RAM!

// BRA: Streaming
import { createReadStream } from 'node:fs';

const stream = createReadStream('huge-file.csv');
stream.on('data', (chunk) => {
  processChunk(chunk);  // 64KB chunks
});
```

## Stream Types

```yaml
Readable:
  - Läsa data
  - fs.createReadStream
  - http request

Writable:
  - Skriva data
  - fs.createWriteStream
  - http response

Duplex:
  - Läsa och skriva
  - TCP socket
  - WebSocket

Transform:
  - Modifiera data
  - zlib (compression)
  - crypto
```

## Readable Streams

```javascript
import { createReadStream } from 'node:fs';
import { Readable } from 'node:stream';

// Fil stream
const fileStream = createReadStream('file.txt', {
  encoding: 'utf8',
  highWaterMark: 64 * 1024  // Chunk size (64KB)
});

fileStream.on('data', (chunk) => {
  console.log('Chunk:', chunk.length);
});

fileStream.on('end', () => {
  console.log('Done reading');
});

// Custom Readable
class CounterStream extends Readable {
  constructor(max) {
    super();
    this.max = max;
    this.current = 0;
  }

  _read() {
    if (this.current <= this.max) {
      this.push(String(this.current++) + '\n');
    } else {
      this.push(null);  // Signalera slut
    }
  }
}

const counter = new CounterStream(100);
counter.pipe(process.stdout);
```

## Writable Streams

```javascript
import { createWriteStream } from 'node:fs';
import { Writable } from 'node:stream';

// Fil stream
const writeStream = createWriteStream('output.txt');

writeStream.write('Hello\n');
writeStream.write('World\n');
writeStream.end('Goodbye\n');

writeStream.on('finish', () => {
  console.log('Write complete');
});

// Custom Writable
class LoggerStream extends Writable {
  _write(chunk, encoding, callback) {
    const line = chunk.toString();
    console.log(`[LOG] ${new Date().toISOString()}: ${line}`);
    callback();  // Signalera klar
  }
}

const logger = new LoggerStream();
logger.write('Message 1');
logger.write('Message 2');
```

## Piping

```javascript
import { createReadStream, createWriteStream } from 'node:fs';
import { createGzip, createGunzip } from 'node:zlib';
import { pipeline } from 'node:stream/promises';

// Enkel pipe
createReadStream('input.txt')
  .pipe(createWriteStream('output.txt'));

// Pipeline (rekommenderat)
await pipeline(
  createReadStream('input.txt'),
  createGzip(),
  createWriteStream('output.txt.gz')
);

// Decompress
await pipeline(
  createReadStream('output.txt.gz'),
  createGunzip(),
  createWriteStream('output.txt')
);

// HTTP streaming
import http from 'node:http';

http.createServer((req, res) => {
  if (req.url === '/video') {
    const videoStream = createReadStream('video.mp4');
    res.writeHead(200, { 'Content-Type': 'video/mp4' });
    videoStream.pipe(res);
  }
}).listen(3000);
```

## Transform Streams

```javascript
import { Transform } from 'node:stream';
import { pipeline } from 'node:stream/promises';

// Custom transform
class UpperCaseTransform extends Transform {
  _transform(chunk, encoding, callback) {
    this.push(chunk.toString().toUpperCase());
    callback();
  }
}

await pipeline(
  createReadStream('input.txt'),
  new UpperCaseTransform(),
  createWriteStream('output.txt')
);

// CSV parser example
class CSVParser extends Transform {
  constructor() {
    super({ objectMode: true });  // Output objects
    this.headers = null;
  }

  _transform(chunk, encoding, callback) {
    const lines = chunk.toString().split('\n');

    for (const line of lines) {
      if (!line.trim()) continue;

      const values = line.split(',');

      if (!this.headers) {
        this.headers = values;
      } else {
        const obj = {};
        this.headers.forEach((h, i) => obj[h] = values[i]);
        this.push(obj);
      }
    }

    callback();
  }
}
```

## Buffers

```javascript
// Buffer = raw binary data

// Skapa buffer
const buf1 = Buffer.from('Hello');
const buf2 = Buffer.alloc(10);  // 10 bytes, fyllt med 0
const buf3 = Buffer.allocUnsafe(10);  // Snabbare, ej nollställd

// Konvertera
const str = buf1.toString('utf8');
const hex = buf1.toString('hex');
const base64 = buf1.toString('base64');

// Från olika format
const fromHex = Buffer.from('48656c6c6f', 'hex');
const fromBase64 = Buffer.from('SGVsbG8=', 'base64');

// Buffer operations
const combined = Buffer.concat([buf1, buf2]);
const slice = buf1.subarray(0, 3);
const copied = Buffer.alloc(5);
buf1.copy(copied);
```

| Stream Type | Metod | Use Case |
|-------------|-------|----------|
| Readable | pipe() | Läsa filer, HTTP req |
| Writable | write() | Skriva filer, HTTP res |
| Transform | pipe() | Kompression, parsing |
| Duplex | pipe() | Sockets |

**Nästa steg:** Node 9 - HTTP Server

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "HTTP Server",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# HTTP Server

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


Skapa web servers med Node.js.

## Basic HTTP Server

```javascript
import http from 'node:http';

const server = http.createServer((req, res) => {
  // Request info
  console.log(req.method);   // GET, POST, etc.
  console.log(req.url);      // /users
  console.log(req.headers);  // { host: '...', ... }

  // Response
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

## Request Handling

```javascript
const server = http.createServer((req, res) => {
  const { method, url } = req;

  // Routing
  if (method === 'GET' && url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>Home Page</h1>');
  }
  else if (method === 'GET' && url === '/api/users') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify([{ id: 1, name: 'Alice' }]));
  }
  else if (method === 'POST' && url === '/api/users') {
    let body = '';

    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', () => {
      const user = JSON.parse(body);
      res.writeHead(201, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ id: 2, ...user }));
    });
  }
  else {
    res.writeHead(404);
    res.end('Not Found');
  }
});
```

## URL Parsing

```javascript
import { URL } from 'node:url';

const server = http.createServer((req, res) => {
  // Parse URL
  const url = new URL(req.url, `http://${req.headers.host}`);

  console.log(url.pathname);    // /users
  console.log(url.searchParams.get('id'));  // ?id=123

  // Path parameters (manuellt)
  const match = url.pathname.match(/^\/users\/(\d+)$/);
  if (match) {
    const userId = match[1];
    res.end(`User ID: ${userId}`);
  }
});
```

## HTTPS Server

```javascript
import https from 'node:https';
import fs from 'node:fs';

const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

const server = https.createServer(options, (req, res) => {
  res.writeHead(200);
  res.end('Secure Hello World');
});

server.listen(443, () => {
  console.log('HTTPS Server running');
});
```

## HTTP Client

```javascript
// Native fetch (Node 18+)
const response = await fetch('https://api.example.com/users');
const users = await response.json();

// POST request
const response = await fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'Alice' })
});

// http module (low-level)
import http from 'node:http';

http.get('http://api.example.com/users', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => console.log(JSON.parse(data)));
});
```

## Keep-Alive & Connection Pooling

```javascript
import http from 'node:http';

// Custom agent med connection pooling
const agent = new http.Agent({
  keepAlive: true,
  maxSockets: 10,
  maxFreeSockets: 5
});

const options = {
  hostname: 'api.example.com',
  port: 80,
  path: '/users',
  agent: agent
};

http.get(options, (res) => {
  // Handle response
});
```

## Server Events

```javascript
const server = http.createServer();

server.on('request', (req, res) => {
  res.end('Hello');
});

server.on('connection', (socket) => {
  console.log('New connection');
});

server.on('close', () => {
  console.log('Server closed');
});

server.on('error', (err) => {
  console.error('Server error:', err);
});

server.listen(3000);

// Graceful shutdown
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Server closed gracefully');
    process.exit(0);
  });
});
```

| Metod | HTTP Status |
|-------|-------------|
| res.statusCode | Sätt status |
| res.setHeader() | Lägg till header |
| res.writeHead() | Status + headers |
| res.write() | Skriv body |
| res.end() | Avsluta response |

**Nästa steg:** Node 10 - Express.js

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Express.js Framework",
                "difficulty": "hard",
                "estimated_minutes": 60,
                "xp_reward": 170,
                "content": r"""
# Express.js Framework

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


Det populäraste Node.js web framework.

## Setup

```bash
npm init -y
npm install express
```

```javascript
import express from 'express';

const app = express();

// Middleware för JSON parsing
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## Routing

```javascript
// HTTP methods
app.get('/users', getUsers);
app.post('/users', createUser);
app.put('/users/:id', updateUser);
app.patch('/users/:id', patchUser);
app.delete('/users/:id', deleteUser);

// Route parameters
app.get('/users/:id', (req, res) => {
  const { id } = req.params;
  res.json({ id });
});

// Query parameters
app.get('/search', (req, res) => {
  const { q, page, limit } = req.query;
  // /search?q=node&page=1&limit=10
  res.json({ q, page, limit });
});

// Multiple parameters
app.get('/users/:userId/posts/:postId', (req, res) => {
  const { userId, postId } = req.params;
  res.json({ userId, postId });
});
```

## Router

```javascript
// routes/users.js
import { Router } from 'express';

const router = Router();

router.get('/', (req, res) => {
  res.json([{ id: 1, name: 'Alice' }]);
});

router.get('/:id', (req, res) => {
  res.json({ id: req.params.id });
});

router.post('/', (req, res) => {
  const user = req.body;
  res.status(201).json(user);
});

export default router;

// app.js
import userRoutes from './routes/users.js';

app.use('/api/users', userRoutes);
// GET /api/users
// GET /api/users/123
// POST /api/users
```

## Middleware

```javascript
// Application-level middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

// Route-specific middleware
const authenticate = (req, res, next) => {
  const token = req.headers.authorization;
  if (!token) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  req.user = verifyToken(token);
  next();
};

app.get('/protected', authenticate, (req, res) => {
  res.json({ user: req.user });
});

// Multiple middleware
app.post('/users',
  authenticate,
  validateBody,
  createUser
);

// Built-in middleware
app.use(express.json());        // Parse JSON body
app.use(express.urlencoded({ extended: true }));  // Parse form data
app.use(express.static('public'));  // Serve static files
```

## Error Handling

```javascript
// Custom error class
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
  }
}

// Async wrapper
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// Route med async
app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) {
    throw new AppError('User not found', 404);
  }
  res.json(user);
}));

// Error handling middleware (sist!)
app.use((err, req, res, next) => {
  const statusCode = err.statusCode || 500;

  res.status(statusCode).json({
    error: err.message,
    stack: process.env.NODE_ENV === 'development' ? err.stack : undefined
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});
```

## Request & Response

```javascript
// Request object
app.post('/users', (req, res) => {
  req.body;          // Parsed body
  req.params;        // Route parameters
  req.query;         // Query string
  req.headers;       // Headers
  req.cookies;       // Cookies (med cookie-parser)
  req.ip;            // Client IP
  req.method;        // HTTP method
  req.path;          // URL path
});

// Response object
app.get('/users', (req, res) => {
  res.status(200);              // Set status
  res.json({ data: [] });       // Send JSON
  res.send('Text');             // Send text/html
  res.sendFile('/path/file');   // Send file
  res.redirect('/other');       // Redirect
  res.cookie('name', 'value');  // Set cookie
  res.set('Header', 'value');   // Set header

  // Chaining
  res.status(201).json({ created: true });
});
```

## Popular Middleware

```javascript
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import compression from 'compression';

// CORS
app.use(cors({
  origin: 'http://localhost:3000',
  credentials: true
}));

// Security headers
app.use(helmet());

// Logging
app.use(morgan('dev'));

// Compression
app.use(compression());
```

| Middleware | Syfte |
|------------|-------|
| express.json() | Parse JSON body |
| cors | Cross-origin requests |
| helmet | Security headers |
| morgan | Request logging |
| compression | Gzip responses |

**Nästa steg:** Node 11 - REST API Design

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "REST API Design",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# REST API Design

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


Bygg professionella APIs.

## REST Principles

```yaml
Resources:
  - Noun-based URLs
  - /users, /posts, /comments

HTTP Methods:
  GET: Läs
  POST: Skapa
  PUT: Ersätt
  PATCH: Uppdatera delvis
  DELETE: Ta bort

Stateless:
  - Ingen server-side session
  - Varje request är komplett
```

## API Structure

```javascript
// routes/api/v1/users.js
import { Router } from 'express';

const router = Router();

// GET /api/v1/users
router.get('/', async (req, res) => {
  const { page = 1, limit = 10, sort = 'createdAt' } = req.query;

  const users = await User.find()
    .sort(sort)
    .skip((page - 1) * limit)
    .limit(Number(limit));

  const total = await User.countDocuments();

  res.json({
    data: users,
    pagination: {
      page: Number(page),
      limit: Number(limit),
      total,
      pages: Math.ceil(total / limit)
    }
  });
});

// GET /api/v1/users/:id
router.get('/:id', async (req, res) => {
  const user = await User.findById(req.params.id);

  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.json({ data: user });
});

// POST /api/v1/users
router.post('/', async (req, res) => {
  const user = await User.create(req.body);
  res.status(201).json({ data: user });
});

// PUT /api/v1/users/:id
router.put('/:id', async (req, res) => {
  const user = await User.findByIdAndUpdate(
    req.params.id,
    req.body,
    { new: true, runValidators: true }
  );

  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.json({ data: user });
});

// DELETE /api/v1/users/:id
router.delete('/:id', async (req, res) => {
  const user = await User.findByIdAndDelete(req.params.id);

  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  res.status(204).send();
});

export default router;
```

## Validation

```javascript
import { body, param, query, validationResult } from 'express-validator';

// Validation middleware
const validate = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
  next();
};

// Route med validering
router.post('/',
  [
    body('email').isEmail().normalizeEmail(),
    body('password').isLength({ min: 8 }),
    body('name').trim().notEmpty()
  ],
  validate,
  createUser
);

router.get('/:id',
  [param('id').isMongoId()],
  validate,
  getUser
);

// Eller med Zod
import { z } from 'zod';

const userSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  name: z.string().min(1)
});

const validateZod = (schema) => (req, res, next) => {
  try {
    req.body = schema.parse(req.body);
    next();
  } catch (error) {
    res.status(400).json({ errors: error.errors });
  }
};

router.post('/', validateZod(userSchema), createUser);
```

## Response Format

```javascript
// Konsistent response format
const sendSuccess = (res, data, statusCode = 200) => {
  res.status(statusCode).json({
    success: true,
    data
  });
};

const sendError = (res, message, statusCode = 500) => {
  res.status(statusCode).json({
    success: false,
    error: message
  });
};

// Pagination helper
const paginate = (data, page, limit, total) => ({
  data,
  pagination: {
    page,
    limit,
    total,
    pages: Math.ceil(total / limit),
    hasNext: page * limit < total,
    hasPrev: page > 1
  }
});
```

## Authentication

```javascript
import jwt from 'jsonwebtoken';

// Login
router.post('/auth/login', async (req, res) => {
  const { email, password } = req.body;

  const user = await User.findOne({ email });
  if (!user || !await user.comparePassword(password)) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const token = jwt.sign(
    { id: user._id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );

  res.json({ token });
});

// Auth middleware
const auth = async (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = await User.findById(decoded.id);
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};

// Protected route
router.get('/me', auth, (req, res) => {
  res.json({ data: req.user });
});
```

## API Versioning

```javascript
// URL versioning
app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);

// Header versioning
const versionMiddleware = (req, res, next) => {
  const version = req.headers['api-version'] || 'v1';
  req.apiVersion = version;
  next();
};
```

| Status Code | Användning |
|-------------|------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Server Error |

**Nästa steg:** Node 12 - Database Integration

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Database Integration",
                "difficulty": "hard",
                "estimated_minutes": 60,
                "xp_reward": 170,
                "content": r"""
# Database Integration

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


Anslut Node.js till databaser.

## MongoDB med Mongoose

```javascript
import mongoose from 'mongoose';

// Anslut
await mongoose.connect(process.env.MONGODB_URI);

console.log('MongoDB connected');

// Schema definition
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  password: {
    type: String,
    required: true,
    minlength: 8,
    select: false  // Exkludera från queries
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user'
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Middleware
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 12);
  next();
});

// Methods
userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

// Static methods
userSchema.statics.findByEmail = function(email) {
  return this.findOne({ email });
};

const User = mongoose.model('User', userSchema);
```

## Mongoose CRUD

```javascript
// Create
const user = await User.create({
  name: 'Alice',
  email: 'alice@example.com',
  password: 'password123'
});

// Read
const users = await User.find();
const user = await User.findById(id);
const user = await User.findOne({ email: 'alice@example.com' });

// With population
const user = await User.findById(id).populate('posts');

// Update
const user = await User.findByIdAndUpdate(
  id,
  { name: 'Alice Updated' },
  { new: true, runValidators: true }
);

// Delete
await User.findByIdAndDelete(id);

// Queries
const users = await User.find({ role: 'admin' })
  .select('name email')
  .sort('-createdAt')
  .limit(10)
  .skip(0);
```

## PostgreSQL med Prisma

```bash
npm install prisma @prisma/client
npx prisma init
```

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  password  String
  posts     Post[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User     @relation(fields: [authorId], references: [id])
  authorId  Int
}
```

```bash
npx prisma migrate dev --name init
npx prisma generate
```

```javascript
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

// Create
const user = await prisma.user.create({
  data: {
    email: 'alice@example.com',
    name: 'Alice',
    password: hashedPassword
  }
});

// Read
const users = await prisma.user.findMany();
const user = await prisma.user.findUnique({
  where: { email: 'alice@example.com' },
  include: { posts: true }
});

// Update
const user = await prisma.user.update({
  where: { id: 1 },
  data: { name: 'Alice Updated' }
});

// Delete
await prisma.user.delete({ where: { id: 1 } });

// Transaction
const [user, post] = await prisma.$transaction([
  prisma.user.create({ data: { ... } }),
  prisma.post.create({ data: { ... } })
]);
```

## Redis

```javascript
import { createClient } from 'redis';

const redis = createClient({
  url: process.env.REDIS_URL
});

await redis.connect();

// String operations
await redis.set('key', 'value');
await redis.set('key', 'value', { EX: 3600 });  // TTL 1h
const value = await redis.get('key');

// Hash
await redis.hSet('user:1', { name: 'Alice', email: 'alice@example.com' });
const user = await redis.hGetAll('user:1');

// List
await redis.lPush('queue', 'item1');
const item = await redis.rPop('queue');

// Set
await redis.sAdd('tags', 'nodejs', 'express');
const tags = await redis.sMembers('tags');

// Caching pattern
async function getCachedUser(id) {
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);

  const user = await User.findById(id);
  await redis.set(`user:${id}`, JSON.stringify(user), { EX: 3600 });
  return user;
}
```

## Connection Pooling

```javascript
// Mongoose (built-in)
await mongoose.connect(uri, {
  maxPoolSize: 10,
  minPoolSize: 2
});

// PostgreSQL (pg)
import pg from 'pg';

const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL,
  max: 20,
  idleTimeoutMillis: 30000
});

const result = await pool.query('SELECT * FROM users WHERE id = $1', [id]);
```

| Database | ORM/Driver | Best For |
|----------|-----------|----------|
| MongoDB | Mongoose | Flexible schema |
| PostgreSQL | Prisma, pg | Relational data |
| Redis | redis | Caching, sessions |
| MySQL | mysql2, Prisma | Relational data |

**Nästa steg:** Node 13 - Authentication & Security

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Authentication & Security",
                "difficulty": "hard",
                "estimated_minutes": 65,
                "xp_reward": 180,
                "content": r"""
# Authentication & Security

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


Säker autentisering i Node.js.

## JWT Authentication

```javascript
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

// Registrering
export async function register(req, res) {
  const { email, password, name } = req.body;

  // Kolla om användare finns
  const existing = await User.findOne({ email });
  if (existing) {
    return res.status(400).json({ error: 'Email already registered' });
  }

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 12);

  // Skapa användare
  const user = await User.create({
    email,
    password: hashedPassword,
    name
  });

  // Generera token
  const token = generateToken(user);

  res.status(201).json({ token, user: { id: user.id, email, name } });
}

// Login
export async function login(req, res) {
  const { email, password } = req.body;

  // Hitta användare
  const user = await User.findOne({ email }).select('+password');
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Verifiera password
  const isValid = await bcrypt.compare(password, user.password);
  if (!isValid) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const token = generateToken(user);
  res.json({ token });
}

// Token generation
function generateToken(user) {
  return jwt.sign(
    { id: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );
}

// Token verification middleware
export function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({ error: 'Token expired' });
    }
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

## Refresh Tokens

```javascript
// Token pair strategy
export async function login(req, res) {
  const user = await validateCredentials(req.body);

  const accessToken = jwt.sign(
    { id: user.id },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  const refreshToken = jwt.sign(
    { id: user.id },
    process.env.REFRESH_SECRET,
    { expiresIn: '7d' }
  );

  // Spara refresh token
  await redis.set(`refresh:${user.id}`, refreshToken, { EX: 7 * 24 * 3600 });

  res.json({ accessToken, refreshToken });
}

// Refresh endpoint
export async function refresh(req, res) {
  const { refreshToken } = req.body;

  try {
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);

    // Verifiera att token fortfarande är giltig
    const storedToken = await redis.get(`refresh:${decoded.id}`);
    if (storedToken !== refreshToken) {
      return res.status(401).json({ error: 'Invalid refresh token' });
    }

    // Generera ny access token
    const accessToken = jwt.sign(
      { id: decoded.id },
      process.env.JWT_SECRET,
      { expiresIn: '15m' }
    );

    res.json({ accessToken });
  } catch (error) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
}
```

## OAuth 2.0 / Passport

```javascript
import passport from 'passport';
import { Strategy as GoogleStrategy } from 'passport-google-oauth20';

passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: '/auth/google/callback'
}, async (accessToken, refreshToken, profile, done) => {
  try {
    // Hitta eller skapa användare
    let user = await User.findOne({ googleId: profile.id });

    if (!user) {
      user = await User.create({
        googleId: profile.id,
        email: profile.emails[0].value,
        name: profile.displayName
      });
    }

    done(null, user);
  } catch (error) {
    done(error);
  }
}));

// Routes
app.get('/auth/google',
  passport.authenticate('google', { scope: ['profile', 'email'] })
);

app.get('/auth/google/callback',
  passport.authenticate('google', { session: false }),
  (req, res) => {
    const token = generateToken(req.user);
    res.redirect(`/app?token=${token}`);
  }
);
```

## Security Best Practices

```javascript
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import mongoSanitize from 'express-mongo-sanitize';
import xss from 'xss-clean';
import hpp from 'hpp';

// Security headers
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 min
  max: 100,
  message: 'Too many requests'
});
app.use('/api', limiter);

// Stricter limit för auth
const authLimiter = rateLimit({
  windowMs: 60 * 60 * 1000,  // 1h
  max: 5,
  skipSuccessfulRequests: true
});
app.use('/auth/login', authLimiter);

// NoSQL injection protection
app.use(mongoSanitize());

// XSS protection
app.use(xss());

// HTTP Parameter Pollution
app.use(hpp());

// CORS
import cors from 'cors';
app.use(cors({
  origin: process.env.FRONTEND_URL,
  credentials: true
}));
```

## Password Security

```javascript
import bcrypt from 'bcrypt';
import zxcvbn from 'zxcvbn';

// Password strength check
function checkPasswordStrength(password) {
  const result = zxcvbn(password);

  if (result.score < 3) {
    throw new Error('Password too weak: ' + result.feedback.warning);
  }

  return true;
}

// Argon2 (modernare alternativ)
import argon2 from 'argon2';

const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 2 ** 16,
  timeCost: 3,
  parallelism: 1
});

const isValid = await argon2.verify(hash, password);
```

## RBAC (Role-Based Access Control)

```javascript
// Roles & permissions
const permissions = {
  admin: ['read', 'write', 'delete', 'manage'],
  editor: ['read', 'write'],
  viewer: ['read']
};

// Middleware
export function authorize(...requiredPermissions) {
  return (req, res, next) => {
    const userPermissions = permissions[req.user.role] || [];

    const hasPermission = requiredPermissions.every(
      perm => userPermissions.includes(perm)
    );

    if (!hasPermission) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }

    next();
  };
}

// Användning
app.delete('/users/:id',
  authenticate,
  authorize('delete', 'manage'),
  deleteUser
);
```

| Koncept | Implementering |
|---------|----------------|
| Password hashing | bcrypt/argon2 |
| Tokens | JWT |
| Sessions | express-session + Redis |
| OAuth | Passport.js |
| Rate limiting | express-rate-limit |

**Nästa steg:** Node 14 - File Handling

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "File Handling",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# File Handling

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


Läs, skriv och hantera filer i Node.js.

## File System Module

```javascript
import fs from 'node:fs/promises';
import path from 'node:path';

// Läs fil
const content = await fs.readFile('file.txt', 'utf-8');
console.log(content);

// Skriv fil
await fs.writeFile('output.txt', 'Hello World');

// Append
await fs.appendFile('log.txt', 'New line\n');

// Kolla om fil finns
try {
  await fs.access('file.txt');
  console.log('File exists');
} catch {
  console.log('File does not exist');
}

// File stats
const stats = await fs.stat('file.txt');
console.log(stats.size);        // bytes
console.log(stats.isFile());    // true/false
console.log(stats.isDirectory());
console.log(stats.mtime);       // modified time
```

## Directory Operations

```javascript
// Lista filer
const files = await fs.readdir('./src');
console.log(files);

// Med file types
const entries = await fs.readdir('./src', { withFileTypes: true });
for (const entry of entries) {
  if (entry.isDirectory()) {
    console.log(`Dir: ${entry.name}`);
  } else {
    console.log(`File: ${entry.name}`);
  }
}

// Skapa directory
await fs.mkdir('new-dir', { recursive: true });

// Ta bort directory
await fs.rm('old-dir', { recursive: true, force: true });

// Kopiera
await fs.cp('src', 'backup', { recursive: true });

// Rename/Move
await fs.rename('old.txt', 'new.txt');
```

## Streams

```javascript
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';
import { createGzip, createGunzip } from 'node:zlib';

// Läsa stora filer
const stream = createReadStream('large-file.txt', {
  encoding: 'utf-8',
  highWaterMark: 64 * 1024  // 64KB chunks
});

stream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes`);
});

stream.on('end', () => {
  console.log('Finished reading');
});

// Kopiera med streams
const source = createReadStream('input.txt');
const dest = createWriteStream('output.txt');

await pipeline(source, dest);

// Komprimera fil
await pipeline(
  createReadStream('input.txt'),
  createGzip(),
  createWriteStream('input.txt.gz')
);

// Dekomprimera
await pipeline(
  createReadStream('input.txt.gz'),
  createGunzip(),
  createWriteStream('output.txt')
);
```

## File Upload (Multer)

```javascript
import multer from 'multer';
import path from 'node:path';

// Disk storage
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    const uniqueName = `${Date.now()}-${Math.random().toString(36).slice(2)}`;
    cb(null, uniqueName + path.extname(file.originalname));
  }
});

// File filter
const fileFilter = (req, file, cb) => {
  const allowed = ['image/jpeg', 'image/png', 'image/gif'];
  if (allowed.includes(file.mimetype)) {
    cb(null, true);
  } else {
    cb(new Error('Invalid file type'), false);
  }
};

const upload = multer({
  storage,
  fileFilter,
  limits: {
    fileSize: 5 * 1024 * 1024  // 5MB
  }
});

// Routes
app.post('/upload', upload.single('file'), (req, res) => {
  res.json({
    filename: req.file.filename,
    path: req.file.path
  });
});

app.post('/upload-multiple', upload.array('files', 5), (req, res) => {
  res.json({ files: req.files.map(f => f.filename) });
});
```

## Cloud Storage (S3)

```javascript
import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const s3 = new S3Client({
  region: process.env.AWS_REGION,
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
  }
});

// Upload
async function uploadToS3(file) {
  const key = `uploads/${Date.now()}-${file.originalname}`;

  await s3.send(new PutObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key,
    Body: file.buffer,
    ContentType: file.mimetype
  }));

  return key;
}

// Signed URL för nedladdning
async function getDownloadUrl(key) {
  const command = new GetObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key
  });

  return await getSignedUrl(s3, command, { expiresIn: 3600 });
}

// Med multer memory storage
const upload = multer({ storage: multer.memoryStorage() });

app.post('/upload', upload.single('file'), async (req, res) => {
  const key = await uploadToS3(req.file);
  res.json({ key });
});
```

## Path Module

```javascript
import path from 'node:path';

// Paths
path.join('src', 'lib', 'utils.js');  // src/lib/utils.js
path.resolve('src', 'lib');            // /absolute/path/src/lib

// Parse path
const parsed = path.parse('/home/user/file.txt');
// { root: '/', dir: '/home/user', base: 'file.txt', ext: '.txt', name: 'file' }

// Extrahera delar
path.dirname('/home/user/file.txt');   // /home/user
path.basename('/home/user/file.txt');  // file.txt
path.extname('/home/user/file.txt');   // .txt

// Normalize
path.normalize('/foo/bar//baz/');      // /foo/bar/baz
```

| Metod | Sync | Async (Promises) |
|-------|------|------------------|
| Läsa | readFileSync | readFile |
| Skriva | writeFileSync | writeFile |
| Kopiera | copyFileSync | copyFile |
| Stats | statSync | stat |

**Nästa steg:** Node 15 - WebSockets

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "WebSockets",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 160,
                "content": r"""
# WebSockets

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


Real-time kommunikation med WebSockets.

## Native WebSocket (ws)

```javascript
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('Client connected');

  // Skicka meddelande till client
  ws.send(JSON.stringify({ type: 'welcome', message: 'Hello!' }));

  // Ta emot meddelanden
  ws.on('message', (data) => {
    const message = JSON.parse(data.toString());
    console.log('Received:', message);

    // Echo back
    ws.send(JSON.stringify({ type: 'echo', data: message }));
  });

  ws.on('close', () => {
    console.log('Client disconnected');
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
});

// Broadcast till alla clients
function broadcast(data) {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
}
```

## Integration med Express

```javascript
import express from 'express';
import { createServer } from 'node:http';
import { WebSocketServer } from 'ws';

const app = express();
const server = createServer(app);
const wss = new WebSocketServer({ server });

// REST endpoints
app.get('/api/status', (req, res) => {
  res.json({ clients: wss.clients.size });
});

// WebSocket handling
wss.on('connection', (ws) => {
  ws.isAlive = true;

  ws.on('pong', () => {
    ws.isAlive = true;
  });

  ws.on('message', (data) => {
    // Handle message
  });
});

// Heartbeat för att detektera döda connections
const interval = setInterval(() => {
  wss.clients.forEach((ws) => {
    if (!ws.isAlive) return ws.terminate();
    ws.isAlive = false;
    ws.ping();
  });
}, 30000);

wss.on('close', () => {
  clearInterval(interval);
});

server.listen(3000);
```

## Socket.IO

```javascript
import express from 'express';
import { createServer } from 'node:http';
import { Server } from 'socket.io';

const app = express();
const server = createServer(app);
const io = new Server(server, {
  cors: {
    origin: process.env.FRONTEND_URL,
    credentials: true
  }
});

// Middleware
io.use((socket, next) => {
  const token = socket.handshake.auth.token;
  try {
    const user = verifyToken(token);
    socket.user = user;
    next();
  } catch {
    next(new Error('Authentication error'));
  }
});

io.on('connection', (socket) => {
  console.log(`User connected: ${socket.user.id}`);

  // Join room
  socket.join(`user:${socket.user.id}`);

  // Event handlers
  socket.on('message', (data) => {
    console.log('Message:', data);

    // Broadcast to all except sender
    socket.broadcast.emit('message', {
      user: socket.user.name,
      text: data.text
    });
  });

  socket.on('join-room', (roomId) => {
    socket.join(roomId);
    io.to(roomId).emit('user-joined', socket.user.name);
  });

  socket.on('disconnect', () => {
    console.log(`User disconnected: ${socket.user.id}`);
  });
});

// Emit from anywhere
function notifyUser(userId, event, data) {
  io.to(`user:${userId}`).emit(event, data);
}

server.listen(3000);
```

## Socket.IO Client

```javascript
import { io } from 'socket.io-client';

const socket = io('http://localhost:3000', {
  auth: {
    token: localStorage.getItem('token')
  }
});

socket.on('connect', () => {
  console.log('Connected to server');
});

socket.on('message', (data) => {
  console.log('Received:', data);
});

// Emit with acknowledgment
socket.emit('message', { text: 'Hello' }, (response) => {
  console.log('Server acknowledged:', response);
});

// Reconnection
socket.on('connect_error', (error) => {
  console.error('Connection error:', error);
});

socket.on('disconnect', (reason) => {
  console.log('Disconnected:', reason);
});
```

## Rooms & Namespaces

```javascript
// Namespaces
const chatNs = io.of('/chat');
const notificationsNs = io.of('/notifications');

chatNs.on('connection', (socket) => {
  // Chat-specific logic
});

// Rooms
io.on('connection', (socket) => {
  // Join
  socket.join('room-123');

  // Send to room
  io.to('room-123').emit('message', 'Hello room!');

  // Leave
  socket.leave('room-123');

  // Get rooms
  console.log(socket.rooms);  // Set { socket.id, 'room-123' }
});

// Broadcast patterns
io.emit('event', data);                    // All clients
socket.broadcast.emit('event', data);       // All except sender
io.to('room').emit('event', data);          // Specific room
socket.to('room').emit('event', data);      // Room except sender
```

## Real-time Chat Example

```javascript
// Server
const users = new Map();

io.on('connection', (socket) => {
  const { username } = socket.handshake.query;
  users.set(socket.id, username);

  io.emit('users', Array.from(users.values()));

  socket.on('chat-message', (msg) => {
    io.emit('chat-message', {
      user: username,
      text: msg,
      timestamp: Date.now()
    });
  });

  socket.on('typing', () => {
    socket.broadcast.emit('typing', username);
  });

  socket.on('disconnect', () => {
    users.delete(socket.id);
    io.emit('users', Array.from(users.values()));
  });
});
```

| Feature | ws | Socket.IO |
|---------|-------|-----------|
| Protocol | WebSocket | WebSocket + fallbacks |
| Rooms | Manual | Built-in |
| Events | data/binary | Custom events |
| Reconnection | Manual | Automatic |
| Broadcasting | Manual | Built-in |

**Nästa steg:** Node 16 - Worker Threads

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Worker Threads",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 155,
                "content": r"""
# Worker Threads

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


Parallell körning för CPU-intensiva uppgifter.

## Basic Worker

```javascript
// main.js
import { Worker, isMainThread, parentPort, workerData } from 'node:worker_threads';

if (isMainThread) {
  // Main thread
  const worker = new Worker('./worker.js', {
    workerData: { numbers: [1, 2, 3, 4, 5] }
  });

  worker.on('message', (result) => {
    console.log('Result from worker:', result);
  });

  worker.on('error', (err) => {
    console.error('Worker error:', err);
  });

  worker.on('exit', (code) => {
    console.log(`Worker exited with code ${code}`);
  });
} else {
  // Worker thread
  const { numbers } = workerData;
  const sum = numbers.reduce((a, b) => a + b, 0);
  parentPort.postMessage(sum);
}
```

## Worker i samma fil

```javascript
import { Worker, isMainThread, parentPort, workerData } from 'node:worker_threads';

function runInWorker(data) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(new URL(import.meta.url), {
      workerData: data
    });

    worker.on('message', resolve);
    worker.on('error', reject);
  });
}

if (isMainThread) {
  // Main thread
  async function main() {
    const result = await runInWorker({ task: 'compute', n: 1000000 });
    console.log('Result:', result);
  }

  main();
} else {
  // Worker thread
  const { task, n } = workerData;

  if (task === 'compute') {
    // CPU-intensiv beräkning
    let sum = 0;
    for (let i = 0; i < n; i++) {
      sum += Math.sqrt(i);
    }
    parentPort.postMessage(sum);
  }
}
```

## Worker Pool

```javascript
import { Worker } from 'node:worker_threads';
import os from 'node:os';

class WorkerPool {
  constructor(workerScript, poolSize = os.cpus().length) {
    this.workerScript = workerScript;
    this.poolSize = poolSize;
    this.workers = [];
    this.freeWorkers = [];
    this.taskQueue = [];

    this.init();
  }

  init() {
    for (let i = 0; i < this.poolSize; i++) {
      this.addWorker();
    }
  }

  addWorker() {
    const worker = new Worker(this.workerScript);

    worker.on('message', (result) => {
      worker.currentCallback(null, result);
      this.freeWorkers.push(worker);
      this.runNext();
    });

    worker.on('error', (err) => {
      worker.currentCallback(err);
      this.freeWorkers.push(worker);
      this.runNext();
    });

    this.workers.push(worker);
    this.freeWorkers.push(worker);
  }

  run(data) {
    return new Promise((resolve, reject) => {
      this.taskQueue.push({
        data,
        callback: (err, result) => err ? reject(err) : resolve(result)
      });
      this.runNext();
    });
  }

  runNext() {
    if (this.taskQueue.length === 0) return;
    if (this.freeWorkers.length === 0) return;

    const worker = this.freeWorkers.pop();
    const task = this.taskQueue.shift();

    worker.currentCallback = task.callback;
    worker.postMessage(task.data);
  }

  async close() {
    await Promise.all(
      this.workers.map(w => w.terminate())
    );
  }
}

// Användning
const pool = new WorkerPool('./cpu-worker.js', 4);

const results = await Promise.all([
  pool.run({ task: 'compute', n: 1000000 }),
  pool.run({ task: 'compute', n: 2000000 }),
  pool.run({ task: 'compute', n: 3000000 }),
]);

await pool.close();
```

## SharedArrayBuffer

```javascript
// Delat minne mellan threads
import { Worker, isMainThread, workerData } from 'node:worker_threads';

if (isMainThread) {
  // Skapa delat minne
  const sharedBuffer = new SharedArrayBuffer(4);
  const sharedArray = new Int32Array(sharedBuffer);
  sharedArray[0] = 0;

  const workers = [];
  for (let i = 0; i < 4; i++) {
    workers.push(new Worker(new URL(import.meta.url), {
      workerData: { sharedBuffer }
    }));
  }

  // Vänta på alla workers
  await Promise.all(workers.map(w =>
    new Promise(resolve => w.on('exit', resolve))
  ));

  console.log('Final value:', sharedArray[0]);
} else {
  const { sharedBuffer } = workerData;
  const sharedArray = new Int32Array(sharedBuffer);

  // Atomic operation
  for (let i = 0; i < 1000; i++) {
    Atomics.add(sharedArray, 0, 1);
  }
}
```

## MessageChannel

```javascript
import { Worker, MessageChannel } from 'node:worker_threads';

const worker = new Worker('./worker.js');

// Skapa kanal
const { port1, port2 } = new MessageChannel();

// Skicka port till worker
worker.postMessage({ type: 'init', port: port1 }, [port1]);

// Kommunicera via kanal
port2.on('message', (msg) => {
  console.log('From worker:', msg);
});

port2.postMessage('Hello via channel');

// I worker.js
parentPort.on('message', ({ type, port }) => {
  if (type === 'init') {
    port.on('message', (msg) => {
      port.postMessage(`Echo: ${msg}`);
    });
  }
});
```

## Use Cases

```yaml
Bra för:
  - CPU-intensiva beräkningar
  - Image/video processing
  - Kryptering/hashing
  - Data transformation
  - Parsing stora filer

Inte bra för:
  - I/O operations (använd async/await)
  - Simple tasks (overhead)
  - Real-time communication
```

| Koncept | Beskrivning |
|---------|-------------|
| isMainThread | Boolean - är vi i main thread? |
| parentPort | Kommunicera med parent |
| workerData | Initial data till worker |
| postMessage | Skicka meddelande |
| SharedArrayBuffer | Delat minne |
| Atomics | Thread-safe operations |

**Nästa steg:** Node 17 - Testing

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Testing",
                "difficulty": "expert",
                "estimated_minutes": 60,
                "xp_reward": 170,
                "content": r"""
# Testing

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


Testa Node.js applikationer effektivt.

## Jest Setup

```bash
npm install -D jest @types/jest
```

```json
// package.json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

```javascript
// jest.config.js
export default {
  testEnvironment: 'node',
  transform: {},
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/**/*.test.js'
  ]
};
```

## Unit Tests

```javascript
// utils/math.js
export function add(a, b) {
  return a + b;
}

export function divide(a, b) {
  if (b === 0) throw new Error('Division by zero');
  return a / b;
}

// utils/math.test.js
import { add, divide } from './math.js';

describe('Math utils', () => {
  describe('add', () => {
    test('adds two positive numbers', () => {
      expect(add(1, 2)).toBe(3);
    });

    test('adds negative numbers', () => {
      expect(add(-1, -2)).toBe(-3);
    });
  });

  describe('divide', () => {
    test('divides two numbers', () => {
      expect(divide(10, 2)).toBe(5);
    });

    test('throws on division by zero', () => {
      expect(() => divide(10, 0)).toThrow('Division by zero');
    });
  });
});
```

## Async Testing

```javascript
// services/user.js
export async function getUser(id) {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) throw new Error('User not found');
  return response.json();
}

// services/user.test.js
import { getUser } from './user.js';

describe('User service', () => {
  test('returns user data', async () => {
    const user = await getUser(1);
    expect(user).toHaveProperty('id');
    expect(user).toHaveProperty('email');
  });

  test('throws for non-existent user', async () => {
    await expect(getUser(999)).rejects.toThrow('User not found');
  });
});
```

## Mocking

```javascript
import { jest } from '@jest/globals';
import { UserService } from './user-service.js';
import { db } from './database.js';

// Mock hela modulen
jest.mock('./database.js');

describe('UserService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('creates user', async () => {
    const mockUser = { id: 1, name: 'Alice' };
    db.users.create.mockResolvedValue(mockUser);

    const result = await UserService.create({ name: 'Alice' });

    expect(db.users.create).toHaveBeenCalledWith({ name: 'Alice' });
    expect(result).toEqual(mockUser);
  });
});

// Mock specifik funktion
const mockFetch = jest.fn();
global.fetch = mockFetch;

test('fetches data', async () => {
  mockFetch.mockResolvedValue({
    ok: true,
    json: () => Promise.resolve({ data: 'test' })
  });

  const result = await fetchData();

  expect(mockFetch).toHaveBeenCalledWith('/api/data');
  expect(result).toEqual({ data: 'test' });
});
```

## API Testing (Supertest)

```javascript
import request from 'supertest';
import { app } from './app.js';

describe('User API', () => {
  describe('GET /api/users', () => {
    test('returns list of users', async () => {
      const response = await request(app)
        .get('/api/users')
        .expect('Content-Type', /json/)
        .expect(200);

      expect(response.body).toHaveProperty('data');
      expect(Array.isArray(response.body.data)).toBe(true);
    });
  });

  describe('POST /api/users', () => {
    test('creates a new user', async () => {
      const userData = {
        email: 'test@example.com',
        name: 'Test User'
      };

      const response = await request(app)
        .post('/api/users')
        .send(userData)
        .expect(201);

      expect(response.body.data.email).toBe(userData.email);
    });

    test('returns 400 for invalid data', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ name: '' })
        .expect(400);

      expect(response.body).toHaveProperty('errors');
    });
  });

  describe('Protected routes', () => {
    let token;

    beforeAll(async () => {
      // Login för att få token
      const res = await request(app)
        .post('/api/auth/login')
        .send({ email: 'admin@example.com', password: 'password' });
      token = res.body.token;
    });

    test('GET /api/me requires auth', async () => {
      await request(app)
        .get('/api/me')
        .expect(401);
    });

    test('GET /api/me with token', async () => {
      const response = await request(app)
        .get('/api/me')
        .set('Authorization', `Bearer ${token}`)
        .expect(200);

      expect(response.body.data.email).toBe('admin@example.com');
    });
  });
});
```

## Test Database

```javascript
// test/setup.js
import { PrismaClient } from '@prisma/client';
import { beforeAll, afterAll, beforeEach } from '@jest/globals';

const prisma = new PrismaClient();

beforeAll(async () => {
  // Migrate test database
  await prisma.$executeRaw`TRUNCATE TABLE users CASCADE`;
});

beforeEach(async () => {
  // Seed test data
  await prisma.user.createMany({
    data: [
      { email: 'admin@example.com', name: 'Admin' },
      { email: 'user@example.com', name: 'User' }
    ]
  });
});

afterEach(async () => {
  // Clean up
  await prisma.user.deleteMany();
});

afterAll(async () => {
  await prisma.$disconnect();
});
```

## Test Matchers

```javascript
// Equality
expect(value).toBe(expected);           // ===
expect(value).toEqual(expected);        // Deep equality
expect(value).toStrictEqual(expected);  // Deep + type

// Truthiness
expect(value).toBeTruthy();
expect(value).toBeFalsy();
expect(value).toBeNull();
expect(value).toBeUndefined();
expect(value).toBeDefined();

// Numbers
expect(value).toBeGreaterThan(3);
expect(value).toBeLessThanOrEqual(5);
expect(value).toBeCloseTo(0.3, 5);

// Strings
expect(value).toMatch(/pattern/);
expect(value).toContain('substring');

// Arrays
expect(array).toContain(item);
expect(array).toHaveLength(3);

// Objects
expect(obj).toHaveProperty('key');
expect(obj).toMatchObject({ key: 'value' });

// Exceptions
expect(() => fn()).toThrow();
expect(() => fn()).toThrow('message');
```

| Test Type | Verktyg | Syfte |
|-----------|---------|-------|
| Unit | Jest | Testa funktioner |
| Integration | Supertest | Testa API endpoints |
| E2E | Playwright | Testa hela flöden |

**Nästa steg:** Node 18 - Security

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Security Best Practices",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 165,
                "content": r"""
# Security Best Practices

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


Säkra Node.js applikationer.

## Input Validation

```javascript
import { z } from 'zod';
import sanitizeHtml from 'sanitize-html';

// Schema validation med Zod
const userSchema = z.object({
  email: z.string().email().toLowerCase(),
  password: z.string()
    .min(8)
    .regex(/[A-Z]/, 'Must contain uppercase')
    .regex(/[0-9]/, 'Must contain number'),
  name: z.string().min(1).max(100).trim()
});

// Validering middleware
function validate(schema) {
  return (req, res, next) => {
    try {
      req.body = schema.parse(req.body);
      next();
    } catch (error) {
      res.status(400).json({
        error: 'Validation failed',
        details: error.errors
      });
    }
  };
}

// Sanitize HTML
const cleanHtml = sanitizeHtml(userInput, {
  allowedTags: ['b', 'i', 'em', 'strong', 'a'],
  allowedAttributes: {
    'a': ['href']
  }
});
```

## SQL Injection Prevention

```javascript
// ALDRIG gör detta:
const query = `SELECT * FROM users WHERE id = ${id}`;  // ❌

// Använd parameterized queries:
// Med pg
const result = await pool.query(
  'SELECT * FROM users WHERE id = $1',
  [id]
);

// Med Prisma (automatiskt säkert)
const user = await prisma.user.findUnique({
  where: { id }
});

// Med Mongoose (automatiskt säkert)
const user = await User.findById(id);
```

## XSS Prevention

```javascript
import helmet from 'helmet';
import xssClean from 'xss-clean';

// Security headers
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:'],
    }
  },
  xssFilter: true,
  noSniff: true,
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' }
}));

// XSS clean middleware
app.use(xssClean());

// Output encoding
import { encode } from 'html-entities';

const safeOutput = encode(userInput);
```

## CSRF Protection

```javascript
import csrf from 'csurf';
import cookieParser from 'cookie-parser';

app.use(cookieParser());

const csrfProtection = csrf({ cookie: true });

// Applicera på state-changing routes
app.get('/form', csrfProtection, (req, res) => {
  res.render('form', { csrfToken: req.csrfToken() });
});

app.post('/submit', csrfProtection, (req, res) => {
  // Hanterar request om token är valid
});

// För API:er med JWT är CSRF inte nödvändigt
// eftersom tokens skickas i headers, inte cookies
```

## Rate Limiting

```javascript
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import { createClient } from 'redis';

const redis = createClient();

// General limiter
const generalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 min
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  store: new RedisStore({
    sendCommand: (...args) => redis.sendCommand(args)
  })
});

// Strict limiter för auth
const authLimiter = rateLimit({
  windowMs: 60 * 60 * 1000,  // 1 timme
  max: 5,
  skipSuccessfulRequests: true,
  message: { error: 'Too many login attempts, try again later' }
});

app.use(generalLimiter);
app.use('/api/auth', authLimiter);
```

## Secure Dependencies

```bash
# Scanna för vulnerabilities
npm audit

# Fixa automatiskt
npm audit fix

# Uppdatera dependencies
npm update

# Kolla outdated packages
npm outdated
```

```javascript
// Använd Snyk
// npm install -g snyk
// snyk test
// snyk monitor

// Renovate/Dependabot för automatiska updates
```

## Environment Variables

```javascript
import dotenv from 'dotenv';

// Ladda .env (endast i development)
if (process.env.NODE_ENV !== 'production') {
  dotenv.config();
}

// Validera required env vars
const requiredEnvVars = [
  'DATABASE_URL',
  'JWT_SECRET',
  'REDIS_URL'
];

for (const envVar of requiredEnvVars) {
  if (!process.env[envVar]) {
    console.error(`Missing required environment variable: ${envVar}`);
    process.exit(1);
  }
}

// Aldrig logga secrets
console.log(process.env);  // ❌

// .gitignore
// .env
// .env.local
// .env.*.local
```

## Security Checklist

```yaml
Authentication:
  - [ ] Använd bcrypt/argon2 för passwords
  - [ ] Implementera rate limiting på login
  - [ ] Använd secure, httpOnly cookies
  - [ ] Implementera token rotation

Headers:
  - [ ] Använd Helmet.js
  - [ ] Sätt Content-Security-Policy
  - [ ] Aktivera HSTS
  - [ ] Disable X-Powered-By

Input:
  - [ ] Validera all input
  - [ ] Sanitize output
  - [ ] Använd parameterized queries
  - [ ] Begränsa request body size

Dependencies:
  - [ ] Kör npm audit regelbundet
  - [ ] Uppdatera dependencies
  - [ ] Använd lock files
  - [ ] Scanna med Snyk/Dependabot
```

| Attack | Prevention |
|--------|------------|
| SQL Injection | Parameterized queries |
| XSS | Input validation, CSP |
| CSRF | CSRF tokens, SameSite cookies |
| Brute Force | Rate limiting |
| Secrets Exposure | Environment variables |

**Nästa steg:** Node 19 - Deployment

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Deployment",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 160,
                "content": r"""
# Deployment

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


Deploya Node.js applikationer till produktion.

## PM2 Process Manager

```bash
npm install -g pm2

# Starta app
pm2 start app.js --name my-app

# Med ecosystem file
pm2 ecosystem
```

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'my-app',
    script: './src/index.js',
    instances: 'max',  // Använd alla CPU cores
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    },
    max_memory_restart: '1G',
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    watch: false,
    ignore_watch: ['node_modules', 'logs']
  }]
};
```

```bash
# Kommandon
pm2 start ecosystem.config.js --env production
pm2 stop my-app
pm2 restart my-app
pm2 reload my-app     # Zero-downtime reload
pm2 delete my-app
pm2 logs my-app
pm2 monit
pm2 save              # Spara process lista
pm2 startup           # Auto-start vid boot
```

## Docker

```dockerfile
# Dockerfile
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Production image
FROM node:20-alpine

WORKDIR /app

# Skapa non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001

COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package.json ./

USER nodejs

EXPOSE 3000

ENV NODE_ENV=production

CMD ["node", "dist/index.js"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

## Cloud Platforms

```yaml
# Railway (railway.toml)
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "npm start"
healthcheckPath = "/health"
healthcheckTimeout = 100
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 3
```

```yaml
# Render (render.yaml)
services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    healthCheckPath: /health
    envVars:
      - key: NODE_ENV
        value: production
```

```yaml
# Fly.io (fly.toml)
app = "my-app"
primary_region = "arn"

[http_service]
  internal_port = 3000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 1

[checks]
  [checks.health]
    port = 3000
    type = "http"
    interval = "15s"
    timeout = "5s"
    path = "/health"
```

## CI/CD (GitHub Actions)

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci
      - run: npm test
      - run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Docker build & push
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:latest
```

## Health Checks

```javascript
// Health endpoint
app.get('/health', async (req, res) => {
  const health = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    checks: {}
  };

  // Database check
  try {
    await prisma.$queryRaw`SELECT 1`;
    health.checks.database = 'ok';
  } catch {
    health.checks.database = 'error';
    health.status = 'degraded';
  }

  // Redis check
  try {
    await redis.ping();
    health.checks.redis = 'ok';
  } catch {
    health.checks.redis = 'error';
    health.status = 'degraded';
  }

  const statusCode = health.status === 'ok' ? 200 : 503;
  res.status(statusCode).json(health);
});
```

| Platform | Best For |
|----------|----------|
| Railway | Simple deploys |
| Render | Static + API |
| Fly.io | Edge deployment |
| AWS/GCP | Enterprise scale |
| Vercel | Serverless API |

**Nästa steg:** Node 20 - Monitoring & Logging

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Monitoring & Logging",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 165,
                "content": r"""
# Monitoring & Logging

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


Övervaka och felsök Node.js applikationer.

## Structured Logging (Pino)

```javascript
import pino from 'pino';

// Skapa logger
const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: process.env.NODE_ENV !== 'production'
    ? { target: 'pino-pretty' }
    : undefined,
  base: {
    env: process.env.NODE_ENV,
    version: process.env.npm_package_version
  }
});

// Användning
logger.info('Server started');
logger.info({ port: 3000 }, 'Listening on port');
logger.warn({ userId: 123 }, 'Rate limit exceeded');
logger.error({ err: error }, 'Database connection failed');

// Child logger med kontext
const requestLogger = logger.child({
  requestId: req.id,
  userId: req.user?.id
});
requestLogger.info('Processing request');
```

## Express Integration

```javascript
import pino from 'pino';
import pinoHttp from 'pino-http';

const logger = pino();

// HTTP request logging
app.use(pinoHttp({
  logger,
  customProps: (req) => ({
    userId: req.user?.id
  }),
  serializers: {
    req: (req) => ({
      method: req.method,
      url: req.url,
      headers: {
        'user-agent': req.headers['user-agent']
      }
    }),
    res: (res) => ({
      statusCode: res.statusCode
    })
  }
}));

// Access logger i routes
app.get('/users', (req, res) => {
  req.log.info('Fetching users');
  // ...
});
```

## Error Tracking (Sentry)

```javascript
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  release: process.env.npm_package_version,
  tracesSampleRate: 0.1,  // 10% av requests
  integrations: [
    new Sentry.Integrations.Http({ tracing: true }),
    new Sentry.Integrations.Express({ app }),
    new Sentry.Integrations.Prisma({ client: prisma })
  ]
});

// Request handler först
app.use(Sentry.Handlers.requestHandler());

// Tracing
app.use(Sentry.Handlers.tracingHandler());

// Routes
app.use('/api', routes);

// Error handler sist
app.use(Sentry.Handlers.errorHandler());

// Custom error capture
try {
  await riskyOperation();
} catch (error) {
  Sentry.captureException(error, {
    tags: { feature: 'payment' },
    extra: { userId: user.id }
  });
}
```

## Metrics (Prometheus)

```javascript
import { Registry, Counter, Histogram, collectDefaultMetrics } from 'prom-client';

const register = new Registry();

// Default Node.js metrics
collectDefaultMetrics({ register });

// Custom metrics
const httpRequestsTotal = new Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'path', 'status'],
  registers: [register]
});

const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'path'],
  buckets: [0.1, 0.3, 0.5, 1, 3, 5],
  registers: [register]
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();

  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;

    httpRequestsTotal.inc({
      method: req.method,
      path: req.route?.path || req.path,
      status: res.statusCode
    });

    httpRequestDuration.observe(
      { method: req.method, path: req.route?.path || req.path },
      duration
    );
  });

  next();
});

// Metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.send(await register.metrics());
});
```

## APM (Application Performance Monitoring)

```javascript
// OpenTelemetry
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();

// Custom spans
import { trace } from '@opentelemetry/api';

const tracer = trace.getTracer('my-app');

async function processOrder(orderId) {
  const span = tracer.startSpan('process-order');
  span.setAttribute('order.id', orderId);

  try {
    await validateOrder(orderId);
    await chargePayment(orderId);
    span.setStatus({ code: SpanStatusCode.OK });
  } catch (error) {
    span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });
    throw error;
  } finally {
    span.end();
  }
}
```

## Alerting

```yaml
# Prometheus alerting rules
groups:
  - name: nodejs
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: High error rate detected

      - alert: SlowResponses
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: 95th percentile response time > 1s
```

## Debugging Tips

```javascript
// Memory debugging
process.memoryUsage();
// { rss, heapTotal, heapUsed, external, arrayBuffers }

// CPU profiling
node --prof app.js
node --prof-process isolate-*.log

// Heap snapshot
import v8 from 'node:v8';
import fs from 'node:fs';

const snapshot = v8.writeHeapSnapshot();
console.log(`Heap snapshot written to ${snapshot}`);

// Debug logs
DEBUG=app:* node app.js

import debug from 'debug';
const log = debug('app:server');
log('Server started');
```

| Tool | Purpose |
|------|---------|
| Pino | Structured logging |
| Sentry | Error tracking |
| Prometheus | Metrics |
| Grafana | Dashboards |
| OpenTelemetry | Distributed tracing |

## Node.js SkillsMap Complete! 🎉

Du har nu lärt dig:

1. **Fundamentals** - Runtime, modules, npm
2. **Async** - Event loop, promises, timers
3. **Backend** - HTTP, Express, REST APIs
4. **Advanced** - Auth, files, WebSockets, workers
5. **Production** - Testing, security, deployment, monitoring

Fortsätt med:
- Microservices Architecture
- GraphQL APIs
- Serverless Functions
- Real-time Applications

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_NODEJS


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_NODEJS["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
