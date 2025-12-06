"""
Dallas FAQ Database - Förtränade svar baserade på plattformens innehåll.
Ingen GPT-kostnad - endast lokala svar från sidans faktiska innehåll.
"""

from typing import Optional, List, Tuple
import re

# FAQ-databas: (keywords, question_patterns, answer)
# Keywords används för snabb filtrering, patterns för bättre matching
FAQ_DATABASE: List[Tuple[List[str], List[str], str]] = [

    # === PLATTFORMEN ===
    (
        ["devopshub", "plattform", "vad är", "hur funkar"],
        ["vad är devopshub", "hur funkar sidan", "vad kan jag göra här"],
        """DevOpsHub är en lärplattform för DevOps! 🚀

Här kan du:
• **Camp DevOps** - Strukturerade moduler med tasks och XP
• **SkillsMaps** - Djupa lärvägar med 20 nodes per ämne
• **Studyflow** - Fokuserade studiesessioner
• **Skillpath Board** - Se din progress och planera din väg

Börja med att välja en modul i Camp DevOps eller utforska SkillsMaps!"""
    ),

    (
        ["camp", "devops", "modul", "moduler"],
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
        ["skillsmap", "skillsmaps", "lärvä", "nodes"],
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
        ["xp", "poäng", "level", "nivå", "progress"],
        ["hur får jag xp", "vad är xp", "hur fungerar poäng", "level"],
        """**XP-systemet** belönar ditt lärande!

• Slutför tasks → Få XP
• Svara rätt på quiz → Bonus XP
• Håll streaks → Extra belöningar

Din XP syns på Dashboard och i din profil. Ju mer du lär dig, desto högre level!"""
    ),

    (
        ["streak", "dag", "dagar", "rad"],
        ["vad är streak", "hur funkar streak", "streak"],
        """**Streaks** håller dig motiverad!

• Studera varje dag för att bygga din streak
• Längre streak = Mer dedikation
• Se din streak på Dashboard

Tips: Sätt ett dagligt mål för att hålla streaken vid liv!"""
    ),

    # === LINUX ===
    (
        ["linux", "kommando", "terminal", "bash", "skal"],
        ["linux kommando", "hur använder jag terminal", "bash"],
        """Linux-kommandon hittar du i **Linux Mastery** modulen.

Grundläggande kommandon täcks i modulen:
• Filhantering (ls, cd, cp, mv, rm)
• Texthantering (cat, grep, sed, awk)
• Permissions (chmod, chown)
• Processer (ps, top, kill)

Gå till Camp DevOps → Linux Mastery för kompletta lektioner!"""
    ),

    (
        ["chmod", "permission", "rättighet", "behörighet"],
        ["chmod", "permissions", "filrättigheter", "hur ändrar jag rättigheter"],
        """**Filrättigheter** täcks i Linux Mastery modulen.

Kort sammanfattning:
• `r` = read (läsa)
• `w` = write (skriva)
• `x` = execute (köra)

Exempel: `chmod 755 script.sh` (rwxr-xr-x)

För fullständig genomgång, gå till: Camp DevOps → Linux Mastery → File Permissions"""
    ),

    # === DOCKER ===
    (
        ["docker", "container", "image", "dockerfile"],
        ["docker", "vad är docker", "hur funkar containers"],
        """**Docker** täcks i Docker-modulen och SkillsMap.

Innehåll:
• Vad är containers och images
• Dockerfile-syntax
• docker-compose
• Volumes och networking
• Best practices

Gå till Camp DevOps → Docker eller SkillsMaps → Docker för att lära dig!"""
    ),

    # === KUBERNETES ===
    (
        ["kubernetes", "k8s", "pod", "deployment", "kubectl"],
        ["kubernetes", "k8s", "vad är kubernetes", "kubectl"],
        """**Kubernetes** täcks i Kubernetes-modulen och SkillsMap.

Innehåll:
• Pods, Deployments, Services
• kubectl-kommandon
• Helm charts
• Scaling och rollouts

Gå till Camp DevOps → Kubernetes eller SkillsMaps → Kubernetes!"""
    ),

    # === GIT ===
    (
        ["git", "github", "branch", "commit", "merge"],
        ["git", "github", "versionhantering", "hur funkar git"],
        """**Git & GitHub** täcks i Git-modulen och SkillsMap.

Innehåll:
• Grundläggande git-kommandon
• Branching och merging
• Pull requests
• GitHub Actions

Gå till Camp DevOps → Git & Workflows eller SkillsMaps → Git!"""
    ),

    # === AWS ===
    (
        ["aws", "amazon", "ec2", "s3", "lambda", "moln", "cloud"],
        ["aws", "amazon web services", "molntjänster", "ec2", "s3"],
        """**AWS** täcks i AWS Core-modulen och SkillsMap.

Innehåll:
• EC2 (virtuella servrar)
• S3 (lagring)
• IAM (behörigheter)
• VPC (nätverk)
• Lambda (serverless)

Gå till Camp DevOps → AWS Core eller SkillsMaps → AWS!"""
    ),

    # === TERRAFORM ===
    (
        ["terraform", "iac", "infrastructure", "infra"],
        ["terraform", "infrastructure as code", "iac"],
        """**Terraform** täcks i Terraform-modulen och SkillsMap.

Innehåll:
• HCL-syntax
• Providers och resources
• Modules
• State management

Gå till Camp DevOps → Terraform eller SkillsMaps → Terraform!"""
    ),

    # === CI/CD ===
    (
        ["cicd", "ci/cd", "pipeline", "jenkins", "github actions"],
        ["ci/cd", "pipeline", "deployment", "continuous"],
        """**CI/CD** täcks i CI/CD Pipelines-modulen och SkillsMap.

Innehåll:
• GitHub Actions
• GitLab CI
• Jenkins
• Deployment strategies

Gå till Camp DevOps → CI/CD eller SkillsMaps → CI/CD Pipelines!"""
    ),

    # === PYTHON ===
    (
        ["python", "scripting", "automation", "boto3"],
        ["python", "python för devops", "scripting"],
        """**Python for DevOps** täcks i Python-modulen och SkillsMap.

Innehåll:
• Python-grunder för automation
• boto3 (AWS SDK)
• subprocess och os-moduler
• JSON/YAML-hantering

Gå till Camp DevOps → Python for DevOps eller SkillsMaps → Python!"""
    ),

    # === HJÄLP & SUPPORT ===
    (
        ["hjälp", "support", "problem", "fel", "funkar inte"],
        ["hjälp", "support", "något funkar inte", "problem"],
        """Behöver du hjälp? 🤝

• **Tekniska problem** - Prova ladda om sidan
• **Frågor om innehåll** - Fråga mig om specifika ämnen
• **Hittar inte något** - Beskriv vad du letar efter

Du kan också kolla Help-sidan i menyn för mer information."""
    ),

    (
        ["dallas", "du", "vem", "assistent", "ai"],
        ["vem är du", "vad är dallas", "vad kan du hjälpa med"],
        """Jag är **Dallas** 🐺 - din guide på DevOpsHub!

Jag kan hjälpa dig med:
• Förklara vad som finns på plattformen
• Guida dig till rätt modul eller SkillsMap
• Svara på frågor om plattformens innehåll

Ställ en fråga så hjälper jag dig hitta rätt!"""
    ),
]

# Fallback-svar när ingen match hittas
NO_MATCH_RESPONSE = """Jag hittade tyvärr inget svar på din fråga i vårt innehåll. 🤔

**Tips:**
• Prova att omformulera frågan
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
        score += 0.3 * min(keyword_matches / len(keywords), 1.0)

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

    # Require minimum confidence of 0.3
    if best_score >= 0.3:
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
