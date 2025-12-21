# =============================================================================
# BLOCK 4: ADVANCED PATTERNS (Noder 13-16) - V3 FORMAT
# =============================================================================

NODE_13_AUTH = {
    "node_id": 13,
    "title": "Authentication & Security",
    "slug": "auth-security",
    "estimated_minutes": 65,
    "xp_reward": 180,
    "prerequisites": [12],
    "content": '''
# Authentication och Security

Saker autentisering i Node.js.

------------------------------------------------------------

## Vad ar Authentication?

Authentication handlar om att verifiera vem anvandaren ar och skydda applikationen mot attacker.

| Koncept | Beskrivning |
|---------|-------------|
| Autentisering | Vem ar du? |
| Auktorisering | Vad far du gora? |
| Tokens | Identitetsbevaring |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Sakerhet | Skydda data och system |
| Compliance | Uppfyll krav (GDPR) |
| Audit trails | Sparbarhet |
| Zero trust | Verifiera alltid |

------------------------------------------------------------

## Snabbreferens

| Koncept | Implementering |
|---------|----------------|
| Password hashing | bcrypt/argon2 |
| Tokens | JWT |
| Sessions | express-session + Redis |
| OAuth | Passport.js |
| Rate limiting | express-rate-limit |

------------------------------------------------------------

## JWT Authentication

```javascript
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

// Registrering
export async function register(req, res) {
  const { email, password, name } = req.body;

  // Kolla om anvandare finns
  const existing = await User.findOne({ email });
  if (existing) {
    return res.status(400).json({ error: 'Email already registered' });
  }

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 12);

  // Skapa anvandare
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

  // Hitta anvandare
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

------------------------------------------------------------

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
  await redis.set('refresh:' + user.id, refreshToken, { EX: 7 * 24 * 3600 });

  res.json({ accessToken, refreshToken });
}

// Refresh endpoint
export async function refresh(req, res) {
  const { refreshToken } = req.body;

  try {
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);

    // Verifiera att token fortfarande ar giltig
    const storedToken = await redis.get('refresh:' + decoded.id);
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

------------------------------------------------------------

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
    // Hitta eller skapa anvandare
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
    res.redirect('/app?token=' + token);
  }
);
```

------------------------------------------------------------

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

// Stricter limit for auth
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

------------------------------------------------------------

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

------------------------------------------------------------

## RBAC (Role-Based Access Control)

```javascript
// Roles och permissions
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

// Anvandning
app.delete('/users/:id',
  authenticate,
  authorize('delete', 'manage'),
  deleteUser
);
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Token expired | Kort livstid | Implementera refresh tokens |
| Password leak | Ingen hashing | Anvand bcrypt/argon2 |
| Brute force | Ingen rate limiting | Implementera rate limit |
| XSS attack | Ingen sanitering | Anvand helmet och xss-clean |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| JWT | Stateless tokens |
| Refresh tokens | Fornyelse utan inloggning |
| RBAC | Rollbaserad behorighet |
| Rate limiting | Skydd mot brute force |

Kom ihag:
- Hasha alltid losenord med bcrypt eller argon2
- Anvand refresh tokens for battre sakerhet
- Implementera rate limiting pa alla endpoints
- Anvand helmet for security headers
- Validera och sanera all input
''',
}

