# =============================================================================
# BLOCK 3: BACKEND DEVELOPMENT (Noder 9-12)
# =============================================================================

NODE_09_HTTP = {
    "node_id": 9,
    "title": "HTTP Server",
    "slug": "http-server",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [8],
    "content": '''
# HTTP Server

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
  const match = url.pathname.match(/^\\/users\\/(\\d+)$/);
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
''',
}

NODE_10_EXPRESS = {
    "node_id": 10,
    "title": "Express.js Framework",
    "slug": "express",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [9],
    "content": '''
# Express.js Framework

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
''',
}

NODE_11_REST = {
    "node_id": 11,
    "title": "REST API Design",
    "slug": "rest-api",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [10],
    "content": '''
# REST API Design

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
''',
}

NODE_12_DATABASE = {
    "node_id": 12,
    "title": "Database Integration",
    "slug": "database",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [11],
    "content": '''
# Database Integration

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
''',
}

NODEJS_BLOCK_3 = [
    NODE_09_HTTP,
    NODE_10_EXPRESS,
    NODE_11_REST,
    NODE_12_DATABASE,
]
