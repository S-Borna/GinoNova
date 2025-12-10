"""
Kubernetes Mastery Module
=========================

20 noder enligt Linux-mallen.
Komplett Kubernetes-kunskap - från pods till produktion.

Track: containers
Difficulty: intermediate
Estimated Hours: 35
"""

MODULE = {
    "name": "Kubernetes Mastery",
    "slug": "kubernetes-mastery",
    "description": "Komplett Kubernetes-orkestrering - från pods till produktion med naturlig svensk pedagogik",
    "track_slug": "containers",
    "order_index": 19,
    "difficulty": "intermediate",
    "estimated_hours": 35,
    "prerequisites": ["docker-mastery"],
    "icon": "☸️",
    "color": "#326CE5",
    "tasks": [
        {
            "title": "Kubernetes Architecture & Core Concepts",
            "slug": "kubernetes-architecture-core-concepts",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# Kubernetes Architecture & Core Concepts

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | Utan K8s-kunskap                | Med K8s-kunskap                |
|---------------------------|--------------------------------|--------------------------------|
| Klusterfel                | Gissar var felet ar            | Vet exakt vilken komponent     |
| Skalning                  | Manuell hantering              | Automatisk orkestrering        |
| Deployment                | SSH till servrar               | Deklarativ YAML                |
| HA och failover           | Komplex manuell setup          | Inbyggt i plattformen          |

Kubernetes ar STANDARD for container-orkestrering - du MASTE kunna det.

------------------------------------------------------------------

## Kubernetes Arkitektur

```
+-----------------------------------------------------------------+
|                    KUBERNETES CLUSTER                           |
+-----------------------------------------------------------------+
|                                                                 |
|  CONTROL PLANE                                                  |
|  -------------                                                  |
|  +---------------+  +---------------+  +---------------+       |
|  |  API Server   |  |   Scheduler   |  |  Controller   |       |
|  |               |  |               |  |   Manager     |       |
|  |  All traffic  |  |  Pod placement|  |  Reconcile    |       |
|  |  goes here    |  |  on nodes     |  |  desired state|       |
|  +---------------+  +---------------+  +---------------+       |
|           |                                                     |
|           ▼                                                     |
|  +---------------+                                              |
|  |     etcd      |  Distributed key-value store                |
|  |               |  Cluster state & config                      |
|  +---------------+                                              |
|                                                                 |
|  WORKER NODES                                                   |
|  ------------                                                   |
|  +---------------------------------------------------------+   |
|  |  Node 1                        Node 2                    |   |
|  |  +---------+ +---------+      +---------+ +---------+  |   |
|  |  | kubelet | |  Pods   |      | kubelet | |  Pods   |  |   |
|  |  +---------+ +---------+      +---------+ +---------+  |   |
|  |  +---------+                  +---------+              |   |
|  |  |kube-proxy|                  |kube-proxy|              |   |
|  |  +---------+                  +---------+              |   |
|  +---------------------------------------------------------+   |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Control Plane - Hjarnan i klustret

Control Plane fattar alla beslut om klustret. Den övervakar, schemalägger och reagerar på händelser.

```bash
kubectl cluster-info
# Visar information om Control Plane
# Du ser API-serverns adress
# CoreDNS-adressen visas också
# Detta är första kommandot för att verifiera att klustret fungerar

kubectl get componentstatuses
# Visar hälsostatus för Control Plane-komponenter
# scheduler - schemaläggaren som placerar pods
# controller-manager - hanterar controllers
# etcd - databasen som lagrar all klusterdata
# Alla ska visa "Healthy" för ett fungerande kluster

kubectl get nodes -o wide
# Visar alla noder i klustret med extra info
# -o wide ger mer detaljer som IP och OS
# STATUS ska vara "Ready" för fungerande noder
# ROLES visar om det är control-plane eller worker
```

---

## API Server - Klustrets receptionist

API Server är den enda komponenten som pratar direkt med etcd. All kommunikation går genom den.

```bash
kubectl api-resources
# Listar alla resurser som API:et stödjer
# Varje resurs har ett namn, shortname och API-grupp
# pods = po, services = svc, deployments = deploy
# Du ser också om resursen är namespaced eller inte

kubectl api-versions
# Visar alla API-versioner som stöds
# apps/v1 - för Deployments, StatefulSets
# v1 - core API för Pods, Services, ConfigMaps
# Äldre versioner som v1beta1 kan finnas men bör undvikas

kubectl get --raw /healthz
# Kollar API-serverns hälsa direkt
# --raw gör ett rått API-anrop utan formatering
# Returnerar "ok" om allt fungerar
# Användbart för health checks i monitoring
```

---

## etcd - Klustrets minne

etcd är en distribuerad key-value databas som lagrar hela klustrets tillstånd.

```bash
kubectl get pods -n kube-system | grep etcd
# Hittar etcd-podden i kube-system namespace
# etcd körs som en pod på control plane-noden
# Utan etcd fungerar ingenting - den är kritisk
# Backup av etcd = backup av hela klustret

# Exempel på etcd backup (kräver etcdctl):
# ETCDCTL_API=3 etcdctl snapshot save backup.db
# Skapar en snapshot av hela etcd-databasen
# backup.db innehåller all klusterdata
# Spara denna fil säkert - den är nyckeln till disaster recovery
```

---

## Worker Nodes - Arbetshästarna

Worker nodes kör dina containers. De tar emot instruktioner från Control Plane och rapporterar tillbaka status.

```bash
kubectl describe node <node-name>
# Visar detaljerad info om en specifik nod
# Capacity - hur mycket CPU/minne noden har
# Allocatable - hur mycket som kan användas av pods
# Conditions - Ready, DiskPressure, MemoryPressure
# Allocated resources - hur mycket som används just nu

kubectl top nodes
# Visar CPU och minnesanvändning per nod
# Kräver att metrics-server är installerat
# CPU visas i millicores (1000m = 1 CPU)
# Memory visas i bytes eller Mi/Gi
```

---

## Kubelet - Nodens agent

Kubelet kör på varje node och ser till att containers körs som de ska.

```bash
systemctl status kubelet
# Visar kubelet-tjänstens status
# Kubelet måste vara "active (running)"
# Om kubelet dör kan noden inte köra nya pods
# Första stället att kolla vid nodproblem

journalctl -u kubelet -f
# Följer kubelet-loggarna i realtid
# -u kubelet filtrerar för kubelet-tjänsten
# -f följer loggarna (som tail -f)
# Här ser du varför pods inte startar
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Control Plane             | Beslutsfattare - API Server, Scheduler, Controller  |
| Worker Nodes              | Arbetare - kor pods via kubelet                     |
| API Server                | ALL kommunikation gar genom den                     |
| etcd                      | Kritisk databas - backup ar livsviktig              |
| kubelet                   | Agent pa varje node som kor containers              |

------------------------------------------------------------------

## Kom ihag

- Control Plane = hjarnan, Worker Nodes = musklerna
- etcd backup ar KRITISK for disaster recovery
- kubectl ar ditt verktyg for att prata med klustret
- API Server ar single point of entry
- kubelet maste kora pa VARJE worker node
""",
        },
        {
            "title": "Pods - Smallest Deployable Unit",
            "slug": "pods-smallest-deployable-unit",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Pods - Smallest Deployable Unit

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | Forstaelse kravs                                    |
|---------------------------|-----------------------------------------------------|
| Felsoka containers        | Pod-status, logs, events                            |
| Multi-container apps      | Sidecar patterns, shared volumes                    |
| Resource management       | Requests vs Limits                                  |
| Networking                | Pod IP, container ports                             |

Pods ar det DU deployer - allt annat ar abstraktion ovanpa.

------------------------------------------------------------------

## Pod Anatomy

```
+-----------------------------------------------------------------+
|                          POD                                    |
+-----------------------------------------------------------------+
|  Pod IP: 10.244.1.5                                             |
|                                                                 |
|  +-----------------+  +-----------------+                      |
|  |   Container 1   |  |   Container 2   |                      |
|  |   (main app)    |  |   (sidecar)     |                      |
|  |   Port: 8080    |  |   Port: 9090    |                      |
|  +--------+--------+  +--------+--------+                      |
|           |                    |                                |
|           +--------+-----------+                                |
|                    |                                            |
|           +--------▼--------+                                   |
|           |  Shared Volume  |                                   |
|           |    /data        |                                   |
|           +-----------------+                                   |
|                                                                 |
|  Containers i samma pod:                                        |
|  - Delar natverk (localhost)                                    |
|  - Delar storage (volumes)                                      |
|  - Schemalaggas pa samma node                                   |
|  - Startar/stoppas tillsammans                                  |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

Pods är den minsta enheten i Kubernetes. Du deployar inte containers direkt - du deployar pods. Som DevOps behöver du förstå:

- **Vad en pod faktiskt är** så du kan designa rätt
- **När du ska ha flera containers i samma pod** vs separata pods
- **Pod-livscykeln** så du förstår vad som händer vid problem
- **Hur du felsöker pods** när saker går fel

---

## Så fungerar Pods

En pod är som ett **delat kontor för containers**. Containers i samma pod delar nätverk (localhost), lagring (volumes) och livscykel (startar och dör tillsammans). De flesta pods har bara en container - men ibland behöver du sidecars för logging, proxies eller liknande.

---

## Skapa och hantera Pods

```bash
kubectl run nginx --image=nginx:latest
# Skapar en enkel pod som kör nginx
# --image anger vilken container image som ska användas
# Podden får namnet "nginx"
# Detta är snabbaste sättet att testa en image

kubectl get pods
# Listar alla pods i current namespace
# NAME - poddens namn
# READY - antal redo containers / totalt
# STATUS - Running, Pending, CrashLoopBackOff, etc.
# AGE - hur länge podden har existerat

kubectl get pods -o wide
# Visar extra information
# IP - poddens interna IP-adress
# NODE - vilken node podden körs på
# Användbart för att se var pods har placerats

kubectl get pods -w
# Watch mode - uppdateras i realtid
# -w följer ändringar live
# Perfekt när du väntar på att pods ska starta
# Ctrl+C för att avsluta
```

---

## Pod YAML - Deklarativ konfiguration

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-server
  labels:
    app: web
    environment: production
spec:
  containers:
  - name: nginx
    image: nginx:1.21
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

```bash
kubectl apply -f pod.yaml
# Skapar eller uppdaterar podden från YAML-filen
# apply är idempotent - säkert att köra flera gånger
# Kubernetes jämför önskat tillstånd med nuvarande
# Endast nödvändiga ändringar görs

kubectl get pod web-server -o yaml
# Visar poddens fullständiga YAML
# Inkluderar status-fält som Kubernetes lagt till
# Bra för att se vad som faktiskt körs
# Använd detta för att lära dig YAML-strukturen
```

---

## Felsöka Pods

```bash
kubectl describe pod <pod-name>
# Visar detaljerad information om podden
# Events - visar vad som hänt (scheduling, pulling, starting)
# Conditions - Ready, Initialized, ContainersReady
# Om podden inte startar - börja här!

kubectl logs <pod-name>
# Visar container-loggarna
# Samma som docker logs men för pods
# Om podden har flera containers: kubectl logs <pod> -c <container>
# Här ser du applikationens output och fel

kubectl logs <pod-name> --previous
# Visar loggar från förra körningen
# Kritiskt vid CrashLoopBackOff
# --previous visar loggar innan containern crashade
# Utan denna flagga ser du bara den nuvarande (tomma) körningen

kubectl exec -it <pod-name> -- /bin/bash
# Öppnar ett shell i containern
# -it = interactive terminal
# -- separerar kubectl-argument från kommandot
# Använd för att felsöka inifrån containern
```

---

## Pod-livscykeln

```bash
kubectl get pods -o jsonpath='{.items[*].status.phase}'
# Visar pod-faserna för alla pods
# Pending - väntar på scheduling eller image pull
# Running - minst en container kör
# Succeeded - alla containers avslutade OK (för Jobs)
# Failed - minst en container avslutade med fel

kubectl delete pod <pod-name>
# Tar bort podden
# Kubernetes skickar SIGTERM till containern
# Väntar 30 sekunder (terminationGracePeriodSeconds)
# Skickar sedan SIGKILL om containern inte avslutat

kubectl delete pod <pod-name> --force --grace-period=0
# Tvingar omedelbar borttagning
# Hoppar över graceful shutdown
# Använd endast om podden hängt sig
# Kan orsaka problem om containern skriver data
```

---

## Multi-container Pods

```bash
kubectl logs <pod-name> -c <container-name>
# Visar loggar för en specifik container i podden
# -c anger vilken container
# Nödvändigt när podden har flera containers
# Utan -c får du fel om det finns flera containers

kubectl exec -it <pod-name> -c <container-name> -- /bin/sh
# Shell i specifik container
# Samma princip som logs
# Sidecars har ofta bara /bin/sh, inte bash
# Testa sh om bash inte finns
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Pod                       | En eller flera containers som delar natverk/storage |
| En container per pod      | Vanligaste monstret - enklast att hantera           |
| kubectl describe          | Forsta stoppet vid felskning                        |
| kubectl logs --previous   | Livraddare vid CrashLoopBackOff                     |
| Efemara pods              | De kan do och aterskapas nar som helst              |

------------------------------------------------------------------

## Kom ihag

- En pod = en IP-adress (delar mellan containers)
- Sidecar pattern for logging, proxies, metrics
- kubectl exec for att felsoka inifrn container
- YAML ar preferred over kubectl run i produktion
- Pod som crashar = kolla events och logs
""",
        },
        {
            "title": "ReplicaSets & Deployments",
            "slug": "replicasets-deployments",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# ReplicaSets & Deployments

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | Utan Deployments                | Med Deployments                |
|---------------------------|--------------------------------|--------------------------------|
| Pod som dor               | Manuellt starta ny             | Automatiskt ersatt             |
| Uppdatera app             | Downtime vid byte              | Rolling update utan downtime   |
| Trasig release            | Panic och manuell rollback     | kubectl rollout undo           |
| Skalning                  | Manuellt hantera pods          | kubectl scale eller HPA        |

Du kor ALDRIG nakna pods i produktion - alltid Deployments.

------------------------------------------------------------------

## Deployment Hierarki

```
+-----------------------------------------------------------------+
|                    DEPLOYMENT HIERARCHY                         |
+-----------------------------------------------------------------+
|                                                                 |
|  DEPLOYMENT (web-app)                                           |
|  ---------------------                                          |
|  replicas: 3                                                    |
|  strategy: RollingUpdate                                        |
|       |                                                         |
|       ▼                                                         |
|  REPLICASET (web-app-7d9f8b6c4)                                |
|  ----------------------------                                   |
|  desired: 3, current: 3, ready: 3                               |
|       |                                                         |
|       +------------+------------+                               |
|       ▼            ▼            ▼                               |
|  +---------+  +---------+  +---------+                         |
|  |  POD 1  |  |  POD 2  |  |  POD 3  |                         |
|  | nginx   |  | nginx   |  | nginx   |                         |
|  | 1.21    |  | 1.21    |  | 1.21    |                         |
|  +---------+  +---------+  +---------+                         |
|                                                                 |
|  Du skapar: Deployment                                          |
|  K8s skapar: ReplicaSet -> Pods                                  |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Skapa en Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
```

```bash
kubectl apply -f deployment.yaml
# Skapar deployment från YAML-filen
# Kubernetes skapar automatiskt en ReplicaSet
# ReplicaSet skapar 3 pods (enligt replicas: 3)
# Alla resurser får labels för spårbarhet

kubectl get deployments
# Listar alla deployments
# READY visar antal redo pods / önskat antal
# UP-TO-DATE visar pods med senaste konfigurationen
# AVAILABLE visar pods som kan ta emot trafik
```

---

## Hantera replicas

```bash
kubectl scale deployment web-app --replicas=5
# Ändrar antal replicas till 5
# Kubernetes skapar 2 nya pods
# Befintliga pods påverkas inte
# Nedsklaningen fungerar likadant

kubectl get pods -l app=web
# Visar alla pods med label app=web
# -l filtrerar på labels
# Du ser nu 5 pods istället för 3
# Alla har unika namn som web-app-xxx-yyy

kubectl autoscale deployment web-app --min=2 --max=10 --cpu-percent=80
# Skapar en HorizontalPodAutoscaler (HPA)
# --min=2 - aldrig färre än 2 pods
# --max=10 - aldrig fler än 10 pods
# --cpu-percent=80 - skala upp vid 80% CPU
# Kräver metrics-server för att fungera
```

---

## Rolling Updates

```bash
kubectl set image deployment/web-app nginx=nginx:1.22
# Uppdaterar image till nginx:1.22
# Kubernetes gör en rolling update
# Nya pods skapas med nya imagen
# Gamla pods tas bort gradvis
# Ingen downtime om allt går rätt

kubectl rollout status deployment/web-app
# Visar status på pågående rollout
# "deployment web-app successfully rolled out"
# Eller visar progress om den pågår
# Väntar tills rollout är klar

kubectl rollout history deployment/web-app
# Visar historik över alla revisioner
# REVISION - versionsnummer
# CHANGE-CAUSE - varför ändringen gjordes
# Behöver --record flaggan vid ändringar för CHANGE-CAUSE
```

---

## Rollbacks

```bash
kubectl rollout undo deployment/web-app
# Rullar tillbaka till föregående version
# Kubernetes skapar en ny ReplicaSet (eller använder gammal)
# Pods byts ut som vid en vanlig update
# Snabbt sätt att återställa vid problem

kubectl rollout undo deployment/web-app --to-revision=2
# Rullar tillbaka till specifik revision
# Kolla revision med 'rollout history' först
# Användbart om flera versioner är dåliga
# Revision 2 blir nu den aktiva

kubectl rollout pause deployment/web-app
# Pausar en pågående rollout
# Bra om du ser problem och vill undersöka
# Inga fler pods uppdateras
# Befintliga pods påverkas inte

kubectl rollout resume deployment/web-app
# Återupptar en pausad rollout
# Fortsätter där den slutade
# Används efter felsökning
# Eller för att fortsätta en canary-deploy
```

---

## ReplicaSets under huven

```bash
kubectl get replicasets
# Visar alla ReplicaSets
# En deployment skapar en ny ReplicaSet vid varje ändring
# Gamla ReplicaSets behålls för rollbacks
# NAME innehåller en hash för att vara unik

kubectl describe replicaset <rs-name>
# Visar detaljer om en ReplicaSet
# Controlled By - vilken Deployment som äger den
# Replicas - önskat/nuvarande/redo antal
# Events - visar skapande av pods

kubectl get pods --show-labels
# Visar alla pods med deras labels
# pod-template-hash identifierar vilken ReplicaSet
# Samma hash som i ReplicaSet-namnet
# Kubernetes använder detta för att matcha pods
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Deployment                | Det du skapar - hanterar ReplicaSets automatiskt    |
| ReplicaSet                | Ser till att ratt antal pods kor                    |
| Rolling updates           | Zero-downtime deploys med gradvis byte              |
| Rollbacks                 | kubectl rollout undo for snabb aterstallning        |
| Skalning                  | --replicas manuellt eller HPA for automatik         |

------------------------------------------------------------------

## Kom ihag

- Deployment -> ReplicaSet -> Pods (hierarkin)
- Aldrig redigera ReplicaSets direkt - lat Deployment hantera
- rollout history visar alla revisioner for rollback
- HPA kraver metrics-server for att fungera
- Gamla ReplicaSets behalls for rollback-mojlighet
""",
        },
        {
            "title": "Services & Networking",
            "slug": "services-networking",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Services & Networking

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Service Type              | Anvandning                                          |
|---------------------------|-----------------------------------------------------|
| ClusterIP                 | Intern kommunikation mellan pods                    |
| NodePort                  | Exponera pa nodernas IP:port                        |
| LoadBalancer              | Cloud load balancer (AWS ELB, GCP LB)               |
| ExternalName              | DNS CNAME till extern tjanst                        |

Services ger STABIL endpoint trots att pods ar efemara.

------------------------------------------------------------------

## Service Typer

```
+-----------------------------------------------------------------+
|                    KUBERNETES SERVICES                          |
+-----------------------------------------------------------------+
|                                                                 |
|  CLUSTERIP (default)           NODEPORT                         |
|  ------------------           --------                          |
|  +-------------+              +-------------+                   |
|  | 10.96.0.100 |              | NodeIP:30080|                   |
|  |   :80       |              |   :30080    |                   |
|  +------+------+              +------+------+                   |
|         |                            |                          |
|    Intern endast               Extern via node IP               |
|                                                                 |
|  LOADBALANCER                  EXTERNALNAME                     |
|  ------------                  ------------                     |
|  +-------------+              +-------------+                   |
|  | 34.56.78.90 |              | CNAME:      |                   |
|  |   :80       |              | db.aws.com  |                   |
|  +------+------+              +-------------+                   |
|         |                                                       |
|    Cloud LB                    DNS alias                        |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## ClusterIP - Intern kommunikation

```yaml
# service-clusterip.yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
  - port: 80
    targetPort: 8080
```

```bash
kubectl apply -f service-clusterip.yaml
# Skapar en ClusterIP service
# ClusterIP är default-typen
# Endast åtkomlig inifrån klustret
# Perfekt för interna microservices

kubectl get services
# Listar alla services
# CLUSTER-IP visar den interna IP:n
# PORT(S) visar port-mappningen
# Externa klienter kan INTE nå ClusterIP

kubectl get endpoints backend-service
# Visar vilka pods som servicen pekar på
# ENDPOINTS listar IP:port för varje pod
# Om listan är tom - inga pods matchar selectorn
# Första stället att kolla om trafik inte fungerar
```

---

## NodePort - Enkel extern åtkomst

```yaml
# service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: NodePort
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```

```bash
kubectl apply -f service-nodeport.yaml
# Skapar en NodePort service
# Öppnar port 30080 på ALLA noder
# Du kan nå servicen via <node-ip>:30080
# NodePort-range är 30000-32767 som default

kubectl get svc web-service
# Visar service-info
# PORT(S) visar 80:30080/TCP
# 80 = service port, 30080 = node port
# TYPE visar NodePort

curl http://<node-ip>:30080
# Når servicen via nodens externa IP
# Fungerar från vilken node som helst
# Kubernetes routar till rätt pod automatiskt
# Enkelt men inte för produktion (ingen SSL, load balancer)
```

---

## LoadBalancer - Cloud load balancing

```yaml
# service-loadbalancer.yaml
apiVersion: v1
kind: Service
metadata:
  name: public-web
spec:
  type: LoadBalancer
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
```

```bash
kubectl apply -f service-loadbalancer.yaml
# Skapar en LoadBalancer service
# Cloud provider skapar en extern load balancer
# Fungerar på AWS, GCP, Azure, etc.
# På bare-metal behöver du MetalLB eller liknande

kubectl get svc public-web
# EXTERNAL-IP visar load balancerns IP
# Kan ta några minuter att provisionera
# <pending> betyder att det fortfarande skapas
# När IP:n syns kan du nå tjänsten externt

kubectl describe svc public-web
# Visar mer detaljer
# LoadBalancer Ingress visar extern IP
# Events visar eventuella problem
# Bra för felsökning av load balancer-skapande
```

---

## DNS och Service Discovery

```bash
kubectl run debug --image=busybox --rm -it -- /bin/sh
# Startar en debug-pod för nätverkstester
# --rm tar bort podden när du avslutar
# -it ger interaktiv terminal
# busybox har nätverksverktyg

# Inne i debug-podden:
nslookup backend-service
# Slår upp DNS för servicen
# Server visar kube-dns/CoreDNS
# Address visar servicens ClusterIP
# Kubernetes DNS fungerar automatiskt

wget -qO- http://backend-service
# Når servicen via dess DNS-namn
# Fungerar för services i samma namespace
# -qO- skriver output till stdout
# Ingen IP behövs - DNS löser det

wget -qO- http://backend-service.default.svc.cluster.local
# Fullständigt DNS-namn (FQDN)
# backend-service = service-namn
# default = namespace
# svc.cluster.local = kluster-suffix
# Använd FQDN för cross-namespace-kommunikation
```

---

## Headless Services

```yaml
# service-headless.yaml
apiVersion: v1
kind: Service
metadata:
  name: db-headless
spec:
  clusterIP: None
  selector:
    app: database
  ports:
  - port: 5432
```

```bash
kubectl apply -f service-headless.yaml
# Skapar en headless service (clusterIP: None)
# Ingen ClusterIP allokeras
# DNS returnerar alla pod-IP:er direkt
# Används för stateful apps som databaser

nslookup db-headless
# Returnerar IP för varje pod, inte en service-IP
# Klienten kan välja vilken pod den vill prata med
# Viktigt för databas-replikering och liknande
# StatefulSets använder ofta headless services
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| ClusterIP                 | Intern kommunikation (default typ)                  |
| NodePort                  | Enkel extern atkomst via nodernas portar            |
| LoadBalancer              | Cloud load balancer for produktion                  |
| DNS                       | Services nas via namn, inte IP                      |
| Endpoints                 | Lista over pods som matchar selector                |

------------------------------------------------------------------

## Kom ihag

- ClusterIP ar default - intern endast
- NodePort range: 30000-32767
- LoadBalancer fungerar bara i cloud (AWS/GCP/Azure)
- DNS format: service.namespace.svc.cluster.local
- Headless (clusterIP: None) for StatefulSets
""",
        },
        {
            "title": "ConfigMaps & Secrets",
            "slug": "configmaps-secrets",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# ConfigMaps & Secrets

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem                   | Utan ConfigMaps/Secrets         | Med ConfigMaps/Secrets          |
|---------------------------|--------------------------------|--------------------------------|
| Miljo-specifik config     | Rebuild image per miljo        | Samma image, olika config      |
| Losenord i kod            | Lackt i Git                    | Separerad och krypterad        |
| Config-andring            | Ny deploy kravs                | Dynamisk uppdatering           |
| Audit                     | Ingen sparbarhet               | Kubernetes RBAC och logs       |

Separation av config fran kod ar KRITISK for sakerhet och flexibilitet.

------------------------------------------------------------------

## ConfigMaps vs Secrets

```
+-----------------------------------------------------------------+
|                    CONFIGMAPS VS SECRETS                        |
+-----------------------------------------------------------------+
|                                                                 |
|  CONFIGMAPS                        SECRETS                      |
|  ----------                        -------                      |
|  - Plain text                      - Base64 encoded             |
|  - Icke-kanslig data               - Kanslig data               |
|  - LOG_LEVEL=debug                 - DB_PASSWORD=xxx            |
|  - Max 1 MB                        - Max 1 MB                   |
|                                                                 |
|  ANVANDNING:                       ANVANDNING:                  |
|  - App config                      - Losenord                   |
|  - Feature flags                   - API-nycklar                |
|  - Endpoints                       - TLS-certifikat             |
|                                                                 |
|  MONTERING:                                                     |
|  +---------------------------------------------+               |
|  |  ENV VARS        eller        VOLUME MOUNT  |               |
|  |  DB_HOST=xxx                  /etc/config/  |               |
|  +---------------------------------------------+               |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Skapa ConfigMaps

```bash
kubectl create configmap app-config --from-literal=DB_HOST=postgres --from-literal=LOG_LEVEL=info
# Skapar ConfigMap från kommandoraden
# --from-literal lägger till key=value par
# app-config blir namnet på ConfigMappen
# Perfekt för snabba tester och små konfigurationer

kubectl create configmap nginx-config --from-file=nginx.conf
# Skapar ConfigMap från en fil
# Filnamnet blir key, innehållet blir value
# Hela filen lagras i ConfigMappen
# Bra för konfigurationsfiler som nginx.conf

kubectl get configmaps
# Listar alla ConfigMaps i namespace
# DATA visar antal key-value par
# AGE visar när den skapades
# Snabb överblick över konfigurationer

kubectl describe configmap app-config
# Visar innehållet i ConfigMappen
# Data-sektionen visar alla key-value par
# Känslig data syns i klartext här!
# Använd Secrets för känslig data istället
```

---

## ConfigMap YAML

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-settings
data:
  DATABASE_HOST: "postgres.default.svc.cluster.local"
  DATABASE_PORT: "5432"
  LOG_LEVEL: "info"
  FEATURE_FLAG_NEW_UI: "true"
```

```bash
kubectl apply -f configmap.yaml
# Skapar eller uppdaterar ConfigMappen
# YAML är bättre för versionskontroll
# Lätt att se alla värden på en gång
# Kan inkluderas i samma repo som applikationen
```

---

## Använda ConfigMaps i Pods

```yaml
# pod-with-configmap.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app
    image: myapp:latest
    envFrom:
    - configMapRef:
        name: app-settings
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: nginx-config
```

```bash
kubectl apply -f pod-with-configmap.yaml
# envFrom laddar ALLA keys som miljövariabler
# volumeMounts monterar ConfigMap som filer
# Båda metoderna kan kombineras
# Välj baserat på hur appen läser konfiguration

kubectl exec app-pod -- env | grep DATABASE
# Verifierar att miljövariabler är satta
# DATABASE_HOST och DATABASE_PORT ska synas
# Appen kan nu läsa dem som vanliga env vars
# Ingen ändring i applikationskoden behövs

kubectl exec app-pod -- cat /etc/config/nginx.conf
# Visar den monterade konfigurationsfilen
# Filen finns i containern som om den kopierats dit
# Uppdateringar propageras automatiskt (med fördröjning)
# Perfekt för appar som läser konfig från fil
```

---

## Secrets - För känslig data

```bash
kubectl create secret generic db-credentials --from-literal=username=admin --from-literal=password=supersecret
# Skapar en Secret från kommandoraden
# generic är den vanligaste typen
# Data base64-kodas automatiskt
# OBS: base64 är INTE kryptering!

kubectl get secrets
# Listar alla Secrets
# TYPE visar typen (Opaque, kubernetes.io/tls, etc.)
# DATA visar antal keys
# Känslig data visas inte i listan

kubectl get secret db-credentials -o yaml
# Visar Secret med base64-kodad data
# data-fältet innehåller kodade värden
# Avkoda med: echo "xxx" | base64 -d
# I produktion - använd extern secrets manager!
```

---

## Secret YAML

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: api-keys
type: Opaque
data:
  API_KEY: YXBpLWtleS0xMjM0NTY=
  SECRET_TOKEN: c3VwZXItc2VjcmV0LXRva2Vu
```

```bash
echo -n "api-key-123456" | base64
# YXBpLWtleS0xMjM0NTY=
# Kodar ett värde till base64 för YAML
# -n förhindrar newline i slutet
# Resultatet går in i data-fältet

kubectl apply -f secret.yaml
# Skapar Secret från YAML
# Värden måste vara base64-kodade i YAML
# Kubernetes avkodar automatiskt vid användning
# Alternativt: använd stringData för klartext i YAML
```

---

## Använda Secrets i Pods

```yaml
# pod-with-secret.yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
    volumeMounts:
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secret-volume
    secret:
      secretName: api-keys
```

```bash
kubectl exec secure-app -- env | grep DB_PASSWORD
# Verifierar att secret är tillgänglig som env var
# Värdet är avkodat (inte base64)
# Appen använder det som vanlig miljövariabel
# Aldrig logga miljövariabler i produktion!

kubectl exec secure-app -- cat /etc/secrets/API_KEY
# Läser secret från monterad volym
# Filen innehåller det avkodade värdet
# readOnly: true förhindrar ändringar
# Säkrare än miljövariabler för vissa användningsfall
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| ConfigMaps                | Icke-kanslig konfiguration i key-value format       |
| Secrets                   | Kanslig data (endast base64-kodad som standard)     |
| envFrom                   | Ladda alla keys som environment variables           |
| volumeMounts              | Montera som filer i container                       |
| Produktion                | Anvand extern secrets manager (Vault, AWS SM)       |

------------------------------------------------------------------

## Kom ihag

- base64 ar INTE kryptering - bara encoding
- Secrets ar inte sakra utan extern lsning (Sealed Secrets, Vault)
- stringData i YAML undviker manuell base64-encoding
- Volume-monterad secret uppdateras automatiskt (med delay)
- Env vars uppdateras INTE - pod maste restartas
""",
        },
        {
            "title": "Namespaces & Resource Organization",
            "slug": "namespaces-resource-organization",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Namespaces & Resource Organization

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | Utan Namespaces                 | Med Namespaces                  |
|---------------------------|--------------------------------|--------------------------------|
| Multi-team kluster        | Namnkonflikter                 | Isolerade resurser             |
| Dev/Staging/Prod          | Riskabel mix                   | Separerade miljoer             |
| Resurskontroll            | Ingen begransning              | ResourceQuota per namespace    |
| Access control            | All-or-nothing                 | RBAC per namespace             |

Namespaces ar GRUNDLAGGANDE for kluster-organisation.

------------------------------------------------------------------

## Namespace Struktur

```
+-----------------------------------------------------------------+
|                    KUBERNETES NAMESPACES                        |
+-----------------------------------------------------------------+
|                                                                 |
|  SYSTEM NAMESPACES                                              |
|  -----------------                                              |
|  kube-system      Kubernetes komponenter (CoreDNS, etc)         |
|  kube-public      Publikt lasbar data                          |
|  kube-node-lease  Node heartbeats                               |
|  default          Resurser utan explicit namespace              |
|                                                                 |
|  USER NAMESPACES                                                |
|  ---------------                                                |
|  +-------------+  +-------------+  +-------------+             |
|  | development |  |   staging   |  | production  |             |
|  | - web-app   |  | - web-app   |  | - web-app   |             |
|  | - api       |  | - api       |  | - api       |             |
|  | - db        |  | - db        |  | - db        |             |
|  +-------------+  +-------------+  +-------------+             |
|                                                                 |
|  Samma namn, olika namespaces = isolerade resurser              |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Standardnamespaces

```bash
kubectl get namespaces
# Listar alla namespaces i klustret
# default - där resurser hamnar om inget anges
# kube-system - Kubernetes interna komponenter
# kube-public - publikt läsbar data
# kube-node-lease - node heartbeats

kubectl get pods -n kube-system
# Visar pods i kube-system namespace
# -n anger namespace
# Här kör CoreDNS, kube-proxy, etc.
# Rör aldrig dessa om du inte vet vad du gör!

kubectl get all --all-namespaces
# Visar ALLA resurser i ALLA namespaces
# --all-namespaces eller -A
# Bra för att få överblick
# Kan bli mycket output i stora kluster
```

---

## Skapa och hantera Namespaces

```bash
kubectl create namespace development
# Skapar ett nytt namespace
# Namnet måste vara unikt i klustret
# Använd beskrivande namn (team-frontend, env-staging)
# Namespaces är gratis - skapa så många du behöver

kubectl config set-context --current --namespace=development
# Sätter default namespace för kubectl
# Nu slipper du skriva -n development hela tiden
# --current ändrar nuvarande context
# Verifiera med: kubectl config view --minify

kubectl get pods
# Visar pods i development namespace (nu default)
# Ingen -n behövs längre
# Mycket smidigare för dagligt arbete
# Kom ihåg att byta tillbaka när du är klar!
```

---

## Namespace YAML

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    environment: production
    team: platform
```

```bash
kubectl apply -f namespace.yaml
# Skapar namespace från YAML
# Labels hjälper till att kategorisera
# Kan användas för policy-enforcement
# Bra för GitOps - namespace definierat i kod
```

---

## Resurser i specifika Namespaces

```yaml
# deployment-in-namespace.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:latest
```

```bash
kubectl apply -f deployment-in-namespace.yaml
# Skapar deployment i production namespace
# namespace: production i metadata
# Alternativt: kubectl apply -f file.yaml -n production
# YAML-definition har företräde om båda anges

kubectl get deployments -n production
# Verifierar att deployment skapades
# Visar endast deployments i production
# Andra namespaces påverkas inte
# Samma namn kan finnas i andra namespaces
```

---

## ResourceQuotas

```yaml
# resourcequota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: development
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    pods: "20"
    services: "10"
```

```bash
kubectl apply -f resourcequota.yaml
# Skapar resursbegränsning för namespace
# Begränsar totala resurser som kan användas
# Förhindrar att ett team tar alla resurser
# Tvingar fram resource requests/limits i pod specs

kubectl describe resourcequota dev-quota -n development
# Visar kvota och nuvarande användning
# Used vs Hard visar förbrukning
# Om Used når Hard - inga fler resurser kan skapas
# Bra för att förstå kapacitet
```

---

## LimitRanges

```yaml
# limitrange.yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: development
spec:
  limits:
  - default:
      cpu: "500m"
      memory: "256Mi"
    defaultRequest:
      cpu: "100m"
      memory: "128Mi"
    type: Container
```

```bash
kubectl apply -f limitrange.yaml
# Sätter default resource requests/limits
# Containers utan limits får dessa automatiskt
# Förhindrar pods utan resursgränser
# Säkrar klustret från resource exhaustion

kubectl describe limitrange default-limits -n development
# Visar konfigurerade limits
# Default, DefaultRequest, Min, Max visas
# Alla containers i namespace följer dessa
# Kan overridas per pod om det behövs
```

---

## Cross-namespace kommunikation

```bash
kubectl exec debug-pod -- wget -qO- http://backend-service.production.svc.cluster.local
# Når en service i annat namespace
# backend-service = service namn
# production = namespace
# svc.cluster.local = kluster DNS-suffix
# Fungerar om nätverkspolicies tillåter det

kubectl get svc -A | grep backend
# Söker efter backend-services i alla namespaces
# -A = --all-namespaces
# NAMESPACE-kolumnen visar var varje service finns
# Hjälper att hitta rätt service att prata med
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Namespaces                | Logiska granser for resurser                        |
| kube-system               | Hands off - Kubernetes interna komponenter          |
| ResourceQuotas            | Begransar total resursanvandning per namespace      |
| LimitRanges               | Satter default limits for containers                |
| Cross-namespace DNS       | service.namespace.svc.cluster.local                 |

------------------------------------------------------------------

## Kom ihag

- default namespace ar for test - anvand egna namespaces i prod
- ResourceQuota utan requests/limits i pods = deployment blockeras
- kubectl config set-context --current --namespace=X andar default
- Vissa resurser ar cluster-wide (nodes, PVs, namespaces sjalva)
- Ta bort namespace = tar bort ALLT i det (var forsiktig!)
""",
        },
        {
            "title": "Labels, Selectors & Annotations",
            "slug": "labels-selectors-annotations",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 65,
            "content": """# Labels, Selectors & Annotations

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Anvandning                | Label/Selector                                      |
|---------------------------|-----------------------------------------------------|
| Service routing           | selector matchar pod labels                         |
| Deployment pods           | matchLabels kopplar ReplicaSet till pods            |
| Node affinity             | Schemalagga pa specifika noder                      |
| Batch operationer         | kubectl delete pods -l app=nginx                    |

Labels ar LIMET som haller ihop Kubernetes-resurser.

------------------------------------------------------------------

## Labels vs Annotations

```
+-----------------------------------------------------------------+
|                    LABELS VS ANNOTATIONS                        |
+-----------------------------------------------------------------+
|                                                                 |
|  LABELS                            ANNOTATIONS                  |
|  ------                            -----------                  |
|  - Key-value pairs                 - Key-value pairs            |
|  - Identifiera objekt              - Metadata/information       |
|  - Anvands av selectors            - INTE for selektion         |
|  - Max 63 chars value              - Storre varden (4KB)        |
|                                                                 |
|  EXEMPEL:                          EXEMPEL:                     |
|  app: nginx                        build-timestamp: "2024-01"   |
|  environment: prod                 git-commit: "abc123"         |
|  version: v1.2.3                   description: "Main web"      |
|  team: platform                    contact: "ops@company.com"   |
|                                                                 |
|  ANVANDNING:                       ANVANDNING:                  |
|  kubectl get pods -l app=nginx     Tooling (Helm, ArgoCD)       |
|  Service selector                  Audit information            |
|  Deployment matchLabels            Dokumentation                |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Lagga till Labels

```bash
kubectl label pods web-pod environment=production
# Lägger till label på en befintlig pod
# environment är key, production är value
# Labels är fritt definierade - välj vad som passar
# Vanliga: app, environment, version, team, tier

kubectl label pods web-pod version=1.2.3
# Lägger till ytterligare en label
# En resurs kan ha hur många labels som helst
# Labels är oberoende av varandra
# Använd dem för att kategorisera på flera sätt

kubectl label pods web-pod environment=staging --overwrite
# Ändrar en befintlig label
# --overwrite krävs för att ändra värde
# Utan flaggan får du ett felmeddelande
# Var försiktig - kan påverka selektorer!

kubectl label pods web-pod version-
# Tar bort en label (notera minustecknet)
# key- (med minus i slutet) tar bort
# Podden har inte längre version-labeln
# Andra labels påverkas inte
```

---

## Labels i YAML

```yaml
# pod-with-labels.yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-server
  labels:
    app: web
    environment: production
    version: "2.1.0"
    team: frontend
    tier: backend
spec:
  containers:
  - name: nginx
    image: nginx:latest
```

```bash
kubectl apply -f pod-with-labels.yaml
# Skapar pod med alla labels
# Labels definieras i metadata.labels
# Citattecken runt version behövs (börjar med siffra)
# Samma labels kan användas på andra resurser
```

---

## Selectors - Filtrera resurser

```bash
kubectl get pods -l app=web
# Visar alla pods med label app=web
# -l är kort för --selector
# Endast matchande pods visas
# Grundläggande filtrering

kubectl get pods -l environment=production,tier=backend
# Flera villkor (AND)
# Komma betyder OCH
# Båda labels måste matcha
# Kraftfull filtrering

kubectl get pods -l 'environment in (production, staging)'
# Set-based selector
# in matchar flera värden
# Visar pods i production ELLER staging
# Citattecken behövs för shell-escaping

kubectl get pods -l 'app!=legacy'
# Negation - alla UTOM legacy
# != betyder "inte lika med"
# Visar alla pods som inte har app=legacy
# Användbart för att exkludera gamla versioner
```

---

## Selectors i Services

```yaml
# service-with-selector.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
    environment: production
  ports:
  - port: 80
    targetPort: 8080
```

```bash
kubectl apply -f service-with-selector.yaml
# Service skickar trafik till pods som matchar ALLA labels
# app=web OCH environment=production måste matcha
# Om en pod saknar en label - ingen trafik
# Selector är hjärtat i Kubernetes service discovery

kubectl get endpoints web-service
# Visar vilka pods som matchar
# Listan uppdateras automatiskt
# Om tom - inga pods matchar selectorn
# Första stället att kolla vid routingproblem
```

---

## Annotations - Metadata utan filtrering

```bash
kubectl annotate pods web-pod description="Main web server"
# Lägger till annotation
# Annotations filtreras INTE med selectors
# Används för metadata, dokumentation, verktyg
# Större värden tillåtna än labels

kubectl annotate pods web-pod kubernetes.io/change-cause="Updated to v2.0"
# Annotation för rollout-historik
# kubernetes.io/ prefix för Kubernetes-standard
# Används av kubectl rollout history
# Dokumenterar varför ändringar gjordes

kubectl describe pod web-pod
# Annotations visas i describe output
# Hittas under Annotations-sektionen
# Kan innehålla JSON, URLs, långa beskrivningar
# Verktyg som Prometheus använder annotations
```

---

## Annotations YAML

```yaml
# pod-with-annotations.yaml
apiVersion: v1
kind: Pod
metadata:
  name: monitored-app
  labels:
    app: monitored
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "9090"
    description: "Application with Prometheus metrics"
    contact: "platform-team@company.com"
spec:
  containers:
  - name: app
    image: myapp:latest
```

```bash
kubectl apply -f pod-with-annotations.yaml
# Prometheus hittar podden via annotations
# prometheus.io/scrape: "true" aktiverar scraping
# prometheus.io/port anger vilken port
# Ingen ändring i Prometheus config behövs!
```

---

## Vanliga Label-konventioner

```yaml
# recommended-labels.yaml
metadata:
  labels:
    app.kubernetes.io/name: myapp
    app.kubernetes.io/instance: myapp-production
    app.kubernetes.io/version: "1.2.3"
    app.kubernetes.io/component: frontend
    app.kubernetes.io/part-of: e-commerce
    app.kubernetes.io/managed-by: helm
```

```bash
kubectl get pods -l 'app.kubernetes.io/part-of=e-commerce'
# Kubernetes rekommenderade labels
# Standardiserat över verktyg och team
# Helm, ArgoCD, och andra verktyg förstår dem
# Ger konsistens i stora organisationer
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Labels                    | For filtrering och selektion (key-value)            |
| Annotations               | For metadata och verktyg (storre varden)            |
| Selectors                 | Hur Services och Deployments hittar pods            |
| Komma-separator           | AND-logik (app=web,env=prod)                        |
| in() operator             | OR-logik (env in (dev,staging))                     |

------------------------------------------------------------------

## Kom ihag

- Labels ar for SELEKTION, annotations ar for INFORMATION
- Service selector MASTE matcha pod labels
- app.kubernetes.io/ prefix ar Kubernetes-standard
- prometheus.io/scrape annotation aktiverar auto-discovery
- --show-labels ar din van vid felskning
""",
        },
        {
            "title": "Ingress Controllers & Routing",
            "slug": "ingress-controllers-routing",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Ingress Controllers & Routing

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | LoadBalancer per service        | Ingress                         |
|---------------------------|--------------------------------|--------------------------------|
| 10 tjanster               | 10 LBs ($$$)                   | 1 Ingress Controller           |
| TLS-certifikat            | Per service                    | Centraliserat                  |
| Routing-regler            | Extern (DNS)                   | I klustret (YAML)              |
| Rate limiting             | Extern service                 | Inbyggt (annotations)          |

Ingress ar KOSTNADSEFFEKTIVT och KRAFTFULLT for HTTP-routing.

------------------------------------------------------------------

## Ingress Arkitektur

```
+-----------------------------------------------------------------+
|                    INGRESS TRAFFIC FLOW                         |
+-----------------------------------------------------------------+
|                                                                 |
|  INTERNET                                                       |
|     |                                                           |
|     ▼                                                           |
|  +-----------------------------------------+                   |
|  |        CLOUD LOAD BALANCER              |                   |
|  |        (AWS ALB / GCP LB)               |                   |
|  +----------------+------------------------+                   |
|                   |                                             |
|                   ▼                                             |
|  +-----------------------------------------+                   |
|  |      INGRESS CONTROLLER (NGINX)         |                   |
|  |                                         |                   |
|  |  Regler:                                |                   |
|  |  - api.example.com  -> api-service       |                   |
|  |  - www.example.com  -> web-service       |                   |
|  |  - /api/*           -> backend-service   |                   |
|  |                                         |                   |
|  +-------+-------------+-------------------+                   |
|          |             |                                        |
|          ▼             ▼                                        |
|     +---------+   +---------+                                  |
|     |api-svc  |   |web-svc  |                                  |
|     |ClusterIP|   |ClusterIP|                                  |
|     +----+----+   +----+----+                                  |
|          |             |                                        |
|          ▼             ▼                                        |
|     +---------+   +---------+                                  |
|     |API Pods |   |Web Pods |                                  |
|     +---------+   +---------+                                  |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Installera Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml
# Installerar NGINX Ingress Controller
# Detta är den vanligaste controllern
# Skapar en LoadBalancer service automatiskt
# Kan ta några minuter att bli redo

kubectl get pods -n ingress-nginx
# Verifierar att controller-podden körs
# ingress-nginx-controller ska vara Running
# Om Pending - kolla events med describe
# Controllern måste köra innan Ingress fungerar

kubectl get svc -n ingress-nginx
# Visar Ingress controllerns service
# EXTERNAL-IP är adressen du använder
# Alla Ingress-regler dirigeras via denna IP
# DNS ska peka hit för dina domäner
```

---

## Skapa Ingress-regler

```yaml
# ingress-basic.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: www.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
```

```bash
kubectl apply -f ingress-basic.yaml
# Skapar Ingress-regel
# host matchar domännamnet
# path matchar URL-sökvägen
# backend pekar på rätt Service
# ingressClassName anger vilken controller som ska hantera

kubectl get ingress
# Listar alla Ingress-regler
# ADDRESS visar controllerns IP
# HOSTS visar vilka domäner som hanteras
# Kan ta en stund innan ADDRESS syns
```

---

## Path-baserad routing

```yaml
# ingress-paths.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /users
        pathType: Prefix
        backend:
          service:
            name: users-service
            port:
              number: 80
      - path: /products
        pathType: Prefix
        backend:
          service:
            name: products-service
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: default-service
            port:
              number: 80
```

```bash
kubectl apply -f ingress-paths.yaml
# /users går till users-service
# /products går till products-service
# / (allt annat) går till default-service
# Ordning spelar roll - mer specifika paths först

curl http://api.example.com/users/123
# Request routas till users-service
# Path /users matchar första regeln
# /123 skickas vidare till backend
# Service hanterar resten av URL:en
```

---

## Host-baserad routing

```yaml
# ingress-hosts.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-host-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
  - host: admin.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-service
            port:
              number: 80
```

```bash
kubectl apply -f ingress-hosts.yaml
# Olika domäner till olika services
# app.example.com -> app-service
# admin.example.com -> admin-service
# Samma IP, olika services baserat på hostname
# Kräver DNS-konfiguration för båda domänerna
```

---

## TLS/SSL med Ingress

```bash
kubectl create secret tls example-tls --cert=fullchain.pem --key=privkey.pem
# Skapar TLS secret från certifikat
# fullchain.pem = certifikatkedja
# privkey.pem = privat nyckel
# Secreten används av Ingress för HTTPS
```

```yaml
# ingress-tls.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: secure-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - secure.example.com
    secretName: example-tls
  rules:
  - host: secure.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: secure-service
            port:
              number: 80
```

```bash
kubectl apply -f ingress-tls.yaml
# TLS termineras vid Ingress controller
# ssl-redirect tvingar HTTP -> HTTPS
# Backend-kommunikation är oftast HTTP
# Certifikatet måste matcha hostname
```

---

## Cert-Manager för automatiska certifikat

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml
# Installerar cert-manager
# Automatiserar Let's Encrypt certifikat
# Förnyar certifikat automatiskt
# Industri-standard för Kubernetes TLS
```

```yaml
# ingress-certmanager.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: auto-tls-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - auto.example.com
    secretName: auto-tls-secret
  rules:
  - host: auto.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: auto-service
            port:
              number: 80
```

```bash
kubectl apply -f ingress-certmanager.yaml
# cert-manager skapar TLS secret automatiskt
# Let's Encrypt certifikat hämtas
# Förnyas 30 dagar innan utgång
# Kräver att ClusterIssuer är konfigurerad först
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Ingress Controller        | Maste installeras separat (nginx, traefik)          |
| Host-baserad routing      | Olika domaner till olika services                   |
| Path-baserad routing      | Olika URL-paths till olika services                 |
| TLS                       | Termineras vid Ingress, certifikat i Secrets        |
| cert-manager              | Automatiserar Let's Encrypt certifikat              |

------------------------------------------------------------------

## Kom ihag

- Ingress kravs separat installation - ar bara en spec
- ingressClassName: nginx ar obligatoriskt (default borttaget)
- pathType: Prefix eller Exact - viktigt for matching
- TLS secret maste finnas FORE Ingress skapas
- cert-manager + Let's Encrypt = gratiscertifikat
""",
        },
        {
            "title": "Persistent Volumes & Storage",
            "slug": "persistent-volumes-storage",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Persistent Volumes & Storage

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | Utan PV                         | Med PV                          |
|---------------------------|--------------------------------|--------------------------------|
| Databas pod dor           | All data forlorad              | Data bevarad                   |
| Pod flyttar till ny node  | Data finns pa gammal node      | Volume foljer med              |
| Backup                    | Manuellt fran container        | Snapshot av volume             |
| Scaling                   | Stateless endast               | Stateful apps mojliga          |

Persistent Volumes ar OBLIGATORISKT for produktionsdatabaser.

------------------------------------------------------------------

## Storage Arkitektur

```
+-----------------------------------------------------------------+
|                    KUBERNETES STORAGE                           |
+-----------------------------------------------------------------+
|                                                                 |
|  POD                              STORAGE BACKEND               |
|  ---                              ---------------               |
|  +-----------------+                                           |
|  |   Container     |              +-----------------+          |
|  |   +---------+   |              |  AWS EBS        |          |
|  |   | /data   |◄--+--------------+  GCP PD         |          |
|  |   +---------+   |              |  Azure Disk     |          |
|  +-----------------+              |  NFS            |          |
|          ▲                        |  Local          |          |
|          |                        +-----------------+          |
|          |                                 ▲                    |
|  +-------+-------+                        |                    |
|  |      PVC      |                        |                    |
|  | "10Gi RWO"    |------------------------+                    |
|  +---------------+                                              |
|          ▲                                                      |
|          |                                                      |
|  +-------+-------+     +-----------------+                     |
|  |      PV       |     |  StorageClass   |                     |
|  | "aws-ebs-10"  |◄----|  "gp2"          |                     |
|  +---------------+     |  provisioner:   |                     |
|                        |  aws-ebs        |                     |
|                        +-----------------+                     |
|                                                                 |
|  PVC = Vad du behover   PV = Specifik disk                     |
|  StorageClass = Hur det skapas automatiskt                      |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## PersistentVolume (PV) - Tillganglig lagring

```yaml
# pv-local.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-storage
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  hostPath:
    path: /data/local-storage
```

```bash
kubectl apply -f pv-local.yaml
# Skapar en PersistentVolume
# capacity definierar storlek
# accessModes - hur den kan monteras
# hostPath är för lokala tester (inte för produktion!)
# I produktion använder du cloud storage

kubectl get pv
# Listar alla PersistentVolumes
# STATUS visar om den är Available, Bound, Released
# CLAIM visar vilken PVC som använder den
# RECLAIM POLICY bestämmer vad som händer vid borttagning
```

---

## PersistentVolumeClaim (PVC) - Beställning av lagring

```yaml
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: database-storage
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

```bash
kubectl apply -f pvc.yaml
# Skapar en PVC - en "beställning" av lagring
# Kubernetes matchar med en passande PV
# Eller skapar en dynamiskt (om StorageClass stödjer det)
# PVC:n blir Bound när matchning hittas

kubectl get pvc
# Visar alla PersistentVolumeClaims
# STATUS ska vara Bound för fungerande lagring
# VOLUME visar vilken PV som matchades
# CAPACITY kan skilja sig från requests (minimum matchar)

kubectl describe pvc database-storage
# Detaljerad info om PVC:n
# Events visar provisioning-processen
# Om Pending - kolla att det finns matchande PV
# Eller att StorageClass kan provisionera dynamiskt
```

---

## Använda PVC i Pods

```yaml
# pod-with-pvc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: database-pod
spec:
  containers:
  - name: postgres
    image: postgres:15
    env:
    - name: POSTGRES_PASSWORD
      value: "secretpassword"
    volumeMounts:
    - name: db-storage
      mountPath: /var/lib/postgresql/data
  volumes:
  - name: db-storage
    persistentVolumeClaim:
      claimName: database-storage
```

```bash
kubectl apply -f pod-with-pvc.yaml
# Monterar PVC:n i containern
# Data i /var/lib/postgresql/data är nu persistent
# Podden kan dö och starta om - data finns kvar
# Samma PVC kan återanvändas av nya pods

kubectl exec database-pod -- ls -la /var/lib/postgresql/data
# Verifierar att data finns
# PostgreSQL skapar sina filer här
# Filerna sparas på PV:n, inte i containern
# Om containern dör, finns filerna kvar på disken
```

---

## StorageClasses - Dynamisk provisioning

```bash
kubectl get storageclass
# Visar tillgängliga StorageClasses
# DEFAULT anger vilken som används om ingen anges
# PROVISIONER visar vem som skapar volymer
# Cloud providers har fördefinierade classes

kubectl describe storageclass standard
# Visar detaljer om StorageClass
# Provisioner - t.ex. kubernetes.io/gce-pd, ebs.csi.aws.com
# Parameters - specifika inställningar för providern
# reclaimPolicy - vad händer med data vid borttagning
```

```yaml
# storageclass-ssd.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
reclaimPolicy: Delete
allowVolumeExpansion: true
```

```bash
kubectl apply -f storageclass-ssd.yaml
# Skapar en StorageClass för SSD-diskar
# Pods som behöver snabb disk kan begära "fast-ssd"
# Volymer skapas automatiskt när PVC:er begär dem
# allowVolumeExpansion = kan utöka storlek senare
```

---

## Access Modes

```bash
# ReadWriteOnce (RWO)
# Kan monteras av EN pod för läsning och skrivning
# Vanligast för databaser
# En pod äger volymen exklusivt

# ReadOnlyMany (ROX)
# Kan monteras av MÅNGA pods för endast läsning
# Bra för statiskt innehåll som delas
# Alla pods läser samma data, ingen kan skriva

# ReadWriteMany (RWX)
# Kan monteras av MÅNGA pods för läsning och skrivning
# Kräver nätverksfilsystem (NFS, CephFS, etc.)
# Inte alla provisioners stödjer detta
```

---

## Utoka lagring

```bash
kubectl patch pvc database-storage -p '{"spec":{"resources":{"requests":{"storage":"10Gi"}}}}'
# Utokar PVC fran 5Gi till 10Gi
# Kraver att StorageClass har allowVolumeExpansion: true
# Volymen vaxer utan att data forloras
# Kan ta tid beroende pa cloud provider

kubectl get pvc database-storage -w
# Foljer expansionsprocessen
# Status andras under tiden
# FileSystemResizePending -> normalt
# Nar klart: ny capacity visas
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| PV                        | Faktisk lagring (admin eller dynamiskt)             |
| PVC                       | Bestallning av lagring (utvecklare)                 |
| StorageClass              | Mall for dynamisk provisioning                      |
| Access Modes              | RWO (en pod), ROX/RWX (manga pods)                  |
| Reclaim Policy            | Retain (spara), Delete (ta bort vid PVC-borttagning)|

------------------------------------------------------------------

## Kom ihag

- PVC binder till PV automatiskt baserat pa storlek och accessMode
- StorageClass med provisioner = dynamisk volym-skapande
- hostPath ar BARA for test - anvand cloud storage i prod
- Retain policy bevarar data aven nar PVC tas bort
- Expansion kraver allowVolumeExpansion: true
""",
        },
        {
            "title": "StatefulSets for Stateful Applications",
            "slug": "statefulsets-stateful-applications",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# StatefulSets for Stateful Applications

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Deployment                | StatefulSet                                         |
|---------------------------|-----------------------------------------------------|
| web-app-abc123            | mysql-0, mysql-1, mysql-2                           |
| Slumpmasiga namn          | Ordnade, forutsagbara namn                          |
| Delad eller ingen PV      | Varje pod far egen PersistentVolume                 |
| Parallell startup         | Sekventiell startup (0 fore 1 fore 2)               |

StatefulSets ar OBLIGATORISKT for databaser och klustrade system.

------------------------------------------------------------------

## StatefulSet Arkitektur

```
+-----------------------------------------------------------------+
|                    STATEFULSET PATTERN                          |
+-----------------------------------------------------------------+
|                                                                 |
|  HEADLESS SERVICE: mysql-headless                               |
|  --------------------------------                               |
|  DNS: mysql-0.mysql-headless.default.svc.cluster.local          |
|       mysql-1.mysql-headless.default.svc.cluster.local          |
|       mysql-2.mysql-headless.default.svc.cluster.local          |
|                                                                 |
|  +-------------+  +-------------+  +-------------+             |
|  |  mysql-0    |  |  mysql-1    |  |  mysql-2    |             |
|  |  (master)   |  |  (replica)  |  |  (replica)  |             |
|  +------+------+  +------+------+  +------+------+             |
|         |                |                |                     |
|         ▼                ▼                ▼                     |
|  +-------------+  +-------------+  +-------------+             |
|  |  PVC: data- |  |  PVC: data- |  |  PVC: data- |             |
|  |  mysql-0    |  |  mysql-1    |  |  mysql-2    |             |
|  +-------------+  +-------------+  +-------------+             |
|                                                                 |
|  Startup order: mysql-0 -> mysql-1 -> mysql-2                     |
|  Shutdown order: mysql-2 -> mysql-1 -> mysql-0                    |
|  Varje pod behaller sin PVC aven vid omstart                    |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## StatefulSet vs Deployment

```bash
# Deployment pods:
# web-app-7d9c8b7f6-abc12
# web-app-7d9c8b7f6-def34
# web-app-7d9c8b7f6-ghi56
# Slumpmasiga namn, ingen ordning, utbytbara

# StatefulSet pods:
# mysql-0
# mysql-1
# mysql-2
# Ordnade namn, forutsagbara, persistenta
```

------------------------------------------------------------------

## Skapa en StatefulSet

```yaml
# statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql-headless
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        ports:
        - containerPort: 3306
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "rootpassword"
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

```bash
kubectl apply -f statefulset.yaml
# Skapar StatefulSet med 3 replicas
# serviceName måste matcha en headless service
# volumeClaimTemplates skapar PVC per pod
# mysql-0, mysql-1, mysql-2 skapas i ordning

kubectl get statefulset mysql
# Visar StatefulSet status
# READY visar antal redo pods
# Pods skapas en i taget, inte parallellt
# Nästa pod startar först när föregående är Ready
```

---

## Headless Service för StatefulSets

```yaml
# headless-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql-headless
spec:
  clusterIP: None
  selector:
    app: mysql
  ports:
  - port: 3306
```

```bash
kubectl apply -f headless-service.yaml
# clusterIP: None gör den headless
# Ingen load balancing - direkt DNS till pods
# Varje pod får sitt eget DNS-namn
# Kritiskt för StatefulSets!

nslookup mysql-0.mysql-headless.default.svc.cluster.local
# DNS-namn för specifik pod
# mysql-0 = pod-namn
# mysql-headless = service-namn
# Returnerar pod-IP direkt, inte service-IP
```

---

## Ordnad scaling

```bash
kubectl scale statefulset mysql --replicas=5
# Skalar upp till 5 replicas
# mysql-3 skapas först, sedan mysql-4
# Varje pod måste vara Ready innan nästa startar
# Ordning garanteras alltid

kubectl scale statefulset mysql --replicas=2
# Skalar ner till 2 replicas
# mysql-4 tas bort först, sedan mysql-3
# Nedskalaningen sker i omvänd ordning
# Data i PVC:er finns kvar (beroende på policy)
```

---

## PVC per pod

```bash
kubectl get pvc
# Varje pod har sin egen PVC
# data-mysql-0, data-mysql-1, data-mysql-2
# Namnkonvention: {volumeClaimTemplate-name}-{pod-name}
# PVC:er finns kvar även om pod/StatefulSet tas bort

kubectl get pv
# Motsvarande PV för varje PVC
# Varje pod har sin egen isolerade lagring
# mysql-0:s data blandas aldrig med mysql-1:s
# Perfekt för databaser som behöver lokal disk
```

---

## Pod management policies

```yaml
# statefulset-parallel.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: cache
spec:
  podManagementPolicy: Parallel
  replicas: 5
  # ... rest of spec
```

```bash
# OrderedReady (default)
# Pods startas/stoppas en i taget
# Väntar på Ready innan nästa
# Bra för databaser med master-slave

# Parallel
# Alla pods startas/stoppas samtidigt
# Snabbare men ingen ordningsgaranti
# Bra för caches eller appar utan inbördes dependencies
```

---

## Uppdatera StatefulSets

```bash
kubectl rollout status statefulset mysql
# Följer en pågående uppdatering
# Pods uppdateras en i taget, i omvänd ordning
# mysql-2 först, sedan mysql-1, sedan mysql-0
# Säkert för master-slave setups (master uppdateras sist)

kubectl rollout undo statefulset mysql
# Rullar tillbaka till föregående version
# Samma ordnade process som vid uppdatering
# Data i PVC:er påverkas inte
# Endast container image/config ändras
```

---

## Partition för canary deploys

```yaml
# statefulset-partition.yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 2
```

```bash
kubectl patch statefulset mysql -p '{"spec":{"updateStrategy":{"rollingUpdate":{"partition":2}}}}'
# Endast pods med index >= 2 uppdateras
# mysql-2 får nya imagen
# mysql-0, mysql-1 behåller gamla
# Perfekt för att testa på en pod först

kubectl patch statefulset mysql -p '{"spec":{"updateStrategy":{"rollingUpdate":{"partition":0}}}}'
# Sätter partition till 0
# Nu uppdateras alla pods
# Gradvis utrullning av bevisad ändring
# Säker canary-deploy för stateful apps
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| StatefulSets              | For databaser och klustrade system                  |
| Ordnade namn              | pod-0, pod-1, pod-2 (forutsagbara och stabila)      |
| Headless Service          | Direkt DNS till varje pod                           |
| volumeClaimTemplates      | Automatisk PVC per pod                              |
| Update order              | Sista forst, sakert for master-slave                |

------------------------------------------------------------------

## Kom ihag

- StatefulSet KRAVER headless service (clusterIP: None)
- PVCs tas INTE bort automatiskt vid delete
- Partition ar kraftfullt for canary deploys
- Orderedready = en i taget, Parallel = alla samtidigt
- mysql-0 ar ofta master, mysql-1+ ar replicas
""",
        },
        {
            "title": "DaemonSets & Node-level Operations",
            "slug": "daemonsets-node-level-operations",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 75,
            "content": """# DaemonSets & Node-level Operations

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Anvandning                | Exempel                                             |
|---------------------------|-----------------------------------------------------|
| Log collection            | Fluentd, Filebeat pa varje node                     |
| Monitoring                | Node exporter, cAdvisor                             |
| Network                   | Calico, Cilium CNI plugins                          |
| Storage                   | CSI drivers for cloud storage                       |

DaemonSets garanterar EN pod per node - perfekt for infra-komponenter.

------------------------------------------------------------------

## DaemonSet vs Deployment

```
+-----------------------------------------------------------------+
|                    DAEMONSET PATTERN                            |
+-----------------------------------------------------------------+
|                                                                 |
|  DEPLOYMENT (replicas: 3)     DAEMONSET                         |
|  ------------------------     ---------                         |
|                                                                 |
|  Node 1: [pod] [pod]          Node 1: [pod]                     |
|  Node 2: [pod]                Node 2: [pod]                     |
|  Node 3: (inga pods)          Node 3: [pod]                     |
|                                                                 |
|  Scheduler valjer noder       EN pod per node (garanterat)      |
|  Kan vara ojamnt fordelat     Alltid en, aldrig fler            |
|                                                                 |
|  NY NODE LAGGS TILL:                                            |
|  Deployment: kanske far pod   DaemonSet: far ALLTID pod         |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Skapa en DaemonSet

DaemonSets är som **vakter** i ett bostadsområde. Varje hus (node) får exakt en vakt (pod). När ett nytt hus byggs får det automatiskt en vakt. Om en vakt slutar ersätts den automatiskt.

---

## Skapa en DaemonSet

```yaml
# daemonset.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  labels:
    app: fluentd
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
        image: fluent/fluentd:v1.16
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: containers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: containers
        hostPath:
          path: /var/lib/docker/containers
```

```bash
kubectl apply -f daemonset.yaml
# Skapar en pod på varje node
# hostPath monterar nodens filsystem i containern
# Fluentd kan nu läsa loggar från alla containers
# Pods skapas automatiskt även på nya noder

kubectl get daemonset fluentd
# DESIRED visar antal noder
# CURRENT visar hur många pods som skapats
# READY visar hur många som är redo
# NODE SELECTOR visas om det finns begränsningar
```

---

## Kontrollera DaemonSet-deployment

```bash
kubectl get pods -l app=fluentd -o wide
# Visar alla DaemonSet-pods med node-info
# -o wide inkluderar NODE-kolumnen
# Du ser en pod per node
# Om en node saknar pod - kolla toleration/selector

kubectl rollout status daemonset fluentd
# Följer uppdateringsstatus
# Visar hur många noder som uppdaterats
# Vänta tills alla är klara
# Samma kommando som för Deployments
```

---

## Begränsa till vissa noder

```yaml
# daemonset-selector.yaml
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
      nodeSelector:
        hardware: gpu
      containers:
      - name: gpu-monitor
        image: nvidia/gpu-monitor:latest
```

```bash
kubectl label node worker-1 hardware=gpu
# Lägger till label på noden
# Endast noder med denna label får DaemonSet-podden
# worker-1 får nu en gpu-monitor pod
# Andra noder utan labeln påverkas inte

kubectl get pods -l app=gpu-monitor -o wide
# Verifierar att pod endast körs på GPU-noder
# NODE-kolumnen ska visa endast labelade noder
# Om ingen pod finns - inga noder matchar selector
# Lägg till labels eller ändra nodeSelector
```

---

## Tolerations för system-pods

```yaml
# daemonset-tolerations.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      - key: node.kubernetes.io/not-ready
        operator: Exists
        effect: NoExecute
      containers:
      - name: exporter
        image: prom/node-exporter:latest
```

```bash
kubectl apply -f daemonset-tolerations.yaml
# tolerations tillåter pods på taintade noder
# control-plane toleration = kör på master-noder
# not-ready toleration = fortsätt köra även vid nodproblem
# Viktigt för monitoring och logging DaemonSets

kubectl get pods -l app=node-exporter -o wide
# Ska visa pods på ALLA noder, inklusive control-plane
# Utan tolerations skulle control-plane noder uteslutas
# Monitoring behöver data från alla noder
# Därför behövs rätt tolerations
```

---

## Uppdateringsstrategier

```yaml
# daemonset-update.yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
```

```bash
# RollingUpdate (default)
# Uppdaterar en node i taget
# maxUnavailable styr hur många samtidigt
# Säkert men kan ta tid i stora kluster

# OnDelete
# Pods uppdateras endast när de manuellt tas bort
# Mer kontroll men kräver manuell hantering
# Bra för kritiska system-pods
```

```bash
kubectl rollout restart daemonset fluentd
# Tvingar omstart av alla pods
# Ny pod skapas på varje node
# Använd för att ladda om konfiguration
# Eller för att tvinga pull av ny image

kubectl rollout history daemonset fluentd
# Visar uppdateringshistorik
# REVISION visar versionsnummer
# Kan rulla tillbaka med rollout undo
# Samma workflow som Deployments
```

------------------------------------------------------------------

## Vanliga DaemonSet-anvandningsfall

```bash
# Logging
# Fluentd, Filebeat - samlar loggar fran alla containers

# Monitoring
# Node Exporter, cAdvisor - samlar metrics fran noder

# Networking
# kube-proxy, Calico, Cilium - natverksfunktionalitet

# Storage
# CSI drivers - tillater pods att anvanda molnlagring

kubectl get daemonsets -n kube-system
# Visar system-DaemonSets
# kube-proxy kor pa alla noder for networking
# Andra addons kan finnas beroende pa klustret
# Ror aldrig dessa utan att veta vad du gor!
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| DaemonSet                 | En pod per node, automatiskt                        |
| Nya noder                 | Far DaemonSet pods automatiskt                      |
| nodeSelector              | Begransar till specifika noder                      |
| tolerations               | Tillater korning pa taintade noder                  |
| Vanliga fall              | Logging, monitoring, networking, storage            |

------------------------------------------------------------------

## Kom ihag

- DaemonSet ar for infra-komponenter, inte apps
- hostPath volumes ar vanliga for att lasa nodens filer
- Tolerations kravs for att kora pa control-plane noder
- updateStrategy styr hur uppdateringar rullas ut
- DESIRED/CURRENT/READY visar DaemonSet-halsa
""",
        },
        {
            "title": "Jobs & CronJobs",
            "slug": "jobs-cronjobs",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Jobs & CronJobs

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario                  | Resurs                                              |
|---------------------------|-----------------------------------------------------|
| Database backup           | CronJob (nattlig)                                   |
| Data migration            | Job (engangskrning)                                |
| Log rotation              | CronJob (varje timme)                               |
| Batch processing          | Job med parallelism                                 |

Jobs/CronJobs ar for BATCH-processer, inte langtkorande tjanster.

------------------------------------------------------------------

## Job vs CronJob

```
+-----------------------------------------------------------------+
|                    JOBS VS CRONJOBS                             |
+-----------------------------------------------------------------+
|                                                                 |
|  JOB                              CRONJOB                       |
|  ---                              -------                       |
|  Kor ENGNG                       Kor pa SCHEMA                  |
|  Manuellt triggas                 Automatiskt triggas           |
|  Ex: migration                    Ex: backup varje natt         |
|                                                                 |
|  JOB LIVSCYKEL:                                                 |
|  +------+    +---------+    +-----------+                      |
|  |Create|---►| Running |---►| Completed |                      |
|  +------+    +---------+    +-----------+                      |
|                  |                                              |
|                  ▼ (vid fel)                                    |
|             +---------+                                         |
|             |  Retry  | (backoffLimit ganger)                   |
|             +---------+                                         |
|                                                                 |
|  CRONJOB SKAPAR JOBS:                                           |
|  CronJob --► Job 1 (00:00)                                      |
|          --► Job 2 (01:00)                                      |
|          --► Job 3 (02:00)                                      |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Skapa ett Job

```yaml
# job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-job
spec:
  template:
    spec:
      containers:
      - name: backup
        image: postgres:15
        command: ["pg_dump", "-h", "postgres-service", "-U", "admin", "-d", "mydb", "-f", "/backup/dump.sql"]
        volumeMounts:
        - name: backup-storage
          mountPath: /backup
      restartPolicy: Never
      volumes:
      - name: backup-storage
        persistentVolumeClaim:
          claimName: backup-pvc
```

```bash
kubectl apply -f job.yaml
# Skapar och startar jobbet
# restartPolicy: Never - skapa ny pod vid fel, restarta inte
# restartPolicy: OnFailure - restarta samma pod vid fel
# Job avslutas när containern returnerar exit code 0

kubectl get jobs
# Listar alla Jobs
# COMPLETIONS visar framgångsrika / totalt
# DURATION visar hur länge jobbet tog
# AGE visar när det skapades

kubectl get pods -l job-name=backup-job
# Visar pods skapade av jobbet
# STATUS Completed = framgångsrikt
# STATUS Error = misslyckades
# Pods finns kvar för loggläsning
```

---

## Hantera Job-resultat

```bash
kubectl logs job/backup-job
# Visar loggar från job-podden
# Fungerar även efter att jobbet avslutats
# Viktig för debugging och verifiering
# Samma output som kubectl logs <pod-name>

kubectl describe job backup-job
# Visar jobdetaljer
# Events visar försök och resultat
# Conditions visar Complete eller Failed
# Pods Created/Succeeded visar statistik

kubectl delete job backup-job
# Tar bort jobbet och dess pods
# Data i volymer finns kvar
# Historik försvinner
# Gör efter att du verifierat resultatet
```

---

## Retry och parallellism

```yaml
# job-parallel.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: process-data
spec:
  completions: 10
  parallelism: 3
  backoffLimit: 4
  template:
    spec:
      containers:
      - name: processor
        image: dataprocessor:latest
      restartPolicy: Never
```

```bash
kubectl apply -f job-parallel.yaml
# completions: 10 - 10 framgångsrika körningar behövs
# parallelism: 3 - max 3 pods samtidigt
# backoffLimit: 4 - max 4 misslyckanden innan ge upp
# Bra för databehandling som kan parallelliseras

kubectl get job process-data -w
# Följer progress i realtid
# COMPLETIONS ökar när pods lyckas
# Nya pods startar när gamla avslutas
# Jobbet är klart vid 10/10 completions
```

---

## TTL för automatisk cleanup

```yaml
# job-ttl.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: temporary-job
spec:
  ttlSecondsAfterFinished: 3600
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["echo", "Done!"]
      restartPolicy: Never
```

```bash
kubectl apply -f job-ttl.yaml
# ttlSecondsAfterFinished: 3600 = ta bort efter 1 timme
# Räknas från när jobbet blev Complete/Failed
# Förhindrar ackumulering av gamla jobs
# Kräver TTLAfterFinished feature gate (på i nyare K8s)
```

---

## CronJobs - Schemalagda jobs

```yaml
# cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nightly-backup
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: postgres:15
            command: ["pg_dump", "-h", "postgres", "-U", "admin", "-d", "mydb"]
          restartPolicy: Never
```

```bash
kubectl apply -f cronjob.yaml
# schedule följer cron-syntax
# "0 2 * * *" = kl 02:00 varje dag
# CronJob skapar Job vid varje körning
# Varje Job skapar en eller flera pods

kubectl get cronjobs
# Listar alla CronJobs
# SCHEDULE visar cron-uttrycket
# SUSPEND visar om det är pausat
# ACTIVE visar pågående jobs
# LAST SCHEDULE visar senaste körning
```

---

## CronJob-konfiguration

```yaml
# cronjob-advanced.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hourly-cleanup
spec:
  schedule: "0 * * * *"
  concurrencyPolicy: Forbid
  startingDeadlineSeconds: 300
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: cleanup
            image: cleanup:latest
          restartPolicy: Never
```

```bash
# concurrencyPolicy:
# Allow - nya jobs startar aven om tidigare kor (default)
# Forbid - hoppa over om foregaende fortfarande kor
# Replace - ta bort foregaende och starta nytt

# startingDeadlineSeconds:
# Max tid efter scheduled time att starta jobbet
# Om missad window - hoppa over den korningen

# History limits:
# Hur manga gamla jobs att behalla
# Bra for debugging men rensa automatiskt
```

------------------------------------------------------------------

## Hantera CronJobs

```bash
kubectl create job manual-backup --from=cronjob/nightly-backup
# Skapar ett manuellt job fran CronJob-mallen
# Anvandbart for att testa eller kora omedelbart
# Jobbet har samma spec som CronJobs vanliga jobs
# Namnet blir "manual-backup"

kubectl patch cronjob nightly-backup -p '{"spec":{"suspend":true}}'
# Pausar CronJob
# Inga nya jobs schemalagges
# Pagaende jobs fortsatter
# Bra vid underhall eller felsokning

kubectl get jobs --sort-by=.metadata.creationTimestamp
# Listar jobs sorterat efter tid
# Senaste langst ner
# Hjalper att folja CronJob-historik
# Kombinera med grep for specifik CronJob
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Job                       | Kor till slutforande, sedan klart                   |
| restartPolicy             | Never (ny pod) eller OnFailure (restarta)           |
| parallelism               | Flera pods samtidigt for snabbare batch             |
| CronJob                   | Schemalagda jobs med cron-syntax                    |
| concurrencyPolicy         | Hantera overlappande korningar                      |

------------------------------------------------------------------

## Kom ihag

- Cron syntax: minut timme dag manad veckodag
- backoffLimit styr antal retries fore fail
- ttlSecondsAfterFinished rensar gamla pods automatiskt
- successfulJobsHistoryLimit och failedJobsHistoryLimit for CronJobs
- kubectl create job --from=cronjob for manuell korning
""",
        },
        {
            "title": "Resource Management & Limits",
            "slug": "resource-management-limits",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Resource Management & Limits

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Utan resursgranser             | Med resursgranser                                |
|--------------------------------|--------------------------------------------------|
| En app tar all CPU             | Garanterade resurser per pod                     |
| OOM kills overallt             | Predictable memory usage                         |
| Oforutsagbar prestanda         | Stabil performance                               |
| Ineffektiv packning            | Optimal node utilization                         |

Resource management ar KRITISKT for stabil produktion.

------------------------------------------------------------------

## Requests vs Limits

```
+-----------------------------------------------------------------+
|                    REQUESTS VS LIMITS                           |
+-----------------------------------------------------------------+
|                                                                 |
|  REQUESTS                         LIMITS                        |
|  --------                         ------                        |
|  "Vad jag BEHOVER"                "Max jag FAR anvanda"         |
|  Garanteras av scheduler          Hard cap                      |
|  Anvands for placement            CPU throttlas, Memory OOMKill |
|                                                                 |
|  EXEMPEL:                                                       |
|  +---------------------------------------------------------+   |
|  |  Pod: app                                                |   |
|  |  requests:           limits:                             |   |
|  |    cpu: 100m           cpu: 500m                         |   |
|  |    memory: 128Mi       memory: 256Mi                     |   |
|  +---------------------------------------------------------+   |
|                                                                 |
|  BETEENDE:                                                      |
|  - Pod far minst 100m CPU och 128Mi memory                     |
|  - Pod kan anvanda upp till 500m CPU (throttlas darofter)      |
|  - Pod som tar >256Mi memory = OOMKilled                       |
|                                                                 |
|  QoS CLASSES:                                                   |
|  Guaranteed: requests = limits (hogst prioritet)                |
|  Burstable:  requests < limits                                  |
|  BestEffort: inga requests/limits (lagst prioritet)            |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Requests vs Limits YAML

```yaml
# pod-resources.yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-demo
spec:
  containers:
  - name: app
    image: nginx:latest
    resources:
      requests:
        memory: "128Mi"
        cpu: "100m"
      limits:
        memory: "256Mi"
        cpu: "500m"
```

```bash
kubectl apply -f pod-resources.yaml
# requests = garanterade resurser vid scheduling
# limits = absolut max som containern får använda
# Schemaläggaren använder requests för placering
# Runtime använder limits för begränsning

kubectl describe pod resource-demo | grep -A 5 "Requests"
# Visar requests och limits
# CPU visas i millicores (m)
# Memory visas i Mi eller Gi
# Verifiera att värdena är som förväntat
```

---

## CPU-beteende

```bash
# CPU är komprimerbar
# Om containern försöker använda mer än limit
# Blir den throttlad (saktar ner), crashar INTE

kubectl top pod resource-demo
# Visar aktuell CPU och minnesanvändning
# Kräver att metrics-server är installerat
# CPU visar millicores (t.ex. 50m = 5% av en kärna)
# Hjälper att räkna ut rätt requests/limits

kubectl describe node <node-name> | grep -A 10 "Allocated resources"
# Visar total resursallokering på noden
# CPU Requests vs Limits
# Memory Requests vs Limits
# Hjälper förstå nodens kapacitet
```

---

## Memory-beteende

```bash
# Memory är INTE komprimerbar
# Om containern försöker använda mer än limit
# Blir den OOMKilled (dödad)

kubectl get pods | grep OOMKilled
# Visar pods som dött av minnesbrist
# OOM = Out Of Memory
# Containern överskred sin memory limit
# Öka limit eller optimera appen

kubectl describe pod <pod-name> | grep -A 2 "Last State"
# Visar senaste tillstånd
# Reason: OOMKilled bekräftar minnesproblem
# Exit Code: 137 är OOM-specifik
# Containers som OOMKillas startas om (restartPolicy)
```

---

## Quality of Service (QoS)

```bash
# Guaranteed
# requests == limits för CPU och Memory
# Högsta prioritet, sist att evictas
# Bäst för kritiska produktionsappar

# Burstable
# requests < limits
# Kan använda mer om tillgängligt
# Evictas före BestEffort, efter Guaranteed

# BestEffort
# Inga requests eller limits satta
# Lägsta prioritet, först att evictas
# Undvik i produktion!

kubectl describe pod resource-demo | grep "QoS Class"
# Visar poddens QoS-klass
# Kubernetes beräknar automatiskt
# Baserat på resource specs
```

---

## LimitRange för namespaces

```yaml
# limitrange.yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: resource-constraints
  namespace: production
spec:
  limits:
  - default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "100m"
      memory: "128Mi"
    max:
      cpu: "2"
      memory: "4Gi"
    min:
      cpu: "50m"
      memory: "64Mi"
    type: Container
```

```bash
kubectl apply -f limitrange.yaml
# default = om ingen limit sätts, använd denna
# defaultRequest = om ingen request sätts
# max/min = tillåtna gränser
# Pods som överskrider max/min avvisas

kubectl describe limitrange resource-constraints -n production
# Visar alla konfigurerade gränser
# Hjälper förstå vad som tillåts
# Valideras vid pod-skapande
# Ger konsekventa resursgränser
```

---

## ResourceQuota för namespaces

```yaml
# resourcequota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: team-a
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
    pods: "50"
```

```bash
kubectl apply -f resourcequota.yaml
# Begränsar total resursanvändning i namespace
# requests.cpu: 10 = max 10 CPU-kärnor totalt
# pods: 50 = max 50 pods i namespace
# Förhindrar att ett team tar alla resurser

kubectl describe resourcequota compute-quota -n team-a
# Used vs Hard visar förbrukning
# Om Used når Hard kan inga fler resurser skapas
# Tvingar teams att vara resursmässigt ansvarsfulla
# Quota måste finnas för alla resurser som begränsas
```

---

## Vertical Pod Autoscaler (VPA)

```yaml
# vpa.yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: nginx-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: nginx
  updatePolicy:
    updateMode: "Auto"
```

```bash
kubectl apply -f vpa.yaml
# VPA justerar requests/limits automatiskt
# Analyserar faktisk resursanvändning
# updateMode: Auto - restarta pods med nya värden
# updateMode: Off - bara rekommendationer

kubectl describe vpa nginx-vpa
# Visar VPA-rekommendationer
# Lower Bound, Target, Upper Bound
# Uncapped Target = utan limits
# Hjälper att hitta rätt storlek
```

---

## Best Practices

```bash
# Borja med requests = limits (Guaranteed QoS)
# Overvaka faktisk anvandning med metrics
# Justera baserat pa observerad anvandning
# Satt alltid requests - annars BestEffort!

# CPU: borja lagt och oka vid throttling
# Memory: borja med vad appen behover + marginal
# OBS: Memory leak = limits hjalper, loser inte problemet

kubectl top pods --sort-by=memory
# Sorterar pods efter minnesanvandning
# Hitta de mest resurshungriga
# Hjalper identifiera optimeringsmojligheter
# Kor regelbundet for kapacitetsplanering
```

------------------------------------------------------------------

## Key Takeaways

| Koncept                   | Detalj                                              |
|---------------------------|-----------------------------------------------------|
| Requests                  | Garanterat minimum, anvands for scheduling          |
| Limits                    | Max tillatet, hard cap                              |
| CPU                       | Throttlas vid limit (appen blir langsam)            |
| Memory                    | OOMKill vid limit (pod dor)                         |
| QoS classes               | Guaranteed > Burstable > BestEffort                 |

------------------------------------------------------------------

## Kom ihag

- ALLTID satt requests - annars ar du BestEffort
- requests = limits ger Guaranteed QoS (hogst prioritet)
- LimitRange ger defaults, ResourceQuota ger totalkvoter
- CPU mats i millicores (1000m = 1 karna)
- Memory mats i Mi/Gi (MiB/GiB)
""",
        },
        {
            "title": "Health Checks & Probes",
            "slug": "health-checks-probes",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Health Checks & Probes

------------------------------------------------------------------

## Varfor viktigt for DevOps?

| Utan probes                    | Med probes                                       |
|--------------------------------|--------------------------------------------------|
| Trasig container kor for evigt | Automatisk omstart vid failure                   |
| Trafik till unready pods       | Intelligent routing till friska pods             |
| Cold start-fel                 | Graceful startup med startupProbe                |
| Manuell intervention           | Self-healing kluster                             |

Probes ar KRITISKA for produktions-stabilitet.

------------------------------------------------------------------

## Probe Typer

```
+-----------------------------------------------------------------+
|                    KUBERNETES PROBES                            |
+-----------------------------------------------------------------+
|                                                                 |
|  STARTUP PROBE           (kor forst)                            |
|  -------------                                                  |
|  "Har containern startat?"                                      |
|  - Vanta pa langsamma startups                                  |
|  - Disablar liveness/readiness tills klar                       |
|  - Fel -> restarta containern                                    |
|                                                                 |
|           | success                                             |
|           ▼                                                     |
|  LIVENESS PROBE          (kontinuerligt)                        |
|  --------------                                                 |
|  "Lever containern?"                                            |
|  - Detekterar deadlocks, hangs                                  |
|  - Fel -> restarta containern                                    |
|                                                                 |
|  READINESS PROBE         (kontinuerligt)                        |
|  ---------------                                                |
|  "Kan containern ta emot trafik?"                               |
|  - Temporary unavailability                                     |
|  - Fel -> ta bort fran Service endpoints                        |
|  - Restartar INTE containern                                    |
|                                                                 |
|  PROBE METODER:                                                 |
|  - httpGet:    HTTP GET request                                 |
|  - tcpSocket:  TCP connection                                   |
|  - exec:       Kor kommando i container                         |
|  - grpc:       gRPC health check                                |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Liveness Probe

```yaml
# liveness.yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-demo
spec:
  containers:
  - name: app
    image: myapp:latest
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 10
      timeoutSeconds: 5
      failureThreshold: 3
```

```bash
kubectl apply -f liveness.yaml
# httpGet anropar /health på port 8080
# initialDelaySeconds = vänta 15s innan första probe
# periodSeconds = proba var 10:e sekund
# failureThreshold = 3 misslyckanden = omstart

kubectl describe pod liveness-demo | grep -A 10 "Liveness"
# Visar liveness probe config
# Och eventuella misslyckanden
# Om container restartats syns det i Events
# Restart Count ökar vid liveness-failures
```

---

## Readiness Probe

```yaml
# readiness.yaml
apiVersion: v1
kind: Pod
metadata:
  name: readiness-demo
  labels:
    app: web
spec:
  containers:
  - name: app
    image: myapp:latest
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
      successThreshold: 1
      failureThreshold: 3
```

```bash
kubectl apply -f readiness.yaml
# Readiness avgör om pod får trafik
# Misslyckande = tas bort från Service endpoints
# Containern STARTAS INTE OM
# Bara trafiken stoppas

kubectl get endpoints web-service
# Visar vilka pods som får trafik
# Pods som failar readiness försvinner härifrån
# När de blir ready igen läggs de till
# Service load balancerar endast till ready pods
```

---

## Startup Probe

```yaml
# startup.yaml
apiVersion: v1
kind: Pod
metadata:
  name: startup-demo
spec:
  containers:
  - name: app
    image: slow-starting-app:latest
    startupProbe:
      httpGet:
        path: /health
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      periodSeconds: 10
```

```bash
kubectl apply -f startup.yaml
# startupProbe tillåter 30 * 10 = 300 sekunder för start
# Liveness/readiness probes väntar tills startup lyckas
# Perfekt för appar med lång uppstartstid
# Utan startup probe skulle liveness döda den innan den startat

kubectl describe pod startup-demo | grep -A 5 "Startup"
# Visar startup probe status
# Success/Failure visas
# Om startup failar startas containern om
# Liveness tar över efter startup lyckas
```

---

## Probe-typer

```yaml
# httpGet - HTTP request
livenessProbe:
  httpGet:
    path: /health
    port: 8080
    httpHeaders:
    - name: Authorization
      value: Bearer token123

# tcpSocket - TCP connection
livenessProbe:
  tcpSocket:
    port: 3306

# exec - kör kommando
livenessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
```

```bash
# httpGet
# Bäst för HTTP-appar
# 200-399 = success, annat = failure
# Kan inkludera headers

# tcpSocket
# Bäst för databaser, caches
# Kontrollerar bara att porten är öppen
# Snabbt och enkelt

# exec
# Flexibelt - kör valfritt kommando
# Exit code 0 = success
# Långsammare än httpGet/tcpSocket
```

---

## Kombinera probes

```yaml
# combined-probes.yaml
apiVersion: v1
kind: Pod
metadata:
  name: production-app
spec:
  containers:
  - name: app
    image: myapp:latest
    ports:
    - containerPort: 8080
    startupProbe:
      httpGet:
        path: /health
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      periodSeconds: 15
      timeoutSeconds: 5
      failureThreshold: 3
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      periodSeconds: 5
      timeoutSeconds: 3
      failureThreshold: 3
```

```bash
kubectl apply -f combined-probes.yaml
# Alla tre probes arbetar tillsammans
# Startup: vänta på att appen startat (upp till 5 min)
# Liveness: starta om vid crash/hang
# Readiness: ta bort trafik vid temporära problem

kubectl get pods -w
# Följ pod-status
# READY 0/1 = readiness failing
# READY 1/1 = redo för trafik
# Restarts ökar vid liveness-failure
```

---

## Felsökning av probes

```bash
kubectl describe pod <pod-name> | grep -A 10 "Events"
# Events visar probe-failures
# "Liveness probe failed" med HTTP status
# "Readiness probe failed" visar varför
# Starta felsökning härifrån

kubectl exec -it <pod-name> -- curl localhost:8080/health
# Testa probe-endpointen manuellt
# Verifiera att appen svarar
# Kolla response code och body
# Om det fungerar - kolla probe config

kubectl logs <pod-name> --previous
# Loggar från förra körningen
# Om liveness dödat containern
# --previous visar vad som hände innan
# Ofta nyckeln till att förstå problemet
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Liveness Probe | Lever den? Starta om vid failure |
| Readiness Probe | Redo for trafik? Ta bort fran Service vid failure |
| Startup Probe | For langsamma startups, blockerar andra probes |
| httpGet | Vanligaste probe-typen, tcpSocket for databaser |
| initialDelaySeconds | Vanta innan forsta probe, matcha appens startup-tid |

## Kom ihag

- ALLTID satt probes i produktion - utan dem ingen self-healing
- Liveness ska kolla om appen ar fundamentalt trasig
- Readiness ska kolla beroenden som databaskoppling
- Startup probe skyddar mot for tidiga liveness-checks
- failureThreshold x periodSeconds = total tolerans for failure
""",
        },
        {
            "title": "RBAC & Security",
            "slug": "rbac-security",
            "difficulty": "hard",
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# RBAC & Security

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan RBAC | Konsekvens |
|------------------|------------|
| Alla har full access | En miss kan ta ner hela klustret |
| Ingen audit trail | Vet inte vem som gjorde vad |
| Delad ServiceAccount | Lateral movement vid kompromiss |
| Over-privileged pods | Angreppyta for attackerare |

RBAC (Role-Based Access Control) binder Subjects (anvandare/serviceaccounts) till Roles (uppsattning permissions) via RoleBindings. Det ar som att ge nycklar - du bestammer vem som far vilka nycklar och vilka dorrar nycklarna oppnar.

+-------------+     +-------------+     +-------------+
|   Subject   |◀---▶| RoleBinding |◀---▶|    Role     |
| (vem)       |     | (koppling)  |     | (vad)       |
+-------------+     +-------------+     +-------------+
      |                   |                   |
      ▼                   ▼                   ▼
+-------------+     +-------------+     +-------------+
| User        |     | namespace   |     | pods: get   |
| Group       |     | eller       |     | pods: list  |
| ServiceAcct |     | cluster     |     | pods: watch |
+-------------+     +-------------+     +-------------+

------------------------------------------------------------

---

## ServiceAccounts

```bash
kubectl get serviceaccounts
# Listar alla ServiceAccounts i namespace
# default skapas automatiskt
# Varje pod kör som en ServiceAccount
# ServiceAccounts används för pod-till-API kommunikation

kubectl create serviceaccount deploy-bot
# Skapar ny ServiceAccount
# Pods kan referera till denna
# Får ingen permission förrän Role binds
# Bra för CI/CD pipelines
```

```yaml
# pod-with-sa.yaml
apiVersion: v1
kind: Pod
metadata:
  name: deploy-pod
spec:
  serviceAccountName: deploy-bot
  containers:
  - name: kubectl
    image: bitnami/kubectl:latest
    command: ["sleep", "infinity"]
```

```bash
kubectl apply -f pod-with-sa.yaml
# Podden kör som deploy-bot ServiceAccount
# Token monteras automatiskt i /var/run/secrets
# Podden kan bara göra det som deploy-bot får
# Utan RoleBinding - kan den inget!
```

---

## Roles och ClusterRoles

```yaml
# role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: development
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["pods/log"]
  verbs: ["get"]
```

```bash
kubectl apply -f role.yaml
# Role = permissions inom ETT namespace
# apiGroups: [""] = core API (pods, services, etc.)
# resources = vilka objekt
# verbs = vilka operationer

kubectl get roles -n development
# Listar alla Roles i namespace
# NAME visar rollnamnet
# Roles är namespace-scoped
# För kluster-wide: använd ClusterRole
```

---

## ClusterRoles

```yaml
# clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-viewer
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["metrics.k8s.io"]
  resources: ["nodes"]
  verbs: ["get", "list"]
```

```bash
kubectl apply -f clusterrole.yaml
# ClusterRole = permissions i HELA klustret
# Nodes är inte namespace-scoped
# Används även för aggregerade permissions
# Kan bindas per-namespace med RoleBinding

kubectl get clusterroles | grep -v system
# Listar ClusterRoles (utan system-roller)
# Många inbyggda roller finns
# view, edit, admin, cluster-admin
# Använd inbyggda roller där möjligt
```

---

## RoleBindings och ClusterRoleBindings

```yaml
# rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: development
subjects:
- kind: ServiceAccount
  name: deploy-bot
  namespace: development
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
kubectl apply -f rolebinding.yaml
# Binder ServiceAccount och User till Role
# subjects = vem får permissions
# roleRef = vilken Role som ger permissions
# RoleBinding = gäller i ett namespace

kubectl get rolebindings -n development
# Listar alla RoleBindings
# ROLE visar vilken role som binds
# Subjects syns i describe output
```

---

## Testa permissions

```bash
kubectl auth can-i get pods --namespace development --as system:serviceaccount:development:deploy-bot
# yes/no svar
# Testar om ServiceAccount kan göra något
# --as impersonerar användare/SA
# Viktigt för att verifiera RBAC

kubectl auth can-i '*' '*' --as system:serviceaccount:kube-system:default
# Testar alla permissions
# '*' = wildcard för alla resources/verbs
# Använd för att hitta över-privilegierade accounts
# cluster-admin kan allt

kubectl auth can-i list pods --all-namespaces --as jane
# Testar cross-namespace permissions
# --all-namespaces kräver oftast ClusterRoleBinding
# Utan det - bara RoleBinding-namespaces
# Helps debug "why can't they do X?"
```

---

## Pod Security

```yaml
# pod-security-context.yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    runAsNonRoot: true
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

```bash
kubectl apply -f pod-security-context.yaml
# runAsUser = kör inte som root
# readOnlyRootFilesystem = ingen skrivning
# capabilities drop ALL = ta bort alla Linux capabilities
# Minimerar attack surface

kubectl exec secure-pod -- id
# Visar vilken användare containern kör som
# uid=1000, gid=3000
# Bekräftar att securityContext fungerar
# Root (uid=0) bör undvikas!
```

---

## Network Policies

```yaml
# networkpolicy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - port: 5432
```

```bash
kubectl apply -f networkpolicy.yaml
# Begränsar nätverkstrafik till/från pods
# Default = all trafik tillåten
# Med policy = endast specificerad trafik
# Kräver CNI som stödjer NetworkPolicies (Calico, Cilium)

kubectl get networkpolicies -n production
# Listar policies i namespace
# Pods utan matchande policy = obegränsade
# Pods med policy = endast explicit trafik
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| ServiceAccount | Identitet for pods, token monteras automatiskt |
| Role | Namespace-scoped permissions (get, list, watch, etc.) |
| ClusterRole | Cluster-wide permissions over alla namespaces |
| RoleBinding | Kopplar Subject till Role i specifikt namespace |
| Pod Security | runAsNonRoot, drop capabilities, readOnlyRootFilesystem |

## Kom ihag

- ALLTID skapa separat ServiceAccount for varje app, anvand inte default
- kubectl auth can-i testar permissions - anvand for att verifiera RBAC
- NetworkPolicies kraver CNI som stodjer dem (Calico, Cilium)
- Drop ALL capabilities och lagg bara till de som behovs
- ClusterRoleBinding ger access i ALLA namespaces - anvand sparsamt
""",
        },
        {
            "title": "Helm Package Manager",
            "slug": "helm-package-manager",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Helm Package Manager

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan Helm | Konsekvens |
|------------------|------------|
| Duplicerad YAML | Samma filer kopieras och modifieras manuellt |
| Ingen templating | Dev, staging, prod har separata filer |
| Svar rollback | Manuell aterskapning vid problem |
| Komplex installation | Manga kubectl apply for en app |

Helm ar Kubernetes pakethanterare. Ett chart ar ett paket med alla YAML-filer for en app. Values ar variabler som anpassar chartet. Nar du installerar skapas en release - en specifik installation av ett chart.

+-------------+     +-------------+     +-------------+
|    Chart    |  +  |   Values    |  =  |   Release   |
|  (template) |     |  (config)   |     |  (instance) |
+-------------+     +-------------+     +-------------+
      |                   |                   |
      ▼                   ▼                   ▼
+-------------+     +-------------+     +-------------+
| Deployment  |     | replicaCount|     |  my-nginx   |
| Service     |     | image.tag   |     |  revision 1 |
| ConfigMap   |     | resources   |     |  Running    |
+-------------+     +-------------+     +-------------+

------------------------------------------------------------

---

## Installera Helm

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
# Installerar Helm CLI
# macOS: brew install helm
# Windows: choco install kubernetes-helm
# Helm pratar direkt med kubectl context

helm version
# Visar installerad Helm-version
# Client version är det viktiga
# Helm 3 behöver ingen server-komponent
# Fungerar direkt med kubeconfig
```

---

## Hantera repositories

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
# Lägger till ett chart repository
# bitnami = lokalt namn för repot
# URL:en innehåller index.yaml med alla charts
# Bitnami har många populära appar

helm repo update
# Uppdaterar lokal cache av repos
# Kör detta regelbundet
# Nya versioner och charts hämtas
# Snabbt - bara metadata laddas

helm search repo nginx
# Söker efter nginx i alla repos
# Visar chart-namn, version, app version
# CHART VERSION vs APP VERSION
# Chart = paket, App = mjukvara i paketet
```

---

## Installera charts

```bash
helm install my-nginx bitnami/nginx
# Installerar nginx chart
# my-nginx = release-namn (du väljer)
# bitnami/nginx = chart från bitnami repo
# Skapar alla Kubernetes-resurser

helm list
# Listar alla installerade releases
# NAME, NAMESPACE, REVISION, STATUS
# CHART visar vilken version som kördes
# Snabb överblick av installationer

helm status my-nginx
# Visar status för en release
# Resources som skapades
# Notes med post-install instruktioner
# Hur du accessa appen
```

---

## Values - Anpassa installationer

```bash
helm show values bitnami/nginx > values.yaml
# Exporterar alla tillgängliga values
# Kommentarer förklarar varje värde
# Utgångspunkt för anpassning
# Ändra och använd med -f

helm install my-nginx bitnami/nginx -f values.yaml
# Installerar med anpassade values
# Dina values överskriver defaults
# Behåll bara det du ändrar
# Lättare att underhålla

helm install my-nginx bitnami/nginx --set replicaCount=3 --set service.type=LoadBalancer
# Enskilda values via kommandoraden
# --set för snabba ändringar
# Bra för CI/CD
# -f för större ändringar
```

---

## Upgrade och Rollback

```bash
helm upgrade my-nginx bitnami/nginx --set replicaCount=5
# Uppgraderar release med nya values
# Kubernetes gör rolling update
# Revision ökar
# Historik sparas för rollback

helm history my-nginx
# Visar alla revisioner
# REVISION, UPDATED, STATUS
# DESCRIPTION visar vad som ändrades
# Hjälper välja revision för rollback

helm rollback my-nginx 1
# Rullar tillbaka till revision 1
# Samma som att uppgradera till gammal config
# Skapar en ny revision
# Snabbt sätt att återställa
```

---

## Skapa egna charts

```bash
helm create mychart
# Skapar chart-skelett
# mychart/Chart.yaml - metadata
# mychart/values.yaml - default values
# mychart/templates/ - Kubernetes YAML med Go templates
# Startpunkt för eget chart

# templates/deployment.yaml exempel:
# replicas: {{ .Values.replicaCount }}
# image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
# Go template syntax
# .Values hämtar från values.yaml
```

```yaml
# mychart/values.yaml
replicaCount: 3
image:
  repository: myapp
  tag: "1.0.0"
service:
  type: ClusterIP
  port: 80
```

```bash
helm install my-release ./mychart
# Installerar från lokal katalog
# Bra för utveckling och test
# Använd absolut eller relativ sökväg
# Samma kommandostruktur som repo-charts
```

---

## Template debugging

```bash
helm template my-release ./mychart
# Renderar templates utan att installera
# Visar genererade YAML
# Perfekt för debugging
# Kör innan install för att verifiera

helm template my-release ./mychart -f prod-values.yaml
# Renderar med specifika values
# Se exakt vad som kommer skapas
# Verifiera innan deploy till produktion
# Inkludera i code review

helm lint ./mychart
# Validerar chart-struktur
# Hittar fel i templates
# Rekommendationer för best practices
# Kör i CI/CD pipeline
```

---

## Helm hooks

```yaml
# templates/pre-install-job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migrate
  annotations:
    "helm.sh/hook": pre-install,pre-upgrade
    "helm.sh/hook-weight": "0"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: myapp:latest
        command: ["./migrate.sh"]
      restartPolicy: Never
```

```bash
# Hooks kor vid specifika tidpunkter
# pre-install = fore alla resurser skapas
# post-install = efter installation klar
# pre-upgrade, post-upgrade = vid uppgradering
# Perfekt for databas-migreringar
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Chart | Paket med Kubernetes YAML-filer och templates |
| Values | Variabler for miljospecifik anpassning |
| Release | En specifik installation av ett chart med namn |
| helm upgrade | Uppdaterar release med nya values, skapar revision |
| helm rollback | Aterstaller till tidigare revision pa sekunder |

## Kom ihag

- helm repo add + helm repo update innan forsta installation
- helm show values exporterar alla tillgangliga konfigurationsalternativ
- helm template renderar YAML utan att installera - perfekt for debugging
- helm lint validerar chart-struktur och best practices
- Hooks kor databas-migreringar automatiskt vid upgrade
""",
        },
        {
            "title": "Monitoring & Observability",
            "slug": "monitoring-observability",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Monitoring & Observability

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan observability | Konsekvens |
|---------------------------|------------|
| Kan inte se resursanvandning | Overraskande OOM-kills och throttling |
| Ingen loggaggregering | Soka manuellt i varje container |
| Saknar alerting | Anvandare rapporterar fel fore dig |
| Ingen tracing | Omojligt hitta flaskhalsar i microservices |

Observability = metrics + logs + traces. Du kan inte fixa det du inte kan se. Prometheus scrapar metrics, Loki samlar loggar, Grafana visualiserar - tillsammans ger de fullstandig insyn i klustret.

+-------------+     +-------------+     +-------------+
|   Metrics   |----▶|  Prometheus |----▶|   Grafana   |
|   Server    |     |   (scrape)  |     |   (visas)   |
+-------------+     +-------------+     +-------------+
       |                   |                   ▲
       ▼                   ▼                   |
+-------------+     +-------------+     +-------------+
|  kubectl    |     |   Loki      |----▶|  Dashboards |
|    top      |     |   (logs)    |     |   Alerts    |
+-------------+     +-------------+     +-------------+

------------------------------------------------------------

---

## Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
# Installerar Metrics Server
# Samlar in CPU/minne från kubelet
# Krävs för kubectl top och HPA
# Lätt - inte för långtidslagring

kubectl get deployment metrics-server -n kube-system
# Verifierar installation
# READY ska vara 1/1
# Kan ta en minut att bli klar
# Om problem - kolla pod-loggar

kubectl top nodes
# Visar CPU och minnesanvändning per node
# CPU i millicores (1000m = 1 kärna)
# Fungerar efter metrics-server är redo
# Första steget för kapacitetsplanering

kubectl top pods --all-namespaces --sort-by=cpu
# Visar pods sorterade efter CPU
# --sort-by=memory för minnesanvändning
# Hittar resurshungriga pods
# Viktig för optimering
```

---

## Prometheus

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
# Lägger till Prometheus Helm repo
# Officiellt community-repo
# Innehåller stack med Prometheus + Grafana
# Enklaste sättet att komma igång

helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
# Installerar hela stacken
# Prometheus, Grafana, Alertmanager
# Node Exporter, kube-state-metrics
# Fördefinierade dashboards och alerts

kubectl get pods -n monitoring
# Visar alla komponenter
# prometheus-server, grafana, alertmanager
# Allt ska vara Running
# Kan ta några minuter att starta
```

---

## Prometheus Queries (PromQL)

```bash
kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 9090
# Öppnar Prometheus UI på localhost:9090
# port-forward tunnlar trafik via kubectl
# Inget externt behövs
# Ctrl+C för att stänga

# I Prometheus UI - kör queries:

container_cpu_usage_seconds_total
# Rå CPU-användning för alla containers
# Counter - ökar över tid
# Aggregera med rate() för användbar data

rate(container_cpu_usage_seconds_total{namespace="default"}[5m])
# CPU per sekund, medel över 5 minuter
# namespace="default" filtrerar
# rate() konverterar counter till gauge
# Perfekt för grafer

sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m])) by (pod)
# Summerar per pod
# by (pod) grupperar resultat
# Användbart för top N pods
# Lägg i Grafana för visualisering
```

---

## Grafana Dashboards

```bash
kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80
# Öppnar Grafana på localhost:3000
# Default: admin/prom-operator (eller admin/admin)
# Fördefinierade dashboards finns
# Kubernetes / Compute Resources mest använd

kubectl get secret prometheus-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 -d
# Hämtar Grafana admin-lösenord
# Behövs vid första inloggning
# base64 -d avkodar
# Ändra lösenordet efter inloggning
```

---

## Logging med Loki

```bash
helm install loki grafana/loki-stack -n monitoring
# Installerar Loki för logghantering
# Promtail samlar loggar från alla pods
# Loki lagrar och indexerar
# Grafana kan query:a Loki

# I Grafana - lägg till Loki datasource:
# URL: http://loki:3100
# Klicka "Save & Test"
# Gå till Explore och välj Loki
```

```bash
# LogQL queries i Grafana:
{namespace="default"}
# Alla loggar från default namespace

{app="nginx"} |= "error"
# Loggar från nginx som innehåller "error"

{namespace="production"} | json | status >= 500
# Parse JSON, filtrera på status >= 500
# Kraftfullt för strukturerade loggar
```

---

## Alerting

```yaml
# prometheus-rule.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: pod-alerts
  namespace: monitoring
  labels:
    release: prometheus
spec:
  groups:
  - name: pod-alerts
    rules:
    - alert: PodCrashLooping
      expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Pod is crash looping"
        description: "Pod {{ $labels.pod }} in namespace {{ $labels.namespace }} is restarting"
```

```bash
kubectl apply -f prometheus-rule.yaml
# Skapar alert-regel
# expr = PromQL query som triggrar alert
# for = hur länge villkoret måste gälla
# Alertmanager skickar notifications

kubectl port-forward svc/prometheus-kube-prometheus-alertmanager -n monitoring 9093
# Öppnar Alertmanager UI
# Visar aktiva alerts
# Konfigurerar notification routes
# Silences för planerade underhåll
```

---

## Service Monitoring

```yaml
# servicemonitor.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-app-monitor
  namespace: monitoring
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
    interval: 30s
  namespaceSelector:
    matchNames:
    - default
```

```bash
kubectl apply -f servicemonitor.yaml
# Säger åt Prometheus att scrapa my-app
# selector matchar Service labels
# endpoints definierar port och intervall
# Automatisk discovery av nya pods

kubectl get servicemonitors -n monitoring
# Listar alla ServiceMonitors
# Prometheus upptäcker dem automatiskt
# Targets syns i Prometheus UI
# Verifiera att scraping fungerar
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Metrics Server | Grundlaggande metrics for kubectl top och HPA |
| Prometheus | Scraping, lagring, queries med PromQL |
| Grafana | Visualisering med dashboards och alerts |
| Loki | Logghantering med LogQL queries |
| ServiceMonitor | CRD for automatisk Prometheus-konfiguration |

## Kom ihag

- Installera prometheus-community Helm chart for komplett stack
- PromQL rate() konverterar counters till anvandbar data
- ServiceMonitor matar Prometheus vilka services som ska scrapas
- Alertmanager skickar notifications vid definierade triggers
- Loki + Grafana = enhetlig plattform for loggar och metrics
""",
        },
        {
            "title": "Troubleshooting Kubernetes",
            "slug": "troubleshooting-kubernetes",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Troubleshooting Kubernetes

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan felsokning | Konsekvens |
|------------------------|------------|
| Slumpmassig debugging | Timmar bortkastade pa gissningar |
| Saknar systematik | Missar rotorsak, fixar symptom |
| Fel verktyg | Ser inte vad som faktiskt hander |
| Ingen process | Panik nar incidenter intraffar |

Saker gar fel - det ar inte "om" utan "nar". Effektiv felsokning foljer ordningen: Nodes -> Pods -> Containers -> Logs -> Events. Borja brett och zooma in. De flesta problem ligger i pods som inte startar eller containers som crashar.

+-----------------------------------------------------------+
|              TROUBLESHOOTING WORKFLOW                      |
+-----------------------------------------------------------+
|  1. kubectl get nodes          - Ar alla noder Ready?      |
|  2. kubectl get pods           - Vilka pods har problem?   |
|  3. kubectl describe pod       - Vad sager Events?         |
|  4. kubectl logs --previous    - Varfor crashade den?      |
|  5. kubectl exec -it           - Debugga inifran           |
+-----------------------------------------------------------+

------------------------------------------------------------

---

## Nodproblem

```bash
kubectl get nodes
# Första steget - är alla noder Ready?
# NotReady = nod kan inte köra pods
# SchedulingDisabled = markerad som underhåll
# Unknown = kontakt förlorad med noden

kubectl describe node <node-name>
# Detaljerad nodinformation
# Conditions visar problem (DiskPressure, MemoryPressure)
# Events visar vad som hänt
# Allocated resources visar om noden är överbelastad

kubectl top nodes
# Resursanvändning i realtid
# Hög CPU/minne = potentiell orsak till problem
# Jämför med Allocatable i describe
# Om nära 100% - skala klustret

systemctl status kubelet
# SSH till noden och kolla kubelet
# Kubelet måste köra för att noden ska fungera
# journalctl -u kubelet för loggar
# Vanlig orsak till NotReady
```

---

## Pod-problem

```bash
kubectl get pods --all-namespaces | grep -v Running
# Hitta alla icke-Running pods
# Pending, CrashLoopBackOff, Error, ImagePullBackOff
# -v Running exkluderar friska pods
# Snabb överblick av problem

kubectl describe pod <pod-name>
# ALLTID börja här för pod-problem
# Events visar scheduling, pulling, starting
# Conditions visar Ready, Initialized
# Oftast hittar du svaret i Events

kubectl get events --sort-by=.lastTimestamp
# Alla kluster-events sorterade efter tid
# Visar bredare bild
# FailedScheduling, FailedMount, etc.
# Hjälper hitta mönster
```

---

## Vanliga pod-statusar

```bash
# Pending
# Pod väntar på scheduling eller resurser
# kubectl describe visar varför
# "Insufficient cpu/memory" = resursbrist
# "No nodes available" = taints/tolerations problem

# ImagePullBackOff
# Kan inte hämta container image
# Fel image-namn, tag saknas, registry problem
# kubectl describe visar image pull error
# Verifiera att imagen finns och är tillgänglig

# CrashLoopBackOff
# Container startar, crashar, startar igen
# kubectl logs --previous visar varför
# Ofta config-fel eller missing dependencies
# Exit code ger ledtrådar

# Error / Failed
# Container avslutade med fel
# kubectl logs för detaljer
# Kolla exit code i describe
# 137 = OOMKilled, 1 = app error
```

---

## Container-debugging

```bash
kubectl logs <pod-name>
# Visar container stdout/stderr
# Om multi-container: -c <container-name>
# -f för att följa i realtid
# Första stället för app-problem

kubectl logs <pod-name> --previous
# Loggar från förra körningen
# KRITISKT vid CrashLoopBackOff
# Visar vad som hände innan crash
# Utan detta ser du bara tom/ny container

kubectl exec -it <pod-name> -- /bin/sh
# Shell i containern
# Felsök inifrån
# Kontrollera filer, miljövariabler, nätverk
# /bin/bash om tillgänglig, annars /bin/sh

kubectl exec <pod-name> -- cat /etc/resolv.conf
# DNS-konfiguration i podden
# Ska peka på kube-dns/CoreDNS
# Om fel - DNS fungerar inte
# Vanlig orsak till service discovery problem
```

---

## Nätverksproblem

```bash
kubectl run debug --image=busybox --rm -it -- /bin/sh
# Tillfällig debug-pod
# --rm tar bort den efteråt
# busybox har grundläggande verktyg
# Perfekt för nätverkstester

# I debug-podden:
nslookup kubernetes
# Testar DNS
# Ska returnera kubernetes service IP
# Om det misslyckas - CoreDNS problem
# Kolla CoreDNS pods i kube-system

wget -qO- http://my-service:80 --timeout=5
# Testar service connectivity
# --timeout för att inte vänta för länge
# Om timeout - kolla endpoints
# Om refused - app lyssnar inte

kubectl get endpoints my-service
# Visar vilka pods service pekar på
# Tom lista = inga pods matchar selector
# Fel port = service misconfiguration
# Första kontrollen vid service problem
```

---

## DNS-debugging

```bash
kubectl run dnsutils --image=tutum/dnsutils --rm -it -- /bin/sh
# Pod med mer DNS-verktyg
# dig och nslookup
# Bättre än busybox för DNS-debugging

dig my-service.default.svc.cluster.local
# Fullständig DNS-lookup
# Visar vilket svar DNS ger
# NXDOMAIN = service finns inte
# Timeout = CoreDNS problem

kubectl logs -n kube-system -l k8s-app=kube-dns
# CoreDNS loggar
# Visar DNS queries och eventuella fel
# Hjälper hitta misconfiguration
# Kontrollera vid DNS-problem
```

---

## Storage-problem

```bash
kubectl get pvc
# Lista PersistentVolumeClaims
# Pending = ingen matchande PV
# Bound = OK
# Lost = PV försvunnit

kubectl describe pvc <pvc-name>
# Detaljer om PVC
# Events visar provisioning-försök
# "waiting for a volume" = ingen PV matchar
# Kolla StorageClass och accessModes

kubectl get pv
# Lista alla PersistentVolumes
# Available = kan bindas
# Bound = redan i användning
# Released = frigjord men inte återanvänd

kubectl describe pod <pod-name> | grep -A 5 "Volumes"
# Volumes som podden försöker montera
# Visar PVC-namn och mount path
# Hjälper koppla pod-problem till storage
```

---

## Debugging cheat sheet

```bash
# Pod startar inte:
kubectl describe pod <pod>     # Kolla Events
kubectl get events             # Bredare bild

# Container crashar:
kubectl logs <pod> --previous  # Loggar innan crash
kubectl describe pod <pod>     # Exit code

# Service fungerar inte:
kubectl get endpoints <svc>    # Är pods kopplade?
kubectl exec debug -- wget     # Nätverkstest

# DNS fungerar inte:
kubectl exec debug -- nslookup # Testa DNS
kubectl logs -n kube-system coredns  # DNS loggar

# Storage fungerar inte:
kubectl get pvc,pv             # Status
kubectl describe pvc <pvc>     # Events
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| kubectl describe | ALLTID forsta kommandot - visar Events och Conditions |
| Events | Kubernetes berattelse om vad den forsokat gora |
| logs --previous | KRITISKT for CrashLoopBackOff - visar loggar innan crash |
| Debug pod | busybox for natverkstester inifran klustret |
| Systematik | Folj ordningen Nodes -> Pods -> Containers -> Logs |

## Kom ihag

- Pending = scheduling-problem, kolla node resources och taints
- ImagePullBackOff = fel image-namn, tag eller registry-access
- CrashLoopBackOff = container crashar, anvand logs --previous
- Exit code 137 = OOMKilled, oka memory limits
- DNS-problem = kolla CoreDNS pods i kube-system namespace
""",
        },
        {
            "title": "GitOps & Continuous Deployment",
            "slug": "gitops-continuous-deployment",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# GitOps & Continuous Deployment

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan GitOps | Konsekvens |
|--------------------|------------|
| Manuella deploys | Skalas inte, felbenaget, tidskravande |
| Ingen audit trail | Vet inte vem som deployade vad och nar |
| Svar rollback | Stressigt aterstella vid problem |
| Config drift | Kluster matchar inte dokumentation |

GitOps vander pa deployment-processen. Istallet for att pusha till klustret, pullar klustret fran Git. En operator (ArgoCD, Flux) overvakar repot och synkroniserar andringar automatiskt. Git = single source of truth.

+-------------+     +-------------+     +-------------+
|  Developer  |----▶|    Git      |----▶|   ArgoCD    |
|  (commit)   |     |   (repo)    |     |  (watch)    |
+-------------+     +-------------+     +-------------+
                                               |
                           +-------------------+
                           ▼
                    +-------------+     +-------------+
                    |  Kubernetes |◀----|    Sync     |
                    |  (cluster)  |     |  (apply)    |
                    +-------------+     +-------------+

------------------------------------------------------------

---

## ArgoCD Installation

```bash
kubectl create namespace argocd
# Skapar namespace för ArgoCD
# Alla ArgoCD-komponenter kör här
# Isolerat från dina applikationer
# Best practice för system-komponenter

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
# Installerar ArgoCD
# Skapar Deployments, Services, CRDs
# Tar en minut att starta
# Verifierar med get pods

kubectl get pods -n argocd
# Alla pods ska vara Running
# argocd-server = UI och API
# argocd-repo-server = hanterar Git repos
# argocd-application-controller = synkroniserar
```

---

## ArgoCD CLI och UI

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
# Öppnar ArgoCD UI på localhost:8080
# HTTPS (acceptera cert-varning)
# UI är huvudsättet att interagera
# CLI finns också för automation

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
# Hämtar admin-lösenordet
# Användarnamn: admin
# Ändra lösenordet efter inloggning
# Eller koppla till SSO/LDAP

argocd login localhost:8080
# CLI login (kräver argocd CLI installerat)
# brew install argocd
# Samma credentials som UI
# Behövs för CLI-kommandon
```

---

## Skapa Application

```yaml
# application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/my-app-config
    targetRevision: HEAD
    path: k8s
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

```bash
kubectl apply -f application.yaml
# Skapar ArgoCD Application
# source = Git repo med Kubernetes YAML
# destination = var i klustret det ska deployeas
# automated = synka automatiskt vid ändringar

argocd app list
# Listar alla Applications
# STATUS visar Synced/OutOfSync
# HEALTH visar Healthy/Degraded/Progressing
# Snabb överblick av alla deployments
```

---

## Repository-struktur

```bash
# Recommended repo structure:
my-app-config/
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
+-- README.md

# base/ innehåller grundläggande YAML
# overlays/ har miljö-specifika ändringar
# Kustomize hanterar skillnaderna
# ArgoCD stödjer Kustomize nativt
```

---

## Sync och Rollback

```bash
argocd app sync my-app
# Tvingar synkronisering nu
# Användbart för manuell deploy
# Eller efter att fixat config
# Med automated - sker automatiskt

argocd app sync my-app --revision abc123
# Synkar till specifik commit
# Användbart för rollback
# Eller för att testa specifik version
# Git hash från repo history

argocd app history my-app
# Visar deployment history
# Revision, deployed at, status
# Samma info som i UI
# Hjälper hitta vad som deployades
```

---

## Flux CD alternativ

```bash
flux bootstrap github \
  --owner=myorg \
  --repository=fleet-infra \
  --path=clusters/production \
  --personal
# Installerar Flux och konfigurerar GitHub
# Skapar repo om det inte finns
# Bootstrappar sig själv via GitOps
# Allt konfigureras via Git efter detta

kubectl get gitrepository -A
# Visar konfigurerade Git-repos
# Flux övervakar dessa för ändringar
# STATUS Ready = fungerar
# Events visar eventuella problem
```

---

## Image Automation

```yaml
# image-update-automation.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageUpdateAutomation
metadata:
  name: auto-update
  namespace: flux-system
spec:
  interval: 1m
  sourceRef:
    kind: GitRepository
    name: fleet-infra
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        email: flux@myorg.com
        name: Flux
      messageTemplate: 'Update image to {{.NewTag}}'
    push:
      branch: main
  update:
    path: ./clusters/production
    strategy: Setters
```

```bash
kubectl apply -f image-update-automation.yaml
# Flux övervakar container registry
# Ny image tag -> commit till Git
# ArgoCD/Flux synkar automatiskt
# Full automation: build -> push -> deploy
```

---

## Secrets hantering

```bash
# Secrets ska INTE committas i klartext!
# Använd Sealed Secrets eller External Secrets

kubeseal --format yaml < secret.yaml > sealed-secret.yaml
# Krypterar secret med klustrets nyckel
# Säkert att committa till Git
# Bara klustret kan dekryptera
# sealed-secrets-controller hanterar

kubectl apply -f sealed-secret.yaml
# Controller dekrypterar och skapar Secret
# Automatiskt vid sync
# Roterar secrets via Git commits
# Audit trail för alla secrets
```

---

## Best Practices

```bash
# 1. Separata repos för config och kod
# App-repo: kod, tests, CI
# Config-repo: Kubernetes YAML, Kustomize/Helm
# Tydlig separation av concerns

# 2. Environment branches eller directories
# branches: main (prod), staging, develop
# directories: overlays/prod, overlays/staging
# Directories är ofta enklare att hantera

# 3. Pull Requests för alla ändringar
# Ingen direkt push till main
# Code review för infra-ändringar
# Merge = deploy

# 4. Notifications
# Slack/Teams integration
# Veta när deploys sker
# Alerting vid sync failures
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| GitOps | Git ar single source of truth for all infrastruktur |
| ArgoCD/Flux | Operators som overvakar Git och synkroniserar till kluster |
| Automated sync | Push till Git = automatisk deploy till kluster |
| Rollback | git revert eller argocd sync till gammal revision |
| Sealed Secrets | Krypterade secrets sakra att committa till Git |

## Kom ihag

- Separera app-repo (kod) fran config-repo (Kubernetes YAML)
- Kustomize overlays for miljospecifik konfiguration
- PR-baserat workflow = code review for infra-andringar
- ALDRIG commit secrets i klartext - anvand Sealed Secrets
- Flux bootstrap konfigurerar sig sjalv via GitOps
""",
        },
        {
            "title": "Kubernetes Best Practices",
            "slug": "kubernetes-best-practices",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Kubernetes Best Practices

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Problem utan best practices | Konsekvens |
|---------------------------|------------|
| Ingen resurshantering | Pods som tar alla resurser, OOM-kills |
| :latest tag | Oforutsagbara deploys, ingen reproducerbarhet |
| Root containers | Sakerhetssarbarheter, potentiell kompromiss |
| Saknar probes | Trafik till ohalsosamma pods, dalig UX |

Kubernetes ar flexibelt - det finns manga satt att gora saker. Best practices hjalper dig bygga for produktion fran dag ett, undvika vanliga misstag och skapa system som skalar med behoven.

+-------------------------------------------------------------+
|               PRODUCTION-READY CHECKLIST                     |
+-------------------------------------------------------------+
| [ ] Resource requests OCH limits satta                       |
| [ ] Liveness OCH readiness probes konfigurerade             |
| [ ] Specifik image tag (ALDRIG :latest)                      |
| [ ] SecurityContext med non-root, readOnlyRootFilesystem    |
| [ ] NetworkPolicies for trafikbegransning                   |
| [ ] PodDisruptionBudget for HA                              |
+-------------------------------------------------------------+

------------------------------------------------------------

---

## Pod Design

```yaml
# good-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: production-ready
  labels:
    app: myapp
    version: "1.2.3"
    environment: production
spec:
  containers:
  - name: app
    image: myapp:1.2.3
    ports:
    - containerPort: 8080
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "500m"
        memory: "256Mi"
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      periodSeconds: 5
    securityContext:
      runAsNonRoot: true
      readOnlyRootFilesystem: true
      allowPrivilegeEscalation: false
```

```bash
# Best practices i exemplet:
# - Specifik image tag (inte :latest)
# - Resource requests OCH limits
# - Liveness OCH readiness probes
# - Security context (non-root, read-only)
# - Meningsfulla labels
```

---

## Deployment Strategies

```yaml
# rolling-update.yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
```

```bash
# RollingUpdate (default och rekommenderat)
# maxSurge = hur många extra pods under update
# maxUnavailable = hur många som kan vara nere
# 25%/25% är bra balans för de flesta fall

# Recreate (bara för speciella fall)
# Alla pods dör innan nya skapas
# Downtime - använd endast om nödvändigt
# T.ex. vid breaking schema changes

# Blue-Green och Canary
# Använd Ingress eller service mesh
# ArgoCD har inbyggt stöd
# Mer kontroll men mer komplexitet
```

---

## Namespace Organisation

```bash
# Per team:
kubectl create namespace team-frontend
kubectl create namespace team-backend
kubectl create namespace team-data

# Per miljö:
kubectl create namespace development
kubectl create namespace staging
kubectl create namespace production

# Eller kombinerat:
kubectl create namespace frontend-prod
kubectl create namespace frontend-staging

# Best practice: namespace per team + miljö
# ResourceQuotas per namespace
# RBAC per namespace
# NetworkPolicies per namespace
```

---

## Configuration Management

```yaml
# Använd ConfigMaps för icke-känslig config
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "info"
  API_ENDPOINT: "https://api.example.com"

# Använd Secrets för känslig data
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  API_KEY: base64-encoded-value

# I produktion - External Secrets eller Sealed Secrets
# ALDRIG commit secrets i klartext
# Rotera secrets regelbundet
```

---

## High Availability

```yaml
# Pod Anti-Affinity - sprid pods över noder
spec:
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchLabels:
              app: myapp
          topologyKey: kubernetes.io/hostname
```

```bash
# Best practices för HA:
# - Minst 3 replicas för kritiska tjänster
# - PodDisruptionBudget för att skydda vid underhåll
# - Anti-affinity för att sprida pods
# - Multi-zone deployment om möjligt

kubectl create poddisruptionbudget myapp-pdb --selector=app=myapp --min-available=2
# Garanterar att minst 2 pods alltid kör
# Skyddar mot oavsiktlig nedskalning
# Respekteras vid node drain
```

---

## Security Checklist

```bash
# 1. Non-root containers
securityContext:
  runAsNonRoot: true
  runAsUser: 1000

# 2. Read-only filesystem
securityContext:
  readOnlyRootFilesystem: true

# 3. Drop capabilities
securityContext:
  capabilities:
    drop:
      - ALL

# 4. Network policies
kubectl apply -f network-policy.yaml

# 5. RBAC med least privilege
kubectl auth can-i --list --as=system:serviceaccount:default:myapp

# 6. Secrets i Secret Manager
# Inte i Git, inte i env vars (loggas ibland)

# 7. Image scanning
# Trivy, Snyk, eller cloud provider scanner
trivy image myapp:1.2.3
```

---

## Resource Management

```bash
# Alltid sätt requests (scheduling)
# Alltid sätt limits (skydd)
# Requests <= Limits
# Guaranteed QoS för kritiska appar

# LimitRange för defaults
kubectl apply -f limitrange.yaml

# ResourceQuota för budgetar
kubectl apply -f resourcequota.yaml

# Vertical Pod Autoscaler för optimering
kubectl apply -f vpa.yaml

# Monitor med kubectl top
kubectl top pods --sort-by=memory
```

---

## Observability

```bash
# 1. Structured logging (JSON)
{"timestamp": "2024-01-15T10:30:00Z", "level": "info", "message": "Request processed", "duration": 150}

# 2. Metrics exposure
# /metrics endpoint i Prometheus format
# ServiceMonitor för automatisk discovery

# 3. Health endpoints
# /health för liveness
# /ready för readiness
# Olika logik för varje

# 4. Distributed tracing
# OpenTelemetry för spans
# Jaeger eller Zipkin för visualisering
```

---

## GitOps Workflow

```bash
# 1. Separera app-repo från config-repo
# App: kod, Dockerfile, tests
# Config: Kubernetes YAML, Helm, Kustomize

# 2. Miljöer via Kustomize overlays
base/
  deployment.yaml
  service.yaml
overlays/
  production/
    kustomization.yaml
  staging/
    kustomization.yaml

# 3. ArgoCD för synkronisering
# Automated sync för staging
# Manual sync för production

# 4. PR-baserat workflow
# Ingen direkt commit till main
# Review innan merge
# Merge = Deploy
```

---

## Disaster Recovery

```bash
# 1. Backup etcd regelbundet
ETCDCTL_API=3 etcdctl snapshot save backup.db

# 2. Backup PersistentVolumes
# Velero för Kubernetes-native backup
velero backup create daily-backup --include-namespaces production

# 3. Infrastructure as Code
# Terraform för kluster
# GitOps för workloads
# Allt ska kunna återskapas från kod

# 4. Test recovery regelbundet
# Restore till test-kluster
# Verifiera att data är intakt
# Dokumentera recovery time
```

---

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Resource requests/limits | ALLTID satta - requests for scheduling, limits for skydd |
| Non-root containers | ALDRIG kor som root - runAsNonRoot: true |
| Specifika image tags | ALDRIG :latest - anvand semantisk versioning |
| Probes | Liveness OCH readiness for varje container |
| GitOps workflow | All config i Git, PR-baserad review, automated sync |

## Kom ihag

- RollingUpdate med maxSurge/maxUnavailable 25% ar bra default
- Pod anti-affinity sprider replicas over olika noder
- PodDisruptionBudget skyddar mot oavsiktlig nedskalning
- Namespace per team + miljo for basta isolering
- Backup etcd och PVs regelbundet - testa recovery
""",
        },
    ],
}
