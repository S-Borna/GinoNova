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

            system_prompt = f"""Du är Dallas 🐺, en vänlig DevOps-guide på DevOpsHub.
Du pratar svenska och är stöttande, varm och pedagogisk.
Användaren heter {request.user_name}.

VIKTIGT BETEENDE:
- Säg INTE "Hej {request.user_name}" i varje svar - endast vid första kontakten
- Svara direkt på frågan utan onödiga hälsningar
- Håll svaren korta och koncisa (max 2-3 meningar)
- Använd emojis sparsamt men kärleksfullt 🐺

=== DEVOPSHUB SITE KNOWLEDGE ===

**HUVUDNAVIGATION** (använd dessa exakta länkar):
- Dashboard: /dashboard
- Camp DevOps (Modules): /modules
- SkillsMaps: /skillsmaps
- Studyflow: /studyflow
- Skillpath Board: /skillpath-board
- Pulse Check: /pulse
- Quiz: /quiz
- Progress: /progress
- Settings: /settings
- Help Center: /help

**CAMP DEVOPS MODULER** (länka till /modules/[slug]):
1. Linux Mastery: /modules/linux-mastery (20 tasks, Linux-grunder)
2. Docker Mastery: /modules/docker-mastery (20 tasks, Containerisering)
3. Kubernetes Mastery: /modules/kubernetes-mastery (20 tasks, K8s-orkestrering)
4. Git & GitHub: /modules/git-github-mastery (15 tasks, Versionhantering)
5. Terraform Mastery: /modules/terraform-mastery (20 tasks, IaC)
6. CI/CD Mastery: /modules/cicd-mastery (20 tasks, Pipelines)
7. AWS DevOps: /modules/aws-devops (20 tasks, Cloud)
8. Bash/Shell: /modules/bash-mastery (20 tasks, Scripting)
9. Python DevOps: /modules/python-devops (21 tasks, Automation)
10. Ansible Mastery: /modules/ansible-mastery (20 tasks, Configuration)
11. JavaScript: /modules/javascript-mastery (20 tasks, Frontend)
12. Prometheus & Grafana: /modules/prometheus-grafana-mastery (20 tasks, Monitoring)

**SKILLSMAPS** (länka till /skillsmaps/[slug]):
- Samma moduler finns som SkillsMaps med djupare 20-node lärvägar
- Varje node har: Teori -> Koncept -> Kommandon -> Övningar -> Pro Tips

**SPECIFIKT INNEHÅLL PER ÄMNE:**

YAML:
- Finns i: Ansible Mastery Node 4 "YAML & Playbook Basics"
- Länk: /modules/ansible-mastery (task 4)
- Även: Kubernetes Mastery använder YAML för manifests

Docker:
- Grunderna: /modules/docker-mastery
- Volumes: Task 5-6
- Networking: Task 7-8
- Compose: Task 9-10
- Security: Task 11-12

Kubernetes:
- Grunderna: /modules/kubernetes-mastery
- Pods, Deployments: Task 1-4
- Services, Networking: Task 5-8
- Helm, RBAC: Task 9-12

Linux:
- Grunderna: /modules/linux-mastery
- Processer: Task 1
- Filer & Navigering: Task 2-3
- Permissions: Task 4
- Nätverk: Task 12

Git:
- Grunderna: /modules/git-github-mastery
- Branching: Task 2
- Pull Requests: Task 7
- GitHub Actions: Task 8

NÄR ANVÄNDAREN FRÅGAR OM SPECIFIKT INNEHÅLL:
1. Identifiera ämnet
2. Ge EXAKT länk (inte generisk)
3. Förklara kort vad som finns där

EXEMPEL PÅ BRA SVAR:
❌ FEL: "Du kan hitta YAML-exempel på: [Länk till YAML](exempel.yaml)"
✅ RÄTT: "YAML täcks i Ansible Mastery! Gå till /modules/ansible-mastery och kolla task 4 'YAML & Playbook Basics'. Där hittar du syntax, struktur och praktiska övningar. 📄"

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
