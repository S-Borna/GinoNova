# =============================================================================
# AI AGENTS - BLOCK 04: AGENT LOOP (Noder 7-8) - V3 FORMAT
# =============================================================================

NODE_07_AGENT_LOOP = {
    "node_id": 7,
    "title": "The Agent Loop",
    "slug": "agent-loop",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [6],
    "content": '''
# The Agent Loop: Perception, Reasoning, Action

Implementera den cykliska process som driver AI-agenter.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Agent Loop?

Agent Loop ar den cykliska processen dar agenten tar emot input, resonerar, agerar och observerar resultat. Det ar hjartat i varje AI-agent.

| Fas | Beskrivning |
|-----|-------------|
| Perception | Ta emot och forsta input |
| Reasoning | Analysera och planera |
| Action | Utfor handling (tool call) |
| Observation | Analysera resultat |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Robusthet | Valdesignad loop hanterar fel |
| Debugging | Enklare att hitta problem |
| Kontroll | Stopping conditions forhindrar loopar |
| Prestanda | Effektiv loop = snabbare agent |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Loop Patterns

| Pattern | Beskrivning | Bast for |
|---------|-------------|----------|
| ReAct | Thought -> Action -> Observation | Steg-for-steg |
| Plan-Execute | Plan forst, sen exekvera | Komplexa uppgifter |
| Reflexion | Lar sig fran misstag | Iterativ forbattring |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Core Agent Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE AGENT LOOP                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  START: User Request                                            │
│           │                                                      │
│           v                                                      │
│  ┌─────────────────┐                                            │
│  │   PERCEPTION    │<────────────────────────────────┐          │
│  │  - Parse input  │                                 │          │
│  │  - Load context │                                 │          │
│  └────────┬────────┘                                 │          │
│           │                                          │          │
│           v                                          │          │
│  ┌─────────────────┐                                 │          │
│  │   REASONING     │                                 │          │
│  │  - Analyze      │                                 │          │
│  │  - Plan next    │                                 │          │
│  │  - Decide       │                                 │          │
│  └────────┬────────┘                                 │          │
│           │                                          │          │
│           v                                          │          │
│     ┌───────────────┐                                │          │
│     │ ACTION TYPE?  │                                │          │
│     └───────┬───────┘                                │          │
│             │                                        │          │
│    ┌────────┼────────┐                               │          │
│    v        v        v                               │          │
│  TOOL    RESPOND   ERROR                             │          │
│  CALL    TO USER   HANDLE                            │          │
│    │        │        │                               │          │
│    v        │        │                               │          │
│  OBSERVE   END      │                                │          │
│  RESULT ────────────┘                                │          │
│    │                                                 │          │
│    └─────────────────────────────────────────────────┘          │
│                                                                  │
│  STOPPING CONDITIONS:                                           │
│  - Task completed                                               │
│  - Max iterations                                               │
│  - Error threshold                                              │
│  - Timeout                                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Agent State

```python
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
import time

class ActionType(Enum):
    TOOL_CALL = "tool_call"
    FINAL_RESPONSE = "final_response"
    ERROR = "error"

@dataclass
class AgentState:
    """Current state of the agent."""
    messages: list = field(default_factory=list)
    iteration: int = 0
    tool_calls_made: int = 0
    errors: list = field(default_factory=list)
    start_time: float = field(default_factory=time.time)

    def elapsed_time(self) -> float:
        return time.time() - self.start_time

@dataclass
class LoopConfig:
    """Configuration for the agent loop."""
    max_iterations: int = 10
    max_tool_calls: int = 20
    timeout_seconds: float = 60.0
    max_consecutive_errors: int = 3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Robust Agent Loop

```python
class AgentLoop:
    """Core agent loop implementation."""

    def __init__(self, client, tools, tool_executor, config=None):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor
        self.config = config or LoopConfig()

    def run(self, user_message: str, system_prompt: str = None) -> str:
        state = AgentState()
        state.messages = [
            {"role": "system", "content": system_prompt or "Du ar en hjalpsam assistent."},
            {"role": "user", "content": user_message}
        ]

        consecutive_errors = 0

        while True:
            state.iteration += 1

            # Kolla stopping conditions
            stop_reason = self._check_stop_conditions(state)
            if stop_reason:
                return f"[Agent stoppad: {stop_reason}]"

            try:
                response = self._call_llm(state.messages)
                message = response.choices[0].message
                state.messages.append(message)

                if message.tool_calls:
                    tool_results = self._process_tools(message.tool_calls, state)
                    state.messages.extend(tool_results)
                    consecutive_errors = 0
                else:
                    return message.content

            except Exception as e:
                consecutive_errors += 1
                state.errors.append(str(e))

                if consecutive_errors >= self.config.max_consecutive_errors:
                    return f"[For manga fel: {e}]"

    def _check_stop_conditions(self, state: AgentState) -> Optional[str]:
        if state.iteration > self.config.max_iterations:
            return f"Max iterationer ({self.config.max_iterations})"
        if state.tool_calls_made > self.config.max_tool_calls:
            return f"Max tool calls ({self.config.max_tool_calls})"
        if state.elapsed_time() > self.config.timeout_seconds:
            return f"Timeout ({self.config.timeout_seconds}s)"
        return None
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ReAct Pattern

```python
REACT_SYSTEM_PROMPT = """
Du ar en AI-assistent som loser uppgifter steg for steg.

For varje steg, folj detta format:
THOUGHT: [Ditt resonemang om situationen]
ACTION: [Verktyget du vill anvanda]
OBSERVATION: [Vad du larde dig]

Nar du har tillracklig information:
THOUGHT: [Slutligt resonemang]
ANSWER: [Ditt svar till anvandaren]

Regler:
1. Forklara alltid ditt resonemang i THOUGHT
2. Anvand endast ett verktyg per iteration
3. Reflektera over resultatet efter varje action
"""

class ReActAgent(AgentLoop):
    """Agent som anvander ReAct pattern."""

    def run(self, user_message: str) -> str:
        return super().run(user_message, system_prompt=REACT_SYSTEM_PROMPT)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Plan-and-Execute Pattern

```python
class PlanExecuteAgent:
    """Agent som planerar fore exekvering."""

    def __init__(self, client, tools, tool_executor):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor

    def run(self, user_message: str) -> str:
        # Steg 1: Skapa plan
        plan = self._create_plan(user_message)

        # Steg 2: Exekvera varje steg
        results = []
        for i, step in enumerate(plan):
            result = self._execute_step(step, results)
            results.append({"step": step, "result": result})

        # Steg 3: Syntetisera slutsvar
        return self._synthesize(user_message, results)

    def _create_plan(self, task: str) -> list:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Skapa en steg-for-steg plan for:
                {task}

                Returnera JSON:
                {{"steps": [{{"description": "...", "tool": "..."}}]}}
                """
            }],
            response_format={"type": "json_object"}
        )
        import json
        return json.loads(response.choices[0].message.content).get("steps", [])
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loop Detector

```python
class LoopDetector:
    """Upptack och bryt oandliga loopar."""

    def __init__(self, window_size: int = 5):
        self.window_size = window_size
        self.recent_actions = []

    def record_action(self, action: str) -> None:
        self.recent_actions.append(action)
        if len(self.recent_actions) > self.window_size * 2:
            self.recent_actions.pop(0)

    def is_looping(self) -> bool:
        if len(self.recent_actions) < self.window_size * 2:
            return False

        recent = self.recent_actions[-self.window_size:]
        previous = self.recent_actions[-self.window_size*2:-self.window_size]

        return recent == previous

    def get_break_prompt(self) -> str:
        return """
        Du verkar upprepa samma handlingar. Prova en annan approach.
        """
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Oandlig loop | Ingen stopping condition | Implementera LoopDetector |
| For lite progress | Ineffektiv planering | Anvand Plan-Execute |
| Saknar kontext | Glommer tidigare steg | Battre state management |
| For langsam | For manga iterationer | Optimera prompt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Agent Loop | Perception -> Reasoning -> Action -> Observe |
| Stopping conditions | Max iterations, timeout, errors |
| ReAct | Explicit reasoning i varje steg |
| Plan-Execute | Planera forst, exekvera sen |

Kom ihag:
- Implementera alltid stopping conditions
- Logga varje iteration for debugging
- Valj pattern baserat pa uppgiftens komplexitet
- Testa loop detection noggrant
'''
}

