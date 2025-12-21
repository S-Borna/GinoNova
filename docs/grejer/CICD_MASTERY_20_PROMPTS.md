# CI/CD Mastery - 20 Opus-promptar

## Modulöversikt

| Prompt | Titel | Svårighetsgrad | Tid | XP |
|--------|-------|----------------|-----|-----|
| 1 | Introduction to CI/CD | Medium | 15 min | 30 |
| 2 | GitHub Actions Fundamentals | Medium | 15 min | 30 |
| 3 | GitLab CI/CD | Medium | 15 min | 30 |
| 4 | Jenkins Pipelines | Medium | 15 min | 30 |
| 5 | Testing in Pipelines | Medium | 15 min | 30 |
| 6 | Build & Release Strategies | Medium | 15 min | 30 |
| 7 | GitLab CI Deep Dive | Medium | 15 min | 30 |
| 8 | Azure DevOps Pipelines | Medium | 15 min | 30 |
| 9 | Container-based CI/CD | Medium | 15 min | 30 |
| 10 | GitOps with ArgoCD | Medium | 15 min | 30 |
| 11 | Secrets Management in CI/CD | Medium | 15 min | 30 |
| 12 | Pipeline Optimization | Medium | 15 min | 30 |
| 13 | Multi-Environment Deployments | Medium | 15 min | 30 |
| 14 | Monitoring CI/CD Pipelines | Medium | 15 min | 30 |
| 15 | Compliance and Audit | Medium | 15 min | 30 |
| 16 | Disaster Recovery for CI/CD | Medium | 15 min | 30 |
| 17 | CircleCI and Other Platforms | Medium | 15 min | 30 |
| 18 | Self-Hosted Runners | Medium | 15 min | 30 |
| 19 | Monorepo CI/CD Patterns | Medium | 15 min | 30 |
| 20 | Enterprise CI/CD Patterns | Medium | 15 min | 30 |

**Totalt:** ~5 timmar, 600 XP

---

## Prompt 1: Introduction to CI/CD

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 1 av 20
- **Titel:** Introduction to CI/CD
- **Slug:** cicd-introduction
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** (ingen - första i modulen)
- **Nästa:** GitHub Actions Fundamentals

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Introduction to CI/CD**.

### Huvudteman att täcka (10 st):
1. Continuous Integration (CI) - definition, principer, fördelar
2. Continuous Delivery vs Continuous Deployment - skillnader och användningsområden
3. Pipeline-anatomi - stages, jobs, steps, triggers
4. DevOps-kultur och CI/CD:s roll i organisationen
5. Build automation och reproducerbarhet
6. Feedback loops och "fail fast"-principen
7. Version control integration och branching-strategier
8. Artifact management och versionering
9. DORA metrics och mätning av CI/CD-effektivitet
10. CI/CD anti-patterns och vanliga misstag

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Rita upp en CI/CD-pipeline med minst 5 stages för en typisk webbapplikation.

**Övning 2 - Tillämpad (10 XP)**
Analysera ett befintligt projekt och identifiera vilka CI/CD-förbättringar som skulle ge störst effekt.

**Övning 3 - Utmanande (10 XP)**
Skapa en plan för att införa CI/CD i en organisation som idag gör manuella deployments.

### DevOps-kontext:
- Startups som vill accelerera releases
- Enterprise-team som moderniserar legacy-system
- Platform-team som bygger interna developer platforms
- Konsulter som hjälper kunder införa DevOps

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 2: GitHub Actions Fundamentals

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 2 av 20
- **Titel:** GitHub Actions Fundamentals
- **Slug:** github-actions-fundamentals
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Introduction to CI/CD
- **Nästa:** GitLab CI/CD

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **GitHub Actions Fundamentals**.

### Huvudteman att täcka (10 st):
1. GitHub Actions arkitektur - workflows, jobs, steps, runners
2. YAML-syntax och workflow-filer i .github/workflows/
3. Triggers - push, pull_request, schedule, workflow_dispatch
4. GitHub-hosted vs self-hosted runners
5. Actions marketplace och community actions
6. Secrets och environment variables
7. Matrix builds och parallella jobb
8. Caching och artifact management
9. Reusable workflows och composite actions
10. Debugging och troubleshooting av workflows

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en enkel workflow som kör tester vid varje push till main-branchen.

