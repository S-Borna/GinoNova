"""
Grafana Dashboards - Beautiful Data Visualization
==================================================

Master Grafana for creating stunning, actionable dashboards. The visualization layer
for Prometheus, Elasticsearch, and every major monitoring system.

Coverage:
- Dashboard creation and design
- Data sources (Prometheus, Elasticsearch, CloudWatch)
- Variables and templating
- Alerting rules
- Plugins and customization
"""

GRAFANA_FUNDAMENTALS = {
    "title": "Grafana Dashboard Mastery",
    "slug": "grafana-dashboards",
    "description": "Learn to build production-grade Grafana dashboards: data sources, variables, alerts, and beautiful visualizations that drive action.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Grafana Dashboard Mastery

## 🎯 TL;DR (30 seconds)

Grafana turns your monitoring data into beautiful, actionable dashboards. Connect to Prometheus, Elasticsearch,
or 100+ data sources. Build dashboards that show what's happening now and predict what will happen next.

**Why this matters:** Data without visualization is useless. Grafana makes monitoring data understandable
to engineers, managers, and executives. 65% of DevOps jobs require Grafana.

---

## 🚀 Why Grafana for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 65% of DevOps Engineer roles require Grafana
- 82% of SRE roles require Grafana
- 58% of Platform Engineer roles require Grafana

**Salary Impact (Sweden):**
| Role | Without Dashboards | With Grafana | Difference |
|------|-------------------|--------------|------------|
| Junior DevOps | 38,000 SEK | 44,000 SEK | **+16%** |
| DevOps Engineer | 45,000 SEK | 53,000 SEK | **+18%** |
| Senior SRE | 60,000 SEK | 72,000 SEK | **+20%** |

**Companies using Grafana:** PayPal, eBay, Bloomberg, Wikimedia, CERN, NASA

---

## 📖 THEORY: Why Grafana?

### The Visualization Problem

**Scenario: Your Prometheus has metrics but...**

❌ **Without Grafana:**
```
Manager: "What's our current request rate?"
You: Open Prometheus, write PromQL query
Manager: "What about yesterday? Last week?"
You: Write more queries...
Manager: "Can I see this myself?"
You: "Uh... let me send you screenshots?"
```

✅ **With Grafana:**
```
Manager: Opens dashboard URL
Dashboard shows:
- Current request rate: 2,345 req/s
- Trend graph showing last 24h
- P95 latency: 234ms
- Error rate: 0.02%
- All auto-refreshing every 5 seconds
Manager: "Perfect, thanks!" ✅
```

---

### What Makes Grafana Powerful

**1. Universal Connector**
- Prometheus, Elasticsearch, InfluxDB, MySQL, PostgreSQL, CloudWatch, Datadog
- One dashboard, multiple data sources

**2. Templating**
- Variables: Select environment (prod/staging) from dropdown
- One dashboard serves all use cases

**3. Alerting**
- Visual alerts with annotations
- Integrated with Slack, PagerDuty, email

**4. Sharing**
- Public dashboards, snapshots, embeds
- JSON export/import for version control

---

## 🛠️ HANDS-ON: Your First Dashboard

### Step 1: Install Grafana

**Using Docker:**
```bash
docker run -d \
  --name=grafana \
  -p 3000:3000 \
  -e GF_SECURITY_ADMIN_PASSWORD=admin \
  grafana/grafana:latest

# Access at http://localhost:3000
# Login: admin / admin
```

**Linux (production):**
```bash
# Add Grafana repository
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

# Install
sudo apt-get update
sudo apt-get install grafana

# Start service
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

---

### Step 2: Add Prometheus Data Source

**Via UI:**
```
1. Configuration (gear icon) → Data Sources
2. Add data source → Prometheus
3. URL: http://localhost:9090 (or your Prometheus URL)
4. Access: Server (default)
5. Save & Test
```

**Via API (automation):**
```bash
curl -X POST http://admin:admin@localhost:3000/api/datasources \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Prometheus",
    "type": "prometheus",
    "url": "http://prometheus:9090",
    "access": "proxy",
    "isDefault": true
  }'
