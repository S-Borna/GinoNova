# =============================================================================
# KUBERNETES MASTERY - BLOCK 4 PART 2: NETWORK POLICIES & AUTOSCALING
# Noder 15-16 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 4 PART 2 - ADVANCED NETWORKING & SCALING
==========================================================
Node 15: Network Policies - Security Boundaries
Node 16: HPA & VPA - Autoscaling
"""

NODE_15 = {
    "id": "k8s_node_15",
    "title": "Network Policies - Security Boundaries",
    "slug": "network-policies-security-boundaries",
    "content": r'''# 🔒 Network Policies - Security Boundaries

## 1. Introduktion & Kontext

Network Policies är Kubernetes inbyggda brandvägg för att kontrollera pod-to-pod och pod-to-external trafik. Som standard är all trafik tillåten - Network Policies låter dig begränsa detta.

### Default Behavior vs Network Policies

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   DEFAULT VS NETWORK POLICIES                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DEFAULT (Utan Network Policies)                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     ALL TRAFFIC ALLOWED                          │   │
│  │                                                                  │   │
│  │  frontend ◄────────────────────────────────────────► backend    │   │
│  │      │                                                   │       │   │
│  │      ▼                                                   ▼       │   │
│  │  database ◄────────────────────────────────────────► redis      │   │
│  │      │                                                   │       │   │
│  │      ▼                                                   ▼       │   │
│  │  internet ◄────────────────────────────────────────► any pod    │   │
│  │                                                                  │   │
│  │  ⚠️ Alla pods kan nå alla andra pods!                           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  MED NETWORK POLICIES                                                    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     EXPLICIT ALLOW ONLY                          │   │
│  │                                                                  │   │
│  │  frontend ─────────────────────────────────────────► backend    │   │
│  │      │                                                   │       │   │
│  │      X (blocked)                                         ▼       │   │
│  │  database ◄───────────────────────────────────────── backend    │   │
│  │      │                                                   │       │   │
│  │      X (blocked)                                         X       │   │
│  │  internet ─────────► frontend only                              │   │
│  │                                                                  │   │
│  │  ✅ Explicit control över all trafik                            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Network Policy Anatomy

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
  namespace: production
spec:
  # Vilka pods denna policy gäller för
  podSelector:
    matchLabels:
      app: backend

  # Vilka policy-typer som definieras
  policyTypes:
    - Ingress          # Inkommande trafik
    - Egress           # Utgående trafik

  # Tillåten inkommande trafik
  ingress:
    - from:
        # Från pods med denna label
        - podSelector:
            matchLabels:
              app: frontend
        # ELLER från denna namespace
        - namespaceSelector:
            matchLabels:
              name: monitoring
        # ELLER från dessa IP-block
        - ipBlock:
            cidr: 10.0.0.0/8
            except:
              - 10.0.1.0/24

      ports:
        - protocol: TCP
          port: 8080

  # Tillåten utgående trafik
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - protocol: TCP
          port: 5432

    # DNS alltid tillåtet
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
```

## 3. Policy Types

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      NETWORK POLICY TYPES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  INGRESS ONLY                                                            │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  policyTypes: [Ingress]                                          │   │
│  │                                                                  │   │
│  │  ┌───────┐          ┌───────┐                                   │   │
│  │  │ Pod A │ ──────▶  │ Pod B │  ✅ Allowed (explicit rule)       │   │
│  │  └───────┘          └───────┘                                   │   │
│  │                          │                                       │   │
│  │                          ▼                                       │   │
│  │                     ┌───────┐                                   │   │
│  │                     │ Pod C │  ✅ Egress allowed (no rule)      │   │
│  │                     └───────┘                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  EGRESS ONLY                                                             │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  policyTypes: [Egress]                                           │   │
│  │                                                                  │   │
│  │  ┌───────┐          ┌───────┐                                   │   │
│  │  │ Pod A │ ◀──────  │ Pod X │  ✅ Ingress allowed (no rule)     │   │
│  │  └───────┘          └───────┘                                   │   │
│  │       │                                                          │   │
│  │       ▼ (explicit rule needed)                                   │   │
│  │  ┌───────┐                                                      │   │
│  │  │ Pod B │  ✅/❌ Depends on egress rule                        │   │
│  │  └───────┘                                                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  BOTH (Ingress + Egress)                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  policyTypes: [Ingress, Egress]                                  │   │
│  │                                                                  │   │
│  │  ALL traffic måste explicit tillåtas                             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Praktiska Övningar

### Övning 1: Deny All Default

```bash
# Deny all ingress i namespace
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}              # Matchar ALLA pods
  policyTypes:
    - Ingress
  # Inga ingress rules = deny all
EOF

# Deny all egress
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-egress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Egress
  # Inga egress rules = deny all (inkl DNS!)
EOF

# Deny all (both)
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
EOF
```

### Övning 2: Allow Specific Traffic

```bash
# Frontend -> Backend policy
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-allow-frontend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
EOF

# Backend -> Database policy
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: database-allow-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: backend
      ports:
        - protocol: TCP
          port: 5432
EOF
```

### Övning 3: Cross-Namespace Policy

```bash
# Allow monitoring namespace to scrape metrics
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-monitoring
  namespace: production
spec:
  podSelector: {}             # Alla pods i production
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: monitoring
          podSelector:
            matchLabels:
              app: prometheus
      ports:
        - protocol: TCP
          port: 9090
EOF

# OBS: AND vs OR logik
# podSelector AND namespaceSelector = Pods med label I namespace med label
# Separata list items = OR
```

### Övning 4: Testa Policies

```bash
# Skapa test-pods
kubectl run frontend --image=nginx --labels="app=frontend" -n production
kubectl run backend --image=nginx --labels="app=backend" -n production
kubectl run attacker --image=nginx --labels="app=attacker" -n production

# Testa connectivity
# Från frontend till backend (ska fungera)
kubectl exec -n production frontend -- curl -s --max-time 2 backend:80

# Från attacker till backend (ska blockas)
kubectl exec -n production attacker -- curl -s --max-time 2 backend:80
```

## 5. Common Patterns

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  NETWORK POLICY PATTERNS                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PATTERN 1: Zero Trust (Deny All + Explicit Allow)                       │
│  ─────────────────────────────────────────────────────────────────────  │
│  1. default-deny-all                                                    │
│  2. allow-dns-egress                                                    │
│  3. allow-frontend-to-backend                                           │
│  4. allow-backend-to-database                                           │
│                                                                          │
│  PATTERN 2: Allow Same Namespace                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│  ingress:                                                               │
│    - from:                                                              │
│        - podSelector: {}    # Alla i samma namespace                    │
│                                                                          │
│  PATTERN 3: Allow External Ingress via Ingress Controller               │
│  ─────────────────────────────────────────────────────────────────────  │
│  ingress:                                                               │
│    - from:                                                              │
│        - namespaceSelector:                                             │
│            matchLabels:                                                 │
│              name: ingress-nginx                                        │
│                                                                          │
│  PATTERN 4: DNS Egress (Required!)                                      │
│  ─────────────────────────────────────────────────────────────────────  │
│  egress:                                                                │
│    - to:                                                                │
│        - namespaceSelector: {}                                          │
│          podSelector:                                                   │
│            matchLabels:                                                 │
│              k8s-app: kube-dns                                          │
│      ports:                                                             │
│        - protocol: UDP                                                  │
│          port: 53                                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                NETWORK POLICY BEST PRACTICES                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Strategy                                                            │
│     □ Börja med default-deny-all                                       │
│     □ Lägg till explicit allow rules                                   │
│     □ Glöm inte DNS egress!                                            │
│                                                                          │
│  ✅ Labeling                                                            │
│     □ Konsistent pod-labeling strategi                                 │
│     □ Labela namespaces för cross-namespace policies                   │
│     □ Dokumentera label-schema                                         │
│                                                                          │
│  ✅ Testing                                                             │
│     □ Testa policies i staging först                                   │
│     □ Verifiera med curl/wget från pods                                │
│     □ Testa både allowed och denied traffic                            │
│                                                                          │
│  ✅ CNI Support                                                         │
│     □ Verifiera att din CNI stöder Network Policies                    │
│     □ Calico, Cilium, Weave Net: ✅                                    │
│     □ Flannel (basic): ❌ (kräver plugin)                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7-14. Sammanfattning & Task

### Policy Decision Matrix

| Scenario | Policy Type |
|----------|-------------|
| Block all incoming | Ingress deny |
| Block all outgoing | Egress deny |
| Allow frontend->backend | Ingress allow |
| Allow DNS | Egress allow port 53 |

---

**Nästa Node:** HPA & VPA →
''',
    "xp_reward": 155,
    "estimated_minutes": 55,
    "prerequisites": ["k8s_node_14"],
    "learning_outcomes": [
        "Förstå Network Policies",
        "Implementera deny-all default",
        "Konfigurera ingress/egress rules",
        "Testa policy enforcement"
    ]
}

NODE_16 = {
    "id": "k8s_node_16",
    "title": "HPA & VPA - Autoscaling",
    "slug": "hpa-vpa-autoscaling",
    "content": r'''# 📈 HPA & VPA - Autoscaling

## 1. Introduktion & Kontext

Kubernetes erbjuder tre typer av autoscaling för att automatiskt anpassa resurser baserat på last: HPA (Horizontal Pod Autoscaler), VPA (Vertical Pod Autoscaler), och Cluster Autoscaler.

### Autoscaling Types

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      AUTOSCALING TYPES                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  HPA (Horizontal Pod Autoscaler)                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Ökar/minskar ANTAL pods baserat på metrics                      │   │
│  │                                                                  │   │
│  │  Low Load          Medium Load        High Load                  │   │
│  │  ┌───┐             ┌───┐ ┌───┐       ┌───┐ ┌───┐ ┌───┐ ┌───┐  │   │
│  │  │Pod│     →       │Pod│ │Pod│   →   │Pod│ │Pod│ │Pod│ │Pod│  │   │
│  │  └───┘             └───┘ └───┘       └───┘ └───┘ └───┘ └───┘  │   │
│  │  replicas: 1       replicas: 2       replicas: 4              │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  VPA (Vertical Pod Autoscaler)                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Justerar RESURSER (CPU/memory) per pod                          │   │
│  │                                                                  │   │
│  │  Under-resourced       Right-sized         Over-resourced        │   │
│  │  ┌─────────┐          ┌───────────┐       ┌───────────────┐     │   │
│  │  │ 100m    │    →     │  500m     │   →   │    200m       │     │   │
│  │  │ 128Mi   │          │  512Mi    │       │    256Mi      │     │   │
│  │  └─────────┘          └───────────┘       └───────────────┘     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  CLUSTER AUTOSCALER                                                      │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Lägger till/tar bort NODER baserat på pending pods              │   │
│  │                                                                  │   │
│  │  ┌──────┐ ┌──────┐         ┌──────┐ ┌──────┐ ┌──────┐          │   │
│  │  │Node 1│ │Node 2│    →    │Node 1│ │Node 2│ │Node 3│          │   │
│  │  └──────┘ └──────┘         └──────┘ └──────┘ └──────┘          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Horizontal Pod Autoscaler (HPA)

### HPA v2 (Current)

```yaml
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

  # Replica limits
  minReplicas: 2
  maxReplicas: 20

  # Metrics
  metrics:
    # CPU utilization (average)
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70

    # Memory utilization
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80

    # Custom metrics (Prometheus)
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: 1000

    # External metrics
    - type: External
      external:
        metric:
          name: queue_messages_ready
          selector:
            matchLabels:
              queue: worker
        target:
          type: Value
          value: 30

  # Scaling behavior
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300    # 5 min window
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60              # Max 10% per minute
        - type: Pods
          value: 4
          periodSeconds: 60              # Max 4 pods per minute
      selectPolicy: Min                  # Använd mest konservativa

    scaleUp:
      stabilizationWindowSeconds: 0      # Ingen delay
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15              # Dubbla var 15s
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max                  # Använd snabbaste
```

### HPA Requirements

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      HPA REQUIREMENTS                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. METRICS SERVER                                                       │
│     kubectl apply -f https://github.com/kubernetes-sigs/metrics-server  │
│                                                                          │
│  2. RESOURCE REQUESTS (Required för CPU/Memory metrics!)                 │
│     containers:                                                          │
│       - name: app                                                        │
│         resources:                                                       │
│           requests:                                                      │
│             cpu: 200m          # ← REQUIRED för HPA                     │
│             memory: 256Mi                                               │
│                                                                          │
│  3. FORMULA                                                             │
│     desiredReplicas = ceil(currentReplicas *                            │
│                            (currentMetricValue / desiredMetricValue))   │
│                                                                          │
│     Exempel:                                                            │
│     Current: 2 replicas, 90% CPU                                        │
│     Target: 70% CPU                                                     │
│     Desired: ceil(2 * (90/70)) = ceil(2.57) = 3 replicas               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Praktiska Övningar

### Övning 1: Basic HPA

```bash
# Skapa deployment med resource requests
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-apache
spec:
  replicas: 1
  selector:
    matchLabels:
      app: php-apache
  template:
    metadata:
      labels:
        app: php-apache
    spec:
      containers:
        - name: php-apache
          image: registry.k8s.io/hpa-example
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: 200m
            limits:
              cpu: 500m
---
apiVersion: v1
kind: Service
metadata:
  name: php-apache
spec:
  ports:
    - port: 80
  selector:
    app: php-apache
EOF

# Skapa HPA
kubectl autoscale deployment php-apache \
  --cpu-percent=50 \
  --min=1 \
  --max=10

# Eller YAML
cat << 'EOF' | kubectl apply -f -
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
EOF

# Verifiera
kubectl get hpa
kubectl describe hpa php-apache
```

### Övning 2: Load Test

```bash
# Terminal 1: Watch HPA
kubectl get hpa php-apache -w

# Terminal 2: Watch pods
kubectl get pods -w

# Terminal 3: Generate load
kubectl run load-generator --image=busybox --rm -it -- sh
while true; do wget -q -O- http://php-apache; done

# Observera scaling up

# Stoppa load (Ctrl+C)
# Observera scaling down (tar 5+ minuter med default settings)
```

### Övning 3: Custom Metrics HPA

```bash
# Kräver Prometheus Adapter
# https://github.com/kubernetes-sigs/prometheus-adapter

cat << 'EOF' | kubectl apply -f -
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: 100
EOF
```

## 4. Vertical Pod Autoscaler (VPA)

### VPA Installation & Config

```bash
# Installation
git clone https://github.com/kubernetes/autoscaler.git
cd autoscaler/vertical-pod-autoscaler/
./hack/vpa-up.sh
```

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp

  updatePolicy:
    updateMode: "Auto"         # Off | Initial | Recreate | Auto

  resourcePolicy:
    containerPolicies:
      - containerName: "*"
        minAllowed:
          cpu: 100m
          memory: 50Mi
        maxAllowed:
          cpu: 2
          memory: 4Gi
        controlledResources: ["cpu", "memory"]
        controlledValues: RequestsAndLimits
```

### VPA Update Modes

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      VPA UPDATE MODES                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  MODE        │ BEHAVIOR                                                  │
│  ────────────────────────────────────────────────────────────────────── │
│  Off         │ Endast rekommendationer, ingen automatisk ändring        │
│  Initial     │ Sätter requests vid pod-skapande (ej restart)            │
│  Recreate    │ Terminerar pods för att uppdatera requests               │
│  Auto        │ Som Recreate, men kan bli In-place i framtiden           │
│                                                                          │
│  ⚠️ VARNING: Recreate/Auto dödar pods för att tillämpa ändringar!       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 5. HPA vs VPA

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      HPA VS VPA COMPARISON                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FEATURE            │ HPA                    │ VPA                       │
│  ─────────────────────────────────────────────────────────────────────  │
│  Scaling method     │ Pod count              │ Pod resources             │
│  Disruption         │ None (adds pods)       │ Pod restart               │
│  Metrics            │ CPU, Memory, Custom    │ Historical usage          │
│  Production ready   │ ✅ Yes                 │ ⚠️ Maturing               │
│  Use with StatefulSet│ ✅ Works              │ ⚠️ Be careful            │
│                                                                          │
│  USE TOGETHER?                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│  ❌ Inte med samma metric (CPU conflicts)                               │
│  ✅ OK: HPA på custom metrics, VPA på resources                         │
│  ✅ OK: VPA i "Off" mode för recommendations only                       │
│                                                                          │
│  RECOMMENDATIONS:                                                        │
│  ─────────────────────────────────────────────────────────────────────  │
│  • Stateless apps: HPA (primary)                                        │
│  • Resource sizing: VPA (Off mode för recs)                             │
│  • Burst traffic: HPA                                                   │
│  • Cost optimization: VPA                                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   AUTOSCALING BEST PRACTICES                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ HPA                                                                  │
│     □ Alltid sätt resource requests                                    │
│     □ Sätt sane min/max replicas                                       │
│     □ Använd behavior för att kontrollera scaling speed                │
│     □ Testa med realistic load                                         │
│                                                                          │
│  ✅ VPA                                                                  │
│     □ Börja med "Off" mode för att se recommendations                  │
│     □ Sätt min/max allowed resources                                   │
│     □ Var försiktig med production - pods restarterar!                 │
│                                                                          │
│  ✅ General                                                              │
│     □ Undvik HPA och VPA på samma metric                               │
│     □ Installera metrics-server                                        │
│     □ Övervaka autoscaler events                                       │
│     □ Kombinera med Cluster Autoscaler för nodes                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7-14. Sammanfattning & Task

### When to Use What

| Scenario | Solution |
|----------|----------|
| Web traffic spikes | HPA |
| Right-size resources | VPA (Off mode) |
| Batch processing | HPA on queue depth |
| Node capacity | Cluster Autoscaler |

---

**Nästa Node:** Pod Disruption Budgets →
''',
    "xp_reward": 165,
    "estimated_minutes": 60,
    "prerequisites": ["k8s_node_15"],
    "learning_outcomes": [
        "Förstå HPA och VPA",
        "Konfigurera autoscaling metrics",
        "Implementera scaling behavior",
        "Välja rätt autoscaling strategy"
    ]
}

# Block 4 Part 2 exports
BLOCK_4_PART_2_NODES = [NODE_15, NODE_16]
