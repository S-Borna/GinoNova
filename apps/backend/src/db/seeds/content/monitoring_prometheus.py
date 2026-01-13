"""
Prometheus Monitoring - Production-Grade Observability
======================================================

Master Prometheus monitoring - the industry standard for metrics collection and alerting.
70% of DevOps jobs require Prometheus knowledge.

Coverage:
- PromQL queries and metrics
- Service discovery
- Alertmanager setup
- Exporters and instrumentation
- Grafana integration
"""

PROMETHEUS_FUNDAMENTALS = {
    "title": "Prometheus Fundamentals & PromQL",
    "slug": "prometheus-fundamentals",
    "description": "Learn Prometheus monitoring from scratch: metrics collection, PromQL queries, service discovery, and alerting. The foundation of modern observability.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Prometheus Fundamentals & PromQL

## 🎯 TL;DR (30 seconds)

Prometheus is a time-series database that collects metrics from your services automatically. Write PromQL queries
to analyze data, create alerts when things break, and visualize in Grafana. 70% of DevOps jobs use Prometheus.

**Why this matters:** Without monitoring, you're blind. Prometheus shows you CPU, memory, request rates, errors,
and latency - the golden signals every production system needs.

---

## 🚀 Why Prometheus for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 70% of DevOps Engineer roles require Prometheus
- 85% of SRE roles require Prometheus
- 65% of Platform Engineer roles require Prometheus

**Salary Impact (Sweden):**
| Role | Without Monitoring | With Prometheus | Difference |
|------|-------------------|----------------|------------|
| Junior DevOps | 38,000 SEK | 45,000 SEK | **+18%** |
| DevOps Engineer | 45,000 SEK | 54,000 SEK | **+20%** |
| Senior SRE | 60,000 SEK | 75,000 SEK | **+25%** |

**Companies using Prometheus:** SoundCloud (created it), DigitalOcean, Ericsson, Spotify, Reddit

---

## 📖 THEORY: What is Prometheus?

### The Problem It Solves

**Scenario: Your production app is slow**

❌ **Without Monitoring:**
```
User: "The site is slow!"
You: "Uhh... let me SSH to 20 servers and check?"
You: "CPU looks fine... memory ok... no idea what's wrong"
Boss: "How long has this been happening?"
You: "No clue 🤷"
*2 hours of random guessing*
```

✅ **With Prometheus:**
```
Alert: "API latency >500ms for 5 minutes"
You: Open Grafana dashboard
You: See database connection pool exhausted
You: Scale up database connections
Total time: 3 minutes ✅
```

---

### What Makes Prometheus Different

**Pull-based (not push-based):**
- Prometheus scrapes metrics from your services
- Services expose HTTP endpoint with metrics
- No agents to install on servers (mostly)

**Time-series database:**
```
http_requests_total{method="GET", status="200"} 12453 @1640000000
http_requests_total{method="GET", status="200"} 12789 @1640000060
http_requests_total{method="GET", status="200"} 13002 @1640000120
```
Each metric has labels (method, status) and timestamps.

**PromQL query language:**
```promql
# Request rate per second over last 5 minutes
rate(http_requests_total[5m])

# CPU usage per container
container_cpu_usage_seconds_total

# 99th percentile latency
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

---

## 🛠️ HANDS-ON: Your First Prometheus Setup

### Step 1: Install Prometheus

**Using Docker (easiest):**
```bash
# Create config directory
mkdir -p ~/prometheus
cd ~/prometheus

# Create prometheus.yml
cat > prometheus.yml <<EOF
global:
  scrape_interval: 15s  # Scrape metrics every 15 seconds

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']  # Monitor Prometheus itself
EOF

# Run Prometheus
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:latest

# Verify
curl http://localhost:9090/metrics
```

**Access Prometheus UI:**
```
Open: http://localhost:9090
```

---

### Step 2: Monitor a Node (Linux Server)

**Install Node Exporter (exposes system metrics):**
```bash
# Download
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz

# Extract and run
tar xvfz node_exporter-1.6.1.linux-amd64.tar.gz
cd node_exporter-1.6.1.linux-amd64
./node_exporter &

# Test metrics
curl http://localhost:9100/metrics
```

**Output:**
```
# HELP node_cpu_seconds_total Seconds the CPUs spent in each mode.
# TYPE node_cpu_seconds_total counter
node_cpu_seconds_total{cpu="0",mode="idle"} 23482.45
node_cpu_seconds_total{cpu="0",mode="system"} 1234.56
node_memory_MemAvailable_bytes 8.294912e+09
node_filesystem_free_bytes{device="/dev/sda1"} 4.234234e+10
```

**Add to Prometheus config:**
```yaml
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']  # Node Exporter
```

**Restart Prometheus:**
```bash
docker restart prometheus
```

**Query in Prometheus UI:**
```promql
# CPU usage percentage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Available memory in GB
node_memory_MemAvailable_bytes / 1024 / 1024 / 1024

# Disk usage percentage
100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)
```

---

### Step 3: Monitor a Web Application

**Example: Python Flask app with Prometheus client**

```python
# app.py
from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY
import time
import random