NODE_08_OBSERVATION_REFLECTION = {
    "node_id": 8,
    "title": "Observation och Reflection",
    "slug": "observation-and-reflection",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "prerequisites": [7],
    "content": '''
# Observation och Reflection

Lar agenten analysera resultat och forbattra sitt beteende.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Observation och Reflection?

Observation ar formagan att forsta vad som hande. Reflection ar formagan att lara sig fran det. Tillsammans gor de agenter intelligenta.

| Komponent | Funktion |
|-----------|----------|
| Observation | Processa och forsta tool output |
| Reflection | Analysera och lara sig |
| Self-correction | Fixa misstag automatiskt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Kvalitet | Agenter som reflekterar ger battre svar |
| Larding | Undviker att upprepa samma misstag |
| Debugging | Enklare att forsta vad som gick fel |
| Effektivitet | Kortare cykler till ratt svar |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Reflection Types

| Typ | Nar | Kostnad |
|-----|-----|---------|
| Immediate | Efter varje action | +1 LLM call/action |
| Checkpoint | Var N:te action | +1 LLM call/checkpoint |
| Final | Vid slutforande | +1 LLM call/task |
| Retrospective | Over flera tasks | Periodisk batch |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Observation Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                   OBSERVATION PIPELINE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TOOL OUTPUT (Raw)                                              │
│  │                                                               │
│  │  {"status": 200, "data": {"temp": 15.5, ...}}                │
│  │                                                               │
│  v                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  PARSER                                                    │ │
│  │  - Extract relevant fields                                 │ │
│  │  - Handle errors                                           │ │
│  └───────────────────────────────────────────────────────────┘ │
│  │                                                               │
│  v                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  SUMMARIZER                                                │ │
│  │  - Condense long outputs                                   │ │
│  │  - Highlight key info                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
│  │                                                               │
│  v                                                               │
│  PROCESSED OBSERVATION                                          │
│  "Vader i Stockholm: 15.5C, molnigt"                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Observation Handler

```python
from dataclasses import dataclass
from typing import Any, Optional
import json

@dataclass
class Observation:
    """Strukturerad observation fran tool output."""
    raw_output: Any
    parsed_data: dict
    summary: str
    relevance_score: float
    anomalies: list[str]

class ObservationHandler:
    """Processa och strukturera tool outputs."""

    def __init__(self, client):
        self.client = client

    def process(self, tool_name: str, raw_output: Any, goal: str) -> Observation:
        parsed = self._parse_output(tool_name, raw_output)
        summary = self._summarize(tool_name, parsed, goal)
        relevance = self._assess_relevance(summary, goal)
        anomalies = self._detect_anomalies(parsed)

        return Observation(
            raw_output=raw_output,
            parsed_data=parsed,
            summary=summary,
            relevance_score=relevance,
            anomalies=anomalies
        )

    def _parse_output(self, tool_name: str, raw_output: Any) -> dict:
        if isinstance(raw_output, dict):
            return raw_output
        try:
            return json.loads(raw_output)
        except:
            return {"text": str(raw_output)}

    def _detect_anomalies(self, parsed: dict) -> list[str]:
        anomalies = []
        if "error" in str(parsed).lower():
            anomalies.append("Error i output")
        if parsed.get("data") == []:
            anomalies.append("Tomt resultat")
        return anomalies
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Reflection Engine

```python
@dataclass
class Reflection:
    """Strukturerad reflection output."""
    assessment: str
    learnings: list[str]
    adjustments: list[str]
    confidence: float
    should_continue: bool

class ReflectionEngine:
    """Generera reflektioner for att forbattra agentbeteende."""

    def __init__(self, client):
        self.client = client
        self.reflection_history = []

    def immediate_reflect(self, action: str, observation: Observation, goal: str) -> Reflection:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Du tog just en action. Reflektera over vad som hande.

                MAL: {goal}
                ACTION: {action}
                OBSERVATION: {observation.summary}

                Svara:
                ASSESSMENT: [din analys]
                LEARNINGS: [lista]
                ADJUSTMENTS: [lista]
                CONFIDENCE: [0.0-1.0]
                CONTINUE: [yes/no]
                """
            }]
        )
        return self._parse_reflection(response.choices[0].message.content)

    def checkpoint_reflect(self, actions_taken: list, goal: str, progress: float) -> Reflection:
        action_summary = "\\n".join([f"- {a}" for a in actions_taken[-5:]])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Checkpoint reflection. Analysera din progress.

                MAL: {goal}
                PROGRESS: {progress:.2f}
                ACTIONS: {action_summary}

                Analysera:
                1. Gar du mot malet?
                2. Vad fungerar?
                3. Vad fungerar inte?
                4. Behover du andra strategi?
                """
            }]
        )
        return self._parse_reflection(response.choices[0].message.content)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Self-Correction System

```python
class SelfCorrectionSystem:
    """Lat agenten korrigera sina egna misstag."""

    def __init__(self, client):
        self.client = client
        self.error_patterns = []

    def check_and_correct(self, action: str, result: str, expected: str) -> Optional[str]:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Action: {action}
                Expected: {expected}
                Actual: {result}

                Matchar resultatet forvantan?
                Om NEJ, vad gick fel och hur korrigerar vi?

                MATCH: [yes/no]
                ISSUE: [problem]
                CORRECTION: [atgard]
                """
            }]
        )

        text = response.choices[0].message.content
        if "MATCH: no" in text.lower():
            for line in text.split("\\n"):
                if line.startswith("CORRECTION:"):
                    return line.replace("CORRECTION:", "").strip()
        return None

    def learn_from_error(self, error_context: dict) -> None:
        self.error_patterns.append(error_context)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Reflective Agent

```python
class ReflectiveAgent:
    """Agent med full observation och reflection."""

    def __init__(self, client, tools, tool_executor):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor

        self.observation_handler = ObservationHandler(client)
        self.reflection_engine = ReflectionEngine(client)
        self.self_correction = SelfCorrectionSystem(client)

        self.actions_taken = []

    def run(self, goal: str, max_iterations: int = 10) -> str:
        messages = [
            {"role": "system", "content": self._get_system_prompt()},
            {"role": "user", "content": goal}
        ]

        for i in range(max_iterations):
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=self.tools
            )

            message = response.choices[0].message
            messages.append(message)

            if message.tool_calls:
                for tool_call in message.tool_calls:
                    result = self.tool_executor(
                        tool_call.function.name,
                        json.loads(tool_call.function.arguments)
                    )

                    observation = self.observation_handler.process(
                        tool_call.function.name,
                        result,
                        goal
                    )

                    self.actions_taken.append(tool_call.function.name)

                    # Checkpoint reflection var 3:e action
                    if len(self.actions_taken) % 3 == 0:
                        reflection = self.reflection_engine.checkpoint_reflect(
                            self.actions_taken, goal, 0.5
                        )
                        if not reflection.should_continue:
                            break

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": observation.summary
                    })
            else:
                return message.content

        return "Max iterations"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| For mycket reflection | Varje action | Anvand checkpoint istallet |
| Missar viktig info | Dalig parsing | Battre observation handler |
| Upprepar misstag | Ingen learning | Implementera error patterns |
| Langsam agent | For manga LLM calls | Battra reflection threshold |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Observation | Transformerar ra output till struktur |
| Reflection | Later agenten lara sig |
| Self-correction | Fixar misstag automatiskt |
| Checkpoint | Strategiska justeringar |

Kom ihag:
- Borja med checkpoint reflections var 3:e action
- Observation parsing ar kritiskt
- Balance cost vs benefit
- Logga all reflection for analys
'''
}

BLOCK_04_NODES = [NODE_07_AGENT_LOOP, NODE_08_OBSERVATION_REFLECTION]
