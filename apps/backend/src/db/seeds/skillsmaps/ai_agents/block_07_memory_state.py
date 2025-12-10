# =============================================================================
# AI AGENTS - BLOCK 07: MEMORY & STATE (Noder 13-14) - V3 FORMAT
# =============================================================================

NODE_13_MEMORY_SYSTEMS = {
    "node_id": 13,
    "title": "Memory Systems",
    "slug": "memory-systems",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [12],
    "content": '''
# Memory Systems

Ge agenter formagan att minnas och lara sig.

------------------------------------------------------------

## Vad ar Agent Memory?

Memory later agenter behalla information mellan interaktioner. Det gor dem mer intelligenta och personliga.

| Memory Type | Varaktighet | Anvandning |
|-------------|-------------|------------|
| Short-term | Session | Konversation |
| Long-term | Persistent | Preferenser |
| Episodic | Specifika events | Tidigare interaktioner |
| Semantic | Fakta | Larad kunskap |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Personalisering | Agent som larer sig preferenser |
| Kontinuitet | Behaller kontext mellan sessioner |
| Effektivitet | Undviker upprepade fragor |
| Intelligens | Battre beslut med historik |

------------------------------------------------------------

## Snabbreferens - Memory Types

| Typ | Implementation | Cost |
|-----|----------------|------|
| Buffer | Lista i minnet | Lag |
| Summary | LLM sammanfattning | Medium |
| Vector | Embedding database | Hog |
| Hybrid | Kombination | Varierar |

------------------------------------------------------------

## Memory Architecture

```
+-----------------------------------------------------------------+
|                   MEMORY ARCHITECTURE                            |
+-----------------------------------------------------------------+
|                                                                  |
|  +-----------------------------------------------------------+ |
|  |                    WORKING MEMORY                          | |
|  |  Current conversation, recent context                      | |
|  +-----------------------------------------------------------+ |
|                           |                                      |
|           +---------------+---------------+                     |
|           v               v               v                      |
|  +-------------+  +-------------+  +-------------+             |
|  | SHORT-TERM |  |  LONG-TERM  |  |  SEMANTIC   |             |
|  |   MEMORY   |  |   MEMORY    |  |   MEMORY    |             |
|  |            |  |             |  |             |              |
|  | - Buffer   |  | - Vector DB |  | - Knowledge |             |
|  | - Last N   |  | - Summaries |  | - Facts     |             |
|  | - Session  |  | - Episodes  |  | - Relations |             |
|  +-------------+  +-------------+  +-------------+             |
|         |                |                |                      |
|         +----------------+----------------+                     |
|                          v                                       |
|  +-----------------------------------------------------------+ |
|  |                   MEMORY RETRIEVAL                         | |
|  |  - Recency weighting                                       | |
|  |  - Relevance scoring                                       | |
|  |  - Importance filtering                                    | |
|  +-----------------------------------------------------------+ |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Buffer Memory

```python
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Message:
    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)

class BufferMemory:
    """Enkel buffer memory som sparar senaste N meddelanden."""

    def __init__(self, max_messages: int = 20):
        self.max_messages = max_messages
        self.messages: list[Message] = []

    def add(self, role: str, content: str) -> None:
        self.messages.append(Message(role=role, content=content))
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_history(self) -> list[dict]:
        return [
            {"role": m.role, "content": m.content}
            for m in self.messages
        ]

    def clear(self) -> None:
        self.messages = []

    def to_prompt_string(self) -> str:
        return "\n".join([
            f"{m.role}: {m.content}" for m in self.messages
        ])
```

------------------------------------------------------------

## Summary Memory

```python
class SummaryMemory:
    """Memory som sammanfattar lange konversationer."""

    def __init__(self, client, summary_threshold: int = 10):
        self.client = client
        self.summary_threshold = summary_threshold
        self.messages: list[Message] = []
        self.summary: str = ""

    def add(self, role: str, content: str) -> None:
        self.messages.append(Message(role=role, content=content))

        if len(self.messages) >= self.summary_threshold:
            self._summarize()

    def _summarize(self) -> None:
        conversation = self.to_prompt_string()

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""Sammanfatta denna konversation koncist:

                Tidigare sammanfattning: {self.summary}

                Ny konversation:
                {conversation}

                Behall viktig information, namn, preferenser och beslut."""
            }]
        )

        self.summary = response.choices[0].message.content
        self.messages = self.messages[-3:]  # Behall senaste 3

    def get_context(self) -> str:
        recent = self.to_prompt_string()
        if self.summary:
            return f"Sammanfattning: {self.summary}\n\nSenaste meddelanden:\n{recent}"
        return recent
```

------------------------------------------------------------

## Vector Memory

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class MemoryEntry:
    content: str
    embedding: list[float]
    metadata: dict
    timestamp: datetime
    importance: float = 1.0

class VectorMemory:
    """Memory med semantic search via embeddings."""

    def __init__(self, client, embedding_model: str = "text-embedding-3-small"):
        self.client = client
        self.embedding_model = embedding_model
        self.entries: list[MemoryEntry] = []

    def add(self, content: str, metadata: dict = None, importance: float = 1.0) -> None:
        embedding = self._get_embedding(content)

        entry = MemoryEntry(
            content=content,
            embedding=embedding,
            metadata=metadata or {},
            timestamp=datetime.now(),
            importance=importance
        )
        self.entries.append(entry)

    def search(self, query: str, top_k: int = 5) -> list[MemoryEntry]:
        query_embedding = self._get_embedding(query)

        scored = []
        for entry in self.entries:
            similarity = self._cosine_similarity(query_embedding, entry.embedding)
            recency = self._recency_score(entry.timestamp)
            score = similarity * 0.7 + recency * 0.2 + entry.importance * 0.1
            scored.append((score, entry))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [entry for _, entry in scored[:top_k]]

    def _get_embedding(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=text
        )
        return response.data[0].embedding

    def _cosine_similarity(self, a: list[float], b: list[float]) -> float:
        a, b = np.array(a), np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def _recency_score(self, timestamp: datetime) -> float:
        hours_ago = (datetime.now() - timestamp).total_seconds() / 3600
        return 1.0 / (1.0 + hours_ago)
```

------------------------------------------------------------

## Hybrid Memory

```python
class HybridMemory:
    """Kombinerar buffer, summary och vector memory."""

    def __init__(self, client):
        self.buffer = BufferMemory(max_messages=10)
        self.summary = SummaryMemory(client, summary_threshold=15)
        self.vector = VectorMemory(client)
        self.client = client

    def add_message(self, role: str, content: str) -> None:
        self.buffer.add(role, content)
        self.summary.add(role, content)

        if role == "assistant" or len(content) > 100:
            self.vector.add(content, {"role": role})

    def get_context(self, current_query: str) -> str:
        recent = self.buffer.get_history()
        summary = self.summary.summary
        relevant = self.vector.search(current_query, top_k=3)

        relevant_text = "\n".join([e.content for e in relevant])

        return f"""
        Sammanfattning av tidigare konversation:
        {summary}

        Relevant tidigare information:
        {relevant_text}

        Senaste meddelanden:
        {self.buffer.to_prompt_string()}
        """
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Kontext overflow | For mycket historik | Anvand summary memory |
| Tappar info | Buffer for kort | Oka max_messages |
| Irrelevant recall | Dalig similarity | Justera retrieval scoring |
| Langsam search | For manga entries | Implementera index |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Buffer | Enkelt, for korta sessioner |
| Summary | Komprimerar lang historik |
| Vector | Semantic search i minne |
| Hybrid | Kombinera for bast resultat |

Kom ihag:
- Borja med buffer, upgradera vid behov
- Summary sparar tokens
- Vector memory kraver embedding calls
- Hybrid ar oftast bast for produktion
'''
}