app = Flask(__name__)

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

@app.route('/')
def home():
    start_time = time.time()

    # Simulate some work
    time.sleep(random.uniform(0.01, 0.1))

    # Record metrics
    REQUEST_COUNT.labels(method='GET', endpoint='/', status='200').inc()
    REQUEST_LATENCY.labels(method='GET', endpoint='/').observe(time.time() - start_time)

    return "Hello, World!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Install dependencies:**
```bash
pip install flask prometheus-client
python app.py
```

**Check metrics:**
```bash
curl http://localhost:5000/metrics
```

**Add to Prometheus:**
```yaml
scrape_configs:
  - job_name: 'flask-app'
    static_configs:
      - targets: ['localhost:5000']
```

---

## 🎓 PromQL Mastery (Interview Essential)

### Basic Queries

**1. Instant Vector (current value):**
```promql
# Current CPU usage
node_cpu_seconds_total

# Requests in last 5 seconds
http_requests_total
```

**2. Range Vector (time range):**
```promql
# CPU data over last 5 minutes
node_cpu_seconds_total[5m]
```

**3. Rate (per-second rate):**
```promql
# HTTP requests per second
rate(http_requests_total[5m])

# CPU usage rate
rate(node_cpu_seconds_total{mode="idle"}[5m])
```

---

### Advanced Queries (Interview Gold)

**4. Aggregation:**
```promql
# Total requests across all servers
sum(rate(http_requests_total[5m]))

# Average CPU per server
avg by (instance) (rate(node_cpu_seconds_total{mode!="idle"}[5m]))

# Max memory usage
max by (pod) (container_memory_usage_bytes)
```

**5. Filtering:**
```promql
# Only 500 errors
rate(http_requests_total{status="500"}[5m])

# Specific endpoints
http_requests_total{endpoint=~"/api/.*"}  # Regex matching
```

**6. Percentiles (p95, p99):**
```promql
# 95th percentile latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# 99th percentile
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

**7. Error Rate:**
```promql
# Percentage of 5xx errors
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
* 100
```

---

## 🚨 Alertmanager Setup

**Create alertmanager.yml:**
```yaml
global:
  resolve_timeout: 5m

route:
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 12h
  receiver: 'slack'

receivers:
  - name: 'slack'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'
        channel: '#alerts'
        title: '{{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'
