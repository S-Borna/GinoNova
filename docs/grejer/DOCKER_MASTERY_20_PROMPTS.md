# Docker Mastery - 20 Node Prompts för Opus

## Modulöversikt

| Nod | Titel | Tid | XP | Svårighet |
|-----|-------|-----|-----|-----------|
| 01 | Docker Fundamentals & Architecture | 45 min | 75 XP | Lätt |
| 02 | Docker Images Deep Dive | 45 min | 75 XP | Lätt |
| 03 | Container Lifecycle Management | 40 min | 70 XP | Lätt |
| 04 | Dockerfile Mastery | 50 min | 85 XP | Medium |
| 05 | Docker Networking | 50 min | 85 XP | Medium |
| 06 | Docker Volumes & Persistence | 45 min | 80 XP | Medium |
| 07 | Docker Compose Fundamentals | 50 min | 85 XP | Medium |
| 08 | Docker Compose Advanced Patterns | 55 min | 95 XP | Svår |
| 09 | Docker Security Best Practices | 50 min | 90 XP | Svår |
| 10 | Docker in Production | 55 min | 95 XP | Svår |
| 11 | Docker Registry & Image Distribution | 45 min | 80 XP | Medium |
| 12 | Docker Multi-stage Builds | 45 min | 80 XP | Medium |
| 13 | Docker Performance Optimization | 50 min | 90 XP | Svår |
| 14 | Docker Debugging & Troubleshooting | 45 min | 80 XP | Medium |
| 15 | Docker with CI/CD | 50 min | 90 XP | Svår |
| 16 | Docker Swarm Basics | 45 min | 80 XP | Medium |
| 17 | Docker Best Practices Summary | 40 min | 75 XP | Medium |
| 18 | Docker Development Workflow | 40 min | 70 XP | Lätt |
| 19 | Docker Ecosystem & Tools | 35 min | 65 XP | Lätt |
| 20 | Docker Certification Path | 40 min | 75 XP | Medium |

**Totalt:** ~15 timmar, 1620 XP

---

## PROMPT 01: Docker Fundamentals & Architecture

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 01
- Titel: Docker Fundamentals & Architecture
- Slug: docker_fundamentals_architecture
- Svårighetsgrad: Lätt
- Tidsuppskattning: 45 minuter
- XP: 75
- Föregående nod: null (första noden)
- Nästa nod: docker_images_deep_dive

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Vad är containerisering och varför behövs det
2. Docker vs virtuella maskiner - arkitekturskillnader
3. Docker Engine komponenter (daemon, CLI, REST API)
4. Container runtime (containerd, runc)
5. Docker Desktop vs Docker Engine på Linux
6. Namespaces och cgroups - grundläggande isolering
7. Union filesystem och layer-arkitektur
8. OCI-standarden (Open Container Initiative)
9. Docker Hub och container registries översikt
10. Installation och verifiering på Linux/macOS/Windows

### Övningar att inkludera:

**Övning 1 - Grundläggande (20 XP)**
Titel: "Din första container"
- Installera Docker och verifiera installation
- Kör docker info och docker version
- Starta hello-world och nginx containers
- Utforska docker ps, docker images

**Övning 2 - Tillämpad (25 XP)**
Titel: "Utforska container-arkitekturen"
- Inspektera containerns namespaces med nsenter
- Visa cgroups-begränsningar
- Jämför processer i container vs host
- Analysera layer-strukturen med docker history

**Övning 3 - Utmanande (30 XP)**
Titel: "Multi-container demonstration"
- Sätt upp en webbserver och databas
- Verifiera isolering mellan containers
- Dokumentera resursanvändning
- Skapa arkitekturdiagram

