"""
AI Agents SkillsMap - Block 07: Memory & State
Nodes 13-14: Memory Systems, State Management
"""

BLOCK_07_NODES = [
    {
        "id": "ai-agents-13",
        "slug": "agent-memory-systems",
        "title": "Agent Memory Systems",
        "order_index": 13,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "concept",
        "prerequisites": ["ai-agents-12"],
        "content": """# Agent Memory Systems

## Varför detta är viktigt

Agenter utan minne är som att prata med någon som har total amnesi — varje
meddelande börjar från noll. Memory systems är kritiska för:

- **Kontext** — Agent minns vad ni pratade om
- **Personalisering** — Agent lär sig användarens preferenser
- **Effektivitet** — Undvik att upprepa samma frågor
- **Long-term learning** — Agent blir bättre över tid

Men minne kostar: tokens, latency, och komplexitet. Denna modul lär dig
designa minnessystem som balanserar dessa tradeoffs.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Implementera short-term conversation memory
- ✅ Bygga long-term semantic memory med embeddings
- ✅ Designa memory retrieval strategies
- ✅ Hantera memory i multi-turn conversations
- ✅ Optimera memory för tokens och latency

## Kärnkoncept

### Memory Types

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MEMORY TYPES                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. CONVERSATION MEMORY (Short-term)                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  User: Vad är mitt ordernummer?                                      │   │
│  │  Agent: Ditt ordernummer är ORD-12345                               │   │
│  │  User: När levereras den?        ◄── "den" refererar till ordern    │   │
│  │  Agent: Beräknad leverans är 15 mars                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  Scope: Nuvarande konversation                                              │
│  Retention: Session-based                                                   │
│  Storage: In-memory / Redis                                                 │
│                                                                              │
│  2. ENTITY MEMORY (Medium-term)                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Entities extracted from conversation:                               │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ user_123:                                                      │  │   │
│  │  │   name: "Maria"                                               │  │   │
│  │  │   preferred_language: "svenska"                               │  │   │
│  │  │   recent_orders: ["ORD-12345", "ORD-12340"]                   │  │   │
│  │  │   interests: ["tech", "devops"]                               │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  Scope: Per user/entity                                                     │
│  Retention: Days to weeks                                                   │
│  Storage: Database                                                          │
│                                                                              │
│  3. SEMANTIC MEMORY (Long-term)                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Vector store with embeddings:                                       │   │
│  │  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   │   │
│  │  │ "Maria gillar   │   │ "Användaren hade│   │ "Senast fixade  │   │   │
│  │  │  kubernetes"    │   │  problem med    │   │  vi DNS-issue   │   │   │
│  │  │  [0.23, 0.87...]│   │  deployment"    │   │  för Maria"     │   │   │
│  │  └─────────────────┘   │  [0.45, 0.12...]│   │  [0.67, 0.34...]│   │   │
│  │                        └─────────────────┘   └─────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  Scope: Cross-session, cross-user learnings                                │
│  Retention: Permanent                                                       │
│  Storage: Vector database (Pinecone, Weaviate)                             │
│                                                                              │
│  4. PROCEDURAL MEMORY (Skills)                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Learned procedures:                                                 │   │
│  │  - "To restart service X: kubectl rollout restart deployment/X"     │   │
│  │  - "When user asks about billing: check stripe_customer_id first"  │   │
│  │  - "For Maria: always respond in Swedish"                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  Scope: Agent capabilities                                                  │
│  Retention: Until updated                                                   │
│  Storage: Database / RAG                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera Memory Systems

### 1. Conversation Memory (Buffer)

```python
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Message:
    role: str  # "user", "assistant", "system"
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict = field(default_factory=dict)

class ConversationMemory:
    \"\"\"Simple buffer memory for conversation history.\"\"\"

    def __init__(self, max_messages: int = 20):
        self.messages: list[Message] = []
        self.max_messages = max_messages

    def add(self, role: str, content: str, **metadata):
        message = Message(role=role, content=content, metadata=metadata)
        self.messages.append(message)

        # Trim if too long
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_context(self) -> list[dict]:
        \"\"\"Get messages in format for LLM.\"\"\"
        return [
            {"role": m.role, "content": m.content}
            for m in self.messages
        ]

    def clear(self):
        self.messages = []

# Usage
memory = ConversationMemory(max_messages=10)
memory.add("user", "Vad är mitt ordernummer?")
memory.add("assistant", "Ditt ordernummer är ORD-12345")
memory.add("user", "När levereras den?")

# Pass to LLM
messages = memory.get_context()
```

### 2. Token-Aware Memory

```python
import tiktoken

class TokenAwareMemory:
    \"\"\"Memory that respects token limits.\"\"\"

    def __init__(self, max_tokens: int = 4000, model: str = "gpt-4"):
        self.max_tokens = max_tokens
        self.encoder = tiktoken.encoding_for_model(model)
        self.messages: list[Message] = []

    def count_tokens(self, text: str) -> int:
        return len(self.encoder.encode(text))

    def add(self, role: str, content: str, **metadata):
        message = Message(role=role, content=content, metadata=metadata)
        self.messages.append(message)
        self._trim_to_fit()

    def _trim_to_fit(self):
        \"\"\"Remove oldest messages until we fit in token limit.\"\"\"
        while self._total_tokens() > self.max_tokens and len(self.messages) > 1:
            # Keep at least the last message
            self.messages.pop(0)

    def _total_tokens(self) -> int:
        return sum(self.count_tokens(m.content) for m in self.messages)

    def get_context(self) -> list[dict]:
        return [{"role": m.role, "content": m.content} for m in self.messages]

    @property
    def token_usage(self) -> dict:
        return {
            "current": self._total_tokens(),
            "max": self.max_tokens,
            "messages": len(self.messages)
        }

# Usage
memory = TokenAwareMemory(max_tokens=2000)
memory.add("user", "Berätta allt om Kubernetes...")
print(memory.token_usage)
```

### 3. Summary Memory

```python
from openai import OpenAI

class SummaryMemory:
    \"\"\"Memory that summarizes old conversations to save tokens.\"\"\"

    def __init__(self,
                 max_recent: int = 5,
                 summarize_threshold: int = 10):
        self.client = OpenAI()
        self.max_recent = max_recent
        self.summarize_threshold = summarize_threshold
        self.summary: str = ""
        self.recent_messages: list[Message] = []

    def add(self, role: str, content: str):
        self.recent_messages.append(Message(role=role, content=content))

        # Summarize when we have too many messages
        if len(self.recent_messages) > self.summarize_threshold:
            self._compress()

    def _compress(self):
        \"\"\"Summarize old messages and keep only recent ones.\"\"\"
        messages_to_summarize = self.recent_messages[:-self.max_recent]

        # Generate summary
        conversation = "\\n".join([
            f"{m.role}: {m.content}" for m in messages_to_summarize
        ])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize this conversation concisely, keeping key facts and decisions:"},
                {"role": "user", "content": conversation}
            ],
            max_tokens=200
        )

        new_summary = response.choices[0].message.content

        # Combine with existing summary
        if self.summary:
            self.summary = f"Previous: {self.summary}\\nRecent: {new_summary}"
        else:
            self.summary = new_summary

        # Keep only recent messages
        self.recent_messages = self.recent_messages[-self.max_recent:]

    def get_context(self) -> list[dict]:
        context = []

        # Add summary as system context
        if self.summary:
            context.append({
                "role": "system",
                "content": f"Summary of earlier conversation: {self.summary}"
            })

        # Add recent messages
        for m in self.recent_messages:
            context.append({"role": m.role, "content": m.content})

        return context
```

### 4. Semantic Memory (Vector Store)

```python
from openai import OpenAI
import numpy as np
from dataclasses import dataclass
from typing import Optional
import json

@dataclass
class MemoryEntry:
    id: str
    content: str
    embedding: list[float]
    metadata: dict
    created_at: datetime = field(default_factory=datetime.now)

class SemanticMemory:
    \"\"\"Long-term memory using embeddings.\"\"\"

    def __init__(self, user_id: str):
        self.client = OpenAI()
        self.user_id = user_id
        self.memories: list[MemoryEntry] = []

    def _embed(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    def _cosine_similarity(self, a: list[float], b: list[float]) -> float:
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def store(self, content: str, **metadata):
        \"\"\"Store a memory with embedding.\"\"\"
        embedding = self._embed(content)

        entry = MemoryEntry(
            id=f"mem_{len(self.memories)}",
            content=content,
            embedding=embedding,
            metadata={"user_id": self.user_id, **metadata}
        )

        self.memories.append(entry)
        return entry.id

    def search(self, query: str, top_k: int = 3, threshold: float = 0.7) -> list[MemoryEntry]:
        \"\"\"Search memories by semantic similarity.\"\"\"
        if not self.memories:
            return []

        query_embedding = self._embed(query)

        # Score all memories
        scored = []
        for memory in self.memories:
            score = self._cosine_similarity(query_embedding, memory.embedding)
            if score >= threshold:
                scored.append((memory, score))

        # Sort by score and return top_k
        scored.sort(key=lambda x: x[1], reverse=True)
        return [m for m, s in scored[:top_k]]

    def forget(self, memory_id: str):
        \"\"\"Remove a specific memory.\"\"\"
        self.memories = [m for m in self.memories if m.id != memory_id]

# Usage
semantic_mem = SemanticMemory(user_id="user_123")

# Store interactions
semantic_mem.store(
    "User had issues with Kubernetes deployments failing",
    category="technical_issue",
    resolved=True
)
semantic_mem.store(
    "User prefers Swedish responses",
    category="preference"
)

# Recall relevant memories
relevant = semantic_mem.search("deployment problem")
for mem in relevant:
    print(f"Memory: {mem.content}")
```

### 5. Complete Memory Manager

```python
class MemoryManager:
    \"\"\"Unified memory manager combining all memory types.\"\"\"

    def __init__(self, user_id: str):
        self.user_id = user_id

        # Different memory types
        self.conversation = TokenAwareMemory(max_tokens=3000)
        self.semantic = SemanticMemory(user_id)
        self.entity = {}  # Simple dict for entity memory

    def add_message(self, role: str, content: str):
        \"\"\"Add message to conversation memory.\"\"\"
        self.conversation.add(role, content)

        # Extract and store important info in semantic memory
        if role == "assistant":
            # Store significant assistant responses
            if len(content) > 100:
                self.semantic.store(
                    content[:500],  # First 500 chars
                    type="response"
                )

    def update_entity(self, key: str, value: any):
        \"\"\"Update entity memory.\"\"\"
        self.entity[key] = {
            "value": value,
            "updated_at": datetime.now().isoformat()
        }

    def get_context(self, query: Optional[str] = None) -> list[dict]:
        \"\"\"Get full context for LLM.\"\"\"
        context = []

        # Add entity context
        if self.entity:
            entity_str = json.dumps(self.entity, indent=2)
            context.append({
                "role": "system",
                "content": f"User context: {entity_str}"
            })

        # Add relevant semantic memories
        if query:
            memories = self.semantic.search(query, top_k=2)
            if memories:
                mem_str = "\\n".join([m.content for m in memories])
                context.append({
                    "role": "system",
                    "content": f"Relevant past context: {mem_str}"
                })

        # Add conversation history
        context.extend(self.conversation.get_context())

        return context

# Usage
memory = MemoryManager(user_id="user_123")

# Update entity info
memory.update_entity("name", "Maria")
memory.update_entity("preferred_language", "svenska")

# Add conversation
memory.add_message("user", "Jag har problem med min deployment")
memory.add_message("assistant", "Jag kan hjälpa dig med deployment-problemet...")

# Get context for next LLM call
context = memory.get_context(query="deployment issues")
```

## Vanliga problem

### Problem 1: "Agenten glömmer viktig info"

```python
# Lösning: Explicit memory extraction
def extract_important_info(message: str) -> list[str]:
    \"\"\"Extract facts worth remembering.\"\"\"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": \"\"\"
            Extract important facts from this message that should be remembered.
            Return as JSON array of strings.
            Only include facts, not opinions or small talk.
            \"\"\"},
            {"role": "user", "content": message}
        ]
    )
    return json.loads(response.choices[0].message.content)
```

### Problem 2: "För många irrelevanta minnen"

```python
# Lösning: Time-decay och relevance scoring
def relevance_score(memory: MemoryEntry, query: str) -> float:
    # Semantic similarity
    similarity = cosine_similarity(query_embed, memory.embedding)

    # Time decay (older = less relevant)
    age_days = (datetime.now() - memory.created_at).days
    time_factor = 1.0 / (1.0 + age_days * 0.1)

    # Access frequency bonus
    access_factor = 1.0 + memory.metadata.get("access_count", 0) * 0.05

    return similarity * time_factor * access_factor
```

## Praktisk övning

**Uppgift:** Bygg ett Personalized Agent Memory System

```python
\"\"\"
TODO: Bygg ett memory system som lär sig användarens preferenser.

Features:
1. Conversation memory med summarization
2. Entity extraction (namn, preferenser, tidigare ärenden)
3. Semantic memory för långsiktigt lärande
4. Memory decay för att glömma irrelevant info

Test scenarios:
- Agent ska minnas användarens namn efter första introduktionen
- Agent ska anpassa svar baserat på tidigare interaktioner
- Agent ska kunna svara på "vad pratade vi om förra gången?"
\"\"\"

class PersonalizedMemory:
    def __init__(self, user_id: str):
        # Din kod här
        pass

    def process_interaction(self, user_message: str, assistant_response: str):
        # Din kod här
        pass

    def get_personalized_context(self, current_query: str) -> list[dict]:
        # Din kod här
        pass

# Test
memory = PersonalizedMemory("user_123")
memory.process_interaction(
    "Hej, jag heter Maria och jag jobbar med DevOps",
    "Hej Maria! Vad kan jag hjälpa dig med idag?"
)
# Senare...
context = memory.get_personalized_context("Kan du hjälpa mig?")
# Ska innehålla: namn=Maria, yrke=DevOps
```

## Sammanfattning

- ✅ **Conversation memory** för session context
- ✅ **Token-aware** trimming för att hålla sig under gränser
- ✅ **Summary memory** komprimerar långa konversationer
- ✅ **Semantic memory** för long-term recall
- ✅ **Memory manager** kombinerar alla typer

## Nästa steg

- **Node 14:** State Management
- **Node 15:** Multi-Agent Systems

---
*Pro tip: Börja enkelt med buffer memory, lägg till semantisk memory när du behöver det!*
"""
    },
    {
        "id": "ai-agents-14",
        "slug": "agent-state-management",
        "title": "Agent State Management",
        "order_index": 14,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["ai-agents-13"],
        "content": """# Agent State Management

## Varför detta är viktigt

Medan memory handlar om vad agenten minns, handlar state om var agenten är
i sin exekvering. State management är kritiskt för:

- **Multi-step tasks** — Håll koll på progress
- **Error recovery** — Återuppta från fel
- **Debugging** — Förstå vad som hände
- **Concurrency** — Hantera parallella requests

Dålig state management leder till inkonsistenta beteenden och svåra buggar.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Designa state machines för agent workflows
- ✅ Implementera checkpoint/resume för long-running tasks
- ✅ Hantera concurrent requests safely
- ✅ Debugga state-related issues
- ✅ Bygga resilient agents som hanterar failures

## Kärnkoncept

### State Machine Basics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT STATE MACHINE                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────┐     User        ┌──────────────┐                              │
│   │  IDLE   │────message────►│   THINKING   │                              │
│   └─────────┘                 └──────┬───────┘                              │
│        ▲                             │                                       │
│        │                    Need     │ Has answer                           │
│        │                    tool?────┤                                       │
│        │                      │      ▼                                       │
│        │               ┌──────▼─────────────┐                               │
│        │               │  EXECUTING_TOOL    │                               │
│        │               └──────────┬─────────┘                               │
│        │                          │                                          │
│        │                   Tool   │                                          │
│        │                   done───┤                                          │
│        │                          ▼                                          │
│        │               ┌────────────────────┐                               │
│        │◄──────────────│    RESPONDING      │                               │
│        │    Response   └────────────────────┘                               │
│        │    sent                                                             │
│        │                                                                     │
│        │               ┌────────────────────┐                               │
│        └───Timeout────►│      ERROR         │                               │
│                        └────────────────────┘                               │
│                                                                              │
│   States:                                                                    │
│   • IDLE - Waiting for input                                                │
│   • THINKING - Processing user message                                      │
│   • EXECUTING_TOOL - Running a tool                                         │
│   • RESPONDING - Generating response                                        │
│   • ERROR - Handling failure                                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Workflow State

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WORKFLOW STATE EXAMPLE                                    │
│                    (Deploy Service Workflow)                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ {                                                                     │   │
│  │   "workflow_id": "deploy_abc123",                                    │   │
│  │   "status": "IN_PROGRESS",                                           │   │
│  │   "current_step": 3,                                                 │   │
│  │   "steps": [                                                         │   │
│  │     {"name": "validate_config", "status": "COMPLETED", "result": {}},│   │
│  │     {"name": "build_image", "status": "COMPLETED", "result": {...}}, │   │
│  │     {"name": "push_registry", "status": "IN_PROGRESS"},              │   │
│  │     {"name": "deploy_k8s", "status": "PENDING"},                     │   │
│  │     {"name": "health_check", "status": "PENDING"}                    │   │
│  │   ],                                                                 │   │
│  │   "context": {                                                       │   │
│  │     "service_name": "auth-service",                                  │   │
│  │     "target_env": "staging",                                         │   │
│  │     "image_tag": "v1.2.3"                                            │   │
│  │   },                                                                 │   │
│  │   "created_at": "2024-01-15T10:30:00Z",                             │   │
│  │   "updated_at": "2024-01-15T10:32:45Z"                              │   │
│  │ }                                                                    │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Benefits:                                                                   │
│  • Resume from step 3 if interrupted                                        │
│  • Show progress to user                                                    │
│  • Rollback to previous state                                               │
│  • Audit trail of what happened                                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera State Management

### 1. Basic State Machine

```python
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Optional, Callable, Any
from datetime import datetime

class AgentState(Enum):
    IDLE = auto()
    THINKING = auto()
    EXECUTING_TOOL = auto()
    WAITING_APPROVAL = auto()
    RESPONDING = auto()
    ERROR = auto()

@dataclass
class StateContext:
    current_state: AgentState = AgentState.IDLE
    previous_state: Optional[AgentState] = None

    # State-specific data
    current_message: Optional[str] = None
    current_tool: Optional[str] = None
    tool_result: Optional[Any] = None
    error: Optional[str] = None

    # Timing
    state_entered_at: datetime = field(default_factory=datetime.now)

    def transition_to(self, new_state: AgentState):
        \"\"\"Transition to a new state.\"\"\"
        self.previous_state = self.current_state
        self.current_state = new_state
        self.state_entered_at = datetime.now()

    @property
    def time_in_state(self) -> float:
        return (datetime.now() - self.state_entered_at).total_seconds()

class StateMachine:
    \"\"\"Simple state machine for agent.\"\"\"

    def __init__(self):
        self.context = StateContext()
        self.transitions: dict[tuple[AgentState, str], AgentState] = {}
        self.handlers: dict[AgentState, Callable] = {}

    def add_transition(self, from_state: AgentState, event: str, to_state: AgentState):
        self.transitions[(from_state, event)] = to_state

    def add_handler(self, state: AgentState, handler: Callable):
        self.handlers[state] = handler

    def trigger(self, event: str, **data):
        \"\"\"Trigger a state transition.\"\"\"
        key = (self.context.current_state, event)

        if key not in self.transitions:
            raise ValueError(f"Invalid transition: {key}")

        new_state = self.transitions[key]
        self.context.transition_to(new_state)

        # Update context with event data
        for k, v in data.items():
            setattr(self.context, k, v)

        # Run handler
        if new_state in self.handlers:
            self.handlers[new_state](self.context)

# Setup
sm = StateMachine()

# Define transitions
sm.add_transition(AgentState.IDLE, "message_received", AgentState.THINKING)
sm.add_transition(AgentState.THINKING, "need_tool", AgentState.EXECUTING_TOOL)
sm.add_transition(AgentState.THINKING, "has_answer", AgentState.RESPONDING)
sm.add_transition(AgentState.EXECUTING_TOOL, "tool_done", AgentState.THINKING)
sm.add_transition(AgentState.EXECUTING_TOOL, "tool_error", AgentState.ERROR)
sm.add_transition(AgentState.RESPONDING, "response_sent", AgentState.IDLE)
sm.add_transition(AgentState.ERROR, "error_handled", AgentState.IDLE)

# Add handlers
def on_thinking(ctx: StateContext):
    print(f"Thinking about: {ctx.current_message}")

sm.add_handler(AgentState.THINKING, on_thinking)

# Usage
sm.trigger("message_received", current_message="Deploy auth-service")
sm.trigger("need_tool", current_tool="deploy")
sm.trigger("tool_done", tool_result={"status": "success"})
sm.trigger("has_answer")
sm.trigger("response_sent")
```

### 2. Workflow State Manager

```python
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Callable
import json
import time

class StepStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

@dataclass
class WorkflowStep:
    name: str
    handler: Callable
    status: StepStatus = StepStatus.PENDING
    result: Optional[dict] = None
    error: Optional[str] = None
    started_at: Optional[float] = None
    completed_at: Optional[float] = None

    @property
    def duration(self) -> Optional[float]:
        if self.started_at and self.completed_at:
            return self.completed_at - self.started_at
        return None

@dataclass
class WorkflowState:
    workflow_id: str
    steps: list[WorkflowStep]
    context: dict = field(default_factory=dict)
    current_step_index: int = 0
    created_at: float = field(default_factory=time.time)

    @property
    def current_step(self) -> Optional[WorkflowStep]:
        if 0 <= self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        return None

    @property
    def is_complete(self) -> bool:
        return all(s.status in [StepStatus.COMPLETED, StepStatus.SKIPPED]
                   for s in self.steps)

    @property
    def has_failed(self) -> bool:
        return any(s.status == StepStatus.FAILED for s in self.steps)

    def to_dict(self) -> dict:
        return {
            "workflow_id": self.workflow_id,
            "current_step": self.current_step_index,
            "is_complete": self.is_complete,
            "has_failed": self.has_failed,
            "steps": [
                {
                    "name": s.name,
                    "status": s.status.value,
                    "duration": s.duration,
                    "error": s.error
                }
                for s in self.steps
            ],
            "context": self.context
        }

class WorkflowExecutor:
    \"\"\"Execute multi-step workflows with state persistence.\"\"\"

    def __init__(self, storage=None):
        self.storage = storage or {}  # In-memory by default

    def create_workflow(self, workflow_id: str, steps: list[tuple[str, Callable]],
                        context: dict = None) -> WorkflowState:
        \"\"\"Create a new workflow.\"\"\"
        workflow = WorkflowState(
            workflow_id=workflow_id,
            steps=[WorkflowStep(name=name, handler=handler) for name, handler in steps],
            context=context or {}
        )
        self._save(workflow)
        return workflow

    def execute(self, workflow_id: str, stop_on_error: bool = True) -> WorkflowState:
        \"\"\"Execute workflow from current position.\"\"\"
        workflow = self._load(workflow_id)

        while not workflow.is_complete and not workflow.has_failed:
            step = workflow.current_step
            if step is None:
                break

            # Execute step
            step.status = StepStatus.IN_PROGRESS
            step.started_at = time.time()
            self._save(workflow)

            try:
                result = step.handler(workflow.context)
                step.result = result
                step.status = StepStatus.COMPLETED

                # Update context with step result
                if result:
                    workflow.context.update(result)

            except Exception as e:
                step.error = str(e)
                step.status = StepStatus.FAILED

                if stop_on_error:
                    self._save(workflow)
                    return workflow

            step.completed_at = time.time()
            workflow.current_step_index += 1
            self._save(workflow)

        return workflow

    def resume(self, workflow_id: str) -> WorkflowState:
        \"\"\"Resume a paused/failed workflow.\"\"\"
        workflow = self._load(workflow_id)

        # Find first non-completed step
        for i, step in enumerate(workflow.steps):
            if step.status in [StepStatus.PENDING, StepStatus.FAILED]:
                workflow.current_step_index = i
                step.status = StepStatus.PENDING  # Reset failed step
                break

        return self.execute(workflow_id)

    def get_status(self, workflow_id: str) -> dict:
        \"\"\"Get workflow status.\"\"\"
        workflow = self._load(workflow_id)
        return workflow.to_dict()

    def _save(self, workflow: WorkflowState):
        self.storage[workflow.workflow_id] = workflow

    def _load(self, workflow_id: str) -> WorkflowState:
        if workflow_id not in self.storage:
            raise ValueError(f"Workflow not found: {workflow_id}")
        return self.storage[workflow_id]

# Usage example
def validate_config(context: dict) -> dict:
    print(f"Validating config for {context['service_name']}")
    return {"config_valid": True}

def build_image(context: dict) -> dict:
    print(f"Building image for {context['service_name']}")
    return {"image_tag": f"{context['service_name']}:latest"}

def deploy(context: dict) -> dict:
    print(f"Deploying {context['image_tag']}")
    return {"deployment_url": f"https://{context['service_name']}.example.com"}

# Create and execute workflow
executor = WorkflowExecutor()

workflow = executor.create_workflow(
    workflow_id="deploy_123",
    steps=[
        ("validate", validate_config),
        ("build", build_image),
        ("deploy", deploy)
    ],
    context={"service_name": "auth-service", "env": "staging"}
)

result = executor.execute("deploy_123")
print(json.dumps(result.to_dict(), indent=2))
```

### 3. Concurrent State Handling

```python
import asyncio
from asyncio import Lock
from typing import Dict
import uuid

class ConcurrentAgentState:
    \"\"\"Thread-safe state management for concurrent requests.\"\"\"

    def __init__(self):
        self._sessions: Dict[str, dict] = {}
        self._locks: Dict[str, Lock] = {}
        self._global_lock = Lock()

    async def _get_lock(self, session_id: str) -> Lock:
        async with self._global_lock:
            if session_id not in self._locks:
                self._locks[session_id] = Lock()
            return self._locks[session_id]

    async def get_state(self, session_id: str) -> dict:
        \"\"\"Get state for a session (creates if not exists).\"\"\"
        lock = await self._get_lock(session_id)
        async with lock:
            if session_id not in self._sessions:
                self._sessions[session_id] = {
                    "messages": [],
                    "current_state": "idle",
                    "context": {}
                }
            return self._sessions[session_id].copy()

    async def update_state(self, session_id: str, updates: dict):
        \"\"\"Update state atomically.\"\"\"
        lock = await self._get_lock(session_id)
        async with lock:
            state = await self.get_state(session_id)
            state.update(updates)
            self._sessions[session_id] = state

    async def with_state(self, session_id: str, handler):
        \"\"\"Execute handler with locked state.\"\"\"
        lock = await self._get_lock(session_id)
        async with lock:
            state = self._sessions.get(session_id, {})
            result = await handler(state)
            self._sessions[session_id] = state
            return result

# Usage
state_manager = ConcurrentAgentState()

async def handle_message(session_id: str, message: str):
    # Get current state
    state = await state_manager.get_state(session_id)

    # Process message
    state["messages"].append({"role": "user", "content": message})
    state["current_state"] = "thinking"

    # Update state
    await state_manager.update_state(session_id, state)

    # ... process with LLM ...

    # Update state again
    await state_manager.update_state(session_id, {
        "current_state": "idle"
    })

# Handle concurrent requests
async def main():
    tasks = [
        handle_message("session_1", "Hello"),
        handle_message("session_1", "How are you?"),  # Same session
        handle_message("session_2", "Different session")
    ]
    await asyncio.gather(*tasks)
```

### 4. State Persistence

```python
import json
import redis
from abc import ABC, abstractmethod

class StateStore(ABC):
    @abstractmethod
    def save(self, key: str, state: dict) -> None:
        pass

    @abstractmethod
    def load(self, key: str) -> Optional[dict]:
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        pass

class RedisStateStore(StateStore):
    \"\"\"Production-ready state storage with Redis.\"\"\"

    def __init__(self, redis_url: str = "redis://localhost:6379", ttl: int = 3600):
        self.client = redis.from_url(redis_url)
        self.ttl = ttl

    def save(self, key: str, state: dict):
        self.client.setex(
            f"agent_state:{key}",
            self.ttl,
            json.dumps(state)
        )

    def load(self, key: str) -> Optional[dict]:
        data = self.client.get(f"agent_state:{key}")
        if data:
            return json.loads(data)
        return None

    def delete(self, key: str):
        self.client.delete(f"agent_state:{key}")

class PersistentAgent:
    \"\"\"Agent with persistent state.\"\"\"

    def __init__(self, store: StateStore):
        self.store = store

    def process(self, session_id: str, message: str) -> str:
        # Load state
        state = self.store.load(session_id) or {
            "messages": [],
            "context": {}
        }

        # Add message
        state["messages"].append({"role": "user", "content": message})

        # Process with LLM...
        response = "..."  # LLM response

        state["messages"].append({"role": "assistant", "content": response})

        # Save state
        self.store.save(session_id, state)

        return response
```

## Praktisk övning

**Uppgift:** Bygg en Resumable Deployment Agent

```python
\"\"\"
TODO: Bygg en agent som kan:

1. Köra multi-step deployments
2. Pausa och återuppta mitt i processen
3. Hantera failures gracefully
4. Visa progress till användaren

Steps:
1. validate_config
2. run_tests
3. build_image
4. push_to_registry
5. deploy_to_staging
6. run_smoke_tests
7. deploy_to_prod (requires approval)

Requirements:
- Om ett steg misslyckas: stoppa och låt användaren fixa
- Användare ska kunna köra "resume" för att fortsätta
- Varje steg ska spara state
- Approval step ska vänta på user input
\"\"\"

class ResumableDeploymentAgent:
    def __init__(self):
        # Din kod här
        pass

    def start_deployment(self, service_name: str, version: str) -> str:
        # Returnera workflow_id
        pass

    def get_status(self, workflow_id: str) -> dict:
        # Returnera current state
        pass

    def resume(self, workflow_id: str) -> dict:
        # Fortsätt från senaste steg
        pass

    def approve_step(self, workflow_id: str, step_name: str) -> dict:
        # Godkänn ett steg som väntar
        pass

# Test
agent = ResumableDeploymentAgent()
wf_id = agent.start_deployment("auth-service", "v1.2.3")
print(agent.get_status(wf_id))
```

## Sammanfattning

- ✅ **State machines** för tydlig agent behavior
- ✅ **Workflow state** för multi-step tasks
- ✅ **Locks** för concurrent access
- ✅ **Persistence** för recovery och resumption

## Nästa steg

- **Node 15:** Multi-Agent Systems
- **Node 16:** Agent Orchestration

---
*Pro tip: Alltid designa för failure — vad händer om agenten kraschar mitt i?*
"""
    }
]
