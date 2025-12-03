# =============================================================================
# BLOCK 5: PRODUCTION (Noder 17-20)
# =============================================================================

NODE_17_TESTING = {
    "node_id": 17,
    "title": "Testing",
    "slug": "testing",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [10],
    "content": '''
# Testing

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
''',
}

NODE_18_SECURITY = {
    "node_id": 18,
    "title": "Security Best Practices",
    "slug": "security",
    "estimated_minutes": 55,
    "xp_reward": 165,
    "prerequisites": [13],
    "content": '''
# Security Best Practices

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
''',
}

NODE_19_DEPLOYMENT = {
    "node_id": 19,
    "title": "Deployment",
    "slug": "deployment",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [17, 18],
    "content": '''
# Deployment

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
''',
}

NODE_20_MONITORING = {
    "node_id": 20,
    "title": "Monitoring & Logging",
    "slug": "monitoring",
    "estimated_minutes": 55,
    "xp_reward": 165,
    "prerequisites": [19],
    "content": '''
# Monitoring & Logging

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
''',
}

NODEJS_BLOCK_5 = [
    NODE_17_TESTING,
    NODE_18_SECURITY,
    NODE_19_DEPLOYMENT,
    NODE_20_MONITORING,
]
