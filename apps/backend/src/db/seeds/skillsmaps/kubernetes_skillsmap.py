# =============================================================================
# KUBERNETES SKILLSMAP - 20 NODER
# Akhilesh Pedagogical Style: Intro → Koncept → Kommandon → Tips → Task
# =============================================================================

KUBERNETES_SKILLSMAP_INFO = {
    "name": "Kubernetes Mastery",
    "slug": "kubernetes-mastery",
    "description": "Behärska container orchestration från pods till produktion",
    "total_nodes": 20,
    "estimated_hours": 30,
    "difficulty": "advanced",
    "prerequisites": ["docker-mastery"],
    "skills": ["Kubernetes", "Pods", "Services", "Deployments", "Helm", "Networking"],
}


# =============================================================================
# BLOCK 1: K8S FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_K8S_INTRO = {
    "node_id": 1,
    "title": "Kubernetes Introduktion",
    "slug": "k8s-intro",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [],
    "content": '''
# Kubernetes Introduktion

Kubernetes (K8s) är industristandard för container orchestration.

## Varför Kubernetes?

| Behov | K8s Lösning |
|-------|-------------|
| Skalning | Auto-scaling |
| High Availability | Self-healing |
| Load Balancing | Services |
| Zero-downtime | Rolling updates |
| Secret Management | Secrets/ConfigMaps |

## Arkitektur

```
┌─────────────────────────────────────────┐
│            Control Plane                │
├─────────┬─────────┬─────────┬──────────┤
│ API     │ etcd    │Scheduler│Controller│
│ Server  │         │         │ Manager  │
└────┬────┴────┬────┴────┬────┴────┬─────┘
     │         │         │         │
┌────▼────┬────▼────┬────▼────┬────▼─────┐
│ Node 1  │ Node 2  │ Node 3  │ Node N   │
├─────────┼─────────┼─────────┼──────────┤
│ kubelet │ kubelet │ kubelet │ kubelet  │
│ pods    │ pods    │ pods    │ pods     │
└─────────┴─────────┴─────────┴──────────┘
```

## Lokalt Kluster

```bash
# Minikube
minikube start
minikube dashboard

# Kind (K8s in Docker)
kind create cluster

# Docker Desktop
# Aktivera Kubernetes i settings

# Verifiera
kubectl cluster-info
kubectl get nodes
```

**Nästa steg:** Node 2 - kubectl Basics
''',
}

NODE_02_KUBECTL_BASICS = {
    "node_id": 2,
    "title": "kubectl Basics",
    "slug": "kubectl-basics",
    "estimated_minutes": 45,
    "xp_reward": 110,
    "prerequisites": [1],
    "content": '''
# kubectl Basics

CLI-verktyget för Kubernetes.

## Grundläggande Kommandon

```bash
# Cluster info
kubectl cluster-info
kubectl get nodes

# Lista resurser
kubectl get pods
kubectl get services
kubectl get deployments
kubectl get all

# Alla namespaces
kubectl get pods -A
kubectl get pods --all-namespaces
```

## Skapa Resurser

```bash
# Imperativt
kubectl run nginx --image=nginx
kubectl create deployment web --image=nginx

# Deklarativt (rekommenderat)
kubectl apply -f deployment.yaml

# Från URL
kubectl apply -f https://example.com/manifest.yaml
```

## Inspektera

```bash
# Describe
kubectl describe pod nginx
kubectl describe node node1

# Logs
kubectl logs mypod
kubectl logs -f mypod         # Follow
kubectl logs mypod -c mycontainer  # Specifik container

# Exec
kubectl exec -it mypod -- bash
kubectl exec mypod -- ls /app
```

## Kontext & Namespace

```bash
# Byt namespace
kubectl config set-context --current --namespace=dev

# Lista contexts
kubectl config get-contexts

# Byt context
kubectl config use-context production
```

| Kommando | Beskrivning |
|----------|-------------|
| get | Lista resurser |
| describe | Detaljerad info |
| apply | Skapa/uppdatera |
| delete | Ta bort |
| logs | Container logs |
| exec | Kör kommando |

**Nästa steg:** Node 3 - Pods
''',
}

