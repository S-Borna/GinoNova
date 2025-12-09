# =============================================================================
# AI AGENTS - BLOCK 06: FRAMEWORKS (Noder 11-12) - V3 FORMAT
# =============================================================================

NODE_11_LANGCHAIN = {
    "node_id": 11,
    "title": "LangChain Framework",
    "slug": "langchain-framework",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [10],
    "content": '''
# LangChain Framework

Det mest populara frameworket for att bygga AI-agenter.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar LangChain?

LangChain ar ett open-source framework for att bygga applikationer med LLMs. Det tillhandahaller byggblock for agenter, chains, memory och tools.

| Komponent | Funktion |
|-----------|----------|
| LLMs | Abstraktion for olika modeller |
| Chains | Sekvenser av operations |
| Agents | Autonoma beslut om tools |
| Memory | Konversationshistorik |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Snabb utveckling | Fardiga komponenter |
| Skalbarhet | Production-ready patterns |
| Ekosystem | Manga integrationer |
| Community | Stort community, bra docs |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - LangChain Components

| Komponent | Import | Anvandning |
|-----------|--------|------------|
| ChatOpenAI | langchain_openai | LLM wrapper |
| Tool | langchain.tools | Custom tools |
| AgentExecutor | langchain.agents | Agent runner |
| ConversationBufferMemory | langchain.memory | Minne |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## LangChain Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   LANGCHAIN ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                      APPLICATION                           │ │
│  └───────────────────────────────────────────────────────────┘ │
│                           │                                      │
│                           v                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                   AGENT EXECUTOR                           │ │
│  │  - Manages agent loop                                      │ │
│  │  - Handles tools                                           │ │
│  │  - Memory integration                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
│                           │                                      │
│           ┌───────────────┼───────────────┐                     │
│           v               v               v                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │    LLM      │  │   TOOLS     │  │   MEMORY    │             │
│  │  - OpenAI   │  │  - Custom   │  │  - Buffer   │             │
│  │  - Anthropic│  │  - Built-in │  │  - Summary  │             │
│  │  - Local    │  │  - API wrap │  │  - Vector   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installation och Setup

```python
# Installation
# pip install langchain langchain-openai

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

# Konfigurera LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Custom Tools

```python
from langchain.tools import tool
from pydantic import BaseModel, Field

# Enkel tool med decorator
@tool
def search_database(query: str) -> str:
    """Sok i databasen efter information."""
    return f"Resultat for: {query}"

# Tool med schema
class WeatherInput(BaseModel):
    city: str = Field(description="Stadens namn")
    units: str = Field(default="celsius", description="Temperaturenhet")

@tool(args_schema=WeatherInput)
def get_weather(city: str, units: str = "celsius") -> str:
    """Hamta vader for en stad."""
    return f"Vader i {city}: 15 grader {units}"

# Tool klass
from langchain.tools import BaseTool
from typing import Type, Optional

class CalculatorTool(BaseTool):
    name: str = "calculator"
    description: str = "Rakna ut matematiska uttryck"
    args_schema: Type[BaseModel] = None

    def _run(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"Resultat: {result}"
        except:
            return "Kunde inte berakna"

tools = [search_database, get_weather, CalculatorTool()]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Agent Setup

```python
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Definiera prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """Du ar en hjalpsam assistent for DevOps-uppgifter.

    Du har tillgang till foljande verktyg:
    - search_database: Sok i databasen
    - get_weather: Hamta vader
    - calculator: Matematiska berakningar

    Anvand verktygen vid behov for att svara pa fragor.
    """),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Skapa agent
agent = create_openai_tools_agent(llm, tools, prompt)

# Skapa executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True
)

# Kor agent
result = agent_executor.invoke({
    "input": "Vad ar vadret i Stockholm och vad ar 15 * 3?"
})
print(result["output"])
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Memory

```python
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory

# Buffer memory - sparar alla meddelanden
buffer_memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Summary memory - sammanfattar lange konversationer
summary_memory = ConversationSummaryMemory(
    llm=llm,
    memory_key="chat_history",
    return_messages=True
)

# Agent med memory
agent_with_memory = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=buffer_memory,
    verbose=True
)

# Forsta fragor
result1 = agent_with_memory.invoke({"input": "Jag heter Erik"})
# Andra fragan - kommer ihag namn
result2 = agent_with_memory.invoke({"input": "Vad heter jag?"})
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## LangChain Expression Language (LCEL)

```python
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Enkel chain med LCEL
chain = prompt | llm | StrOutputParser()

# Mer komplex chain
from langchain_core.runnables import RunnableParallel

analysis_chain = RunnableParallel(
    weather=get_weather,
    calculation=CalculatorTool()
) | llm | StrOutputParser()

# Conditional routing
from langchain_core.runnables import RunnableBranch

route_chain = RunnableBranch(
    (lambda x: "vader" in x["input"].lower(), weather_chain),
    (lambda x: "rakna" in x["input"].lower(), math_chain),
    default_chain
)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Agent stannar | Max iterations | Oka max_iterations |
| Tool not found | Fel tool name | Kolla tool names |
| Memory overflow | For lang konversation | Anvand SummaryMemory |
| Parsing error | Dalig LLM output | handle_parsing_errors=True |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| AgentExecutor | Korer agent loop |
| Tools | @tool decorator for custom tools |
| Memory | Buffer eller Summary |
| LCEL | Deklarativ chain building |

Kom ihag:
- Anvand create_openai_tools_agent for moderna agenter
- Valj memory baserat pa konversationslanfd
- LCEL ar framtiden for LangChain
- verbose=True under utveckling
'''
}

