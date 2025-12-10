# =============================================================================
# KUBERNETES MASTERY - BLOCK 1 PART 2: PODS & DEPLOYMENTS
# Noder 3-4 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 1 PART 2 - FUNDAMENTALS
========================================
Node 3: Pods - K8s Minsta Deployment Unit
Node 4: Deployments - Replica Management & Updates
"""

NODE_3 = {
    "id": "k8s_node_3",
    "title": "Pods - K8s Minsta Deployment Unit",
    "slug": "pods-kubernetes-deployment-unit",
    "content": r'''# 🎪 Pods - K8s Minsta Deployment Unit

## 1. Introduktion & Kontext

En Pod är den minsta deployerbara enheten i Kubernetes. Medan du kanske tänker på containers, arbetar Kubernetes alltid med Pods - en abstraktion som kan innehålla en eller flera containers.

### Pod Koncept

```
+-------------------------------------------------------------------------+
|                         POD CONCEPT                                      |
+-------------------------------------------------------------------------+
|                                                                          |
|  Container World          Kubernetes World                               |
|  ===============          ================                               |
|                                                                          |
|  +-------------+         +---------------------------------+            |
|  |  Container  |         |            POD                   |            |
|  |   (nginx)   |   --▶  |  +-------------+                |            |
|  +-------------+         |  |  Container  |                |            |
|                          |  |   (nginx)   |                |            |
|                          |  +-------------+                |            |
|                          |  • Shared network namespace     |            |
|                          |  • Shared storage volumes       |            |
|                          |  • Shared lifecycle             |            |
|                          +---------------------------------+            |
|                                                                          |
|  Multi-Container Pod:                                                    |
|  +---------------------------------------------------------+            |
|  |                        POD                               |            |
|  |  +---------+  +---------+  +---------+                 |            |
|  |  |   App   |  | Sidecar |  |  Init   |                 |            |
|  |  |Container|  |Container|  |Container|                 |            |
|  |  +---------+  +---------+  +---------+                 |            |
|  |       |             |            |                      |            |
|  |       +-------------+------------+                      |            |
|  |              localhost (127.0.0.1)                      |            |
|  |              shared volumes                             |            |
|  +---------------------------------------------------------+            |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Teknisk Djupdykning

### Pod Anatomy

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  namespace: default
  labels:
    app: myapp
    environment: production
    version: v1.0.0
  annotations:
    description: "Main application pod"
    maintainer: "team@example.com"
spec:
  # Scheduling
  nodeName: worker-1                    # Specifik node
  nodeSelector:                         # Label-baserad
    disk: ssd

  # Restart policy
  restartPolicy: Always                 # Always, OnFailure, Never

  # Grace period
  terminationGracePeriodSeconds: 30

  # Service Account
  serviceAccountName: app-sa

  # Security Context (pod-level)
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000

  # Containers
  containers:
    - name: app
      image: myapp:v1.0.0
      imagePullPolicy: IfNotPresent     # Always, Never, IfNotPresent

      # Ports
      ports:
        - name: http
          containerPort: 8080
          protocol: TCP

      # Environment Variables
      env:
        - name: DB_HOST
          value: "postgres.default.svc"
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password

      # Resource Management
      resources:
        requests:                        # Minsta garanterade
          memory: "128Mi"
          cpu: "100m"
        limits:                          # Maximum
          memory: "256Mi"
          cpu: "500m"

      # Health Checks
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 15
        periodSeconds: 10

      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 5

      # Volume Mounts
      volumeMounts:
        - name: config
          mountPath: /etc/app/config
          readOnly: true
        - name: data
          mountPath: /data

  # Volumes
  volumes:
    - name: config
      configMap:
        name: app-config
    - name: data
      persistentVolumeClaim:
        claimName: app-data-pvc
```

### Pod Lifecycle

```
+-------------------------------------------------------------------------+
|                         POD LIFECYCLE                                    |
+-------------------------------------------------------------------------+
|                                                                          |
|  Pod Created                                                             |
|      |                                                                   |
|      ▼                                                                   |
|  +---------+                                                            |
|  | Pending | ◀-- Väntar på scheduling, image pull, etc.                |
|  +----+----+                                                            |
|       |                                                                  |
|       ▼                                                                  |
|  +--------------------------------------------------------------+       |
|  |                    Init Containers                            |       |
|  |  +---------+    +---------+    +---------+                  |       |
|  |  | init-1  |---▶| init-2  |---▶| init-3  |                  |       |
|  |  +---------+    +---------+    +---------+                  |       |
|  |       |              |              |                         |       |
|  |    Success       Success        Success                       |       |
|  +--------------------------------------------------------------+       |
|       |                                                                  |
|       ▼                                                                  |
|  +---------+                                                            |
|  | Running | ◀-- Alla containers kör                                   |
|  +----+----+                                                            |
|       |                                                                  |
|       +---------------+----------------+                                |
|       ▼               ▼                ▼                                 |
|  +----------+   +----------+   +-----------+                           |
|  |Succeeded |   |  Failed  |   |  Unknown  |                           |
|  | (Jobs)   |   | (Crash)  |   |(Node lost)|                           |
|  +----------+   +----------+   +-----------+                           |
|                                                                          |
|  Pod Phases:                                                             |
|  • Pending:   Accepterad, väntar på scheduling                          |
|  • Running:   Bound till node, minst en container kör                   |
|  • Succeeded: Alla containers avslutade OK (exit 0)                     |
|  • Failed:    Minst en container avslutade med fel                      |
|  • Unknown:   Kan inte hämta status (oftast node-problem)               |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 3. Pod-typer

### Single Container Pod (Vanligast)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.24-alpine
      ports:
        - containerPort: 80
      resources:
        requests:
          memory: "64Mi"
          cpu: "50m"
        limits:
          memory: "128Mi"
          cpu: "100m"
```

### Multi-Container Pod (Sidecar Pattern)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
  labels:
    app: myapp
spec:
  containers:
    # Main application
    - name: app
      image: myapp:v1
      ports:
        - containerPort: 8080
      volumeMounts:
        - name: logs
          mountPath: /var/log/app

    # Sidecar: Log shipper
    - name: log-shipper
      image: fluentd:v1.14
      volumeMounts:
        - name: logs
          mountPath: /var/log/app
          readOnly: true
        - name: fluentd-config
          mountPath: /etc/fluentd

    # Sidecar: Metrics exporter
    - name: metrics
      image: prom/statsd-exporter
      ports:
        - containerPort: 9102

  volumes:
    - name: logs
      emptyDir: {}
    - name: fluentd-config
      configMap:
        name: fluentd-config
```

### Init Container Pattern

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-init
spec:
  initContainers:
    # Vänta på databas
    - name: wait-for-db
      image: busybox:1.36
      command: ['sh', '-c', 'until nc -z postgres 5432; do sleep 2; done']

    # Migrera databas
    - name: db-migrate
      image: myapp-migrations:v1
      command: ['./migrate.sh', 'up']
      env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url

    # Ladda config från extern källa
    - name: config-loader
      image: curlimages/curl
      command: ['sh', '-c', 'curl -o /config/app.json http://config-service/config']
      volumeMounts:
        - name: config
          mountPath: /config

  containers:
    - name: app
      image: myapp:v1
      volumeMounts:
        - name: config
          mountPath: /etc/app

  volumes:
    - name: config
      emptyDir: {}
```

## 4. Pod Management

### Skapa Pods

```bash
# Imperativt (snabbt för test)
kubectl run nginx --image=nginx:1.24
kubectl run busybox --image=busybox --rm -it -- sh

# Declarativt (rekommenderat)
kubectl apply -f pod.yaml

# Från stdin
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: quick-pod
spec:
  containers:
    - name: nginx
      image: nginx
EOF

# Dry-run för att generera YAML
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
```

### Inspektera Pods

```bash
# Lista pods
kubectl get pods
kubectl get pods -o wide                    # Med IP och node
kubectl get pods -o yaml                    # Full spec
kubectl get pods --show-labels              # Med labels

# Detaljerad information
kubectl describe pod nginx

# Pod logs
kubectl logs nginx                          # Alla logs
kubectl logs nginx --tail=100               # Senaste 100 rader
kubectl logs nginx -f                       # Follow
kubectl logs nginx -c sidecar               # Specifik container
kubectl logs nginx --previous               # Förra container (om crashad)

# Resursanvändning
kubectl top pod nginx
kubectl top pods --containers               # Per container
```

### Interagera med Pods

```bash
# Kör kommando i pod
kubectl exec nginx -- ls /etc/nginx
kubectl exec nginx -- cat /etc/nginx/nginx.conf

# Interaktiv shell
kubectl exec -it nginx -- /bin/bash
kubectl exec -it nginx -c sidecar -- /bin/sh

# Port forward
kubectl port-forward pod/nginx 8080:80
kubectl port-forward pod/nginx 8080:80 &    # Bakgrund

# Kopiera filer
kubectl cp nginx:/etc/nginx/nginx.conf ./nginx.conf
kubectl cp ./config.json nginx:/etc/config/

# Debug pod
kubectl debug -it nginx --image=busybox --target=nginx
```

### Ta bort Pods

```bash
# Ta bort specifik pod
kubectl delete pod nginx

# Force delete (om pod hänger)
kubectl delete pod nginx --grace-period=0 --force

# Ta bort alla pods i namespace
kubectl delete pods --all -n development

# Ta bort pods med label
kubectl delete pods -l app=test
```

## 5. Praktiska Övningar

### Övning 1: Skapa och utforska en Pod

```bash
# Skapa en enkel pod
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: exploration-pod
  labels:
    purpose: learning
spec:
  containers:
    - name: main
      image: nginx:1.24
      ports:
        - containerPort: 80
      resources:
        requests:
          memory: "64Mi"
          cpu: "50m"
        limits:
          memory: "128Mi"
          cpu: "100m"
EOF

# Utforska
kubectl get pod exploration-pod -o yaml | head -50
kubectl describe pod exploration-pod
kubectl logs exploration-pod
kubectl exec -it exploration-pod -- /bin/bash
```

### Övning 2: Multi-container Pod

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-demo
spec:
  containers:
    - name: writer
      image: busybox
      command: ['sh', '-c', 'while true; do echo "$(date) - Hello from writer" >> /shared/log.txt; sleep 5; done']
      volumeMounts:
        - name: shared-data
          mountPath: /shared

    - name: reader
      image: busybox
      command: ['sh', '-c', 'tail -f /shared/log.txt']
      volumeMounts:
        - name: shared-data
          mountPath: /shared

  volumes:
    - name: shared-data
      emptyDir: {}
EOF

# Se logs från reader
kubectl logs multi-container-demo -c reader -f
```

## 6. Vanliga Fel & Lösningar

### ImagePullBackOff

```bash
# Symptom
kubectl get pods
# NAME   READY   STATUS             RESTARTS   AGE
# app    0/1     ImagePullBackOff   0          2m

# Diagnos
kubectl describe pod app | grep -A5 Events

# Vanliga orsaker:
# 1. Fel image-namn
# 2. Image finns inte
# 3. Autentisering krävs

# Lösning 1: Rätt image-namn
kubectl set image pod/app app=nginx:1.24

# Lösning 2: Lägg till image pull secret
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=pass

# Använd i pod spec:
# spec:
#   imagePullSecrets:
#     - name: regcred
```

### CrashLoopBackOff

```bash
# Symptom
kubectl get pods
# NAME   READY   STATUS             RESTARTS   AGE
# app    0/1     CrashLoopBackOff   5          10m

# Diagnos
kubectl logs app --previous     # Logs från förra körningen
kubectl describe pod app        # Events

# Vanliga orsaker:
# 1. Applikationen crashar
# 2. Fel command/args
# 3. Missing environment variables
# 4. OOMKilled (minne)

# Lösning: Debug
kubectl run debug --image=app:v1 --rm -it -- /bin/sh
```

### Pending Pod

```bash
# Symptom
kubectl get pods
# NAME   READY   STATUS    RESTARTS   AGE
# app    0/1     Pending   0          5m

# Diagnos
kubectl describe pod app

# Vanliga orsaker och lösningar:

# 1. Insufficient resources
kubectl describe nodes | grep -A5 "Allocated resources"
# Lösning: Minska requests eller lägg till noder

# 2. Node selector matchar ingen node
kubectl get nodes --show-labels
# Lösning: Fixa nodeSelector eller lägg till label på node

# 3. PVC pending
kubectl get pvc
# Lösning: Skapa PV eller StorageClass
```

## 7. Best Practices

```
+-------------------------------------------------------------------------+
|                      POD BEST PRACTICES                                  |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Design                                                               |
|     □ En container per pod (såvida inte sidecar)                        |
|     □ Stateless om möjligt                                              |
|     □ Graceful shutdown (SIGTERM handling)                              |
|     □ Logs till stdout/stderr                                           |
|                                                                          |
|  ✅ Resources                                                           |
|     □ ALLTID sätt requests och limits                                   |
|     □ Requests = genomsnittlig användning                               |
|     □ Limits = maximal användning                                       |
|     □ Undvik limit >> request (bursting)                                |
|                                                                          |
|  ✅ Health Checks                                                       |
|     □ ALLTID definiera liveness och readiness probes                    |
|     □ Readiness: Redo att ta emot trafik                                |
|     □ Liveness: Behöver omstartas?                                      |
|     □ Startup probe för långsamma startups                              |
|                                                                          |
|  ✅ Security                                                            |
|     □ runAsNonRoot: true                                                |
|     □ readOnlyRootFilesystem: true                                      |
|     □ Undvik privileged: true                                           |
|     □ Använd securityContext                                            |
|                                                                          |
|  ✅ Labels & Annotations                                                |
|     □ app: applikationsnamn                                             |
|     □ version: v1.0.0                                                   |
|     □ environment: production                                           |
|     □ team: platform                                                    |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 8. Resource Requests vs Limits

```
+-------------------------------------------------------------------------+
|                   RESOURCE REQUESTS VS LIMITS                            |
+-------------------------------------------------------------------------+
|                                                                          |
|  Requests: Garanterad resurs. Scheduler använder för placement.         |
|  Limits: Maximum resurs. Överskridande -> throttling/OOMKill            |
|                                                                          |
|  CPU (millicores):                                                       |
|  +------------------------------------------------------+               |
|  |                                                       |               |
|  |  request: 100m         limit: 500m                   |               |
|  |      |                     |                          |               |
|  |      ▼                     ▼                          |               |
|  |  +-----------------------------------------------+   |               |
|  |  |########░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|        |               |
|  |  |100m    |                              500m|        |               |
|  |  |garanterad         kan bursta till      |        |               |
|  |  +-----------------------------------------------+   |               |
|  |                                                       |               |
|  |  Om över limit: CPU throttling (långsammare)         |               |
|  +------------------------------------------------------+               |
|                                                                          |
|  Memory (bytes):                                                         |
|  +------------------------------------------------------+               |
|  |                                                       |               |
|  |  request: 128Mi        limit: 256Mi                  |               |
|  |      |                     |                          |               |
|  |      ▼                     ▼                          |               |
|  |  +-----------------------------------------------+   |               |
|  |  |################░░░░░░░░░░░░░░░░░░░░░|            |               |
|  |  |128Mi          |                    256Mi|            |               |
|  |  |garanterad     kan använda mer          |            |               |
|  |  +-----------------------------------------------+   |               |
|  |                                                       |               |
|  |  Om över limit: OOMKilled (container dödas)          |               |
|  +------------------------------------------------------+               |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 9. Verkliga Scenarion

### Scenario: Production-ready Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: production-api
  labels:
    app: api
    version: v2.1.0
    environment: production
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "9090"
spec:
  serviceAccountName: api-service-account

  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000

  containers:
    - name: api
      image: company/api:v2.1.0

      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL

      ports:
        - name: http
          containerPort: 8080
        - name: metrics
          containerPort: 9090

      env:
        - name: LOG_LEVEL
          value: "info"
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: api-config
              key: db_host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: api-secrets
              key: db_password

      resources:
        requests:
          memory: "256Mi"
          cpu: "200m"
        limits:
          memory: "512Mi"
          cpu: "1000m"

      livenessProbe:
        httpGet:
          path: /health/live
          port: http
        initialDelaySeconds: 30
        periodSeconds: 10
        timeoutSeconds: 5
        failureThreshold: 3

      readinessProbe:
        httpGet:
          path: /health/ready
          port: http
        initialDelaySeconds: 5
        periodSeconds: 5
        timeoutSeconds: 3
        failureThreshold: 3

      volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: config
          mountPath: /etc/api
          readOnly: true

  volumes:
    - name: tmp
      emptyDir: {}
    - name: config
      configMap:
        name: api-config

  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 100
          podAffinityTerm:
            labelSelector:
              matchLabels:
                app: api
            topologyKey: kubernetes.io/hostname

  terminationGracePeriodSeconds: 60
```

## 10-14. Sammanfattning & Task

### Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **Pod** | Minsta deployerbara enhet |
| **Containers** | En eller flera per pod |
| **Resources** | requests & limits |
| **Probes** | liveness, readiness, startup |
| **Lifecycle** | Pending -> Running -> Succeeded/Failed |

### Praktisk Task

```bash
# Skapa en production-ready pod med:
# 1. Resource limits
# 2. Health probes
# 3. Security context
# 4. ConfigMap environment

# Verifiera att allt fungerar!
kubectl get pod -o yaml | grep -A20 spec
```

---

**Nästa Node:** Deployments - Replica Management ->
''',
    "xp_reward": 155,
    "estimated_minutes": 60,
    "prerequisites": ["k8s_node_2"],
    "learning_outcomes": [
        "Förstå Pod-konceptet djupgående",
        "Skapa single och multi-container pods",
        "Implementera health probes",
        "Hantera pod resources"
    ]
}

NODE_4 = {
    "id": "k8s_node_4",
    "title": "Deployments - Replica Management & Updates",
    "slug": "deployments-replica-management-updates",
    "content": r'''# 🚀 Deployments - Replica Management & Updates

## 1. Introduktion & Kontext

Deployments är den rekommenderade metoden för att hantera stateless applikationer i Kubernetes. De tillhandahåller declarative updates, rolling deployments, och rollback-funktionalitet.

### Deployment vs Pod

```
+-------------------------------------------------------------------------+
|                     DEPLOYMENT VS POD                                    |
+-------------------------------------------------------------------------+
|                                                                          |
|  Direkt Pod:                                                             |
|  +-----------------------------------------+                            |
|  |               POD                        |                            |
|  |  • Ingen self-healing                   |                            |
|  |  • Ingen skalning                       |                            |
|  |  • Ingen rolling updates                |                            |
|  |  • Pod dör -> Stay dead                  |                            |
|  +-----------------------------------------+                            |
|                                                                          |
|  Via Deployment:                                                         |
|  +-----------------------------------------------------------------+   |
|  |                      DEPLOYMENT                                  |   |
|  |  +-----------------------------------------------------------+  |   |
|  |  |                    REPLICASET                              |  |   |
|  |  |  +---------+  +---------+  +---------+                   |  |   |
|  |  |  |  POD 1  |  |  POD 2  |  |  POD 3  |                   |  |   |
|  |  |  +---------+  +---------+  +---------+                   |  |   |
|  |  +-----------------------------------------------------------+  |   |
|  |  • Self-healing (pod dör -> ny skapas)                           |   |
|  |  • Skalning (replicas: 3 -> 10)                                  |   |
|  |  • Rolling updates (zero downtime)                              |   |
|  |  • Rollback (kubectl rollout undo)                              |   |
|  +-----------------------------------------------------------------+   |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Deployment Anatomy

### Fullständig Deployment Spec

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  namespace: production
  labels:
    app: api-server
    version: v2.0.0
  annotations:
    kubernetes.io/change-cause: "Update to v2.0.0 with new features"
spec:
  # Antal replicas
  replicas: 3

  # Revision history för rollbacks
  revisionHistoryLimit: 10

  # Deployment strategi
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1          # Extra pods under update
      maxUnavailable: 0    # Alltid minst replicas tillgängliga

  # Selector måste matcha template labels
  selector:
    matchLabels:
      app: api-server

  # Pod template
  template:
    metadata:
      labels:
        app: api-server
        version: v2.0.0
      annotations:
        prometheus.io/scrape: "true"
    spec:
      containers:
        - name: api
          image: company/api:v2.0.0
          ports:
            - containerPort: 8080
          resources:
            requests:
              memory: "256Mi"
              cpu: "200m"
            limits:
              memory: "512Mi"
              cpu: "1000m"
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
```

## 3. Deployment Strategies

### RollingUpdate (Default)

```
+-------------------------------------------------------------------------+
|                    ROLLING UPDATE STRATEGY                               |
+-------------------------------------------------------------------------+
|                                                                          |
|  Initial State (v1):                                                     |
|  +---------+  +---------+  +---------+                                 |
|  | Pod v1  |  | Pod v1  |  | Pod v1  |                                 |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
|  Step 1: Skapa ny pod (maxSurge: 1)                                     |
|  +---------+  +---------+  +---------+  +---------+                    |
|  | Pod v1  |  | Pod v1  |  | Pod v1  |  | Pod v2  | <- Creating         |
|  +---------+  +---------+  +---------+  +---------+                    |
|                                                                          |
|  Step 2: Ta bort gammal pod                                             |
|  +---------+  +---------+  +---------+                                 |
|  | Pod v1  |  | Pod v1  |  | Pod v2  |                                 |
|  +---------+  +---------+  +---------+  (v1 terminated)                |
|                                                                          |
|  Step 3-4: Upprepa                                                      |
|  +---------+  +---------+  +---------+                                 |
|  | Pod v2  |  | Pod v2  |  | Pod v2  |                                 |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
|  Configuration:                                                          |
|  strategy:                                                               |
|    type: RollingUpdate                                                  |
|    rollingUpdate:                                                       |
|      maxSurge: 25%        # 25% extra pods under update                |
|      maxUnavailable: 25%  # 25% kan vara unavailable                   |
|                                                                          |
+-------------------------------------------------------------------------+
```

### Recreate Strategy

```
+-------------------------------------------------------------------------+
|                      RECREATE STRATEGY                                   |
+-------------------------------------------------------------------------+
|                                                                          |
|  Initial State:                                                          |
|  +---------+  +---------+  +---------+                                 |
|  | Pod v1  |  | Pod v1  |  | Pod v1  |                                 |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
|  Step 1: Terminera alla (DOWNTIME!)                                     |
|  +---------+  +---------+  +---------+                                 |
|  |Terminat |  |Terminat |  |Terminat |                                 |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
|  Step 2: Skapa nya                                                       |
|  +---------+  +---------+  +---------+                                 |
|  | Pod v2  |  | Pod v2  |  | Pod v2  |                                 |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
|  ⚠️  Användning: Endast när man INTE kan ha flera versioner samtidigt   |
|                                                                          |
|  Configuration:                                                          |
|  strategy:                                                               |
|    type: Recreate                                                       |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 4. Deployment Operations

### Skapa & Uppdatera

```bash
# Skapa deployment
kubectl apply -f deployment.yaml

# Imperativ skapning (för test)
kubectl create deployment nginx --image=nginx:1.24

# Uppdatera image
kubectl set image deployment/api-server api=company/api:v2.1.0

# Uppdatera med annotation (för history)
kubectl set image deployment/api-server api=company/api:v2.1.0 \
  --record  # Deprecated men fungerar

# Bättre: Använd annotate
kubectl annotate deployment api-server \
  kubernetes.io/change-cause="Upgrade to v2.1.0 - fix memory leak"
```

### Skalning

```bash
# Manuell skalning
kubectl scale deployment api-server --replicas=5

# Conditional scaling
kubectl scale deployment api-server --replicas=10 --current-replicas=5

# Autoscaling (HPA)
kubectl autoscale deployment api-server \
  --min=3 \
  --max=10 \
  --cpu-percent=70
```

### Rollout Management

```bash
# Rollout status
kubectl rollout status deployment/api-server

# Rollout history
kubectl rollout history deployment/api-server

# Visa specifik revision
kubectl rollout history deployment/api-server --revision=3

# Pausa rollout
kubectl rollout pause deployment/api-server

# Återuppta rollout
kubectl rollout resume deployment/api-server

# Rollback
kubectl rollout undo deployment/api-server

# Rollback till specifik revision
kubectl rollout undo deployment/api-server --to-revision=2

# Restart all pods (same image)
kubectl rollout restart deployment/api-server
```

## 5. ReplicaSet Relationship

```
+-------------------------------------------------------------------------+
|                DEPLOYMENT -> REPLICASET -> PODS                            |
+-------------------------------------------------------------------------+
|                                                                          |
|  kubectl get all -l app=api-server                                      |
|                                                                          |
|  NAME                             READY   STATUS    RESTARTS   AGE      |
|  pod/api-server-7d9f8c6b5-abc12  1/1     Running   0          5m       |
|  pod/api-server-7d9f8c6b5-def34  1/1     Running   0          5m       |
|  pod/api-server-7d9f8c6b5-ghi56  1/1     Running   0          5m       |
|                                                                          |
|  NAME                        READY   UP-TO-DATE   AVAILABLE   AGE      |
|  deployment.apps/api-server  3/3     3            3           10m      |
|                                                                          |
|  NAME                                   DESIRED   CURRENT   READY  AGE |
|  replicaset.apps/api-server-7d9f8c6b5  3         3         3      5m  |
|  replicaset.apps/api-server-6c7d5e4f3  0         0         0      10m |
|                   ↑                                                     |
|                   | Gammal ReplicaSet (för rollback)                   |
|                                                                          |
|  Hierarki:                                                              |
|  +--------------+                                                       |
|  |  Deployment  | ---- Hanterar ReplicaSets                            |
|  +------+-------+                                                       |
|         |                                                               |
|         ▼                                                               |
|  +--------------+                                                       |
|  |  ReplicaSet  | ---- Hanterar Pods (aktuell version)                 |
|  +------+-------+                                                       |
|         |                                                               |
|         ▼                                                               |
|  +-----+ +-----+ +-----+                                               |
|  | Pod | | Pod | | Pod |                                               |
|  +-----+ +-----+ +-----+                                               |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 6. Praktiska Övningar

### Övning 1: Blue-Green Deployment Simulation

```bash
# Skapa "blue" deployment
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
  labels:
    app: myapp
    version: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    metadata:
      labels:
        app: myapp
        version: blue
    spec:
      containers:
        - name: app
          image: nginx:1.23
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
    version: blue    # Points to blue
  ports:
    - port: 80
EOF

# Deploya "green" version
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-green
  labels:
    app: myapp
    version: green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: green
  template:
    metadata:
      labels:
        app: myapp
        version: green
    spec:
      containers:
        - name: app
          image: nginx:1.24
          ports:
            - containerPort: 80
EOF

# Byt trafik till green
kubectl patch service myapp -p '{"spec":{"selector":{"version":"green"}}}'

# Rollback till blue
kubectl patch service myapp -p '{"spec":{"selector":{"version":"blue"}}}'
```

### Övning 2: Canary Deployment

```bash
# Stable deployment (90% trafik)
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-stable
spec:
  replicas: 9
  selector:
    matchLabels:
      app: myapp
      track: stable
  template:
    metadata:
      labels:
        app: myapp
        track: stable
    spec:
      containers:
        - name: app
          image: nginx:1.23
---
# Canary deployment (10% trafik)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-canary
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
      track: canary
  template:
    metadata:
      labels:
        app: myapp
        track: canary
    spec:
      containers:
        - name: app
          image: nginx:1.24
---
# Service selects both
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp    # Selects both stable AND canary
  ports:
    - port: 80
EOF

# Öka canary gradvis
kubectl scale deployment app-canary --replicas=3
kubectl scale deployment app-stable --replicas=7
```

## 7. Vanliga Fel & Lösningar

### Deployment Stuck

```bash
# Symptom
kubectl rollout status deployment/api-server
# Waiting for deployment "api-server" rollout to finish: 1 old replicas pending termination...

# Diagnos
kubectl get pods -l app=api-server
kubectl describe deployment api-server

# Orsaker:
# 1. Readiness probe failing
# 2. Resource constraints
# 3. Image pull errors
# 4. PDB blocking

# Lösning
kubectl describe pod <pod-name>    # Se events
kubectl logs <pod-name>            # Se app logs
kubectl rollout undo deployment/api-server  # Rollback om nödvändigt
```

### Pods Not Starting

```bash
# Diagnos
kubectl get events --sort-by='.lastTimestamp' | tail -20
kubectl describe pod <pod-name>

# Vanliga fel:
# - FailedScheduling: Resource constraints
# - ImagePullBackOff: Wrong image or auth
# - CrashLoopBackOff: App crashing

# Snabb debug
kubectl run debug --image=busybox -it --rm -- sh
```

## 8. Best Practices

```
+-------------------------------------------------------------------------+
|                   DEPLOYMENT BEST PRACTICES                              |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Replicas & Availability                                             |
|     □ Minst 2 replicas för produktion                                   |
|     □ Använd PodDisruptionBudget                                        |
|     □ Sprid pods över noder (podAntiAffinity)                           |
|     □ Sätt revisionHistoryLimit (default 10)                            |
|                                                                          |
|  ✅ Updates                                                             |
|     □ Använd RollingUpdate (default)                                    |
|     □ maxSurge: 25%, maxUnavailable: 25%                               |
|     □ Alltid readiness probes                                           |
|     □ Sätt minReadySeconds (30-60s för stabilitet)                      |
|                                                                          |
|  ✅ Rollbacks                                                           |
|     □ Annotera deployments (change-cause)                               |
|     □ Testa rollback-procedur                                           |
|     □ Behåll tillräcklig revision history                               |
|                                                                          |
|  ✅ Images                                                              |
|     □ Använd specifika tags, ALDRIG :latest                             |
|     □ Använd image digest för reproducerbarhet                          |
|     □ imagePullPolicy: IfNotPresent                                     |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 9. Production Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: production-api
  namespace: production
  labels:
    app.kubernetes.io/name: api
    app.kubernetes.io/version: "2.1.0"
    app.kubernetes.io/component: backend
  annotations:
    kubernetes.io/change-cause: "v2.1.0 - Performance improvements"
spec:
  replicas: 5
  revisionHistoryLimit: 5

  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0

  minReadySeconds: 30
  progressDeadlineSeconds: 600

  selector:
    matchLabels:
      app.kubernetes.io/name: api

  template:
    metadata:
      labels:
        app.kubernetes.io/name: api
        app.kubernetes.io/version: "2.1.0"
    spec:
      serviceAccountName: api-sa

      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000

      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchLabels:
                  app.kubernetes.io/name: api
              topologyKey: kubernetes.io/hostname

      containers:
        - name: api
          image: company/api:v2.1.0@sha256:abc123...
          imagePullPolicy: IfNotPresent

          ports:
            - name: http
              containerPort: 8080
            - name: metrics
              containerPort: 9090

          resources:
            requests:
              memory: "256Mi"
              cpu: "200m"
            limits:
              memory: "512Mi"
              cpu: "1000m"

          livenessProbe:
            httpGet:
              path: /health/live
              port: http
            initialDelaySeconds: 30
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3

          readinessProbe:
            httpGet:
              path: /health/ready
              port: http
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3

          startupProbe:
            httpGet:
              path: /health/startup
              port: http
            failureThreshold: 30
            periodSeconds: 10

          envFrom:
            - configMapRef:
                name: api-config
          env:
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: db_password

          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL

          volumeMounts:
            - name: tmp
              mountPath: /tmp

      volumes:
        - name: tmp
          emptyDir: {}

      terminationGracePeriodSeconds: 60
```

## 10-14. Sammanfattning & Task

### Sammanfattning

| Feature | Beskrivning |
|---------|-------------|
| **Replicas** | Antal pod-kopior |
| **Strategy** | RollingUpdate eller Recreate |
| **Rollback** | `kubectl rollout undo` |
| **History** | revisionHistoryLimit |
| **Scaling** | Manuell eller HPA |

### Praktisk Task

```bash
# 1. Skapa deployment med 3 replicas
# 2. Uppdatera image och observera rolling update
# 3. Kolla rollout history
# 4. Gör rollback
# 5. Sätt upp autoscaling

kubectl create deployment myapp --image=nginx:1.23 --replicas=3
kubectl set image deployment/myapp nginx=nginx:1.24
kubectl rollout history deployment/myapp
kubectl rollout undo deployment/myapp
kubectl autoscale deployment myapp --min=3 --max=10 --cpu-percent=70
```

---

**Nästa Node:** Services - Networking & Load Balancing ->
''',
    "xp_reward": 160,
    "estimated_minutes": 65,
    "prerequisites": ["k8s_node_3"],
    "learning_outcomes": [
        "Förstå Deployment-konceptet",
        "Implementera rolling updates",
        "Hantera rollbacks",
        "Konfigurera deployment strategies"
    ]
}

# Block 1 Part 2 exports
BLOCK_1_PART_2_NODES = [NODE_3, NODE_4]
