# =============================================================================
# BLOCK 2: ASYNC PROGRAMMING (Noder 5-8)
# =============================================================================

NODE_05_EVENT_LOOP = {
    "node_id": 5,
    "title": "Event Loop",
    "slug": "event-loop",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [1],
    "content": '''
# Event Loop

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
''',
}

NODE_06_ASYNC = {
    "node_id": 6,
    "title": "Promises & Async/Await",
    "slug": "async-await",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [5],
    "content": '''
# Promises & Async/Await

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
''',
}

NODE_07_EVENTS = {
    "node_id": 7,
    "title": "Event Emitter",
    "slug": "events",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [5],
    "content": '''
# Event Emitter

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
''',
}

NODE_08_STREAMS = {
    "node_id": 8,
    "title": "Streams & Buffers",
    "slug": "streams",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [7],
    "content": '''
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
      this.push(String(this.current++) + '\\n');
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

writeStream.write('Hello\\n');
writeStream.write('World\\n');
writeStream.end('Goodbye\\n');

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
    const lines = chunk.toString().split('\\n');

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
''',
}

NODEJS_BLOCK_2 = [
    NODE_05_EVENT_LOOP,
    NODE_06_ASYNC,
    NODE_07_EVENTS,
    NODE_08_STREAMS,
]
