"""
Dallas FAQ Database - Förtränade svar baserade på plattformens innehåll.
Ingen GPT-kostnad - endast lokala svar från sidans faktiska innehåll.

Uppdaterad: 2025-12-06 - Täcker alla moduler och topics
"""

from typing import Optional, List, Tuple
import re

# FAQ-databas: (keywords, question_patterns, answer)
# Keywords används för snabb filtrering, patterns för bättre matching
FAQ_DATABASE: List[Tuple[List[str], List[str], str]] = [

    # ==========================================================================
    # PLATTFORMEN - Allmänna frågor
    # ==========================================================================
    (
        ["ginonova", "plattform", "vad är", "hur funkar", "sida", "sidan"],
        ["vad är ginonova", "hur funkar sidan", "vad kan jag göra här"],
        """GinoNova är en lärplattform för DevOps! 🚀

Här kan du:
• **Camp DevOps** - Strukturerade moduler med tasks och XP
• **SkillsMaps** - Djupa lärvägar med 20 nodes per ämne
• **Studyflow** - Fokuserade studiesessioner
• **Skillpath Board** - Se din progress och planera din väg

Börja med att välja en modul i Camp DevOps eller utforska SkillsMaps!"""
    ),

    (
        ["camp", "modul", "moduler", "bootcamp"],
        ["vad är camp devops", "hur funkar moduler", "vilka moduler finns"],
        """**Camp DevOps** innehåller strukturerade lärmoduler:

📚 **Tillgängliga moduler:**
• Environment Setup - Kom igång med din utvecklingsmiljö
• Linux Mastery - Behärska Linux från grunden
• Shell Scripting - Automatisera med Bash
• Git & Workflows - Versionhantering och samarbete
• Python for DevOps - Scripting och automation
• AWS Core - Molntjänster och infrastruktur
• Docker - Containerisering
• Kubernetes - Container orchestration
• Terraform - Infrastructure as Code
• CI/CD Pipelines - Automatiserad deployment

Varje modul har tasks som ger XP när du slutför dem!"""
    ),

    (
        ["skillsmap", "skillsmaps", "lärvä", "nodes", "nod"],
        ["vad är skillsmaps", "hur funkar skillsmaps", "skillsmap"],
        """**SkillsMaps** är djupa lärvägar med 20 nodes per ämne.

Varje node innehåller:
• Detaljerad teori och koncept
• Kodexempel och kommandon
• Praktiska övningar
• Pro tips från erfarna DevOps-ingenjörer

Tillgängliga SkillsMaps: Linux, Python, Docker, Kubernetes, AWS, Terraform, Git, CI/CD, och fler!

Gå till SkillsMaps i menyn för att börja."""
    ),

    (
        ["studyflow", "studie", "session", "fokus"],
        ["vad är studyflow", "hur funkar studyflow", "studiesession"],
        """**Studyflow** hjälper dig fokusera på lärandet.

Funktioner:
• Starta fokuserade studiesessioner
• Spåra tid per modul
• Pomodoro-liknande intervaller
• Se din studiestatistik

Gå till Studyflow i menyn för att starta en session!"""
    ),

    (
        ["xp", "poäng", "level", "nivå", "progress", "framsteg"],
        ["hur får jag xp", "vad är xp", "hur fungerar poäng", "level"],
        """**XP-systemet** belönar ditt lärande!

• Slutför tasks -> Få XP
• Svara rätt på quiz -> Bonus XP
• Håll streaks -> Extra belöningar

Din XP syns på Dashboard och i din profil. Ju mer du lär dig, desto högre level!"""
    ),

    (
        ["dallas", "du", "vem", "assistent", "ai", "hjälp"],
        ["vem är du", "vad är dallas", "vad kan du hjälpa med"],
        """Jag är **Dallas** 🐺 - din guide på GinoNova!

Jag kan hjälpa dig med:
• Förklara vad som finns på plattformen
• Guida dig till rätt modul eller SkillsMap
• Svara på frågor om plattformens innehåll

Ställ en fråga så hjälper jag dig hitta rätt!"""
    ),

    # ==========================================================================
    # LINUX MASTERY - 20 nodes
    # ==========================================================================
    (
        ["process", "processer", "ps", "top", "htop", "kill", "signal"],
        ["process", "processer", "hur dödar jag process", "visa processer", "ps aux"],
        """**Process Management** täcks i Linux Mastery -> Node 1.

Innehåll:
• `ps`, `top`, `htop` - Visa processer
• `kill`, `killall`, `pkill` - Avsluta processer
• Process states (Running, Sleeping, Zombie)
• Signals (SIGTERM, SIGKILL)
• Background/foreground jobs

Gå till: **SkillsMaps -> Linux Mastery -> Process Management**"""
    ),

    (
        ["fil", "filer", "katalog", "mapp", "ls", "cd", "pwd", "find", "locate"],
        ["navigera filer", "hitta filer", "ls kommando", "cd kommando", "find"],
        """**Filsystemnavigering** täcks i Linux Mastery -> Node 2.

Innehåll:
• `ls`, `cd`, `pwd` - Grundläggande navigering
• `find`, `locate` - Hitta filer
• Filsystemets struktur (/etc, /var, /home)
• Relativa vs absoluta sökvägar

Gå till: **SkillsMaps -> Linux Mastery -> File System Navigation**"""
    ),

    (
        ["cp", "mv", "rm", "mkdir", "touch", "kopiera", "flytta", "ta bort"],
        ["kopiera fil", "flytta fil", "ta bort fil", "skapa mapp", "cp mv rm"],
        """**Filoperationer** täcks i Linux Mastery -> Node 3.

Innehåll:
• `cp` - Kopiera filer och mappar
• `mv` - Flytta/byt namn
• `rm` - Ta bort (VARNING: ingen papperskorg!)
• `mkdir`, `touch` - Skapa mappar och filer

Gå till: **SkillsMaps -> Linux Mastery -> File Operations**"""
    ),

    (
        ["chmod", "chown", "permission", "rättighet", "behörighet", "rwx", "755", "644"],
        ["chmod", "permissions", "filrättigheter", "hur ändrar jag rättigheter", "rwx"],
        """**Filrättigheter** täcks i Linux Mastery -> Node 4.

Innehåll:
• `r`, `w`, `x` - Read, Write, Execute
• `chmod` - Ändra rättigheter (755, 644, u+x)
• `chown` - Ändra ägare
• Speciella: SUID, SGID, Sticky bit
• Säkerhet: Varför 777 är farligt

Gå till: **SkillsMaps -> Linux Mastery -> File Permissions**"""
    ),

    (
        ["grep", "sed", "awk", "cut", "sort", "uniq", "text", "söka"],
        ["grep", "söka i filer", "sed", "awk", "texthantering"],
        """**Textbearbetning** täcks i Linux Mastery -> Node 5.

Innehåll:
• `grep` - Sök i text (regex!)
• `sed` - Stream editor (ersätt text)
• `awk` - Kraftfull textanalys
• `cut`, `sort`, `uniq` - Manipulera output

Gå till: **SkillsMaps -> Linux Mastery -> Text Processing**"""
    ),

    (
        ["vim", "nano", "vi", "editor", "textredigera"],
        ["vim", "nano", "hur använder jag vim", "texteditor i terminal"],
        """**Texteditorer** täcks i Linux Mastery -> Node 6.

Innehåll:
• `vim` - Kraftfull men brant inlärningskurva
• `nano` - Enklare, nybörjarvänlig
• vim-lägen: Normal, Insert, Visual
• Spara och avsluta (:wq, :q!)

Gå till: **SkillsMaps -> Linux Mastery -> Text Editors**"""
    ),

    (
        ["redirect", "pipe", "|", ">", ">>", "<", "stdin", "stdout", "stderr"],
        ["redirect", "pipe", "omdirigera output", "stdout stderr"],
        """**I/O Redirection** täcks i Linux Mastery -> Node 7.

Innehåll:
• `>` - Skriv till fil (överskriver)
• `>>` - Lägg till i fil
• `|` - Pipe mellan kommandon
• `2>&1` - Redirect stderr
• `/dev/null` - Kasta output

Gå till: **SkillsMaps -> Linux Mastery -> I/O Redirection**"""
    ),

    (
        ["user", "användare", "grupp", "useradd", "passwd", "sudo", "root"],
        ["skapa användare", "useradd", "sudo", "root", "grupper"],
        """**Användarhantering** täcks i Linux Mastery -> Node 8.

Innehåll:
• `useradd`, `userdel` - Skapa/ta bort användare
• `passwd` - Hantera lösenord
• `groups`, `usermod` - Grupphantering
• `sudo` - Köra som root
• `/etc/passwd`, `/etc/shadow`

Gå till: **SkillsMaps -> Linux Mastery -> User Management**"""
    ),

    (
        ["apt", "yum", "dnf", "paket", "install", "package", "brew"],
        ["installera paket", "apt install", "yum", "pakethantering"],
        """**Pakethantering** täcks i Linux Mastery -> Node 9.

Innehåll:
• `apt` (Debian/Ubuntu)
• `yum`/`dnf` (RHEL/CentOS)
• `brew` (macOS)
• Uppdatera system
• Repositories

Gå till: **SkillsMaps -> Linux Mastery -> Package Management**"""
    ),

    (
        ["systemd", "service", "systemctl", "tjänst", "daemon", "start", "stop", "enable"],
        ["systemctl", "starta tjänst", "service", "daemon"],
        """**Tjänstehantering** täcks i Linux Mastery -> Node 10.

Innehåll:
• `systemctl start/stop/restart`
• `systemctl enable/disable`
• Service-filer och unit-filer
• journalctl för loggar
• Boot targets

Gå till: **SkillsMaps -> Linux Mastery -> Service Management**"""
    ),

    (
        ["disk", "partition", "mount", "df", "du", "fdisk", "lvm", "lagring"],
        ["disk", "partition", "mount", "hur mycket plats", "df du"],
        """**Disk & Lagring** täcks i Linux Mastery -> Node 11.

Innehåll:
• `df`, `du` - Diskutrymme
• `mount`, `umount` - Montera filsystem
• `fdisk`, `parted` - Partitionering
• LVM - Logical Volume Manager
• RAID-koncept

Gå till: **SkillsMaps -> Linux Mastery -> Disk & Storage**"""
    ),

    (
        ["nätverk", "network", "ip", "ifconfig", "netstat", "ss", "ping", "traceroute", "subnet", "subnetting", "cidr"],
        ["nätverk", "ip adress", "subnetting", "subnet", "ping", "nätverksproblem"],
        """**Nätverk** täcks i Linux Mastery -> Node 12.

Innehåll:
• `ip addr`, `ifconfig` - Visa nätverksinfo
• `ping`, `traceroute` - Testa anslutning
• `netstat`, `ss` - Nätverksanslutningar
• **Subnetting & CIDR** - IP-beräkning
• Nätverkskonfiguration

Gå till: **SkillsMaps -> Linux Mastery -> Networking**"""
    ),

    (
        ["dns", "nslookup", "dig", "host", "resolv", "domän"],
        ["dns", "nslookup", "domänuppslagning", "dig"],
        """**DNS** täcks i Linux Mastery -> Node 13.

Innehåll:
• Hur DNS fungerar
• `nslookup`, `dig`, `host`
• `/etc/resolv.conf`
• `/etc/hosts`
• DNS-felsökning

Gå till: **SkillsMaps -> Linux Mastery -> DNS**"""
    ),

    (
        ["firewall", "brandvägg", "iptables", "ufw", "firewalld", "port"],
        ["firewall", "öppna port", "iptables", "ufw", "brandvägg"],
        """**Brandvägg** täcks i Linux Mastery -> Node 14.

Innehåll:
• `iptables` - Lågnivå brandvägg
• `ufw` - Enkelt Ubuntu-gränssnitt
• `firewalld` - RHEL/CentOS
• Öppna/stänga portar
• Chains och regler

Gå till: **SkillsMaps -> Linux Mastery -> Firewall**"""
    ),

    (
        ["ssh", "scp", "sftp", "nyckel", "key", "remote", "anslut"],
        ["ssh", "ansluta remote", "ssh nyckel", "scp"],
        """**SSH** täcks i Linux Mastery -> Node 15.

Innehåll:
• SSH-anslutning: `ssh user@host`
• SSH-nycklar: `ssh-keygen`
• `scp`, `sftp` - Filöverföring
• SSH config-fil
• Port forwarding & tunnlar

Gå till: **SkillsMaps -> Linux Mastery -> SSH**"""
    ),

    (
        ["tar", "gzip", "zip", "arkiv", "komprimera", "packa"],
        ["tar", "zip", "packa filer", "komprimera", "arkivera"],
        """**Arkivering** täcks i Linux Mastery -> Node 16.

Innehåll:
• `tar` - Skapa arkiv
• `gzip`, `bzip2` - Komprimera
• `tar -czvf` - Packa och komprimera
• `unzip`, `tar -xzvf` - Packa upp

Gå till: **SkillsMaps -> Linux Mastery -> Archiving**"""
    ),

    (
        ["cron", "crontab", "schemalägg", "automatisk", "jobb"],
        ["cron", "crontab", "schemalägg kommando", "automatisera"],
        """**Cron Jobs** täcks i Linux Mastery -> Node 17.

Innehåll:
• `crontab -e` - Redigera cron
• Cron-syntax: `* * * * *`
• Vanliga scheman
• Logga cron-output
• systemd timers

Gå till: **SkillsMaps -> Linux Mastery -> Cron & Scheduling**"""
    ),

    (
        ["log", "logg", "syslog", "journalctl", "loggar", "dmesg"],
        ["loggar", "var finns loggar", "journalctl", "syslog"],
        """**Logghantering** täcks i Linux Mastery -> Node 18.

Innehåll:
• `/var/log/` - Var loggar finns
• `journalctl` - Systemd-loggar
• `dmesg` - Kernel-loggar
• `tail -f` - Följa loggar live
• Log rotation

Gå till: **SkillsMaps -> Linux Mastery -> Log Management**"""
    ),

    (
        ["performance", "prestanda", "cpu", "minne", "memory", "ram", "vmstat", "iostat"],
        ["prestanda", "cpu användning", "minnesanvändning", "slow", "långsamt"],
        """**Prestanda** täcks i Linux Mastery -> Node 19.

Innehåll:
• `top`, `htop` - CPU/minne live
• `vmstat`, `iostat` - Detaljerad statistik
• `free -h` - Minnesanvändning
• Load average
• Flaskhalsar

Gå till: **SkillsMaps -> Linux Mastery -> Performance Monitoring**"""
    ),

    (
        ["troubleshoot", "felsök", "problem", "debug", "fungerar inte"],
        ["felsökning", "något fungerar inte", "debug", "troubleshoot"],
        """**Felsökning** täcks i Linux Mastery -> Node 20.

Innehåll:
• Systematisk felsökning
• Vanliga problem och lösningar
• Nätverksproblem
• Diskproblem
• Serviceproblem

Gå till: **SkillsMaps -> Linux Mastery -> Troubleshooting**"""
    ),

    # ==========================================================================
    # DOCKER
    # ==========================================================================
    (
        ["docker", "container", "containers"],
        ["vad är docker", "docker", "containers"],
        """**Docker** täcks i Docker-modulen och SkillsMap.

20 nodes som täcker:
• Vad är containers vs VMs
• docker run, ps, stop, rm
• Images och Dockerfile
• docker-compose
• Networking och volumes
• Docker Hub
• Multi-stage builds
• Security best practices

Gå till: **SkillsMaps -> Docker Mastery**"""
    ),

    (
        ["dockerfile", "image", "build", "bygga"],
        ["dockerfile", "bygga image", "docker build", "skapa image"],
        """**Dockerfile & Images** täcks i Docker Mastery.

Innehåll:
• FROM, RUN, COPY, CMD, ENTRYPOINT
• docker build -t myapp .
• Multi-stage builds
• .dockerignore
• Image layers och caching

Gå till: **SkillsMaps -> Docker Mastery -> Images**"""
    ),

    (
        ["docker-compose", "compose", "multi-container"],
        ["docker-compose", "compose", "flera containers"],
        """**Docker Compose** täcks i Docker Mastery.

Innehåll:
• docker-compose.yml syntax
• services, networks, volumes
• docker-compose up/down
• Environment variables
• Depends_on och healthchecks

Gå till: **SkillsMaps -> Docker Mastery -> Compose**"""
    ),

    (
        ["docker volume", "volym", "persistent", "data"],
        ["docker volume", "spara data", "persistent data"],
        """**Docker Volumes** täcks i Docker Mastery.

Innehåll:
• Named volumes vs bind mounts
• docker volume create/ls/rm
• Backup och restore
• Volume drivers

Gå till: **SkillsMaps -> Docker Mastery -> Volumes**"""
    ),

    (
        ["docker network", "nätverk", "bridge", "host"],
        ["docker nätverk", "containers kommunicera", "docker network"],
        """**Docker Networking** täcks i Docker Mastery.

Innehåll:
• Bridge, host, overlay networks
• docker network create
• Container DNS
• Port mapping (-p)
• Network isolation

Gå till: **SkillsMaps -> Docker Mastery -> Networking**"""
    ),

    # ==========================================================================
    # KUBERNETES
    # ==========================================================================
    (
        ["kubernetes", "k8s"],
        ["vad är kubernetes", "k8s", "kubernetes"],
        """**Kubernetes** täcks i Kubernetes-modulen och SkillsMap.

20 nodes som täcker:
• Pods, Deployments, Services
• kubectl-kommandon
• ConfigMaps och Secrets
• Ingress
• Helm charts
• RBAC
• Scaling och rollouts
• Production best practices

Gå till: **SkillsMaps -> Kubernetes Mastery**"""
    ),

    (
        ["pod", "pods"],
        ["vad är pod", "kubernetes pod", "pods"],
        """**Pods** täcks i Kubernetes Mastery.

Innehåll:
• Vad är en Pod (minsta deploybara enhet)
• Pod spec och containers
• Multi-container pods
• Pod lifecycle
• kubectl get/describe pods

Gå till: **SkillsMaps -> Kubernetes Mastery -> Pods**"""
    ),

    (
        ["deployment", "deployments", "replica"],
        ["deployment", "kubernetes deployment", "replicas"],
        """**Deployments** täcks i Kubernetes Mastery.

Innehåll:
• Deployment spec
• ReplicaSets
• Rolling updates
• Rollbacks
• Scaling

Gå till: **SkillsMaps -> Kubernetes Mastery -> Deployments**"""
    ),

    (
        ["kubectl"],
        ["kubectl", "kubernetes kommandon"],
        """**kubectl** täcks i Kubernetes Mastery.

Vanliga kommandon:
• kubectl get pods/services/deployments
• kubectl describe <resource>
• kubectl logs <pod>
• kubectl exec -it <pod> -- bash
• kubectl apply -f manifest.yaml

Gå till: **SkillsMaps -> Kubernetes Mastery**"""
    ),

    (
        ["helm", "chart", "charts"],
        ["helm", "helm chart", "kubernetes paket"],
        """**Helm** täcks i Kubernetes Mastery.

Innehåll:
• Vad är Helm (K8s pakethanterare)
• helm install/upgrade/rollback
• Skapa egna charts
• values.yaml
• Helm repositories

Gå till: **SkillsMaps -> Kubernetes Mastery -> Helm**"""
    ),

    (
        ["ingress", "load balancer", "lb"],
        ["ingress", "exponera app", "load balancer"],
        """**Ingress** täcks i Kubernetes Mastery.

Innehåll:
• Ingress controllers
• Routing rules
• TLS/SSL
• Path-based routing
• Host-based routing

Gå till: **SkillsMaps -> Kubernetes Mastery -> Ingress**"""
    ),

    # ==========================================================================
    # GIT
    # ==========================================================================
    (
        ["git"],
        ["vad är git", "git", "versionhantering"],
        """**Git** täcks i Git-modulen och SkillsMap.

Innehåll:
• git init, clone, add, commit
• Branching och merging
• Pull requests
• Merge conflicts
• Git workflows (GitFlow, trunk-based)
• GitHub Actions

Gå till: **SkillsMaps -> Git & GitHub**"""
    ),

    (
        ["branch", "gren", "branching"],
        ["git branch", "skapa branch", "branching"],
        """**Git Branching** täcks i Git-modulen.

Innehåll:
• git branch <name>
• git checkout / git switch
• git merge
• git rebase
• Branch strategies

Gå till: **SkillsMaps -> Git & GitHub -> Branching**"""
    ),

    (
        ["merge", "conflict", "konflikt", "sammanfoga"],
        ["merge conflict", "git merge", "lösa konflikt"],
        """**Merge & Conflicts** täcks i Git-modulen.

Innehåll:
• git merge
• Merge conflicts - hur de uppstår
• Lösa conflicts i editor
• git mergetool
• Aborta merge

Gå till: **SkillsMaps -> Git & GitHub -> Merging**"""
    ),

    (
        ["rebase"],
        ["git rebase", "rebase vs merge"],
        """**Git Rebase** täcks i Git-modulen.

Innehåll:
• git rebase vs merge
• Interactive rebase
• Squash commits
• När man ska använda rebase
• Golden rule (aldrig rebase public)

Gå till: **SkillsMaps -> Git & GitHub -> Rebase**"""
    ),

    (
        ["github actions", "actions", "workflow"],
        ["github actions", "ci/cd github", "workflow"],
        """**GitHub Actions** täcks i Git och CI/CD-modulerna.

Innehåll:
• .github/workflows/
• YAML-syntax
• Triggers (push, PR, schedule)
• Jobs och steps
• Secrets och variables

Gå till: **SkillsMaps -> Git & GitHub -> GitHub Actions**
eller **SkillsMaps -> CI/CD Pipelines**"""
    ),

    # ==========================================================================
    # AWS
    # ==========================================================================
    (
        ["aws", "amazon", "moln", "cloud"],
        ["aws", "amazon web services", "molntjänster"],
        """**AWS** täcks i AWS Core-modulen och SkillsMap.

20 nodes som täcker:
• EC2 - Virtuella servrar
• S3 - Objektlagring
• IAM - Identitetshantering
• VPC - Nätverk
• Lambda - Serverless
• RDS - Databaser
• ECS/EKS - Containers
• CloudFormation - IaC

Gå till: **SkillsMaps -> AWS**"""
    ),

    (
        ["ec2", "instans", "server", "virtuell"],
        ["ec2", "aws server", "virtuell maskin aws"],
        """**EC2** täcks i AWS-modulen.

Innehåll:
• Starta EC2-instanser
• Instance types
• Security Groups
• Key pairs
• AMIs
• Auto Scaling

Gå till: **SkillsMaps -> AWS -> EC2**"""
    ),

    (
        ["s3", "bucket", "objektlagring"],
        ["s3", "aws lagring", "bucket"],
        """**S3** täcks i AWS-modulen.

Innehåll:
• Buckets och objects
• Storage classes
• Versioning
• Lifecycle policies
• Access policies
• Static website hosting

Gå till: **SkillsMaps -> AWS -> S3**"""
    ),

    (
        ["iam", "role", "policy", "behörighet aws"],
        ["iam", "aws permissions", "role", "policy"],
        """**IAM** täcks i AWS-modulen.

Innehåll:
• Users, Groups, Roles
• Policies (JSON)
• Least privilege principle
• MFA
• Cross-account access

Gå till: **SkillsMaps -> AWS -> IAM**"""
    ),

    (
        ["vpc", "subnet", "aws nätverk"],
        ["vpc", "aws nätverk", "subnet aws"],
        """**VPC** täcks i AWS-modulen.

Innehåll:
• Skapa VPC
• Subnets (public/private)
• Internet Gateway
• NAT Gateway
• Route tables
• Security Groups vs NACLs

Gå till: **SkillsMaps -> AWS -> VPC**"""
    ),

    (
        ["lambda", "serverless", "funktion"],
        ["lambda", "serverless", "aws function"],
        """**Lambda** täcks i AWS-modulen.

Innehåll:
• Skapa Lambda-funktioner
• Triggers (API Gateway, S3, etc.)
• Runtime environments
• Layers
• Pricing model

Gå till: **SkillsMaps -> AWS -> Lambda**"""
    ),

    # ==========================================================================
    # TERRAFORM
    # ==========================================================================
    (
        ["terraform", "iac", "infrastructure as code"],
        ["terraform", "infrastructure as code", "iac"],
        """**Terraform** täcks i Terraform-modulen och SkillsMap.

20 nodes som täcker:
• HCL-syntax
• Providers
• Resources
• Variables och outputs
• Modules
• State management
• Workspaces
• Best practices

Gå till: **SkillsMaps -> Terraform**"""
    ),

    (
        ["hcl", "terraform syntax"],
        ["hcl", "terraform syntax", "terraform kod"],
        """**HCL-syntax** täcks i Terraform-modulen.

Innehåll:
• Blocks: resource, data, variable
• Attributes och arguments
• Expressions och functions
• Loops och conditionals

Gå till: **SkillsMaps -> Terraform -> HCL Basics**"""
    ),

    (
        ["terraform state", "tfstate"],
        ["terraform state", "state fil", "tfstate"],
        """**Terraform State** täcks i Terraform-modulen.

Innehåll:
• Vad är state
• Remote state (S3, etc.)
• State locking
• terraform import
• terraform state mv/rm

Gå till: **SkillsMaps -> Terraform -> State Management**"""
    ),

    (
        ["terraform module", "modul terraform"],
        ["terraform module", "terraform modul", "återanvändbar kod"],
        """**Terraform Modules** täcks i Terraform-modulen.

Innehåll:
• Skapa modules
• Module sources
• Input/output variables
• Module registry
• Best practices

Gå till: **SkillsMaps -> Terraform -> Modules**"""
    ),

    # ==========================================================================
    # CI/CD
    # ==========================================================================
    (
        ["cicd", "ci/cd", "pipeline", "continuous"],
        ["ci/cd", "pipeline", "continuous integration", "continuous deployment"],
        """**CI/CD** täcks i CI/CD Pipelines-modulen och SkillsMap.

20 nodes som täcker:
• CI vs CD vs CD
• GitHub Actions
• GitLab CI
• Jenkins
• ArgoCD & GitOps
• Testing i pipelines
• Deployment strategies

Gå till: **SkillsMaps -> CI/CD Pipelines**"""
    ),

    (
        ["jenkins"],
        ["jenkins", "jenkins pipeline"],
        """**Jenkins** täcks i CI/CD-modulen.

Innehåll:
• Jenkins installation
• Jenkinsfile syntax
• Declarative vs Scripted
• Plugins
• Agents och executors

Gå till: **SkillsMaps -> CI/CD Pipelines -> Jenkins**"""
    ),

    (
        ["gitlab ci", "gitlab"],
        ["gitlab ci", "gitlab pipeline"],
        """**GitLab CI** täcks i CI/CD-modulen.

Innehåll:
• .gitlab-ci.yml
• Stages och jobs
• Runners
• Artifacts
• Environments

Gå till: **SkillsMaps -> CI/CD Pipelines -> GitLab CI**"""
    ),

    (
        ["argocd", "gitops"],
        ["argocd", "gitops", "kubernetes deployment"],
        """**ArgoCD & GitOps** täcks i CI/CD-modulen.

Innehåll:
• GitOps principer
• ArgoCD installation
• Application CRDs
• Sync policies
• Rollbacks

Gå till: **SkillsMaps -> CI/CD Pipelines -> ArgoCD**"""
    ),

    # ==========================================================================
    # PYTHON
    # ==========================================================================
    (
        ["python"],
        ["python", "python devops", "scripting python"],
        """**Python for DevOps** täcks i Python-modulen och SkillsMap.

21 nodes som täcker:
• Python-grunder
• Scripting och automation
• boto3 (AWS SDK)
• paramiko (SSH)
• subprocess
• JSON/YAML-hantering
• API-anrop (requests)
• Testa med pytest

Gå till: **SkillsMaps -> Python for DevOps**"""
    ),

    (
        ["boto3", "aws sdk", "python aws"],
        ["boto3", "python aws", "aws sdk python"],
        """**boto3** täcks i Python for DevOps.

Innehåll:
• Installation och setup
• EC2-operationer
• S3-operationer
• IAM-hantering
• Error handling

Gå till: **SkillsMaps -> Python for DevOps -> boto3**"""
    ),

    (
        ["subprocess", "os", "shell python"],
        ["subprocess", "köra kommandon python", "os modul"],
        """**subprocess & os** täcks i Python for DevOps.

Innehåll:
• subprocess.run()
• os.system() (undvik!)
• Capture output
• Error handling
• Säkerhet (shell injection)

Gå till: **SkillsMaps -> Python for DevOps -> System Commands**"""
    ),

    # ==========================================================================
    # BASH / SHELL
    # ==========================================================================
    (
        ["bash", "shell", "script", "scripting"],
        ["bash", "shell script", "bash scripting"],
        """**Shell Scripting** täcks i Shell/Bash-modulen och SkillsMap.

20 nodes som täcker:
• Bash-grunder
• Variabler och arrays
• Conditionals (if/else)
• Loops (for, while)
• Functions
• Input/output
• Error handling
• Best practices

Gå till: **SkillsMaps -> Shell/Bash** eller **Camp DevOps -> Shell Scripting**"""
    ),

    # ==========================================================================
    # HJÄLP & SUPPORT
    # ==========================================================================
    (
        ["börja", "start", "nybörjare", "var börjar jag"],
        ["var börjar jag", "ny här", "hur startar jag"],
        """Välkommen! 🎉 Här är förslag på hur du börjar:

**Rekommenderad ordning:**
1. **Linux Mastery** - Grunden för allt DevOps
2. **Git & Workflows** - Versionhantering är kritiskt
3. **Docker** - Containerisering
4. **CI/CD** - Automatisering
5. **Kubernetes** - Container orchestration
6. **AWS/Terraform** - Molninfrastruktur

Gå till **Camp DevOps** och börja med första modulen!"""
    ),

    (
        ["hjälp", "support", "problem", "fel", "funkar inte"],
        ["hjälp", "support", "något funkar inte", "problem"],
        """Behöver du hjälp? 🤝

• **Tekniska problem** - Prova ladda om sidan
• **Frågor om innehåll** - Fråga mig om specifika ämnen
• **Hittar inte något** - Beskriv vad du letar efter

Du kan också kolla Help-sidan i menyn för mer information."""
    ),
]

