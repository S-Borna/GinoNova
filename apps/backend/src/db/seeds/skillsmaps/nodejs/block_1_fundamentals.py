# =============================================================================
# BLOCK 1: FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_INTRO = {
    "node_id": 1,
    "title": "Introduction to Node.js",
    "slug": "intro",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "prerequisites": [],
    "content": '''
# Introduction to Node.js

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Node.js?

Node.js ar en JavaScript runtime byggd pa V8-motorn som lat dig kora JavaScript pa servern.

```
┌─────────────────────────────────────────────────────────────────┐
│                    NODE.JS OVERVIEW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Definition:                                                    │
│  - JavaScript runtime byggd pa V8                               │
│  - Server-side JavaScript                                       │
│  - Event-driven, non-blocking I/O                               │
│                                                                  │
│  Historia:                                                      │
│  - 2009: Ryan Dahl skapar Node.js                               │
│  - 2010: npm lanseras                                           │
│  - 2015: io.js merge, Node.js Foundation                        │
│  - 2019: OpenJS Foundation                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Tooling | npm ar hjarta i modern CI/CD for JS-projekt |
| Microservices | Node.js ar perfekt for latta, snabba tjanster |
| Skalbarhet | Event loop hanterar tusentals connections |
| Full-stack | Samma sprak frontend och backend |
| Automation | Byggverktyg, scripts, CLI-tools |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Funktion |
|----------|----------|
| node --version | Visa Node-version |
| node app.js | Kor en JavaScript-fil |
| node | Starta REPL |
| npm --version | Visa npm-version |
| process.env | Miljovanriabler |
| process.cwd() | Aktuell katalog |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Node.js vs Browser

```javascript
// Browser-only
window, document, DOM, localStorage

// Node.js-only
process, fs, http, path, os, crypto

// Bada har
console, setTimeout, JSON, fetch (Node 18+)

// Global object
// Browser: window
// Node.js: global (eller globalThis)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installation

```bash
# macOS med Homebrew
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Version manager (rekommenderat)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 20
nvm use 20

# Verifiera
node --version
npm --version
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hello World

```javascript
// hello.js
console.log('Hello, Node.js!');

// Kor
// $ node hello.js
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Process Object

```javascript
// process - global objekt i Node.js

// Aktuell Node version
console.log(process.version);

// Miljovariabler
console.log(process.env.NODE_ENV);

// Aktuell working directory
console.log(process.cwd());

// Kommandoradsargument
console.log(process.argv);
// ['node', 'app.js', '--port', '3000']

// Avsluta programmet
process.exit(0);  // Success
process.exit(1);  // Error
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Node.js Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Node.js Application                           │
├─────────────────────────────────────────────────────────────────┤
│                     Node.js APIs                                 │
│         (http, fs, path, crypto, events, etc.)                  │
├─────────────────────────────────────────────────────────────────┤
│                    Node.js Bindings                              │
├──────────────────────────┬──────────────────────────────────────┤
│           V8             │           libuv                       │
│    (JavaScript Engine)   │    (Async I/O, Event Loop)           │
└──────────────────────────┴──────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| node not found | Inte installerat | Installera via nvm |
| Permission denied | Fel rattigheter | Anvand nvm istallet for sudo |
| Version mismatch | Fel Node-version | nvm use <version> |
| Module not found | Saknar dependencies | npm install |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| V8 | Kompilerar JS till maskinkod |
| libuv | Event loop, async I/O |
| process | Global info om korfande process |
| npm | Pakethanterare for Node.js |
| REPL | Interaktiv Node-terminal |

### Kom ihag
- Node.js ar JavaScript pa servern
- Anvand nvm for att hantera versioner
- process ger tillgang till miljon
- Event loop ar nyckel till prestanda
- npm ar varldens storsta paketregister
''',
}

