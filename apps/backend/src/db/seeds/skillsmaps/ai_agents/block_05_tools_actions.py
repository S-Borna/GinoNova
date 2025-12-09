# =============================================================================
# AI AGENTS - BLOCK 05: TOOLS & ACTIONS (Noder 9-10) - V3 FORMAT
# =============================================================================

NODE_09_ADVANCED_TOOL_DESIGN = {
    "node_id": 9,
    "title": "Avancerad Tool Design",
    "slug": "advanced-tool-design",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [8],
    "content": '''
# Avancerad Tool Design

Bygga robusta, skalbara och sakra tools for AI-agenter.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Avancerad Tool Design?

Professionella tools kraver mer an bara funktionalitet. De maste vara robusta, sakra, dokumenterade och effektiva.

| Aspekt | Grundlaggande | Avancerat |
|--------|--------------|-----------|
| Validering | Enkel | Djup, med constraints |
| Felhantering | Try/except | Retries, fallbacks |
| Sakerhet | Ingen | Input sanitation |
| Dokumentation | Minimal | Full schema |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Driftssakerhet | Robusta tools = stabil agent |
| Kostnadseffektivitet | Bra schema = farre felaktiga calls |
| Skalbarhet | Valdesignade tools ar atervandningsbara |
| Sakerhet | Forhindrar injection och missbruk |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Tool Components

| Komponent | Funktion | Exempel |
|-----------|----------|---------|
| Schema | Definierar interface | JSON Schema |
| Validator | Kontrollerar input | Pydantic |
| Executor | Utfor handlingen | Python function |
| Error handler | Hanterar fel | Retries, fallback |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tool Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    TOOL ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LLM Request                                                    │
│  │                                                               │
│  v                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  INPUT VALIDATOR                                           │ │
│  │  - JSON Schema validation                                  │ │
│  │  - Type coercion                                           │ │
│  │  - Constraint checking                                     │ │
│  └───────────────────────────────────────────────────────────┘ │
│  │                                                               │
│  v                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  SECURITY LAYER                                            │ │
│  │  - Input sanitization                                      │ │
│  │  - Rate limiting                                           │ │
│  │  - Permission checks                                       │ │
│  └───────────────────────────────────────────────────────────┘ │
│  │                                                               │
│  v                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  EXECUTOR                                                  │ │
│  │  - Actual tool logic                                       │ │
│  │  - With retry mechanism                                    │ │
│  │  - Timeout handling                                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│  │                                                               │
│  v                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  OUTPUT FORMATTER                                          │ │
│  │  - Standardize response                                    │ │
│  │  - Error wrapping                                          │ │
│  │  - Truncation if needed                                    │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Advanced Tool Framework

```python
from pydantic import BaseModel, Field, validator
from typing import Generic, TypeVar, Callable, Any
from functools import wraps
from enum import Enum
import time

T = TypeVar('T', bound=BaseModel)
R = TypeVar('R')

class ToolError(Enum):
    VALIDATION_ERROR = "validation_error"
    EXECUTION_ERROR = "execution_error"
    TIMEOUT_ERROR = "timeout_error"
    PERMISSION_ERROR = "permission_error"

class ToolResult(BaseModel, Generic[R]):
    success: bool
    data: R = None
    error: str = None
    error_type: ToolError = None
    execution_time_ms: float = 0

class Tool(Generic[T, R]):
    """Base class for all tools."""

    def __init__(
        self,
        name: str,
        description: str,
        input_model: type[T],
        executor: Callable[[T], R],
        max_retries: int = 3,
        timeout_seconds: float = 30.0,
        requires_confirmation: bool = False
    ):
        self.name = name
        self.description = description
        self.input_model = input_model
        self.executor = executor
        self.max_retries = max_retries
        self.timeout_seconds = timeout_seconds
        self.requires_confirmation = requires_confirmation

    def to_openai_schema(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.input_model.model_json_schema()
            }
        }

    def execute(self, args: dict) -> ToolResult:
        start = time.time()

        # Validering
        try:
            validated = self.input_model(**args)
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Validation error: {e}",
                error_type=ToolError.VALIDATION_ERROR
            )

        # Exekvering med retries
        for attempt in range(self.max_retries):
            try:
                result = self.executor(validated)
                return ToolResult(
                    success=True,
                    data=result,
                    execution_time_ms=(time.time() - start) * 1000
                )
            except Exception as e:
                if attempt == self.max_retries - 1:
                    return ToolResult(
                        success=False,
                        error=str(e),
                        error_type=ToolError.EXECUTION_ERROR
                    )
                time.sleep(2 ** attempt)  # Exponential backoff
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Input Validation

```python
from pydantic import BaseModel, Field, validator, field_validator
import re

class SearchInput(BaseModel):
    """Validated search input."""

    query: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Search query"
    )
    max_results: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Max results"
    )
    filters: dict = Field(
        default_factory=dict,
        description="Optional filters"
    )

    @field_validator('query')
    @classmethod
    def sanitize_query(cls, v: str) -> str:
        # Ta bort potentiellt farliga tecken
        v = re.sub(r'[<>{}]', '', v)
        return v.strip()

    @field_validator('filters')
    @classmethod
    def validate_filters(cls, v: dict) -> dict:
        allowed_keys = {'category', 'date_from', 'date_to', 'status'}
        return {k: v for k, v in v.items() if k in allowed_keys}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Layer

```python
class SecurityLayer:
    """Security checks for tool execution."""

    def __init__(self, rate_limit_per_minute: int = 60):
        self.rate_limit = rate_limit_per_minute
        self.call_counts = {}

    def check_rate_limit(self, user_id: str) -> bool:
        import time
        current_minute = int(time.time() / 60)
        key = f"{user_id}:{current_minute}"

        self.call_counts[key] = self.call_counts.get(key, 0) + 1
        return self.call_counts[key] <= self.rate_limit

    def sanitize_input(self, value: str) -> str:
        dangerous_patterns = [
            r'(\$\{.*?\})',    # Template injection
            r'({{.*?}})',      # Jinja injection
            r'(<script.*?>)',  # XSS
        ]

        for pattern in dangerous_patterns:
            value = re.sub(pattern, '', value, flags=re.IGNORECASE)
        return value

    def check_permissions(self, user_id: str, tool_name: str) -> bool:
        # Implementera permission check
        return True
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Composite Tools

```python
class CompositeToolInput(BaseModel):
    """Input for composite tool."""
    primary_query: str
    include_metadata: bool = True

class CompositeTool:
    """Tool som kombinerar flera andra tools."""

    def __init__(self, tools: list[Tool]):
        self.tools = {t.name: t for t in tools}

    def execute_sequence(self, sequence: list[dict]) -> list[ToolResult]:
        results = []
        context = {}

        for step in sequence:
            tool_name = step["tool"]
            args = self._resolve_references(step["args"], context)

            result = self.tools[tool_name].execute(args)
            results.append(result)

            if step.get("store_as"):
                context[step["store_as"]] = result.data

        return results

    def _resolve_references(self, args: dict, context: dict) -> dict:
        """Resolve $ref.path references."""
        resolved = {}
        for key, value in args.items():
            if isinstance(value, str) and value.startswith("$"):
                path = value[1:].split(".")
                resolved[key] = self._get_nested(context, path)
            else:
                resolved[key] = value
        return resolved
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Schema mismatch | Fel typer | Strang Pydantic validation |
| Timeout | Langsam externa API | Implementera timeout |
| Rate limit | For manga requests | SecurityLayer med rate limit |
| Injection | Osanerad input | sanitize_input() |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Pydantic | Anvand for all input validation |
| Retries | Exponential backoff for extern services |
| Security | Sanitize, rate limit, permissions |
| Composites | Bygg komplexa flows fran enkla tools |

Kom ihag:
- Validera alltid input med Pydantic
- Implementera rate limiting fran borjan
- Sanitize all string input
- Logga alla tool executions
'''
}

