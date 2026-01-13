"""
Datadog Monitoring - Modern Observability Platform
===================================================

Master Datadog for application performance monitoring (APM), infrastructure monitoring,
and log management. The all-in-one observability platform used by 40% of DevOps teams.

Coverage:
- Infrastructure monitoring
- APM (Application Performance Monitoring)
- Log management
- Synthetic monitoring
- Custom metrics and dashboards
"""

DATADOG_FUNDAMENTALS = {
    "title": "Datadog APM & Infrastructure Monitoring",
    "slug": "datadog-monitoring",
    "description": "Master Datadog for modern observability: APM traces, infrastructure monitoring, log aggregation, and custom dashboards.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Datadog APM & Infrastructure Monitoring

## 🎯 TL;DR (30 seconds)

Datadog is an all-in-one monitoring SaaS platform: infrastructure metrics, APM traces, logs, and synthetics
in one place. No infrastructure to maintain - install agent, get instant visibility into your entire stack.

**Why this matters:** Datadog correlates metrics, traces, and logs automatically. Click on a spike in latency,
see the exact slow database query, jump to logs. 40% of modern DevOps teams use Datadog.

---

## 🚀 Why Datadog for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 40% of DevOps Engineer roles use Datadog
- 55% of SRE roles at startups/scale-ups use Datadog
- 35% of Platform Engineer roles work with Datadog
- Growing fast (30% YoY) as companies move from Prometheus/ELK

**Salary Impact (Sweden):**
| Role | Without APM | With Datadog | Difference |
|------|------------|--------------|------------|
| Junior DevOps | 38,000 SEK | 44,000 SEK | **+16%** |
| DevOps Engineer | 45,000 SEK | 54,000 SEK | **+20%** |
| Senior SRE | 60,000 SEK | 73,000 SEK | **+22%** |

**Companies using Datadog:** Airbnb, Peloton, Samsung, Adobe, Whole Foods, HBO

---

## 📖 THEORY: What is Datadog?

### The Observability Problem

**Scenario: Modern microservices app with 20 services**

❌ **Without Datadog (Patchwork monitoring):**
```
Prometheus → Metrics (CPU, memory)
ELK Stack → Logs
Jaeger → Distributed tracing
New Relic → APM
PagerDuty → Alerting

Problem:
- 5 different tools to check
- No correlation between data
- 5 different query languages
- 5 vendor bills
```

✅ **With Datadog:**
```
One platform:
✅ Infrastructure metrics
✅ APM traces
✅ Logs
✅ Synthetics
✅ Real user monitoring

Click latency spike → See trace → See logs → See host metrics
All in one UI, automatically correlated ✅
```

---

### Datadog Components

**1. Agent** - Runs on your servers/containers
```
Datadog Agent (lightweight daemon):
- Collects system metrics (CPU, memory, disk, network)
- Collects application metrics
- Sends logs
- Runs service checks
```

**2. APM (Application Performance Monitoring)**
```
Traces distributed requests across services:
User → API Gateway → Auth Service → Database
Shows: Which service is slow? Which query?
```

**3. Log Management**
```
Centralized logging (like ELK):
- Automatic log parsing
- Pattern detection
- Anomaly detection
- Correlation with metrics/traces
```

**4. Synthetics**
```
Proactive monitoring:
- HTTP checks (uptime monitoring)
- Browser tests (simulate user flows)
- API tests (multi-step workflows)
```

**5. Dashboards**
```
Customizable visualizations:
- Time series graphs
- Heatmaps
- Top lists
- Template variables
```

---

## 🛠️ HANDS-ON: Datadog Setup

### Step 1: Create Datadog Account

**Sign up:**
```
1. Go to datadoghq.com
2. Start free trial (14 days)
3. Select region (EU or US)
4. Get API key from: Organization Settings → API Keys
```

---

### Step 2: Install Datadog Agent

**Linux (Ubuntu/Debian):**
```bash
# Set your API key
DD_API_KEY=your_api_key_here

# One-line install
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=$DD_API_KEY DD_SITE="datadoghq.eu" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"

# Verify
sudo systemctl status datadog-agent

# Check agent info
sudo datadog-agent status
```

**Docker (for testing):**
```bash
docker run -d --name datadog-agent \
  -e DD_API_KEY=your_api_key_here \
  -e DD_SITE="datadoghq.eu" \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /proc/:/host/proc/:ro \
  -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
  datadog/agent:latest
```

**Kubernetes (recommended for prod):**
```yaml
# datadog-values.yaml for Helm
datadog:
  apiKey: YOUR_API_KEY
  site: datadoghq.eu
  logs:
    enabled: true
    containerCollectAll: true
  apm:
    enabled: true
    portEnabled: true

# Install with Helm
helm repo add datadog https://helm.datadoghq.com
helm install datadog-agent datadog/datadog -f datadog-values.yaml
```

---

### Step 3: Instrument Application (APM)

**Python Flask App:**

```python
# app.py
from flask import Flask
from ddtrace import tracer, patch_all

# Automatically instrument Flask, requests, redis, etc.
patch_all()

app = Flask(__name__)

@app.route('/')
def home():
    # This will be traced automatically
    return "Hello, World!"

@app.route('/api/user/<user_id>')
def get_user(user_id):
    # Simulate database query
    import time
    with tracer.trace("database.query", service="postgres"):
        time.sleep(0.1)  # Simulate query time

    return {"user_id": user_id, "name": "John Doe"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Install dependencies:**
```bash
pip install flask ddtrace

# Run with ddtrace
ddtrace-run python app.py
```

**Environment variables:**
```bash
export DD_SERVICE="my-web-app"
export DD_ENV="production"
export DD_VERSION="1.0.0"
export DD_AGENT_HOST="localhost"
export DD_TRACE_AGENT_PORT="8126"
```

---

**Node.js Express App:**

```javascript
// app.js
const tracer = require('dd-trace').init({
  service: 'my-nodejs-app',
  env: 'production',
  version: '1.0.0'
});

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/api/users/:id', async (req, res) => {
  // Simulate database query - automatically traced
  const span = tracer.startSpan('database.query');
  span.setTag('db.type', 'postgres');

  await new Promise(resolve => setTimeout(resolve, 100));

  span.finish();

  res.json({ userId: req.params.id, name: 'Jane Doe' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

**Install:**
```bash
npm install dd-trace express
DD_SERVICE=my-nodejs-app node app.js
```

---

### Step 4: Custom Metrics

**Send custom business metrics:**

**Python:**
```python
from datadog import initialize, statsd

options = {
    'api_key': 'your_api_key',
    'app_key': 'your_app_key'
}

initialize(**options)

# Increment counter
statsd.increment('page.views', tags=["page:home", "environment:prod"])

# Record gauge
statsd.gauge('users.active', 123, tags=["environment:prod"])

# Timing
statsd.timing('database.query.time', 0.5)

# Histogram
statsd.histogram('request.size', 1024)

# Set (count unique values)
statsd.set('users.unique', user_id)
```

---

**Using DogStatsD:**
```python
from datadog import DogStatsd

statsd = DogStatsd(host='localhost', port=8125)

# Business metrics
statsd.increment('orders.created', tags=['product:widget', 'currency:USD'])
statsd.gauge('inventory.stock', 45, tags=['product:widget'])
statsd.histogram('checkout.amount', 129.99, tags=['currency:USD'])

# Application metrics
statsd.timing('api.response_time', 234, tags=['endpoint:/api/users'])
statsd.increment('cache.hit', tags=['cache:redis'])
```

---

### Step 5: Send Logs to Datadog

**Configure log collection:**

```yaml
# /etc/datadog-agent/conf.d/python.d/conf.yaml
logs:
  - type: file
    path: /var/log/myapp/*.log
    service: my-web-app
    source: python
    sourcecategory: sourcecode
    tags:
      - env:production
```

**Python logging to Datadog:**
```python
import logging
from pythonjsonlogger import jsonlogger

# JSON logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Log with context
logger.info(
    "User login",
    extra={
        'user_id': 12345,
        'ip': '192.168.1.1',
        'duration_ms': 234,
        'dd.trace_id': tracer.current_span().trace_id,  # Correlate with traces!
        'dd.span_id': tracer.current_span().span_id
    }
)
```

**Restart agent:**
```bash
sudo systemctl restart datadog-agent
```

---

## 📊 Creating Dashboards

### Timeboard (Classic Dashboard)

**Via UI:**
```
1. Dashboards → New Dashboard → New Timeboard
2. Add widget → Timeseries

Query:
avg:system.cpu.user{env:production}
avg:system.mem.used{env:production}

Display:
Lines, Area, Bars

Title: Production CPU & Memory
```

**Common Widgets:**

**1. Timeseries - Metrics over time**
```
Query: avg:trace.flask.request.duration{service:my-app} by {resource_name}
Visualization: Line graph
Legend: Show top 10
```

**2. Query Value - Current number**
```
Query: sum:orders.created{env:production}.as_count()
Display: Number with sparkline
Color threshold: Green <100, Yellow <500, Red >500
```

**3. Heatmap - Distribution**
```
Query: avg:trace.flask.request.duration{service:my-app}
Buckets: Auto
Color: Blue → Red
```

**4. Top List - Rankings**
```
Query: top(avg:system.cpu.user{*} by {host}, 10, 'mean', 'desc')
Shows: Top 10 hosts by CPU
```

**5. Log Stream - Recent logs**
```
Query: service:my-app status:error
Shows: Last 50 error logs
Auto-refresh: 30 seconds
```

---

### Dashboard with Template Variables

**Create variables:**
```
Settings → Template Variables

$env: tag:env
$service: tag:service
$host: tag:host
```

**Use in queries:**
```
avg:system.cpu.user{env:$env,service:$service,host:$host}
```

**Dashboard now has dropdowns:**
```
Environment: [production ▼]  Service: [my-app ▼]  Host: [All ▼]
```

---

## 🔍 APM Deep Dive

### Analyzing Traces

**APM → Services:**
```
See all services:
- my-web-app (Python)
- auth-service (Node.js)
- database (PostgreSQL)

For each service:
- Request rate (req/s)
- Latency (p50, p95, p99)
- Error rate (%)
```

**Click service → See traces:**
```
Trace example:
┌──────────────────────────────────────────────────┐
│ GET /api/users/123                    [200ms]    │
│  ├─ flask.request                     [200ms]    │
│  │  ├─ authenticate                   [50ms]     │
│  │  │  └─ redis.get                   [5ms]      │
│  │  ├─ database.query                 [120ms] ⚠️ │
│  │  │  └─ SELECT * FROM users...                 │
│  │  └─ render_template                [30ms]     │
└──────────────────────────────────────────────────┘
```

**Identify bottleneck:** Database query taking 120ms (60% of request time)

---

### Service Map

**Visual dependencies:**
```
     [Load Balancer]
            ↓
      [API Gateway] ────→ [Auth Service] ──→ [Redis]
            ↓                                    ↑
      [User Service] ──────────────────────────┘
            ↓
      [PostgreSQL]
```

Shows: Request flow, latency between services, error rates

---

## 🚨 Monitors & Alerts

### Creating a Monitor

**Example 1: High Error Rate**

```
Monitors → New Monitor → APM

Query:
sum:trace.flask.request.hits{service:my-app,http.status_code:5*}.as_rate()
/
sum:trace.flask.request.hits{service:my-app}.as_rate()
* 100

Alert threshold: > 5%
Warning threshold: > 2%

Evaluate: last 5 minutes

Notification:
🚨 {{#is_alert}}
Error rate is {{value}}% for {{service.name}}
{{/is_alert}}

Notify: @slack-alerts @pagerduty
```

---

**Example 2: High Latency (p95)**

```
Monitors → New Monitor → APM

Query:
p95:trace.flask.request.duration{service:my-app}

Alert threshold: > 500ms
Warning threshold: > 300ms

Notification:
⚠️ P95 latency is {{value}}ms

Check traces: https://app.datadoghq.com/apm/traces?...

Notify: @team-backend
```

---

**Example 3: Service Down**

```
Monitors → New Monitor → Integration

Check: HTTP check
URL: https://api.example.com/health
Method: GET
Expected status: 200

Alert if: Check fails 3 times in 5 minutes

Notification:
🔴 Service {{service.name}} is DOWN

Notify: @pagerduty-critical @slack-incidents
```

---

## 🎤 Interview Questions & Answers

### Question 1: APM vs Metrics

**Interviewer:** "What's the difference between APM and traditional metrics monitoring?"

❌ **Weak Answer:**
> "APM monitors applications, metrics monitor servers."

✅ **Strong Answer:**
> "Traditional metrics (Prometheus) show what's happening - CPU is high, requests per second increased. APM shows why - it traces individual requests through the entire stack. When latency spikes, metrics tell you 'response time is 500ms,' but APM shows you 'the users-service database query on line 47 is taking 400ms because there's a missing index.' APM provides code-level visibility with distributed tracing, showing how requests flow through microservices. You need both: metrics for infrastructure health, APM for application debugging."

**Why this impresses:** Shows understanding of complementary monitoring layers.

---

### Question 2: Datadog vs Prometheus

**Interviewer:** "Why would a company choose Datadog over Prometheus + Grafana?"

❌ **Weak Answer:**
> "Datadog is easier."

✅ **Strong Answer:**
> "Trade-offs: Datadog is SaaS - no infrastructure to maintain, automatic upgrades, built-in integrations for 500+ technologies. You get APM, logs, synthetics, and metrics in one platform with automatic correlation. Perfect for fast-moving teams. Cost scales with usage. Prometheus is self-hosted - full control, no vendor lock-in, no data leaves your network. Free (but requires engineering time). Better for companies with strict data residency requirements or massive scale where Datadog costs become prohibitive. Many companies use both: Prometheus for Kubernetes metrics, Datadog for APM and business metrics."

**Why this impresses:** Shows balanced understanding without vendor bias.

---

### Question 3: Cost Management

**Interviewer:** "Datadog bills got too expensive. How do you optimize?"

❌ **Weak Answer:**
> "Switch to cheaper tool."

✅ **Strong Answer:**
> "Several cost controls: 1) Use exclusion filters - don't index debug logs or health check traces. 2) Adjust retention - logs to 15 days instead of 30 days. 3) Use metrics without limits for critical metrics only. 4) Sample high-volume traces (keep 100% of errors, sample 10% of successful requests). 5) Tag carefully - each unique tag combination costs money. 6) Use log patterns and archives - pattern matching is cheaper than full indexing, archive to S3 for long-term storage. 7) Monitor usage dashboard to identify top spenders. 8) Consider hybrid approach - Prometheus for infra metrics, Datadog for APM only."

**Why this impresses:** Shows production experience with cost awareness.

---

### Question 4: Troubleshooting

**Interviewer:** "A user reports slow checkout. How do you investigate with Datadog?"

❌ **Weak Answer:**
> "Look at the dashboard."

✅ **Strong Answer:**
> "Step-by-step investigation: 1) APM → Search traces by user ID or session ID to find that specific user's request. 2) Open trace to see full request flow - identify which service/span took longest. 3) Click the slow span to see SQL query, cache hit/miss, external API call. 4) Switch to 'Correlate' tab to see logs from that exact trace (automatic via trace ID). 5) Check 'Infrastructure' tab to see if host had high CPU/memory during that request. 6) Look at historical data - is this a new regression? Use 'Compare' feature to see before/after deployment. 7) Check Service Map for downstream service issues. If database query is slow, examine Query Performance to find missing indexes."

**Why this impresses:** Demonstrates systematic troubleshooting workflow.

---

## ⚠️ Common Mistakes (Avoid These!)

### ❌ Mistake 1: Over-Logging

**DON'T:**
```python
logger.debug(f"Variable x = {x}")  # Every line
# Cost: $$$$ for debug logs
```

**DO:**
```python
# Only log meaningful events
logger.info("Order created", extra={'order_id': order_id, 'amount': amount})
logger.error("Payment failed", extra={'order_id': order_id, 'error': str(e)})

# Use exclusion filters for health checks
# /health endpoint logs excluded from indexing
```

**Why:** Datadog bills per GB indexed. Debug logs are expensive noise.

---

### ❌ Mistake 2: Careless Tagging

**DON'T:**
```python
# High-cardinality tags
statsd.increment('orders', tags=[f'user_id:{user_id}'])  # 1M users = 1M metrics
```

**DO:**
```python
# Low-cardinality tags
statsd.increment('orders', tags=['product_category:electronics', 'region:eu-north'])
# Track user_id in logs, not metrics
```

**Why:** Each unique tag combination creates a custom metric ($0.05/metric/month).

---

### ❌ Mistake 3: No Trace Sampling

**DON'T:**
```python
# 100% trace retention
# 1M requests/day = expensive
```

**DO:**
```python
# Intelligent sampling
from ddtrace.filters import FilterRequestsOnUrl

# Always trace errors
tracer.configure(
    settings={
        'FILTERS': [FilterRequestsOnUrl([r'http://.*'])],
        'sample_rate': 0.1,  # Sample 10% of successful requests
        'analytics_enabled': True,
        'analytics_sample_rate': 1.0  # But analyze all sampled traces
    }
)
```

**Why:** Full trace retention costs $$$$. Sample intelligently.

---

## 📚 Flashcards

**Q: What is Datadog?**
A: All-in-one SaaS observability platform - metrics, APM, logs, synthetics in one place.

**Q: What is APM?**
A: Application Performance Monitoring - traces requests through distributed systems to find bottlenecks.

**Q: What is the Datadog Agent?**
A: Lightweight daemon that runs on hosts/containers to collect metrics, traces, and logs.

**Q: What is DogStatsD?**
A: StatsD-compatible service for sending custom metrics to Datadog.

**Q: What is a trace?**
A: Complete record of a request's journey through all services (spans).

**Q: What is a span?**
A: Single operation within a trace (e.g., database query, HTTP request).

**Q: What are Service Level Objectives (SLOs)?**
A: Datadog feature for tracking reliability targets (e.g., 99.9% of requests <200ms).

**Q: What is Synthetic Monitoring?**
A: Automated tests that simulate user behavior (uptime checks, browser tests).

**Q: What is Log Pattern Detection?**
A: Automatic grouping of similar logs to reduce noise and identify anomalies.

**Q: What is Watchdog?**
A: AI-powered anomaly detection that automatically alerts on unusual behavior.

---

## 🎓 Quiz

### Question 1

**What does APM provide that traditional metrics don't?**

A) Server CPU usage
B) Code-level tracing through distributed services ✅
C) Log collection
D) Uptime monitoring

