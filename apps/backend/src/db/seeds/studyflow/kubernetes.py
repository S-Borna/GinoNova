"""
Kubernetes Studyflow Data
Flashcards och Multiple Choice för Kubernetes
"""

KUBERNETES_MODULE = {
    "slug": "kubernetes",
    "title": "Kubernetes",
    "description": "Container orchestration med K8s",
    "icon": "Cloud",
    "topics": [
        {
            "id": "k8s-basics",
            "title": "Kubernetes Basics",
            "flashcards": [
                {"front": "Vad är Kubernetes?", "back": "Container orchestration platform för automatiserad deployment, scaling, management"},
                {"front": "Vad är en Pod?", "back": "Minsta deployable unit - en eller flera containers"},
                {"front": "Vad är en Node?", "back": "Worker machine (fysisk/virtuell) som kör Pods"},
                {"front": "Vad är Control Plane?", "back": "Hjärnan i K8s - API server, scheduler, controller manager"},
                {"front": "Vad är kubectl?", "back": "CLI-verktyg för att interagera med Kubernetes"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad är den minsta deployable unit i K8s?",
                    "options": ["Container", "Pod", "Node", "Deployment"],
                    "correct": 1,
                    "explanation": "Pod är minsta unit och kan innehålla en eller flera containers."
                },
                {
                    "question": "Vad är kubectl?",
                    "options": ["K8s API", "CLI-verktyg", "Container runtime", "Network plugin"],
                    "correct": 1,
                    "explanation": "kubectl är kommandoradsverktyget för K8s-kluster."
                },
            ]
        },
        {
            "id": "k8s-pods",
            "title": "Pods & Containers",
            "flashcards": [
                {"front": "kubectl get pods", "back": "Listar alla pods i current namespace"},
                {"front": "kubectl describe pod <name>", "back": "Visar detaljerad info om en pod"},
                {"front": "kubectl logs <pod>", "back": "Visar loggar från pod"},
                {"front": "kubectl exec -it <pod> -- bash", "back": "Öppnar shell i en pod"},
                {"front": "Vad är Pod lifecycle?", "back": "Pending → Running → Succeeded/Failed"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur ser man loggar från en pod?",
                    "options": ["kubectl log", "kubectl logs", "kubectl show logs", "kubectl get logs"],
                    "correct": 1,
                    "explanation": "kubectl logs <pod-name> visar container-loggar."
                },
                {
                    "question": "Vad betyder Pod status 'Pending'?",
                    "options": ["Körs", "Väntar på scheduling/resurser", "Fel uppstod", "Avslutad"],
                    "correct": 1,
                    "explanation": "Pending = pod väntar på att scheduleras till en node."
                },
            ]
        },
        {
            "id": "k8s-deployments",
            "title": "Deployments",
            "flashcards": [
                {"front": "Vad är en Deployment?", "back": "Deklarativ hantering av Pods och ReplicaSets"},
                {"front": "Vad är replicas?", "back": "Antal Pod-kopior som ska köras"},
                {"front": "kubectl scale deployment --replicas=3", "back": "Ändrar antal replicas till 3"},
                {"front": "Vad är Rolling Update?", "back": "Gradvis uppdatering utan downtime"},
                {"front": "kubectl rollout undo", "back": "Rullar tillbaka till föregående version"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad hanterar en Deployment?",
                    "options": ["Services", "Pods via ReplicaSet", "Volumes", "Secrets"],
                    "correct": 1,
                    "explanation": "Deployment hanterar Pods genom att skapa/hantera ReplicaSets."
                },
                {
                    "question": "Hur gör man rollback i K8s?",
                    "options": ["kubectl revert", "kubectl rollout undo", "kubectl restore", "kubectl back"],
                    "correct": 1,
                    "explanation": "kubectl rollout undo deployment/<name> rullar tillbaka."
                },
            ]
        },
        {
            "id": "k8s-services",
            "title": "Services & Networking",
            "flashcards": [
                {"front": "Vad är en Service?", "back": "Stabil nätverks-endpoint för att nå Pods"},
                {"front": "ClusterIP", "back": "Default - intern IP endast inom klustret"},
                {"front": "NodePort", "back": "Exponerar service på varje nodes IP:port"},
                {"front": "LoadBalancer", "back": "Skapar extern load balancer (cloud)"},
                {"front": "Ingress", "back": "HTTP/HTTPS routing till services"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilken Service-typ är default?",
                    "options": ["NodePort", "LoadBalancer", "ClusterIP", "ExternalName"],
                    "correct": 2,
                    "explanation": "ClusterIP är default och ger intern cluster-adress."
                },
                {
                    "question": "Vad används Ingress för?",
                    "options": ["Storage", "HTTP/HTTPS routing", "Logging", "Monitoring"],
                    "correct": 1,
                    "explanation": "Ingress hanterar extern HTTP/HTTPS-trafik till services."
                },
            ]
        },
        {
            "id": "k8s-config",
            "title": "ConfigMaps & Secrets",
            "flashcards": [
                {"front": "Vad är ConfigMap?", "back": "Lagrar icke-känslig konfiguration som key-value"},
                {"front": "Vad är Secret?", "back": "Lagrar känslig data (base64-encoded)"},
                {"front": "Hur använder pod ConfigMap?", "back": "Som env vars eller mounted volume"},
                {"front": "kubectl create secret generic", "back": "Skapar en secret från literal eller fil"},
                {"front": "Varför inte secrets i git?", "back": "Säkerhetsrisk - använd sealed secrets eller extern vault"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad lagrar en Secret?",
                    "options": ["Logs", "Metrics", "Känslig data (lösenord etc)", "Pod-definitioner"],
                    "correct": 2,
                    "explanation": "Secrets lagrar känslig data som lösenord, tokens, nycklar."
                },
                {
                    "question": "Hur encodas data i Secrets?",
                    "options": ["Krypterad", "Base64", "Plain text", "SHA256"],
                    "correct": 1,
                    "explanation": "Secrets är base64-encoded (inte krypterade som default!)."
                },
            ]
        },
        {
            "id": "k8s-storage",
            "title": "Persistent Storage",
            "flashcards": [
                {"front": "Vad är PersistentVolume (PV)?", "back": "Kluster-resurs för lagring"},
                {"front": "Vad är PersistentVolumeClaim (PVC)?", "back": "Request för lagring från en Pod"},
                {"front": "Vad är StorageClass?", "back": "Definierar typ av lagring (SSD, HDD etc)"},
                {"front": "accessModes: ReadWriteOnce", "back": "Kan mountas read-write av en node"},
                {"front": "accessModes: ReadWriteMany", "back": "Kan mountas read-write av flera nodes"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad requestar en PVC?",
                    "options": ["CPU", "Memory", "Storage", "Network"],
                    "correct": 2,
                    "explanation": "PVC (PersistentVolumeClaim) begär lagringsutrymme."
                },
                {
                    "question": "Vad definierar en StorageClass?",
                    "options": ["Pod-templat", "Lagringstyp och provisioner", "Network policy", "RBAC"],
                    "correct": 1,
                    "explanation": "StorageClass definierar lagringstyp och hur den provisioneras."
                },
            ]
        },
    ]
}