**Övning 2 - Tillämpad (10 XP)**
Implementera en matrix build som testar mot flera Node.js-versioner och operativsystem.

**Övning 3 - Utmanande (10 XP)**
Skapa en reusable workflow som kan användas av flera repositories.

### DevOps-kontext:
- Open source-projekt med community contributions
- Små team som vill ha snabb uppsättning utan infrastruktur
- Enterprise med GitHub Enterprise Server
- Migrering från andra CI-system till GitHub Actions

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 3: GitLab CI/CD

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 3 av 20
- **Titel:** GitLab CI/CD
- **Slug:** gitlab-cicd
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** GitHub Actions Fundamentals
- **Nästa:** Jenkins Pipelines

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **GitLab CI/CD**.

### Huvudteman att täcka (10 st):
1. GitLab CI/CD arkitektur och integration med GitLab
2. .gitlab-ci.yml syntax och struktur
3. Stages, jobs och pipeline-design
4. GitLab Runners - shared, group, project runners
5. Variables och secrets i GitLab
6. Artifacts och cache
7. Auto DevOps och templates
8. Environments och deployment tracking
9. Merge request pipelines och review apps
10. GitLab CI vs GitHub Actions - jämförelse

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en grundläggande .gitlab-ci.yml med build, test och deploy stages.

**Övning 2 - Tillämpad (10 XP)**
Implementera en pipeline med artifacts som skickas mellan stages.

**Övning 3 - Utmanande (10 XP)**
Konfigurera review apps som skapas automatiskt för merge requests.

### DevOps-kontext:
- Organisationer som använder GitLab som allt-i-ett DevOps-plattform
- Migrering från Jenkins till GitLab CI
- Self-hosted GitLab-installationer
- GitLab.com SaaS-användare

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 4: Jenkins Pipelines

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 4 av 20
- **Titel:** Jenkins Pipelines
- **Slug:** jenkins-pipelines
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** GitLab CI/CD
- **Nästa:** Testing in Pipelines

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Jenkins Pipelines**.

### Huvudteman att täcka (10 st):
1. Jenkins arkitektur - master, agents, executors
2. Declarative vs Scripted Pipeline syntax
3. Jenkinsfile och Pipeline-as-Code
4. Stages, steps och post-actions
5. Jenkins plugins ekosystem
6. Shared libraries för återanvändbar kod
7. Blue Ocean UI och pipeline visualization
8. Jenkins X och cloud-native Jenkins
9. Security och credentials management
10. Jenkins i container-miljöer

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en Declarative Pipeline med build, test och deploy stages.

**Övning 2 - Tillämpad (10 XP)**
Implementera en shared library med återanvändbara pipeline-steg.

**Övning 3 - Utmanande (10 XP)**
Migrera en komplex Scripted Pipeline till Declarative syntax.

### DevOps-kontext:
- Enterprise med befintlig Jenkins-infrastruktur
- Team som moderniserar från freestyle jobs till Pipeline
- Organisationer med komplexa approval-workflows
- Hybrid cloud-miljöer med legacy-integration

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 5: Testing in Pipelines

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 5 av 20
- **Titel:** Testing in Pipelines
- **Slug:** testing-in-pipelines
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Jenkins Pipelines
- **Nästa:** Build & Release Strategies

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Testing in Pipelines**.

### Huvudteman att täcka (10 st):
1. Test pyramid och teststrategier i CI/CD
2. Unit tests - snabba, isolerade, högt coverage
3. Integration tests - databas, API, externa tjänster
4. End-to-end tests - Selenium, Cypress, Playwright
5. Test coverage och quality gates
6. Parallel test execution för snabbare feedback
7. SAST och DAST security testing
8. Performance och load testing i pipelines
9. Test data management och fixtures
10. Test reporting och visualization

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Konfigurera en pipeline som kör unit tests och rapporterar coverage.

**Övning 2 - Tillämpad (10 XP)**
Implementera parallella test jobs med test splitting.

