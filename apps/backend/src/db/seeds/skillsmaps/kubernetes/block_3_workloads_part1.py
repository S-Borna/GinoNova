# =============================================================================
# KUBERNETES MASTERY - BLOCK 3 PART 1: STATEFULSETS & JOBS
# Noder 9-10 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 3 PART 1 - STATEFUL WORKLOADS
=============================================
Node 9: StatefulSets - Stateful Applications
Node 10: Jobs & CronJobs - Batch Processing
"""

NODE_9 = {
    "id": "k8s_node_9",
    "title": "StatefulSets - Stateful Applications",
    "slug": "statefulsets-stateful-applications",
    "content": r'''# 🗄️ StatefulSets - Stateful Applications

## 1. Introduktion & Kontext

StatefulSets är för applikationer som kräver stabil identitet, persistent storage, och ordnad deployment/skalning. Typiska användningsområden inkluderar databaser, message queues, och distribuerade system som kräver koordinering.

### StatefulSet vs Deployment

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 STATEFULSET VS DEPLOYMENT                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DEPLOYMENT (Stateless)                                                  │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Pods har:                                                       │   │
│  │  • Random namn (nginx-7d9f8c6b5-abc12)                          │   │
│  │  • Delat storage (alla läser samma PVC)                         │   │
│  │  • Parallell start/stop                                         │   │
│  │  • Random DNS (via Service)                                     │   │
│  │                                                                  │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                         │   │
│  │  │nginx-abc│  │nginx-def│  │nginx-ghi│  ← Interchangeable       │   │
│  │  └─────────┘  └─────────┘  └─────────┘                         │   │
│  │       │            │            │                               │   │
│  │       └────────────┼────────────┘                               │   │
│  │                    │                                             │   │
│  │              ┌─────▼─────┐                                      │   │
│  │              │Shared PVC │                                      │   │
│  │              └───────────┘                                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  STATEFULSET (Stateful)                                                  │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Pods har:                                                       │   │
│  │  • Stabil ordningstal (postgres-0, postgres-1, postgres-2)      │   │
│  │  • Eget storage (varje pod har egen PVC)                        │   │
│  │  • Sekventiell start/stop (0 före 1 före 2)                     │   │
│  │  • Stabil DNS (postgres-0.postgres-svc.ns.svc.cluster.local)    │   │
│  │                                                                  │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │   │
│  │  │postgres-0│  │postgres-1│  │postgres-2│  ← Unique identity   │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘                      │   │
│  │       │             │             │                             │   │
│  │  ┌────▼────┐   ┌────▼────┐   ┌────▼────┐                       │   │
│  │  │ PVC-0   │   │ PVC-1   │   │ PVC-2   │  ← Dedicated storage  │   │
│  │  └─────────┘   └─────────┘   └─────────┘                       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. StatefulSet Guarantees

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    STATEFULSET GUARANTEES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. STABLE POD IDENTITY                                                  │
│     Pod names: <statefulset-name>-<ordinal>                             │
│     postgres-0, postgres-1, postgres-2...                               │
│                                                                          │
│  2. STABLE NETWORK IDENTITY                                             │
│     DNS: <pod-name>.<service-name>.<namespace>.svc.cluster.local        │
│     postgres-0.postgres-headless.default.svc.cluster.local              │
│                                                                          │
│  3. STABLE STORAGE                                                       │
│     Varje pod får egen PVC som följer med även efter pod-restart        │
│     PVC-namn: <volumeClaimTemplate-name>-<statefulset-name>-<ordinal>   │
│     data-postgres-0, data-postgres-1, data-postgres-2                   │
│                                                                          │
│  4. ORDERED DEPLOYMENT & SCALING                                        │
│     Start:  0 → 1 → 2 (väntar tills föregående är Ready)               │
│     Scale down: 2 → 1 → 0                                               │
│     Delete: 2 → 1 → 0                                                   │
│                                                                          │
│  5. ORDERED ROLLING UPDATES                                             │
│     Update: 2 → 1 → 0 (högst ordinal först)                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. StatefulSet Anatomy

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: database
spec:
  # Service som hanterar nätverksidentitet
  serviceName: postgres-headless      # REQUIRED

  # Antal replicas
  replicas: 3

  # Pod Management Policy
  podManagementPolicy: OrderedReady   # OrderedReady | Parallel

  # Update Strategy
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 0                    # Pods >= partition uppdateras

  # Selector
  selector:
    matchLabels:
      app: postgres

  # Pod Template
  template:
    metadata:
      labels:
        app: postgres
    spec:
      terminationGracePeriodSeconds: 30

      containers:
        - name: postgres
          image: postgres:15

          ports:
            - name: postgres
              containerPort: 5432

          env:
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: password

            # Pod identity som env var
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name

          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql/data

          livenessProbe:
            exec:
              command: ["pg_isready", "-U", "postgres"]
            initialDelaySeconds: 30
            periodSeconds: 10

          readinessProbe:
            exec:
              command: ["pg_isready", "-U", "postgres"]
            initialDelaySeconds: 5
            periodSeconds: 5

  # Volume Claim Templates - varje pod får egen PVC!
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        storageClassName: fast-ssd
        resources:
          requests:
            storage: 10Gi
```

## 4. Headless Service

```yaml
# REQUIRED för StatefulSet - ger stabil DNS
apiVersion: v1
kind: Service
metadata:
  name: postgres-headless
  labels:
    app: postgres
spec:
  clusterIP: None                     # HEADLESS!
  selector:
    app: postgres
  ports:
    - name: postgres
      port: 5432
      targetPort: postgres
---
# Optional: Regular service för load balancing
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  type: ClusterIP
  selector:
    app: postgres
  ports:
    - port: 5432
      targetPort: postgres
```

### DNS Resolution

```bash
# Headless service DNS
# Ger alla pod IPs
nslookup postgres-headless.default.svc.cluster.local

# Individual pod DNS
nslookup postgres-0.postgres-headless.default.svc.cluster.local
nslookup postgres-1.postgres-headless.default.svc.cluster.local

# Användning i applikation
# Primary: postgres-0.postgres-headless.default.svc.cluster.local:5432
# Replica: postgres-1.postgres-headless.default.svc.cluster.local:5432
```

## 5. Praktiska Övningar

### Övning 1: PostgreSQL StatefulSet

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: postgres-secret
type: Opaque
stringData:
  password: mysecretpassword
---
apiVersion: v1
kind: Service
metadata:
  name: postgres-headless
spec:
  clusterIP: None
  selector:
    app: postgres
  ports:
    - port: 5432
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres-headless
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
          env:
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: password
            - name: PGDATA
              value: /var/lib/postgresql/data/pgdata
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql/data
          readinessProbe:
            exec:
              command: ["pg_isready", "-U", "postgres"]
            initialDelaySeconds: 5
            periodSeconds: 5
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
EOF

# Observera ordnad deployment
kubectl get pods -w

# Verifiera DNS
kubectl run dns-test --image=busybox --rm -it -- sh
nslookup postgres-0.postgres-headless
nslookup postgres-1.postgres-headless

# Verifiera PVCs
kubectl get pvc
```

### Övning 2: Scaling och Updates

```bash
# Scale up (observera ordning)
kubectl scale statefulset postgres --replicas=5

# Scale down (omvänd ordning)
kubectl scale statefulset postgres --replicas=3

# Rolling update (partition for canary)
kubectl patch statefulset postgres -p '{"spec":{"updateStrategy":{"rollingUpdate":{"partition":2}}}}'
kubectl set image statefulset/postgres postgres=postgres:16

# Endast postgres-2 uppdateras (partition >= 2)
kubectl get pods -l app=postgres -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.containers[0].image}{"\n"}{end}'

# Fullständig rollout
kubectl patch statefulset postgres -p '{"spec":{"updateStrategy":{"rollingUpdate":{"partition":0}}}}'
```

## 6. Vanliga Fel & Lösningar

### Pod Stuck in Pending

```bash
# Symptom: postgres-1 startar inte

# Diagnos
kubectl describe pod postgres-1
kubectl get pvc

# Vanlig orsak: PVC kan inte bindas
# Lösning: Kontrollera StorageClass och PV availability
kubectl get storageclass
kubectl get pv
```

### Data Loss vid Delete

```bash
# ⚠️ VIKTIGT: PVCs raderas INTE automatiskt
kubectl delete statefulset postgres
kubectl get pvc    # PVCs finns kvar!

# För att radera allt (FARLIGT!)
kubectl delete statefulset postgres --cascade=orphan  # Behåll pods
kubectl delete pvc -l app=postgres                    # Radera PVCs
```

## 7. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   STATEFULSET BEST PRACTICES                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Design                                                               │
│     □ Använd ENDAST för stateful workloads                              │
│     □ Headless service är REQUIRED                                       │
│     □ Implementera proper health checks                                  │
│     □ Hantera leader election om nödvändigt                             │
│                                                                          │
│  ✅ Storage                                                              │
│     □ Använd StorageClass med Retain policy                             │
│     □ Testa backup/restore procedure                                    │
│     □ Övervaka disk usage                                               │
│                                                                          │
│  ✅ Updates                                                              │
│     □ Använd partition för staged rollouts                              │
│     □ Testa på staging först                                            │
│     □ Ha rollback-plan                                                  │
│                                                                          │
│  ✅ Operations                                                          │
│     □ Dokumentera startup/shutdown ordning                              │
│     □ Automatisera backup                                               │
│     □ Övervaka replication lag                                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Sammanfattning & Task

### When to Use StatefulSet

| Requirement | Use StatefulSet? |
|-------------|------------------|
| Stable pod names | ✅ Yes |
| Persistent storage per pod | ✅ Yes |
| Ordered deployment | ✅ Yes |
| Stateless web app | ❌ Use Deployment |
| Background workers | ❌ Use Deployment |

---

**Nästa Node:** Jobs & CronJobs →
''',
    "xp_reward": 160,
    "estimated_minutes": 60,
    "prerequisites": ["k8s_node_8"],
    "learning_outcomes": [
        "Förstå StatefulSet-konceptet",
        "Implementera headless services",
        "Hantera stateful workloads",
        "Konfigurera volumeClaimTemplates"
    ]
}

NODE_10 = {
    "id": "k8s_node_10",
    "title": "Jobs & CronJobs - Batch Processing",
    "slug": "jobs-cronjobs-batch-processing",
    "content": r'''# ⏰ Jobs & CronJobs - Batch Processing

## 1. Introduktion & Kontext

Jobs och CronJobs är för batch-arbeten som ska köras en gång eller enligt schema. Till skillnad från Deployments som kör kontinuerligt, är Jobs designade för arbeten som avslutas.

### Job vs Deployment

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      JOB VS DEPLOYMENT                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DEPLOYMENT (Long-running)                                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  restartPolicy: Always                                           │   │
│  │                                                                  │   │
│  │  Start ─────────────────────────────────────────────────▶ ∞     │   │
│  │        Kör för alltid, restart om crash                         │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  JOB (Run-to-completion)                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  restartPolicy: Never | OnFailure                                │   │
│  │                                                                  │   │
│  │  Start ────────────────────────▶ Complete ✓                     │   │
│  │        Kör tills klart, exit 0 = success                        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  CRONJOB (Scheduled Jobs)                                                │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  schedule: "0 2 * * *"                                           │   │
│  │                                                                  │   │
│  │  02:00 ──▶ Job ──▶ ✓                                            │   │
│  │  02:00 ──▶ Job ──▶ ✓   (nästa dag)                              │   │
│  │  02:00 ──▶ Job ──▶ ✓   (nästa dag)                              │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Job Types

### Simple Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-backup
spec:
  # Retry settings
  backoffLimit: 4                    # Max retries before giving up
  activeDeadlineSeconds: 3600        # Max total runtime (1 hour)

  template:
    spec:
      restartPolicy: Never           # REQUIRED: Never or OnFailure

      containers:
        - name: backup
          image: postgres:15
          command: ["pg_dump", "-h", "postgres", "-U", "admin", "-d", "mydb"]
          env:
            - name: PGPASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: password
          volumeMounts:
            - name: backup
              mountPath: /backup

      volumes:
        - name: backup
          persistentVolumeClaim:
            claimName: backup-pvc
```

### Parallel Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: process-queue
spec:
  # Parallel processing
  completions: 10                    # Total successful completions needed
  parallelism: 3                     # Max concurrent pods
  completionMode: Indexed            # NonIndexed | Indexed

  backoffLimit: 4

  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: worker
          image: myapp/worker:v1
          env:
            # JOB_COMPLETION_INDEX: 0, 1, 2, ... (med Indexed mode)
            - name: WORKER_INDEX
              valueFrom:
                fieldRef:
                  fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
```

### Work Queue Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: work-queue
spec:
  parallelism: 5                     # Antal workers
  # completions utelämnas = work queue mode

  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: worker
          image: myapp/queue-worker:v1
          # Worker hämtar arbete från kö, exit 0 när kön är tom
```

## 3. CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  # Cron schedule
  schedule: "0 2 * * *"              # Varje dag kl 02:00
  timeZone: "Europe/Stockholm"       # K8s 1.27+

  # Concurrency policy
  concurrencyPolicy: Forbid          # Allow | Forbid | Replace

  # History limits
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1

  # Deadline
  startingDeadlineSeconds: 300       # Max delay för start

  # Suspend
  suspend: false                     # true = pausad

  # Job template
  jobTemplate:
    spec:
      backoffLimit: 3
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: backup
              image: backup-tool:v1
              command: ["/backup.sh"]
```

### Cron Schedule Syntax

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      CRON SCHEDULE SYNTAX                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌───────────── minute (0 - 59)                                         │
│  │ ┌───────────── hour (0 - 23)                                         │
│  │ │ ┌───────────── day of month (1 - 31)                               │
│  │ │ │ ┌───────────── month (1 - 12)                                    │
│  │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday = 0)                │
│  │ │ │ │ │                                                               │
│  * * * * *                                                               │
│                                                                          │
│  Exempel:                                                                │
│  ────────────────────────────────────────────────────────────────────── │
│  */15 * * * *     │ Var 15:e minut                                      │
│  0 * * * *        │ Varje timme (hh:00)                                 │
│  0 0 * * *        │ Varje dag vid midnatt                               │
│  0 2 * * *        │ Varje dag kl 02:00                                  │
│  0 0 * * 0        │ Varje söndag vid midnatt                            │
│  0 0 1 * *        │ Första dagen i månaden                              │
│  0 0 1 1 *        │ 1 januari vid midnatt                               │
│  0 8-17 * * 1-5   │ Varje timme 08-17 på vardagar                       │
│  0 */2 * * *      │ Varannan timme                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Praktiska Övningar

### Övning 1: Database Backup Job

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: db-backup-manual
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: backup
          image: busybox
          command:
            - sh
            - -c
            - |
              echo "Starting backup at $(date)"
              echo "Simulating database backup..."
              sleep 10
              echo "Backup completed at $(date)"
              exit 0
EOF

# Övervaka job
kubectl get jobs -w
kubectl get pods -l job-name=db-backup-manual
kubectl logs job/db-backup-manual

# Se job completion
kubectl describe job db-backup-manual
```

### Övning 2: Parallel Processing

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel-job
spec:
  completions: 5
  parallelism: 3
  completionMode: Indexed
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: worker
          image: busybox
          command:
            - sh
            - -c
            - |
              INDEX=${JOB_COMPLETION_INDEX}
              echo "Worker $INDEX starting"
              sleep $((INDEX * 2 + 5))
              echo "Worker $INDEX completed"
EOF

# Observera parallell körning
kubectl get pods -l job-name=parallel-job -w

# Se logs från alla workers
for i in 0 1 2 3 4; do
  echo "=== Worker $i ==="
  kubectl logs parallel-job-$i
done
```

### Övning 3: CronJob Setup

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hourly-report
spec:
  schedule: "*/5 * * * *"            # Var 5:e minut (för test)
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: report
              image: busybox
              command:
                - sh
                - -c
                - |
                  echo "Report generated at $(date)"
EOF

# Övervaka
kubectl get cronjob
kubectl get jobs -w

# Manuell trigger
kubectl create job manual-report --from=cronjob/hourly-report

# Suspend cronjob
kubectl patch cronjob hourly-report -p '{"spec":{"suspend":true}}'
```

## 5. Job Completion Handling

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     JOB COMPLETION STATES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SUCCESS (exit 0)                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Job: COMPLETE                                                   │   │
│  │  Pod: Succeeded                                                  │   │
│  │                                                                  │   │
│  │  kubectl get job backup                                         │   │
│  │  NAME     COMPLETIONS   DURATION   AGE                          │   │
│  │  backup   1/1           45s        2m                           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  FAILURE (exit != 0)                                                    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  restartPolicy: OnFailure                                        │   │
│  │  → Container restarts i samma pod                               │   │
│  │  → backoffLimit kontrollerar max retries                        │   │
│  │                                                                  │   │
│  │  restartPolicy: Never                                            │   │
│  │  → Ny pod skapas för varje retry                                │   │
│  │  → backoffLimit kontrollerar max pods                           │   │
│  │                                                                  │   │
│  │  Efter backoffLimit: Job = Failed                               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6. Vanliga Fel & Lösningar

### Job Stuck in Active

```bash
# Symptom: Job aldrig completar

# Diagnos
kubectl describe job my-job
kubectl logs job/my-job

# Vanliga orsaker:
# 1. Container hänger (sätt activeDeadlineSeconds)
# 2. restartPolicy: Always (FELAKTIG för Jobs!)
# 3. Exit code != 0

# Force delete
kubectl delete job my-job
```

### CronJob Not Triggering

```bash
# Diagnos
kubectl describe cronjob my-cronjob
# Se "Last Schedule Time" och Events

# Vanliga orsaker:
# 1. suspend: true
# 2. Fel cron syntax
# 3. startingDeadlineSeconds för kort

# Manuell test
kubectl create job test-run --from=cronjob/my-cronjob
```

## 7. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   JOBS BEST PRACTICES                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Job Design                                                          │
│     □ Sätt activeDeadlineSeconds för timeout                            │
│     □ Använd backoffLimit baserat på job-typ                            │
│     □ Gör jobs idempotenta (kan köras flera gånger)                     │
│     □ Log progress för debugging                                        │
│                                                                          │
│  ✅ CronJob                                                             │
│     □ Använd concurrencyPolicy: Forbid för de flesta fall               │
│     □ Sätt startingDeadlineSeconds                                      │
│     □ Begränsa history (successfulJobsHistoryLimit)                     │
│     □ Övervaka job failures                                             │
│                                                                          │
│  ✅ Monitoring                                                          │
│     □ Alerting på job failures                                          │
│     □ Track job duration                                                │
│     □ Log centralization                                                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Sammanfattning & Task

### Job Types Summary

| Type | Use Case | Key Settings |
|------|----------|--------------|
| **Single Job** | One-time task | completions: 1 |
| **Parallel Job** | Process N items | completions: N, parallelism: M |
| **Work Queue** | Dynamic work | parallelism only |
| **CronJob** | Scheduled tasks | schedule: "* * * * *" |

### Praktisk Task

```bash
# 1. Skapa CronJob som kör var 5:e minut
# 2. Manuellt trigga en körning
# 3. Verifiera job completion
# 4. Rensa history
```

---

**Nästa Node:** DaemonSets & RBAC →
''',
    "xp_reward": 145,
    "estimated_minutes": 50,
    "prerequisites": ["k8s_node_9"],
    "learning_outcomes": [
        "Förstå Jobs och CronJobs",
        "Implementera parallel processing",
        "Konfigurera cron schedules",
        "Hantera job failures"
    ]
}

# Block 3 Part 1 exports
BLOCK_3_PART_1_NODES = [NODE_9, NODE_10]
