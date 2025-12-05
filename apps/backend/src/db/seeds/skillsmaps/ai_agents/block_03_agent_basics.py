"""
AI Agents SkillsMap - Block 03: Agent Basics
Nodes 5-6: What are AI Agents, Agent Tools
"""

BLOCK_03_NODES = [
    {
        "id": "ai-agents-05",
        "slug": "what-are-ai-agents",
        "title": "What are AI Agents?",
        "order_index": 5,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-04"],
        "content": """# What are AI Agents?

## Varför detta är viktigt

En LLM utan agentkapacitet är som en expert som kan svara på frågor men aldrig agera.
AI Agents är nästa evolution — system som kan:

- **Planera** multi-steg uppgifter autonomt
- **Agera** genom att använda externa verktyg
- **Observera** resultat och anpassa sig
- **Lära sig** (inom en session) från sina misstag

År 2024 var "agent" det mest hypade ordet i AI. Men majoriteten av "agenter" är glorifierade
chatbots. Efter denna modul kommer du förstå vad en RIKTIG agent är — och hur du bygger en.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Definiera vad som skiljer en agent från en enkel LLM-applikation
- ✅ Identifiera de fyra kärnkomponenterna i en agent
- ✅ Klassificera agenter efter autonomi (nivå 1-5)
- ✅ Välja rätt agentarkitektur för olika use cases
- ✅ Förstå varför vissa "agenter" egentligen inte är agenter

## Kärnkoncept

### Agent vs Chatbot vs RAG

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI APPLICATION SPECTRUM                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LEVEL 0: Basic LLM                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  User → LLM → Response                                               │   │
│  │  • Single turn                                                        │   │
│  │  • No memory                                                          │   │
│  │  • No tools                                                           │   │
│  │  • Example: Simple Q&A                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LEVEL 1: Chatbot                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  User → LLM (+ conversation history) → Response                      │   │
│  │  • Multi-turn conversation                                            │   │
│  │  • Session memory                                                     │   │
│  │  • No tools                                                           │   │
│  │  • Example: Customer support bot                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LEVEL 2: RAG Application                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  User → Retriever → LLM (+ context) → Response                       │   │
│  │  • Access to external knowledge                                       │   │
│  │  • No autonomous actions                                              │   │
│  │  • Example: Documentation assistant                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LEVEL 3: Simple Agent                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  User → LLM → [Tool Call] → Observation → Response                   │   │
│  │  • Can use tools                                                      │   │
│  │  • Single action                                                      │   │
│  │  • Human in the loop                                                  │   │
│  │  • Example: Code assistant med file access                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LEVEL 4: Agentic System (ReAct, CoT)                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  User → Plan → Action → Observe → Reflect → Action → ... → Done      │   │
│  │  • Multi-step reasoning                                               │   │
│  │  • Tool chaining                                                      │   │
│  │  • Self-correction                                                    │   │
│  │  • Example: Research agent, code refactoring                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LEVEL 5: Autonomous Agent                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Goal → Plan → Execute → Monitor → Adjust → ... (continuous)         │   │
│  │  • Minimal human intervention                                         │   │
│  │  • Long-running tasks                                                 │   │
│  │  • Creates sub-agents                                                 │   │
│  │  • Example: AutoGPT, BabyAGI (experimental)                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### De fyra kärnkomponenterna

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT CORE COMPONENTS                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                         ┌─────────────────┐                                 │
│                         │    🧠 BRAIN     │                                 │
│                         │   (LLM/Model)   │                                 │
│                         │                 │                                 │
│                         │ • Reasoning     │                                 │
│                         │ • Planning      │                                 │
│                         │ • Decisions     │                                 │
│                         └────────┬────────┘                                 │
│                                  │                                          │
│            ┌─────────────────────┼─────────────────────┐                   │
│            │                     │                     │                    │
│            ▼                     ▼                     ▼                    │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐          │
│  │  👁️ PERCEPTION  │   │  🛠️ TOOLS       │   │  💾 MEMORY      │          │
│  │                 │   │                 │   │                 │           │
│  │ • User input    │   │ • Code exec     │   │ • Short-term    │          │
│  │ • File content  │   │ • Web search    │   │ • Long-term     │          │
│  │ • API responses │   │ • Database      │   │ • Episodic      │          │
│  │ • Observations  │   │ • File I/O      │   │ • Semantic      │          │
│  └─────────────────┘   └─────────────────┘   └─────────────────┘          │
│                                                                              │
│                         ┌─────────────────┐                                 │
│                         │  🎯 ACTION      │                                 │
│                         │                 │                                 │
│                         │ • Tool calls    │                                 │
│                         │ • Responses     │                                 │
│                         │ • State updates │                                 │
│                         └─────────────────┘                                 │
│                                                                              │
│  SIMPLIFIED: Brain decides, Tools execute, Memory persists, Perception     │
│              gathers information from environment                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Agent Use Cases

| Use Case | Autonomy Level | Tools Needed | Risk Level |
|----------|----------------|--------------|------------|
| **Code completion** | 2-3 | None/File read | Low |
| **Code generation** | 3 | File write, exec | Medium |
| **Research assistant** | 3-4 | Web search, RAG | Low |
| **Data analysis** | 3-4 | Python exec, DB | Medium |
| **Customer support** | 2-3 | CRM, knowledge base | Medium |
| **DevOps automation** | 4 | Shell, cloud APIs | High |
| **Autonomous coding** | 4-5 | Full env access | Very High |

## Steg-för-steg: Din första agent

### 1. Setup

```python
from openai import OpenAI
import json
from typing import Callable

client = OpenAI()

# Definiera tillgängliga verktyg
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Hämta väderinformation för en stad",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Stadens namn, t.ex. 'Stockholm'"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Utför matematiska beräkningar",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Matematiskt uttryck, t.ex. '2 + 2 * 3'"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]
```

### 2. Implementera verktygsfunktioner

```python
def get_weather(city: str) -> str:
    \"\"\"Simulerad väderdata (i produktion: använd riktig API).\"\"\"
    # Fake data för demo
    weather_data = {
        "stockholm": {"temp": 5, "condition": "cloudy"},
        "gothenburg": {"temp": 7, "condition": "rainy"},
        "malmö": {"temp": 8, "condition": "sunny"},
    }

    city_lower = city.lower()
    if city_lower in weather_data:
        data = weather_data[city_lower]
        return f"Väder i {city}: {data['temp']}°C, {data['condition']}"
    return f"Ingen väderdata för {city}"

def calculate(expression: str) -> str:
    \"\"\"Säker matematisk beräkning.\"\"\"
    try:
        # VARNING: eval() är farligt! Använd ast.literal_eval eller numexpr i produktion
        # Här tillåter vi bara säkra operationer
        allowed_chars = set("0123456789+-*/().% ")
        if not all(c in allowed_chars for c in expression):
            return "Fel: Ogiltiga tecken i uttrycket"

        result = eval(expression)
        return f"Resultat: {expression} = {result}"
    except Exception as e:
        return f"Fel vid beräkning: {e}"

# Mappa funktionsnamn till funktioner
TOOL_FUNCTIONS = {
    "get_weather": get_weather,
    "calculate": calculate
}
```

### 3. Bygg agent-loopen

```python
def run_agent(user_message: str, max_iterations: int = 5) -> str:
    \"\"\"
    Kör en enkel ReAct-liknande agent.

    Loop:
    1. Skicka meddelande till LLM
    2. Om LLM vill använda verktyg → kör verktyg
    3. Skicka tillbaka resultat till LLM
    4. Repetera tills LLM ger slutgiltigt svar
    \"\"\"
    messages = [
        {
            "role": "system",
            "content": \"\"\"Du är en hjälpsam assistent med tillgång till verktyg.
            Använd verktyg när det behövs för att svara på frågor.
            När du har all information du behöver, ge ett sammanfattande svar.\"\"\"
        },
        {"role": "user", "content": user_message}
    ]

    for iteration in range(max_iterations):
        print(f"\\n--- Iteration {iteration + 1} ---")

        # Anropa LLM
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"  # LLM väljer om verktyg behövs
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        # Kolla om LLM vill använda verktyg
        if assistant_message.tool_calls:
            print(f"🛠️ Agent vill använda {len(assistant_message.tool_calls)} verktyg")

            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                print(f"  → Kör {function_name}({arguments})")

                # Kör verktyget
                if function_name in TOOL_FUNCTIONS:
                    result = TOOL_FUNCTIONS[function_name](**arguments)
                else:
                    result = f"Okänt verktyg: {function_name}"

                print(f"  ← Resultat: {result}")

                # Lägg till verktygsresultat i konversationen
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        else:
            # Inget verktygsanrop = slutgiltigt svar
            print("✅ Agent klar med slutgiltigt svar")
            return assistant_message.content

    return "Max iterationer nådda utan slutgiltigt svar"

# Test agenten
print(run_agent("Vad är vädret i Stockholm och vad är 15% av 200?"))
```

### 4. Förbättra med ReAct-prompting

```python
REACT_SYSTEM_PROMPT = \"\"\"
Du är en AI-assistent som löser uppgifter genom att tänka steg för steg.

För varje steg:
1. THOUGHT: Analysera vad du vet och vad du behöver veta
2. ACTION: Om du behöver information, använd ett verktyg
3. OBSERVATION: Analysera verktygets resultat
4. Repetera tills du har tillräcklig information
5. ANSWER: Ge ett slutgiltigt, sammanfattande svar

Exempel:
User: Vad är vädret i Stockholm och hur känns det?

THOUGHT: Jag behöver veta aktuellt väder i Stockholm för att kunna beskriva hur det känns.
ACTION: get_weather(city="Stockholm")
OBSERVATION: Väder i Stockholm: 5°C, cloudy
THOUGHT: Nu vet jag temperaturen och vädret. 5°C med molnigt är kyligt men inte extremt kallt.
ANSWER: I Stockholm är det just nu 5°C och molnigt. Det känns kyligt, så en jacka rekommenderas.

Börja nu med användarens fråga.
\"\"\"

def run_react_agent(user_message: str) -> str:
    messages = [
        {"role": "system", "content": REACT_SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]

    # Samma loop som innan men med ReAct prompting
    return run_agent_loop(messages)
```

## Vanliga problem

### Problem 1: "Agenten fastnar i oändlig loop"

```python
# Lösning: Implementera guard rails
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

# Användning
guards = AgentGuards(max_iterations=5, max_tool_calls=15)
```

### Problem 2: "Agenten använder fel verktyg"

```python
# Lösning: Bättre verktygsbeskrivningar
BETTER_TOOL = {
    "type": "function",
    "function": {
        "name": "search_database",
        "description": \"\"\"
        Sök i produktdatabasen. Använd ENDAST för att hitta produktinformation.

        ANVÄND DETTA VERKTYG NÄR:
        - Användaren frågar om en specifik produkt
        - Du behöver priser eller lagerstatus

        ANVÄND INTE DETTA VERKTYG FÖR:
        - Allmänna frågor
        - Väder eller tid
        - Beräkningar
        \"\"\",
        "parameters": {...}
    }
}
```

### Problem 3: "Agenten hallucinerar verktygsresultat"

```python
# Lösning: Explicit tool-result validation
def validate_tool_result(tool_name: str, result: str) -> str:
    \"\"\"Markera verktygsresultat tydligt för LLM.\"\"\"
    return f\"\"\"
    [TOOL RESULT - {tool_name}]
    {result}
    [END TOOL RESULT]

    VIKTIGT: Basera ditt svar ENDAST på ovanstående verktygsresultat.
    Gissa inte eller lägg till information som inte finns i resultatet.
    \"\"\"
```

## Praktisk övning

**Uppgift:** Bygg en Research Agent

```python
class ResearchAgent:
    \"\"\"
    En agent som kan:
    1. Söka på webben (simulerat)
    2. Sammanfatta text
    3. Jämföra information från olika källor

    TODO: Implementera följande metoder
    \"\"\"

    def __init__(self):
        self.sources = []
        self.findings = []

    def search(self, query: str) -> list[dict]:
        \"\"\"Simulera webbsökning. Returnera lista med 'title' och 'snippet'.\"\"\"
        # Din kod här
        pass

    def summarize(self, text: str) -> str:
        \"\"\"Sammanfatta text med LLM.\"\"\"
        # Din kod här
        pass

    def research(self, topic: str) -> str:
        \"\"\"
        Huvudmetod: Utför research om ett ämne.

        Steg:
        1. Sök efter information
        2. Sammanfatta varje källa
        3. Syntetisera till en rapport
        \"\"\"
        # Din kod här
        pass

# Test
agent = ResearchAgent()
report = agent.research("Fördelar och nackdelar med microservices")
print(report)
```

## Sammanfattning

- ✅ **Agent ≠ Chatbot** — Agenter kan planera, agera och observera
- ✅ **Fyra komponenter:** Brain (LLM), Tools, Memory, Perception
- ✅ **Autonomi-nivåer** varierar från 1 (tool use) till 5 (autonomous)
- ✅ **ReAct pattern:** Think → Act → Observe → Repeat
- ✅ **Guard rails** är kritiska för att undvika oändliga loopar

## Nästa steg

Nu när du förstår vad en agent är, fortsätt till:

- **Node 6:** Agent Tools — Djupdykning i verktygsdesign
- **Node 7:** Agent Loop — Perception, Reasoning, Action

---
*Pro tip: Starta med enkel tool use (nivå 3) innan du bygger autonoma system!*
"""
    },
    {
        "id": "ai-agents-06",
        "slug": "agent-tools",
        "title": "Agent Tools och Function Calling",
        "order_index": 6,
        "estimated_minutes": 50,
        "xp_reward": 130,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["ai-agents-05"],
        "content": """# Agent Tools och Function Calling

## Varför detta är viktigt

Tools är det som ger agenter superkrafter. En LLM utan tools kan bara generera text.
En LLM MED tools kan:

- **Söka på webben** i realtid
- **Köra kod** och se resultat
- **Skriva till databaser**
- **Skicka email och notifikationer**
- **Kontrollera externa system**

OpenAI:s function calling (nu "tools") revolutionerade agentbyggande 2023. Det låter
LLM:en strukturerat beskriva vilken funktion den vill anropa, istället för att gissa
baserat på text-output. Resultatet? 10x mer pålitliga agenter.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Designa tool-scheman med JSON Schema
- ✅ Implementera säkra tool-funktioner
- ✅ Hantera parallella och sekventiella tool calls
- ✅ Validera tool-inputs och outputs
- ✅ Bygga återanvändbara tool-bibliotek

## Kärnkoncept

### Tool Anatomy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TOOL/FUNCTION SCHEMA                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  {                                                                           │
│    "type": "function",                                                       │
│    "function": {                                                             │
│      "name": "search_products",          ← Unikt namn (snake_case)          │
│      "description": "Sök efter...",      ← LLM läser detta för att välja   │
│      "parameters": {                      ← JSON Schema format              │
│        "type": "object",                                                     │
│        "properties": {                                                       │
│          "query": {                                                          │
│            "type": "string",                                                 │
│            "description": "Sökterm"      ← Hjälper LLM fylla i korrekt     │
│          },                                                                  │
│          "category": {                                                       │
│            "type": "string",                                                 │
│            "enum": ["electronics", "clothing", "food"],  ← Begränsa val    │
│            "description": "Produktkategori"                                 │
│          },                                                                  │
│          "max_results": {                                                    │
│            "type": "integer",                                                │
│            "default": 10                  ← Defaultvärde                    │
│          }                                                                   │
│        },                                                                    │
│        "required": ["query"]              ← Obligatoriska fält              │
│      }                                                                       │
│    }                                                                         │
│  }                                                                           │
│                                                                              │
│  LLM OUTPUT (tool_call):                                                    │
│  {                                                                           │
│    "id": "call_abc123",                                                      │
│    "type": "function",                                                       │
│    "function": {                                                             │
│      "name": "search_products",                                              │
│      "arguments": "{\"query\": \"laptop\", \"category\": \"electronics\"}" │
│    }                                                                         │
│  }                                                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Tool Types

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         COMMON TOOL CATEGORIES                              │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  📖 RETRIEVAL TOOLS                                                        │
│  ├─ search_web: Sök på internet                                            │
│  ├─ search_database: Query intern databas                                  │
│  ├─ read_file: Läs filinnehåll                                             │
│  └─ get_api_data: Hämta från extern API                                    │
│                                                                             │
│  ✏️ MUTATION TOOLS                                                         │
│  ├─ write_file: Skriv till fil                                             │
│  ├─ update_database: Uppdatera DB                                          │
│  ├─ send_email: Skicka meddelande                                          │
│  └─ create_ticket: Skapa ärende i system                                   │
│                                                                             │
│  🔧 COMPUTATION TOOLS                                                      │
│  ├─ execute_code: Kör Python/JS kod                                        │
│  ├─ calculate: Matematiska beräkningar                                     │
│  ├─ analyze_data: Statistisk analys                                        │
│  └─ generate_chart: Skapa visualisering                                    │
│                                                                             │
│  🌐 INTEGRATION TOOLS                                                      │
│  ├─ slack_message: Skicka till Slack                                       │
│  ├─ github_action: Trigga GitHub workflow                                  │
│  ├─ jira_update: Uppdatera Jira ticket                                     │
│  └─ calendar_event: Skapa kalenderhändelse                                 │
│                                                                             │
│  RISK LEVELS:                                                               │
│  🟢 Read-only (search, get) - Låg risk                                     │
│  🟡 Create (write, send) - Medium risk                                     │
│  🔴 Delete/Execute (rm, exec) - Hög risk → KRÄVER APPROVAL                 │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Bygg ett Tool Library

### 1. Base Tool Pattern

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional
import json

@dataclass
class ToolResult:
    \"\"\"Standardiserat resultat från verktyg.\"\"\"
    success: bool
    data: Any
    error: Optional[str] = None

    def to_string(self) -> str:
        if self.success:
            return json.dumps(self.data) if isinstance(self.data, dict) else str(self.data)
        return f"Error: {self.error}"

class BaseTool(ABC):
    \"\"\"Abstrakt basklass för alla verktyg.\"\"\"

    @property
    @abstractmethod
    def name(self) -> str:
        \"\"\"Unikt verktygsnamn.\"\"\"
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        \"\"\"Beskrivning för LLM.\"\"\"
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        \"\"\"JSON Schema för parametrar.\"\"\"
        pass

    @abstractmethod
    def execute(self, **kwargs) -> ToolResult:
        \"\"\"Kör verktyget med givna parametrar.\"\"\"
        pass

    def to_openai_schema(self) -> dict:
        \"\"\"Konvertera till OpenAI tool format.\"\"\"
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }
```

### 2. Implementera konkreta verktyg

```python
import requests
from datetime import datetime

class WeatherTool(BaseTool):
    \"\"\"Hämta väderinformation.\"\"\"

    @property
    def name(self) -> str:
        return "get_weather"

    @property
    def description(self) -> str:
        return \"\"\"
        Hämta aktuellt väder för en stad.
        Returnerar temperatur, väderförhållanden och luftfuktighet.
        \"\"\"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Stadsnamn, t.ex. 'Stockholm' eller 'New York'"
                },
                "units": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "default": "celsius",
                    "description": "Temperaturenhet"
                }
            },
            "required": ["city"]
        }

    def execute(self, city: str, units: str = "celsius") -> ToolResult:
        try:
            # I produktion: använd riktig väder-API
            # api_key = os.getenv("WEATHER_API_KEY")
            # response = requests.get(f"https://api.weather.com/...")

            # Simulerad data för demo
            weather_data = {
                "city": city,
                "temperature": 15 if units == "celsius" else 59,
                "unit": "°C" if units == "celsius" else "°F",
                "condition": "partly cloudy",
                "humidity": 65,
                "timestamp": datetime.now().isoformat()
            }

            return ToolResult(success=True, data=weather_data)

        except Exception as e:
            return ToolResult(success=False, data=None, error=str(e))


class CalculatorTool(BaseTool):
    \"\"\"Säker matematisk kalkylator.\"\"\"

    @property
    def name(self) -> str:
        return "calculate"

    @property
    def description(self) -> str:
        return \"\"\"
        Utför matematiska beräkningar.
        Stödjer: +, -, *, /, **, sqrt, sin, cos, tan, log
        Exempel: "sqrt(16) + 2**3" → 12.0
        \"\"\"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Matematiskt uttryck att beräkna"
                }
            },
            "required": ["expression"]
        }

    def execute(self, expression: str) -> ToolResult:
        import math

        # Tillåtna funktioner och konstanter
        safe_dict = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "log10": math.log10,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "round": round,
        }

        try:
            # Validera input
            allowed_chars = set("0123456789+-*/().%** sqrtincoanloge")
            clean_expr = expression.replace(" ", "")

            # Ersätt funktionsnamn temporärt för validering
            for func in safe_dict:
                clean_expr = clean_expr.replace(func, "")

            if not all(c in allowed_chars for c in clean_expr):
                return ToolResult(
                    success=False,
                    data=None,
                    error="Ogiltiga tecken i uttrycket"
                )

            # Beräkna med begränsad namespace
            result = eval(expression, {"__builtins__": {}}, safe_dict)

            return ToolResult(success=True, data={
                "expression": expression,
                "result": result
            })

        except Exception as e:
            return ToolResult(success=False, data=None, error=f"Beräkningsfel: {e}")


class WebSearchTool(BaseTool):
    \"\"\"Sök på webben (simulerat).\"\"\"

    @property
    def name(self) -> str:
        return "web_search"

    @property
    def description(self) -> str:
        return \"\"\"
        Sök på webben efter information.
        Använd för aktuell information som LLM inte har.
        Returnerar topp 5 resultat med titel, snippet och URL.
        \"\"\"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Sökfras"
                },
                "num_results": {
                    "type": "integer",
                    "default": 5,
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Antal resultat"
                }
            },
            "required": ["query"]
        }

    def execute(self, query: str, num_results: int = 5) -> ToolResult:
        # I produktion: använd Google Search API, Bing, eller SerpAPI
        # response = requests.get("https://serpapi.com/search", params={...})

        # Simulerad data
        fake_results = [
            {
                "title": f"Result {i+1} for '{query}'",
                "snippet": f"This is a snippet about {query}...",
                "url": f"https://example.com/{query.replace(' ', '-')}/{i}"
            }
            for i in range(num_results)
        ]

        return ToolResult(success=True, data={
            "query": query,
            "results": fake_results,
            "total_results": num_results
        })
```

### 3. Tool Registry och execution

```python
class ToolRegistry:
    \"\"\"Hantera och exekvera verktyg.\"\"\"

    def __init__(self):
        self.tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        \"\"\"Registrera ett verktyg.\"\"\"
        self.tools[tool.name] = tool

    def get_schemas(self) -> list[dict]:
        \"\"\"Hämta alla verktygsscheman för OpenAI API.\"\"\"
        return [tool.to_openai_schema() for tool in self.tools.values()]

    def execute(self, tool_name: str, arguments: dict) -> ToolResult:
        \"\"\"Exekvera ett verktyg med givna argument.\"\"\"
        if tool_name not in self.tools:
            return ToolResult(
                success=False,
                data=None,
                error=f"Unknown tool: {tool_name}"
            )

        tool = self.tools[tool_name]
        return tool.execute(**arguments)

# Skapa registry och registrera verktyg
registry = ToolRegistry()
registry.register(WeatherTool())
registry.register(CalculatorTool())
registry.register(WebSearchTool())

# Använd med OpenAI
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Vad är vädret i Stockholm?"}],
    tools=registry.get_schemas(),
    tool_choice="auto"
)
```

### 4. Hantera tool calls

```python
def process_tool_calls(response, registry: ToolRegistry) -> list[dict]:
    \"\"\"Process tool calls från LLM response.\"\"\"
    tool_results = []

    message = response.choices[0].message

    if not message.tool_calls:
        return []

    for tool_call in message.tool_calls:
        # Extrahera info
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"🛠️ Executing: {tool_name}({arguments})")

        # Exekvera verktyg
        result = registry.execute(tool_name, arguments)

        # Formatera för API
        tool_results.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result.to_string()
        })

        print(f"   Result: {result.to_string()[:100]}...")

    return tool_results

# Full agent loop med tool handling
def agent_with_tools(user_message: str, registry: ToolRegistry) -> str:
    messages = [
        {"role": "system", "content": "Du är en hjälpsam assistent med tillgång till verktyg."},
        {"role": "user", "content": user_message}
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=registry.get_schemas(),
            tool_choice="auto"
        )

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            # Process och lägg till tool results
            tool_results = process_tool_calls(response, registry)
            messages.extend(tool_results)
        else:
            # Inget verktygsanrop = slutgiltigt svar
            return message.content

# Test
print(agent_with_tools(
    "Beräkna 15% av 250 och berätta sedan vad vädret är i London",
    registry
))
```

## Vanliga problem

### Problem 1: "LLM anropar fel verktyg"

```python
# Lösning: Mer explicit beskrivning med exempel
class ImprovedSearchTool(BaseTool):
    @property
    def description(self) -> str:
        return \"\"\"
        Sök i produktdatabasen.

        ANVÄND FÖR:
        ✓ "Hitta produkter under 500kr"
        ✓ "Sök efter blå tröjor"
        ✓ "Finns iPhone 15 i lager?"

        ANVÄND INTE FÖR:
        ✗ Allmän information
        ✗ Väder eller nyheter
        ✗ Beräkningar

        EXEMPEL INPUT:
        - query: "laptop gaming"
        - category: "electronics"
        - max_price: 15000
        \"\"\"
```

### Problem 2: "Tool arguments är felaktiga"

```python
# Lösning: Validera med Pydantic
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

    # Fortsätt med validerade params
    ...
```

### Problem 3: "Parallella tool calls hanteras fel"

```python
import asyncio

async def process_tool_calls_parallel(tool_calls, registry) -> list[dict]:
    \"\"\"Process multiple tool calls in parallel.\"\"\"

    async def execute_single(tool_call):
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        # Kör i thread pool för sync functions
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: registry.execute(tool_name, arguments)
        )

        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result.to_string()
        }

    # Kör alla parallellt
    results = await asyncio.gather(*[
        execute_single(tc) for tc in tool_calls
    ])

    return list(results)
```

## Praktisk övning

**Uppgift:** Bygg ett komplett tool library

```python
class FileSystemTool(BaseTool):
    \"\"\"
    TODO: Implementera ett filsystemverktyg som kan:
    - list_files: Lista filer i en katalog
    - read_file: Läsa innehåll från en fil
    - write_file: Skriva till en fil (med bekräftelse!)

    SÄKERHET:
    - Begränsa till specifik workspace-katalog
    - Validera filnamn (inga ../path/traversal)
    - Kräv bekräftelse för write operations
    \"\"\"
    pass

class DatabaseTool(BaseTool):
    \"\"\"
    TODO: Implementera ett databasverktyg som kan:
    - query: Köra SELECT queries
    - insert: Lägga till data
    - update: Uppdatera data

    SÄKERHET:
    - Endast parametriserade queries
    - Ingen DROP/DELETE utan explicit tillstånd
    - Loggning av alla operationer
    \"\"\"
    pass

# Skapa och testa ditt tool library
my_registry = ToolRegistry()
my_registry.register(FileSystemTool(workspace="/tmp/agent-workspace"))
my_registry.register(DatabaseTool(connection_string="sqlite:///test.db"))

# Test
result = agent_with_tools(
    "Lista alla .py filer i workspace och visa innehållet i den största",
    my_registry
)
```

## Sammanfattning

- ✅ **Tools** ger agenter förmågan att interagera med omvärlden
- ✅ **JSON Schema** definierar verktygets parametrar
- ✅ **ToolRegistry** centraliserar hantering och execution
- ✅ **Validering** (Pydantic) förhindrar felaktiga inputs
- ✅ **Säkerhet** är kritiskt — kategorisera efter risk och kräv approval

## Nästa steg

Nu när du kan bygga verktyg, fortsätt till:

- **Node 7:** Agent Loop — Perception, Reasoning, Action cycle
- **Node 8:** Observation & Reflection — Hur agenter lär sig

---
*Pro tip: Börja med read-only tools och lägg till write/execute försiktigt!*
"""
    }
]
