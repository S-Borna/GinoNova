"use client"

/**
 * FastTrack - DevOps Tools Library
 *
 * Complete reference for all DevOps tools with:
 * - Tool cards with info, installation, usage
 * - Flashcards & Quiz for each tool
 * - Combine mode to study multiple tools
 * - Search & filter by category
 */

import * as React from "react"
import { useState, useMemo } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { cn } from "@/lib/utils"
import {
    Search,
    BookOpen,
    Brain,
    CheckSquare,
    Square,
    ArrowRight,
    Combine,
    X,
    Sparkles,
    ExternalLink,
    Terminal,
    Box,
    Server,
    Cloud,
    Database,
    GitBranch,
    Shield,
    Code,
    Layers,
    Monitor,
    Cpu,
    HardDrive,
    Network,
    Lock,
    Zap,
    FileJson,
    FileCode,
    Settings,
    Container,
} from "lucide-react"

/* ============================================================================
   TOOLS DATA - Complete DevOps Tools Library
   ============================================================================ */

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

/* ============================================================================
   ICON COMPONENT MAPPING
   ============================================================================ */

const CATEGORY_ICONS: Record<string, React.ElementType> = {
    dataformat: FileJson,
    containers: Box,
    orchestration: Container,
    linux: Terminal,
    python: Code,
    virtualization: Monitor,
    cloud: Cloud,
    cicd: GitBranch,
    monitoring: Cpu,
    network: Network,
    database: Database,
    security: Shield,
}

/* ============================================================================
   FASTTRACK PAGE COMPONENT
   ============================================================================ */

