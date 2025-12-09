# =============================================================================
# BLOCK 2: ASYNC PROGRAMMING (Noder 5-8) - V3 FORMAT
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

Hjartat av Node.js async-modell.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Event Loop?

Event Loop ar den mekanism som gor att Node.js kan hantera tusentals samtidiga operationer trots att det ar single-threaded.

| Egenskap | Beskrivning |
|----------|-------------|
| Funktion | Hanterar async operations |
| Modell | Single-threaded men non-blocking |
| Process | Koar callbacks for exekvering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Skalbarhet | Hog concurrency utan extra tradar |
| Prestanda | Effektiv I/O-hantering |
| Responsivitet | Applikationen blockeras inte |
| Resursanvandning | Lagt minnesavtryck per anslutning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Koncept | Beskrivning | Nar det kors |
|---------|-------------|--------------|
| process.nextTick | Microtask queue | Direkt efter nuvarande operation |
| Promise.then | Microtask queue | Efter nextTick |
| setTimeout | Timers phase | I timers-fasen |
| setImmediate | Check phase | I check-fasen |
| I/O callbacks | Poll phase | I poll-fasen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event Loop Phases

```
   ┌───────────────────────────┐
┌─>│           timers          │  setTimeout, setInterval
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │     pending callbacks     │  I/O callbacks
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │       idle, prepare       │  intern anvandning
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │           poll            │  I/O, network
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │           check           │  setImmediate
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │      close callbacks      │  socket.on('close')
│  └─────────────┬─────────────┘
└───────────────<┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
// 2: setTimeout     (timers phase)
// 3: setImmediate   (check phase)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Microtasks vs Macrotasks

```javascript
// Microtasks (kors forst)
process.nextTick(() => console.log('nextTick'));
Promise.resolve().then(() => console.log('Promise'));
queueMicrotask(() => console.log('queueMicrotask'));

// Macrotasks (kors i faser)
setTimeout(() => console.log('setTimeout'));
setInterval(() => console.log('setInterval'));
setImmediate(() => console.log('setImmediate'));
```

Prioritetsordning:

| Prioritet | Typ | Exempel |
|-----------|-----|---------|
| 1 (hogst) | nextTick | process.nextTick |
| 2 | Microtasks | Promise.then |
| 3 | Macrotasks | setTimeout, I/O |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## process.nextTick

```javascript
// Kors direkt efter nuvarande operation
// Innan event loop fortsatter

function asyncOperation(callback) {
  // Garantera async
  process.nextTick(() => {
    callback(null, 'result');
  });
}

// Anvandning
asyncOperation((err, result) => {
  console.log(result);
});
console.log('After call');  // Loggas forst!
```

Viktigt: For manga nextTick kan blockera I/O. Anvand setImmediate for CPU-intensivt arbete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## setImmediate vs setTimeout

```javascript
// setImmediate: check phase
// setTimeout(..., 0): timers phase

// I main script: ordning odefinierad
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));

// I I/O callback: setImmediate alltid forst
const fs = require('fs');