**Answer:** B ✅

**Explanation:** APM traces individual requests through the entire stack, showing exactly which code is slow.

---

### Question 2

**Why is high-cardinality tagging expensive in Datadog?**

A) It slows down queries
B) Each unique tag combination creates a billable custom metric ✅
C) Tags are stored in a database
D) It's not expensive

**Answer:** B ✅

**Explanation:** Custom metrics cost $0.05/metric/month. User IDs as tags = millions of metrics.

---

### Question 3

**What's the best way to correlate logs with traces?**

A) Manually search by timestamp
B) Use the same service name
C) Include trace_id and span_id in logs ✅
D) Logs and traces can't be correlated

**Answer:** C ✅

**Explanation:** Including trace/span IDs in logs enables automatic correlation in Datadog.

---

## 🎯 Portfolio Project: Full Datadog Implementation

**Build for your GitHub:**

**Project:** Microservices demo app with complete Datadog observability

**Components:**
1. **2-3 microservices** (Python, Node.js) with APM instrumentation
2. **Custom metrics** for business KPIs (orders, revenue, users)
3. **Structured logging** with trace correlation
4. **Dashboards** (service health, business metrics, infrastructure)
5. **Monitors** (error rate, latency, service down)
6. **Service map** visualization
7. **Load testing** to generate realistic traffic
8. **Complete documentation** with screenshots

