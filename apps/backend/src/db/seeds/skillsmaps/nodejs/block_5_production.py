# =============================================================================
# BLOCK 5: PRODUCTION (Noder 17-20) - V3 FORMAT
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

Testa Node.js-applikationer med Jest.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Testing?

Testing ar processen att verifiera att koden fungerar som forvantat och upptacka buggar innan produktion.

| Testtyp | Beskrivning |
|---------|-------------|
| Unit tests | Testar enskilda funktioner |
| Integration | Testar komponenter tillsammans |
| E2E | Testar hela flodet |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| CI/CD | Automatiserad kvalitetskontroll |
| Regression | Fanga buggar tidigt |
| Refactoring | Modifiera kod sakert |
| Dokumentation | Tester visar hur koden ska anvandas |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Jest-funktion | Beskrivning |
|---------------|-------------|
| describe | Gruppera tester |
| it / test | Enskilt testfall |
| expect | Assertion |
| beforeEach | Kor fore varje test |
| afterAll | Kor efter alla tester |
| jest.mock | Mocka modul |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Jest Setup

```javascript
// jest.config.js
export default {
  testEnvironment: 'node',
  transform: {},
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  coverageDirectory: 'coverage',
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/**/*.test.js'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80
    }
  }
};
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Unit Tests

```javascript
// math.js
export function add(a, b) {
  return a + b;
}

export function divide(a, b) {
  if (b === 0) throw new Error('Division by zero');
  return a / b;
}

// math.test.js
import { add, divide } from './math.js';

