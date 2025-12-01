"""
AI Assistant Service - Phase 16
OpenAI integration for chat, hints, and explanations.
"""
import os
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = """Du är DevOps Wizard 🧙‍♂️ - den ultimata AI-tutorn för DevOpsHub plattformen.

## DITT UPPDRAG
Du är hjärtat av DevOpsHub - en AI-mentor som hjälper användare att bli DevOps-experter.
Du är kunnig, vänlig, och alltid redo att hjälpa.

## DINA KUNSKAPSOMRÅDEN
Du är expert på alla ämnen som finns på plattformen:

### Kärnkunskaper (SkillsMaps):
- **Linux**: Processer, filer, permissions, text processing, vim/nano, I/O redirection,
  användare, paket, services, disk/storage, nätverk, DNS, firewall, SSH, arkivering,
  cron, environment, loggar, troubleshooting
- **Python for DevOps**: Scripting, automation, boto3, paramiko, subprocess, JSON/YAML
- **Docker**: Images, containers, volumes, networking, Dockerfile, compose
- **Kubernetes**: Pods, deployments, services, ingress, helm, operators
- **AWS**: EC2, S3, IAM, VPC, Lambda, ECS, EKS, CloudFormation
- **Terraform**: Providers, resources, modules, state, workspaces
- **Git**: Branches, merges, rebasing, workflows, GitHub Actions
- **CI/CD**: Pipelines, testing, deployment strategies, GitOps

### Plattformsfunktioner:
- SkillsMaps: Strukturerade lärvägar med 20 djupa nodes per ämne
- Tasks: Praktiska övningar med XP-belöningar
- Labs: Hands-on miljöer för att öva
- Studyflow: Optimerad studiesession
- Progress tracking: Spåra framsteg och streaks

## RIKTLINJER

### Pedagogisk approach:
1. **Förklara koncept** - Använd Akhilesh-stilen:
   - Intro (varför är detta viktigt?)
   - Koncept (vad är det?)
   - Kommandon/kod (med kommentarer)
   - Pro Tips (erfarenhetsbaserade tips)
   - Praktisk övning

2. **Ge hints, inte svar** - När någon är fast:
   - Ställ ledande frågor
   - Peka på relevant dokumentation
   - Ge ett delsteg åt gången

3. **Var uppmuntrande** - Lärande tar tid:
   - Fira framsteg
   - Normalisera misstag
   - Föreslå nästa steg

### Språk:
- Svara på samma språk som användaren
- Var professionell men personlig
- Använd emoji sparsamt för att vara vänlig 🚀

### Kodexempel:
- Inkludera alltid körbara exempel
- Kommentera viktiga delar
- Visa både "rätt" och "fel" sätt när relevant

Du har tillgång till information om studentens framsteg och nuvarande uppgift i kontexten."""


async def get_ai_response(
    message: str,
    context: Optional[dict] = None,
    history: Optional[List[dict]] = None,
    system_override: Optional[str] = None
) -> dict:
    """
    Get response from OpenAI API.

    Args:
        message: User's message
        context: Optional context (module, task info)
        history: Previous messages in conversation
        system_override: Custom system prompt

    Returns:
        dict with 'response', 'tokens_used', 'error'
    """
    if not OPENAI_API_KEY:
        return {
            "response": "AI Assistant är inte konfigurerad. Kontakta support för hjälp.",
            "tokens_used": 0,
            "error": "not_configured"
        }

    try:
        from openai import AsyncOpenAI
        client = AsyncOpenAI(api_key=OPENAI_API_KEY)

        # Build messages array
        system_content = system_override or SYSTEM_PROMPT

        # Add context to system prompt if available
        if context:
            context_parts = []
            if context.get("module"):
                context_parts.append(f"Modul: {context['module']}")
            if context.get("task"):
                context_parts.append(f"Uppgift: {context['task']}")
            if context.get("progress"):
                context_parts.append(f"Framsteg: {context['progress']}%")
            if context_parts:
                system_content += f"\n\nAktuell kontext:\n" + "\n".join(context_parts)

        messages = [{"role": "system", "content": system_content}]

        # Add conversation history (last 10 messages)
        if history:
            for h in history[-10:]:
                messages.append({
                    "role": h.get("role", "user"),
                    "content": h.get("content", "")
                })

        # Add current message
        messages.append({"role": "user", "content": message})

        # Call OpenAI API
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )

        return {
            "response": response.choices[0].message.content,
            "tokens_used": response.usage.total_tokens if response.usage else 0,
            "error": None
        }

    except ImportError:
        logger.error("OpenAI module not installed")
        return {
            "response": "AI-tjänsten är tillfälligt otillgänglig.",
            "tokens_used": 0,
            "error": "module_not_installed"
        }
    except Exception as e:
        logger.error(f"AI error: {type(e).__name__}: {e}")
        return {
            "response": "Ett fel uppstod. Försök igen om en stund.",
            "tokens_used": 0,
            "error": str(e)
        }