NODE_02_MODULES = {
    "node_id": 2,
    "title": "Modules: CommonJS & ESM",
    "slug": "modules",
    "estimated_minutes": 45,
    "xp_reward": 125,
    "prerequisites": [1],
    "content": '''
# Modules: CommonJS & ESM

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Modules?

Organisera kod i ateranvandbara moduler for battre struktur och underhall.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Maintainability | Modularitet forenklar underhall |
| Testing | Isolerade moduler ar lattare att testa |
| Bundling | Webpack/Rollup hanterar moduler |
| Tree-shaking | ESM mojliggor borttagning av oanvand kod |
| Dependency | Tydliga beroenden mellan komponenter |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Format | Import | Export |
|--------|--------|--------|
| CommonJS | require() | module.exports |
| ESM | import | export |
| Dynamic | await import() | - |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Aktivera ESM

```json
// package.json - for hela projektet
{
  "name": "my-app",
  "type": "module"
}
```

```javascript
// Eller anvand .mjs extension
// file.mjs = ESM
// file.cjs = CommonJS
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CJS vs ESM

```
┌─────────────────────────────────────────────────────────────────┐
│                    CJS vs ESM                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CommonJS:                      ESM:                            │
│  - require() / module.exports   - import / export               │
│  - Synkron laddning             - Asynkron laddning             │
│  - Runtime                      - Compile time (statisk)        │
│  - Default i legacy Node        - Default i browser, modern Node│
│                                                                  │
│  Rekommendation: Anvand ESM for nya projekt                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inbyggda Moduler

```javascript
// Importera inbyggda moduler (anvand node: prefix)
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import crypto from 'node:crypto';
import os from 'node:os';
import events from 'node:events';
import url from 'node:url';
import util from 'node:util';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## __dirname och __filename

```javascript
// CommonJS - direkt tillgangliga
console.log(__dirname);
console.log(__filename);

// ESM - kraver workaround
import { fileURLToPath } from 'node:url';
import { dirname } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dynamic Import

```javascript
// Dynamisk import (fungerar i bade CJS och ESM)
async function loadModule() {
  const module = await import('./dynamic-module.js');
  module.doSomething();
}

// Villkorlig import
if (process.env.NODE_ENV === 'development') {
  const devTools = await import('./dev-tools.js');
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Cannot use import | ESM inte aktiverat | Lagg till "type": "module" |
| __dirname undefined | ESM har inte det | Anvand fileURLToPath |
| ERR_REQUIRE_ESM | CJS importerar ESM | Anvand dynamic import |
| Circular dependency | Moduler refererar varandra | Refaktorera strukturen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| CommonJS | Legacy format med require() |
| ESM | Modern standard med import/export |
| node: prefix | Rekommenderat for inbyggda moduler |
| Dynamic import | Ladda moduler vid runtime |
| Resolution | Node soker core -> node_modules -> path |

### Kom ihag
- Anvand ESM for nya projekt
- Satt "type": "module" i package.json
- node: prefix for inbyggda moduler
- Dynamic import for villkorlig laddning
- Moduler mojliggor tree-shaking
''',
}

NODE_03_NPM = {
    "node_id": 3,
    "title": "npm & Package Management",
    "slug": "npm",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [2],
    "content": '''
# npm & Package Management

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar npm?

Node Package Manager ar varldens storsta register av mjukvarupaket.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| CI/CD | npm install ar central i build pipelines |
| Lockfiles | package-lock.json garanterar reproducerabarhet |
| Security | npm audit hittar sarbarheter |
| Caching | Snabba builds med cache |
| Scripts | Standardiserade kommandon for team |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Funktion |
|----------|----------|
| npm init -y | Skapa package.json |
| npm install | Installera alla dependencies |
| npm i <pkg> | Installera paket |
| npm i -D <pkg> | Installera dev dependency |
| npm run <script> | Kor npm script |
| npm audit | Kontrollera sarbarheter |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## npm Basics

```bash
# Initiera projekt
npm init              # Interaktivt
npm init -y           # Med defaults

# Installera paket
npm install express           # dependencies
npm install -D jest           # devDependencies
npm install -g nodemon        # Globalt

# Kortform
npm i express
npm i -D jest
npm i -g nodemon

# Ta bort paket
npm uninstall express
npm un express

# Uppdatera
npm update
npm update express
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "jest": "^29.7.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Semantic Versioning

```
┌─────────────────────────────────────────────────────────────────┐
│                 SEMANTIC VERSIONING                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Format: MAJOR.MINOR.PATCH (ex: 4.18.2)                         │
│                                                                  │
│  MAJOR: Breaking changes      (4.x.x -> 5.0.0)                  │
│  MINOR: Nya features          (4.18.x -> 4.19.0)                │
│  PATCH: Bug fixes             (4.18.2 -> 4.18.3)                │
│                                                                  │
│  Ranges:                                                        │
│  "^4.18.2" = 4.18.2 - 4.x.x  (MINOR + PATCH)                   │
│  "~4.18.2" = 4.18.2 - 4.18.x (Endast PATCH)                    │
│  "4.18.2"  = Exakt version                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
# Kora scripts
npm run dev
npm run test
npm start          # "start" behover inte "run"
npm test           # "test" behover inte "run"

# Med argument
npm run test -- --watch
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## package-lock.json

```
┌─────────────────────────────────────────────────────────────────┐
│                 PACKAGE-LOCK.JSON                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Syfte:                                                         │
│  - Laser exakta versioner                                       │
│  - Reproducerbara builds                                        │
│  - Snabbare installation                                        │
│                                                                  │
│  Viktigt:                                                       │
│  - Committa till git                                            │
│  - Genereras automatiskt                                        │
│  - Uppdateras vid npm install                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## npm Alternativ

| Tool | Fordel | Kommando |
|------|--------|----------|
| npm | Standard med Node.js | npm install |
| yarn | Snabbare, workspaces | yarn add |
| pnpm | Effektivt diskutrymme | pnpm add |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Workspaces (Monorepo)

```json
// package.json (root)
{
  "name": "my-monorepo",
  "workspaces": ["packages/*"]
}
```

```bash
# Installera for alla workspaces
npm install

# Kora script i specifik workspace
npm run test -w packages/api

# Kora i alla workspaces
npm run test --workspaces
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## npx

```bash
# Kora paket utan global installation
npx create-react-app my-app
npx typescript --init
npx jest

# Kora specifik version
npx node@18 app.js

# Kora lokal binary
npx eslint .
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| ERESOLVE | Version-konflikt | npm install --legacy-peer-deps |
| EACCES | Behorighetsproblem | Anvand nvm, inte sudo |
| ENOENT | Fil saknas | npm install fran scratch |
| audit vulns | Sarbarheter | npm audit fix |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| package.json | Projektets manifest |
| package-lock.json | Exakta versioner, committa |
| semver | MAJOR.MINOR.PATCH |
| scripts | Standardisera kommandon |
| npx | Kora utan installation |

### Kom ihag
- Committa alltid package-lock.json
- Anvand caret (^) for flexibilitet
- npm audit for sakerhet
- npm ci i CI/CD for reproducerbarhet
- scripts standardiserar teamet
''',
}