NODE_03_PODS = {
    "node_id": 3,
    "title": "Pods",
    "slug": "pods",
    "estimated_minutes": 55,
    "xp_reward": 130,
    "prerequisites": [2],
    "content": '''
# Pods

Pods är minsta deployable unit.

## Pod YAML

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  containers:
    - name: app
      image: nginx:1.24
      ports:
        - containerPort: 80
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

## Skapa & Hantera

```bash
# Skapa pod
kubectl apply -f pod.yaml

# Status
kubectl get pods
kubectl get pod myapp -o wide
kubectl get pod myapp -o yaml

# Ta bort
kubectl delete pod myapp
kubectl delete -f pod.yaml
```

## Multi-container Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi
spec:
  containers:
    - name: app
      image: myapp
      ports:
        - containerPort: 8080
    - name: sidecar
      image: fluentd
      volumeMounts:
        - name: logs
          mountPath: /var/log
  volumes:
    - name: logs
      emptyDir: {}
```

## Pod Lifecycle

```
Pending → Running → Succeeded/Failed
              ↓
          CrashLoopBackOff
```

| State | Beskrivning |
|-------|-------------|
| Pending | Väntar på scheduling |
| Running | Kör |
| Succeeded | Avslutad OK |
| Failed | Avslutad med fel |
| Unknown | Node-kommunikation borta |

**Nästa steg:** Node 4 - Deployments
''',
}

NODE_04_DEPLOYMENTS = {
    "node_id": 4,
    "title": "Deployments",
    "slug": "deployments",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [3],
    "content": '''
# Deployments

Deklarativ pod-hantering med replicas.

## Deployment YAML

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
        - name: app
          image: myapp:v1
          ports:
            - containerPort: 8080
```

## Hantera Deployments

```bash
# Skapa
kubectl apply -f deployment.yaml

# Skala
kubectl scale deployment myapp --replicas=5

# Uppdatera image
kubectl set image deployment/myapp app=myapp:v2

# Rollout status
kubectl rollout status deployment/myapp

# Historia
kubectl rollout history deployment/myapp

# Rollback
kubectl rollout undo deployment/myapp
kubectl rollout undo deployment/myapp --to-revision=2
```

## Update Strategy

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Extra pods under update
      maxUnavailable: 0  # Alltid min replicas
```

## ReplicaSet

```bash
# Deployment skapar ReplicaSet
kubectl get rs

# ReplicaSet hanterar Pods
kubectl get pods -l app=myapp
```

| Strategy | Beskrivning |
|----------|-------------|
| RollingUpdate | Gradvis ersättning |
| Recreate | Stoppa alla, starta nya |

**Nästa steg:** Node 5 - Services
''',
}

KUBERNETES_SKILLSMAP_BLOCK_1 = [
    NODE_01_K8S_INTRO,
    NODE_02_KUBECTL_BASICS,
    NODE_03_PODS,
    NODE_04_DEPLOYMENTS,
]


# =============================================================================
# BLOCK 2: SERVICES & NETWORKING (Noder 5-8)
# =============================================================================

NODE_05_SERVICES = {
    "node_id": 5,
    "title": "Services",
    "slug": "services",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": [4],
    "content": '''
# Kubernetes Services

Stabil nätverksendpoint för pods.

## Service Types

```yaml
# ClusterIP (default) - Intern åtkomst
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

## NodePort

```yaml
# NodePort - Extern via node IP
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
  type: NodePort
```

## LoadBalancer

```yaml
# LoadBalancer - Cloud LB
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
  type: LoadBalancer
```

## Service DNS

```bash
# DNS format
<service>.<namespace>.svc.cluster.local

# Exempel
myapp.default.svc.cluster.local
myapp.default    # Kortform
myapp            # Samma namespace
```

| Type | Åtkomst |
|------|---------|
| ClusterIP | Endast internt |
| NodePort | nodeIP:nodePort |
| LoadBalancer | Extern IP |
| ExternalName | DNS alias |

**Nästa steg:** Node 6 - Ingress
''',
}

NODE_06_INGRESS = {
    "node_id": 6,
    "title": "Ingress",
    "slug": "ingress",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [5],
    "content": '''
# Ingress

HTTP/S routing till services.

## Ingress Controller

```bash
# Installera NGINX Ingress
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

# Verifiera
kubectl get pods -n ingress-nginx
```

## Basic Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp
                port:
                  number: 80
```

## Path-based Routing

```yaml
spec:
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /api/v1
            pathType: Prefix
            backend:
              service:
                name: api-v1
                port:
                  number: 80
          - path: /api/v2
            pathType: Prefix
            backend:
              service:
                name: api-v2
                port:
                  number: 80
```

## TLS

```yaml
spec:
  tls:
    - hosts:
        - myapp.example.com
      secretName: myapp-tls
  rules:
    - host: myapp.example.com
```

```bash
# Skapa TLS secret
kubectl create secret tls myapp-tls \\
  --cert=tls.crt \\
  --key=tls.key
```

**Nästa steg:** Node 7 - ConfigMaps & Secrets
''',
}