export default function FastTrackPage() {
    const router = useRouter()
    const [searchQuery, setSearchQuery] = useState("")
    const [selectedCategory, setSelectedCategory] = useState("all")

    // Combine mode
    const [combineMode, setCombineMode] = useState(false)
    const [selectedTools, setSelectedTools] = useState<Set<string>>(new Set())

    // Filter tools
    const filteredTools = useMemo(() => {
        return TOOLS_DATA.filter(tool => {
            const matchesSearch =
                tool.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                tool.shortDesc.toLowerCase().includes(searchQuery.toLowerCase()) ||
                tool.category.toLowerCase().includes(searchQuery.toLowerCase())

            const matchesCategory = selectedCategory === "all" || tool.category === selectedCategory

            return matchesSearch && matchesCategory
        })
    }, [searchQuery, selectedCategory])

    function toggleTool(slug: string) {
        if (!combineMode) {
            // Navigate to tool detail
            router.push(`/fasttrack/${slug}`)
            return
        }

        setSelectedTools(prev => {
            const newSet = new Set(prev)
            if (newSet.has(slug)) {
                newSet.delete(slug)
            } else {
                newSet.add(slug)
            }
            return newSet
        })
    }

    function exitCombineMode() {
        setCombineMode(false)
        setSelectedTools(new Set())
    }

    // Stats for selected tools
    const selectedStats = TOOLS_DATA
        .filter(t => selectedTools.has(t.slug))
        .reduce(
            (acc, t) => ({
                flashcards: acc.flashcards + t.flashcardCount,
                quiz: acc.quiz + t.quizCount,
            }),
            { flashcards: 0, quiz: 0 }
        )

    // Total stats
    const totalStats = TOOLS_DATA.reduce(
        (acc, t) => ({
            flashcards: acc.flashcards + t.flashcardCount,
            quiz: acc.quiz + t.quizCount,
            tools: acc.tools + 1,
        }),
        { flashcards: 0, quiz: 0, tools: 0 }
    )

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <div className="flex items-center gap-3 mb-2">
                        <div className="p-2 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600">
                            <Zap className="w-6 h-6 text-white" />
                        </div>
                        <h1 className="text-3xl font-bold">FastTrack</h1>
                    </div>
                    <p className="text-zinc-400">
                        Komplett verktygsbibliotek för DevOps - lär dig med Flashcards & Quiz
                    </p>
                </div>

                {/* Stats Bar */}
                <div className="grid grid-cols-3 gap-4 mb-8">
                    <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4 text-center">
                        <p className="text-2xl font-bold text-amber-400">{totalStats.tools}</p>
                        <p className="text-sm text-zinc-500">Verktyg</p>
                    </div>
                    <div className="bg-zinc-900/60 border border-purple-500/30 rounded-xl p-4 text-center">
                        <p className="text-2xl font-bold text-purple-400">{totalStats.flashcards}</p>
                        <p className="text-sm text-zinc-500">Flashcards</p>
                    </div>
                    <div className="bg-zinc-900/60 border border-blue-500/30 rounded-xl p-4 text-center">
                        <p className="text-2xl font-bold text-blue-400">{totalStats.quiz}</p>
                        <p className="text-sm text-zinc-500">Quiz-frågor</p>
                    </div>
                </div>

                {/* Search & Filter */}
                <div className="flex flex-col md:flex-row gap-4 mb-6">
                    {/* Search */}
                    <div className="relative flex-1">
                        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                        <input
                            type="text"
                            placeholder="Sök verktyg..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className={cn(
                                "w-full pl-12 pr-4 py-3 rounded-xl",
                                "bg-zinc-900 border border-zinc-800",
                                "text-white placeholder-zinc-500",
                                "focus:outline-none focus:border-amber-500/50"
                            )}
                        />
                    </div>

                    {/* Combine Button */}
                    {!combineMode ? (
                        <button
                            onClick={() => setCombineMode(true)}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-xl",
                                "bg-gradient-to-r from-amber-600 to-orange-600",
                                "hover:from-amber-500 hover:to-orange-500",
                                "font-medium transition-all"
                            )}
                        >
                            <Combine className="w-5 h-5" />
                            Kombinera verktyg
                        </button>
                    ) : (
                        <button
                            onClick={exitCombineMode}
                            className={cn(
                                "flex items-center gap-2 px-6 py-3 rounded-xl",
                                "bg-zinc-800 border border-zinc-700",
                                "hover:bg-zinc-700",
                                "font-medium transition-all"
                            )}
                        >
                            <X className="w-5 h-5" />
                            Avbryt
                        </button>
                    )}
                </div>

                {/* Category Filter */}
                <div className="flex flex-wrap gap-2 mb-8">
                    {TOOL_CATEGORIES.map((cat) => {
                        const Icon = cat.icon
                        const isActive = selectedCategory === cat.id
                        return (
                            <button
                                key={cat.id}
                                onClick={() => setSelectedCategory(cat.id)}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-lg",
                                    "transition-all duration-200",
                                    isActive
                                        ? "bg-amber-500/20 text-amber-400 border border-amber-500/30"
                                        : "bg-zinc-900 text-zinc-400 border border-zinc-800 hover:border-zinc-700"
                                )}
                            >
                                <Icon className="w-4 h-4" />
                                {cat.label}
                            </button>
                        )
                    })}
                </div>

                {/* Combine Mode Selection Bar */}
                {combineMode && selectedTools.size > 0 && (
                    <div className={cn(
                        "fixed bottom-0 left-0 right-0 z-50",
                        "bg-zinc-900/95 backdrop-blur-lg border-t border-amber-500/30",
                        "p-4"
                    )}>
                        <div className="max-w-7xl mx-auto flex items-center justify-between">
                            <div className="flex items-center gap-4">
                                <div className="text-sm">
                                    <span className="text-amber-400 font-bold">{selectedTools.size}</span>
                                    <span className="text-zinc-400"> verktyg valda</span>
                                </div>
                                <div className="text-sm text-zinc-500">
                                    {selectedStats.flashcards} flashcards • {selectedStats.quiz} quiz-frågor
                                </div>
                            </div>
                            <div className="flex gap-3">
                                <Link
                                    href={`/fasttrack/session?tools=${Array.from(selectedTools).join(",")}&mode=flashcards`}
                                    className={cn(
                                        "flex items-center gap-2 px-6 py-2.5 rounded-xl",
                                        "bg-purple-600 hover:bg-purple-500",
                                        "font-medium transition-all"
                                    )}
                                >
                                    <BookOpen className="w-4 h-4" />
                                    Flashcards
                                </Link>
                                <Link
                                    href={`/fasttrack/session?tools=${Array.from(selectedTools).join(",")}&mode=quiz`}
                                    className={cn(
                                        "flex items-center gap-2 px-6 py-2.5 rounded-xl",
                                        "bg-blue-600 hover:bg-blue-500",
                                        "font-medium transition-all"
                                    )}
                                >
                                    <Brain className="w-4 h-4" />
                                    Quiz
                                </Link>
                            </div>
                        </div>
                    </div>
                )}

                {/* Tools Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 pb-24">
                    {filteredTools.map((tool) => {
                        const isSelected = selectedTools.has(tool.slug)
                        const CategoryIcon = CATEGORY_ICONS[tool.category] || Layers

                        return (
                            <div
                                key={tool.slug}
                                onClick={() => toggleTool(tool.slug)}
                                className={cn(
                                    "group relative rounded-2xl p-5 cursor-pointer",
                                    "bg-zinc-900/60 border transition-all duration-300",
                                    combineMode && isSelected
                                        ? "border-amber-500 bg-amber-500/10 shadow-[0_0_20px_rgba(245,158,11,0.2)]"
                                        : "border-zinc-800 hover:border-zinc-700 hover:bg-zinc-800/60"
                                )}
                            >
                                {/* Selection Checkbox (Combine Mode) */}
                                {combineMode && (
                                    <div className="absolute top-4 right-4">
                                        {isSelected ? (
                                            <CheckSquare className="w-5 h-5 text-amber-400" />
                                        ) : (
                                            <Square className="w-5 h-5 text-zinc-600" />
                                        )}
                                    </div>
                                )}

                                {/* Tool Header */}
                                <div className="flex items-start gap-4 mb-4">
                                    <div className={cn(
                                        "w-14 h-14 rounded-xl flex items-center justify-center text-2xl",
                                        "bg-gradient-to-br from-zinc-800 to-zinc-900",
                                        "border border-zinc-700"
                                    )}>
                                        {tool.icon}
                                    </div>
                                    <div className="flex-1 min-w-0">
                                        <h3 className="font-semibold text-white text-lg truncate">
                                            {tool.name}
                                        </h3>
                                        <p className="text-sm text-zinc-400 truncate">
                                            {tool.shortDesc}
                                        </p>
                                    </div>
                                </div>

                                {/* Category Badge */}
                                <div className="flex items-center gap-2 mb-3">
                                    <CategoryIcon className="w-3.5 h-3.5 text-zinc-500" />
                                    <span className="text-xs text-zinc-500 capitalize">
                                        {TOOL_CATEGORIES.find(c => c.id === tool.category)?.label || tool.category}
                                    </span>
                                </div>

                                {/* Stats */}
                                <div className="flex items-center gap-4">
                                    <div className="flex items-center gap-1.5">
                                        <BookOpen className="w-4 h-4 text-purple-400" />
                                        <span className="text-sm text-zinc-400">{tool.flashcardCount}</span>
                                    </div>
                                    <div className="flex items-center gap-1.5">
                                        <Brain className="w-4 h-4 text-blue-400" />
                                        <span className="text-sm text-zinc-400">{tool.quizCount}</span>
                                    </div>
                                    {tool.officialUrl && (
                                        <ExternalLink className="w-4 h-4 text-zinc-600 ml-auto" />
                                    )}
                                </div>

                                {/* Hover Arrow (non-combine mode) */}
                                {!combineMode && (
                                    <div className={cn(
                                        "absolute top-1/2 right-4 -translate-y-1/2",
                                        "opacity-0 group-hover:opacity-100 transition-opacity"
                                    )}>
                                        <ArrowRight className="w-5 h-5 text-amber-400" />
                                    </div>
                                )}
                            </div>
                        )
                    })}
                </div>

                {/* Empty State */}
                {filteredTools.length === 0 && (
                    <div className="text-center py-20">
                        <Search className="w-16 h-16 text-zinc-700 mx-auto mb-4" />
                        <p className="text-zinc-400 text-lg">
                            Inga verktyg matchar din sökning
                        </p>
                        <button
                            onClick={() => {
                                setSearchQuery("")
                                setSelectedCategory("all")
                            }}
                            className="mt-4 text-amber-400 hover:text-amber-300"
                        >
                            Rensa filter
                        </button>
                    </div>
                )}
            </div>
        </div>
    )
}
