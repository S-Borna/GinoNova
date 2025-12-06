"""
AI Assistant Service - Phase 16
Dallas FAQ-baserat system - svarar endast med plattformens innehåll.
GPT används INTE för att undvika kostnader och hålla svar relevanta.
"""
import os
from typing import Optional, List
import logging

from .dallas_faq import get_dallas_response

logger = logging.getLogger(__name__)


async def get_ai_response(
    message: str,
    context: Optional[dict] = None,
    history: Optional[List[dict]] = None,
    system_override: Optional[str] = None
) -> dict:
    """
    Get response from Dallas FAQ database.
    NO GPT CALLS - only local FAQ matching for cost control.

    Args:
        message: User's message
        context: Optional context (module, task info)
        history: Previous messages in conversation
        system_override: Ignored (kept for API compatibility)

    Returns:
        dict with 'response', 'tokens_used', 'error'
    """
    # Use FAQ database only - no GPT
    faq_result = get_dallas_response(message)

    return {
        "response": faq_result["response"],
        "tokens_used": 0,  # No API calls = no tokens
        "error": None
    }


async def get_hint(
    task_title: str,
    task_description: str,
    user_question: str,
    user_attempt: Optional[str] = None
) -> dict:
    """
    Get a hint for a specific task.
    Returns a generic helpful hint (no GPT).
    """
    hint = f"""💡 **Tips för "{task_title}"**

Läs igenom uppgiftsbeskrivningen noggrant och försök bryta ner den i mindre steg.

**Allmänna tips:**
• Kontrollera syntax och stavning
• Testa en sak i taget
• Läs eventuella felmeddelanden noggrant

Kolla modulens innehåll för mer detaljerad hjälp!"""

    return {
        "hint": hint,
        "tokens_used": 0,
        "error": None
    }


async def explain_concept(
    concept: str,
    context: Optional[str] = None,
    level: str = "intermediate"
) -> dict:
    """
    Try to explain a concept using FAQ database.
    """
    # Try FAQ first
    faq_result = get_dallas_response(concept)

    return {
        "explanation": faq_result["response"],
        "tokens_used": 0,
        "error": None
    }


async def suggest_next_steps(
    completed_modules: List[str],
    current_module: Optional[str] = None,
    user_goals: Optional[str] = None
) -> dict:
    """
    Suggest next learning steps based on progress.
    Returns static suggestions (no GPT).
    """
    suggestions = """🎯 **Förslag på nästa steg**

**Rekommenderad ordning:**
1. **Linux Mastery** - Grunden för allt DevOps
2. **Git & Workflows** - Versionhantering är kritiskt
3. **Docker** - Containerisering
4. **CI/CD Pipelines** - Automatiserad deployment
5. **Kubernetes** - Container orchestration
6. **AWS/Terraform** - Molninfrastruktur

**Tips:**
• Slutför en modul helt innan du går vidare
• Gör alla praktiska övningar
• Kolla SkillsMaps för djupare förståelse

Gå till Camp DevOps för att börja!"""

    return {
        "suggestions": suggestions,
        "tokens_used": 0,
        "error": None
    }
    return {
        "suggestions": result["response"],
        "tokens_used": result["tokens_used"],
        "error": result["error"]
    }