**Övning 3 - Utmanande (10 XP)**
Skapa en quality gate som blockerar deployment vid otillräcklig coverage.

### DevOps-kontext:
- Team som vill införa test-driven development
- Legacy-system som behöver tester före modernisering
- Regulated industries med compliance-krav på testning
- Microservices med komplexa integrationsberoenden

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 6: Build & Release Strategies

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 6 av 20
- **Titel:** Build & Release Strategies
- **Slug:** build-release-strategies
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Testing in Pipelines
- **Nästa:** GitLab CI Deep Dive

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Build & Release Strategies**.

### Huvudteman att täcka (10 st):
1. Semantic Versioning (SemVer) och release naming
2. Branching strategies - GitFlow, GitHub Flow, Trunk-based
3. Blue-green deployments
4. Canary releases och progressive delivery
5. Feature flags och feature toggles
6. Rolling updates och zero-downtime deployments
7. Rollback strategies och disaster recovery
8. Release trains och scheduled releases
9. Hotfix workflows och emergency patches
10. Release notes automation och changelog generation

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Implementera automatisk versioning med SemVer baserat på commit messages.

**Övning 2 - Tillämpad (10 XP)**
Skapa en blue-green deployment pipeline med automatisk rollback.

**Övning 3 - Utmanande (10 XP)**
Implementera canary releases med gradvis traffic shifting.

### DevOps-kontext:
- E-commerce med höga tillgänglighetskrav
- SaaS-produkter med kontinuerliga releases
- Mobile backends med app store review-cykler
- Enterprise med change management-processer

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 7: GitLab CI Deep Dive

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 7 av 20
- **Titel:** GitLab CI Deep Dive
- **Slug:** gitlab-ci-deep-dive
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Build & Release Strategies
- **Nästa:** Azure DevOps Pipelines

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **GitLab CI Deep Dive**.

### Huvudteman att täcka (10 st):
1. DAG (Directed Acyclic Graph) pipelines och needs keyword
2. Parent-child pipelines och multi-project pipelines
3. CI/CD components och include templates
4. Dynamic pipelines med rules och workflow
5. Review apps och dynamic environments
6. Security scanning (SAST, DAST, dependency scanning)
7. Container registry och package registry integration
8. Compliance pipelines och audit trails
9. GitLab Pages och static site deployment
10. Performance optimization och pipeline caching

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Implementera en DAG pipeline med parallella och beroende jobs.

**Övning 2 - Tillämpad (10 XP)**
Skapa en parent-child pipeline för ett multi-service projekt.

**Övning 3 - Utmanande (10 XP)**
Konfigurera compliance pipeline med mandatory security scans.

### DevOps-kontext:
- Stora organisationer med komplexa pipeline-behov
- Security-fokuserade team med compliance-krav
- Monorepos med många services
- Platform teams som bygger CI/CD templates

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 8: Azure DevOps Pipelines

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 8 av 20
- **Titel:** Azure DevOps Pipelines
- **Slug:** azure-devops-pipelines
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** GitLab CI Deep Dive
- **Nästa:** Container-based CI/CD

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Azure DevOps Pipelines**.

### Huvudteman att täcka (10 st):
1. Azure Pipelines arkitektur - YAML vs Classic
2. Stages, jobs och tasks i YAML pipelines
3. Trigger och schedule configuration
4. Environments och deployment approvals
5. Variable groups och secrets management
6. Templates och pipeline reuse
7. Azure Artifacts integration
8. Service connections och Azure integration
9. Self-hosted agents vs Microsoft-hosted
10. Azure DevOps vs GitHub Actions

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en YAML pipeline med build, test och deploy stages.

**Övning 2 - Tillämpad (10 XP)**
Implementera deployment med approvals och environment gates.

**Övning 3 - Utmanande (10 XP)**
Skapa pipeline templates som kan återanvändas mellan projekt.

### DevOps-kontext:
- Microsoft-centrerade organisationer
- .NET och Azure-ekosystem
- Enterprise med Azure AD integration
- Hybrid cloud med on-premises och Azure

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 9: Container-based CI/CD

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 9 av 20
- **Titel:** Container-based CI/CD
- **Slug:** container-based-cicd
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Azure DevOps Pipelines
- **Nästa:** GitOps with ArgoCD

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Container-based CI/CD**.

