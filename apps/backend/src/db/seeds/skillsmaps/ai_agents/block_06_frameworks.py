"""
AI Agents SkillsMap - Block 06: Frameworks
Nodes 11-12: LangChain, LlamaIndex & AutoGen
"""

BLOCK_06_NODES = [
    {
        "id": "ai-agents-11",
        "slug": "langchain-framework",
        "title": "LangChain Framework Deep Dive",
        "order_index": 11,
        "estimated_minutes": 50,
        "xp_reward": 130,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["ai-agents-10"],
        "content": """# LangChain Framework Deep Dive

## Varför detta är viktigt

LangChain är det mest populära frameworket för att bygga LLM-baserade applikationer.
Det ger dig:

- **Abstraktioner** som förenklar komplex agent-logik
- **Integrationer** med 100+ datakällor och verktyg
- **Battle-tested patterns** som fungerar i produktion
- **Community** med tusentals utvecklare

Men LangChain har också kritik: det kan vara "over-engineered" för enkla use cases.
Denna modul lär dig använda LangChain effektivt och veta när det är rätt val.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Bygga agenter med LangChain's agent frameworks
- ✅ Implementera custom tools och chains
- ✅ Använda LangChain Expression Language (LCEL)
- ✅ Integrera med externa data via retrievers
- ✅ Debugga och optimera LangChain-applikationer

## Kärnkoncept

### LangChain Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     LANGCHAIN ARCHITECTURE                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                        LANGCHAIN CORE                                 │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐ │   │
│  │  │   Models    │ │   Prompts   │ │  Retrievers │ │    Runnables    │ │   │
│  │  │  (LLMs,     │ │  (Templates,│ │  (Vector,   │ │    (LCEL)       │ │   │
│  │  │   Chat)     │ │   Few-shot) │ │   BM25)     │ │                 │ │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                       LANGCHAIN AGENTS                               │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐ │   │
│  │  │   Tools     │ │   Agents    │ │   Memory    │ │   Callbacks     │ │   │
│  │  │  (Built-in, │ │  (ReAct,    │ │  (Buffer,   │ │   (Logging,     │ │   │
│  │  │   Custom)   │ │   OpenAI)   │ │   Summary)  │ │    Streaming)   │ │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                      INTEGRATIONS                                     │   │
│  │  OpenAI  │  Anthropic  │  Pinecone  │  Postgres  │  Slack  │  ...   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### LCEL (LangChain Expression Language)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            LCEL BASICS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LCEL = Pipe Operator för LangChain                                        │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  chain = prompt | model | output_parser                              │   │
│  │          ─────┬─   ───┬──   ─────┬────────                           │   │
│  │               │       │          │                                    │   │
│  │          Format      Call      Parse                                 │   │
│  │          input       LLM       output                                │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LCEL Fördelar:                                                             │
│  • Streaming out-of-the-box                                                 │
│  • Async support inbyggd                                                    │
│  • Batch processing                                                         │
│  • Automatic retry/fallback                                                 │
│                                                                              │
│  LCEL Komponenter:                                                          │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐   │
│  │ RunnableSeq   │ │ RunnablePara  │ │ RunnableBranch│ │ RunnableLambda│   │
│  │ (chain)       │ │ (parallel)    │ │ (if/else)     │ │ (custom func) │   │
│  └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: LangChain Agent

### 1. Basic LCEL Chain

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful DevOps assistant."),
    ("human", "{question}")
])

# Build chain with LCEL
chain = prompt | model | StrOutputParser()

# Run chain
response = chain.invoke({"question": "Vad är Kubernetes?"})
print(response)

# Stream response
for chunk in chain.stream({"question": "Förklara Docker containers"}):
    print(chunk, end="", flush=True)

# Batch process
questions = [
    {"question": "Vad är CI/CD?"},
    {"question": "Förklara GitOps"},
    {"question": "Vad är Infrastructure as Code?"}
]
responses = chain.batch(questions)
```

### 2. Custom Tools

```python
from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field
from typing import Optional

# Simple decorator-based tool
@tool
def search_documentation(query: str) -> str:
    \"\"\"Search the internal documentation for relevant information.

    Use this when the user asks about company-specific processes,
    internal tools, or policies.

    Args:
        query: The search term or question

    Returns:
        Relevant documentation snippets
    \"\"\"
    # Mock implementation
    docs = {
        "deployment": "Deploy using: kubectl apply -f deployment.yaml",
        "monitoring": "Use Grafana dashboards at grafana.internal.com",
        "incidents": "Follow runbook at wiki.internal.com/incidents"
    }

    for key, value in docs.items():
        if key in query.lower():
            return value

    return "No documentation found for: " + query


# Structured tool with Pydantic
class DeploymentParams(BaseModel):
    service_name: str = Field(description="Name of the service to deploy")
    environment: str = Field(description="Target environment: dev, staging, prod")
    version: Optional[str] = Field(default="latest", description="Version to deploy")

@tool(args_schema=DeploymentParams)
def deploy_service(service_name: str, environment: str, version: str = "latest") -> str:
    \"\"\"Deploy a service to a specified environment.

    ⚠️ This triggers an actual deployment! Use with caution.

    Args:
        service_name: The service to deploy
        environment: Target environment
        version: Service version (default: latest)

    Returns:
        Deployment status and URL
    \"\"\"
    # Validate environment
    if environment == "prod" and version == "latest":
        return "Error: Cannot deploy 'latest' to production. Specify a version."

    # Mock deployment
    return f\"\"\"
    ✅ Deployment initiated:
    - Service: {service_name}
    - Environment: {environment}
    - Version: {version}
    - Status: Rolling out (3/5 replicas ready)
    - URL: https://{service_name}.{environment}.example.com
    \"\"\"

# Dynamic tool creation
def create_api_tool(api_name: str, base_url: str):
    \"\"\"Factory for creating API tools.\"\"\"

    @tool(name=f"call_{api_name}_api")
    def api_tool(endpoint: str, method: str = "GET") -> str:
        f\"\"\"Call the {api_name} API.

        Args:
            endpoint: API endpoint path
            method: HTTP method (GET, POST, etc.)
        \"\"\"
        # Implementation here
        return f"Called {base_url}/{endpoint}"

    return api_tool

# Create multiple API tools
github_tool = create_api_tool("github", "https://api.github.com")
jira_tool = create_api_tool("jira", "https://jira.company.com/api")
```

### 3. Building an Agent

```python
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Define tools
tools = [search_documentation, deploy_service]

# Create prompt with agent scratchpad
prompt = ChatPromptTemplate.from_messages([
    ("system", \"\"\"You are a DevOps assistant that helps with deployments,
    monitoring, and troubleshooting.

    Always:
    1. Search documentation first before taking actions
    2. Confirm with the user before deploying to production
    3. Explain what you're doing and why
    \"\"\"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create agent
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_openai_tools_agent(model, tools, prompt)

# Create executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # Show reasoning
    max_iterations=10,
    handle_parsing_errors=True
)

# Run agent
result = agent_executor.invoke({
    "input": "Deploy the auth-service to staging"
})
print(result["output"])
```

### 4. Advanced: Agent with Memory

```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Create memory store
message_histories = {}

def get_session_history(session_id: str):
    if session_id not in message_histories:
        message_histories[session_id] = ChatMessageHistory()
    return message_histories[session_id]

# Wrap agent with memory
agent_with_memory = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

# Use with session
config = {"configurable": {"session_id": "user_123"}}

# First message
result1 = agent_with_memory.invoke(
    {"input": "Jag vill deploya auth-service"},
    config=config
)

# Follow-up (has context from first message)
result2 = agent_with_memory.invoke(
    {"input": "Gör det till staging istället"},
    config=config
)
```

### 5. RAG with Retrievers

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Create documents
docs = [
    Document(page_content="Kubernetes pods should have resource limits defined.",
             metadata={"source": "k8s-best-practices.md"}),
    Document(page_content="Use Helm charts for reproducible deployments.",
             metadata={"source": "deployment-guide.md"}),
    Document(page_content="Monitor CPU and memory with Prometheus metrics.",
             metadata={"source": "monitoring-setup.md"})
]

# Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Create RAG chain
prompt = ChatPromptTemplate.from_template(\"\"\"
Answer based on the following context:

{context}

Question: {input}
\"\"\")

document_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Use RAG
response = retrieval_chain.invoke({
    "input": "How should I set up monitoring?"
})
print(response["answer"])
```

## Vanliga problem

### Problem 1: "Agent loopar oändligt"

```python
# Lösning: Begränsa iterations och lägg till early stopping
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=5,  # Max 5 tool calls
    max_execution_time=30,  # Max 30 seconds
    early_stopping_method="force"  # Force stop after max
)
```

### Problem 2: "Token limit exceeded"

```python
# Lösning: Använd ConversationSummaryMemory
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(
    llm=ChatOpenAI(model="gpt-4o-mini"),
    max_token_limit=1000
)
```

### Problem 3: "Svårt att debugga"

```python
from langchain.callbacks import LangChainTracer
from langsmith import Client

# Enable LangSmith tracing
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "my-project"

# Or use custom callback
from langchain_core.callbacks import BaseCallbackHandler

class DebugCallback(BaseCallbackHandler):
    def on_tool_start(self, tool, input_str, **kwargs):
        print(f"🔧 Tool: {tool.name} | Input: {input_str}")

    def on_tool_end(self, output, **kwargs):
        print(f"✅ Output: {output[:100]}...")

agent_executor.invoke(
    {"input": "Deploy auth-service"},
    config={"callbacks": [DebugCallback()]}
)
```

## Praktisk övning

**Uppgift:** Bygg en LangChain DevOps Agent

```python
\"\"\"
TODO: Bygg en komplett DevOps agent med:

1. Tools:
   - check_service_status(service_name) -> health check
   - get_logs(service_name, lines=100) -> recent logs
   - restart_service(service_name) -> restart
   - scale_service(service_name, replicas) -> scale up/down

2. Memory:
   - Kom ihåg tidigare kommandon i sessionen
   - Summera långa konversationer

3. RAG:
   - Ladda runbooks från Markdown-filer
   - Sök relevant dokumentation vid troubleshooting

4. Guardrails:
   - Kräv bekräftelse för destructive operations
   - Logga alla actions till audit trail
\"\"\"

class DevOpsAgent:
    def __init__(self):
        # Din kod här
        pass

    def chat(self, message: str, session_id: str) -> str:
        # Din kod här
        pass

# Test
agent = DevOpsAgent()
print(agent.chat("Varför är auth-service långsam?", "session_1"))
print(agent.chat("Kan du starta om den?", "session_1"))
```

## Sammanfattning

- ✅ **LCEL** är det moderna sättet att bygga chains
- ✅ **@tool decorator** för enkla verktyg
- ✅ **Pydantic schemas** för validering
- ✅ **AgentExecutor** orkestrerar agent + tools
- ✅ **Memory** via RunnableWithMessageHistory

## Nästa steg

- **Node 12:** LlamaIndex & AutoGen
- **Node 13:** Memory Systems — Short & Long-term

---
*Pro tip: Börja enkelt! Använd inte LangChain om en enkel prompt räcker.*
"""
    },
    {
        "id": "ai-agents-12",
        "slug": "llamaindex-autogen",
        "title": "LlamaIndex & AutoGen Frameworks",
        "order_index": 12,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "concept",
        "prerequisites": ["ai-agents-11"],
        "content": """# LlamaIndex & AutoGen Frameworks

## Varför detta är viktigt

Medan LangChain dominerar, finns det specialiserade frameworks som är bättre
för specifika use cases:

- **LlamaIndex** — Optimerat för RAG och knowledge management
- **AutoGen** — Microsoft's framework för multi-agent conversations
- **CrewAI** — Role-based multi-agent orchestration

Att känna till alternativen hjälper dig välja rätt verktyg för jobbet.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Använda LlamaIndex för avancerad RAG
- ✅ Bygga multi-agent systems med AutoGen
- ✅ Jämföra frameworks och välja rätt för ditt use case
- ✅ Kombinera frameworks för komplexa system

## LlamaIndex Deep Dive

### LlamaIndex Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LLAMAINDEX ARCHITECTURE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         DATA LAYER                                    │   │
│  │  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐          │   │
│  │  │  PDF     │   │  Notion  │   │  Slack   │   │  Code    │          │   │
│  │  │  Reader  │   │  Reader  │   │  Reader  │   │  Reader  │          │   │
│  │  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘          │   │
│  │       └──────────────┴──────────────┴──────────────┘                 │   │
│  │                              │                                        │   │
│  │                       ┌──────▼──────┐                                │   │
│  │                       │   Document   │                                │   │
│  │                       │   Chunking   │                                │   │
│  │                       └──────┬──────┘                                │   │
│  └──────────────────────────────┼───────────────────────────────────────┘   │
│                                 │                                            │
│  ┌──────────────────────────────▼───────────────────────────────────────┐   │
│  │                        INDEX LAYER                                    │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │   │
│  │  │  VectorStore │  │   Summary    │  │  Knowledge   │                │   │
│  │  │    Index     │  │    Index     │  │    Graph     │                │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘                │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                            │
│  ┌──────────────────────────────▼───────────────────────────────────────┐   │
│  │                       QUERY LAYER                                     │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                   │   │
│  │  │  Retriever  │  │   Router    │  │   Agent     │                   │   │
│  │  │  (Top-K)    │  │  (Multi-    │  │   Query     │                   │   │
│  │  │             │  │   Index)    │  │   Engine    │                   │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### LlamaIndex: Advanced RAG

```python
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    StorageContext
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Configure global settings
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=200)

# Load documents
documents = SimpleDirectoryReader("./docs/runbooks").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine(
    similarity_top_k=5,
    response_mode="compact"  # Summarize results
)

response = query_engine.query("How do I troubleshoot high CPU usage?")
print(response.response)
print(f"Sources: {[n.node.metadata for n in response.source_nodes]}")
```

### LlamaIndex: Router for Multiple Indexes

```python
from llama_index.core import SummaryIndex
from llama_index.core.query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector
from llama_index.core.tools import QueryEngineTool

# Create different index types
vector_index = VectorStoreIndex.from_documents(runbook_docs)
summary_index = SummaryIndex.from_documents(policy_docs)

# Create query engines
vector_engine = vector_index.as_query_engine()
summary_engine = summary_index.as_query_engine()

# Create tools with descriptions
tools = [
    QueryEngineTool.from_defaults(
        query_engine=vector_engine,
        description="Use for specific technical questions about runbooks and procedures"
    ),
    QueryEngineTool.from_defaults(
        query_engine=summary_engine,
        description="Use for policy questions that need comprehensive overview"
    )
]

# Router automatically picks the right index
router_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=tools
)

# Routing happens automatically
response = router_engine.query("What's our incident response policy?")
```

### LlamaIndex: Agentic RAG

```python
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool

# Custom tool
def get_server_metrics(hostname: str) -> dict:
    \"\"\"Get current CPU/memory metrics for a server.\"\"\"
    # Mock implementation
    return {"cpu": 75.5, "memory": 82.3, "disk": 45.0}

# Create agent with RAG + custom tools
agent = ReActAgent.from_tools(
    tools=[
        QueryEngineTool.from_defaults(
            query_engine=query_engine,
            name="search_docs",
            description="Search technical documentation"
        ),
        FunctionTool.from_defaults(
            fn=get_server_metrics,
            name="get_metrics",
            description="Get server metrics by hostname"
        )
    ],
    llm=Settings.llm,
    verbose=True
)

# Agent can combine RAG + tools
response = agent.chat(
    "Server prod-web-01 has high CPU. Check the metrics and find relevant troubleshooting docs."
)
```

## AutoGen: Multi-Agent Systems

### AutoGen Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AUTOGEN ARCHITECTURE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                    CONVERSATION PATTERNS                              │   │
│  │                                                                       │   │
│  │   Two-Agent        Group Chat           Hierarchical                 │   │
│  │   ┌───┐ ┌───┐      ┌───┐               ┌─────────────┐              │   │
│  │   │ A │◄►│ B │      │ A │◄──┐           │  Manager    │              │   │
│  │   └───┘ └───┘      └───┘   │           └──────┬──────┘              │   │
│  │                       ▲    │                  │                      │   │
│  │                       │    ▼           ┌──────┼──────┐              │   │
│  │                    ┌──┴──┐ │           ▼      ▼      ▼              │   │
│  │                    │  B  │◄┤        ┌───┐  ┌───┐  ┌───┐            │   │
│  │                    └─────┘ │        │ A │  │ B │  │ C │            │   │
│  │                       ▲    │        └───┘  └───┘  └───┘            │   │
│  │                       │    ▼                                        │   │
│  │                    ┌──┴──┐ │                                        │   │
│  │                    │  C  │◄┘                                        │   │
│  │                    └─────┘                                          │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Agent Types:                                                                │
│  ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐         │
│  │ ConversableAgent  │ │ AssistantAgent    │ │ UserProxyAgent    │         │
│  │ (Base class)      │ │ (LLM-powered)     │ │ (Human/Code exec) │         │
│  └───────────────────┘ └───────────────────┘ └───────────────────┘         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### AutoGen: Basic Two-Agent Chat

```python
from autogen import AssistantAgent, UserProxyAgent

# Create an AI assistant
assistant = AssistantAgent(
    name="DevOps_Expert",
    system_message=\"\"\"You are a DevOps expert.
    You help with infrastructure, CI/CD, and Kubernetes questions.
    Always provide practical, actionable advice.
    \"\"\",
    llm_config={"model": "gpt-4o-mini"}
)

# Create a user proxy (represents the human)
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # Or "ALWAYS" for interactive
    max_consecutive_auto_reply=5,
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Write a Kubernetes deployment for a Python Flask app."
)
```

### AutoGen: Group Chat

```python
from autogen import GroupChat, GroupChatManager

# Create specialized agents
architect = AssistantAgent(
    name="Architect",
    system_message="You design system architecture. Focus on scalability and reliability.",
    llm_config={"model": "gpt-4o-mini"}
)

developer = AssistantAgent(
    name="Developer",
    system_message="You write clean, tested code. Implement the architect's designs.",
    llm_config={"model": "gpt-4o-mini"}
)

reviewer = AssistantAgent(
    name="Reviewer",
    system_message="You review code for bugs, security issues, and best practices.",
    llm_config={"model": "gpt-4o-mini"}
)

# Create group chat
group_chat = GroupChat(
    agents=[architect, developer, reviewer],
    messages=[],
    max_round=10,
    speaker_selection_method="auto"  # LLM decides who speaks next
)

# Manager orchestrates the conversation
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"model": "gpt-4o-mini"}
)

# Start group conversation
architect.initiate_chat(
    manager,
    message="Design and implement a rate limiting service for our API gateway."
)
```

### AutoGen: Code Execution

```python
from autogen import AssistantAgent, UserProxyAgent

# Coder agent
coder = AssistantAgent(
    name="Coder",
    system_message=\"\"\"You write Python code.
    When asked to solve a problem, write complete, runnable code.
    Use code blocks with ```python and ```.
    \"\"\",
    llm_config={"model": "gpt-4o-mini"}
)

# Executor with code execution
executor = UserProxyAgent(
    name="Executor",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "workspace",
        "use_docker": True,  # Safer!
        "timeout": 60
    },
    is_termination_msg=lambda msg: "DONE" in msg.get("content", "").upper()
)

# The executor will run code that the coder writes
executor.initiate_chat(
    coder,
    message=\"\"\"
    Write a Python script that:
    1. Fetches the top 5 Hacker News stories
    2. Extracts titles and URLs
    3. Prints them formatted nicely

    Say DONE when the code works.
    \"\"\"
)
```

## Framework Comparison

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     FRAMEWORK COMPARISON                                     │
├────────────────┬─────────────────┬─────────────────┬────────────────────────┤
│                │   LangChain     │   LlamaIndex    │      AutoGen          │
├────────────────┼─────────────────┼─────────────────┼────────────────────────┤
│ Best For       │ General agents  │ RAG/Knowledge   │ Multi-agent systems   │
│                │ & integrations  │ management      │ & code generation     │
├────────────────┼─────────────────┼─────────────────┼────────────────────────┤
│ Complexity     │ High            │ Medium          │ Medium                │
├────────────────┼─────────────────┼─────────────────┼────────────────────────┤
│ Learning Curve │ Steep           │ Moderate        │ Moderate              │
├────────────────┼─────────────────┼─────────────────┼────────────────────────┤
│ Integrations   │ 100+            │ 40+             │ 10+                   │
├────────────────┼─────────────────┼─────────────────┼────────────────────────┤
│ Production     │ ⭐⭐⭐⭐⭐     │ ⭐⭐⭐⭐        │ ⭐⭐⭐               │
│ Ready          │                 │                 │ (Still maturing)      │
├────────────────┼─────────────────┼─────────────────┼────────────────────────┤
│ Use When       │ Need many       │ Heavy document  │ Agents need to        │
│                │ integrations    │ processing/RAG  │ collaborate           │
└────────────────┴─────────────────┴─────────────────┴────────────────────────┘
```

## Hybrid Approach: Combining Frameworks

```python
# Use LlamaIndex for RAG, LangChain for agent orchestration
from llama_index.core import VectorStoreIndex
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.tools import tool

# LlamaIndex for knowledge base
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Wrap as LangChain tool
@tool
def search_knowledge_base(query: str) -> str:
    \"\"\"Search the internal knowledge base for information.\"\"\"
    response = query_engine.query(query)
    return str(response)

# Use in LangChain agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

tools = [search_knowledge_base]
model = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a knowledge base."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

agent = create_openai_tools_agent(model, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)

# Best of both worlds!
response = executor.invoke({"input": "How do I set up monitoring?"})
```

## Praktisk övning

**Uppgift:** Bygg ett Multi-Agent DevOps Team

```python
\"\"\"
TODO: Skapa ett team av specialiserade agenter:

1. Incident Commander
   - Tar emot incident alerts
   - Koordinerar response
   - Bestämmer vem som ska agera

2. Diagnostics Agent
   - Kollar metrics och logs
   - Identifierar root cause
   - Använder RAG för runbooks

3. Remediation Agent
   - Föreslår och utför fixes
   - Kör scripts/commands
   - Verifierar att fix fungerade

4. Communication Agent
   - Skriver status updates
   - Notifierar stakeholders
   - Dokumenterar incident

Scenarios att testa:
- "API latency spiked to 5s"
- "Database connection pool exhausted"
- "Kubernetes pod CrashLoopBackOff"
\"\"\"

from autogen import GroupChat, GroupChatManager

class IncidentResponseTeam:
    def __init__(self):
        # Skapa dina agenter här
        pass

    def handle_incident(self, alert: str) -> dict:
        # Din kod här
        pass

# Test
team = IncidentResponseTeam()
result = team.handle_incident("Alert: API latency > 5s on prod-web cluster")
```

## Sammanfattning

- ✅ **LlamaIndex** för document-heavy RAG applications
- ✅ **AutoGen** för multi-agent collaboration
- ✅ **LangChain** för general-purpose med många integrations
- ✅ **Hybrid** — kombinera frameworks för best of both worlds

## Nästa steg

- **Node 13:** Memory Systems — Short & Long-term
- **Node 14:** State Management

---
*Pro tip: Välj framework baserat på ditt primära use case, inte popularitet!*
"""
    }
]