# Fallback-svar när ingen match hittas
NO_MATCH_RESPONSE = """Jag hittade tyvärr inget svar på din fråga i vårt innehåll. 🤔

**Tips:**
• Prova att omformulera frågan
• Fråga om specifika ämnen (Docker, Linux, etc.)
• Utforska modulerna i Camp DevOps
• Kolla SkillsMaps för djupare innehåll

Jag kan hjälpa dig hitta rätt modul om du berättar vad du vill lära dig!"""


def normalize_text(text: str) -> str:
    """Normalize text for matching."""
    text = text.lower().strip()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text


def calculate_match_score(query: str, keywords: List[str], patterns: List[str]) -> float:
    """
    Calculate how well a query matches an FAQ entry.
    Returns a score from 0.0 to 1.0
    """
    query_normalized = normalize_text(query)
    query_words = set(query_normalized.split())

    score = 0.0

    # Check keyword matches (each keyword match adds to score)
    keyword_matches = sum(1 for kw in keywords if kw in query_normalized)
    if keyword_matches > 0:
        score += 0.4 * min(keyword_matches / len(keywords), 1.0)

    # Check pattern matches (stronger signal)
    for pattern in patterns:
        pattern_normalized = normalize_text(pattern)
        pattern_words = set(pattern_normalized.split())

        # Word overlap
        overlap = len(query_words & pattern_words)
        if overlap > 0:
            pattern_score = overlap / max(len(pattern_words), len(query_words))
            score = max(score, 0.5 + 0.5 * pattern_score)

    return min(score, 1.0)


def find_best_match(query: str) -> Tuple[Optional[str], float]:
    """
    Find the best matching FAQ answer for a query.
    Returns (answer, confidence_score) or (None, 0.0)
    """
    best_answer = None
    best_score = 0.0

    for keywords, patterns, answer in FAQ_DATABASE:
        score = calculate_match_score(query, keywords, patterns)
        if score > best_score:
            best_score = score
            best_answer = answer

    # Require minimum confidence of 0.25 (lowered for better matching)
    if best_score >= 0.25:
        return best_answer, best_score

    return None, 0.0


def get_dallas_response(query: str) -> dict:
    """
    Get Dallas response from FAQ database.
    No GPT calls - only local matching.

    Returns:
        dict with 'response', 'confidence', 'source'
    """
    answer, confidence = find_best_match(query)

    if answer:
        return {
            "response": answer,
            "confidence": confidence,
            "source": "faq_database"
        }

    return {
        "response": NO_MATCH_RESPONSE,
        "confidence": 0.0,
        "source": "no_match"
    }