NODE_04_ERRORS = {
    "node_id": 4,
    "title": "Error Handling",
    "slug": "error-handling",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [1],
    "content": '''
# Error Handling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Error Handling?

Korrekt felhantering ar kritiskt for stabila och debuggbara applikationer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Observability | Strukturerade fel forenklar debugging |
| Resilience | Graceful shutdown skyddar data |
| Monitoring | Felkategorier mojliggor alerting |
| Recovery | Automatisk restart vid fatala fel |
| Logs | Strukturerade fel i centraliserad logging |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Feltyp | Hantering |
|--------|-----------|
| Synkron | try-catch |
| Callback | error-first pattern |
| Promise | .catch() |
| Async/await | try-catch |
| Uncaught | process.on('uncaughtException') |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Try-Catch

```javascript
// Synkrona fel
try {
  const data = JSON.parse(invalidJson);
} catch (error) {
  console.error('Parse error:', error.message);
} finally {
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Custom Errors

```javascript
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

// Anvandning
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
    throw error;
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Graceful Shutdown

```javascript
let server;

server = app.listen(3000);

function shutdown() {
  console.log('Shutting down gracefully...');

  server.close(() => {
    console.log('HTTP server closed');

    mongoose.connection.close(false, () => {
      console.log('MongoDB closed');
      process.exit(0);
    });
  });

  setTimeout(() => {
    console.error('Forced shutdown');
    process.exit(1);
  }, 10000);
}

process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Uncaught Exceptions

```javascript
// Fanga uncaught exceptions (sista utvag)
process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
  process.exit(1);
});

// Unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
});

// OBS: Dessa ar sista utvag!
// Applikationen ar i undefined state
// Best practice: graceful shutdown
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Error Middleware (Express)

```javascript
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) throw new NotFoundError('User');
  res.json(user);
}));

// Error handling middleware
app.use((error, req, res, next) => {
  console.error(error.stack);

  if (error instanceof ValidationError) {
    return res.status(400).json({
      error: 'Validation Error',
      message: error.message
    });
  }

  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'production'
      ? 'Something went wrong'
      : error.message
  });
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Unhandled rejection | Promise utan catch | Lagg till .catch() eller try-catch |
| Memory leak | Listeners inte borttagna | removeListener pa cleanup |
| Crash loop | Uncaught exception | Implementera graceful shutdown |
| Silent failure | Error svaljd | Logga och re-throw |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Custom Errors | Skapa specifika felklasser |
| Error-first | Callback-konvention i Node |
| Graceful shutdown | Stang connections ordentligt |
| asyncHandler | Wrappa async routes |
| process.on | Sista utvag for uncaught |

### Kom ihag
- Skapa custom errors for olika scenarion
- Wrappa async kod i try-catch
- Implementera graceful shutdown
- Logga strukturerat for debugging
- Uncaught handlers ar sista utvag
''',
}

NODEJS_BLOCK_1 = [
    NODE_01_INTRO,
    NODE_02_MODULES,
    NODE_03_NPM,
    NODE_04_ERRORS,
]