```

---

### Step 3: Create Your First Dashboard

**Manual Creation:**
```
1. Create (+ icon) → Dashboard
2. Add new panel
3. Select metric: rate(http_requests_total[5m])
4. Panel title: "Request Rate"
5. Legend: {{method}} - {{status}}
6. Apply
7. Save dashboard (disk icon)
```

**PromQL Queries for Panels:**

**Panel 1: Request Rate**
```promql
sum(rate(http_requests_total[5m])) by (method, status)
```
Visualization: Time series graph

**Panel 2: Error Rate Percentage**
```promql
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
* 100
```
Visualization: Stat (single number)

**Panel 3: P95 Latency**
```promql
histogram_quantile(0.95,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
)
```
Visualization: Gauge

**Panel 4: CPU Usage**
```promql
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```
Visualization: Time series with threshold

---

## 🎨 Dashboard Design Best Practices

### Layout Strategy (TOP to BOTTOM)

**Level 1: Executive Summary (Row 1)**
```
┌────────────────────────────────────────────────────────┐
│  [Uptime: 99.9%]  [RPS: 2.3K]  [Errors: 0.02%]        │
│  Big numbers, single stat panels, GREEN = good        │
└────────────────────────────────────────────────────────┘
```

**Level 2: Key Metrics (Row 2)**
```
┌─────────────────────┐  ┌─────────────────────┐
│  Request Rate       │  │  Error Rate         │
│  (time series)      │  │  (time series)      │
└─────────────────────┘  └─────────────────────┘
```

**Level 3: Detailed Breakdowns (Rows 3+)**
```
┌──────────────────────────────────────────────────────┐
│  Requests by Endpoint (bar chart)                    │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│  Latency Heatmap                                      │
└──────────────────────────────────────────────────────┘
```

---

### Golden Signals Dashboard

**Every production service needs these 4 metrics:**

**1. Latency** - How fast?
```promql
histogram_quantile(0.95,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
)
```

**2. Traffic** - How much?
```promql
sum(rate(http_requests_total[5m]))
```

**3. Errors** - How many failures?
```promql
sum(rate(http_requests_total{status=~"5.."}[5m]))
```

**4. Saturation** - How full?
```promql
# CPU
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory
100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)

# Disk
100 - (node_filesystem_avail_bytes / node_filesystem_size_bytes * 100)
```

---

## 🔧 Variables & Templating (Production Essential)

### Why Variables?

**Without variables:**
- 10 environments = 10 separate dashboards
- 50 services = 50 dashboards
- Total: 500 dashboards to maintain 😱

**With variables:**
- 1 dashboard with dropdowns
- Select environment, service, region dynamically
- Maintain 1 dashboard ✅

---

### Creating Variables

**Variable 1: Environment**
```
Settings → Variables → Add variable

Name: env
Type: Query
Data source: Prometheus
Query: label_values(http_requests_total, environment)
```

**Variable 2: Service**
```
Name: service
Type: Query
Query: label_values(http_requests_total{environment="$env"}, service)
```

**Variable 3: Instance**
```
Name: instance
Type: Query
Query: label_values(http_requests_total{environment="$env",service="$service"}, instance)
```

**Use in queries:**
```promql
# Instead of hardcoded
rate(http_requests_total{environment="production",service="api"}[5m])

# Use variables
rate(http_requests_total{environment="$env",service="$service"}[5m])
```

**Dashboard now has dropdowns:**
```
Environment: [Production ▼]  Service: [api ▼]  Instance: [All ▼]
```

---

## 🚨 Grafana Alerting

### Creating an Alert

**Panel Alert (simple):**
```
1. Edit panel
2. Alert tab
3. Create Alert

Conditions:
- WHEN avg() OF query(A, 5m, now) IS ABOVE 80