NODE_14_STATE_MANAGEMENT = {
    "node_id": 14,
    "title": "State Management",
    "slug": "state-management",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [13],
    "content": '''
# State Management

Hantera agentens tillstand genom komplexa workflows.

------------------------------------------------------------

## Vad ar Agent State?

State ar all information agenten behover for att fatta beslut. Det inkluderar konversation, minnne, aktivt task och metadata.

| State Type | Innehaller |
|------------|------------|
| Conversation | Meddelanden, context |
| Task | Nuvarande mal, progress |
| Memory | Historik, learnings |
| System | Config, permissions |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Debugging | Klar state = latt att debugga |
| Persistence | Spara och ladda sessioner |
| Skalbarhet | Stateless workers |
| Recovery | Aterstall fran fel |

------------------------------------------------------------

## Snabbreferens - State Patterns

| Pattern | Anvandning | Komplexitet |
|---------|------------|-------------|
| Immutable | Enkel, sakert | Lag |
| Event-sourced | Full historik | Hog |
| Graph-based | Komplexa workflows | Medium |
| Checkpointed | Long-running | Medium |

------------------------------------------------------------

## State Architecture

```
+-----------------------------------------------------------------+
|                    STATE ARCHITECTURE                            |
+-----------------------------------------------------------------+
|                                                                  |
|  +-----------------------------------------------------------+ |
|  |                    AGENT STATE                             | |
|  +-----------------------------------------------------------+ |
|  |  conversation_state:                                       | |
|  |    - messages[]                                            | |
|  |    - current_turn                                          | |
|  |                                                            | |
|  |  task_state:                                               | |
|  |    - current_goal                                          | |
|  |    - completed_steps[]                                     | |
|  |    - pending_actions[]                                     | |
|  |                                                            | |
|  |  memory_state:                                             | |
|  |    - short_term                                            | |
|  |    - long_term_ref                                         | |
|  |                                                            | |
|  |  system_state:                                             | |
|  |    - config                                                | |
|  |    - permissions                                           | |
|  |    - rate_limits                                           | |
|  +-----------------------------------------------------------+ |
|                           |                                      |
|                           v                                      |
|  +-----------------------------------------------------------+ |
|  |                   STATE STORE                              | |
|  |  Redis / PostgreSQL / File System                         | |
|  +-----------------------------------------------------------+ |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Immutable State

```python
from dataclasses import dataclass, field, replace
from typing import FrozenSet
from datetime import datetime
import json

@dataclass(frozen=True)
class ConversationState:
    messages: tuple = ()
    turn_count: int = 0

@dataclass(frozen=True)
class TaskState:
    goal: str = ""
    completed_steps: tuple = ()
    status: str = "pending"

@dataclass(frozen=True)
class AgentState:
    conversation: ConversationState = field(default_factory=ConversationState)
    task: TaskState = field(default_factory=TaskState)
    created_at: datetime = field(default_factory=datetime.now)
    version: int = 0

    def add_message(self, role: str, content: str) -> "AgentState":
        new_messages = self.conversation.messages + ({"role": role, "content": content},)
        new_conversation = replace(
            self.conversation,
            messages=new_messages,
            turn_count=self.conversation.turn_count + 1
        )
        return replace(self, conversation=new_conversation, version=self.version + 1)

    def complete_step(self, step: str) -> "AgentState":
        new_steps = self.task.completed_steps + (step,)
        new_task = replace(self.task, completed_steps=new_steps)
        return replace(self, task=new_task, version=self.version + 1)

    def to_dict(self) -> dict:
        return {
            "conversation": {
                "messages": list(self.conversation.messages),
                "turn_count": self.conversation.turn_count
            },
            "task": {
                "goal": self.task.goal,
                "completed_steps": list(self.task.completed_steps),
                "status": self.task.status
            },
            "version": self.version
        }
```

------------------------------------------------------------

## Event-Sourced State

```python
from dataclasses import dataclass
from typing import Union
from datetime import datetime
from enum import Enum

class EventType(Enum):
    MESSAGE_ADDED = "message_added"
    STEP_COMPLETED = "step_completed"
    GOAL_SET = "goal_set"
    ERROR_OCCURRED = "error_occurred"

@dataclass
class Event:
    type: EventType
    payload: dict
    timestamp: datetime = field(default_factory=datetime.now)
    version: int = 0

class EventStore:
    def __init__(self):
        self.events: list[Event] = []

    def append(self, event: Event) -> None:
        event.version = len(self.events)
        self.events.append(event)

    def get_events(self, since_version: int = 0) -> list[Event]:
        return self.events[since_version:]

class EventSourcedState:
    """State som byggs fran events."""

    def __init__(self, store: EventStore):
        self.store = store
        self.messages = []
        self.completed_steps = []
        self.goal = ""
        self.errors = []

    def rebuild(self) -> None:
        self.messages = []
        self.completed_steps = []

        for event in self.store.events:
            self._apply(event)

    def _apply(self, event: Event) -> None:
        if event.type == EventType.MESSAGE_ADDED:
            self.messages.append(event.payload)
        elif event.type == EventType.STEP_COMPLETED:
            self.completed_steps.append(event.payload["step"])
        elif event.type == EventType.GOAL_SET:
            self.goal = event.payload["goal"]
        elif event.type == EventType.ERROR_OCCURRED:
            self.errors.append(event.payload)
```

------------------------------------------------------------

## Checkpointed State

```python
import json
from pathlib import Path

class CheckpointManager:
    """Spara och ladda state checkpoints."""

    def __init__(self, checkpoint_dir: str = "./checkpoints"):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(exist_ok=True)

    def save(self, state: AgentState, session_id: str) -> str:
        checkpoint_id = f"{session_id}_{state.version}"
        path = self.checkpoint_dir / f"{checkpoint_id}.json"

        with open(path, "w") as f:
            json.dump(state.to_dict(), f)

        return checkpoint_id

    def load(self, checkpoint_id: str) -> AgentState:
        path = self.checkpoint_dir / f"{checkpoint_id}.json"

        with open(path, "r") as f:
            data = json.load(f)

        return self._dict_to_state(data)

    def list_checkpoints(self, session_id: str) -> list[str]:
        pattern = f"{session_id}_*.json"
        return [p.stem for p in self.checkpoint_dir.glob(pattern)]

    def _dict_to_state(self, data: dict) -> AgentState:
        conversation = ConversationState(
            messages=tuple(data["conversation"]["messages"]),
            turn_count=data["conversation"]["turn_count"]
        )
        task = TaskState(
            goal=data["task"]["goal"],
            completed_steps=tuple(data["task"]["completed_steps"]),
            status=data["task"]["status"]
        )
        return AgentState(
            conversation=conversation,
            task=task,
            version=data["version"]
        )
```

------------------------------------------------------------

## State Machine

```python
from enum import Enum, auto

class WorkflowState(Enum):
    IDLE = auto()
    PLANNING = auto()
    EXECUTING = auto()
    WAITING_INPUT = auto()
    COMPLETED = auto()
    ERROR = auto()

class StateMachine:
    """Finite state machine for agent workflow."""

    TRANSITIONS = {
        WorkflowState.IDLE: [WorkflowState.PLANNING],
        WorkflowState.PLANNING: [WorkflowState.EXECUTING, WorkflowState.ERROR],
        WorkflowState.EXECUTING: [WorkflowState.WAITING_INPUT, WorkflowState.COMPLETED, WorkflowState.ERROR],
        WorkflowState.WAITING_INPUT: [WorkflowState.EXECUTING],
        WorkflowState.COMPLETED: [WorkflowState.IDLE],
        WorkflowState.ERROR: [WorkflowState.IDLE, WorkflowState.PLANNING]
    }

    def __init__(self):
        self.state = WorkflowState.IDLE
        self.history = []

    def transition(self, to_state: WorkflowState) -> bool:
        if to_state in self.TRANSITIONS.get(self.state, []):
            self.history.append((self.state, to_state))
            self.state = to_state
            return True
        return False

    def can_transition(self, to_state: WorkflowState) -> bool:
        return to_state in self.TRANSITIONS.get(self.state, [])
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| State corruption | Mutable state | Anvand immutable |
| Lost state | Ingen persistence | Implementera checkpoints |
| Invalid transition | Dold state logic | Anvand state machine |
| Memory leak | Ingen cleanup | Implementera TTL |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Immutable | Sakrast, lattest att debugga |
| Event-sourced | Full historik, replay |
| Checkpoints | Recovery for long-running |
| State machine | Explicit workflow control |

Kom ihag:
- Immutable state forhindrar buggar
- Event sourcing for audit trail
- Checkpoints for lange sessioner
- State machines for komplexa workflows
'''
}

BLOCK_07_NODES = [NODE_13_MEMORY_SYSTEMS, NODE_14_STATE_MANAGEMENT]