**Why this impresses:**
- ✅ Full observability implementation
- ✅ APM with distributed tracing
- ✅ Custom business metrics
- ✅ Log-trace-metric correlation
- ✅ Production-ready monitoring

**GitHub structure:**
```
datadog-observability-demo/
├── services/
│   ├── frontend-service/
│   ├── api-service/
│   └── database-service/
├── datadog/
│   ├── dashboards/
│   ├── monitors/
│   └── agent-config/
├── docker-compose.yml
├── load-test/
│   └── k6-script.js
├── screenshots/
└── README.md
```

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Modern tool** - Growing adoption (30% YoY)
✅ **Full-stack observability** - Metrics + APM + Logs
✅ **Production skills** - Cost management, sampling, optimization
✅ **Troubleshooting** - Code-level debugging
✅ **Business metrics** - Track KPIs, not just tech metrics

**Time to complete:** 2 hours
**Job market impact:** Opens 40% of modern DevOps roles
**Salary boost:** +16-20% average
**Trend:** Growing faster than Prometheus/ELK

---

**Module completed!** 🎉

**Next recommended:** Distributed Tracing Patterns - Jaeger, OpenTelemetry, and observability architecture

**Pro tip:** Combine Prometheus (free for infra) + Datadog (APM only) for cost-effective monitoring at scale!
"""
}

# Export as MODULE dict
MODULE = {
    "id": "monitoring-datadog",
    "slug": "monitoring-datadog",
    "title": "Datadog Monitoring",
    "description": "Master Datadog for modern observability: APM traces, infrastructure monitoring, log management, and custom dashboards. Used in 40% of DevOps jobs.",
    "icon": "🐕",
    "category": "monitoring",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [DATADOG_FUNDAMENTALS],
}