### DevOps-kontext:
- Visa hur containerisering löser "works on my machine"-problemet
- Förklara microservices-arkitektur och Docker
- CI/CD-pipelines med containers
- Kubernetes som nästa steg efter Docker

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion (3-4 stycken, berätta VARFÖR detta är viktigt)
2. Teori (huvudinnehållet, 6-8 undersektioner med ###)
3. Steg-för-steg Guide (numrerade steg med kodblock)
4. Praktiska Exempel (3-4 realistiska scenarios)
5. Bästa Praxis (minst 5 punkter)
6. Vanliga Fallgropar (minst 4 med lösningar)
7. Övningar (alla tre övningarna ovan, med <details>-taggar för lösningar)
8. Kopplingar (till andra noder i modulen)
9. Sammanfattning (bullet points)
10. Nyckelkommandon (tabell med kommando|beskrivning|exempel)
11. Referenser (officiella docs, böcker, tutorials)

## FORMATKRAV
- Använd denna separator mellan ALLA huvudsektioner:
  ------------------------------------------------------------
  (60 bindestreck)
- INGA emojis i rubriker eller brödtext
- Använd ASCII för diagram: +, -, |, inte Unicode box-drawing

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående - berätta som en mentor
- Alla kodblock ska ha UTFÖRLIGA kommentarer som förklarar:
  - VAD kommandot gör
  - VARFÖR vi gör det
  - Förväntad output
- Använd <details><summary>Ledtråd</summary>...</details> och <details><summary>Lösning</summary>...</details> för övningar
- Varje kodexempel ska vara körbart och testat
- Inkludera output/förväntat resultat för kommandon
- Använd analogier: "Tänk på det som..."
```

---

## PROMPT 02: Docker Images Deep Dive

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 02
- Titel: Docker Images Deep Dive
- Slug: docker_images_deep_dive
- Svårighetsgrad: Lätt
- Tidsuppskattning: 45 minuter
- XP: 75
- Föregående nod: docker_fundamentals_architecture
- Nästa nod: container_lifecycle_management

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Vad är en Docker image - immutable layers
2. Image vs Container - konceptuell skillnad
3. Docker Hub och officiella images
4. Image naming convention (registry/repo:tag)
5. Layer-systemet och caching
6. docker pull, push, tag kommandon
7. docker images och docker image inspect
8. Image history och layer-analys
9. Dangling images och cleanup
10. Image digests och content-addressable storage

### Övningar att inkludera:

**Övning 1 - Grundläggande (20 XP)**
Titel: "Image-hantering basics"
- Sök efter och ladda ner images från Docker Hub
- Lista och filtrera images
- Tagga images med nya namn
- Ta bort images och hantera dangling images

**Övning 2 - Tillämpad (25 XP)**
Titel: "Layer-analys"
- Använd docker history för att analysera layers
- Jämför storleken på olika base images (alpine vs ubuntu)
- Inspektera image metadata med docker inspect
- Exportera och importera images som tar-filer

**Övning 3 - Utmanande (30 XP)**
Titel: "Image audit och cleanup"
- Identifiera och analysera alla images på systemet
- Skapa ett cleanup-script för oanvända images
- Beräkna diskutrymme som kan frigöras
- Dokumentera image-dependencies

### DevOps-kontext:
- Image scanning i CI/CD-pipelines
- Vulnerability assessment med Trivy/Clair
- Base image selection best practices
- Image versioning strategies för produktion

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 03: Container Lifecycle Management

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 03
- Titel: Container Lifecycle Management
- Slug: container_lifecycle_management
- Svårighetsgrad: Lätt
- Tidsuppskattning: 40 minuter
- XP: 70
- Föregående nod: docker_images_deep_dive
- Nästa nod: dockerfile_mastery

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Container states (created, running, paused, stopped, dead)
2. docker run och dess viktigaste flaggor (-d, -it, --rm, --name)
3. docker start, stop, restart, kill
4. docker pause och unpause
5. docker attach vs docker exec
6. Container logs och log drivers
7. docker stats för realtidsövervakning
8. Container auto-restart policies
9. Graceful shutdown och SIGTERM/SIGKILL
10. Container prune och cleanup strategies

### Övningar att inkludera:

**Övning 1 - Grundläggande (20 XP)**
Titel: "Container lifecycle basics"
- Skapa, starta, stoppa och ta bort containers
- Öva på attach vs exec
- Arbeta med detached mode
- Hantera container naming

**Övning 2 - Tillämpad (25 XP)**
Titel: "Logging och monitoring"
- Konfigurera olika log drivers
- Följ logs i realtid med docker logs -f
- Övervaka resurser med docker stats
- Implementera log rotation

**Övning 3 - Utmanande (25 XP)**
Titel: "Restart policies och resilience"
- Testa olika restart policies (no, on-failure, always, unless-stopped)
- Simulera container crashes
- Implementera graceful shutdown i en app
- Mät startup/shutdown-tider

### DevOps-kontext:
- Container orchestration preview (Kubernetes pods)
- Health checks i produktion
- Log aggregation med ELK/Loki
- Monitoring med Prometheus/Grafana

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 04: Dockerfile Mastery

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 04
- Titel: Dockerfile Mastery
- Slug: dockerfile_mastery
- Svårighetsgrad: Medium
- Tidsuppskattning: 50 minuter
- XP: 85
- Föregående nod: container_lifecycle_management
- Nästa nod: docker_networking

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Dockerfile syntax och struktur
2. FROM - base images och best practices
3. RUN, COPY, ADD - skillnader och användning
4. ENV, ARG - miljövariabler och build arguments
5. WORKDIR, USER - arbetskataloger och säkerhet
6. EXPOSE, VOLUME - portar och volymer
7. CMD vs ENTRYPOINT - exec form vs shell form
8. Layer optimization och caching
9. .dockerignore för effektiva builds
10. LABEL och HEALTHCHECK instruktioner

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Din första Dockerfile"
- Skapa Dockerfile för en Python/Node.js-applikation
- Implementera korrekt COPY och WORKDIR
- Använd ENV för konfiguration
- Testa CMD och ENTRYPOINT

**Övning 2 - Tillämpad (30 XP)**
Titel: "Optimerad Dockerfile"
- Optimera layer-ordning för bättre caching
- Implementera .dockerignore
- Reducera image-storlek med alpine base
- Lägg till HEALTHCHECK

**Övning 3 - Utmanande (30 XP)**
Titel: "Production-ready Dockerfile"
- Implementera non-root user
- Använd ARG för build-time variabler
- Skapa en Dockerfile med multiple stages preview
- Dokumentera och validera med hadolint

### DevOps-kontext:
- Dockerfile linting i CI/CD
- Automated builds på Docker Hub/GitHub Actions
- Security scanning av Dockerfiles
- GitOps och Dockerfile versioning

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 05: Docker Networking

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 05
- Titel: Docker Networking
- Slug: docker_networking
- Svårighetsgrad: Medium
- Tidsuppskattning: 50 minuter
- XP: 85
- Föregående nod: dockerfile_mastery
- Nästa nod: docker_volumes_persistence

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Docker networking overview - CNM (Container Network Model)
2. Bridge network - default och custom bridges
3. Host network mode - när och varför
4. None network - isolerade containers
5. Overlay networks - multi-host networking
6. Port mapping (-p) och EXPOSE
7. DNS och service discovery i Docker
8. docker network create, connect, disconnect
9. Network inspection och troubleshooting
10. Container-to-container kommunikation

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Network basics"
- Skapa och inspektera olika network types
- Anslut containers till nätverk
- Testa container-to-container kommunikation
- Implementera port mapping

**Övning 2 - Tillämpad (30 XP)**
Titel: "Custom bridge networks"
- Skapa isolerade nätverk för olika applikationer
- Implementera DNS-baserad service discovery
- Testa nätverksisolering mellan containers
- Konfigurera subnet och gateway

**Övning 3 - Utmanande (30 XP)**
Titel: "Multi-container networking"
- Sätt upp en 3-tier applikation (frontend, backend, db)
- Implementera network segmentation
- Debugga nätverksproblem med tcpdump/netcat
- Dokumentera nätverksarkitekturen

### DevOps-kontext:
- Service mesh introduction (Istio, Linkerd)
- Kubernetes networking jämförelse
- Network policies och security
- Load balancing med Docker

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 06: Docker Volumes & Persistence

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 06
- Titel: Docker Volumes & Persistence
- Slug: docker_volumes_persistence
- Svårighetsgrad: Medium
- Tidsuppskattning: 45 minuter
- XP: 80
- Föregående nod: docker_networking
- Nästa nod: docker_compose_fundamentals

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Varför persistence behövs - containers är ephemeral
2. Tre sätt att hantera data: volumes, bind mounts, tmpfs
3. Named volumes vs anonymous volumes
4. docker volume create, ls, inspect, rm
5. Bind mounts - host paths i containers
6. Volume drivers och plugins
7. Data sharing mellan containers
8. Backup och restore av volumes
9. Volumes i Dockerfiles (VOLUME instruction)
10. Read-only volumes och security

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Volume basics"
- Skapa och hantera named volumes
- Använd bind mounts för utveckling
- Dela data mellan containers
- Inspektera volume innehåll

**Övning 2 - Tillämpad (25 XP)**
Titel: "Database persistence"
- Sätt upp PostgreSQL/MySQL med persistent storage
- Testa data persistence över container restarts
- Implementera backup-strategi
- Migrera data mellan volumes

**Övning 3 - Utmanande (30 XP)**
Titel: "Production volume patterns"
- Implementera read-only containers med volumes
- Skapa backup/restore scripts
- Hantera volume permissions korrekt
- Sätt upp volume monitoring

### DevOps-kontext:
- Kubernetes PersistentVolumes jämförelse
- CSI (Container Storage Interface)
- Stateful applications i containers
- Data lifecycle management

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 07: Docker Compose Fundamentals

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 07
- Titel: Docker Compose Fundamentals
- Slug: docker_compose_fundamentals
- Svårighetsgrad: Medium
- Tidsuppskattning: 50 minuter
- XP: 85
- Föregående nod: docker_volumes_persistence
- Nästa nod: docker_compose_advanced_patterns

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Vad är Docker Compose - multi-container orchestration
2. docker-compose.yml syntax och struktur
3. Services, networks, volumes i Compose
4. docker compose up, down, ps, logs
5. Environment variables och .env filer
6. depends_on och service startup order
7. Build vs Image i services
8. Port mapping och expose i Compose
9. Compose file versioning
10. docker compose config för validering

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Första Compose-projektet"
- Skapa docker-compose.yml för en enkel webbapp
- Använd docker compose up/down
- Arbeta med logs och ps
- Hantera environment variables

**Övning 2 - Tillämpad (30 XP)**
Titel: "Multi-service application"
- Sätt upp frontend + backend + databas
- Konfigurera networks och volumes
- Implementera depends_on korrekt
- Använd .env för konfiguration

**Övning 3 - Utmanande (30 XP)**
Titel: "Development environment"
- Skapa en komplett utvecklingsmiljö
- Implementera hot-reload med bind mounts
- Hantera multiple environments (dev/prod)
- Lägg till debugging och profiling services

### DevOps-kontext:
- Compose vs Kubernetes
- Local development workflows
- CI/CD integration med Compose
- Testing med Compose

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 08: Docker Compose Advanced Patterns

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 08
- Titel: Docker Compose Advanced Patterns
- Slug: docker_compose_advanced_patterns
- Svårighetsgrad: Svår
- Tidsuppskattning: 55 minuter
- XP: 95
- Föregående nod: docker_compose_fundamentals
- Nästa nod: docker_security_best_practices

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Compose profiles för selective service startup
2. extends och YAML anchors för DRY
3. Healthchecks i Compose
4. Resource limits (CPU, memory)
5. Multiple Compose files och overrides
6. docker compose watch för development
7. Secrets och configs i Compose
8. Deploy section för production hints
9. Networking advanced (aliases, links legacy)
10. Compose plugins och extensions

### Övningar att inkludera:

**Övning 1 - Tillämpad (30 XP)**
Titel: "Profiles och overrides"
- Implementera profiles för dev/test/prod
- Använd override files för environments
- Skapa DRY config med YAML anchors
- Validera med docker compose config

**Övning 2 - Svår (35 XP)**
Titel: "Production-ready Compose"
- Implementera healthchecks för alla services
- Konfigurera resource limits
- Hantera secrets korrekt
- Sätt upp logging och monitoring

**Övning 3 - Utmanande (30 XP)**
Titel: "Complex application stack"
- Bygg en microservices-demo med 5+ services
- Implementera service mesh patterns
- Konfigurera inter-service authentication
- Skapa deployment documentation

### DevOps-kontext:
- Compose to Kubernetes migration
- GitOps med Compose
- Testning av microservices lokalt
- Production deployment patterns

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 09: Docker Security Best Practices

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 09
- Titel: Docker Security Best Practices
- Slug: docker_security_best_practices
- Svårighetsgrad: Svår
- Tidsuppskattning: 50 minuter
- XP: 90
- Föregående nod: docker_compose_advanced_patterns
- Nästa nod: docker_in_production

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Container isolation och kernel sharing
2. Rootless Docker och user namespaces
3. Non-root containers - USER instruction
4. Read-only filesystems och tmpfs
5. Capabilities och seccomp profiles
6. Image scanning med Trivy, Grype, Snyk
7. Docker Content Trust och image signing
8. Secrets management best practices
9. Network security och policies
10. Runtime security monitoring

### Övningar att inkludera:

**Övning 1 - Tillämpad (30 XP)**
Titel: "Secure Dockerfile"
- Implementera non-root user i container
- Skapa minimal base image
- Scanna image med Trivy
- Fixa identifierade vulnerabilities

**Övning 2 - Svår (30 XP)**
Titel: "Runtime security"
- Konfigurera seccomp profile
- Implementera read-only filesystem
- Dropp unnecessary capabilities
- Testa med docker-bench-security

**Övning 3 - Utmanande (30 XP)**
Titel: "Security audit"
- Genomför full security audit av en application stack
- Implementera Docker Content Trust
- Skapa security compliance checklist
- Dokumentera threat model

### DevOps-kontext:
- DevSecOps pipeline integration
- Compliance (SOC2, PCI-DSS, HIPAA)
- Container security i Kubernetes
- Incident response för containers

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 10: Docker in Production

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 10
- Titel: Docker in Production
- Slug: docker_in_production
- Svårighetsgrad: Svår
- Tidsuppskattning: 55 minuter
- XP: 95
- Föregående nod: docker_security_best_practices
- Nästa nod: docker_registry_image_distribution

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Production vs Development - key differences
2. Logging strategies (json-file, syslog, fluentd)
3. Health checks och self-healing
4. Resource management och limits
5. Rolling updates och blue-green deployments
6. High availability patterns
7. Docker daemon configuration för produktion
8. Monitoring med Prometheus/Grafana
9. Backup och disaster recovery
10. Cost optimization i container environments

### Övningar att inkludera:

**Övning 1 - Tillämpad (30 XP)**
Titel: "Production configuration"
- Konfigurera Docker daemon för produktion
- Implementera centralized logging
- Sätt upp health checks
- Konfigurera resource limits

**Övning 2 - Svår (35 XP)**
Titel: "Monitoring och alerting"
- Sätt upp Prometheus + Grafana för Docker
- Skapa dashboards för container metrics
- Implementera alerting rules
- Testa incident scenarios

**Övning 3 - Utmanande (30 XP)**
Titel: "Production deployment"
- Implementera zero-downtime deployment
- Skapa backup/restore procedurer
- Dokumentera runbooks
- Genomför load testing

### DevOps-kontext:
- SRE practices för containers
- Capacity planning
- Incident management
- Cost allocation och showback

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 11: Docker Registry & Image Distribution

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 11
- Titel: Docker Registry & Image Distribution
- Slug: docker_registry_image_distribution
- Svårighetsgrad: Medium
- Tidsuppskattning: 45 minuter
- XP: 80
- Föregående nod: docker_in_production
- Nästa nod: docker_multistage_builds

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Docker Hub - features och limitations
2. Private registries - Harbor, GitLab Registry, ECR, ACR, GCR
3. Self-hosted Docker Registry
4. docker login och credential management
5. Image tagging strategies (semver, git SHA, latest)
6. Pull-through cache och mirror registries
7. Registry security och access control
8. Image replication och geo-distribution
9. Garbage collection och storage management
10. OCI Distribution Specification

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Registry basics"
- Sätt upp lokal Docker Registry
- Push och pull images
- Implementera basic authentication
- Lista images i registry via API

**Övning 2 - Tillämpad (25 XP)**
Titel: "Enterprise registry"
- Konfigurera TLS för registry
- Implementera access control
- Sätt upp pull-through cache
- Integrera med CI/CD

**Övning 3 - Utmanande (30 XP)**
Titel: "Multi-registry strategy"
- Implementera image promotion mellan registries
- Skapa automated cleanup policies
- Konfigurera registry replication
- Dokumentera image lifecycle

### DevOps-kontext:
- Registry i CI/CD pipelines
- Multi-cloud registry strategies
- Compliance och audit logging
- Cost management för registry storage

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 12: Docker Multi-stage Builds

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 12
- Titel: Docker Multi-stage Builds
- Slug: docker_multistage_builds
- Svårighetsgrad: Medium
- Tidsuppskattning: 45 minuter
- XP: 80
- Föregående nod: docker_registry_image_distribution
- Nästa nod: docker_performance_optimization

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Varför multi-stage builds - small, secure images
2. Multi-stage syntax och FROM ... AS
3. COPY --from för artifact extraction
4. Build targets med --target
5. Parallell builds med BuildKit
6. Caching strategies i multi-stage
7. Language-specific patterns (Go, Java, Node.js, Python)
8. Scratch images för minimal footprint
9. Distroless images från Google
10. Debugging multi-stage builds

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Första multi-stage build"
- Konvertera en enkel Dockerfile till multi-stage
- Jämför image storlekar före/efter
- Använd named stages
- Testa --target för development builds

**Övning 2 - Tillämpad (25 XP)**
Titel: "Language-specific multi-stage"
- Bygg Go-application med scratch final stage
- Bygg Node.js app med multi-stage
- Optimera för build cache
- Implementera test stage

**Övning 3 - Utmanande (30 XP)**
Titel: "Advanced patterns"
- Skapa multi-architecture builds
- Implementera conditional stages
- Använd BuildKit cache mounts
- Skapa reusable builder images

### DevOps-kontext:
- CI/CD optimization med multi-stage
- Security scanning av final images
- Supply chain security
- Build time vs image size tradeoffs

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 13: Docker Performance Optimization

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 13
- Titel: Docker Performance Optimization
- Slug: docker_performance_optimization
- Svårighetsgrad: Svår
- Tidsuppskattning: 50 minuter
- XP: 90
- Föregående nod: docker_multistage_builds
- Nästa nod: docker_debugging_troubleshooting

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Build performance - caching, parallelization
2. BuildKit features och DOCKER_BUILDKIT=1
3. Image size optimization techniques
4. Runtime performance - CPU, memory tuning
5. Storage drivers och performance (overlay2, btrfs)
6. Network performance optimization
7. I/O performance och volume drivers
8. Container startup time optimization
9. Resource limits och cgroups v2
10. Profiling och benchmarking tools

### Övningar att inkludera:

**Övning 1 - Tillämpad (30 XP)**
Titel: "Build optimization"
- Analysera och optimera build times
- Implementera BuildKit cache mounts
- Parallellisera builds
- Mät och dokumentera förbättringar

**Övning 2 - Svår (30 XP)**
Titel: "Runtime optimization"
- Profilera container performance
- Tuning CPU och memory limits
- Optimera I/O med volumes
- Implementera resource quotas

**Övning 3 - Utmanande (30 XP)**
Titel: "Performance benchmarking"
- Skapa benchmarking suite för containers
- Jämför olika storage drivers
- Analysera network latency
- Dokumentera performance baselines

### DevOps-kontext:
- Performance testing i CI/CD
- Capacity planning med metrics
- Cost vs performance tradeoffs
- SLOs för container performance

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 14: Docker Debugging & Troubleshooting

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 14
- Titel: Docker Debugging & Troubleshooting
- Slug: docker_debugging_troubleshooting
- Svårighetsgrad: Medium
- Tidsuppskattning: 45 minuter
- XP: 80
- Föregående nod: docker_performance_optimization
- Nästa nod: docker_with_cicd

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. docker logs och log analysis
2. docker exec för live debugging
3. docker inspect för deep analysis
4. docker events för real-time monitoring
5. docker diff för filesystem changes
6. Network debugging med tcpdump, netcat
7. Container crash analysis
8. Common errors och lösningar
9. Debug images och debugging sidecars
10. Docker daemon logs och troubleshooting

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Basic debugging"
- Debugga en crashande container
- Analysera logs för felmeddelanden
- Använd exec för live troubleshooting
- Inspektera container state

**Övning 2 - Tillämpad (25 XP)**
Titel: "Network debugging"
- Debugga container-to-container connectivity
- Analysera DNS resolution problems
- Identifiera port conflicts
- Testa med network debugging tools

**Övning 3 - Utmanande (30 XP)**
Titel: "Complex troubleshooting"
- Skapa och debugga ett multi-container scenario
- Identifiera resource exhaustion
- Analysera storage issues
- Dokumentera troubleshooting runbook

### DevOps-kontext:
- Incident response procedures
- On-call debugging strategies
- Post-mortem analysis
- Automated alerting och detection

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 15: Docker with CI/CD

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 15
- Titel: Docker with CI/CD
- Slug: docker_with_cicd
- Svårighetsgrad: Svår
- Tidsuppskattning: 50 minuter
- XP: 90
- Föregående nod: docker_debugging_troubleshooting
- Nästa nod: docker_swarm_basics

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Docker i CI/CD pipelines - overview
2. GitHub Actions med Docker
3. GitLab CI och Docker-in-Docker
4. Jenkins med Docker agents
5. Build, test, push patterns
6. Image tagging strategies i CI/CD
7. Security scanning i pipelines
8. Cache optimization för CI builds
9. Multi-platform builds i CI
10. Deployment automation med Docker

### Övningar att inkludera:

**Övning 1 - Tillämpad (30 XP)**
Titel: "GitHub Actions pipeline"
- Skapa komplett Docker CI/CD i GitHub Actions
- Implementera build, test, push stages
- Konfigurera caching
- Push till Docker Hub/GHCR

**Övning 2 - Svår (30 XP)**
Titel: "GitLab CI pipeline"
- Sätt upp Docker-in-Docker
- Implementera security scanning
- Konfigurera multi-environment deployment
- Hantera secrets korrekt

**Övning 3 - Utmanande (30 XP)**
Titel: "Advanced CI/CD patterns"
- Implementera multi-arch builds
- Skapa release automation
- Integrera vulnerability scanning
- Dokumentera pipeline architecture

### DevOps-kontext:
- DevSecOps integration
- GitOps deployment patterns
- Compliance i CI/CD
- Deployment strategies (canary, blue-green)

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 16: Docker Swarm Basics

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 16
- Titel: Docker Swarm Basics
- Slug: docker_swarm_basics
- Svårighetsgrad: Medium
- Tidsuppskattning: 45 minuter
- XP: 80
- Föregående nod: docker_with_cicd
- Nästa nod: docker_best_practices_summary

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Docker Swarm vs Kubernetes - when to use
2. Swarm architecture (managers, workers)
3. docker swarm init och join
4. Services och tasks
5. Overlay networks i Swarm
6. Scaling services
7. Rolling updates och rollbacks
8. Secrets och configs i Swarm
9. Stack deploy med Compose files
10. Swarm monitoring och maintenance

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Swarm cluster setup"
- Initiera Swarm cluster (single-node)
- Skapa och skala services
- Inspektera cluster state
- Hantera service updates

**Övning 2 - Tillämpad (25 XP)**
Titel: "Multi-service deployment"
- Deploy en stack med docker stack deploy
- Konfigurera overlay networking
- Implementera secrets management
- Testa rolling updates

**Övning 3 - Utmanande (30 XP)**
Titel: "Production Swarm"
- Sätt upp multi-node Swarm (med Docker Machine eller VMs)
- Implementera high availability
- Konfigurera monitoring
- Dokumentera operational procedures

### DevOps-kontext:
- Swarm vs Kubernetes decision matrix
- Migration path till Kubernetes
- Edge computing med Swarm
- Hybrid deployments

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 17: Docker Best Practices Summary

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 17
- Titel: Docker Best Practices Summary
- Slug: docker_best_practices_summary
- Svårighetsgrad: Medium
- Tidsuppskattning: 40 minuter
- XP: 75
- Föregående nod: docker_swarm_basics
- Nästa nod: docker_development_workflow

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Dockerfile best practices checklist
2. Image building guidelines
3. Security hardening checklist
4. Networking best practices
5. Volume och data management
6. Compose patterns och anti-patterns
7. CI/CD integration guidelines
8. Production readiness checklist
9. Monitoring och logging standards
10. Documentation och tagging conventions

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Best practices audit"
- Granska en befintlig Dockerfile mot best practices
- Identifiera och dokumentera violations
- Föreslå förbättringar
- Prioritera åtgärder

**Övning 2 - Tillämpad (25 XP)**
Titel: "Refactoring project"
- Ta ett dåligt Docker-projekt
- Applicera all best practices
- Dokumentera före/efter
- Mät förbättringar (storlek, säkerhet, build time)

**Övning 3 - Utmanande (25 XP)**
Titel: "Best practices template"
- Skapa en organisation template repository
- Inkludera Dockerfile templates
- Skapa CI/CD templates
- Dokumentera standards

### DevOps-kontext:
- Organizational standards
- Compliance frameworks
- Code review guidelines
- DevOps maturity model

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 18: Docker Development Workflow

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 18
- Titel: Docker Development Workflow
- Slug: docker_development_workflow
- Svårighetsgrad: Lätt
- Tidsuppskattning: 40 minuter
- XP: 70
- Föregående nod: docker_best_practices_summary
- Nästa nod: docker_ecosystem_tools

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Local development med Docker
2. Hot-reload och live development
3. Dev containers och VS Code integration
4. Development vs production Dockerfiles
5. docker compose watch för development
6. Database seeding och migrations
7. Debugging i containers
8. Environment parity (dev/staging/prod)
9. Team onboarding med Docker
10. Local testing strategies

### Övningar att inkludera:

**Övning 1 - Grundläggande (20 XP)**
Titel: "Development environment"
- Sätt upp lokal dev environment med Compose
- Implementera hot-reload
- Konfigurera VS Code med containers
- Testa development workflow

**Övning 2 - Tillämpad (25 XP)**
Titel: "Full-stack development"
- Skapa development setup för full-stack app
- Implementera database migrations
- Sätt upp debugging
- Dokumentera onboarding process

**Övning 3 - Utmanande (25 XP)**
Titel: "Team workflow"
- Skapa standardiserat development setup
- Implementera environment parity
- Skapa automated testing
- Dokumentera team guidelines

### DevOps-kontext:
- Developer experience (DX)
- Inner loop optimization
- Team productivity metrics
- Onboarding automation

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 19: Docker Ecosystem & Tools

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 19
- Titel: Docker Ecosystem & Tools
- Slug: docker_ecosystem_tools
- Svårighetsgrad: Lätt
- Tidsuppskattning: 35 minuter
- XP: 65
- Föregående nod: docker_development_workflow
- Nästa nod: docker_certification_path

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Container alternatives (Podman, containerd, CRI-O)
2. Image building tools (Buildah, Kaniko, BuildKit)
3. Security tools (Trivy, Grype, Snyk, Clair)
4. Orchestration overview (Kubernetes, Nomad)
5. Registry solutions (Harbor, Quay, Artifactory)
6. Monitoring tools (cAdvisor, Prometheus)
7. GUI tools (Portainer, Lens, Docker Desktop)
8. Development tools (Dive, hadolint, dockle)
9. Cloud container services (ECS, ACI, Cloud Run)
10. CNCF landscape och container ecosystem

### Övningar att inkludera:

**Övning 1 - Grundläggande (20 XP)**
Titel: "Tool exploration"
- Installera och testa Podman som Docker-alternativ
- Använd Dive för image analysis
- Prova Portainer för GUI management
- Jämför tooling experience

**Övning 2 - Tillämpad (20 XP)**
Titel: "Security toolchain"
- Sätt upp security scanning pipeline
- Jämför Trivy vs Grype
- Implementera hadolint för linting
- Dokumentera security workflow

**Övning 3 - Utmanande (25 XP)**
Titel: "Ecosystem evaluation"
- Utvärdera container orchestration options
- Jämför registry solutions
- Skapa tool selection matrix
- Dokumentera recommendations

### DevOps-kontext:
- Tool evaluation criteria
- Vendor lock-in considerations
- Open source vs commercial
- Future-proofing decisions

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## PROMPT 20: Docker Certification Path

```
Du är en mass-content-generator för DevOpsHub. Generera EN KOMPLETT NOD enligt EXAKT denna struktur.

## METADATA
- Modul: docker_mastery
- Nod: 20
- Titel: Docker Certification Path
- Slug: docker_certification_path
- Svårighetsgrad: Medium
- Tidsuppskattning: 40 minuter
- XP: 75
- Föregående nod: docker_ecosystem_tools
- Nästa nod: null (sista noden)

## INNEHÅLLSKRAV

### Huvudteman att täcka:
1. Docker Certified Associate (DCA) overview
2. Exam domains och viktning
3. Kubernetes certifications (CKA, CKAD, CKS)
4. Cloud-specific certifications
5. Studiestrategier och resurser
6. Hands-on practice recommendations
7. Exam tips och format
8. Career paths med certifications
9. Continuous learning i container ecosystem
10. Community och networking

### Övningar att inkludera:

**Övning 1 - Grundläggande (25 XP)**
Titel: "Self-assessment"
- Genomför self-assessment mot DCA domains
- Identifiera kunskapsluckor
- Skapa personlig studieplan
- Sätt upp timeline

**Övning 2 - Tillämpad (25 XP)**
Titel: "Practice labs"
- Genomför hands-on labs för varje domain
- Dokumentera lärande
- Skapa flashcards för key concepts
- Ta practice tests

**Övning 3 - Utmanande (25 XP)**
Titel: "Certification roadmap"
- Skapa långsiktig certification roadmap
- Planera för Kubernetes certifications
- Identifiera karriärmål
- Dokumentera learning path

### DevOps-kontext:
- Certification ROI
- Industry demand
- Skill gap analysis
- Professional development

## STRUKTURKRAV

Generera EXAKT dessa 11 sektioner (INGA EMOJIS):

Generera EXAKT dessa 11 sektioner (INGA EMOJIS i rubriker):

1. Introduktion
2. Teori
3. 🎯 Steg-för-steg Guide
4. Praktiska Exempel
5. Basta Praxis
6. Vanliga Fallgropar
7. Ovningar (med <details>-taggar för lösningar)
8. Kopplingar
9. Sammanfattning
10. Nyckelkommandon
11. Referenser

## STILKRAV
- Skriv på SVENSKA
- Använd "du"-form genomgående
- Alla kodblock ska ha kommentarer
- Använd <details><summary>Lösning</summary>...</details> för övningslösningar
```

---

## Batch Processing Workflow

1. Kopiera en prompt åt gången till Opus
2. Verifiera output mot checklistan
3. Spara som `NOD_XX_slug.md`
4. Upprepa för nästa nod

**Uppskattad tid:** 20 noder × 15 min = ~5 timmar
