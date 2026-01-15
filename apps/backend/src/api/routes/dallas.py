"""
Dallas Chat API - Billig GPT för pulsmätning
=============================================

Använder GPT-3.5-turbo (billigast) för enkla samtal.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import os
import random

router = APIRouter(prefix="/dallas", tags=["dallas"])


class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = "general"
    user_name: Optional[str] = "du"
    user_id: Optional[str] = None  # For usage tracking


class ChatResponse(BaseModel):
    response: str
    context: str


# Fallback-svar om OpenAI inte är konfigurerad
FALLBACK_RESPONSES = {
    "pulse_check": [
        "Tack för att du delar! Det är viktigt att checka in med sig själv. Vad skulle hjälpa dig mest just nu - lite lugn repetition med flashcards eller en utmaning med quiz? 🎯",
        "Jag hör dig! DevOps-resan har sina upp och nedgångar. Kom ihåg att varje liten bit räknas. Vill du att vi fokuserar på något specifikt idag? 💪",
        "Det låter som att du har mycket på gång! Ta det i din egen takt. Ska vi börja med något enkelt för att komma igång? 🌟",
        "Tack för att du är ärlig! Det är första steget. Vill du prata mer om det, eller ska vi hoppa in i lite lärande? 📚",
        "Jag förstår helt! Ibland behöver man bara ta ett andetag. När du känner dig redo finns jag här. Vad lockar dig mest - Linux, Docker eller något annat? 🐺",
    ],
    "general": [
        "Intressant fråga! Berätta mer så hjälper jag dig. 🤔",
        "Jag är här för att guida dig genom DevOps-djungeln! Vad vill du veta mer om? 🌴",
        "Bra att du frågar! Låt oss utforska det tillsammans. 🚀",
    ]
}


@router.post("/chat", response_model=ChatResponse)
async def chat_with_dallas(request: ChatRequest):
    """
    Chatta med Dallas - din DevOps-guide.
    Försöker använda OpenAI GPT-3.5-turbo, annars fallback.
    """
    from uuid import UUID as UUIDType
    from ...services.ai_usage_service import log_ai_usage

    # Try multiple env var names for OpenAI key (OPENAI_KEY first - Railway config)
    openai_key = os.getenv("OPENAI_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("OPEN_AI_KEY")

    # Debug: Log which key was found
    print(f"Dallas: OPENAI_KEY={'set' if os.getenv('OPENAI_KEY') else 'not set'}")
    print(f"Dallas: OPENAI_API_KEY={'set' if os.getenv('OPENAI_API_KEY') else 'not set'}")
    print(f"Dallas: openai_key={'found' if openai_key else 'NOT FOUND'}")

    if openai_key:
        try:
            import openai
            client = openai.OpenAI(api_key=openai_key)

            system_prompt = f"""Du är Dallas 🐺, en vänlig DevOps-guide på GinoNova.
Du pratar svenska och är stöttande, varm och pedagogisk.
Användaren heter {request.user_name}.

VIKTIGT BETEENDE:
- Säg INTE "Hej {request.user_name}" i varje svar - endast vid första kontakten
- Svara direkt på frågan utan onödiga hälsningar
- Håll svaren korta och koncisa (max 2-3 meningar)
- Använd emojis sparsamt men kärleksfullt 🐺

=== GINONOVA SITE KNOWLEDGE ===

**HUVUDNAVIGATION** (använd dessa exakta länkar):
- Dashboard: /dashboard
- Camp DevOps (3 huvudmoduler): /modules
- SkillsMaps (31+ moduler): /skillsmaps
- FastTrack (DevOps-verktyg): /fasttrack
- AI Quiz Generator: /quiz
- Code Playground: /playground
- Studyroom: /study
- Skillpath Board: /skillpath-board
- Pulsmätning: /pulse
- Community: /community
- Analytics: /analytics
- Progress: /progress
- Certificates: /certificates
- Settings: /settings
- Help Center: /help

**CAMP DEVOPS MODULER** (endast 3 moduler på /modules):
1. Linux 24/7: /modules/linux-247 (Linux-grunder, terminalen, processer)
2. Linux Tentaplugg: /modules/linux-tentaplugg (Tentafokuserat innehåll)
3. Hands-On Lab: /modules/hands-on-lab (Praktiska övningar)

**SKILLSMAPS** (31+ avancerade moduler på /skillsmaps/[slug]):
Core Skills:
- kubernetes-fundamentals (Container orchestration)
- cicd-pipelines-advanced (Avancerade pipelines)
- terraform-iac (Infrastructure as Code)
- ansible-automation (Configuration Management)
- python-for-devops (Python automation)
- prompt-engineering-devops (AI för DevOps)

Cloud Platforms:
- aws-fundamentals (Amazon Web Services)
- azure-fundamentals (Microsoft Azure)
- gcp-fundamentals (Google Cloud Platform)
- multicloud-architecture (Multi-cloud strategier)

Monitoring:
- prometheus-monitoring (Metrics & alerting)
- grafana-visualization (Dashboards)
- elk-stack (Logging stack)
- datadog-monitoring (Full-stack observability)

Databases:
- postgresql-fundamentals (Relationsdatabas)
- redis-caching (In-memory databas)
- mongodb-fundamentals (NoSQL)

Messaging:
- kafka-streams (Event streaming)
- rabbitmq-messaging (Message broker)

Networking:
- istio-service-mesh (Service mesh)
- nginx-reverse-proxy (Load balancer & proxy)

Security:
- devsecops-security (Security integration)
- vault-secrets (Secrets management)