Notifications:
- Send to: Slack
```

**Alert Rule (advanced, Grafana 9+):**
```yaml
# Alert: High Error Rate
Evaluate: every 1m for 5m

PromQL:
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
* 100
> 5

Annotations:
  Summary: High error rate detected
  Description: Error rate is {{ $values.A }}%

Labels:
  severity: critical
  team: backend
```

---

### Notification Channels

**Slack Integration:**
```bash
# In Grafana UI:
Alerting → Contact points → New contact point

Type: Slack
Webhook URL: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
Channel: #alerts
Message:
  🚨 {{ .Labels.alertname }}
  Severity: {{ .Labels.severity }}
  {{ .Annotations.description }}
```

**PagerDuty Integration:**
```
Type: PagerDuty
Integration Key: YOUR_PAGERDUTY_KEY
Auto resolve: Yes
```

---

## 📊 Advanced Panel Types

### 1. Stat Panel (Single Number)
**Use for:** Current value, KPIs
```promql
sum(rate(http_requests_total[5m]))
```
**Options:**
- Color thresholds: Green <100, Yellow <500, Red >500
- Sparkline: Show trend
- Unit: requests/sec

---

### 2. Gauge Panel
**Use for:** Percentage, saturation
```promql
100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)
```
**Options:**
- Min: 0, Max: 100
- Thresholds: Green <70, Yellow <85, Red >85

---

### 3. Bar Chart
**Use for:** Comparison, top-N
```promql
topk(10, sum by (endpoint) (rate(http_requests_total[5m])))
```

---

### 4. Heatmap
**Use for:** Latency distribution over time
```promql
sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
```

---

### 5. Table
**Use for:** Detailed listings
```promql
sum by (instance, version) (up)
```
**Columns:** Instance, Version, Status

---

### 6. Logs Panel
**Use for:** Correlating metrics with logs
```
Data source: Loki
Query: {job="app"} |= "error"
```

---

## 🎓 Real-World Dashboard Examples

### Dashboard 1: Kubernetes Cluster Overview

**Panels:**
```yaml
Row 1: Cluster Stats
  - Total Nodes (stat)
  - Total Pods (stat)
  - CPU Usage % (gauge)
  - Memory Usage % (gauge)

Row 2: Resource Usage
  - CPU Usage by Node (time series)
  - Memory Usage by Node (time series)

Row 3: Pod Status
  - Running Pods (time series)
  - Failed Pods (time series)
  - Pod Restarts (table)

Row 4: Network
  - Network I/O (time series)
  - DNS Queries (time series)
```

---

### Dashboard 2: Web Application Performance

**Panels:**
```yaml
Row 1: Health
  - Uptime (stat)
  - Request Rate (stat)
  - Error Rate % (stat)
  - P95 Latency (stat)

Row 2: Traffic
  - Requests per second (time series)
  - Requests by method GET/POST (time series)

Row 3: Errors
  - Error rate % (time series)
  - Error count by endpoint (bar chart)
  - Recent errors (logs panel)

Row 4: Performance
  - Latency heatmap
  - P50/P95/P99 latency (time series)
  - Slowest endpoints (table)

Row 5: Infrastructure
  - CPU usage (time series)
  - Memory usage (time series)
  - Database connections (time series)
```

---

### Dashboard 3: Database Monitoring

```yaml
Row 1: Overview
  - Connections (stat)
  - Queries/sec (stat)
  - Cache Hit Ratio (gauge)
  - Replication Lag (stat)

Row 2: Performance
  - Query duration (time series)
  - Slow queries (table)
  - Lock wait time (time series)

Row 3: Resources
  - CPU usage (time series)
  - Memory usage (time series)
  - Disk I/O (time series)
