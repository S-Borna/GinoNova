# =============================================================================
# AI AGENTS - BLOCK 03: AGENT BASICS (Noder 5-6) - V3 FORMAT
# =============================================================================

NODE_05_WHAT_ARE_AGENTS = {
    "node_id": 5,
    "title": "Vad ar AI Agenter?",
    "slug": "what-are-ai-agents",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [4],
    "content": '''
# Vad ar AI Agenter?

Forsta skillnaden mellan LLMs, chatbots och riktiga AI-agenter.

------------------------------------------------------------

## Vad ar en AI Agent?

En AI-agent ar ett system som kan planera, agera, observera och anpassa sig autonomt. Till skillnad fran en chatbot kan agenter anvanda verktyg och fatta beslut.

| Komponent | Funktion |
|-----------|----------|
| Brain (LLM) | Resonemang och beslut |
| Tools | Interagera med omvarlden |
| Memory | Minns kontext och historik |
| Perception | Tar emot information |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Automation | Agenter kan automatisera komplexa uppgifter |
| Effektivitet | Minskar manuellt arbete |
| Skalbarhet | Hanterar manga uppgifter parallellt |
| Flexibilitet | Anpassar sig till nya situationer |

------------------------------------------------------------

## Snabbreferens - Autonominiva

| Niva | Typ | Beskrivning |
|------|-----|-------------|
| 0 | Basic LLM | Single turn, inget minne |
| 1 | Chatbot | Multi-turn, sessionsminne |
| 2 | RAG | Tillgang till extern kunskap |
| 3 | Simple Agent | Kan anvanda verktyg |
| 4 | Agentic System | Multi-step reasoning |
| 5 | Autonomous | Minimal human intervention |

------------------------------------------------------------

## Agent vs Chatbot vs RAG

```
+-----------------------------------------------------------------+
|                   AI APPLICATION SPECTRUM                        |
+-----------------------------------------------------------------+
|                                                                  |
|  LEVEL 0: Basic LLM                                             |
|  +-----------------------------------------------------------+ |
|  |  User -> LLM -> Response                                   | |
|  |  - Single turn, no memory, no tools                        | |
|  +-----------------------------------------------------------+ |
|                                                                  |
|  LEVEL 1: Chatbot                                               |
|  +-----------------------------------------------------------+ |
|  |  User -> LLM (+ history) -> Response                       | |
|  |  - Multi-turn, session memory                              | |
|  +-----------------------------------------------------------+ |
|                                                                  |
|  LEVEL 2: RAG Application                                       |
|  +-----------------------------------------------------------+ |
|  |  User -> Retriever -> LLM (+ context) -> Response          | |
|  |  - External knowledge, no autonomous actions               | |
|  +-----------------------------------------------------------+ |
|                                                                  |
|  LEVEL 3-4: Agent                                               |
|  +-----------------------------------------------------------+ |
|  |  User -> Plan -> Action -> Observe -> Reflect -> Done      | |
|  |  - Multi-step reasoning, tool use, self-correction         | |
|  +-----------------------------------------------------------+ |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## De Fyra Karnkomponenterna

```
+-----------------------------------------------------------------+
|                   AGENT CORE COMPONENTS                          |
+-----------------------------------------------------------------+
|                                                                  |
|                      +-----------------+                        |
|                      |    BRAIN        |                        |
|                      |   (LLM/Model)   |                        |
|                      |                 |                        |
|                      |  - Reasoning    |                        |
|                      |  - Planning     |                        |
|                      |  - Decisions    |                        |
|                      +--------+--------+                        |
|                               |                                  |
|         +---------------------+---------------------+           |
|         |                     |                     |           |
|         v                     v                     v           |
|  +-------------+     +-------------+     +-------------+       |
|  | PERCEPTION  |     |   TOOLS     |     |   MEMORY    |       |
|  |             |     |             |     |             |       |
|  | - User input|     | - Code exec |     | - Short-term|       |
|  | - File read |     | - Web search|     | - Long-term |       |
|  | - API resp  |     | - Database  |     | - Semantic  |       |
|  +-------------+     +-------------+     +-------------+       |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Agent Use Cases

| Use Case | Niva | Verktyg | Risk |
|----------|------|---------|------|
| Code completion | 2-3 | Filaccess | Lag |
| Research assistant | 3-4 | Webbsok, RAG | Lag |
| Data analysis | 3-4 | Python, DB | Medium |
| DevOps automation | 4 | Shell, Cloud APIs | Hog |
| Autonomous coding | 4-5 | Full miljoaccess | Mycket hog |

------------------------------------------------------------

## Din Forsta Agent

```python
from openai import OpenAI
import json

client = OpenAI()

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Hamta vaderinformation for en stad",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Stadens namn"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

def get_weather(city: str) -> str:
    """Simulerad vaderdata."""
    weather_data = {
        "stockholm": {"temp": 5, "condition": "cloudy"},
        "gothenburg": {"temp": 7, "condition": "rainy"},
    }
    city_lower = city.lower()
    if city_lower in weather_data:
        data = weather_data[city_lower]
        return f"Vader i {city}: {data['temp']}C, {data['condition']}"
    return f"Ingen vaderdata for {city}"

TOOL_FUNCTIONS = {"get_weather": get_weather}
```

------------------------------------------------------------

## Agent Loop

```python
def run_agent(user_message: str, max_iterations: int = 5) -> str:
    """Kor en enkel agent loop."""
    messages = [
        {"role": "system", "content": "Du ar en hjalpsam assistent."},
        {"role": "user", "content": user_message}
    ]

    for iteration in range(max_iterations):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if assistant_message.tool_calls:
            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                result = TOOL_FUNCTIONS[function_name](**arguments)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        else:
            return assistant_message.content

    return "Max iterationer nadda"

print(run_agent("Vad ar vadret i Stockholm?"))
```

------------------------------------------------------------

## Guard Rails

```python
class AgentGuards:
    def __init__(self, max_iterations: int = 10, max_tool_calls: int = 20):
        self.max_iterations = max_iterations
        self.max_tool_calls = max_tool_calls
        self.tool_call_count = 0

    def check_iteration(self, iteration: int) -> bool:
        if iteration >= self.max_iterations:
            raise Exception("Max iterations exceeded")
        return True

    def check_tool_call(self) -> bool:
        self.tool_call_count += 1
        if self.tool_call_count > self.max_tool_calls:
            raise Exception("Max tool calls exceeded")
        return True
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Oandlig loop | Ingen stopping condition | Implementera guard rails |
| Fel verktyg | Otydlig beskrivning | Battre tool descriptions |
| Hallucinerar resultat | Saknar validering | Validera tool results |
| For langsamt | For manga iterationer | Begrans max_iterations |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Agent vs Chatbot | Agenter kan planera, agera och observera |
| Fyra komponenter | Brain, Tools, Memory, Perception |
| Autonominiva | 0-5, valj ratt niva for use case |
| Guard rails | Kritiskt for att undvika problem |

Kom ihag:
- Borja med enkel tool use (niva 3)
- Implementera alltid guard rails
- Testa noggrant innan produktion
- Hogre autonomi = hogre risk
'''
}