async def get_hint(
    task_title: str,
    task_description: str,
    user_question: str,
    user_attempt: Optional[str] = None
) -> dict:
    """
    Get a hint for a specific task without giving away the answer.

    Args:
        task_title: Title of the task
        task_description: Task description/instructions
        user_question: What the user is asking about
        user_attempt: What the user has tried (optional)

    Returns:
        dict with 'hint', 'tokens_used', 'error'
    """
    hint_prompt = f"""Studenten arbetar med uppgiften "{task_title}".

Uppgiftsbeskrivning:
{task_description}

Studentens fråga: {user_question}
"""

    if user_attempt:
        hint_prompt += f"\nStudentens försök:\n{user_attempt}\n"

    hint_prompt += """
Ge en pedagogisk hint som:
1. Leder studenten i rätt riktning
2. INTE ger hela svaret direkt
3. Uppmuntrar till att tänka själv
4. Kan inkludera ett litet exempel om relevant"""

    result = await get_ai_response(hint_prompt)
    return {
        "hint": result["response"],
        "tokens_used": result["tokens_used"],
        "error": result["error"]
    }


async def explain_concept(
    concept: str,
    context: Optional[str] = None,
    level: str = "intermediate"
) -> dict:
    """
    Explain a DevOps concept in a pedagogical way.

    Args:
        concept: The concept to explain
        context: Related context (module, task)
        level: Explanation level (beginner, intermediate, advanced)

    Returns:
        dict with 'explanation', 'tokens_used', 'error'
    """
    level_instructions = {
        "beginner": "Förklara på ett enkelt sätt, använd analogier, undvik jargong.",
        "intermediate": "Ge en balanserad förklaring med tekniska detaljer och exempel.",
        "advanced": "Förklara på djupet, inkludera edge cases och best practices."
    }

    explain_prompt = f"""Förklara konceptet "{concept}" för en DevOps-student.

Nivå: {level}
{level_instructions.get(level, level_instructions['intermediate'])}

{f'Relaterad kontext: {context}' if context else ''}

Inkludera:
1. Vad det är och varför det är viktigt
2. Ett praktiskt exempel
3. Vanliga misstag att undvika
4. Nästa steg att lära sig"""

    result = await get_ai_response(explain_prompt)
    return {
        "explanation": result["response"],
        "tokens_used": result["tokens_used"],
        "error": result["error"]
    }


async def suggest_next_steps(
    completed_modules: List[str],
    current_module: Optional[str] = None,
    user_goals: Optional[str] = None
) -> dict:
    """
    Suggest next learning steps based on progress.
    """
    steps_prompt = f"""Baserat på studentens framsteg, föreslå nästa steg:

Avklarade moduler: {', '.join(completed_modules) if completed_modules else 'Inga ännu'}
{f'Nuvarande modul: {current_module}' if current_module else ''}
{f'Studentens mål: {user_goals}' if user_goals else ''}

Ge 3-5 konkreta förslag på:
1. Vad de bör fokusera på härnäst
2. Praktiska övningar att göra
3. Koncept att fördjupa sig i"""

    result = await get_ai_response(steps_prompt)
    return {
        "suggestions": result["response"],
        "tokens_used": result["tokens_used"],
        "error": result["error"]
    }
