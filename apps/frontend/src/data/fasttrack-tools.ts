/**
 * FastTrack Tools Data
 * Complete DevOps tools library
 */

import {
    FileJson,
    Box,
    Container,
    Terminal,
    Code,
    Monitor,
    Cloud,
    GitBranch,
    Cpu,
    Network,
    Database,
    Shield,
    Layers,
} from "lucide-react"

export interface Tool {
    slug: string
    name: string
    category: string
    icon: string
    shortDesc: string
    description: string
    installation: {
        apt?: string
        brew?: string
        pip?: string
        npm?: string
        other?: string
    }
    useCases: string[]
    keyFeatures: string[]
    officialUrl?: string
    docsUrl?: string
    flashcardCount: number
    quizCount: number
}

export const TOOL_CATEGORIES = [
    { id: "all", label: "Alla", icon: Layers },
    { id: "dataformat", label: "Dataformat", icon: FileJson },
    { id: "containers", label: "Containers", icon: Box },
    { id: "orchestration", label: "Orchestration", icon: Container },
    { id: "linux", label: "Linux & CLI", icon: Terminal },
    { id: "python", label: "Python", icon: Code },
    { id: "virtualization", label: "Virtualisering", icon: Monitor },
    { id: "cloud", label: "Cloud & IaC", icon: Cloud },
    { id: "cicd", label: "CI/CD", icon: GitBranch },
    { id: "monitoring", label: "Monitoring", icon: Cpu },
    { id: "network", label: "Nätverk", icon: Network },
    { id: "database", label: "Databaser", icon: Database },
    { id: "security", label: "Säkerhet", icon: Shield },
]

