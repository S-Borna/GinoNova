# =============================================================================
# KUBERNETES MASTERY - BLOCK 5 PART 1: PDB & PROBES
# Noder 17-18 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 5 PART 1 - PRODUCTION RELIABILITY
===================================================
Node 17: Pod Disruption Budgets - Availability Guarantees
Node 18: Probes - Health Checks
"""

NODE_17 = {
    "id": "k8s_node_17",
    "title": "Pod Disruption Budgets - Availability Guarantees",
    "slug": "pod-disruption-budgets-availability",
    "content": r'''# 🛡️ Pod Disruption Budgets - Availability Guarantees

## 1. Introduktion & Kontext

Pod Disruption Budgets (PDBs) definierar minimalt antal pods som måste vara tillgängliga under voluntary disruptions som node drain, cluster upgrades, och rolling deployments.

### Voluntary vs Involuntary Disruptions

```
┌─────────────────────────────────────────────────────────────────────────┐
│              VOLUNTARY VS INVOLUNTARY DISRUPTIONS                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  VOLUNTARY DISRUPTIONS (PDB Respects)                                    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  • kubectl drain (node maintenance)                              │   │
│  │  • Cluster upgrades                                              │   │
│  │  • Rolling deployments                                           │   │
│  │  • kubectl delete pod (with eviction API)                       │   │
│  │  • Cluster autoscaler scale-down                                │   │
│  │                                                                  │   │
│  │  ✅ PDB kan blockera/fördröja dessa                             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  INVOLUNTARY DISRUPTIONS (PDB Cannot Stop)                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  • Hardware failure                                              │   │
│  │  • Kernel panic                                                  │   │
│  │  • Node out of resources (OOM kill)                             │   │
│  │  • Cloud provider instance deletion                             │   │
│  │  • kubectl delete pod (direct, ej eviction)                     │   │
│  │                                                                  │   │
│  │  ❌ PDB kan INTE förhindra dessa                                │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. PDB Mechanics

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PDB MECHANICS                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SCENARIO: Node Drain med PDB                                            │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Deployment: replicas=3                                           │  │
│  │  PDB: minAvailable=2                                              │  │
│  │                                                                   │  │
│  │  Initial State:                                                   │  │
│  │  Node 1        Node 2        Node 3                               │  │
│  │  ┌─────┐      ┌─────┐      ┌─────┐                               │  │
│  │  │Pod A│      │Pod B│      │Pod C│                               │  │
│  │  └─────┘      └─────┘      └─────┘                               │  │
│  │  Available: 3  ✅ PDB satisfied (3 >= 2)                         │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  kubectl drain node-1                                             │  │
│  │                                                                   │  │
│  │  Step 1: Evict Pod A from Node 1                                  │  │
│  │  Node 1        Node 2        Node 3                               │  │
│  │  ┌─────┐      ┌─────┐      ┌─────┐                               │  │
│  │  │DRAIN│      │Pod B│      │Pod C│                               │  │
│  │  └─────┘      └─────┘      └─────┘                               │  │
│  │  Available: 2  ✅ Still OK (2 >= 2)                              │  │
│  │                                                                   │  │
│  │  Step 2: Pod A rescheduled to Node 2 or 3                        │  │
│  │  Node 1        Node 2              Node 3                         │  │
│  │  ┌─────┐      ┌─────┐┌─────┐      ┌─────┐                        │  │
│  │  │EMPTY│      │Pod B││Pod A│      │Pod C│                        │  │
│  │  └─────┘      └─────┘└─────┘      └─────┘                        │  │
│  │  Available: 3  ✅ Drain complete                                 │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Om vi försöker drain node-2 MEDAN pod A fortfarande evictas:    │  │
│  │                                                                   │  │
│  │  Node 1        Node 2        Node 3                               │  │
│  │  ┌─────┐      ┌─────┐      ┌─────┐                               │  │
│  │  │DRAIN│      │Pod B│      │Pod C│                               │  │
│  │  └─────┘      └─────┘      └─────┘                               │  │
│  │  Available: 2                                                     │  │
│  │                                                                   │  │
│  │  Försök drain node-2:                                            │  │
│  │  ❌ BLOCKED! Would leave only 1 available (1 < 2)                │  │
│  │  error: Cannot evict pod as it would violate pod disruption      │  │
│  │         budget                                                    │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. PDB Specifications

### minAvailable

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  # Minimum pods som måste vara tillgängliga
  minAvailable: 2                    # Absolute number
  # ELLER
  minAvailable: "50%"                # Percentage

  selector:
    matchLabels:
      app: myapp
```

### maxUnavailable

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  # Maximum pods som får vara unavailable
  maxUnavailable: 1                  # Absolute number
  # ELLER
  maxUnavailable: "25%"              # Percentage

  selector:
    matchLabels:
      app: myapp
```

### minAvailable vs maxUnavailable

```
┌─────────────────────────────────────────────────────────────────────────┐
│              minAvailable VS maxUnavailable                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  replicas: 4                                                             │
│                                                                          │
│  minAvailable: 2                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  • Minst 2 pods måste alltid vara tillgängliga                  │   │
│  │  • Max 2 kan vara unavailable samtidigt                         │   │
│  │  • Bra för: "Behöver alltid X kapacitet"                        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  maxUnavailable: 1                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  • Max 1 pod får vara unavailable                               │   │
│  │  • Minst 3 måste vara available                                 │   │
│  │  • Bra för: "En i taget för maintenance"                        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ⚠️ Använd ENDAST EN av minAvailable eller maxUnavailable               │
│                                                                          │
│  PROCENT BERÄKNING:                                                      │
│  minAvailable: "50%" med 5 replicas = ceil(5 * 0.5) = 3 min available   │
│  maxUnavailable: "25%" med 5 replicas = floor(5 * 0.25) = 1 max unav.   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Praktiska Övningar

### Övning 1: Basic PDB

```bash
# Skapa deployment
kubectl create deployment nginx --image=nginx --replicas=3

# Skapa PDB
cat << 'EOF' | kubectl apply -f -
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: nginx
EOF

# Verifiera
kubectl get pdb
kubectl describe pdb nginx-pdb

# Output:
# Allowed disruptions: 1
# Current: 3
# Desired: 2
```

### Övning 2: Test PDB med Drain

```bash
# Se vilken node pods kör på
kubectl get pods -o wide

# Försök drain node med en pod
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data

# Om PDB blockerar:
# error: cannot delete pod as it would violate the pod's disruption budget

# Force (ignorerar PDB - FARLIGT)
kubectl drain <node-name> --ignore-daemonsets --force --delete-emptydir-data

# Undrain
kubectl uncordon <node-name>
```

### Övning 3: PDB med Percentage

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: critical-app-pdb
spec:
  maxUnavailable: "25%"
  selector:
    matchLabels:
      app: critical-app
      tier: production
EOF

# Med 8 replicas: max 2 unavailable (floor(8 * 0.25) = 2)
# Med 3 replicas: max 0 unavailable (floor(3 * 0.25) = 0) ← Problem!
```

## 5. Common Patterns

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PDB PATTERNS                                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PATTERN 1: High Availability Web Service                                │
│  ─────────────────────────────────────────────────────────────────────  │
│  replicas: 5                                                            │
│  PDB: minAvailable: 3                                                   │
│  → Alltid 60% kapacitet                                                 │
│                                                                          │
│  PATTERN 2: Rolling Update Safe                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│  replicas: 3                                                            │
│  PDB: maxUnavailable: 1                                                 │
│  Deployment: maxUnavailable: 1, maxSurge: 1                             │
│  → En pod i taget                                                       │
│                                                                          │
│  PATTERN 3: Stateful (Database Cluster)                                  │
│  ─────────────────────────────────────────────────────────────────────  │
│  replicas: 3 (1 primary, 2 replica)                                     │
│  PDB: minAvailable: 2                                                   │
│  → Quorum preserved                                                     │
│                                                                          │
│  PATTERN 4: Singleton (Allow 0)                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│  replicas: 1                                                            │
│  PDB: maxUnavailable: 1                                                 │
│  → Tillåter drain (annars blockeras)                                    │
│                                                                          │
│  ⚠️ ANTI-PATTERN: PDB som blockerar all eviction                        │
│  ─────────────────────────────────────────────────────────────────────  │
│  replicas: 2                                                            │
│  PDB: minAvailable: 2                                                   │
│  → Kan ALDRIG drain noder!                                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PDB BEST PRACTICES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Design                                                               │
│     □ Matcha PDB med deployment strategy                                │
│     □ Undvik PDB som blockerar all eviction                            │
│     □ Använd labels som matchar deployment selector                     │
│                                                                          │
│  ✅ Values                                                               │
│     □ minAvailable < replicas (annars blockeras drain)                  │
│     □ Var försiktig med % på små deployments                           │
│     □ Testa PDB med drain i staging                                    │
│                                                                          │
│  ✅ Operations                                                          │
│     □ Dokumentera PDB för ops team                                     │
│     □ Monitor PDB violations                                           │
│     □ Ha process för emergency override                                │
│                                                                          │
│  ✅ Multiple Deployments                                                │
│     □ Separata PDBs per deployment                                     │
│     □ Koordinera för shared nodes                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7-14. Sammanfattning & Task

### PDB Quick Reference

| Replicas | Recommended PDB |
|----------|-----------------|
| 1 | maxUnavailable: 1 |
| 2-3 | maxUnavailable: 1 |
| 4+ | minAvailable: 50% |

---

**Nästa Node:** Probes - Health Checks →
''',
    "xp_reward": 145,
    "estimated_minutes": 50,
    "prerequisites": ["k8s_node_16"],
    "learning_outcomes": [
        "Förstå Pod Disruption Budgets",
        "Konfigurera minAvailable/maxUnavailable",
        "Implementera availability guarantees",
        "Koordinera PDB med deployment strategy"
    ]
}

NODE_18 = {
    "id": "k8s_node_18",
    "title": "Probes - Health Checks",
    "slug": "probes-health-checks",
    "content": r'''# 💓 Probes - Health Checks

## 1. Introduktion & Kontext

Kubernetes probes är health checks som låter Kubernetes förstå om din applikation är redo att ta emot trafik, fortfarande lever, och om den har startat korrekt.

### Three Types of Probes

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      KUBERNETES PROBES                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  STARTUP PROBE (K8s 1.16+)                                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  "Har applikationen startat?"                                    │   │
│  │                                                                  │   │
│  │  • Körs FÖRST vid container start                               │   │
│  │  • Blockerar liveness/readiness tills success                   │   │
│  │  • Bra för slow-starting apps (Java, .NET)                      │   │
│  │                                                                  │   │
│  │  Container Start ──▶ Startup Probe ──▶ Success ──▶              │   │
│  │                                        │                         │   │
│  │                            Liveness + Readiness starts           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  LIVENESS PROBE                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  "Är applikationen vid liv?"                                     │   │
│  │                                                                  │   │
│  │  • Detekterar deadlocks, hangs                                  │   │
│  │  • Failure → Container RESTART                                  │   │
│  │  • ⚠️ Restart fixar inte alla problem!                          │   │
│  │                                                                  │   │
│  │  Running ──▶ Liveness OK ──▶ Running                            │   │
│  │    │              │                                              │   │
│  │    │         Failure                                             │   │
│  │    │              │                                              │   │
│  │    │              ▼                                              │   │
│  │    │         Container Killed                                    │   │
│  │    │              │                                              │   │
│  │    └───────◀──── Restart                                        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  READINESS PROBE                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  "Är applikationen redo för trafik?"                             │   │
│  │                                                                  │   │
│  │  • Kontrollerar om pod kan ta emot requests                     │   │
│  │  • Failure → Pod tas bort från Service endpoints                │   │
│  │  • Container fortsätter köra (ingen restart)                    │   │
│  │                                                                  │   │
│  │  Service ──▶ [Pod 1] [Pod 2] [Pod 3]                            │   │
│  │                 │       │       │                                │   │
│  │              Ready   Ready   NOT Ready                           │   │
│  │                 │       │       │                                │   │
│  │  Traffic ───▶ [Pod 1] [Pod 2]  X (no traffic)                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Probe Mechanisms

```yaml
# HTTP GET - Most common
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
    httpHeaders:
      - name: Custom-Header
        value: MyValue
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 3
  failureThreshold: 3
  successThreshold: 1

# TCP Socket - For non-HTTP services
livenessProbe:
  tcpSocket:
    port: 3306
  initialDelaySeconds: 15
  periodSeconds: 10

# Exec Command - Run command in container
livenessProbe:
  exec:
    command:
      - cat
      - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5

# gRPC (K8s 1.24+)
livenessProbe:
  grpc:
    port: 9090
    service: health
  initialDelaySeconds: 10
```

## 3. Probe Parameters

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PROBE PARAMETERS                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PARAMETER              │ DEFAULT │ DESCRIPTION                          │
│  ─────────────────────────────────────────────────────────────────────  │
│  initialDelaySeconds    │ 0       │ Sekunder före första probe           │
│  periodSeconds          │ 10      │ Intervall mellan probes              │
│  timeoutSeconds         │ 1       │ Timeout för varje probe              │
│  failureThreshold       │ 3       │ Failures före unhealthy              │
│  successThreshold       │ 1       │ Successes före healthy               │
│                                   │ (måste vara 1 för liveness)          │
│                                                                          │
│  TIMELINE EXAMPLE:                                                       │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  initialDelaySeconds: 10                                                │
│  periodSeconds: 5                                                       │
│  failureThreshold: 3                                                    │
│                                                                          │
│  0s        10s       15s       20s       25s       30s                  │
│  │          │         │         │         │         │                   │
│  │          ▼         ▼         ▼         ▼         ▼                   │
│  │       Probe 1   Probe 2   Probe 3   Probe 4   Probe 5               │
│  │          ✓         ✓         ✗         ✗         ✗                   │
│  │                                                   │                   │
│  │                               3 failures ─────────┤                   │
│  │                                                   ▼                   │
│  Start                                          Container                │
│  Container                                      Restarted                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Complete Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: myapp:v1
          ports:
            - containerPort: 8080

          # STARTUP PROBE - Slow starting app
          startupProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 3
            failureThreshold: 30      # 30 * 10 = 300s max startup

          # LIVENESS PROBE - App alive?
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 0    # Starts after startup probe
            periodSeconds: 10
            timeoutSeconds: 3
            failureThreshold: 3

          # READINESS PROBE - Ready for traffic?
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 0
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3
            successThreshold: 1

          resources:
            limits:
              memory: 512Mi
              cpu: 500m
            requests:
              memory: 256Mi
              cpu: 200m
```

## 5. Praktiska Övningar

### Övning 1: Implementera Health Endpoints

```python
# app.py - Flask example
from flask import Flask, jsonify
import time

app = Flask(__name__)
startup_time = time.time()
ready = False

@app.route('/healthz')
def health():
    """Liveness probe - är appen vid liv?"""
    return jsonify({"status": "healthy"}), 200

@app.route('/ready')
def readiness():
    """Readiness probe - kan ta emot trafik?"""
    global ready

    # Simulera startup tid
    if time.time() - startup_time < 30:
        return jsonify({"status": "starting"}), 503

    # Check dependencies
    if not check_database():
        return jsonify({"status": "database unavailable"}), 503

    return jsonify({"status": "ready"}), 200

def check_database():
    # Check DB connection
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### Övning 2: Test Probes

```bash
# Deploy med probes
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: probe-test
spec:
  replicas: 1
  selector:
    matchLabels:
      app: probe-test
  template:
    metadata:
      labels:
        app: probe-test
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
          livenessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
EOF

# Observera probe status
kubectl describe pod -l app=probe-test

# Simulera liveness failure
kubectl exec -it $(kubectl get pod -l app=probe-test -o name) -- rm /usr/share/nginx/html/index.html

# Watch restart
kubectl get pods -w
```

### Övning 3: Debugging Probes

```bash
# Se probe events
kubectl describe pod <pod-name>

# Common issues:
# - Liveness probe failed: Get "http://10.0.0.1:8080/healthz": dial tcp: connection refused
# - Readiness probe failed: HTTP probe failed with statuscode: 503

# Manual test
kubectl exec <pod> -- curl -s localhost:8080/healthz
kubectl exec <pod> -- wget -qO- localhost:8080/ready
```

## 6. Common Anti-Patterns

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   PROBE ANTI-PATTERNS                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ❌ ANTI-PATTERN 1: Liveness = Readiness                                 │
│  ─────────────────────────────────────────────────────────────────────  │
│  Problem: DB-beroende i liveness → restart loop vid DB problem          │
│                                                                          │
│  ✅ Fix:                                                                 │
│     Liveness: Intern health (kan jag processa?)                         │
│     Readiness: Extern health (DB up? Cache warm?)                       │
│                                                                          │
│  ❌ ANTI-PATTERN 2: För aggressiv liveness                               │
│  ─────────────────────────────────────────────────────────────────────  │
│  Problem: timeoutSeconds: 1, failureThreshold: 1                        │
│           → Onödiga restarts vid tillfällig load                        │
│                                                                          │
│  ✅ Fix:                                                                 │
│     timeoutSeconds: 3-5                                                 │
│     failureThreshold: 3                                                 │
│                                                                          │
│  ❌ ANTI-PATTERN 3: Ingen startup probe för slow apps                    │
│  ─────────────────────────────────────────────────────────────────────  │
│  Problem: initialDelaySeconds: 300 i liveness                           │
│           → Döda containers upptäcks inte på 5 min                      │
│                                                                          │
│  ✅ Fix:                                                                 │
│     Använd startupProbe med hög failureThreshold                        │
│     Liveness kan ha låg initialDelaySeconds                             │
│                                                                          │
│  ❌ ANTI-PATTERN 4: Heavy probes                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│  Problem: Probe gör DB-query → belastar system                          │
│                                                                          │
│  ✅ Fix:                                                                 │
│     Lightweight endpoints                                                │
│     Cache probe results                                                  │
│     Separate /healthz (simple) och /ready (with deps)                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PROBE BEST PRACTICES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Design                                                               │
│     □ Separata /healthz och /ready endpoints                           │
│     □ Liveness: Endast intern health                                   │
│     □ Readiness: Include dependency checks                             │
│     □ startupProbe för slow-starting apps                              │
│                                                                          │
│  ✅ Parameters                                                          │
│     □ Rimlig timeout (3-10s)                                           │
│     □ failureThreshold >= 3                                            │
│     □ Startup: failureThreshold * periodSeconds > max startup time     │
│                                                                          │
│  ✅ Implementation                                                      │
│     □ Fast endpoints (< 200ms)                                         │
│     □ Ingen auth på probe endpoints                                    │
│     □ Return 200 OK för healthy                                        │
│     □ Return 503 för unhealthy                                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Sammanfattning & Task

### Probe Selection Guide

| Use Case | Probe | Action on Failure |
|----------|-------|-------------------|
| App hung/deadlock | Liveness | Restart container |
| DB connection lost | Readiness | Remove from service |
| Slow startup | Startup | Wait longer |

---

**Nästa Node:** Logging & Monitoring →
''',
    "xp_reward": 155,
    "estimated_minutes": 55,
    "prerequisites": ["k8s_node_17"],
    "learning_outcomes": [
        "Förstå probe-typer",
        "Implementera health endpoints",
        "Konfigurera probe parameters",
        "Undvika common anti-patterns"
    ]
}

# Block 5 Part 1 exports
BLOCK_5_PART_1_NODES = [NODE_17, NODE_18]
