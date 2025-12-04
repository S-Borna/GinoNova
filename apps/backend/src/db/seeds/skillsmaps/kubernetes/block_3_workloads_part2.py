# =============================================================================
# KUBERNETES MASTERY - BLOCK 3 PART 2: DAEMONSETS & RBAC
# Noder 11-12 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 3 PART 2 - SPECIALIZED WORKLOADS
=================================================
Node 11: DaemonSets - Node-Level Services
Node 12: RBAC - Role-Based Access Control
"""

NODE_11 = {
    "id": "k8s_node_11",
    "title": "DaemonSets - Node-Level Services",
    "slug": "daemonsets-node-level-services",
    "content": r'''# 🔄 DaemonSets - Node-Level Services

## 1. Introduktion & Kontext

DaemonSets säkerställer att en kopia av en Pod körs på varje (eller utvalda) noder i klustret. De är perfekta för node-level services som logging agents, monitoring exporters, och network plugins.

### DaemonSet vs Deployment

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   DAEMONSET VS DEPLOYMENT                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DEPLOYMENT                                                              │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  replicas: 3                                                     │   │
│  │  Scheduler väljer vilka noder som får pods                       │   │
│  │                                                                  │   │
│  │  Node 1     Node 2     Node 3     Node 4     Node 5              │   │
│  │  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐           │   │
│  │  │ Pod │    │     │    │ Pod │    │     │    │ Pod │           │   │
│  │  └─────┘    └─────┘    └─────┘    └─────┘    └─────┘           │   │
│  │                                                                  │   │
│  │  Pods distribueras baserat på resources och scheduling          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  DAEMONSET                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  En pod per node (automatiskt)                                   │   │
│  │  Ny node? → Pod skapas automatiskt                              │   │
│  │                                                                  │   │
│  │  Node 1     Node 2     Node 3     Node 4     Node 5              │   │
│  │  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐           │   │
│  │  │ Pod │    │ Pod │    │ Pod │    │ Pod │    │ Pod │           │   │
│  │  └─────┘    └─────┘    └─────┘    └─────┘    └─────┘           │   │
│  │                                                                  │   │
│  │  Varje node får exakt en pod                                    │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Typiska Användningsfall

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   DAEMONSET USE CASES                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. LOG COLLECTION                                                       │
│     ┌──────────────────────────────────────────┐                        │
│     │  Fluentd / Fluent Bit / Filebeat         │                        │
│     │  • Samlar logs från varje node           │                        │
│     │  • Mountar /var/log                       │                        │
│     │  • Skickar till centralt system          │                        │
│     └──────────────────────────────────────────┘                        │
│                                                                          │
│  2. NODE MONITORING                                                      │
│     ┌──────────────────────────────────────────┐                        │
│     │  node-exporter / cAdvisor                │                        │
│     │  • Exponerar node metrics                 │                        │
│     │  • CPU, memory, disk, network            │                        │
│     │  • Prometheus scraper                     │                        │
│     └──────────────────────────────────────────┘                        │
│                                                                          │
│  3. CLUSTER NETWORKING                                                   │
│     ┌──────────────────────────────────────────┐                        │
│     │  CNI plugins (Calico, Weave, Cilium)     │                        │
│     │  • Nätverksconfig per node               │                        │
│     │  • Pod networking                         │                        │
│     │  • Network policies                       │                        │
│     └──────────────────────────────────────────┘                        │
│                                                                          │
│  4. STORAGE DAEMONS                                                      │
│     ┌──────────────────────────────────────────┐                        │
│     │  glusterd / Ceph OSD                      │                        │
│     │  • Distributed storage                   │                        │
│     │  • Accessar node disks                   │                        │
│     └──────────────────────────────────────────┘                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. DaemonSet Anatomy

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: logging
  labels:
    app: fluentd
spec:
  # Selector
  selector:
    matchLabels:
      app: fluentd

  # Update Strategy
  updateStrategy:
    type: RollingUpdate          # RollingUpdate | OnDelete
    rollingUpdate:
      maxUnavailable: 1          # Max pods unavailable under update

  # Pod Template
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      # Tolerations för master/control-plane noder
      tolerations:
        - key: node-role.kubernetes.io/control-plane
          effect: NoSchedule
        - key: node-role.kubernetes.io/master
          effect: NoSchedule

      # Node selector (optional - begränsa till vissa noder)
      # nodeSelector:
      #   disk: ssd

      # Service Account
      serviceAccountName: fluentd

      # Containers
      containers:
        - name: fluentd
          image: fluent/fluentd-kubernetes-daemonset:v1.16

          resources:
            limits:
              memory: 200Mi
              cpu: 100m
            requests:
              memory: 100Mi
              cpu: 50m

          volumeMounts:
            - name: varlog
              mountPath: /var/log
              readOnly: true
            - name: varlibdockercontainers
              mountPath: /var/lib/docker/containers
              readOnly: true
            - name: config
              mountPath: /fluentd/etc

          env:
            - name: FLUENT_ELASTICSEARCH_HOST
              value: "elasticsearch.logging"

      terminationGracePeriodSeconds: 30

      # Volumes
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
        - name: config
          configMap:
            name: fluentd-config
```

## 4. Node Selector & Affinity

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: gpu-monitor
spec:
  selector:
    matchLabels:
      app: gpu-monitor
  template:
    metadata:
      labels:
        app: gpu-monitor
    spec:
      # Kör ENDAST på noder med GPU
      nodeSelector:
        accelerator: nvidia-tesla

      # Eller med nodeAffinity (mer flexibelt)
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: accelerator
                    operator: In
                    values:
                      - nvidia-tesla
                      - nvidia-v100

      containers:
        - name: nvidia-smi
          image: nvidia/dcgm-exporter:latest
```

## 5. Praktiska Övningar

### Övning 1: Node Exporter DaemonSet

```bash
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: default
  labels:
    app: node-exporter
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      hostNetwork: true          # Använd host network
      hostPID: true              # Se host processes

      containers:
        - name: node-exporter
          image: prom/node-exporter:latest
          args:
            - "--path.procfs=/host/proc"
            - "--path.sysfs=/host/sys"
          ports:
            - containerPort: 9100
              hostPort: 9100
          volumeMounts:
            - name: proc
              mountPath: /host/proc
              readOnly: true
            - name: sys
              mountPath: /host/sys
              readOnly: true

      volumes:
        - name: proc
          hostPath:
            path: /proc
        - name: sys
          hostPath:
            path: /sys
EOF

# Verifiera
kubectl get daemonset node-exporter
kubectl get pods -l app=node-exporter -o wide

# Testa metrics
kubectl port-forward ds/node-exporter 9100:9100
curl localhost:9100/metrics | head
```

### Övning 2: Selektiv DaemonSet

```bash
# Labela specifika noder
kubectl label nodes node1 workload=compute
kubectl label nodes node2 workload=compute

# DaemonSet endast för compute noder
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: compute-agent
spec:
  selector:
    matchLabels:
      app: compute-agent
  template:
    metadata:
      labels:
        app: compute-agent
    spec:
      nodeSelector:
        workload: compute
      containers:
        - name: agent
          image: busybox
          command: ["sleep", "infinity"]
EOF

# Verifiera
kubectl get pods -l app=compute-agent -o wide
# Endast på noder med label workload=compute
```

## 6. Update Strategies

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   DAEMONSET UPDATE STRATEGIES                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ROLLINGUPDATE (default)                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Uppdaterar pods en i taget                                      │   │
│  │                                                                  │   │
│  │  maxUnavailable: 1                                               │   │
│  │  maxSurge: 0 (kan inte vara > 0 för DaemonSet)                  │   │
│  │                                                                  │   │
│  │  Node 1 ─▶ Update ─▶ Ready ─▶                                   │   │
│  │  Node 2                    ─▶ Update ─▶ Ready ─▶                │   │
│  │  Node 3                                        ─▶ Update ─▶     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ONDELETE                                                                │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Manuell kontroll                                                │   │
│  │  Ny pod skapas först när gammal raderas                          │   │
│  │                                                                  │   │
│  │  1. Ändra DaemonSet spec                                        │   │
│  │  2. Inget händer automatiskt                                    │   │
│  │  3. kubectl delete pod på nod                                   │   │
│  │  4. Ny pod med ny spec skapas                                   │   │
│  │                                                                  │   │
│  │  Användning: Kritiska system-pods                               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   DAEMONSET BEST PRACTICES                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Resource Management                                                  │
│     □ Sätt resource limits (DaemonSets körs på ALLA noder!)            │
│     □ Prioritera minimala images                                        │
│     □ Undvik resource-heavy operationer                                 │
│                                                                          │
│  ✅ Tolerations                                                         │
│     □ Inkludera control-plane tolerations om nödvändigt                │
│     □ Hantera custom taints                                             │
│                                                                          │
│  ✅ Updates                                                              │
│     □ Använd RollingUpdate för de flesta fall                           │
│     □ OnDelete för kritiska system-komponenter                          │
│     □ Testa updates i staging först                                     │
│                                                                          │
│  ✅ Security                                                            │
│     □ Minimera hostPath mounts                                          │
│     □ Använd read-only där möjligt                                      │
│     □ Kör som non-root om möjligt                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Sammanfattning & Task

### DaemonSet Comparison

| Feature | DaemonSet | Deployment |
|---------|-----------|------------|
| Pod per node | ✅ Guaranteed | ❌ Varies |
| Auto-scaling | ❌ Node count | ✅ HPA |
| Use case | Node services | Applications |
| New node | Auto pod | No auto pod |

---

**Nästa Node:** RBAC - Security →
''',
    "xp_reward": 140,
    "estimated_minutes": 45,
    "prerequisites": ["k8s_node_10"],
    "learning_outcomes": [
        "Förstå DaemonSet-konceptet",
        "Implementera node-level services",
        "Konfigurera node selectors",
        "Hantera update strategies"
    ]
}

NODE_12 = {
    "id": "k8s_node_12",
    "title": "RBAC - Role-Based Access Control",
    "slug": "rbac-role-based-access-control",
    "content": r'''# 🔐 RBAC - Role-Based Access Control

## 1. Introduktion & Kontext

RBAC (Role-Based Access Control) är Kubernetes säkerhetsmodell för att kontrollera vem som kan göra vad i klustret. Det är fundamentalt för multi-tenant och produktions-kluster.

### RBAC Components

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      RBAC COMPONENTS                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────┐          ┌─────────────────┐                       │
│  │    SUBJECT      │          │      ROLE       │                       │
│  │  (Vem)          │          │  (Rättigheter)  │                       │
│  ├─────────────────┤          ├─────────────────┤                       │
│  │ • User          │          │ • Role          │                       │
│  │ • Group         │───────▶  │   (namespace)   │                       │
│  │ • ServiceAccount│          │ • ClusterRole   │                       │
│  └─────────────────┘          │   (cluster-wide)│                       │
│           │                   └─────────────────┘                       │
│           │                            │                                 │
│           │         ┌──────────────────┘                                │
│           │         │                                                    │
│           ▼         ▼                                                    │
│  ┌──────────────────────────────┐                                       │
│  │       ROLEBINDING            │                                       │
│  │  (Kopplar Subject till Role) │                                       │
│  ├──────────────────────────────┤                                       │
│  │ • RoleBinding (namespace)    │                                       │
│  │ • ClusterRoleBinding         │                                       │
│  │   (cluster-wide)             │                                       │
│  └──────────────────────────────┘                                       │
│                                                                          │
│  FLOW:                                                                   │
│  User "alice" ──▶ RoleBinding ──▶ Role "developer" ──▶ Can GET pods    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Role vs ClusterRole

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   ROLE VS CLUSTERROLE                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ROLE (Namespace-scoped)                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  • Gäller endast inom ett namespace                              │   │
│  │  • Kan inte accessa cluster-resources                            │   │
│  │                                                                  │   │
│  │  ┌─────────────────────────────────────────────────────────┐    │   │
│  │  │ Namespace: development                                   │    │   │
│  │  │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────────┐ ┌──────────┐      │    │   │
│  │  │ │Pods │ │Svcs │ │CMs  │ │Secrets  │ │Deployments│      │    │   │
│  │  │ └──▲──┘ └──▲──┘ └──▲──┘ └────▲────┘ └─────▲────┘      │    │   │
│  │  │    └───────┴───────┴─────────┴────────────┘            │    │   │
│  │  │                    Role: developer                      │    │   │
│  │  └─────────────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  CLUSTERROLE (Cluster-scoped)                                            │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  • Gäller i hela klustret                                        │   │
│  │  • Kan accessa cluster-resources (nodes, namespaces, etc.)       │   │
│  │  • Kan användas med RoleBinding (i ett namespace)               │   │
│  │                                                                  │   │
│  │  ┌─────────────────────────────────────────────────────────┐    │   │
│  │  │ Cluster-wide                                             │    │   │
│  │  │ ┌─────┐ ┌──────────┐ ┌───┐ ┌────────────────┐          │    │   │
│  │  │ │Nodes│ │Namespaces│ │PVs│ │StorageClasses  │          │    │   │
│  │  │ └──▲──┘ └────▲─────┘ └─▲─┘ └───────▲────────┘          │    │   │
│  │  │    └─────────┴─────────┴───────────┘                    │    │   │
│  │  │              ClusterRole: cluster-admin                  │    │   │
│  │  └─────────────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. RBAC Resources

### Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
  namespace: development
rules:
  # Pods - full access
  - apiGroups: [""]
    resources: ["pods", "pods/log", "pods/exec"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]

  # Services - read only
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["get", "list", "watch"]

  # Deployments
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "create", "update", "patch"]

  # ConfigMaps & Secrets - read only
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list", "watch"]

  # Specific resources by name
  - apiGroups: [""]
    resources: ["secrets"]
    resourceNames: ["app-secrets"]    # Endast denna secret
    verbs: ["get"]
```

### ClusterRole

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-reader
rules:
  # Nodes - cluster resource
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["get", "list", "watch"]

  # Namespaces - cluster resource
  - apiGroups: [""]
    resources: ["namespaces"]
    verbs: ["get", "list"]

  # PersistentVolumes - cluster resource
  - apiGroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get", "list", "watch"]
```

### RoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-binding
  namespace: development
subjects:
  # User
  - kind: User
    name: alice
    apiGroup: rbac.authorization.k8s.io

  # Group
  - kind: Group
    name: developers
    apiGroup: rbac.authorization.k8s.io

  # ServiceAccount
  - kind: ServiceAccount
    name: ci-bot
    namespace: ci-cd

roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
```

### ClusterRoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin-binding
subjects:
  - kind: User
    name: admin
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

## 4. RBAC Verbs

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        RBAC VERBS                                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  VERB              │ DESCRIPTION                  │ HTTP EQUIVALENT      │
│  ─────────────────────────────────────────────────────────────────────  │
│  get               │ Läs enskild resurs           │ GET (single)         │
│  list              │ Lista resurser               │ GET (collection)     │
│  watch             │ Watch för ändringar          │ GET (watch)          │
│  create            │ Skapa ny resurs              │ POST                 │
│  update            │ Fullständig update           │ PUT                  │
│  patch             │ Partiell update              │ PATCH                │
│  delete            │ Radera resurs                │ DELETE               │
│  deletecollection  │ Radera collection            │ DELETE (collection)  │
│                                                                          │
│  SPECIAL VERBS:                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│  impersonate       │ Impersonate users/groups     │ (special)            │
│  bind              │ Skapa RoleBindings           │ (special)            │
│  escalate          │ Escalate privileges          │ (special)            │
│                                                                          │
│  SUBRESOURCES:                                                           │
│  ─────────────────────────────────────────────────────────────────────  │
│  pods/log          │ kubectl logs                 │                      │
│  pods/exec         │ kubectl exec                 │                      │
│  pods/portforward  │ kubectl port-forward         │                      │
│  pods/status       │ Pod status subresource       │                      │
│  deployments/scale │ kubectl scale                │                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 5. Praktiska Övningar

### Övning 1: Developer Role

```bash
# Skapa namespace
kubectl create namespace dev-team

# Skapa Role
cat << 'EOF' | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
  namespace: dev-team
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "configmaps"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "create", "update"]
EOF

# Skapa RoleBinding
cat << 'EOF' | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-binding
  namespace: dev-team
subjects:
  - kind: User
    name: alice
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
EOF

# Testa (kräver user cert/token)
kubectl auth can-i get pods --namespace=dev-team --as=alice
kubectl auth can-i delete nodes --as=alice
```

### Övning 2: ServiceAccount RBAC

```bash
# Skapa ServiceAccount
kubectl create serviceaccount ci-bot -n dev-team

# Ge CI-bot permissions
cat << 'EOF' | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ci-bot-binding
  namespace: dev-team
subjects:
  - kind: ServiceAccount
    name: ci-bot
    namespace: dev-team
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
EOF

# Testa som ServiceAccount
kubectl auth can-i get pods -n dev-team --as=system:serviceaccount:dev-team:ci-bot
```

### Övning 3: Debugging RBAC

```bash
# Check current user permissions
kubectl auth can-i --list

# Check specific permission
kubectl auth can-i create deployments --namespace=production

# Check as another user
kubectl auth can-i get secrets --as=developer --namespace=dev-team

# Get all bindings för user
kubectl get rolebindings,clusterrolebindings -A -o wide | grep alice

# Describe role
kubectl describe role developer -n dev-team

# API resources and verbs
kubectl api-resources --verbs=list --namespaced=true
```

## 6. Built-in ClusterRoles

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   BUILT-IN CLUSTERROLES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  cluster-admin                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Full access till ALLT i klustret                                │   │
│  │  ⚠️ ANVÄND SPARSAMT                                              │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  admin                                                                   │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Full access inom namespace                                      │   │
│  │  Kan skapa Roles/RoleBindings                                   │   │
│  │  Kan INTE modifiera namespace/quota                             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  edit                                                                    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Read/write access till de flesta namespace-resurser            │   │
│  │  Kan INTE se Roles/RoleBindings                                 │   │
│  │  Kan INTE accessa Secrets (default)                             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  view                                                                    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Read-only access till namespace-resurser                       │   │
│  │  Kan INTE se Secrets eller Roles                                │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     RBAC BEST PRACTICES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Principle of Least Privilege                                        │
│     □ Ge minimala rättigheter som behövs                               │
│     □ Börja restrictive, öppna vid behov                               │
│     □ Använd namespace-scoped Roles där möjligt                        │
│                                                                          │
│  ✅ ServiceAccounts                                                     │
│     □ Skapa dedikerade SA per applikation                              │
│     □ Undvik default ServiceAccount                                    │
│     □ Disable automounting om ej nödvändigt                            │
│                                                                          │
│  ✅ Auditing                                                            │
│     □ Logga RBAC-relaterade API-anrop                                  │
│     □ Granska bindings regelbundet                                     │
│     □ Använd kubectl auth can-i för testing                            │
│                                                                          │
│  ✅ Organization                                                        │
│     □ Använd Groups istället för individuella users                    │
│     □ Standardisera role-namn                                          │
│     □ Dokumentera custom roles                                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Sammanfattning & Task

### Quick Reference

| Resource | Scope | Use Case |
|----------|-------|----------|
| Role | Namespace | App-specific permissions |
| ClusterRole | Cluster | Cluster-wide resources |
| RoleBinding | Namespace | Bind to namespace Role |
| ClusterRoleBinding | Cluster | Bind cluster-wide |

### Praktisk Task

```bash
# Skapa setup för development team:
# 1. Namespace: dev-team
# 2. Role: developer (pods, deployments, services)
# 3. Role: deployer (full deploy access)
# 4. RoleBindings för team members
```

---

**Nästa Node:** Helm Basics →
''',
    "xp_reward": 160,
    "estimated_minutes": 55,
    "prerequisites": ["k8s_node_11"],
    "learning_outcomes": [
        "Förstå RBAC-konceptet",
        "Skapa Roles och ClusterRoles",
        "Konfigurera RoleBindings",
        "Implementera least privilege"
    ]
}

# Block 3 Part 2 exports
BLOCK_3_PART_2_NODES = [NODE_11, NODE_12]