describe('Math functions', () => {
  describe('add', () => {
    it('should add two positive numbers', () => {
      expect(add(2, 3)).toBe(5);
    });

    it('should handle negative numbers', () => {
      expect(add(-1, 1)).toBe(0);
    });
  });

  describe('divide', () => {
    it('should divide two numbers', () => {
      expect(divide(10, 2)).toBe(5);
    });

    it('should throw on division by zero', () => {
      expect(() => divide(10, 0)).toThrow('Division by zero');
    });
  });
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Mocking

```javascript
// userService.js
export async function getUser(id) {
  const response = await fetch('/api/users/' + id);
  return response.json();
}

// userService.test.js
import { getUser } from './userService.js';

// Mock fetch globalt
global.fetch = jest.fn();

describe('getUser', () => {
  beforeEach(() => {
    fetch.mockClear();
  });

  it('should fetch user by id', async () => {
    const mockUser = { id: 1, name: 'Test User' };
    fetch.mockResolvedValueOnce({
      json: () => Promise.resolve(mockUser)
    });

    const user = await getUser(1);

    expect(fetch).toHaveBeenCalledWith('/api/users/1');
    expect(user).toEqual(mockUser);
  });

  it('should handle errors', async () => {
    fetch.mockRejectedValueOnce(new Error('Network error'));

    await expect(getUser(1)).rejects.toThrow('Network error');
  });
});

// Mock en hel modul
jest.mock('./database.js', () => ({
  query: jest.fn()
}));

import { query } from './database.js';

test('mocked database', async () => {
  query.mockResolvedValue([{ id: 1 }]);
  const result = await query('SELECT * FROM users');
  expect(result).toEqual([{ id: 1 }]);
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## API Testing (Supertest)

```javascript
import request from 'supertest';
import app from './app.js';

describe('API Tests', () => {
  describe('GET /api/users', () => {
    it('should return all users', async () => {
      const response = await request(app)
        .get('/api/users')
        .expect('Content-Type', /json/)
        .expect(200);

      expect(response.body).toBeInstanceOf(Array);
    });
  });

  describe('POST /api/users', () => {
    it('should create a user', async () => {
      const newUser = { name: 'Test', email: 'test@test.com' };

      const response = await request(app)
        .post('/api/users')
        .send(newUser)
        .expect(201);

      expect(response.body.name).toBe('Test');
      expect(response.body.id).toBeDefined();
    });

    it('should validate required fields', async () => {
      await request(app)
        .post('/api/users')
        .send({})
        .expect(400);
    });
  });

  describe('Protected routes', () => {
    let token;

    beforeAll(async () => {
      const res = await request(app)
        .post('/auth/login')
        .send({ email: 'test@test.com', password: 'password' });
      token = res.body.token;
    });

    it('should access protected route with token', async () => {
      await request(app)
        .get('/api/profile')
        .set('Authorization', 'Bearer ' + token)
        .expect(200);
    });

    it('should reject without token', async () => {
      await request(app)
        .get('/api/profile')
        .expect(401);
    });
  });
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Test Database

```javascript
// testSetup.js
import { MongoMemoryServer } from 'mongodb-memory-server';
import mongoose from 'mongoose';

let mongod;

export async function setupTestDB() {
  mongod = await MongoMemoryServer.create();
  const uri = mongod.getUri();
  await mongoose.connect(uri);
}

export async function teardownTestDB() {
  await mongoose.connection.dropDatabase();
  await mongoose.connection.close();
  await mongod.stop();
}

export async function clearTestDB() {
  const collections = mongoose.connection.collections;
  for (const key in collections) {
    await collections[key].deleteMany({});
  }
}

// I tester
describe('User model', () => {
  beforeAll(async () => {
    await setupTestDB();
  });

  afterAll(async () => {
    await teardownTestDB();
  });

  beforeEach(async () => {
    await clearTestDB();
  });

  it('should create a user', async () => {
    const user = await User.create({
      name: 'Test',
      email: 'test@test.com'
    });

    expect(user.id).toBeDefined();
    expect(user.name).toBe('Test');
  });
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Coverage

```bash
# Kor tester med coverage
npm test -- --coverage

# Watch mode
npm test -- --watch

# Specifik fil
npm test -- users.test.js

# Match pattern
npm test -- --testNamePattern="should create"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Timeout | Async ej hanterad | await och done() |
| Mock ej aterstald | Saknas clearMocks | beforeEach med mockClear |
| DB state | Delad data mellan tester | beforeEach cleanup |
| Flaky tests | Timing issues | Anvand waitFor/retry |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Jest | Testramverk |
| Mocking | Simulera beroenden |
| Supertest | API-tester |
| Coverage | Mat testtackning |

Kom ihag:
- Skriv tester for kritisk logik
- Mocka externa beroenden
- Anvand test-database for integrationstester
- Sikta pa 80%+ coverage
- Kor tester i CI/CD
''',
}

NODE_18_SECURITY = {
    "node_id": 18,
    "title": "Security Best Practices",
    "slug": "security-practices",
    "estimated_minutes": 55,
    "xp_reward": 165,
    "prerequisites": [13],
    "content": '''
# Security Best Practices

Skydda din Node.js-applikation mot vanliga attacker.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Security?

Security handlar om att skydda applikationen mot attacker, datalackage och andra hot.

| Attacktyp | Beskrivning |
|-----------|-------------|
| Injection | Skadlig kod i input |
| XSS | Script i webbsidor |
| CSRF | Forgad request |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Data protection | Skydda anvandardata |
| Compliance | GDPR, SOC2 |
| Reputation | Undvik intrång |
| Cost | Sakerhetsincidenter ar dyra |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Skydd | Verktyg/Metod |
|-------|---------------|
| Headers | helmet |
| Rate limiting | express-rate-limit |
| Input validation | joi, zod |
| SQL Injection | Parameterized queries |
| XSS | DOMPurify, escape output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Input Validation

```javascript
import Joi from 'joi';

// Schema definition
const userSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).pattern(/[A-Z]/).pattern(/[0-9]/).required(),
  age: Joi.number().integer().min(18).max(120),
  role: Joi.string().valid('user', 'admin').default('user')
});

// Validation middleware
export function validate(schema) {
  return (req, res, next) => {
    const { error, value } = schema.validate(req.body, {
      abortEarly: false,
      stripUnknown: true
    });

    if (error) {
      const errors = error.details.map(d => ({
        field: d.path.join('.'),
        message: d.message
      }));
      return res.status(400).json({ errors });
    }

    req.body = value;
    next();
  };
}

// Anvandning
app.post('/users', validate(userSchema), createUser);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SQL Injection Prevention

```javascript
// FARLIGT - SQL Injection
const query = "SELECT * FROM users WHERE email = '" + email + "'";

// SAKERT - Parameterized queries
// PostgreSQL (pg)
const result = await client.query(
  'SELECT * FROM users WHERE email = $1',
  [email]
);

// MySQL
const [rows] = await connection.execute(
  'SELECT * FROM users WHERE email = ?',
  [email]
);

// ORM (Prisma)
const user = await prisma.user.findUnique({
  where: { email }
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## XSS Prevention

```javascript
import createDOMPurify from 'dompurify';
import { JSDOM } from 'jsdom';
import escape from 'lodash/escape.js';

const window = new JSDOM('').window;
const DOMPurify = createDOMPurify(window);

// Sanera HTML-input
function sanitizeHtml(dirty) {
  return DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p'],
    ALLOWED_ATTR: ['href']
  });
}

// Escape for rendering
function escapeForHtml(text) {
  return escape(text);
}

// Content Security Policy
import helmet from 'helmet';

app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", "data:", "https:"],
    connectSrc: ["'self'", "https://api.example.com"]
  }
}));
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CSRF Protection

```javascript
import csrf from 'csurf';
import cookieParser from 'cookie-parser';

app.use(cookieParser());
app.use(csrf({ cookie: true }));

// Skicka token till frontend
app.get('/csrf-token', (req, res) => {
  res.json({ csrfToken: req.csrfToken() });
});

// Error handler
app.use((err, req, res, next) => {
  if (err.code === 'EBADCSRFTOKEN') {
    return res.status(403).json({ error: 'Invalid CSRF token' });
  }
  next(err);
});

// Frontend: inkludera token i requests
fetch('/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'CSRF-Token': csrfToken
  },
  body: JSON.stringify(data)
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rate Limiting

```javascript
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import { createClient } from 'redis';

const redis = createClient();

// Global rate limit
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minuter
  max: 100,
  message: { error: 'Too many requests, try again later' },
  standardHeaders: true,
  legacyHeaders: false,
  store: new RedisStore({
    sendCommand: (...args) => redis.sendCommand(args)
  })
});

app.use(globalLimiter);

// Striktare for auth endpoints
const authLimiter = rateLimit({
  windowMs: 60 * 60 * 1000,  // 1 timme
  max: 5,
  skipSuccessfulRequests: true,
  message: { error: 'Too many login attempts' }
});

app.use('/auth/login', authLimiter);
app.use('/auth/register', authLimiter);

// Per-user rate limiting
const userLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 30,
  keyGenerator: (req) => req.user?.id || req.ip
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secure Headers (Helmet)

```javascript
import helmet from 'helmet';

app.use(helmet());

// Eller med custom config
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      objectSrc: ["'none'"],
      upgradeInsecureRequests: []
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' }
}));

// Manuella headers
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  next();
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Environment Security

```javascript
// .env - ALDRIG i git
DATABASE_URL=postgres://user:pass@host/db
JWT_SECRET=super-secret-key
API_KEY=external-api-key

// Validera env
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  PORT: z.coerce.number().default(3000)
});

const env = envSchema.parse(process.env);

// Secrets i produktion
// - AWS Secrets Manager
// - HashiCorp Vault
// - Kubernetes Secrets
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dependency Security

```bash
# Kontrollera sarbarheter
npm audit

# Fixa automatiskt
npm audit fix

# Uppdatera dependencies
npx npm-check-updates -u

# Renovate/Dependabot for automatiska PRs
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| SQL Injection | Osaner input | Parameterized queries |
| XSS | Osaner output | CSP + sanitering |
| Secrets leaked | Hardkodade | Environment variables |
| Brute force | Ingen limit | Rate limiting |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Validation | Validera all input |
| Sanitization | Sanera output |
| Rate limiting | Begransar requests |
| Headers | Skyddande HTTP-headers |

Kom ihag:
- Validera och sanera all input
- Anvand parameterized queries
- Implementera rate limiting
- Anvand helmet for security headers
- Kor npm audit regelbundet
''',
}

NODE_19_DEPLOYMENT = {
    "node_id": 19,
    "title": "Deployment",
    "slug": "deployment",
    "estimated_minutes": 65,
    "xp_reward": 180,
    "prerequisites": [17, 18],
    "content": '''
# Deployment

Deploya Node.js-applikationer till produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Deployment?

Deployment ar processen att gora din applikation tillganglig for anvandare i en produktionsmiljo.

| Metod | Beskrivning |
|-------|-------------|
| Traditional | VPS/Server |
| Container | Docker/K8s |
| Serverless | Functions |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Automation | Konsekvent deployment |
| Reliability | Minimera driftstopp |
| Scalability | Hantera last |
| Rollback | Aterga vid problem |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Plattform | Typ | Best for |
|-----------|-----|----------|
| Railway | PaaS | Snabb start |
| Render | PaaS | Full-stack |
| AWS ECS | Container | Skalbarhet |
| Vercel | Serverless | Frontend + API |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PM2 Process Manager

```javascript
// ecosystem.config.cjs
module.exports = {
  apps: [{
    name: 'api',
    script: './src/index.js',
    instances: 'max',  // Cluster mode
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    },
    // Logging
    log_file: './logs/combined.log',
    out_file: './logs/out.log',
    error_file: './logs/error.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    // Auto-restart
    watch: false,
    max_memory_restart: '1G',
    // Graceful shutdown
    kill_timeout: 5000,
    wait_ready: true,
    listen_timeout: 10000
  }]
};
```

```bash
# Starta
pm2 start ecosystem.config.cjs --env production

# Reload utan downtime
pm2 reload api

# Monitoring
pm2 monit

# Cluster scaling
pm2 scale api 4

# Startup script
pm2 startup
pm2 save
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Docker

```dockerfile
# Dockerfile
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:20-alpine

WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .

# Non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

ENV NODE_ENV=production
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["node", "src/index.js"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://postgres:password@db/app
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    deploy:
      replicas: 2
      resources:
        limits:
          memory: 512M

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: password
      POSTGRES_DB: app
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
      - run: npm run lint

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Push to registry
        run: |
          echo ${{ secrets.REGISTRY_PASSWORD }} | docker login -u ${{ secrets.REGISTRY_USER }} --password-stdin
          docker push myapp:${{ github.sha }}

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: |
          curl -X POST ${{ secrets.DEPLOY_WEBHOOK }} \
            -H "Authorization: Bearer ${{ secrets.DEPLOY_TOKEN }}" \
            -d '{"image": "myapp:${{ github.sha }}"}'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Health Checks

```javascript
// Grundlaggande health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

// Detaljerad health check
app.get('/health/ready', async (req, res) => {
  const checks = {
    database: false,
    redis: false,
    memory: true
  };

  try {
    // Database check
    await db.query('SELECT 1');
    checks.database = true;
  } catch (e) {
    console.error('Database check failed:', e);
  }

  try {
    // Redis check
    await redis.ping();
    checks.redis = true;
  } catch (e) {
    console.error('Redis check failed:', e);
  }

  // Memory check
  const used = process.memoryUsage().heapUsed / 1024 / 1024;
  checks.memory = used < 500;  // Under 500MB

  const healthy = Object.values(checks).every(Boolean);

  res.status(healthy ? 200 : 503).json({
    status: healthy ? 'healthy' : 'unhealthy',
    checks,
    uptime: process.uptime()
  });
});

// Liveness (ar processen igång?)
app.get('/health/live', (req, res) => {
  res.status(200).send('OK');
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Graceful Shutdown

```javascript
import { createServer } from 'node:http';

const server = createServer(app);
let isShuttingDown = false;

// Signaler for shutdown
process.on('SIGTERM', gracefulShutdown);
process.on('SIGINT', gracefulShutdown);

async function gracefulShutdown(signal) {
  console.log('Received ' + signal + ', shutting down gracefully');
  isShuttingDown = true;

  // Stoppa nya requests
  server.close(async () => {
    console.log('HTTP server closed');

    // Stang databaskopplingar
    await db.end();
    await redis.quit();

    console.log('All connections closed');
    process.exit(0);
  });

  // Force shutdown efter timeout
  setTimeout(() => {
    console.error('Forced shutdown');
    process.exit(1);
  }, 10000);
}

// Middleware for att avvisa nya requests under shutdown
app.use((req, res, next) => {
  if (isShuttingDown) {
    res.set('Connection', 'close');
    return res.status(503).json({ error: 'Server is shutting down' });
  }
  next();
});

// PM2 ready signal
process.send?.('ready');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Container crashar | Out of memory | Satt memory limits |
| Slow startup | Tunga dependencies | Multi-stage build |
| Downtime vid deploy | Ingen graceful shutdown | Implementera shutdown |
| Lost requests | Ingen health check | Lagg till readiness probe |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| PM2 | Process manager |
| Docker | Containerisering |
| CI/CD | Automatiserad deploy |
| Health checks | Overvakning |

Kom ihag:
- Anvand PM2 eller container orchestration
- Implementera health checks
- Graceful shutdown ar kritiskt
- Automatisera med CI/CD
- Testa i staging fore produktion
''',
}

NODE_20_MONITORING = {
    "node_id": 20,
    "title": "Monitoring & Logging",
    "slug": "monitoring-logging",
    "estimated_minutes": 60,
    "xp_reward": 175,
    "prerequisites": [19],
    "content": '''
# Monitoring och Logging

Overvaka och logga din Node.js-applikation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Monitoring?

Monitoring och logging handlar om att samla in data om applikationens halsa, prestanda och fel.

| Typ | Beskrivning |
|-----|-------------|
| Logs | Text-baserade handelser |
| Metrics | Numerisk data over tid |
| Traces | Request-floden |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Debugging | Hitta problem snabbt |
| Performance | Identifiera flaskhalsar |
| Alerting | Reagera pa problem |
| Capacity | Planera skalning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| Pino | Snabb logging |
| Sentry | Error tracking |
| Prometheus | Metriker |
| Grafana | Visualisering |
| OpenTelemetry | Distributed tracing |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Structured Logging (Pino)

```javascript
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: process.env.NODE_ENV === 'development'
    ? { target: 'pino-pretty' }
    : undefined,
  base: {
    service: 'api',
    version: process.env.npm_package_version
  },
  redact: ['password', 'token', 'authorization']
});

// Anvandning
logger.info('Server started');
logger.info({ port: 3000 }, 'Listening');

logger.error({ err: error, userId }, 'Failed to process request');

logger.debug({ query, params }, 'Database query');

// Child logger med context
const reqLogger = logger.child({ requestId: req.id });
reqLogger.info('Processing request');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Request Logging

```javascript
import pinoHttp from 'pino-http';

const httpLogger = pinoHttp({
  logger,
  genReqId: (req) => req.headers['x-request-id'] || crypto.randomUUID(),
  customLogLevel: (req, res, err) => {
    if (res.statusCode >= 500 || err) return 'error';
    if (res.statusCode >= 400) return 'warn';
    return 'info';
  },
  customSuccessMessage: (req, res) => {
    return req.method + ' ' + req.url + ' ' + res.statusCode;
  },
  customErrorMessage: (req, res, err) => {
    return 'Request failed: ' + err.message;
  },
  // Exkludera health checks
  autoLogging: {
    ignore: (req) => req.url === '/health'
  }
});

app.use(httpLogger);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Error Tracking (Sentry)

```javascript
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  release: process.env.npm_package_version,
  tracesSampleRate: process.env.NODE_ENV === 'production' ? 0.1 : 1.0,
  integrations: [
    new Sentry.Integrations.Http({ tracing: true }),
    new Sentry.Integrations.Express({ app })
  ]
});

// Request handler FORST
app.use(Sentry.Handlers.requestHandler());
app.use(Sentry.Handlers.tracingHandler());

// Routes...

// Error handler SIST
app.use(Sentry.Handlers.errorHandler());

// Manual capture
try {
  await riskyOperation();
} catch (error) {
  Sentry.captureException(error, {
    tags: { feature: 'payment' },
    extra: { userId, orderId }
  });
  throw error;
}

// Breadcrumbs
Sentry.addBreadcrumb({
  category: 'user',
  message: 'User logged in',
  level: 'info'
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Metrics (Prometheus)

```javascript
import promClient from 'prom-client';

// Default metrics
promClient.collectDefaultMetrics();

// Custom metrics
const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests',
  labelNames: ['method', 'route', 'status'],
  buckets: [0.01, 0.05, 0.1, 0.5, 1, 5]
});

const httpRequestsTotal = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'route', 'status']
});