NODE_06_AGENT_TOOLS = {
    "node_id": 6,
    "title": "Agent Tools och Function Calling",
    "slug": "agent-tools",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [5],
    "content": '''
# Agent Tools och Function Calling

Bygg verktyg som ger agenter superkrafter.

------------------------------------------------------------

## Vad ar Agent Tools?

Tools ar funktioner som agenten kan anropa for att interagera med omvarlden. OpenAIs function calling later LLM strukturerat beskriva vilken funktion den vill anvanda.

| Tool-typ | Exempel | Risk |
|----------|---------|------|
| Retrieval | web_search, read_file | Lag |
| Mutation | write_file, send_email | Medium |
| Computation | execute_code, calculate | Medium |
| Integration | slack_message, github_action | Hog |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Automation | Agenter kan kora kommandon |
| Integration | Koppla ihop olika system |
| Effektivitet | Automatisera repetitiva uppgifter |
| Flexibilitet | Lagg till nya verktyg efter behov |

------------------------------------------------------------

## Snabbreferens - Tool Schema

| Falt | Beskrivning |
|------|-------------|
| name | Unikt verktygsnamn (snake_case) |
| description | LLM laser detta for att valja |
| parameters | JSON Schema for input |
| required | Obligatoriska falt |

------------------------------------------------------------

## Tool Schema Struktur

```
+-----------------------------------------------------------------+
|                   TOOL/FUNCTION SCHEMA                           |
+-----------------------------------------------------------------+
|                                                                  |
|  {                                                               |
|    "type": "function",                                           |
|    "function": {                                                 |
|      "name": "search_products",                                  |
|      "description": "Sok efter produkter i databasen",          |
|      "parameters": {                                             |
|        "type": "object",                                         |
|        "properties": {                                           |
|          "query": {                                              |
|            "type": "string",                                     |
|            "description": "Sokterm"                              |
|          },                                                      |
|          "category": {                                           |
|            "type": "string",                                     |
|            "enum": ["electronics", "clothing"]                   |
|          },                                                      |
|          "max_results": {                                        |
|            "type": "integer",                                    |
|            "default": 10                                         |
|          }                                                       |
|        },                                                        |
|        "required": ["query"]                                     |
|      }                                                           |
|    }                                                             |
|  }                                                               |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Base Tool Pattern

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional
import json

@dataclass
class ToolResult:
    """Standardiserat resultat fran verktyg."""
    success: bool
    data: Any
    error: Optional[str] = None

    def to_string(self) -> str:
        if self.success:
            return json.dumps(self.data) if isinstance(self.data, dict) else str(self.data)
        return f"Error: {self.error}"

class BaseTool(ABC):
    """Abstrakt basklass for alla verktyg."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        pass

    @abstractmethod
    def execute(self, **kwargs) -> ToolResult:
        pass

    def to_openai_schema(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }
```

------------------------------------------------------------

## Konkreta Verktyg

```python
class WeatherTool(BaseTool):
    """Hamta vaderinformation."""

    @property
    def name(self) -> str:
        return "get_weather"

    @property
    def description(self) -> str:
        return "Hamta aktuellt vader for en stad."

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Stadsnamn"
                }
            },
            "required": ["city"]
        }

    def execute(self, city: str) -> ToolResult:
        # I produktion: anvand riktig API
        weather_data = {
            "city": city,
            "temperature": 15,
            "condition": "cloudy"
        }
        return ToolResult(success=True, data=weather_data)


class CalculatorTool(BaseTool):
    """Saker matematisk kalkylator."""

    @property
    def name(self) -> str:
        return "calculate"

    @property
    def description(self) -> str:
        return "Utfor matematiska berakningar."

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Matematiskt uttryck"
                }
            },
            "required": ["expression"]
        }

    def execute(self, expression: str) -> ToolResult:
        import math
        safe_dict = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "pi": math.pi,
        }
        try:
            result = eval(expression, {"__builtins__": {}}, safe_dict)
            return ToolResult(success=True, data={"result": result})
        except Exception as e:
            return ToolResult(success=False, data=None, error=str(e))
```

------------------------------------------------------------

## Tool Registry

```python
class ToolRegistry:
    """Hantera och exekvera verktyg."""

    def __init__(self):
        self.tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        self.tools[tool.name] = tool

    def get_schemas(self) -> list[dict]:
        return [tool.to_openai_schema() for tool in self.tools.values()]

    def execute(self, tool_name: str, arguments: dict) -> ToolResult:
        if tool_name not in self.tools:
            return ToolResult(
                success=False,
                data=None,
                error=f"Unknown tool: {tool_name}"
            )
        return self.tools[tool_name].execute(**arguments)

# Anvandning
registry = ToolRegistry()
registry.register(WeatherTool())
registry.register(CalculatorTool())

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Vad ar vadret i Stockholm?"}],
    tools=registry.get_schemas(),
    tool_choice="auto"
)
```

------------------------------------------------------------

## Hantera Tool Calls

```python
def process_tool_calls(response, registry: ToolRegistry) -> list[dict]:
    """Process tool calls fran LLM response."""
    tool_results = []
    message = response.choices[0].message

    if not message.tool_calls:
        return []

    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"Executing: {tool_name}({arguments})")
        result = registry.execute(tool_name, arguments)

        tool_results.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result.to_string()
        })

    return tool_results
```

------------------------------------------------------------

## Battre Tool Beskrivningar

```python
class ImprovedSearchTool(BaseTool):
    @property
    def description(self) -> str:
        return """
        Sok i produktdatabasen.

        ANVAND FOR:
        - Hitta produkter under 500kr
        - Sok efter bla trojor
        - Kolla om iPhone finns i lager

        ANVAND INTE FOR:
        - Allman information
        - Vader eller nyheter
        - Berakningar
        """
```

------------------------------------------------------------

## Validering med Pydantic

```python
from pydantic import BaseModel, Field, validator

class SearchParams(BaseModel):
    query: str = Field(..., min_length=1, max_length=200)
    category: str = Field(default="all")
    max_results: int = Field(default=10, ge=1, le=50)

    @validator('query')
    def clean_query(cls, v):
        return v.strip().lower()

def execute(self, **kwargs) -> ToolResult:
    try:
        params = SearchParams(**kwargs)
    except Exception as e:
        return ToolResult(success=False, data=None, error=f"Invalid params: {e}")
    # Fortsatt med validerade params
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| LLM anropar fel verktyg | Otydlig beskrivning | Mer explicit med exempel |
| Felaktiga arguments | Ingen validering | Anvand Pydantic |
| Parallella calls misslyckas | Synkron kod | Anvand asyncio |
| Sakerhetsproblem | Ingen input-sanering | Validera all input |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Tools | Ger agenter formagan att interagera |
| JSON Schema | Definierar verktygets parametrar |
| ToolRegistry | Centraliserar hantering |
| Validering | Pydantic forindrar felaktig input |

Kom ihag:
- Borja med read-only tools
- Validera all input
- Skriv tydliga beskrivningar
- Kategorisera efter risk
'''
}

BLOCK_03_NODES = [NODE_05_WHAT_ARE_AGENTS, NODE_06_AGENT_TOOLS]