NODE_10_ACTION_PATTERNS = {
    "node_id": 10,
    "title": "Action Patterns",
    "slug": "action-patterns",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [9],
    "content": '''
# Action Patterns

Designmonster for olika typer av agent-actions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Action Patterns?

Action patterns ar beprövade designmonster for hur agenter ska utfora olika typer av handlingar.

| Pattern | Bast for |
|---------|----------|
| Fire-and-forget | Enkla operationer |
| Request-response | Synkrona operationer |
| Saga | Multi-step transactions |
| Observer | Event-driven actions |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Konsistens | Beprövade patterns = farre buggar |
| Underhall | Kanda patterns = latttare att forsta |
| Skalbarhet | Ratt pattern for ratt scenario |
| Felhantering | Inbyggd recovery |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Pattern Selection

| Scenario | Pattern | Exempel |
|----------|---------|---------|
| Skicka notis | Fire-and-forget | Slack message |
| API anrop | Request-response | Vader lookup |
| Boka resa | Saga | Flyg + hotell + hyrbil |
| Monitor | Observer | Logga alla events |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pattern Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                   ACTION PATTERNS                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FIRE-AND-FORGET           REQUEST-RESPONSE                     │
│  ┌───────┐                 ┌───────┐                            │
│  │ Agent │──────>          │ Agent │◄─────►                     │
│  └───────┘      │          └───────┘       │                    │
│           ┌─────v─────┐              ┌─────┴─────┐              │
│           │  Service  │              │  Service  │              │
│           └───────────┘              └───────────┘              │
│                                                                  │
│  SAGA                      OBSERVER                             │
│  ┌───────┐                 ┌───────┐                            │
│  │ Agent │──┬──┬──┐        │ Agent │                            │
│  └───────┘  │  │  │        └───┬───┘                            │
│        ┌────┘  │  └────┐       │                                │
│        v       v       v       v                                │
│     ┌────┐  ┌────┐  ┌────┐  ┌─────────┐                        │
│     │ S1 │  │ S2 │  │ S3 │  │ Events  │                        │
│     └────┘  └────┘  └────┘  └─────────┘                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Fire-and-Forget

```python
from dataclasses import dataclass
import asyncio
from typing import Callable, Any

@dataclass
class FireAndForgetAction:
    """Action som inte vantar pa resultat."""
    name: str
    executor: Callable

    async def execute(self, args: dict) -> str:
        # Starta utan att vanta
        asyncio.create_task(self._run(args))
        return f"Action '{self.name}' startad"

    async def _run(self, args: dict) -> None:
        try:
            await self.executor(**args)
        except Exception as e:
            # Logga men kasta inte
            print(f"[{self.name}] Error: {e}")

# Exempel: Slack notification
async def send_slack_notification(channel: str, message: str):
    # Asynkront anrop till Slack
    await asyncio.sleep(0.1)  # Simulerad latency
    print(f"Slack: {message}")

slack_action = FireAndForgetAction(
    name="send_slack",
    executor=send_slack_notification
)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Request-Response

```python
@dataclass
class RequestResponseAction:
    """Synkron action med retry och timeout."""
    name: str
    executor: Callable
    timeout_seconds: float = 30.0
    max_retries: int = 3

    async def execute(self, args: dict) -> dict:
        for attempt in range(self.max_retries):
            try:
                result = await asyncio.wait_for(
                    self.executor(**args),
                    timeout=self.timeout_seconds
                )
                return {"success": True, "data": result}
            except asyncio.TimeoutError:
                if attempt == self.max_retries - 1:
                    return {"success": False, "error": "Timeout"}
            except Exception as e:
                if attempt == self.max_retries - 1:
                    return {"success": False, "error": str(e)}
                await asyncio.sleep(2 ** attempt)
        return {"success": False, "error": "Max retries exceeded"}

# Exempel: Vader API
async def get_weather(city: str) -> dict:
    await asyncio.sleep(0.1)  # Simulerad API call
    return {"city": city, "temp": 15.5, "condition": "cloudy"}

weather_action = RequestResponseAction(
    name="get_weather",
    executor=get_weather
)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Saga Pattern

```python
from enum import Enum

class SagaState(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    COMPENSATING = "compensating"
    FAILED = "failed"

@dataclass
class SagaStep:
    name: str
    execute: Callable
    compensate: Callable  # Rollback function

class Saga:
    """Multi-step transaction med automatisk rollback."""

    def __init__(self, steps: list[SagaStep]):
        self.steps = steps
        self.completed_steps = []
        self.state = SagaState.PENDING

    async def execute(self, initial_context: dict) -> dict:
        context = initial_context.copy()

        for step in self.steps:
            try:
                result = await step.execute(context)
                context.update(result)
                self.completed_steps.append(step)
            except Exception as e:
                await self._compensate()
                return {"success": False, "error": str(e)}

        self.state = SagaState.COMPLETED
        return {"success": True, "context": context}

    async def _compensate(self) -> None:
        self.state = SagaState.COMPENSATING

        for step in reversed(self.completed_steps):
            try:
                await step.compensate()
            except:
                pass  # Best effort compensation

        self.state = SagaState.FAILED

# Exempel: Bokningssaga
booking_saga = Saga([
    SagaStep(
        name="book_flight",
        execute=lambda ctx: book_flight(ctx["destination"]),
        compensate=lambda: cancel_flight_booking()
    ),
    SagaStep(
        name="book_hotel",
        execute=lambda ctx: book_hotel(ctx["destination"], ctx["flight_id"]),
        compensate=lambda: cancel_hotel_booking()
    ),
    SagaStep(
        name="book_car",
        execute=lambda ctx: book_car(ctx["destination"]),
        compensate=lambda: cancel_car_booking()
    )
])
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Observer Pattern

```python
from dataclasses import dataclass, field
from typing import Protocol

class ActionObserver(Protocol):
    async def on_action_start(self, action_name: str, args: dict) -> None: ...
    async def on_action_complete(self, action_name: str, result: dict) -> None: ...
    async def on_action_error(self, action_name: str, error: Exception) -> None: ...

@dataclass
class ObservableAction:
    """Action som notifierar observers."""
    name: str
    executor: Callable
    observers: list[ActionObserver] = field(default_factory=list)

    def add_observer(self, observer: ActionObserver) -> None:
        self.observers.append(observer)

    async def execute(self, args: dict) -> dict:
        for obs in self.observers:
            await obs.on_action_start(self.name, args)

        try:
            result = await self.executor(**args)
            for obs in self.observers:
                await obs.on_action_complete(self.name, result)
            return result
        except Exception as e:
            for obs in self.observers:
                await obs.on_action_error(self.name, e)
            raise

class LoggingObserver:
    """Observer som loggar alla actions."""

    async def on_action_start(self, name: str, args: dict) -> None:
        print(f"[START] {name}: {args}")

    async def on_action_complete(self, name: str, result: dict) -> None:
        print(f"[COMPLETE] {name}: {result}")

    async def on_action_error(self, name: str, error: Exception) -> None:
        print(f"[ERROR] {name}: {error}")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Action Coordinator

```python
class ActionCoordinator:
    """Koordinerar actions med ratt pattern."""

    def __init__(self):
        self.fire_and_forget = []
        self.request_response = []
        self.sagas = {}
        self.observers = []

    def register_action(self, action, pattern: str):
        if pattern == "fire_and_forget":
            self.fire_and_forget.append(action)
        elif pattern == "request_response":
            self.request_response.append(action)

    def register_saga(self, name: str, saga: Saga):
        self.sagas[name] = saga

    async def execute(self, action_name: str, args: dict, pattern: str = "request_response") -> dict:
        if pattern == "saga" and action_name in self.sagas:
            return await self.sagas[action_name].execute(args)

        action = self._find_action(action_name, pattern)
        if action:
            return await action.execute(args)

        return {"error": f"Action {action_name} not found"}

    def _find_action(self, name: str, pattern: str):
        actions = (
            self.fire_and_forget if pattern == "fire_and_forget"
            else self.request_response
        )
        return next((a for a in actions if a.name == name), None)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Lost notification | Fire-and-forget utan retry | Anvand message queue |
| Inkonsistent state | Saga utan compensation | Implementera rollback |
| Miss events | Observer inte registrerad | Logga registreringar |
| Deadlock | Cirkulara dependencies | Asynkron exekvering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Fire-and-forget | For notifikationer och logging |
| Request-response | For synkrona operationer |
| Saga | For multi-step transactions |
| Observer | For event-driven systems |

Kom ihag:
- Valj pattern baserat pa use case
- Implementera alltid compensation for sagas
- Observer ar bra for logging och metrics
- Kombinera patterns vid behov
'''
}

BLOCK_05_NODES = [NODE_09_ADVANCED_TOOL_DESIGN, NODE_10_ACTION_PATTERNS]
