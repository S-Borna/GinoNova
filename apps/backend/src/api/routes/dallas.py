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

    # Try multiple env var names for OpenAI key
    openai_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY") or os.getenv("OPEN_AI_KEY")

    if openai_key:
        try:
            import openai
            client = openai.OpenAI(api_key=openai_key)

            system_prompt = f"""Du är Dallas, en vänlig DevOps-guide på DevOpsHub.
Du pratar svenska och är stöttande, varm och pedagogisk.
Användaren heter {request.user_name}.

Om context är 'pulse_check':
- Fråga hur användaren mår
- Var empatisk och stöttande
- Föreslå lärresurser baserat på deras humör
- Håll svaren korta och personliga (max 2-3 meningar)

Använd emojis sparsamt men kärleksfullt. 🐺"""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": request.message}
                ],
                max_tokens=150,
                temperature=0.8
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
            print(f"Dallas OpenAI error: {e}")
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
    """Kolla om Dallas är online"""
    return {
        "status": "online",
        "name": "Dallas",
        "role": "Din DevOps-guide",
        "mood": "🐺 Redo att hjälpa!"
    }