```

---

## 🎤 Interview Questions & Answers

### Question 1: Dashboard Design

**Interviewer:** "How do you design an effective dashboard?"

❌ **Weak Answer:**
> "Add graphs for all metrics."

✅ **Strong Answer:**
> "Follow the inverted pyramid: Top row has single-stat panels showing overall health - executives can glance and leave. Middle rows have time-series graphs for engineers investigating issues. Bottom rows have detailed tables and breakdowns. Use the Golden Signals framework: Latency, Traffic, Errors, Saturation. Apply RED (Rate, Errors, Duration) or USE (Utilization, Saturation, Errors) methodology. Keep dashboards focused - one dashboard per service, not one mega-dashboard. Use variables for environment/service selection."

**Why this impresses:** Shows understanding of user personas and monitoring frameworks.

---

### Question 2: Variables

**Interviewer:** "Why use variables in dashboards?"

❌ **Weak Answer:**
> "To make dashboards dynamic."

✅ **Strong Answer:**
> "Variables prevent dashboard sprawl. Without variables, you need separate dashboards for each environment, service, and region - that's 5 envs × 50 services × 3 regions = 750 dashboards to maintain. With variables, you have 1 dashboard with dropdowns. Variables also enable multi-select (compare multiple services side-by-side) and enable users to self-serve data without creating new dashboards. For teams, this means less maintenance and more consistency."

**Why this impresses:** Demonstrates scaling and maintenance considerations.

---

### Question 3: Alerting

**Interviewer:** "Grafana vs Prometheus Alertmanager for alerting?"

❌ **Weak Answer:**
> "Both do alerts, so either works."

✅ **Strong Answer:**
> "They serve different purposes. Prometheus Alertmanager is better for metrics-based alerts that need sophisticated routing, grouping, and deduplication. It's PromQL-native and handles alert state tracking across Prometheus restarts. Grafana alerting is better when you need to alert on multiple data sources (combine Prometheus and Elasticsearch queries), or when you want unified alert management with visualization. In production, many teams use Prometheus Alertmanager for critical infrastructure alerts, and Grafana for business metrics and cross-datasource alerts."

**Why this impresses:** Shows nuanced understanding of tool trade-offs.

---

### Question 4: Performance

**Interviewer:** "Your dashboard is loading slowly. How do you optimize?"

❌ **Weak Answer:**
> "Add more servers."

✅ **Strong Answer:**
> "Several optimizations: 1) Reduce time range - loading 30 days of data is slow, default to 6 hours. 2) Limit query resolution - use $__interval variable to prevent querying every second over 24 hours. 3) Use recording rules in Prometheus for expensive queries. 4) Reduce panel count - 50 panels means 50 queries every refresh. 5) Increase refresh interval - 5s is usually overkill, use 30s or 1m. 6) Cache data source queries when possible. 7) Use the Query Inspector to find slow queries and optimize PromQL. The root cause is usually too much data or too many queries."

**Why this impresses:** Shows performance troubleshooting methodology.

---

## ⚠️ Common Mistakes (Avoid These!)

### ❌ Mistake 1: Dashboard Overload

**DON'T:**
```
One dashboard with 100 panels showing everything
```

**DO:**
```
Focused dashboards:
- Infrastructure Overview (top-level)
- Service Dashboard (per service)
- Database Dashboard (per database)
Link related dashboards
```

**Why:** Cognitive overload. Users can't process 100 graphs.

---

### ❌ Mistake 2: Meaningless Alerts

**DON'T:**
```
Alert: CPU > 50% for 1 minute
(fires 50 times/day, everyone ignores)
```

**DO:**
```
Alert: CPU > 90% for 10 minutes
(actionable, indicates real problem)
```

**Why:** Alert fatigue destroys on-call culture.

---

### ❌ Mistake 3: Hard-Coded Values

**DON'T:**
```promql
rate(http_requests_total{service="api",env="prod"}[5m])
```

**DO:**
```promql
rate(http_requests_total{service="$service",env="$env"}[5m])
```

**Why:** Reusability. One dashboard for all environments.

---

## 📚 Flashcards

**Q: What is Grafana?**
A: Visualization platform for creating dashboards from multiple data sources (Prometheus, Elasticsearch, etc).

**Q: What are Grafana variables?**
A: Dynamic dropdown values that make dashboards reusable across environments/services.

**Q: What are the Golden Signals?**
A: Latency, Traffic, Errors, Saturation - the 4 key metrics for any service.

**Q: What is a Stat panel?**
A: Single-value panel showing current metric value with optional sparkline and thresholds.

**Q: What is a Gauge panel?**
A: Circular gauge showing percentage/ratio with color thresholds.

**Q: How do you share dashboards?**
A: Dashboard JSON export, snapshot URLs, or embed codes for public dashboards.

**Q: What data sources does Grafana support?**
A: Prometheus, Elasticsearch, InfluxDB, MySQL, PostgreSQL, CloudWatch, and 100+ more.

**Q: What is dashboard as code?**
A: Storing dashboard JSON in Git for version control and automation.

**Q: What is a mixed data source query?**
A: Panel that combines data from multiple sources (e.g., Prometheus + Elasticsearch).

**Q: What is annotation in Grafana?**
A: Visual markers on graphs showing events like deployments, incidents, releases.

---

## 🎓 Quiz

### Question 1

**What panel type should you use to show current request rate as a single number?**

A) Time series
B) Stat ✅
C) Gauge
D) Heatmap

**Answer:** B ✅

**Explanation:** Stat panels display single values prominently, perfect for current metrics.

---

### Question 2

**Why use variables in dashboards?**

A) They make dashboards load faster
B) They allow one dashboard to serve multiple environments ✅
C) They are required by Grafana
D) They improve graph resolution

**Answer:** B ✅

**Explanation:** Variables enable dynamic filtering, reducing dashboard sprawl.

---

### Question 3

**What are the Golden Signals?**

A) HTTP status codes
B) CPU, Memory, Disk, Network
C) Latency, Traffic, Errors, Saturation ✅
D) Uptime, Downtime, SLA, SLO

**Answer:** C ✅

**Explanation:** The four key metrics that matter for monitoring any user-facing system.

---

## 🎯 Portfolio Project: Production Dashboard Set

**Build for your GitHub:**

**Project:** Complete Grafana dashboard collection for microservices

**Deliverables:**
1. **Infrastructure Dashboard** - Kubernetes cluster overview
2. **Application Dashboard** - Golden signals per service
3. **Database Dashboard** - PostgreSQL/MySQL metrics
4. **Business Dashboard** - Revenue, signups, conversions
5. **JSON files** in Git for IaC
6. **Documentation** with screenshots

**Why this impresses:**
- ✅ Production-ready dashboards
- ✅ Multiple data sources
- ✅ Variables and templating
- ✅ Proper dashboard hierarchy
- ✅ Documentation

**GitHub structure:**
```
grafana-dashboards/
├── dashboards/
│   ├── infrastructure.json
│   ├── application.json
│   ├── database.json
│   └── business.json
├── datasources/
│   └── prometheus.yml
├── screenshots/
│   └── *.png
├── docker-compose.yml
└── README.md
```

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Dashboard design** - Create actionable visualizations
✅ **Variables mastery** - Build scalable dashboards
✅ **Multi-source** - Prometheus + Elasticsearch + more
✅ **Alerting** - Integrate with incident response
✅ **Best practices** - Golden Signals, RED, USE methods

**Time to complete:** 2 hours
**Job market impact:** Opens 65% of DevOps roles
**Salary boost:** +16-18% average

---

**Module completed!** 🎉

**Next recommended:** ELK Stack - Master log aggregation and analysis
"""
}

# Export as MODULE dict
MODULE = {
    "id": "monitoring-grafana",
    "slug": "monitoring-grafana",
    "title": "Grafana Dashboards",
    "description": "Master Grafana for beautiful monitoring dashboards: data sources, variables, alerting, and production-ready visualizations. Required in 65% of DevOps jobs.",
    "icon": "📈",
    "category": "monitoring",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [GRAFANA_FUNDAMENTALS],
}