NODE_07_CONFIGMAPS_SECRETS = {
    "node_id": 7,
    "title": "ConfigMaps & Secrets",
    "slug": "configmaps-secrets",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [6],
    "content": '''
# ConfigMaps & Secrets

Konfigurations- och hemlighetshantering.

## ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: postgres
  LOG_LEVEL: info
  config.json: |
    {"feature": true}
```

```bash
# Skapa från fil
kubectl create configmap app-config --from-file=config.json

# Från literals
kubectl create configmap app-config --from-literal=LOG_LEVEL=debug
```

## Secrets

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=  # base64
stringData:
  username: admin  # Klartext (konverteras)
```

```bash
# Skapa secret
kubectl create secret generic db-secret \\
  --from-literal=password=secret123
```

## Använda i Pod

```yaml
spec:
  containers:
    - name: app
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: LOG_LEVEL
      envFrom:
        - configMapRef:
            name: app-config
      volumeMounts:
        - name: config
          mountPath: /etc/config
  volumes:
    - name: config
      configMap:
        name: app-config
```

**Nästa steg:** Node 8 - Volumes & Storage
''',
}

NODE_08_VOLUMES_STORAGE = {
    "node_id": 8,
    "title": "Volumes & Storage",
    "slug": "volumes-storage",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": '''
# Kubernetes Volumes & Storage

Persistent data i K8s.

## EmptyDir

```yaml
spec:
  containers:
    - name: app
      volumeMounts:
        - name: cache
          mountPath: /cache
  volumes:
    - name: cache
      emptyDir: {}
```

## PersistentVolume & Claim

```yaml
# PersistentVolume
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-data
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: /data

---
# PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

## Använda PVC

```yaml
spec:
  containers:
    - name: app
      volumeMounts:
        - name: data
          mountPath: /data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: app-data
```

## StorageClass

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
reclaimPolicy: Delete
allowVolumeExpansion: true
```

| Access Mode | Beskrivning |
|-------------|-------------|
| ReadWriteOnce | En node r/w |
| ReadOnlyMany | Flera nodes ro |
| ReadWriteMany | Flera nodes r/w |

**Nästa steg:** Node 9 - StatefulSets
''',
}

KUBERNETES_SKILLSMAP_BLOCK_2 = [
    NODE_05_SERVICES,
    NODE_06_INGRESS,
    NODE_07_CONFIGMAPS_SECRETS,
    NODE_08_VOLUMES_STORAGE,
]


# =============================================================================
# BLOCK 3: STATEFULSETS & WORKLOADS (Noder 9-12)
# =============================================================================

NODE_09_STATEFULSETS = {
    "node_id": 9,
    "title": "StatefulSets",
    "slug": "statefulsets",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [8],
    "content": '''
# StatefulSets

Stateful applikationer med stabil identitet.

## StatefulSet YAML

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
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 10Gi
```

## Headless Service

```yaml
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

## Pod Naming

```bash
# Stabil ordning
postgres-0
postgres-1
postgres-2

# DNS
postgres-0.postgres.default.svc.cluster.local
```

## Deployment vs StatefulSet

| Aspekt | Deployment | StatefulSet |
|--------|------------|-------------|
| Pod-namn | Random | Ordnad (0,1,2) |
| Storage | Delad | Per-pod PVC |
| Scaling | Parallell | Sekventiell |
| Updates | Rolling | Ordered |

**Nästa steg:** Node 10 - Jobs & CronJobs
''',
}

NODE_10_JOBS_CRONJOBS = {
    "node_id": 10,
    "title": "Jobs & CronJobs",
    "slug": "jobs-cronjobs",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [9],
    "content": '''
# Jobs & CronJobs

Batch och schemalagda uppgifter.

## Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup
spec:
  completions: 1
  parallelism: 1
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: backup
          image: backup-tool
          command: ["./backup.sh"]
```

## CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: "0 2 * * *"  # Varje dag kl 02:00
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: backup
              image: backup-tool
```

## Job Patterns

```yaml
# Parallel job
spec:
  completions: 10
  parallelism: 3  # 3 pods samtidigt

# Work queue
spec:
  completions: null
  parallelism: 3
```

## Hantera Jobs

```bash
# Lista
kubectl get jobs
kubectl get cronjobs

# Manuell trigger
kubectl create job --from=cronjob/daily-backup manual-backup

# Ta bort
kubectl delete job backup
```

| Cron | Betydelse |
|------|-----------|
| 0 * * * * | Varje timme |
| 0 0 * * * | Varje dag |
| 0 0 * * 0 | Varje söndag |
| */15 * * * * | Var 15:e minut |

**Nästa steg:** Node 11 - DaemonSets
''',
}

NODE_11_DAEMONSETS = {
    "node_id": 11,
    "title": "DaemonSets",
    "slug": "daemonsets",
    "estimated_minutes": 40,
    "xp_reward": 120,
    "prerequisites": [10],
    "content": '''
# DaemonSets

En pod per node.

## DaemonSet YAML

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  selector:
    matchLabels:
      app: fluentd
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      containers:
        - name: fluentd
          image: fluentd
          volumeMounts:
            - name: varlog
              mountPath: /var/log
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
```

## Användningsområden

| Use Case | Exempel |
|----------|---------|
| Logging | Fluentd, Filebeat |
| Monitoring | Node Exporter |
| Networking | CNI plugins |
| Storage | CSI drivers |

## Node Selector

```yaml
spec:
  template:
    spec:
      nodeSelector:
        node-type: worker
```

## Tolerations

```yaml
spec:
  template:
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
```

```bash
# Lista DaemonSets
kubectl get ds

# Status
kubectl describe ds fluentd
```

**Nästa steg:** Node 12 - RBAC
''',
}

NODE_12_RBAC = {
    "node_id": 12,
    "title": "RBAC",
    "slug": "rbac",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [11],
    "content": '''
# RBAC - Role-Based Access Control

Behörighetsstyrning i Kubernetes.

## ServiceAccount

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
```

## Role (Namespace-scope)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
```

## RoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
subjects:
  - kind: ServiceAccount
    name: app-sa
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

## ClusterRole (Cluster-wide)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "list"]
```

## Pod med ServiceAccount

```yaml
spec:
  serviceAccountName: app-sa
  containers:
    - name: app
      image: myapp
```

| Resurs | Scope |
|--------|-------|
| Role | Namespace |
| ClusterRole | Cluster |
| RoleBinding | Namespace |
| ClusterRoleBinding | Cluster |

**Nästa steg:** Node 13 - Helm Basics
''',
}

KUBERNETES_SKILLSMAP_BLOCK_3 = [
    NODE_09_STATEFULSETS,
    NODE_10_JOBS_CRONJOBS,
    NODE_11_DAEMONSETS,
    NODE_12_RBAC,
]


# =============================================================================
# BLOCK 4: HELM & NETWORKING (Noder 13-16)
# =============================================================================

NODE_13_HELM_BASICS = {
    "node_id": 13,
    "title": "Helm Basics",
    "slug": "helm-basics",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [4],
    "content": '''
# Helm Basics

Kubernetes package manager.

## Installation

```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verifiera
helm version
```

## Grundläggande Kommandon

```bash
# Lägg till repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Sök charts
helm search repo nginx
helm search hub postgresql

# Installera
helm install my-nginx bitnami/nginx

# Lista releases
helm list

# Avinstallera
helm uninstall my-nginx
```

## Anpassa Installation

```bash
# Se tillgängliga values
helm show values bitnami/nginx

# Installera med values
helm install my-nginx bitnami/nginx \\
  --set replicaCount=3 \\
  --set service.type=LoadBalancer

# Med values-fil
helm install my-nginx bitnami/nginx -f values.yaml
```

## values.yaml

```yaml
replicaCount: 3
image:
  repository: nginx
  tag: "1.24"
service:
  type: LoadBalancer
  port: 80
resources:
  limits:
    cpu: 100m
    memory: 128Mi
```

**Nästa steg:** Node 14 - Helm Charts
''',
}

NODE_14_HELM_CHARTS = {
    "node_id": 14,
    "title": "Helm Charts",
    "slug": "helm-charts",
    "estimated_minutes": 60,
    "xp_reward": 160,
    "prerequisites": [13],
    "content": '''
# Skapa Helm Charts

Bygg egna charts.

## Skapa Chart

```bash
helm create myapp

myapp/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl
│   └── NOTES.txt
└── charts/
```

## Chart.yaml

```yaml
apiVersion: v2
name: myapp
description: My application
type: application
version: 1.0.0
appVersion: "1.0.0"
dependencies:
  - name: postgresql
    version: "12.x.x"
    repository: https://charts.bitnami.com/bitnami
```

## Templates

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "myapp.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.service.port }}
```

## Utveckla & Testa

```bash
# Lint
helm lint myapp/

# Dry-run
helm install myapp ./myapp --dry-run --debug

# Template output
helm template myapp ./myapp

# Installera lokalt
helm install myapp ./myapp
```

## Uppgradera

```bash
# Uppgradera release
helm upgrade myapp ./myapp

# Rollback
helm rollback myapp 1
helm history myapp
```

**Nästa steg:** Node 15 - Network Policies
''',
}

NODE_15_NETWORK_POLICIES = {
    "node_id": 15,
    "title": "Network Policies",
    "slug": "network-policies",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [5],
    "content": '''
# Network Policies

Nätverkssegmentering i K8s.

## Default Deny

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

## Allow Specific Traffic

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-policy
spec:
  podSelector:
    matchLabels:
      app: api
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
```

## Egress Policy

```yaml
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Egress
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - port: 5432
    - to:
        - namespaceSelector:
            matchLabels:
              name: kube-system
      ports:
        - port: 53
          protocol: UDP
```

## Namespace Selector

```yaml
ingress:
  - from:
      - namespaceSelector:
          matchLabels:
            env: production
        podSelector:
          matchLabels:
            app: frontend
```

| Policy | Effekt |
|--------|--------|
| podSelector: {} | Alla pods |
| Ingress deny | Ingen inkommande |
| Egress deny | Ingen utgående |

**Nästa steg:** Node 16 - HPA & VPA
''',
}

NODE_16_HPA_VPA = {
    "node_id": 16,
    "title": "HPA & VPA",
    "slug": "hpa-vpa",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [4],
    "content": '''
# HPA & VPA

Auto-scaling i Kubernetes.

## Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
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
```

## Metrics Server

```bash
# Installera
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Verifiera
kubectl top nodes
kubectl top pods
```

## kubectl HPA

```bash
# Skapa HPA
kubectl autoscale deployment myapp --min=2 --max=10 --cpu-percent=70

# Status
kubectl get hpa
kubectl describe hpa myapp
```

## VPA (Vertical Pod Autoscaler)

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  updatePolicy:
    updateMode: "Auto"
```

| Scaling | HPA | VPA |
|---------|-----|-----|
| Vad | Antal pods | Pod resources |
| När | CPU/Memory threshold | Resource recommendations |
| Best for | Stateless | Stateful |

**Nästa steg:** Node 17 - Pod Disruption Budgets
''',
}

KUBERNETES_SKILLSMAP_BLOCK_4 = [
    NODE_13_HELM_BASICS,
    NODE_14_HELM_CHARTS,
    NODE_15_NETWORK_POLICIES,
    NODE_16_HPA_VPA,
]


# =============================================================================
# BLOCK 5: PRODUCTION & MONITORING (Noder 17-20)
# =============================================================================

NODE_17_PDB = {
    "node_id": 17,
    "title": "Pod Disruption Budgets",
    "slug": "pdb",
    "estimated_minutes": 40,
    "xp_reward": 130,
    "prerequisites": [4],
    "content": '''
# Pod Disruption Budgets

Garantera tillgänglighet vid underhåll.

## PDB YAML

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: myapp
```

## Alternativ: maxUnavailable

```yaml
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: myapp
```

## Procent

```yaml
spec:
  minAvailable: 50%
  selector:
    matchLabels:
      app: myapp
```

## Hantera

```bash
# Lista
kubectl get pdb

# Status
kubectl describe pdb myapp-pdb

# Drain node (respekterar PDB)
kubectl drain node1 --ignore-daemonsets
```

| Setting | Betydelse |
|---------|-----------|
| minAvailable: 2 | Minst 2 pods |
| maxUnavailable: 1 | Max 1 pod nere |
| minAvailable: 50% | Minst halva |

**Nästa steg:** Node 18 - Probes
''',
}

NODE_18_PROBES = {
    "node_id": 18,
    "title": "Liveness & Readiness Probes",
    "slug": "probes",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [3],
    "content": '''
# Liveness & Readiness Probes

Hälsokontroller för pods.

## Liveness Probe

```yaml
spec:
  containers:
    - name: app
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 15
        periodSeconds: 10
        timeoutSeconds: 5
        failureThreshold: 3
```

## Readiness Probe

```yaml
spec:
  containers:
    - name: app
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 5
```

## Startup Probe

```yaml
spec:
  containers:
    - name: app
      startupProbe:
        httpGet:
          path: /health
          port: 8080
        failureThreshold: 30
        periodSeconds: 10
```

## Probe-typer

```yaml
# HTTP
httpGet:
  path: /health
  port: 8080

# TCP
tcpSocket:
  port: 5432

# Command
exec:
  command:
    - cat
    - /tmp/healthy
```

| Probe | Syfte | Fail Action |
|-------|-------|-------------|
| Liveness | Är alive? | Restart |
| Readiness | Redo för trafik? | Remove from LB |
| Startup | Startad? | Block other probes |

**Nästa steg:** Node 19 - Logging & Monitoring
''',
}

NODE_19_LOGGING_MONITORING = {
    "node_id": 19,
    "title": "Logging & Monitoring",
    "slug": "logging-monitoring",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [18],
    "content": '''
# Logging & Monitoring

Observability i Kubernetes.

## Prometheus Stack

```bash
# Installera med Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm install prometheus prometheus-community/kube-prometheus-stack \\
  --namespace monitoring \\
  --create-namespace
```

## ServiceMonitor

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: myapp
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
    - port: metrics
      path: /metrics
      interval: 15s
```

## Loki för Logs

```bash
helm install loki grafana/loki-stack \\
  --namespace logging \\
  --create-namespace \\
  --set grafana.enabled=true
```

## kubectl logs

```bash
# Pod logs
kubectl logs mypod
kubectl logs -f mypod          # Follow
kubectl logs mypod --previous  # Crashed container

# Multi-container
kubectl logs mypod -c sidecar

# Label selector
kubectl logs -l app=myapp
```

## Grafana Dashboards

```yaml
# ConfigMap för dashboard
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-dashboard
  labels:
    grafana_dashboard: "1"
data:
  dashboard.json: |
    { ... }
```

| Stack | Komponent |
|-------|-----------|
| Metrics | Prometheus |
| Logs | Loki/ELK |
| Visualization | Grafana |
| Tracing | Jaeger/Zipkin |

**Nästa steg:** Node 20 - Production Best Practices
''',
}

NODE_20_PRODUCTION_BEST_PRACTICES = {
    "node_id": 20,
    "title": "Production Best Practices",
    "slug": "production-best-practices",
    "estimated_minutes": 60,
    "xp_reward": 175,
    "prerequisites": [19],
    "content": '''
# Kubernetes Production Best Practices

## Resource Management

```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "100m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

## Security Context

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
    - name: app
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
```

## Pod Anti-Affinity

```yaml
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app: myapp
          topologyKey: kubernetes.io/hostname
```

## Priority Classes

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
```

## Checklist

| Område | Best Practice |
|--------|---------------|
| Resources | Alltid requests/limits |
| Replicas | Minst 2 för HA |
| Probes | Liveness + Readiness |
| PDB | Skydda vid drain |
| Anti-affinity | Sprid över nodes |
| Security | Non-root, read-only |
| Secrets | Extern secret mgmt |
| Monitoring | Prometheus + Grafana |
| Logging | Centralized logging |
| Backup | etcd + PV snapshots |

**🎉 Grattis! Du har slutfört Kubernetes Mastery SkillsMap!**
''',
}

KUBERNETES_SKILLSMAP_BLOCK_5 = [
    NODE_17_PDB,
    NODE_18_PROBES,
    NODE_19_LOGGING_MONITORING,
    NODE_20_PRODUCTION_BEST_PRACTICES,
]


# =============================================================================
# FULL EXPORT
# =============================================================================

KUBERNETES_SKILLSMAP_ALL_NODES = (
    KUBERNETES_SKILLSMAP_BLOCK_1 +
    KUBERNETES_SKILLSMAP_BLOCK_2 +
    KUBERNETES_SKILLSMAP_BLOCK_3 +
    KUBERNETES_SKILLSMAP_BLOCK_4 +
    KUBERNETES_SKILLSMAP_BLOCK_5
)