### Huvudteman att täcka (10 st):
1. Docker builds i CI/CD pipelines
2. Container registries (Docker Hub, ECR, GCR, ACR)
3. Image tagging strategies och versioning
4. Container scanning och vulnerability detection
5. Multi-stage builds för optimerade images
6. Kaniko och rootless container builds
7. Multi-arch builds för ARM och AMD64
8. Cache optimization för snabbare builds
9. Deployment till Kubernetes från CI/CD
10. GitOps-ready container workflows

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en pipeline som bygger och pushar Docker images till ett registry.

**Övning 2 - Tillämpad (10 XP)**
Implementera container scanning med Trivy/Snyk som quality gate.

**Övning 3 - Utmanande (10 XP)**
Skapa multi-arch builds som stödjer både ARM64 och AMD64.

### DevOps-kontext:
- Kubernetes-first organisationer
- Microservices-arkitekturer
- Edge computing med ARM-enheter
- Security-fokuserade team med supply chain concerns

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 10: GitOps with ArgoCD

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 10 av 20
- **Titel:** GitOps with ArgoCD
- **Slug:** gitops-argocd
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Container-based CI/CD
- **Nästa:** Secrets Management in CI/CD

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **GitOps with ArgoCD**.

### Huvudteman att täcka (10 st):
1. GitOps principer - deklarativ, versionerad, automatiserad
2. ArgoCD arkitektur och komponenter
3. Application och ApplicationSet resources
4. Sync policies och auto-sync
5. Health checks och status monitoring
6. Multi-cluster management
7. Kustomize och Helm integration
8. RBAC och project isolation
9. ArgoCD vs Flux - jämförelse
10. Progressive delivery med Argo Rollouts

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Installera ArgoCD och deploy en enkel applikation från Git.

**Övning 2 - Tillämpad (10 XP)**
Konfigurera ApplicationSet för multi-environment deployment.

**Övning 3 - Utmanande (10 XP)**
Implementera canary deployment med Argo Rollouts.

### DevOps-kontext:
- Kubernetes-native organisationer
- Multi-cluster enterprise deployments
- Platform teams som vill ge self-service till dev teams
- Compliance-krav på audit trails för deployments

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 11: Secrets Management in CI/CD

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 11 av 20
- **Titel:** Secrets Management in CI/CD
- **Slug:** secrets-management-cicd
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** GitOps with ArgoCD
- **Nästa:** Pipeline Optimization

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Secrets Management in CI/CD**.

### Huvudteman att täcka (10 st):
1. Secrets management principer - never commit, rotate, audit
2. Platform-specifika secrets (GitHub Secrets, GitLab CI Variables)
3. HashiCorp Vault integration i pipelines
4. AWS Secrets Manager och Parameter Store
5. Azure Key Vault integration
6. External Secrets Operator för Kubernetes
7. SOPS och age för encrypted secrets i Git
8. Dynamic secrets och short-lived credentials
9. Secrets scanning och leak detection
10. Audit trails och compliance för secrets access

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Konfigurera secrets i GitHub Actions och använd dem säkert i pipelines.

**Övning 2 - Tillämpad (10 XP)**
Integrera HashiCorp Vault med en CI/CD pipeline för dynamic secrets.

**Övning 3 - Utmanande (10 XP)**
Implementera External Secrets Operator för att synka secrets till Kubernetes.

### DevOps-kontext:
- Regulated industries med strikta compliance-krav
- Multi-cloud organisationer med centraliserad secrets management
- Security teams som vill ha kontroll och audit
- DevSecOps-kultur med security shift-left

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 12: Pipeline Optimization

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 12 av 20
- **Titel:** Pipeline Optimization
- **Slug:** pipeline-optimization
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Secrets Management in CI/CD
- **Nästa:** Multi-Environment Deployments

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Pipeline Optimization**.