NODE_14_FILES = {
    "node_id": 14,
    "title": "File Handling",
    "slug": "file-handling",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [9],
    "content": '''
# File Handling

Las, skriv och hantera filer i Node.js.

------------------------------------------------------------

## Vad ar File Handling?

File handling ar operationer for att lasa, skriva och manipulera filer pa filsystemet.

| Operation | Beskrivning |
|-----------|-------------|
| Read | Lasa filinnehall |
| Write | Skriva till fil |
| Stream | Hantera stora filer |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Log files | Lasa och analysera loggar |
| Config files | Hantera konfiguration |
| Uploads | Hantera filuppladdningar |
| Backups | Automatiserade backuper |

------------------------------------------------------------

## Snabbreferens

| Metod | Sync | Async (Promises) |
|-------|------|------------------|
| Lasa | readFileSync | readFile |
| Skriva | writeFileSync | writeFile |
| Kopiera | copyFileSync | copyFile |
| Stats | statSync | stat |

------------------------------------------------------------

## File System Module

```javascript
import fs from 'node:fs/promises';
import path from 'node:path';

// Las fil
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

------------------------------------------------------------

## Directory Operations

```javascript
// Lista filer
const files = await fs.readdir('./src');
console.log(files);

// Med file types
const entries = await fs.readdir('./src', { withFileTypes: true });
for (const entry of entries) {
  if (entry.isDirectory()) {
    console.log('Dir: ' + entry.name);
  } else {
    console.log('File: ' + entry.name);
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

------------------------------------------------------------

## Streams

```javascript
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';
import { createGzip, createGunzip } from 'node:zlib';

// Lasa stora filer
const stream = createReadStream('large-file.txt', {
  encoding: 'utf-8',
  highWaterMark: 64 * 1024  // 64KB chunks
});

stream.on('data', (chunk) => {
  console.log('Received ' + chunk.length + ' bytes');
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

------------------------------------------------------------

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
    const uniqueName = Date.now() + '-' + Math.random().toString(36).slice(2);
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

------------------------------------------------------------

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
  const key = 'uploads/' + Date.now() + '-' + file.originalname;

  await s3.send(new PutObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key,
    Body: file.buffer,
    ContentType: file.mimetype
  }));

  return key;
}

// Signed URL for download
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

------------------------------------------------------------

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

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| ENOENT | Fil finns inte | Kontrollera path |
| EACCES | Behorighetsfel | Kontrollera permissions |
| EMFILE | For manga oppna filer | Anvand streams |
| Memory overflow | Stor fil i minnet | Anvand streams |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| fs/promises | Async filoperationer |
| Streams | For stora filer |
| Multer | Filuppladdningar |
| Path | Hantera filsokvagar |

Kom ihag:
- Anvand alltid fs/promises for async
- Streams for stora filer
- Validera filtyper vid uppladdning
- Anvand path.join for platformoberoende sokvagar
- Cloud storage for produktion
''',
}

NODE_15_WEBSOCKETS = {
    "node_id": 15,
    "title": "WebSockets",
    "slug": "websockets",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [10],
    "content": '''
# WebSockets

Real-time kommunikation med WebSockets.

------------------------------------------------------------

## Vad ar WebSockets?

WebSockets ar ett protokoll for tvavagskommunikation mellan klient och server i realtid.

| Egenskap | Beskrivning |
|----------|-------------|
| Bidirectional | Bada kan skicka nar som helst |
| Persistent | Oppet connection |
| Low latency | Minimal fordrojning |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Real-time dashboards | Live metriker |
| Log streaming | Direkta loggar |
| Notifications | Push-meddelanden |
| Chat/Collaboration | Teamkommunikation |

------------------------------------------------------------

## Snabbreferens

| Feature | ws | Socket.IO |
|---------|-------|-----------|
| Protocol | WebSocket | WebSocket + fallbacks |
| Rooms | Manual | Built-in |
| Events | data/binary | Custom events |
| Reconnection | Manual | Automatic |
| Broadcasting | Manual | Built-in |

------------------------------------------------------------

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

------------------------------------------------------------

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

// Heartbeat for att detektera doda connections
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

------------------------------------------------------------

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
  console.log('User connected: ' + socket.user.id);

  // Join room
  socket.join('user:' + socket.user.id);

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
    console.log('User disconnected: ' + socket.user.id);
  });
});

// Emit from anywhere
function notifyUser(userId, event, data) {
  io.to('user:' + userId).emit(event, data);
}

server.listen(3000);
```

------------------------------------------------------------

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

------------------------------------------------------------

## Rooms och Namespaces

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

------------------------------------------------------------

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

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Connection refused | Server ej startad | Kontrollera server |
| CORS error | CORS ej konfigurerat | Konfigurera cors i Socket.IO |
| Memory leak | Listeners ej borttagna | Rensa vid disconnect |
| Stale connections | Ingen heartbeat | Implementera ping/pong |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| WebSocket | Raw protocol |
| Socket.IO | Abstraction med extras |
| Rooms | Gruppera connections |
| Namespaces | Separera logik |

Kom ihag:
- WebSockets for tvavagskommunikation
- Socket.IO for produktionsapplikationer
- Implementera heartbeat for connection health
- Anvand rooms for att gruppera klienter
- Hantera reconnection gracefully
''',
}