const activeConnections = new promClient.Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();
  activeConnections.inc();

  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    const route = req.route?.path || req.path;

    httpRequestDuration.observe(
      { method: req.method, route, status: res.statusCode },
      duration
    );

    httpRequestsTotal.inc(
      { method: req.method, route, status: res.statusCode }
    );

    activeConnections.dec();
  });

  next();
});

// Metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', promClient.register.contentType);
  res.send(await promClient.register.metrics());
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## OpenTelemetry (Distributed Tracing)

```javascript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

const sdk = new NodeSDK({
  serviceName: 'api',
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT
  }),
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();

// Graceful shutdown
process.on('SIGTERM', () => {
  sdk.shutdown()
    .then(() => console.log('Tracing terminated'))
    .catch((err) => console.error('Error terminating tracing', err))
    .finally(() => process.exit(0));
});

// Manual spans
import { trace } from '@opentelemetry/api';

const tracer = trace.getTracer('my-service');

async function processOrder(orderId) {
  const span = tracer.startSpan('processOrder');
  span.setAttribute('orderId', orderId);

  try {
    // Process...
    span.setStatus({ code: 1 });
  } catch (error) {
    span.setStatus({ code: 2, message: error.message });
    span.recordException(error);
    throw error;
  } finally {
    span.end();
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Alerting

```javascript
// Slack integration
async function sendAlert(message, severity = 'warning') {
  await fetch(process.env.SLACK_WEBHOOK, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: '[' + severity.toUpperCase() + '] ' + message,
      attachments: [{
        color: severity === 'error' ? 'danger' : 'warning',
        fields: [
          { title: 'Service', value: 'api', short: true },
          { title: 'Environment', value: process.env.NODE_ENV, short: true }
        ]
      }]
    })
  });
}

// Alert pa error rate
let errorCount = 0;
const ERROR_THRESHOLD = 10;
const WINDOW_MS = 60000;

setInterval(() => {
  if (errorCount > ERROR_THRESHOLD) {
    sendAlert('High error rate: ' + errorCount + ' errors/minute', 'error');
  }
  errorCount = 0;
}, WINDOW_MS);

app.use((err, req, res, next) => {
  errorCount++;
  next(err);
});
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Logging overhead | Synkron logging | Anvand async (Pino) |
| Missing context | Ingen request ID | Propagera trace ID |
| Alert fatigue | For manga alerts | Justera thresholds |
| Log flooding | Debug i produktion | Konfigurera log levels |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Structured logging | JSON-format |
| Metrics | Numerisk data |
| Tracing | Request-floden |
| Alerting | Proaktiv notifiering |

Kom ihag:
- Anvand structured logging (Pino)
- Sentry for error tracking
- Prometheus for metriker
- OpenTelemetry for distributed tracing
- Satt upp alerts for kritiska problem
''',
}

NODEJS_BLOCK_5 = [
    NODE_17_TESTING,
    NODE_18_SECURITY,
    NODE_19_DEPLOYMENT,
    NODE_20_MONITORING,
]
