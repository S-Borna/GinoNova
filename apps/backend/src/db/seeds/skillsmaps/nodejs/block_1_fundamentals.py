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
''',
}

NODEJS_BLOCK_1 = [
    NODE_01_INTRO,
    NODE_02_MODULES,
    NODE_03_NPM,
    NODE_04_ERRORS,
]