### Huvudteman att täcka (10 st):
1. Caching strategies - dependencies, build artifacts, layers
2. Parallelization och fan-out/fan-in patterns
3. Incremental builds och change detection
4. Resource allocation och right-sizing
5. Queue management och concurrency limits
6. Flaky test detection och quarantine
7. Pipeline analytics och bottleneck identification
8. Cost optimization för cloud-hosted runners
9. Fail-fast strategies och early termination
10. Build time benchmarking och tracking

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Implementera dependency caching som halverar build-tiden.

**Övning 2 - Tillämpad (10 XP)**
Konfigurera parallella test jobs med intelligent test splitting.

**Övning 3 - Utmanande (10 XP)**
Skapa en dashboard som trackar build times och identifierar regressioner.

### DevOps-kontext:
- Stora monorepos med långa build-tider
- Teams som vill sänka CI/CD-kostnader
- Organisationer med developer experience-fokus
- Snabb feedback-loop som critical path

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 13: Multi-Environment Deployments

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 13 av 20
- **Titel:** Multi-Environment Deployments
- **Slug:** multi-environment-deployments
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Pipeline Optimization
- **Nästa:** Monitoring CI/CD Pipelines

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Multi-Environment Deployments**.

### Huvudteman att täcka (10 st):
1. Environment strategier - dev, staging, production
2. Environment-specifik configuration management
3. Promotion workflows och approval gates
4. Database migrations across environments
5. Feature environments och preview deployments
6. Infrastructure as Code per environment
7. Environment parity och drift prevention
8. Teardown och cleanup automation
9. Cost management för multiple environments
10. Testing strategies per environment level

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en pipeline som deployer till dev och staging med olika configs.

**Övning 2 - Tillämpad (10 XP)**
Implementera promotion workflow med manual approval för production.

**Övning 3 - Utmanande (10 XP)**
Skapa ephemeral preview environments för varje pull request.

### DevOps-kontext:
- SaaS-produkter med multiple tenants
- Enterprise med strikt separation mellan miljöer
- Startups som behöver snabb iteration i dev
- Regulated industries med mandatory staging

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 14: Monitoring CI/CD Pipelines

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 14 av 20
- **Titel:** Monitoring CI/CD Pipelines
- **Slug:** monitoring-cicd-pipelines
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Multi-Environment Deployments
- **Nästa:** Compliance and Audit

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Monitoring CI/CD Pipelines**.

### Huvudteman att täcka (10 st):
1. DORA metrics implementation (deployment frequency, lead time, etc.)
2. Pipeline dashboards och visualization
3. Alerting på build failures och anomalies
4. Build time trends och regression detection
5. Deployment tracking och rollback metrics
6. Test result aggregation och flaky test detection
7. Cost monitoring för CI/CD infrastructure
8. Integration med observability platforms (Datadog, Grafana)
9. Incident correlation mellan deployments och issues
10. Executive reporting och engineering metrics

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Konfigurera notifications för build failures till Slack/Teams.

**Övning 2 - Tillämpad (10 XP)**
Bygg en dashboard som visar DORA metrics för teamet.

**Övning 3 - Utmanande (10 XP)**
Implementera automatic correlation mellan deployments och error rates.

### DevOps-kontext:
- Engineering managers som behöver metrics
- Platform teams som supportar många team
- Organizations som implementerar DevOps transformation
- SRE teams som vill förstå deployment impact

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 15: Compliance and Audit

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 15 av 20
- **Titel:** Compliance and Audit
- **Slug:** compliance-audit
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Monitoring CI/CD Pipelines
- **Nästa:** Disaster Recovery for CI/CD

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Compliance and Audit**.

### Huvudteman att täcka (10 st):
1. Compliance frameworks (SOC2, HIPAA, PCI-DSS, GDPR)
2. Audit trails för deployments och changes
3. Mandatory approvals och separation of duties
4. Immutable build artifacts och provenance
5. Security scanning requirements
6. Change management integration
7. Signed commits och verified pipelines
8. Retention policies för logs och artifacts
9. Compliance-as-Code och automated checks
10. Audit reports och evidence collection

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Konfigurera mandatory code review och approval för main branch.

