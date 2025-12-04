# =============================================================================
# KUBERNETES MASTERY - BLOCK 5 PART 2: LOGGING, MONITORING & BEST PRACTICES
# Noder 19-20 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 5 PART 2 - OBSERVABILITY & PRODUCTION
=======================================================
Node 19: Logging & Monitoring - Observability
Node 20: Production Best Practices - Checklista
"""

NODE_19 = {
    "id": "k8s_node_19",
    "title": "Logging & Monitoring - Observability",
    "slug": "logging-monitoring-observability",
    "content": r'''# 📊 Logging & Monitoring - Observability

## 1. Introduktion & Kontext

Observability i Kubernetes består av tre pelare: Logs, Metrics, och Traces. Tillsammans ger de fullständig insikt i ditt klusters och dina applikationers hälsa.

### Three Pillars of Observability

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   THREE PILLARS OF OBSERVABILITY                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │                         LOGS                                        │ │
│  │  "Vad hände?"                                                       │ │
│  │                                                                     │ │
│  │  • Container stdout/stderr                                          │ │
│  │  • Kubernetes events                                                │ │
│  │  • Audit logs                                                       │ │
│  │                                                                     │ │
│  │  Tools: ELK Stack, Loki, Fluentd, CloudWatch                       │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │                        METRICS                                      │ │
│  │  "Hur mår systemet?"                                                │ │
│  │                                                                     │ │
│  │  • CPU, Memory, Disk usage                                          │ │
│  │  • Request rate, latency, errors                                    │ │
│  │  • Custom business metrics                                          │ │
│  │                                                                     │ │
│  │  Tools: Prometheus, Grafana, Datadog, CloudWatch                   │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │                        TRACES                                       │ │
│  │  "Hur flödar requests?"                                             │ │
│  │                                                                     │ │
│  │  • Distributed tracing                                              │ │
│  │  • Request path through services                                    │ │
│  │  • Latency breakdown                                                │ │
│  │                                                                     │ │
│  │  Tools: Jaeger, Zipkin, OpenTelemetry                              │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Kubernetes Logging

### Log Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   KUBERNETES LOG ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  POD                                                              │  │
│  │  ┌─────────────────────────────────────────────────────────────┐ │  │
│  │  │  Container                                                   │ │  │
│  │  │  ┌───────────────────────────────────────────────────────┐  │ │  │
│  │  │  │  Application                                          │  │ │  │
│  │  │  │  console.log("Hello")  ──▶  stdout                    │  │ │  │
│  │  │  │  console.error("Error") ──▶  stderr                   │  │ │  │
│  │  │  └───────────────────────────────────────────────────────┘  │ │  │
│  │  └─────────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                              │                                          │
│                              ▼                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  NODE                                                             │  │
│  │  Container Runtime (containerd/docker)                            │  │
│  │            │                                                      │  │
│  │            ▼                                                      │  │
│  │  /var/log/pods/<namespace>_<pod>_<uid>/<container>/0.log         │  │
│  │  /var/log/containers/<pod>_<ns>_<container>-<id>.log             │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                              │                                          │
│                              ▼                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  LOG AGGREGATOR (DaemonSet)                                       │  │
│  │  Fluentd / Fluent Bit / Filebeat                                  │  │
│  │  • Läser logs från /var/log                                       │  │
│  │  • Parsar och enrichar                                            │  │
│  │  • Skickar till central storage                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                              │                                          │
│                              ▼                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  CENTRAL LOG STORAGE                                              │  │
│  │  Elasticsearch / Loki / CloudWatch Logs                           │  │
│  │                      │                                             │  │
│  │                      ▼                                             │  │
│  │  VISUALIZATION: Kibana / Grafana                                  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Kubectl Logs

```bash
# Basic logs
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container-name>

# Follow logs (live)
kubectl logs -f <pod-name>

# Previous container (efter restart)
kubectl logs <pod-name> --previous

# Last N lines
kubectl logs <pod-name> --tail=100

# Since timestamp
kubectl logs <pod-name> --since=1h
kubectl logs <pod-name> --since-time=2024-01-01T00:00:00Z

# All pods med label
kubectl logs -l app=myapp --all-containers

# Multi-container pod
kubectl logs <pod-name> --all-containers=true
```

## 3. Prometheus Monitoring

### Prometheus Architecture

```yaml
# Prometheus deployment (simplified)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      serviceAccountName: prometheus
      containers:
        - name: prometheus
          image: prom/prometheus:v2.47.0
          args:
            - "--config.file=/etc/prometheus/prometheus.yml"
            - "--storage.tsdb.path=/prometheus"
            - "--web.enable-lifecycle"
          ports:
            - containerPort: 9090
          volumeMounts:
            - name: config
              mountPath: /etc/prometheus
            - name: storage
              mountPath: /prometheus
      volumes:
        - name: config
          configMap:
            name: prometheus-config
        - name: storage
          emptyDir: {}
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s

    scrape_configs:
      # Kubernetes API server
      - job_name: 'kubernetes-apiservers'
        kubernetes_sd_configs:
          - role: endpoints
        scheme: https
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        authorization:
          credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
        relabel_configs:
          - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
            action: keep
            regex: default;kubernetes;https

      # Kubernetes nodes
      - job_name: 'kubernetes-nodes'
        kubernetes_sd_configs:
          - role: node
        scheme: https
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        authorization:
          credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token

      # Pods with prometheus.io/scrape annotation
      - job_name: 'kubernetes-pods'
        kubernetes_sd_configs:
          - role: pod
        relabel_configs:
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
            action: keep
            regex: true
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
            action: replace
            target_label: __metrics_path__
            regex: (.+)
```

### Application Metrics

```python
# Python app with Prometheus metrics
from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest

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
    with REQUEST_LATENCY.labels('GET', '/').time():
        REQUEST_COUNT.labels('GET', '/', '200').inc()
        return "Hello World"

@app.route('/metrics')
def metrics():
    return generate_latest()
```

```yaml
# Pod with Prometheus annotations
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
spec:
  containers:
    - name: myapp
      image: myapp:v1
      ports:
        - containerPort: 8080
```

## 4. Praktiska Övningar

### Övning 1: Loki + Grafana Logging

```bash
# Install Loki stack med Helm
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install loki grafana/loki-stack \
  --namespace logging \
  --create-namespace \
  --set grafana.enabled=true \
  --set prometheus.enabled=true

# Get Grafana password
kubectl get secret loki-grafana -n logging -o jsonpath="{.data.admin-password}" | base64 --decode

# Port forward Grafana
kubectl port-forward svc/loki-grafana -n logging 3000:80

# Open http://localhost:3000
# Add Loki as data source
# Query: {namespace="default"}
```

### Övning 2: Prometheus Queries

```bash
# Port forward Prometheus
kubectl port-forward svc/prometheus -n monitoring 9090:9090

# PromQL queries:

# CPU usage by pod
sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m])) by (pod)

# Memory usage
container_memory_usage_bytes{namespace="default"}

# HTTP request rate
rate(http_requests_total[5m])

# 99th percentile latency
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Pod restart count
sum(kube_pod_container_status_restarts_total) by (pod)
```

### Övning 3: Alerting Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: app-alerts
  namespace: monitoring
spec:
  groups:
    - name: app
      rules:
        - alert: HighErrorRate
          expr: |
            sum(rate(http_requests_total{status=~"5.."}[5m]))
            / sum(rate(http_requests_total[5m])) > 0.05
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "High error rate detected"
            description: "Error rate is {{ $value | humanizePercentage }}"

        - alert: PodCrashLooping
          expr: |
            rate(kube_pod_container_status_restarts_total[15m]) > 0
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "Pod {{ $labels.pod }} is crash looping"
```

## 5. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                OBSERVABILITY BEST PRACTICES                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Logging                                                              │
│     □ Logga till stdout/stderr (inte filer)                            │
│     □ Strukturerade logs (JSON)                                        │
│     □ Inkludera request ID för tracing                                 │
│     □ Rätt log levels (debug, info, warn, error)                       │
│                                                                          │
│  ✅ Metrics                                                              │
│     □ RED method: Rate, Errors, Duration                               │
│     □ USE method: Utilization, Saturation, Errors                      │
│     □ Custom business metrics                                          │
│     □ Cardinality-aware labels                                         │
│                                                                          │
│  ✅ Alerting                                                            │
│     □ Alert på symptoms, inte orsaker                                  │
│     □ Actionable alerts                                                │
│     □ Undvik alert fatigue                                             │
│     □ Runbooks för varje alert                                         │
│                                                                          │
│  ✅ Dashboards                                                          │
│     □ Golden signals overview                                          │
│     □ Service-specifika dashboards                                     │
│     □ Infrastructure dashboards                                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6-14. Sammanfattning & Task

### Observability Stack Recommendations

| Need | Tool | Purpose |
|------|------|---------|
| Metrics | Prometheus + Grafana | Time-series data |
| Logs | Loki / ELK | Log aggregation |
| Traces | Jaeger | Distributed tracing |
| All-in-one | Datadog / New Relic | SaaS solution |

---

**Nästa Node:** Production Best Practices →
''',
    "xp_reward": 160,
    "estimated_minutes": 60,
    "prerequisites": ["k8s_node_18"],
    "learning_outcomes": [
        "Förstå observability pillars",
        "Implementera centraliserad logging",
        "Konfigurera Prometheus metrics",
        "Sätta upp alerting rules"
    ]
}

NODE_20 = {
    "id": "k8s_node_20",
    "title": "Production Best Practices - Checklista",
    "slug": "production-best-practices-checklist",
    "content": r'''# ✅ Production Best Practices - Checklista

## 1. Introduktion & Kontext

Den här noden sammanfattar alla kritiska best practices för att köra Kubernetes i produktion. Använd detta som en checklista före varje produktions-deploy.

### Production Readiness Checklist

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PRODUCTION READINESS CHECKLIST                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │  TIER 1: MUST HAVE (Critical)                                       │ │
│  │  ─────────────────────────────────────────────────────────────────  │ │
│  │  □ Resource requests & limits                                       │ │
│  │  □ Liveness & Readiness probes                                     │ │
│  │  □ Multiple replicas (replicas >= 2)                               │ │
│  │  □ Pod Disruption Budget                                            │ │
│  │  □ Secrets management (ej plaintext)                               │ │
│  │  □ Network Policies                                                 │ │
│  │  □ RBAC & ServiceAccount                                           │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │  TIER 2: SHOULD HAVE (Important)                                    │ │
│  │  ─────────────────────────────────────────────────────────────────  │ │
│  │  □ Horizontal Pod Autoscaler                                        │ │
│  │  □ Pod Anti-Affinity                                                │ │
│  │  □ Topology Spread Constraints                                      │ │
│  │  □ Security Context (non-root, read-only fs)                       │ │
│  │  □ Centralized logging                                              │ │
│  │  □ Prometheus metrics                                               │ │
│  │  □ Alerting rules                                                   │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │  TIER 3: NICE TO HAVE (Optimization)                                │ │
│  │  ─────────────────────────────────────────────────────────────────  │ │
│  │  □ Priority Classes                                                 │ │
│  │  □ Pod Topology Spread                                              │ │
│  │  □ Vertical Pod Autoscaler (recommendations)                        │ │
│  │  □ Cost optimization                                                │ │
│  │  □ FinOps practices                                                 │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Complete Production Deployment

```yaml
# production-deployment.yaml - Full example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
  labels:
    app: myapp
    version: v1.0.0
spec:
  replicas: 3                        # ✅ Multiple replicas

  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0              # ✅ Zero downtime deploy

  selector:
    matchLabels:
      app: myapp

  template:
    metadata:
      labels:
        app: myapp
        version: v1.0.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      # ✅ ServiceAccount (ej default)
      serviceAccountName: myapp

      # ✅ Security Context
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000

      # ✅ Pod Anti-Affinity
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app: myapp
                topologyKey: kubernetes.io/hostname

      # ✅ Topology Spread
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app: myapp

      containers:
        - name: myapp
          image: mycompany/myapp:v1.0.0
          imagePullPolicy: IfNotPresent

          # ✅ Security Context (container-level)
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL

          ports:
            - name: http
              containerPort: 8080

          # ✅ Resource Requests & Limits
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi

          # ✅ Environment från Secrets/ConfigMaps
          envFrom:
            - configMapRef:
                name: myapp-config
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: myapp-secrets
                  key: database-url

          # ✅ Startup Probe (för slow-starting apps)
          startupProbe:
            httpGet:
              path: /healthz
              port: http
            failureThreshold: 30
            periodSeconds: 10

          # ✅ Liveness Probe
          livenessProbe:
            httpGet:
              path: /healthz
              port: http
            initialDelaySeconds: 0
            periodSeconds: 10
            timeoutSeconds: 3
            failureThreshold: 3

          # ✅ Readiness Probe
          readinessProbe:
            httpGet:
              path: /ready
              port: http
            initialDelaySeconds: 0
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3

          volumeMounts:
            - name: tmp
              mountPath: /tmp
            - name: cache
              mountPath: /app/cache

      volumes:
        - name: tmp
          emptyDir: {}
        - name: cache
          emptyDir: {}

      terminationGracePeriodSeconds: 30
---
# ✅ Service
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: production
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
    - name: http
      port: 80
      targetPort: http
---
# ✅ Pod Disruption Budget
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
  namespace: production
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: myapp
---
# ✅ Horizontal Pod Autoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
---
# ✅ Network Policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: myapp-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - port: http
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - port: 5432
    # DNS
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - port: 53
          protocol: UDP
```

## 3. Security Checklist

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      SECURITY CHECKLIST                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  POD SECURITY                                                            │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ runAsNonRoot: true                                                   │
│  □ readOnlyRootFilesystem: true                                         │
│  □ allowPrivilegeEscalation: false                                      │
│  □ capabilities: drop ALL                                               │
│  □ Ingen hostNetwork, hostPID, hostIPC                                  │
│  □ Secrets via secretKeyRef (ej env i plaintext)                        │
│                                                                          │
│  RBAC                                                                    │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ Dedicated ServiceAccount per app                                     │
│  □ Minimala permissions (least privilege)                               │
│  □ Inga cluster-admin bindings för apps                                 │
│  □ Regular audit av RoleBindings                                        │
│                                                                          │
│  NETWORK                                                                 │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ Default deny NetworkPolicy                                           │
│  □ Explicit allow rules                                                 │
│  □ Namespace isolation                                                  │
│  □ TLS för all intern kommunikation                                     │
│                                                                          │
│  IMAGE SECURITY                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ Trusted base images                                                  │
│  □ Image scanning i CI/CD                                               │
│  □ No :latest tags                                                      │
│  □ Image pull policy: IfNotPresent eller Always                         │
│  □ Private registry med authentication                                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Disaster Recovery

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      DISASTER RECOVERY                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  BACKUP                                                                  │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ etcd backup (cluster state)                                          │
│  □ PersistentVolume snapshots                                           │
│  □ Database backups                                                     │
│  □ Secrets backup (encrypted)                                           │
│  □ GitOps - all manifests i Git                                         │
│                                                                          │
│  HIGH AVAILABILITY                                                       │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ Multi-AZ deployment                                                  │
│  □ Pod anti-affinity                                                    │
│  □ Multiple replicas                                                    │
│  □ Database replication                                                 │
│  □ Load balancer health checks                                          │
│                                                                          │
│  TESTING                                                                 │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ Regular backup restore tests                                         │
│  □ Chaos engineering                                                    │
│  □ Failover drills                                                      │
│  □ Documented runbooks                                                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 5. Cost Optimization

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      COST OPTIMIZATION                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  RIGHT-SIZING                                                           │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ VPA recommendations för resource requests                            │
│  □ Rightsized node pools                                                │
│  □ Resource quotas per namespace                                        │
│  □ LimitRanges för defaults                                             │
│                                                                          │
│  AUTOSCALING                                                            │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ HPA baserat på actual load                                           │
│  □ Cluster autoscaler                                                   │
│  □ Scale to zero för dev/staging                                        │
│  □ Scheduled scaling för predictable load                               │
│                                                                          │
│  SPOT/PREEMPTIBLE                                                       │
│  ─────────────────────────────────────────────────────────────────────  │
│  □ Spot instances för fault-tolerant workloads                          │
│  □ Mixed on-demand + spot node pools                                    │
│  □ Proper PDB för spot termination                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6. Pre-Deploy Checklist

```bash
#!/bin/bash
# pre-deploy-check.sh

echo "=== Pre-Deploy Checklist ==="

# Check resource requests
kubectl get deploy -o json | jq '.items[] | select(.spec.template.spec.containers[].resources.requests == null) | .metadata.name'

# Check probes
kubectl get deploy -o json | jq '.items[] | select(.spec.template.spec.containers[].livenessProbe == null) | .metadata.name'

# Check replicas
kubectl get deploy -o json | jq '.items[] | select(.spec.replicas < 2) | .metadata.name'

# Check PDBs
kubectl get pdb -A

# Check NetworkPolicies
kubectl get networkpolicy -A

# Check secrets (should not be in env directly)
kubectl get deploy -o yaml | grep -i "value:" | grep -i password

echo "=== Checklist Complete ==="
```

## 7. Final Summary

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   KUBERNETES MASTERY COMPLETED! 🎉                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Du har nu genomgått hela Kubernetes Mastery-modulen!                    │
│                                                                          │
│  BLOCK 1: Fundamentals                                                   │
│  ├── Node 1: K8s Introduction                                           │
│  ├── Node 2: kubectl Mastery                                            │
│  ├── Node 3: Pods                                                       │
│  └── Node 4: Deployments                                                │
│                                                                          │
│  BLOCK 2: Services & Networking                                          │
│  ├── Node 5: Services                                                   │
│  ├── Node 6: Ingress                                                    │
│  ├── Node 7: ConfigMaps & Secrets                                       │
│  └── Node 8: Volumes & Storage                                          │
│                                                                          │
│  BLOCK 3: Advanced Workloads                                             │
│  ├── Node 9: StatefulSets                                               │
│  ├── Node 10: Jobs & CronJobs                                           │
│  ├── Node 11: DaemonSets                                                │
│  └── Node 12: RBAC                                                      │
│                                                                          │
│  BLOCK 4: Helm & Advanced                                                │
│  ├── Node 13: Helm Basics                                               │
│  ├── Node 14: Helm Charts                                               │
│  ├── Node 15: Network Policies                                          │
│  └── Node 16: HPA & VPA                                                 │
│                                                                          │
│  BLOCK 5: Production                                                     │
│  ├── Node 17: Pod Disruption Budgets                                    │
│  ├── Node 18: Probes                                                    │
│  ├── Node 19: Logging & Monitoring                                      │
│  └── Node 20: Production Best Practices ← DU ÄR HÄR!                   │
│                                                                          │
│  GRATTIS! Du är nu redo för production Kubernetes! 🚀                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Praktisk Task

### Final Deployment Exercise

```bash
# Deploy en komplett production-ready applikation med:
# 1. Deployment med alla best practices
# 2. Service + Ingress
# 3. ConfigMap + Secret
# 4. PDB
# 5. HPA
# 6. Network Policy
# 7. Probes (startup, liveness, readiness)
# 8. Resource requests/limits
# 9. Security context
# 10. ServiceAccount med RBAC

# Validera:
kubectl get all,pdb,hpa,networkpolicy,sa -n production
kubectl describe deploy myapp -n production
```

---

**🎓 Kubernetes Mastery: COMPLETE!**
''',
    "xp_reward": 200,
    "estimated_minutes": 90,
    "prerequisites": ["k8s_node_19"],
    "learning_outcomes": [
        "Förstå production readiness",
        "Implementera complete deployment",
        "Följa security best practices",
        "Planera disaster recovery"
    ]
}

# Block 5 Part 2 exports
BLOCK_5_PART_2_NODES = [NODE_19, NODE_20]
