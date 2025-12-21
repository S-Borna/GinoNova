"""
Kubernetes Advanced - Tasks 11-20 (Production & Operations)
Premium Bootcamp-Quality Content
"""

TASKS_ADVANCED = [
    {
        "title": "StatefulSets for Stateful Applications",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 🗄️ StatefulSets for Stateful Applications

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå StatefulSets vs Deployments
- Stable network identities
- Ordered deployment och scaling
- Persistent storage per pod

---

## 📖 StatefulSet vs Deployment

```
+-------------------------------------------------------------+
|            DEPLOYMENT vs STATEFULSET                         |
+-------------------------------------------------------------+
|                                                              |
|  Deployment:                  StatefulSet:                   |
|  +-----------------+         +-----------------+           |
|  | web-6d4f7b8c-a1 |         |    web-0        |           |
|  | web-6d4f7b8c-b2 |         |    web-1        |           |
|  | web-6d4f7b8c-c3 |         |    web-2        |           |
|  +-----------------+         +-----------------+           |
|                                                              |
|  • Random names              • Stable ordinal index         |
|  • Any order                 • Ordered create/delete        |
|  • Shared storage            • Unique storage per pod       |
|  • Interchangeable           • Stable network identity      |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 StatefulSet Manifest

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: standard
      resources:
        requests:
          storage: 10Gi
---
# Headless Service (required)
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  clusterIP: None  # Headless
  selector:
    app: postgres
  ports:
  - port: 5432
```

---

## 🔗 Stable Network Identity

```
+-------------------------------------------------------------+
|                STATEFULSET DNS                               |
+-------------------------------------------------------------+
|                                                              |
|  Pod DNS Format:                                            |
|  <pod-name>.<service-name>.<namespace>.svc.cluster.local    |
|                                                              |
|  Example (postgres StatefulSet):                            |
|  +-----------------------------------------------------+   |
|  |  postgres-0.postgres.default.svc.cluster.local      |   |
|  |  postgres-1.postgres.default.svc.cluster.local      |   |
|  |  postgres-2.postgres.default.svc.cluster.local      |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  Headless Service returns all Pod IPs:                      |
|  postgres.default.svc -> [10.244.0.5, 10.244.1.6, ...]      |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔄 Ordering Guarantees

```bash
# Create order: 0, 1, 2, 3...
# Delete order: 3, 2, 1, 0... (reverse)

# Scale up
kubectl scale statefulset postgres --replicas=5
# Creates: postgres-3, postgres-4 (in order)

# Scale down
kubectl scale statefulset postgres --replicas=2
# Deletes: postgres-4, postgres-3 (reverse order)
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Deploy StatefulSet
```bash
# Deploy postgres StatefulSet
kubectl apply -f postgres-statefulset.yaml

# Watch creation order
kubectl get pods -w

# Test DNS
kubectl run test --rm -it --image=busybox -- sh
# nslookup postgres-0.postgres

# Cleanup
kubectl delete statefulset postgres
kubectl delete pvc -l app=postgres
```

---

## 📚 Sammanfattning

| Feature | Deployment | StatefulSet |
|---------|------------|-------------|
| Pod names | Random | Ordinal |
| Storage | Shared | Per-pod |
| Scaling | Parallel | Sequential |
| Network ID | Random | Stable |

**Nästa steg:** DaemonSets & Jobs

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "DaemonSets, Jobs & CronJobs",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 150,
        "content": r"""
# ⚙️ DaemonSets, Jobs & CronJobs

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- DaemonSets för node-level workloads
- Jobs för one-time tasks
- CronJobs för scheduled tasks
- Use cases och patterns

---

## 📖 Workload Types

```
+-------------------------------------------------------------+
|                    WORKLOAD TYPES                            |
+-------------------------------------------------------------+
|                                                              |
|  DaemonSet           Job                CronJob              |
|  +-------------+    +-------------+    +-------------+     |
|  | One pod per |    | Run-to-     |    | Scheduled   |     |
|  | node        |    | completion  |    | Jobs        |     |
|  |             |    |             |    |             |     |
|  | • Logging   |    | • Migrations|    | • Backups   |     |
|  | • Monitoring|    | • Batch     |    | • Reports   |     |
|  | • Network   |    | • One-time  |    | • Cleanup   |     |
|  +-------------+    +-------------+    +-------------+     |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  selector:
    matchLabels:
      name: fluentd
  template:
    metadata:
      labels:
        name: fluentd
    spec:
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        effect: NoSchedule
      containers:
      - name: fluentd
        image: fluentd:latest
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```

---

## 📝 Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
spec:
  completions: 1
  parallelism: 1
  backoffLimit: 3
  activeDeadlineSeconds: 600
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: migrate
        image: myapp:migrate
        command: ["./migrate.sh"]
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
```

---

## 📝 CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup
spec:
  schedule: "0 2 * * *"  # Daily at 2 AM
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: backup
            image: backup-tool:latest
            command: ["./backup.sh"]
```

---

## 🔧 Commands

```bash
# DaemonSet
kubectl get daemonsets
kubectl describe ds fluentd

# Jobs
kubectl get jobs
kubectl logs job/db-migration
kubectl delete job db-migration

# CronJobs
kubectl get cronjobs
kubectl create job --from=cronjob/backup manual-backup
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Run Job
```bash
# Skapa job
kubectl create job test-job --image=busybox -- echo "Hello K8s"

# Watch
kubectl get jobs -w
kubectl logs job/test-job

# Cleanup
kubectl delete job test-job
```

---

## 📚 Sammanfattning

| Type | Use Case |
|------|----------|
| DaemonSet | Log collection, monitoring |
| Job | Migrations, batch processing |
| CronJob | Backups, scheduled tasks |

**Nästa steg:** Resource Management

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Resource Management & QoS",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 📊 Resource Management & QoS

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Requests vs Limits
- Quality of Service classes
- LimitRanges och ResourceQuotas
- Pod Priority och Preemption

---

## 📖 Requests vs Limits

```
+-------------------------------------------------------------+
|                REQUESTS vs LIMITS                            |
+-------------------------------------------------------------+
|                                                              |
|  Requests = Guaranteed minimum                               |
|  Limits = Maximum allowed                                    |
|                                                              |
|  Memory Usage:                                               |
|  +-----------------------------------------------------+   |
|  |  0MB          256MB         512MB         1GB      |   |
|  |  |             |             |             |        |   |
|  |  +-------------+             |             |        |   |
|  |  |   REQUEST   |             |             |        |   |
|  |  |             |             |             |        |   |
|  |  +-------------+-------------+             |        |   |
|  |  |          ACTUAL           |             |        |   |
|  |  |                           |             |        |   |
|  |  +---------------------------+-------------+        |   |
|  |  |              LIMIT                       |        |   |
|  |  +------------------------------------------+        |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  If actual > limit -> OOMKilled                              |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 Resource Specification

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: app
    image: myapp:v1
    resources:
      requests:
        memory: "256Mi"
        cpu: "250m"      # 0.25 CPU
      limits:
        memory: "512Mi"
        cpu: "500m"      # 0.5 CPU
```

---

## 🎯 QoS Classes

```
+-------------------------------------------------------------+
|                    QoS CLASSES                               |
+-------------------------------------------------------------+
|                                                              |
|  1. Guaranteed (highest priority)                           |
|     • requests == limits för CPU och memory                |
|     • Sista att bli evicted                                |
|                                                              |
|  2. Burstable                                               |
|     • requests < limits                                     |
|     • Eller bara requests satt                             |
|                                                              |
|  3. BestEffort (lowest priority)                            |
|     • Inga requests eller limits                           |
|     • Första att bli evicted                               |
|                                                              |
+-------------------------------------------------------------+
```

```yaml
# Guaranteed
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "256Mi"
    cpu: "250m"

# Burstable
resources:
  requests:
    memory: "128Mi"
  limits:
    memory: "256Mi"

# BestEffort
# (no resources specified)
```

---

## 🔧 LimitRange & ResourceQuota

```yaml
# LimitRange - defaults per container
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: dev
spec:
  limits:
  - default:
      memory: "256Mi"
      cpu: "200m"
    defaultRequest:
      memory: "128Mi"
      cpu: "100m"
    max:
      memory: "1Gi"
      cpu: "1"
    min:
      memory: "64Mi"
      cpu: "50m"
    type: Container

---
# ResourceQuota - total per namespace
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: dev
spec:
  hard:
    requests.cpu: "4"
    requests.memory: "8Gi"
    limits.cpu: "8"
    limits.memory: "16Gi"
    pods: "20"
    persistentvolumeclaims: "10"
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Resource Limits
```bash
# Skapa namespace med quota
kubectl create namespace test-quota

# Apply quota
kubectl apply -f - <<EOF
apiVersion: v1
kind: ResourceQuota
metadata:
  name: test-quota
  namespace: test-quota
spec:
  hard:
    pods: "5"
    requests.memory: "1Gi"
EOF

# Verifiera
kubectl describe quota -n test-quota
```

---

## 📚 Sammanfattning

| Koncept | Syfte |
|---------|-------|
| Requests | Scheduling guarantee |
| Limits | Maximum usage |
| LimitRange | Defaults per pod |
| ResourceQuota | Total per namespace |

**Nästa steg:** Autoscaling

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Kubernetes Autoscaling",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 📈 Kubernetes Autoscaling

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Horizontal Pod Autoscaler (HPA)
- Vertical Pod Autoscaler (VPA)
- Cluster Autoscaler
- Custom metrics

---

## 📖 Autoscaling Types

```
+-------------------------------------------------------------+
|                 AUTOSCALING TYPES                            |
+-------------------------------------------------------------+
|                                                              |
|  HPA (Horizontal)           VPA (Vertical)                  |
|  +-----------------+       +-----------------+             |
|  | Add more pods   |       | Resize pods     |             |
|  |                 |       |                 |             |
|  |  [P] [P] [P]    |       |     [P]         |             |
|  |       +         |       |    ↑↓           |             |
|  |  [P] [P] [P]    |       |  CPU/Mem        |             |
|  +-----------------+       +-----------------+             |
|                                                              |
|  Cluster Autoscaler                                         |
|  +-----------------------------------------------------+   |
|  |  Add/Remove nodes based on pending pods             |   |
|  |                                                      |   |
|  |  [Node] [Node] [Node] + [Node]                      |   |
|  +-----------------------------------------------------+   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 HPA Manifest

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
```

---

## 🔧 HPA Commands

```bash
# Skapa HPA
kubectl autoscale deployment my-app \
  --min=2 --max=10 --cpu-percent=70

# Se HPA status
kubectl get hpa
kubectl describe hpa my-app-hpa

# Manuell test
kubectl run -it load-test --image=busybox --rm -- sh
# while true; do wget -q -O- http://my-app; done
```

---

## 📊 Custom Metrics

```yaml
# HPA med custom metrics
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: queue-based-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: worker
  minReplicas: 1
  maxReplicas: 20
  metrics:
  - type: External
    external:
      metric:
        name: queue_messages_count
        selector:
          matchLabels:
            queue: jobs
      target:
        type: AverageValue
        averageValue: "30"
```

---

## 📝 VPA Manifest

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: Auto  # Off, Initial, Auto
  resourcePolicy:
    containerPolicies:
    - containerName: app
      minAllowed:
        cpu: "100m"
        memory: "128Mi"
      maxAllowed:
        cpu: "2"
        memory: "4Gi"
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Setup HPA
```bash
# Ensure metrics-server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Deploy app with resources
kubectl create deployment php-apache \
  --image=registry.k8s.io/hpa-example \
  --requests=cpu=200m

kubectl expose deployment php-apache --port=80

# Create HPA
kubectl autoscale deployment php-apache \
  --cpu-percent=50 --min=1 --max=10

# Generate load
kubectl run -it load-gen --rm --image=busybox -- sh
# while true; do wget -q -O- http://php-apache; done

# Watch scaling
kubectl get hpa -w
```

---

## 📚 Sammanfattning

| Autoscaler | Skalar | Baserat på |
|------------|--------|------------|
| HPA | Pod replicas | CPU, Memory, Custom |
| VPA | Pod resources | Historical usage |
| Cluster | Nodes | Pending pods |

**Nästa steg:** Monitoring & Observability

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Monitoring & Observability",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 📊 Monitoring & Observability

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Prometheus för metrics
- Grafana för visualisering
- Kubernetes metrics och events
- Alerting

---

## 📖 Observability Stack

```
+-------------------------------------------------------------+
|                OBSERVABILITY STACK                           |
+-------------------------------------------------------------+
|                                                              |
|  +------------------------------------------------------+  |
|  |                     Grafana                           |  |
|  |                  (Visualization)                      |  |
|  +-------------------------+----------------------------+  |
|                            |                                |
|           +----------------+----------------+              |
|           |                |                |               |
|           ▼                ▼                ▼               |
|  +-------------+  +-------------+  +-----------------+    |
|  | Prometheus  |  |    Loki     |  |     Tempo       |    |
|  |  (Metrics)  |  |   (Logs)    |  |   (Traces)      |    |
|  +------+------+  +------+------+  +--------+--------+    |
|         |                |                   |              |
|         |                |                   |              |
|  +------▼--------------▼-------------------▼----------+   |
|  |               Kubernetes Cluster                    |   |
|  |  [Pods]  [Services]  [Nodes]  [Events]             |   |
|  +----------------------------------------------------+   |
|                                                             |
+-------------------------------------------------------------+
```

---

## 🔧 Prometheus Stack Installation

```bash
# Med Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack

# Port forward
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090
kubectl port-forward svc/prometheus-grafana 3000:80
```

---

## 📝 ServiceMonitor

```yaml
# För att monitora egen app
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-app-monitor
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
```

---

## 📈 PromQL Queries

```promql
# Pod CPU usage
sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m])) by (pod)

# Memory usage
container_memory_working_set_bytes{namespace="default"} / 1024 / 1024

# Request rate
sum(rate(http_requests_total[5m])) by (service)

# Error rate
sum(rate(http_requests_total{status=~"5.."}[5m]))
/ sum(rate(http_requests_total[5m]))

# Pod restarts
sum(kube_pod_container_status_restarts_total) by (pod)
```

---

## 🚨 AlertManager

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: app-alerts
spec:
  groups:
  - name: app.rules
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
      expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Pod {{ $labels.pod }} is crash looping"
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Setup Monitoring
```bash
# Install kube-prometheus-stack
helm install monitoring prometheus-community/kube-prometheus-stack

# Access Grafana
kubectl port-forward svc/monitoring-grafana 3000:80
# Default: admin/prom-operator

# Check Prometheus targets
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090
# Go to Status -> Targets
```

---

## 📚 Sammanfattning

| Tool | Purpose |
|------|---------|
| Prometheus | Metrics collection |
| Grafana | Visualization |
| AlertManager | Alert routing |
| Loki | Log aggregation |

**Nästa steg:** Troubleshooting Kubernetes

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Troubleshooting Kubernetes",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 165,
        "content": r"""
# 🔍 Troubleshooting Kubernetes

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Debugging pods och containers
- Common issues och lösningar
- Cluster troubleshooting
- Logging och events

---

## 📖 Troubleshooting Workflow

```
+-------------------------------------------------------------+
|              TROUBLESHOOTING WORKFLOW                        |
+-------------------------------------------------------------+
|                                                              |
|  1. Check Pod Status                                        |
|     kubectl get pods                                        |
|     kubectl describe pod <name>                             |
|                                                              |
|  2. Check Logs                                              |
|     kubectl logs <pod>                                      |
|     kubectl logs <pod> --previous                           |
|                                                              |
|  3. Check Events                                            |
|     kubectl get events --sort-by='.lastTimestamp'          |
|                                                              |
|  4. Check Resources                                         |
|     kubectl top pods                                        |
|     kubectl describe node                                   |
|                                                              |
|  5. Debug Container                                         |
|     kubectl exec -it <pod> -- sh                           |
|     kubectl debug <pod> --image=busybox                    |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🚨 Common Issues

```
+-------------------------------------------------------------+
|                   COMMON POD ISSUES                          |
+-------------------------------------------------------------+
|                                                              |
|  ImagePullBackOff                                           |
|  +- Wrong image name/tag                                   |
|  +- Private registry auth                                  |
|  +- Image doesn't exist                                    |
|                                                              |
|  CrashLoopBackOff                                           |
|  +- Application error                                      |
|  +- Missing config/secrets                                 |
|  +- Resource limits too low                                |
|                                                              |
|  Pending                                                    |
|  +- Insufficient resources                                 |
|  +- Node selector/affinity                                 |
|  +- PVC not bound                                          |
|                                                              |
|  OOMKilled                                                  |
|  +- Memory limit too low                                   |
|  +- Memory leak in app                                     |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 Debug Commands

```bash
# Pod status
kubectl get pods -o wide
kubectl describe pod my-pod

# Logs
kubectl logs my-pod
kubectl logs my-pod -c sidecar  # Specific container
kubectl logs my-pod --previous  # Previous crash

# Events
kubectl get events --sort-by='.lastTimestamp'
kubectl get events --field-selector involvedObject.name=my-pod

# Resource usage
kubectl top pods
kubectl top nodes

# Exec into pod
kubectl exec -it my-pod -- sh
kubectl exec my-pod -- cat /etc/config/app.conf

# Debug pod (ephemeral container)
kubectl debug my-pod -it --image=busybox

# Copy files
kubectl cp my-pod:/var/log/app.log ./app.log
```

---

## 🌐 Network Troubleshooting

```bash
# DNS test
kubectl run test --rm -it --image=busybox -- nslookup kubernetes

# Service endpoints
kubectl get endpoints my-service

# Network connectivity
kubectl run test --rm -it --image=nicolaka/netshoot -- bash
# Inside: curl http://my-service
# Inside: nslookup my-service
# Inside: traceroute my-service

# Check service
kubectl describe svc my-service
```

---

## 🔍 Node Troubleshooting

```bash
# Node status
kubectl get nodes -o wide
kubectl describe node <node-name>

# Node conditions
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="Ready")].status}{"\n"}{end}'

# Node resources
kubectl describe node | grep -A 5 "Allocated resources"

# Cordon/Drain
kubectl cordon node-1       # Mark unschedulable
kubectl drain node-1 --ignore-daemonsets  # Evict pods
kubectl uncordon node-1     # Allow scheduling
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Debug Failing Pod
```bash
# Create failing pod
kubectl run failing-pod --image=busybox -- exit 1

# Check status
kubectl get pods

# Check events
kubectl describe pod failing-pod

# Check logs
kubectl logs failing-pod --previous

# Cleanup
kubectl delete pod failing-pod
```

---

## 📚 Sammanfattning

| Status | Första steg |
|--------|-------------|
| ImagePullBackOff | Check image name |
| CrashLoopBackOff | Check logs |
| Pending | Check events |
| OOMKilled | Increase limits |

**Nästa steg:** GitOps with Kubernetes

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "GitOps with ArgoCD",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 165,
        "content": r"""
# 🔄 GitOps with ArgoCD

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå GitOps principer
- Installera och konfigurera ArgoCD
- Application deployment
- Sync strategies

---

## 📖 GitOps Principles

```
+-------------------------------------------------------------+
|                    GITOPS WORKFLOW                           |
+-------------------------------------------------------------+
|                                                              |
|  Developer              Git Repository          Kubernetes   |
|  +----------+          +--------------+       +----------+ |
|  |  Change  |--Push---▶|   Desired    |       |  Actual  | |
|  |  Code    |          |   State      |       |  State   | |
|  +----------+          +------+-------+       +----+-----+ |
|                               |                     |       |
|                               |    ArgoCD           |       |
|                               |  +---------+        |       |
|                               +-▶| Compare |◀-------+       |
|                                  |  & Sync |                |
|                                  +---------+                |
|                                                              |
|  Git = Single source of truth                               |
|  All changes through Git (no kubectl apply)                 |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 ArgoCD Installation

```bash
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for pods
kubectl wait --for=condition=Ready pods --all -n argocd --timeout=300s

# Get initial admin password
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d

# Port forward
kubectl port-forward svc/argocd-server -n argocd 8080:443

# CLI login
argocd login localhost:8080
```

---

## 📝 Application Manifest

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/myapp-k8s.git
    targetRevision: HEAD
    path: manifests
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

---

## 🔄 Sync Strategies

```yaml
# Manual sync
syncPolicy: {}

# Automated sync
syncPolicy:
  automated:
    prune: true      # Delete resources not in Git
    selfHeal: true   # Revert manual changes
    allowEmpty: false

# With waves (order)
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"  # Lower = first
```

---

## 📂 Repository Structure

```
myapp-k8s/
+-- base/
|   +-- deployment.yaml
|   +-- service.yaml
|   +-- kustomization.yaml
+-- overlays/
|   +-- dev/
|   |   +-- kustomization.yaml
|   +-- staging/
|   |   +-- kustomization.yaml
|   +-- production/
|       +-- kustomization.yaml
+-- argocd/
    +-- application.yaml
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Deploy with ArgoCD
```bash
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Create app via CLI
argocd app create nginx \
  --repo https://github.com/argoproj/argocd-example-apps.git \
  --path guestbook \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default

# Sync
argocd app sync nginx

# Watch status
argocd app get nginx
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| GitOps | Git as source of truth |
| ArgoCD | GitOps operator |
| Application | ArgoCD CRD |
| Sync | Reconcile Git -> Cluster |

**Nästa steg:** Production Best Practices

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Production Best Practices",
        "difficulty": "hard",
        "estimated_minutes": 60,
        "xp_reward": 170,
        "content": r"""
# 🏭 Production Best Practices

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- High availability patterns
- Security hardening
- Multi-tenancy
- Disaster recovery

---

## 📖 HA Architecture

```
+-------------------------------------------------------------+
|              HIGH AVAILABILITY SETUP                         |
+-------------------------------------------------------------+
|                                                              |
|  +-----------------------------------------------------+   |
|  |              Load Balancer                           |   |
|  +-----------------------+-----------------------------+   |
|                          |                                  |
|         +----------------+----------------+                |
|         |                |                |                 |
|  +------▼------+  +------▼------+  +------▼------+        |
|  | Control     |  | Control     |  | Control     |        |
|  | Plane 1     |  | Plane 2     |  | Plane 3     |        |
|  +-------------+  +-------------+  +-------------+        |
|                                                             |
|  +------------------------------------------------------+  |
|  |                    etcd cluster                       |  |
|  |    [etcd-1]         [etcd-2]         [etcd-3]        |  |
|  +------------------------------------------------------+  |
|                                                             |
|  +-------------+  +-------------+  +-------------+        |
|  |  Worker 1   |  |  Worker 2   |  |  Worker N   |        |
|  |   AZ-a      |  |   AZ-b      |  |   AZ-c      |        |
|  +-------------+  +-------------+  +-------------+        |
|                                                             |
+-------------------------------------------------------------+
```

---

## 🔐 Security Checklist

```yaml
# Pod Security Standards
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted

---
# Secure Pod
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:v1
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    resources:
      limits:
        memory: "256Mi"
        cpu: "500m"
```

---

## 📊 Production Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: production-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: production-app
  template:
    metadata:
      labels:
        app: production-app
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchLabels:
                app: production-app
            topologyKey: kubernetes.io/hostname
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            app: production-app
      containers:
      - name: app
        image: myapp:v1.0.0
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "1"
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 10
      terminationGracePeriodSeconds: 60
```

---

## 💾 Backup & DR

```bash
# etcd backup
ETCDCTL_API=3 etcdctl snapshot save snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/etcd/ca.crt \
  --cert=/etc/etcd/server.crt \
  --key=/etc/etcd/server.key

# Velero backup
velero backup create production-backup --include-namespaces production

# Restore
velero restore create --from-backup production-backup
```

---

## 📋 Production Checklist

```
+-------------------------------------------------------------+
|              PRODUCTION CHECKLIST                            |
+-------------------------------------------------------------+
|                                                              |
|  ☐ Resource requests/limits set                            |
|  ☐ Health probes configured                                |
|  ☐ Pod anti-affinity for HA                               |
|  ☐ Network policies in place                              |
|  ☐ RBAC properly configured                               |
|  ☐ Secrets encrypted at rest                              |
|  ☐ Pod Security Standards enforced                        |
|  ☐ Monitoring/alerting setup                              |
|  ☐ Logging aggregation                                    |
|  ☐ Backup strategy implemented                            |
|  ☐ Disaster recovery tested                               |
|  ☐ GitOps workflow established                            |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📚 Sammanfattning

| Area | Best Practice |
|------|---------------|
| HA | Multi-AZ, anti-affinity |
| Security | PSS, NetworkPolicy, RBAC |
| Reliability | Probes, PDB, resources |
| Observability | Metrics, logs, traces |
| DR | etcd backup, Velero |

**Nästa steg:** CKA/CKAD Certification Prep

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Kubernetes Operators & CRDs",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 165,
        "content": r"""
# 🤖 Kubernetes Operators & CRDs

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Custom Resource Definitions
- Operator pattern
- Bygga enkla operators
- Popular operators

---

## 📖 CRD & Operator Concept

```
+-------------------------------------------------------------+
|                 OPERATOR PATTERN                             |
+-------------------------------------------------------------+
|                                                              |
|  Custom Resource Definition (CRD)                           |
|  +-----------------------------------------------------+   |
|  |  Extends Kubernetes API                              |   |
|  |  Defines new resource types                         |   |
|  +-----------------------------------------------------+   |
|                           |                                 |
|                           ▼                                 |
|  Custom Resource (CR)                                       |
|  +-----------------------------------------------------+   |
|  |  Instance of CRD                                     |   |
|  |  apiVersion: myapp.io/v1                            |   |
|  |  kind: Database                                     |   |
|  +-----------------------------------------------------+   |
|                           |                                 |
|                           ▼                                 |
|  Operator (Controller)                                      |
|  +-----------------------------------------------------+   |
|  |  Watches CR changes                                  |   |
|  |  Reconciles desired -> actual state                  |   |
|  |  Creates/manages K8s resources                      |   |
|  +-----------------------------------------------------+   |
|                                                             |
+-------------------------------------------------------------+
```

---

## 📝 CRD Definition

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.myapp.io
spec:
  group: myapp.io
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
                enum: ["postgres", "mysql"]
              version:
                type: string
              replicas:
                type: integer
                minimum: 1
                maximum: 5
              storage:
                type: string
            required: ["engine", "version"]
          status:
            type: object
            properties:
              phase:
                type: string
              ready:
                type: boolean
    subresources:
      status: {}
  scope: Namespaced
  names:
    plural: databases
    singular: database
    kind: Database
    shortNames:
    - db
```

---

## 📝 Custom Resource

```yaml
apiVersion: myapp.io/v1
kind: Database
metadata:
  name: my-postgres
spec:
  engine: postgres
  version: "15"
  replicas: 3
  storage: "10Gi"
```

---

## 🔧 Using CRDs

```bash
# Apply CRD
kubectl apply -f database-crd.yaml

# Create instance
kubectl apply -f my-database.yaml

# List custom resources
kubectl get databases
kubectl get db  # short name

# Describe
kubectl describe db my-postgres
```

---

## 🌟 Popular Operators

```
+-------------------------------------------------------------+
|                  POPULAR OPERATORS                           |
+-------------------------------------------------------------+
|                                                              |
|  Databases                                                  |
|  +- CloudNativePG (PostgreSQL)                             |
|  +- MongoDB Community Operator                             |
|  +- MySQL Operator                                         |
|                                                              |
|  Messaging                                                  |
|  +- Strimzi (Kafka)                                        |
|  +- RabbitMQ Cluster Operator                              |
|                                                              |
|  Certificates                                               |
|  +- cert-manager                                           |
|                                                              |
|  GitOps                                                     |
|  +- ArgoCD                                                 |
|                                                              |
|  Monitoring                                                 |
|  +- Prometheus Operator                                    |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Install cert-manager
```bash
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml

# Check CRDs
kubectl get crds | grep cert-manager

# Create ClusterIssuer
kubectl apply -f - <<EOF
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-staging
spec:
  acme:
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-staging
    solvers:
    - http01:
        ingress:
          class: nginx
EOF

# List issuers
kubectl get clusterissuer
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| CRD | Extend K8s API |
| CR | Instance av CRD |
| Operator | Controller för CR |
| Reconciliation | Sync desired -> actual |

**🎉 Grattis! Du har slutfört Kubernetes Mastery!**

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Complete Kubernetes Project",
        "difficulty": "hard",
        "estimated_minutes": 65,
        "xp_reward": 180,
        "content": r"""
# 🎯 Complete Kubernetes Project

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Bygga production-grade K8s deployment
- Full GitOps workflow
- Monitoring och alerting
- End-to-end implementation

---

## 🏗️ Project Architecture

```
+-------------------------------------------------------------+
|              COMPLETE K8S PROJECT                            |
+-------------------------------------------------------------+
|                                                              |
|  +-----------------------------------------------------+   |
|  |                   Ingress (nginx)                    |   |
|  |                 app.example.com                      |   |
|  +-------------------------+---------------------------+   |
|                            |                                |
|              +-------------+-------------+                 |
|              |             |             |                  |
|              ▼             ▼             ▼                  |
|        +---------+   +---------+   +---------+            |
|        |Frontend |   |   API   |   | Worker  |            |
|        | (3 pods)|   | (3 pods)|   | (2 pods)|            |
|        +----+----+   +----+----+   +----+----+            |
|             |             |             |                   |
|             +-------------+-------------+                  |
|                           |                                 |
|        +------------------+------------------+            |
|        |                  |                   |            |
|        ▼                  ▼                   ▼            |
|  +----------+      +----------+       +----------+       |
|  |PostgreSQL|      |  Redis   |       | RabbitMQ |       |
|  |(StatefulS|      | (Deploy) |       | (Deploy) |       |
|  +----------+      +----------+       +----------+       |
|                                                             |
+-------------------------------------------------------------+
```

---

## 📂 Repository Structure

```
k8s-project/
+-- base/
|   +-- namespace.yaml
|   +-- frontend/
|   |   +-- deployment.yaml
|   |   +-- service.yaml
|   +-- api/
|   |   +-- deployment.yaml
|   |   +-- service.yaml
|   |   +-- hpa.yaml
|   +-- worker/
|   |   +-- deployment.yaml
|   +-- postgres/
|   |   +-- statefulset.yaml
|   |   +-- service.yaml
|   |   +-- pvc.yaml
|   +-- redis/
|   |   +-- deployment.yaml
|   |   +-- service.yaml
|   +-- kustomization.yaml
+-- overlays/
|   +-- dev/
|   |   +-- kustomization.yaml
|   |   +-- patches/
|   +-- production/
|       +-- kustomization.yaml
|       +-- patches/
|       +-- secrets/
+-- monitoring/
|   +-- prometheus-rules.yaml
|   +-- servicemonitor.yaml
+-- argocd/
    +-- application.yaml
```

---

## 📝 Base Manifests

```yaml
# base/api/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api
        image: api:latest
        ports:
        - containerPort: 8080
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: url
        - name: REDIS_URL
          value: redis://redis:6379
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "1"
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
```

---

## 🔧 Kustomize Overlays

```yaml
# overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
- ../../base

replicas:
- name: api
  count: 5
- name: frontend
  count: 3

images:
- name: api
  newTag: v1.2.3
- name: frontend
  newTag: v1.2.3

patches:
- path: patches/api-resources.yaml
- path: patches/ingress-tls.yaml

secretGenerator:
- name: db-credentials
  files:
  - secrets/db-url
```

---

## 🚀 ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-production
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/k8s-project.git
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

---

## 🏋️ Deployment Steps

```bash
# 1. Create namespace
kubectl create namespace production

# 2. Create secrets
kubectl create secret generic db-credentials \
  -n production \
  --from-literal=url='postgresql://...'

# 3. Deploy with kustomize
kubectl apply -k overlays/production/

# 4. Or with ArgoCD
kubectl apply -f argocd/application.yaml

# 5. Verify
kubectl get all -n production
kubectl get ingress -n production

# 6. Test
curl -k https://app.example.com/api/health
```

---

## 📚 Sammanfattning

| Component | Technology |
|-----------|------------|
| Package Management | Kustomize/Helm |
| GitOps | ArgoCD |
| Ingress | nginx-ingress |
| TLS | cert-manager |
| Monitoring | Prometheus/Grafana |
| Scaling | HPA |

**🎉 Grattis! Du har slutfört hela Kubernetes Mastery kursen!**

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
]