fs.readFile('file.txt', () => {
  setTimeout(() => console.log('timeout'), 0);
  setImmediate(() => console.log('immediate'));
  // Alltid: immediate forst, sedan timeout
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Blocking Event Loop

```javascript
// DALIGT: Blockerar event loop
app.get('/compute', (req, res) => {
  const result = heavyComputation();  // Blockerar!
  res.json({ result });
});

// BATTRE: Dela upp arbetet
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

// BAST: Worker threads for CPU-intensivt
const { Worker } = require('worker_threads');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring Event Loop

```javascript
// Mat event loop lag
let lastCheck = Date.now();

setInterval(() => {
  const now = Date.now();
  const lag = now - lastCheck - 1000;

  if (lag > 100) {
    console.warn('Event loop lag: ' + lag + 'ms');
  }

  lastCheck = now;
}, 1000);

// Eller anvand paket
const blocked = require('blocked-at');

blocked((time, stack) => {
  console.log('Blocked for ' + time + 'ms');
  console.log(stack);
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Blockerad event loop | Synkron CPU-intensiv kod | Anvand Worker threads |
| Memory leaks | For manga nextTick | Begransat antal, anvand setImmediate |
| Oforutsagbar ordning | Blanda timers i main | Var medveten om fasernas ordning |
| Callback hell | Djupt nastlade callbacks | Anvand async/await |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Viktigt att komma ihag |
|---------|------------------------|
| Single-threaded | Node.js kor JavaScript i en trad |
| Non-blocking | I/O-operationer blockerar inte |
| Faser | Event loop har specifika faser |
| Prioritet | nextTick > Promises > Timers |

Kom ihag:
- Event loop ar hjartat av Node.js asynkrona modell
- Microtasks kors fore macrotasks
- Undvik att blockera event loop med synkron kod
- Anvand Worker threads for CPU-intensivt arbete
- Overvaka event loop lag i produktion
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
# Promises och Async/Await

Modern asynkron programmering i Node.js.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Promises?

Promises ar ett satt att hantera asynkrona operationer utan djupt nastlade callbacks.

| Egenskap | Beskrivning |
|----------|-------------|
| Pending | Operationen pagar |
| Fulfilled | Operationen lyckades |
| Rejected | Operationen misslyckades |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| CI/CD Scripts | Hantera asynkrona build-steg |
| API-anrop | Parallella requests till tjanster |
| Filoperationer | Lasa/skriva konfigurationsfiler |
| Databasoperationer | Hantera queries effektivt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Metod | Anvandning | Beteende |
|-------|------------|----------|
| Promise.all | Alla maste lyckas | Returnerar array |
| Promise.allSettled | Alla oavsett resultat | Returnerar status |
| Promise.race | Forsta som blir klar | Returnerar forsta |
| Promise.any | Forsta som lyckas | Ignorerar rejects |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Callbacks (Legacy)

```javascript
// Callback hell - undvik detta
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

// Anvand Promise
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Promise Utilities

```javascript
// Promise.all - alla maste lyckas
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

// Promise.race - forsta som blir klar
const result = await Promise.race([
  fetch(primaryUrl),
  fetch(backupUrl)
]);

// Promise.any - forsta som lyckas
const result = await Promise.any([
  fetch(url1),
  fetch(url2)
]);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Common Patterns

```javascript
// Sequential (en at gangen)
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Promisify

```javascript
import { promisify } from 'node:util';
import fs from 'node:fs';

// Konvertera callback till Promise
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

// Anvandning
const data = await readFile('file.txt');

// Eller anvand fs/promises
import { readFile, writeFile } from 'node:fs/promises';

const data = await readFile('file.txt');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Unhandled rejection | Saknar catch | Lagg till catch eller try/catch |
| Sequential istallet for parallel | await i loop | Anvand Promise.all |
| Memory issues | For manga parallella | Begransat concurrency med p-limit |
| Lost errors | Ignorerar rejected | Anvand Promise.allSettled |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Pattern | Anvandningsfall |
|---------|-----------------|
| Sequential | Beroende operationer |
| Promise.all | Oberoende, alla kravs |
| Promise.allSettled | Oberoende, partiellt OK |
| Promise.race | Forsta svaret vinner |
| Promise.any | Forsta framgang vinner |

Kom ihag:
- Async/await ar syntaktiskt socker over Promises
- Anvand alltid try/catch for felhantering
- Promise.all for parallella oberoende operationer
- Undvik await i loopar om operationerna ar oberoende
- Promisify konverterar callback-funktioner till Promises
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Event Emitter?

Event Emitter ar ett designmonster som tillater objekt att kommunicera genom att skicka och lyssna pa events.

| Egenskap | Beskrivning |
|----------|-------------|
| Publisher | Skickar events med emit() |
| Subscriber | Lyssnar pa events med on() |
| Decoupling | Losar koppling mellan komponenter |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Logging | Event-baserad loggning |
| Monitoring | Reagera pa systemhandelser |
| Webhooks | Hantera inkommande events |
| Microservices | Kommunikation mellan tjanster |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Metod | Beskrivning | Anvandning |
|-------|-------------|------------|
| on() | Lagg till listener | Lyssna pa events |
| once() | Lyssna en gang | Engangshandelser |
| emit() | Trigga event | Skicka data |
| off() | Ta bort listener | Cleanup |
| removeAllListeners() | Ta bort alla | Full cleanup |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Basics

```javascript
import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// Lyssna pa event
emitter.on('message', (data) => {
  console.log('Received:', data);
});

// Emit event
emitter.emit('message', 'Hello World');
// Output: Received: Hello World

// Flera argument
emitter.on('user', (name, age) => {
  console.log(name + ' is ' + age + ' years old');
});

emitter.emit('user', 'Alice', 30);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event Methods

```javascript
const emitter = new EventEmitter();

// on() - Lyssna (alias: addListener)
emitter.on('event', handler);

// once() - Lyssna en gang
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Custom Event Emitter

```javascript
import { EventEmitter } from 'node:events';

class Database extends EventEmitter {
  constructor() {
    super();
    this.connected = false;
  }

  async connect() {
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

// Anvandning
const db = new Database();

db.on('connected', () => console.log('DB connected!'));
db.on('query', (sql) => console.log('Executing:', sql));
db.on('disconnected', () => console.log('DB disconnected'));

await db.connect();
await db.query('SELECT * FROM users');
db.disconnect();
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Error Events

```javascript
const emitter = new EventEmitter();

// Om ingen lyssnare: kraschar processen
emitter.emit('error', new Error('Something failed'));

// Lagg alltid till error handler
emitter.on('error', (error) => {
  console.error('Error occurred:', error.message);
});

emitter.emit('error', new Error('Something failed'));
// Hanteras nu sakert
```

Viktigt: Lagg ALLTID till en error-lyssnare for att undvika processkrasch.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Async Events

```javascript
import { EventEmitter } from 'node:events';
import { once } from 'node:events';

const emitter = new EventEmitter();

// Async listener
emitter.on('process', async (data) => {
  await processData(data);
  console.log('Processing complete');
});

// Emit vantar inte automatiskt
emitter.emit('process', myData);
console.log('After emit');  // Loggas direkt

// For att vanta pa specifikt event
setTimeout(() => emitter.emit('ready', 'data'), 1000);

const [data] = await once(emitter, 'ready');
console.log('Received:', data);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Best Practices

```javascript
// Satt max listeners (default: 10)
emitter.setMaxListeners(20);

// Rensa listeners for att undvika memory leaks
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

// prepend listener (kors forst)
emitter.prependListener('event', handler);
emitter.prependOnceListener('event', handler);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| MaxListenersExceeded | For manga listeners | Oka limit eller rensa |
| Memory leak | Listeners ej borttagna | Anvand off() i cleanup |
| Uncaught error | Ingen error listener | Lagg alltid till error handler |
| Lost events | Listener tillagd sent | Registrera fore emit |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Metod | Beskrivning |
|-------|-------------|
| on() | Lagg till listener |
| once() | Lyssna en gang |
| emit() | Trigga event |
| off() | Ta bort listener |
| removeAllListeners() | Ta bort alla |

Kom ihag:
- Event Emitter ar grunden for Node.js I/O
- Lagg alltid till error-lyssnare
- Rensa listeners for att undvika memory leaks
- Anvand once() for engangshandelser
- Streams och HTTP-server ar EventEmitters
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
# Streams och Buffers

Effektiv hantering av stora datamangder.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Streams?

Streams ar ett satt att hantera data i bitar istallet for att ladda allt i minnet.

| Egenskap | Beskrivning |
|----------|-------------|
| Chunked | Data behandlas i bitar |
| Memory-efficient | Lagt minnesavtryck |
| Pipeable | Kan kedjas ihop |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Log processing | Hantera stora loggfiler |
| File transfers | Effektiv filoverforing |
| Data pipelines | ETL-processer |
| Video streaming | Media-leverans |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Stream-typ | Metod | Anvandning |
|------------|-------|------------|
| Readable | pipe() | Lasa filer, HTTP req |
| Writable | write() | Skriva filer, HTTP res |
| Transform | pipe() | Kompression, parsing |
| Duplex | pipe() | Sockets |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor Streams?

```javascript
// DALIGT: Laser hela filen i minnet
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stream Types

| Typ | Beskrivning | Exempel |
|-----|-------------|---------|
| Readable | Lasa data | fs.createReadStream, http request |
| Writable | Skriva data | fs.createWriteStream, http response |
| Duplex | Lasa och skriva | TCP socket, WebSocket |
| Transform | Modifiera data | zlib (compression), crypto |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
    console.log('[LOG] ' + new Date().toISOString() + ': ' + line);
    callback();  // Signalera klar
  }
}

const logger = new LoggerStream();
logger.write('Message 1');
logger.write('Message 2');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Buffers

```javascript
// Buffer = raw binary data

// Skapa buffer
const buf1 = Buffer.from('Hello');
const buf2 = Buffer.alloc(10);  // 10 bytes, fyllt med 0
const buf3 = Buffer.allocUnsafe(10);  // Snabbare, ej nollstalld

// Konvertera
const str = buf1.toString('utf8');
const hex = buf1.toString('hex');
const base64 = buf1.toString('base64');

// Fran olika format
const fromHex = Buffer.from('48656c6c6f', 'hex');
const fromBase64 = Buffer.from('SGVsbG8=', 'base64');

// Buffer operations
const combined = Buffer.concat([buf1, buf2]);
const slice = buf1.subarray(0, 3);
const copied = Buffer.alloc(5);
buf1.copy(copied);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Memory spike | Laser hela filen | Anvand streams |
| Backpressure | Skriver snabbare an lasning | Hantera drain event |
| Data loss | Pipe error | Anvand pipeline() |
| Encoding issues | Fel encoding | Ange encoding explicit |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Streams | Hantera data i chunks |
| Buffers | Raw binary data |
| Pipeline | Sakert satt att kedja streams |
| Transform | Modifiera data on-the-fly |

Kom ihag:
- Anvand streams for stora filer
- Pipeline ar sakrare an pipe
- Buffers ar for raa binardata
- Transform streams for databearbetning
- Hantera alltid error-events pa streams
''',
}

NODEJS_BLOCK_2 = [
    NODE_05_EVENT_LOOP,
    NODE_06_ASYNC,
    NODE_07_EVENTS,
    NODE_08_STREAMS,
]