CI/CD Advanced:
- jenkins-advanced (Advanced pipelines)
- gitlab-ci-cd (GitLab CI/CD)
- argocd-gitops (GitOps deployment)

Languages:
- go-for-devops (Go programming)
- yaml-json-fundamentals (Data formats)

**FASTTRACK VERKTYG** (länka till /fasttrack eller /fasttrack/[tool-slug]):
DevOps-verktyg med flashcards, quiz och kodexempel:
- Docker, Kubernetes, Terraform, Ansible
- AWS CLI, Git, Bash, Python
- Nginx, Redis, PostgreSQL, Prometheus
- YAML, JSON, TOML och 50+ fler verktyg

**SPECIFIKT INNEHÅLL PER ÄMNE:**

Linux:
- Grunderna: /modules/linux-247 (Terminalen, kommandon, processer)
- Tentafokus: /modules/linux-tentaplugg (Examensförberedelse)
- Praktik: /modules/hands-on-lab (Hands-on övningar)

Kubernetes:
- Grunderna: /skillsmaps/kubernetes-fundamentals
- Pods, Deployments, Services, ConfigMaps, Secrets
- Helm, Ingress, RBAC

Docker:
- Finns i: FastTrack /fasttrack/docker
- Även: Kubernetes kräver Docker-kunskap

YAML & JSON:
- Specifik modul: /skillsmaps/yaml-json-fundamentals
- Även: FastTrack /fasttrack/yaml och /fasttrack/json

Terraform:
- Infrastructure as Code: /skillsmaps/terraform-iac

Git:
- Finns i: FastTrack /fasttrack/git
- Branching, merging, GitHub workflows

CI/CD:
- Advanced Pipelines: /skillsmaps/cicd-pipelines-advanced
- GitLab CI: /skillsmaps/gitlab-ci-cd
- ArgoCD GitOps: /skillsmaps/argocd-gitops
- Jenkins: /skillsmaps/jenkins-advanced

Python:
- DevOps Automation: /skillsmaps/python-for-devops

Cloud:
- AWS: /skillsmaps/aws-fundamentals
- Azure: /skillsmaps/azure-fundamentals  
- GCP: /skillsmaps/gcp-fundamentals
- Multi-cloud: /skillsmaps/multicloud-architecture

Monitoring:
- Prometheus: /skillsmaps/prometheus-monitoring
- Grafana: /skillsmaps/grafana-visualization
- ELK Stack: /skillsmaps/elk-stack
- Datadog: /skillsmaps/datadog-monitoring

Git:
- Grunderna: /modules/git-github-mastery
- Branching: Task 2
- Pull Requests: Task 7
- GitHub Actions: Task 8

NÄR ANVÄNDAREN FRÅGAR OM SPECIFIKT INNEHÅLL:
1. Identifiera ämnet
2. Ge EXAKT länk baserad på aktuella moduler
3. Förklara kort vad som finns där
4. Använd ALLTID /skillsmaps/ för avancerat innehåll och /fasttrack/ för verktyg

EXEMPEL PÅ BRA SVAR:
❌ FEL: "Du kan hitta YAML-exempel på: /modules/yaml-mastery"
✅ RÄTT: "YAML täcks både i SkillsMaps och FastTrack! För djupgående lärning: /skillsmaps/yaml-json-fundamentals. För snabb referens med kodexempel: /fasttrack/yaml 📄"

❌ FEL: "Kolla Kubernetes Mastery för pods"
✅ RÄTT: "Pods och Deployments finns i /skillsmaps/kubernetes-fundamentals. Perfekt för dig! 🚀"

Om context är 'pulse_check':
- Fråga hur användaren mår
- Var empatisk och stöttande
- Föreslå lärresurser baserat på deras humör"""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": request.message}
                ],
                max_tokens=300,
                temperature=0.7
            )

            # Log AI usage
            usage = response.usage
            if usage:
                user_uuid = None
                if request.user_id:
                    try:
                        user_uuid = UUIDType(request.user_id)
                    except ValueError:
                        pass

                log_ai_usage(
                    feature="dallas",
                    model="gpt-3.5-turbo",
                    prompt_tokens=usage.prompt_tokens,
                    completion_tokens=usage.completion_tokens,
                    user_id=user_uuid,
                    request_type=request.context or "general",
                )

            return ChatResponse(
                response=response.choices[0].message.content,
                context=request.context
            )

        except Exception as e:
            # Om OpenAI failar, använd fallback
            print(f"Dallas OpenAI error: {type(e).__name__}: {e}")
            pass

    # Fallback-svar (no AI usage logged for fallback)
    context_key = request.context or "general"
    context_responses = FALLBACK_RESPONSES.get(context_key, FALLBACK_RESPONSES["general"])
    response_text = random.choice(context_responses)

    return ChatResponse(
        response=response_text,
        context=request.context
    )

@router.get("/status")
async def dallas_status():
    """Kolla om Dallas är online och om OpenAI är konfigurerad"""
    openai_key = os.getenv("OPENAI_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("OPEN_AI_KEY")

    return {
        "status": "online",
        "name": "Dallas",
        "role": "Din DevOps-guide",
        "mood": "🐺 Redo att hjälpa!",
        "openai_configured": bool(openai_key),
        "openai_key_source": "OPENAI_KEY" if os.getenv("OPENAI_KEY") else ("OPENAI_API_KEY" if os.getenv("OPENAI_API_KEY") else ("OPEN_AI_KEY" if os.getenv("OPEN_AI_KEY") else "none"))
    }