**Övning 2 - Tillämpad (10 XP)**
Implementera audit logging för alla pipeline executions.

**Övning 3 - Utmanande (10 XP)**
Skapa compliance pipeline som genererar evidence för SOC2 audit.

### DevOps-kontext:
- Fintech med PCI-DSS krav
- Healthcare med HIPAA compliance
- Enterprise som förbereder SOC2 certification
- Government contractors med strict audit requirements

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 16: Disaster Recovery for CI/CD

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 16 av 20
- **Titel:** Disaster Recovery for CI/CD
- **Slug:** disaster-recovery-cicd
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Compliance and Audit
- **Nästa:** CircleCI and Other Platforms

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Disaster Recovery for CI/CD**.

### Huvudteman att täcka (10 st):
1. CI/CD system som single point of failure
2. Backup strategies för pipeline configuration
3. High availability för self-hosted CI/CD
4. Cross-region och multi-cloud DR
5. Rollback procedures och versioned configs
6. Secret recovery och key rotation
7. Runner fleet redundancy
8. Incident response för CI/CD outages
9. Testing DR procedures regularly
10. Business continuity planning

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa backup av all pipeline configuration till separat repository.

**Övning 2 - Tillämpad (10 XP)**
Implementera fallback till alternativ CI/CD platform.

**Övning 3 - Utmanande (10 XP)**
Designa och testa full DR procedure för CI/CD infrastructure.

### DevOps-kontext:
- Mission-critical applications med höga SLAs
- Regulated industries med DR requirements
- Multi-region deployments
- Organizations med strict RTO/RPO targets

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 17: CircleCI and Other Platforms

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 17 av 20
- **Titel:** CircleCI and Other Platforms
- **Slug:** circleci-other-platforms
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Disaster Recovery for CI/CD
- **Nästa:** Self-Hosted Runners

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **CircleCI and Other Platforms**.

### Huvudteman att täcka (10 st):
1. CircleCI arkitektur och config.yml
2. CircleCI orbs och reusable configuration
3. Travis CI för open source
4. Buildkite för enterprise
5. TeamCity och JetBrains ecosystem
6. Drone CI för container-native workflows
7. Tekton för Kubernetes-native CI/CD
8. Comparison matrix för CI/CD platforms
9. Migration strategies mellan platforms
10. Vendor lock-in considerations

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Skapa en CircleCI config.yml för ett Node.js projekt.

**Övning 2 - Tillämpad (10 XP)**
Migrera en GitHub Actions workflow till CircleCI format.

**Övning 3 - Utmanande (10 XP)**
Skapa en platform-agnostic CI/CD abstraction layer.

### DevOps-kontext:
- Teams som utvärderar CI/CD platforms
- Organizations som migrerar från legacy CI
- Multi-platform strategies
- Open source maintainers

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 18: Self-Hosted Runners

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 18 av 20
- **Titel:** Self-Hosted Runners
- **Slug:** self-hosted-runners
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** CircleCI and Other Platforms
- **Nästa:** Monorepo CI/CD Patterns

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Self-Hosted Runners**.

### Huvudteman att täcka (10 st):
1. Self-hosted vs cloud-hosted runners - trade-offs
2. GitHub Actions self-hosted runner setup
3. GitLab Runner configuration och registration
4. Runner på Kubernetes med actions-runner-controller
5. Runner fleet management och autoscaling
6. Security hardening för runners
7. Ephemeral runners och clean environments
8. GPU och specialized hardware runners
9. On-premises integration
10. Cost analysis och break-even calculations

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Installera och registrera en self-hosted GitHub Actions runner.

**Övning 2 - Tillämpad (10 XP)**
Konfigurera autoscaling runners på Kubernetes.

**Övning 3 - Utmanande (10 XP)**
Implementera ephemeral runners med automatic cleanup.

### DevOps-kontext:
- Security-sensitive organizations med on-premises requirements
- Cost-conscious teams med high CI/CD usage
- Specialized hardware needs (GPU, ARM)
- Hybrid cloud environments

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 19: Monorepo CI/CD Patterns

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 19 av 20
- **Titel:** Monorepo CI/CD Patterns
- **Slug:** monorepo-cicd-patterns
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Self-Hosted Runners
- **Nästa:** Enterprise CI/CD Patterns

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Monorepo CI/CD Patterns**.

