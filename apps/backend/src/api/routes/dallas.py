"""
Dallas Chat API - Intelligent DevOps Guide
==========================================

Använder GPT-4o-mini för smartare, billigare svar.
Full kunskapsbas för alla moduler, quiz och flashcards.
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


# Fallback-svar om OpenAI inte är konfigurerad - TEKNISKA SVAR, ALDRIG GENERISKA!
FALLBACK_RESPONSES = {
    "pulse_check": [
        "Tack för att du delar! Det är viktigt att checka in med sig själv. Vad skulle hjälpa dig mest just nu - lite lugn repetition med flashcards eller en utmaning med quiz? 🎯",
        "Jag hör dig! DevOps-resan har sina upp och nedgångar. Kom ihåg att varje liten bit räknas. Vill du att vi fokuserar på något specifikt idag? 💪",
        "Det låter som att du har mycket på gång! Ta det i din egen takt. Ska vi börja med något enkelt för att komma igång? 🌟",
    ],
    "general": [
        "Jag försöker nå min AI-hjärna men får inget svar just nu. 🐺 Testa igen om en stund, eller kolla dokumentationen direkt: https://man7.org/linux/man-pages/",
        "Mitt AI-system svarar inte just nu. Prova igen snart! Under tiden kan du kolla officiella docs: https://docs.docker.com/ eller https://kubernetes.io/docs/",
    ]
}

# Comprehensive DevOps knowledge base
DALLAS_SYSTEM_PROMPT = """Du är Dallas 🐺, GinoNovas AI-drivna DevOps-expert och studiekompis.
Användaren heter {user_name}.

=== SPRÅK ===
Svara ALLTID på svenska. Behåll engelska tekniska termer (container, pod, etc.) men förklara på svenska.

=== PERSONLIGHET ===
- Varm, pedagogisk och tekniskt briljant
- Avslappnad men professionell ton
- Emojis sparsamt 🐺

=== SVARSSTIL ===
- Svara DIREKT på frågan - aldrig "Bra fråga! Låt oss utforska..."
- Ge KONKRETA, KORREKTA svar (2-4 meningar)
- Inkludera kodexempel när relevant
- Om du är osäker, säg det - gissa aldrig

=== DOKUMENTATION (KRITISKT!) ===
VARJE tekniskt svar MÅSTE avslutas med länk till officiell dokumentation:

- Linux-kommandon: https://man7.org/linux/man-pages/man1/KOMMANDO.1.html
- Docker: https://docs.docker.com/
- Kubernetes: https://kubernetes.io/docs/
- Git: https://git-scm.com/docs/KOMMANDO
- Terraform: https://developer.hashicorp.com/terraform/docs
- Ansible: https://docs.ansible.com/
- AWS: https://docs.aws.amazon.com/
- Python: https://docs.python.org/3/

Använd din kunskap för att länka till RÄTT sida/sektion baserat på frågan.
Du har tillgång till all offentlig dokumentation - använd den!

=== GINONOVA NAVIGATION ===
- Dashboard: /dashboard
- Camp DevOps: /modules
- SkillsMaps: /skillsmaps
- FastTrack: /fasttrack
- AI Quiz: /ai-quiz
- Studyroom: /study
- Pulsmätning: /pulse

=== EXEMPELSVAR ===

Fråga: "Skillnaden mellan symbolic och hard link?"
Svar: "**Symbolic link** pekar på filens sökväg (som genväg), kan peka på mappar och över filsystem. **Hard link** pekar på samma inode (samma data), kan inte peka på mappar. Om originalet tas bort: symlink går sönder, hard link fungerar fortfarande.

📖 Man page: https://man7.org/linux/man-pages/man1/ln.1.html"

Fråga: "Hur kör jag en Docker container?"
Svar: "`docker run -d -p 8080:80 --name myapp nginx` startar en nginx-container i bakgrunden (-d), mappar port 8080 till 80, och namnger den 'myapp'.

📖 Docker docs: https://docs.docker.com/engine/reference/run/"
"""

@router.post("/chat", response_model=ChatResponse)
async def chat_with_dallas(request: ChatRequest):
    """
    Chatta med Dallas - din DevOps-expert.
    Använder GPT-4o-mini för bättre svar till lägre kostnad.
    """
    from uuid import UUID as UUIDType
    from ...services.ai_usage_service import log_ai_usage

    # Try multiple env var names for OpenAI key (OPENAI_KEY first - Railway config)
    openai_key = os.getenv("OPENAI_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("OPEN_AI_KEY")

    # Debug: Log which key was found
    print(f"Dallas: OPENAI_KEY={'set' if os.getenv('OPENAI_KEY') else 'not set'}")
    print(f"Dallas: openai_key={'found' if openai_key else 'NOT FOUND'}")

    if openai_key:
        try:
            import openai
            client = openai.OpenAI(api_key=openai_key)

            system_prompt = DALLAS_SYSTEM_PROMPT.format(user_name=request.user_name)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": request.message}
                ],
                max_tokens=500,
                temperature=0.7
            )

            # Get the response content FIRST before any logging
            response_content = response.choices[0].message.content

            # Try to log AI usage (don't let it fail the request)
            try:
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
                        model="gpt-4o-mini",
                        prompt_tokens=usage.prompt_tokens,
                        completion_tokens=usage.completion_tokens,
                        user_id=user_uuid,
                        request_type=request.context or "general",
                    )
            except Exception as log_error:
                print(f"Dallas: Failed to log usage (non-critical): {log_error}")

            return ChatResponse(
                response=response_content,
                context=request.context
            )

        except Exception as e:
            # Om OpenAI failar, logga och returnera faktiskt felmeddelande för debugging
            error_msg = f"{type(e).__name__}: {str(e)}"
            print(f"Dallas OpenAI error: {error_msg}")

            # Returnera felet temporärt för debugging (ta bort i produktion)
            return ChatResponse(
                response=f"⚠️ Dallas kunde inte nå GPT-4o-mini. Fel: {error_msg[:200]}. Kontakta support om detta fortsätter.",
                context=request.context
            )

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
        "role": "Din DevOps-expert med full kunskapsbas",
        "model": "gpt-4o-mini",
        "mood": "🐺 Redo att hjälpa!",
        "openai_configured": bool(openai_key),
        "openai_key_source": "OPENAI_KEY" if os.getenv("OPENAI_KEY") else ("OPENAI_API_KEY" if os.getenv("OPENAI_API_KEY") else ("OPEN_AI_KEY" if os.getenv("OPEN_AI_KEY") else "none"))
    }