```

**Create alert rules (alerts.yml):**
```yaml
groups:
  - name: example
    interval: 30s
    rules:
      - alert: HighCPUUsage
        expr: 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is {{ $value }}%"

      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service {{ $labels.job }} is down"
          description: "{{ $labels.instance }} has been down for more than 1 minute"

      - alert: HighErrorRate
        expr: sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate"
          description: "Error rate is {{ $value | humanizePercentage }}"

      - alert: DiskSpaceLow
        expr: (node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100 < 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Low disk space on {{ $labels.instance }}"
          description: "Only {{ $value }}% disk space remaining"
```

---

## 🔍 Service Discovery (Auto-Discovery)

### Kubernetes Service Discovery

**Automatic discovery of pods:**
```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      # Only scrape pods with prometheus.io/scrape=true annotation
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      # Use custom port if specified
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
```

**Annotate your pods:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
```

---

### AWS EC2 Service Discovery

```yaml
scrape_configs:
  - job_name: 'aws-ec2'
    ec2_sd_configs:
      - region: eu-north-1
        port: 9100
        filters:
          - name: tag:monitoring
            values: [enabled]
```

---

## 📊 Common Exporters

**1. Node Exporter** - System metrics (CPU, memory, disk)
**2. cAdvisor** - Container metrics
**3. Blackbox Exporter** - HTTP/HTTPS/TCP probes
**4. PostgreSQL Exporter** - Database metrics
**5. Redis Exporter** - Cache metrics
**6. NGINX Exporter** - Web server metrics

**Example: Blackbox Exporter for website monitoring**
```yaml
scrape_configs:
  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
        - https://example.com
        - https://api.example.com
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: localhost:9115  # Blackbox exporter address
```

---

## 🎤 Interview Questions & Answers

### Question 1: Architecture

**Interviewer:** "Explain the Prometheus pull model. Why not push?"

❌ **Weak Answer:**
> "Prometheus pulls metrics from services."

✅ **Strong Answer:**
> "Prometheus uses a pull model where it scrapes HTTP endpoints at regular intervals. This has advantages: 1) Prometheus controls the scrape rate, preventing overload. 2) Services don't need to know where to push. 3) Easy to detect if a target is down - no metrics means service is down. 4) Can test endpoints manually with curl. The downside is services behind firewalls need push gateway, and short-lived jobs need special handling. But for long-running services, pull is simpler and more reliable."

**Why this impresses:** Shows understanding of trade-offs and architecture decisions.

---

### Question 2: PromQL

**Interviewer:** "Write a query to show the error rate as a percentage."

❌ **Weak Answer:**
> "Count the errors?"

✅ **Strong Answer:**
```promql
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
* 100
```
> "This calculates errors per second divided by total requests per second over 5 minutes, multiplied by 100 for percentage. The regex 5.. matches all 5xx status codes. I use rate() instead of increase() because rate gives per-second average, which is more stable for alerting."

**Why this impresses:** Demonstrates PromQL fluency and explains reasoning.

---

### Question 3: Troubleshooting

**Interviewer:** "Prometheus shows no data for a target. How do you debug?"

❌ **Weak Answer:**
> "Check if Prometheus is running?"

✅ **Strong Answer:**
> "First, check the Targets page in Prometheus UI to see the scrape error. Common issues: 1) Target down - verify service is running and port is open with `curl http://target:port/metrics`. 2) Wrong port in config. 3) Network/firewall blocking scrapes. 4) Metrics endpoint returns wrong content-type (needs text/plain). 5) Target takes >10s to respond (scrape timeout). Check Prometheus logs for scrape errors. If metrics work manually but not in Prometheus, check service discovery config and relabel rules."

**Why this impresses:** Shows systematic debugging approach and common failure modes.

---

### Question 4: Production Practice

**Interviewer:** "How do you prevent Prometheus from running out of disk space?"

❌ **Weak Answer:**
> "Buy more disk space?"

✅ **Strong Answer:**
> "Several approaches: 1) Set retention time: `--storage.tsdb.retention.time=15d` keeps only 15 days of data. 2) Set retention size: `--storage.tsdb.retention.size=50GB` limits total storage. 3) Reduce cardinality - avoid high-cardinality labels like user IDs or request IDs. 4) Decrease scrape frequency for low-priority targets. 5) Use recording rules to pre-aggregate expensive queries. 6) For long-term storage, use Thanos or Cortex to offload to S3. A single Prometheus instance should handle 10-15 days of data, then archive to remote storage."

**Why this impresses:** Shows production experience and multiple solution approaches.

---

## ⚠️ Common Mistakes (Avoid These!)

### ❌ Mistake 1: High-Cardinality Labels

**DON'T:**
```python
# BAD: User ID in label = millions of time series
REQUEST_COUNT.labels(user_id="12345", endpoint="/api").inc()
```

**DO:**
```python
# GOOD: Only low-cardinality labels
REQUEST_COUNT.labels(endpoint="/api", status="200").inc()
```

**Why:** Each unique label combination creates a new time series. Million users = million time series = Prometheus dies.

---

### ❌ Mistake 2: Using Gauges for Counters

**DON'T:**
```python
# BAD: Setting request count directly
REQUEST_GAUGE.set(12345)
```

**DO:**
```python
# GOOD: Increment counter
REQUEST_COUNT.inc()
```

**Why:** Counters can use rate() and increase(). Gauges can't. Use Counter for things that only go up.

---

### ❌ Mistake 3: Missing Rate Function

**DON'T:**
```promql
# BAD: Raw counter value is useless
http_requests_total
```

**DO:**
```promql
# GOOD: Rate shows requests per second
rate(http_requests_total[5m])
```

**Why:** Counter values are cumulative and reset. Rate converts to per-second speed.

---

## 📚 Flashcards

**Q: What is Prometheus?**
A: Open-source monitoring system with time-series database and powerful query language (PromQL).

**Q: Pull vs Push model?**
A: Prometheus pulls metrics from targets via HTTP scraping. Targets expose /metrics endpoint.

**Q: What is PromQL?**
A: Prometheus Query Language for querying time-series data.

**Q: What is a Counter?**
A: Metric that only goes up (requests, errors). Use with rate() function.

**Q: What is a Gauge?**
A: Metric that goes up and down (CPU, memory, temperature).

**Q: What is a Histogram?**
A: Metric that counts observations in buckets (latency percentiles).

**Q: What is rate()?**
A: Function that calculates per-second average rate of a counter.

**Q: What is Alertmanager?**
A: Component that handles alert routing, grouping, and notifications.

**Q: What is a target?**
A: Service that Prometheus scrapes for metrics.

**Q: What is an exporter?**
A: Program that exposes metrics from third-party systems (MySQL, Redis, etc).

---

## 🎓 Quiz

### Question 1

**What metric type should you use for counting HTTP requests?**

A) Gauge
B) Counter ✅
C) Histogram
D) Summary