NODE_12_OTHER_FRAMEWORKS = {
    "node_id": 12,
    "title": "LlamaIndex, AutoGen och Fler",
    "slug": "llamaindex-autogen",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [11],
    "content": '''
# LlamaIndex, AutoGen och Fler

Utforska alternativa frameworks for AI-agenter.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Framework Oversikt

Olika frameworks har olika styrkor och anvandningsomraden.

| Framework | Bast for |
|-----------|----------|
| LlamaIndex | RAG och datakallor |
| AutoGen | Multi-agent konversationer |
| CrewAI | Rollbaserade team |
| Haystack | Search och QA |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Ratt verktyg | Olika problem kraver olika losningar |
| Flexibilitet | Kombinera frameworks vid behov |
| Framtidssaker | Ekosystemet utvecklas snabbt |
| Kostnad | Vissa frameworks ar mer effektiva |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Framework Selection

| Scenario | Framework | Motivering |
|----------|-----------|------------|
| Sok i dokument | LlamaIndex | Bast pa RAG |
| Agent team | AutoGen | Multi-agent |
| Rollbaserat | CrewAI | Enkelt rollsystem |
| Enterprise search | Haystack | Production-ready |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Framework Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│                  FRAMEWORK COMPARISON                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LANGCHAIN          LLAMAINDEX        AUTOGEN                   │
│  ┌──────────┐       ┌──────────┐      ┌──────────┐              │
│  │ Chains   │       │ Indexes  │      │ Agents   │              │
│  │ Agents   │       │ Query    │      │ Converse │              │
│  │ Tools    │       │ RAG      │      │ Roles    │              │
│  │ Memory   │       │ Nodes    │      │ Groups   │              │
│  └──────────┘       └──────────┘      └──────────┘              │
│      │                  │                  │                     │
│      v                  v                  v                     │
│  General-purpose   Data-focused     Multi-agent                 │
│  Agent building    RAG/Search       Conversations               │
│                                                                  │
│  CREWAI            HAYSTACK                                     │
│  ┌──────────┐      ┌──────────┐                                 │
│  │ Crew     │      │ Pipeline │                                 │
│  │ Tasks    │      │ Nodes    │                                 │
│  │ Roles    │      │ Stores   │                                 │
│  └──────────┘      └──────────┘                                 │
│      │                  │                                        │
│      v                  v                                        │
│  Role-based        Enterprise                                   │
│  teams             search/QA                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## LlamaIndex

```python
# pip install llama-index llama-index-llms-openai

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# Ladda dokument
documents = SimpleDirectoryReader("./docs").load_data()

# Skapa index
index = VectorStoreIndex.from_documents(documents)

# Query engine
query_engine = index.as_query_engine()

# Tool fran query engine
query_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="doc_search",
        description="Sok i dokumentationen"
    )
)

# Skapa agent
llm = OpenAI(model="gpt-4o-mini")
agent = ReActAgent.from_tools(
    [query_tool],
    llm=llm,
    verbose=True
)

# Kor
response = agent.chat("Vad sager dokumentationen om deployment?")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AutoGen

```python
# pip install pyautogen

import autogen

# Konfiguration
config_list = [{"model": "gpt-4o-mini", "api_key": "..."}]

# Skapa agenter
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)

# Starta konversation
user_proxy.initiate_chat(
    assistant,
    message="Skriv en Python-funktion som raknar fibonacci"
)

# Group chat med flera agenter
coder = autogen.AssistantAgent(
    name="coder",
    system_message="Du ar en expert Python-programmerare"
)

reviewer = autogen.AssistantAgent(
    name="reviewer",
    system_message="Du ar en kodgranskare"
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, reviewer],
    messages=[],
    max_round=10
)

manager = autogen.GroupChatManager(groupchat=groupchat)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CrewAI

```python
# pip install crewai

from crewai import Agent, Task, Crew, Process

# Definiera agenter med roller
researcher = Agent(
    role="Forskare",
    goal="Hitta relevant information",
    backstory="Expert pa att hitta och analysera information",
    verbose=True
)

writer = Agent(
    role="Skribent",
    goal="Skriva tydliga rapporter",
    backstory="Expert pa att kommunicera teknisk information"
)

# Definiera tasks
research_task = Task(
    description="Undersok senaste trenderna inom {topic}",
    expected_output="En sammanfattning av viktiga trender",
    agent=researcher
)

write_task = Task(
    description="Skriv en rapport baserad pa forskningen",
    expected_output="En valstrukturerad rapport",
    agent=writer
)

# Skapa crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

# Kor
result = crew.kickoff(inputs={"topic": "AI i DevOps"})
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Haystack

```python
# pip install haystack-ai

from haystack import Pipeline
from haystack.components.generators import OpenAIGenerator
from haystack.components.builders import PromptBuilder

# Enkel pipeline
prompt_template = """
Svara pa fragan baserat pa kontexten.

Kontext: {{context}}
Fraga: {{question}}
"""

prompt_builder = PromptBuilder(template=prompt_template)
generator = OpenAIGenerator(model="gpt-4o-mini")

pipeline = Pipeline()
pipeline.add_component("prompt_builder", prompt_builder)
pipeline.add_component("generator", generator)
pipeline.connect("prompt_builder", "generator")

# Kor pipeline
result = pipeline.run({
    "prompt_builder": {
        "context": "DevOps ar...",
        "question": "Vad ar DevOps?"
    }
})
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Index tom | Inga dokument | Kolla SimpleDirectoryReader |
| AutoGen loop | Ingen termination | Satt max_round |
| CrewAI task fail | Otydlig description | Mer specifik task |
| Haystack error | Disconnected components | Kolla pipeline.connect |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Framework | Bast for |
|-----------|----------|
| LlamaIndex | RAG, dokumentsokning |
| AutoGen | Multi-agent konversationer |
| CrewAI | Rollbaserade team |
| Haystack | Enterprise pipelines |

Kom ihag:
- LlamaIndex for RAG-tunga applikationer
- AutoGen for multi-agent konversationer
- CrewAI for enkla rollbaserade teams
- Valj framework baserat pa use case
'''
}

BLOCK_06_NODES = [NODE_11_LANGCHAIN, NODE_12_OTHER_FRAMEWORKS]