NODE_16_WORKERS = {
    "node_id": 16,
    "title": "Worker Threads",
    "slug": "worker-threads",
    "estimated_minutes": 50,
    "xp_reward": 155,
    "prerequisites": [5],
    "content": '''
# Worker Threads

Parallell korning for CPU-intensiva uppgifter.

------------------------------------------------------------

## Vad ar Worker Threads?

Worker Threads gor det mojligt att kora JavaScript i parallella tradar for CPU-intensivt arbete.

| Egenskap | Beskrivning |
|----------|-------------|
| Parallellism | Flera tradar samtidigt |
| CPU-bound | For tunga berakningar |
| Isolation | Separat minne per worker |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Build tools | Parallella builds |
| Data processing | Tunga berakningar |
| Image processing | Bild-/videobearbetning |
| Encryption | Kryptografiska operationer |

------------------------------------------------------------

## Snabbreferens

| Koncept | Beskrivning |
|---------|-------------|
| isMainThread | Boolean - ar vi i main thread? |
| parentPort | Kommunicera med parent |
| workerData | Initial data till worker |
| postMessage | Skicka meddelande |
| SharedArrayBuffer | Delat minne |
| Atomics | Thread-safe operations |

------------------------------------------------------------

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
    console.log('Worker exited with code ' + code);
  });
} else {
  // Worker thread
  const { numbers } = workerData;
  const sum = numbers.reduce((a, b) => a + b, 0);
  parentPort.postMessage(sum);
}
```

------------------------------------------------------------

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
    // CPU-intensiv berakning
    let sum = 0;
    for (let i = 0; i < n; i++) {
      sum += Math.sqrt(i);
    }
    parentPort.postMessage(sum);
  }
}
```

------------------------------------------------------------

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

// Anvandning
const pool = new WorkerPool('./cpu-worker.js', 4);

const results = await Promise.all([
  pool.run({ task: 'compute', n: 1000000 }),
  pool.run({ task: 'compute', n: 2000000 }),
  pool.run({ task: 'compute', n: 3000000 }),
]);

await pool.close();
```

------------------------------------------------------------

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

  // Vanta pa alla workers
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

------------------------------------------------------------

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
      port.postMessage('Echo: ' + msg);
    });
  }
});
```

------------------------------------------------------------

## Use Cases

| Bra for | Inte bra for |
|---------|--------------|
| CPU-intensiva berakningar | I/O operations |
| Image/video processing | Enkla uppgifter |
| Kryptering/hashing | Real-time communication |
| Data transformation | Simpla tasks (overhead) |
| Parsing stora filer | |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Worker crash | Uncaught error | Lagg till error handler |
| Slow communication | Stora meddelanden | Anvand SharedArrayBuffer |
| Memory leak | Workers ej terminerade | Anropa terminate() |
| Race conditions | Delat minne | Anvand Atomics |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Worker Threads | Parallella tradar |
| Worker Pool | Ateranvand workers |
| SharedArrayBuffer | Delat minne |
| Atomics | Thread-safe operations |

Kom ihag:
- Anvand workers for CPU-intensivt arbete
- Worker pools for effektivitet
- SharedArrayBuffer for delat minne
- Atomics for thread-safe operationer
- Undvik workers for I/O-operationer
''',
}

NODEJS_BLOCK_4 = [
    NODE_13_AUTH,
    NODE_14_FILES,
    NODE_15_WEBSOCKETS,
    NODE_16_WORKERS,
]