**Answer:** B ✅

**Explanation:** Counters are for values that only increase. Use rate() to convert to requests per second.

---

### Question 2

**This PromQL query calculates what?**
```promql
rate(http_requests_total[5m])
```

A) Total requests in 5 minutes
B) Average requests per second over last 5 minutes ✅
C) Current request count
D) Request rate since Prometheus started

**Answer:** B ✅

**Explanation:** rate() calculates per-second average over the specified time range.

---

### Question 3

**Why should you avoid using user IDs as labels?**

A) User IDs are private data
B) High cardinality causes too many time series ✅
C) Labels can't contain numbers
D) PromQL doesn't support numeric labels

**Answer:** B ✅

**Explanation:** Each unique label combination creates a new time series. Millions of users = millions of series = performance disaster.

---

## 🎯 Portfolio Project: Complete Monitoring Stack

**Build for your GitHub:**

**Project:** Full-stack monitoring with Prometheus + Grafana

**Components:**
1. Python/Node.js web app with Prometheus metrics
2. Prometheus server with alerts
3. Grafana dashboards
4. Alertmanager with Slack notifications
5. Docker Compose setup

**Why this impresses:**
- ✅ Production-ready monitoring setup
- ✅ PromQL queries in dashboards
- ✅ Alerting configuration
- ✅ Complete documentation
- ✅ Infrastructure as code

**GitHub structure:**
```
prometheus-monitoring-stack/
├── app/
│   ├── Dockerfile
│   └── app.py (with metrics)
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.yml
├── grafana/
│   └── dashboards/
├── alertmanager/
│   └── config.yml
├── docker-compose.yml
└── README.md
```

---

## 🌟 Why This Module Prepares You for Jobs

✅ **PromQL mastery** - Write complex queries in interviews
✅ **Production setup** - You know the full stack
✅ **Alerting** - Understand when and how to alert
✅ **Best practices** - Avoid high-cardinality mistakes
✅ **Hands-on experience** - Real metrics from real apps

**Time to complete:** 2 hours
**Job market impact:** Opens 70% of DevOps roles
**Salary boost:** +18-20% average

---

**Module completed!** 🎉

**Next recommended:** Grafana Dashboards - Visualize your Prometheus data beautifully
"""
}

# Export as MODULE dict
MODULE = {
    "id": "monitoring-prometheus",
    "slug": "monitoring-prometheus",
    "title": "Prometheus Monitoring",
    "description": "Master Prometheus monitoring: PromQL queries, service discovery, alerting, and instrumentation. Required in 70% of DevOps jobs.",
    "icon": "📊",
    "category": "monitoring",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [PROMETHEUS_FUNDAMENTALS],
}