export const TOOLS_DATA: Tool[] = [
    // DATAFORMAT
    {
        slug: "yaml",
        name: "YAML",
        category: "dataformat",
        icon: "📄",
        shortDesc: "Human-readable data serialization",
        description: "YAML (YAML Ain't Markup Language) är ett dataformat som är lätt att läsa för människor. Används flitigt i Kubernetes, Docker Compose, Ansible och CI/CD-konfigurationer.",
        installation: {
            pip: "pip install pyyaml",
            npm: "npm install yaml"
        },
        useCases: ["Kubernetes manifests", "Docker Compose", "Ansible playbooks", "CI/CD pipelines", "Konfigurationsfiler"],
        keyFeatures: ["Indentation-baserad syntax", "Stöd för listor och maps", "Anchors & aliases", "Multi-document stöd"],
        officialUrl: "https://yaml.org",
        docsUrl: "https://yaml.org/spec/1.2.2/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "json",
        name: "JSON",
        category: "dataformat",
        icon: "📋",
        shortDesc: "JavaScript Object Notation",
        description: "JSON är ett lättviktigt datautbytesformat baserat på JavaScript-syntax. Standard för API-kommunikation och konfiguration.",
        installation: {
            other: "Inbyggt i de flesta språk"
        },
        useCases: ["REST APIs", "Konfigurationsfiler", "NoSQL databaser", "Web storage", "Package manifests"],
        keyFeatures: ["Strikt syntax", "Bred språkstöd", "Lätt att parsa", "Självbeskrivande"],
        officialUrl: "https://www.json.org",
        docsUrl: "https://www.json.org/json-en.html",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "toml",
        name: "TOML",
        category: "dataformat",
        icon: "⚙️",
        shortDesc: "Tom's Obvious Minimal Language",
        description: "TOML är ett konfigurationsfilformat som är lätt att läsa. Populärt i Rust (Cargo.toml) och Python (pyproject.toml).",
        installation: {
            pip: "pip install toml",
            npm: "npm install @iarna/toml"
        },
        useCases: ["Python projects (pyproject.toml)", "Rust projects (Cargo.toml)", "Hugo sites", "Konfigurationsfiler"],
        keyFeatures: ["Explicit typning", "Nested tables", "Datum/tid-stöd", "Inline tables"],
        officialUrl: "https://toml.io",
        docsUrl: "https://toml.io/en/v1.0.0",
        flashcardCount: 10,
        quizCount: 6
    },
    // CONTAINERS
    {
        slug: "docker",
        name: "Docker",
        category: "containers",
        icon: "🐳",
        shortDesc: "Container platform",
        description: "Docker är en plattform för att bygga, distribuera och köra applikationer i containers. Isolerar applikationer från underliggande system.",
        installation: {
            apt: "sudo apt install docker.io",
            brew: "brew install docker"
        },
        useCases: ["Applikationscontainers", "Microservices", "Utvecklingsmiljöer", "CI/CD builds", "Deployment"],
        keyFeatures: ["Dockerfile", "Docker Compose", "Multi-stage builds", "Volumes", "Networks", "Registry"],
        officialUrl: "https://www.docker.com",
        docsUrl: "https://docs.docker.com",
        flashcardCount: 25,
        quizCount: 20
    },
    {
        slug: "podman",
        name: "Podman",
        category: "containers",
        icon: "🦭",
        shortDesc: "Daemonless container engine",
        description: "Podman är ett Docker-alternativ som kör containers utan daemon. Rootless by default, kompatibelt med Docker CLI.",
        installation: {
            apt: "sudo apt install podman",
            brew: "brew install podman"
        },
        useCases: ["Rootless containers", "Docker replacement", "Pod management", "Systemd integration"],
        keyFeatures: ["Daemonless", "Rootless", "Pod support", "Docker-kompatibel", "Systemd integration"],
        officialUrl: "https://podman.io",
        docsUrl: "https://docs.podman.io",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "containerd",
        name: "containerd",
        category: "containers",
        icon: "📦",
        shortDesc: "Container runtime",
        description: "containerd är en industri-standard container runtime som hanterar hela container-livscykeln. Används av Docker och Kubernetes.",
        installation: {
            apt: "sudo apt install containerd"
        },
        useCases: ["Kubernetes runtime", "Docker backend", "Container management", "Image management"],
        keyFeatures: ["OCI-kompatibel", "Snapshots", "CRI support", "Plugin architecture"],
        officialUrl: "https://containerd.io",
        docsUrl: "https://containerd.io/docs/",
        flashcardCount: 8,
        quizCount: 5
    },
    // ORCHESTRATION
    {
        slug: "kubernetes",
        name: "Kubernetes",
        category: "orchestration",
        icon: "☸️",
        shortDesc: "Container orchestration",
        description: "Kubernetes (K8s) är en open-source plattform för att automatisera deployment, skalning och hantering av containeriserade applikationer.",
        installation: {
            brew: "brew install kubectl",
            other: "curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
        },
        useCases: ["Container orchestration", "Microservices", "Auto-scaling", "Self-healing", "Rolling updates"],
        keyFeatures: ["Pods", "Services", "Deployments", "ConfigMaps", "Secrets", "Ingress", "Namespaces"],
        officialUrl: "https://kubernetes.io",
        docsUrl: "https://kubernetes.io/docs/",
        flashcardCount: 30,
        quizCount: 25
    },
    {
        slug: "helm",
        name: "Helm",
        category: "orchestration",
        icon: "⎈",
        shortDesc: "Kubernetes package manager",
        description: "Helm är pakethanteraren för Kubernetes. Använder charts för att definiera, installera och uppgradera Kubernetes-applikationer.",
        installation: {
            brew: "brew install helm",
            other: "curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash"
        },
        useCases: ["Application packaging", "Release management", "Dependency management", "Templating"],
        keyFeatures: ["Charts", "Values", "Releases", "Repositories", "Hooks", "Subcharts"],
        officialUrl: "https://helm.sh",
        docsUrl: "https://helm.sh/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "docker-compose",
        name: "Docker Compose",
        category: "orchestration",
        icon: "🎼",
        shortDesc: "Multi-container Docker",
        description: "Docker Compose definierar och kör multi-container Docker-applikationer med en YAML-fil. Perfekt för lokal utveckling.",
        installation: {
            apt: "sudo apt install docker-compose-plugin",
            brew: "brew install docker-compose"
        },
        useCases: ["Lokal utveckling", "Multi-service apps", "Testing environments", "CI/CD"],
        keyFeatures: ["Services", "Networks", "Volumes", "Environment variables", "Depends_on", "Profiles"],
        officialUrl: "https://docs.docker.com/compose/",
        docsUrl: "https://docs.docker.com/compose/compose-file/",
        flashcardCount: 18,
        quizCount: 12
    },
    // LINUX & CLI
    {
        slug: "bash",
        name: "Bash",
        category: "linux",
        icon: "💻",
        shortDesc: "Bourne Again Shell",
        description: "Bash är standard shell i de flesta Linux-distributioner. Kraftfullt scripting-språk för automation och systemadministration.",
        installation: {
            apt: "sudo apt install bash",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Shell scripting", "Automation", "System administration", "CI/CD scripts", "Cron jobs"],
        keyFeatures: ["Variables", "Functions", "Conditionals", "Loops", "Pipes", "Redirections", "Subshells"],
        officialUrl: "https://www.gnu.org/software/bash/",
        docsUrl: "https://www.gnu.org/software/bash/manual/",
        flashcardCount: 20,
        quizCount: 15
    },
    {
        slug: "alpine",
        name: "Alpine Linux",
        category: "linux",
        icon: "🏔️",
        shortDesc: "Minimal Linux distro",
        description: "Alpine Linux är en säkerhetsfokuserad, lättviktig Linux-distribution. Populär som bas-image för Docker containers (~5MB).",
        installation: {
            other: "docker pull alpine:latest"
        },
        useCases: ["Docker base images", "Minimal containers", "Edge computing", "Security-focused systems"],
        keyFeatures: ["musl libc", "BusyBox", "apk package manager", "~5MB storlek", "Security-hardened"],
        officialUrl: "https://alpinelinux.org",
        docsUrl: "https://wiki.alpinelinux.org",
        flashcardCount: 10,
        quizCount: 8
    },
    {
        slug: "systemd",
        name: "systemd",
        category: "linux",
        icon: "⚙️",
        shortDesc: "System & service manager",
        description: "systemd är init-systemet och service manager för moderna Linux-distributioner. Hanterar tjänster, logging och boot-processen.",
        installation: {
            other: "Förinstallerat på de flesta moderna Linux-distros"
        },
        useCases: ["Service management", "Boot process", "Logging (journald)", "Timers (cron replacement)", "Socket activation"],
        keyFeatures: ["Units", "Targets", "journalctl", "systemctl", "Timers", "Socket activation"],
        officialUrl: "https://systemd.io",
        docsUrl: "https://www.freedesktop.org/software/systemd/man/",
        flashcardCount: 15,
        quizCount: 12
    },
    {
        slug: "nginx",
        name: "Nginx",
        category: "linux",
        icon: "🌐",
        shortDesc: "Web server & reverse proxy",
        description: "Nginx är en högpresterande web server, reverse proxy och load balancer. Används av miljontals webbplatser världen över.",
        installation: {
            apt: "sudo apt install nginx",
            brew: "brew install nginx"
        },
        useCases: ["Web server", "Reverse proxy", "Load balancer", "SSL termination", "Static file serving", "API gateway"],
        keyFeatures: ["Event-driven", "Low memory", "Upstream", "Location blocks", "SSL/TLS", "Caching"],
        officialUrl: "https://nginx.org",
        docsUrl: "https://nginx.org/en/docs/",
        flashcardCount: 20,
        quizCount: 15
    },
    // PYTHON
    {
        slug: "python-kwargs",
        name: "**kwargs",
        category: "python",
        icon: "🐍",
        shortDesc: "Keyword arguments",
        description: "**kwargs låter funktioner ta emot godtyckligt antal keyword arguments som en dictionary. Centralt koncept i Python.",
        installation: {
            other: "Inbyggt i Python"
        },
        useCases: ["Flexibla funktioner", "Wrapper functions", "Decorators", "API design", "Config passing"],
        keyFeatures: ["Dictionary unpacking", "Valfria parametrar", "Forwarding arguments", "Kombination med *args"],
        docsUrl: "https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments",
        flashcardCount: 8,
        quizCount: 6
    },
    {
        slug: "python-classes",
        name: "Python Classes",
        category: "python",
        icon: "🏛️",
        shortDesc: "Object-Oriented Python",
        description: "Python classes är grunden för objektorienterad programmering. Definierar objekt med attribut och metoder.",
        installation: {
            other: "Inbyggt i Python"
        },
        useCases: ["OOP", "Data modeling", "Encapsulation", "Inheritance", "Polymorphism"],
        keyFeatures: ["__init__", "self", "Inheritance", "Class methods", "Static methods", "Properties", "Dunder methods"],
        docsUrl: "https://docs.python.org/3/tutorial/classes.html",
        flashcardCount: 15,
        quizCount: 12
    },
    {
        slug: "python-decorators",
        name: "Decorators",
        category: "python",
        icon: "🎀",
        shortDesc: "Function wrappers",
        description: "Decorators i Python är ett designmönster som låter dig modifiera funktioners beteende. Används för logging, caching, auth etc.",
        installation: {
            other: "Inbyggt i Python"
        },
        useCases: ["Logging", "Timing", "Caching", "Authentication", "Rate limiting", "Validation"],
        keyFeatures: ["@syntax", "Wrapper functions", "functools.wraps", "Chaining decorators", "Class decorators"],
        docsUrl: "https://docs.python.org/3/glossary.html#term-decorator",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "virtualenv",
        name: "virtualenv",
        category: "python",
        icon: "📦",
        shortDesc: "Python virtual environments",
        description: "Virtual environments isolerar Python-projekt med egna dependencies. Förhindrar konflikter mellan projektens paket.",
        installation: {
            pip: "pip install virtualenv",
            other: "python -m venv (inbyggt)"
        },
        useCases: ["Project isolation", "Dependency management", "Testing", "Development environments"],
        keyFeatures: ["Isolerade environments", "requirements.txt", "activate/deactivate", "venv vs virtualenv"],
        docsUrl: "https://docs.python.org/3/library/venv.html",
        flashcardCount: 8,
        quizCount: 5
    },
    // VIRTUALIZATION
    {
        slug: "virtualbox",
        name: "VirtualBox",
        category: "virtualization",
        icon: "📟",
        shortDesc: "Desktop virtualization",
        description: "VirtualBox är en gratis virtualiseringsplattform från Oracle för att köra virtuella maskiner på din dator.",
        installation: {
            apt: "sudo apt install virtualbox",
            brew: "brew install --cask virtualbox"
        },
        useCases: ["Lokala VMs", "Testing", "Utvecklingsmiljöer", "Multi-OS testing", "Snapshots"],
        keyFeatures: ["Cross-platform", "Snapshots", "Shared folders", "Networking modes", "Guest additions"],
        officialUrl: "https://www.virtualbox.org",
        docsUrl: "https://www.virtualbox.org/manual/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "vagrant",
        name: "Vagrant",
        category: "virtualization",
        icon: "📦",
        shortDesc: "VM workflow automation",
        description: "Vagrant automatiserar skapande och hantering av virtuella utvecklingsmiljöer. Infrastructure as Code för VMs.",
        installation: {
            brew: "brew install vagrant",
            other: "https://www.vagrantup.com/downloads"
        },
        useCases: ["Reproducerbara miljöer", "Team development", "Testing infrastructure", "Local Kubernetes"],
        keyFeatures: ["Vagrantfile", "Boxes", "Provisioning", "Multi-machine", "Synced folders", "Port forwarding"],
        officialUrl: "https://www.vagrantup.com",
        docsUrl: "https://developer.hashicorp.com/vagrant/docs",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "kvm",
        name: "KVM",
        category: "virtualization",
        icon: "🖥️",
        shortDesc: "Linux kernel virtualization",
        description: "KVM (Kernel-based Virtual Machine) är en Linux-kernelmodul för full virtualisering. Höga prestanda, används i molntjänster.",
        installation: {
            apt: "sudo apt install qemu-kvm libvirt-daemon-system"
        },
        useCases: ["Server virtualization", "Cloud infrastructure", "High-performance VMs", "Live migration"],
        keyFeatures: ["Hardware-assisted", "QEMU integration", "libvirt", "Live migration", "Snapshots"],
        officialUrl: "https://www.linux-kvm.org",
        docsUrl: "https://www.linux-kvm.org/page/Documents",
        flashcardCount: 10,
        quizCount: 6
    },
    // CLOUD & IAC
    {
        slug: "terraform",
        name: "Terraform",
        category: "cloud",
        icon: "🏗️",
        shortDesc: "Infrastructure as Code",
        description: "Terraform är ett IaC-verktyg från HashiCorp för att bygga, ändra och versionshantera infrastruktur säkert och effektivt.",
        installation: {
            brew: "brew install terraform",
            other: "https://developer.hashicorp.com/terraform/downloads"
        },
        useCases: ["Cloud provisioning", "Multi-cloud", "Infrastructure versioning", "State management"],
        keyFeatures: ["HCL syntax", "Providers", "State", "Modules", "Plan/Apply", "Workspaces"],
        officialUrl: "https://www.terraform.io",
        docsUrl: "https://developer.hashicorp.com/terraform/docs",
        flashcardCount: 20,
        quizCount: 15
    },
    {
        slug: "ansible",
        name: "Ansible",
        category: "cloud",
        icon: "🔧",
        shortDesc: "Configuration management",
        description: "Ansible är ett agentless automatiseringsverktyg för configuration management, application deployment och task automation.",
        installation: {
            pip: "pip install ansible",
            apt: "sudo apt install ansible"
        },
        useCases: ["Configuration management", "App deployment", "Orchestration", "Provisioning", "Security compliance"],
        keyFeatures: ["Agentless", "YAML playbooks", "Inventory", "Modules", "Roles", "Galaxy", "Idempotent"],
        officialUrl: "https://www.ansible.com",
        docsUrl: "https://docs.ansible.com",
        flashcardCount: 18,
        quizCount: 12
    },
    {
        slug: "aws-cli",
        name: "AWS CLI",
        category: "cloud",
        icon: "☁️",
        shortDesc: "Amazon Web Services CLI",
        description: "AWS CLI är kommandoradsverktyget för att hantera AWS-tjänster. Automatisera och scripta din molninfrastruktur.",
        installation: {
            pip: "pip install awscli",
            brew: "brew install awscli"
        },
        useCases: ["AWS management", "Automation", "CI/CD integration", "Scripting", "Resource management"],
        keyFeatures: ["Profiles", "Output formats", "S3 sync", "Query filtering", "MFA support"],
        officialUrl: "https://aws.amazon.com/cli/",
        docsUrl: "https://docs.aws.amazon.com/cli/",
        flashcardCount: 15,
        quizCount: 10
    },
    // CI/CD
    {
        slug: "github-actions",
        name: "GitHub Actions",
        category: "cicd",
        icon: "🐙",
        shortDesc: "GitHub CI/CD",
        description: "GitHub Actions automatiserar software workflows direkt i GitHub. Build, test och deploy från ditt repository.",
        installation: {
            other: "Aktiveras i .github/workflows/"
        },
        useCases: ["CI/CD pipelines", "Automated testing", "Deployment", "Issue management", "Code review automation"],
        keyFeatures: ["Workflows", "Jobs", "Steps", "Actions marketplace", "Matrix builds", "Secrets", "Environments"],
        officialUrl: "https://github.com/features/actions",
        docsUrl: "https://docs.github.com/en/actions",
        flashcardCount: 18,
        quizCount: 12
    },
    {
        slug: "gitlab-ci",
        name: "GitLab CI/CD",
        category: "cicd",
        icon: "🦊",
        shortDesc: "GitLab pipelines",
        description: "GitLab CI/CD är inbyggt i GitLab för automatiserad build, test och deployment. Definieras i .gitlab-ci.yml.",
        installation: {
            other: "Aktiveras med .gitlab-ci.yml"
        },
        useCases: ["CI/CD pipelines", "Auto DevOps", "Container registry", "Deployment", "Security scanning"],
        keyFeatures: ["Stages", "Jobs", "Runners", "Artifacts", "Environments", "Auto DevOps", "Parent-child pipelines"],
        officialUrl: "https://docs.gitlab.com/ee/ci/",
        docsUrl: "https://docs.gitlab.com/ee/ci/yaml/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "jenkins",
        name: "Jenkins",
        category: "cicd",
        icon: "🎩",
        shortDesc: "Automation server",
        description: "Jenkins är en open-source automation server för att bygga, testa och deploya software. Extremt utbyggbart med plugins.",
        installation: {
            apt: "sudo apt install jenkins",
            brew: "brew install jenkins"
        },
        useCases: ["CI/CD pipelines", "Build automation", "Deployment", "Scheduled jobs", "Multi-platform builds"],
        keyFeatures: ["Pipelines (Jenkinsfile)", "Plugins", "Distributed builds", "Blue Ocean UI", "Credentials management"],
        officialUrl: "https://www.jenkins.io",
        docsUrl: "https://www.jenkins.io/doc/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "argocd",
        name: "ArgoCD",
        category: "cicd",
        icon: "🐙",
        shortDesc: "GitOps for Kubernetes",
        description: "ArgoCD är ett deklarativt GitOps continuous delivery-verktyg för Kubernetes. Synkar Git-state till klustret.",
        installation: {
            other: "kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml"
        },
        useCases: ["GitOps", "Kubernetes deployments", "Multi-cluster", "Application management", "Rollbacks"],
        keyFeatures: ["GitOps", "Application CRD", "Sync", "Health status", "Rollback", "SSO", "RBAC"],
        officialUrl: "https://argo-cd.readthedocs.io",
        docsUrl: "https://argo-cd.readthedocs.io/en/stable/",
        flashcardCount: 12,
        quizCount: 8
    },
    // MONITORING
    {
        slug: "prometheus",
        name: "Prometheus",
        category: "monitoring",
        icon: "🔥",
        shortDesc: "Metrics & monitoring",
        description: "Prometheus är ett monitoring och alerting toolkit. Pull-baserat system med kraftfull query language (PromQL).",
        installation: {
            brew: "brew install prometheus",
            other: "docker run prom/prometheus"
        },
        useCases: ["Metrics collection", "Alerting", "Kubernetes monitoring", "Application monitoring", "Infrastructure monitoring"],
        keyFeatures: ["Pull-based", "PromQL", "Alertmanager", "Service discovery", "Exporters", "Federation"],
        officialUrl: "https://prometheus.io",
        docsUrl: "https://prometheus.io/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "grafana",
        name: "Grafana",
        category: "monitoring",
        icon: "📊",
        shortDesc: "Visualization & dashboards",
        description: "Grafana är en plattform för monitoring och observability. Visualisera metrics, logs och traces med vackra dashboards.",
        installation: {
            apt: "sudo apt install grafana",
            brew: "brew install grafana"
        },
        useCases: ["Dashboards", "Alerting", "Data visualization", "Log analysis", "Metrics exploration"],
        keyFeatures: ["Datasources", "Dashboards", "Panels", "Alerting", "Annotations", "Variables", "Plugins"],
        officialUrl: "https://grafana.com",
        docsUrl: "https://grafana.com/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    // NETWORK
    {
        slug: "ssh",
        name: "SSH",
        category: "network",
        icon: "🔐",
        shortDesc: "Secure Shell",
        description: "SSH (Secure Shell) är ett protokoll för säker kommunikation över osäkra nätverk. Standard för remote access.",
        installation: {
            apt: "sudo apt install openssh-client",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Remote access", "File transfer (SCP/SFTP)", "Tunneling", "Port forwarding", "Git authentication"],
        keyFeatures: ["Public key auth", "Config file", "Agent forwarding", "Tunneling", "Jump hosts", "SCP/SFTP"],
        docsUrl: "https://www.openssh.com/manual.html",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "ssl-tls",
        name: "SSL/TLS",
        category: "network",
        icon: "🔒",
        shortDesc: "Transport Layer Security",
        description: "TLS (och dess föregångare SSL) säkrar kommunikation över internet. Grund för HTTPS och säker datautbyte.",
        installation: {
            apt: "sudo apt install openssl"
        },
        useCases: ["HTTPS", "Secure APIs", "Email encryption", "VPN", "Certificate management"],
        keyFeatures: ["Certificates", "Certificate chains", "Let's Encrypt", "Certificate authorities", "TLS handshake"],
        officialUrl: "https://www.openssl.org",
        docsUrl: "https://www.openssl.org/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    // DATABASE
    {
        slug: "postgresql",
        name: "PostgreSQL",
        category: "database",
        icon: "🐘",
        shortDesc: "Relational database",
        description: "PostgreSQL är en kraftfull, open-source relationsdatabas med avancerade features som JSON-stöd och full-text search.",
        installation: {
            apt: "sudo apt install postgresql",
            brew: "brew install postgresql"
        },
        useCases: ["Web applications", "Data warehousing", "Geospatial data", "OLTP", "Analytics"],
        keyFeatures: ["ACID", "JSON/JSONB", "Full-text search", "Extensions", "Replication", "Partitioning"],
        officialUrl: "https://www.postgresql.org",
        docsUrl: "https://www.postgresql.org/docs/",
        flashcardCount: 18,
        quizCount: 12
    },
    {
        slug: "redis",
        name: "Redis",
        category: "database",
        icon: "🔴",
        shortDesc: "In-memory data store",
        description: "Redis är en in-memory data structure store. Används som databas, cache och message broker med extremt snabb prestanda.",
        installation: {
            apt: "sudo apt install redis-server",
            brew: "brew install redis"
        },
        useCases: ["Caching", "Session storage", "Real-time analytics", "Message queues", "Leaderboards", "Rate limiting"],
        keyFeatures: ["In-memory", "Data structures", "Pub/Sub", "Lua scripting", "Cluster", "Persistence"],
        officialUrl: "https://redis.io",
        docsUrl: "https://redis.io/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    // GIT
    {
        slug: "git",
        name: "Git",
        category: "cicd",
        icon: "📚",
        shortDesc: "Version control",
        description: "Git är det distribuerade versionshanteringssystemet som används av miljontals utvecklare. Grund för GitHub, GitLab etc.",
        installation: {
            apt: "sudo apt install git",
            brew: "brew install git"
        },
        useCases: ["Version control", "Collaboration", "Code review", "Branch management", "CI/CD integration"],
        keyFeatures: ["Branches", "Merge/Rebase", "Commits", "Tags", "Remote repos", "Hooks", "Submodules"],
        officialUrl: "https://git-scm.com",
        docsUrl: "https://git-scm.com/doc",
        flashcardCount: 20,
        quizCount: 15
    },
]