### Huvudteman att täcka (10 st):
1. Monorepo benefits och challenges för CI/CD
2. Change detection och affected targets
3. Nx, Turborepo, Bazel för monorepo builds
4. Path-based triggers och selective pipelines
5. Dependency graph och build ordering
6. Caching strategies för monorepos
7. Parallel builds och distributed execution
8. Versioning och releasing from monorepos
9. Team ownership och CODEOWNERS
10. Scaling CI/CD för large monorepos

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Konfigurera path-based triggers för ett monorepo.

**Övning 2 - Tillämpad (10 XP)**
Implementera Nx affected builds för smart change detection.

**Övning 3 - Utmanande (10 XP)**
Skapa distributed build pipeline med remote caching.

### DevOps-kontext:
- Large organizations med many interconnected services
- Platform teams managing shared libraries
- Startups choosing repo strategy
- Migration from polyrepo to monorepo

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Prompt 20: Enterprise CI/CD Patterns

```markdown
# Opus Content Generation Prompt

## Metadata
- **Modul:** CI/CD Mastery
- **Node:** 20 av 20
- **Titel:** Enterprise CI/CD Patterns
- **Slug:** enterprise-cicd-patterns
- **Svårighetsgrad:** Medium
- **Beräknad tid:** 15 minuter
- **XP:** 30
- **Föregående:** Monorepo CI/CD Patterns
- **Nästa:** (ingen - sista i modulen)

## Uppdrag

Skapa en pedagogiskt strukturerad utbildningstext om **Enterprise CI/CD Patterns**.

### Huvudteman att täcka (10 st):
1. Internal Developer Platform (IDP) koncept
2. Golden paths och standardized pipelines
3. Self-service och platform as a product
4. Multi-tenant CI/CD platforms
5. Governance och centralized control
6. Template libraries och reusable components
7. Integration med enterprise tools (ServiceNow, Jira)
8. Metrics och executive reporting
9. Cost allocation och chargeback
10. CI/CD maturity models

### Övningar (3 st):

**Övning 1 - Grundläggande (10 XP)**
Designa en golden path för en standard microservice.

**Övning 2 - Tillämpad (10 XP)**
Skapa ett template library för common pipeline patterns.

**Övning 3 - Utmanande (10 XP)**
Implementera cost allocation dashboard för CI/CD usage per team.

### DevOps-kontext:
- Platform engineering teams
- Enterprise DevOps transformation
- Large organizations with many development teams
- Cost-conscious IT leadership

### Struktur att följa:
1. 🎯 Introduktion med hook och varför detta är viktigt
2. 📚 Förkunskaper och koppling till tidigare innehåll
3. 🎯 Tydliga lärandemål (3-5 mål)
4. 💡 Huvudinnehåll med koncept, förklaringar, exempel
5. ✅ Best practices och branschstandard
6. ⚠️ Vanliga misstag att undvika
7. 🏋️ Övningar med tydliga instruktioner och XP
8. 🔗 Koppling till andra noder i grafen
9. 📝 Sammanfattning och key takeaways
10. 🔑 Nyckelbegrepp och definitioner
11. 📚 Referenser och fördjupning

### Stil:
- Svenska språket genomgående
- "Du"-tilltal, engagerande och pedagogiskt
- Kodexempel med kommentarer
- Praktiska tips i <details>-taggar
- Progression från grundläggande till avancerat
```

---

## Sammanfattning

**CI/CD Mastery** innehåller 20 prompts som täcker:

- **Grundläggande CI/CD:** Koncept, pipelines, DevOps-kultur
- **Platforms:** GitHub Actions, GitLab CI, Jenkins, Azure DevOps, CircleCI
- **Advanced:** GitOps, secrets, containers, testing
- **Enterprise:** Compliance, DR, monorepos, platform engineering

**Total tid:** ~5 timmar
**Total XP:** 600

Alla prompts är Medium svårighetsgrad för konsistent progression genom modulen.
