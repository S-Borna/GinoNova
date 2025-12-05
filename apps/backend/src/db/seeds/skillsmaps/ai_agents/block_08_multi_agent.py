"""
AI Agents SkillsMap - Block 08: Multi-Agent Systems
Nodes 15-16: Multi-Agent Design, Orchestration
"""

BLOCK_08_NODES = [
    {
        "id": "ai-agents-15",
        "slug": "multi-agent-systems",
        "title": "Multi-Agent Systems Design",
        "order_index": 15,
        "estimated_minutes": 50,
        "xp_reward": 130,
        "difficulty": "hard",
        "node_type": "concept",
        "prerequisites": ["ai-agents-14"],
        "content": """# Multi-Agent Systems Design

## Varför detta är viktigt

En ensam agent kan vara bra på en sak, men komplexa uppgifter kräver ofta
specialisering. Multi-agent systems låter dig:

- **Specialisera** — Varje agent är expert på sitt område
- **Parallellisera** — Flera agenter jobbar samtidigt
- **Validera** — Agenter granskar varandras arbete
- **Skala** — Lägg till fler agenter vid behov

Men multi-agent systems är också mer komplexa. Denna modul lär dig
designa effektiva team av agenter.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Designa agent team arkitekturer
- ✅ Implementera agent-to-agent kommunikation
- ✅ Hantera konflikter och konsensus
- ✅ Välja rätt topologi för ditt use case
- ✅ Undvika vanliga multi-agent fallgropar

## Kärnkoncept

### Multi-Agent Topologies

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MULTI-AGENT TOPOLOGIES                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. HIERARCHICAL (Manager → Workers)                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    ┌───────────────┐                                 │   │
│  │                    │   Manager     │                                 │   │
│  │                    │   (Planning)  │                                 │   │
│  │                    └───────┬───────┘                                 │   │
│  │                            │                                          │   │
│  │              ┌─────────────┼─────────────┐                           │   │
│  │              ▼             ▼             ▼                           │   │
│  │        ┌─────────┐   ┌─────────┐   ┌─────────┐                      │   │
│  │        │ Worker  │   │ Worker  │   │ Worker  │                      │   │
│  │        │  (Code) │   │ (Test)  │   │ (Deploy)│                      │   │
│  │        └─────────┘   └─────────┘   └─────────┘                      │   │
│  │                                                                      │   │
│  │  ✓ Clear chain of command                                           │   │
│  │  ✓ Easy to understand                                               │   │
│  │  ✗ Single point of failure (manager)                                │   │
│  │  ✗ Bottleneck at manager                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  2. PEER-TO-PEER (Collaborative)                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │        ┌─────────┐ ◄──────► ┌─────────┐                             │   │
│  │        │ Agent A │          │ Agent B │                             │   │
│  │        │ (Design)│          │  (Code) │                             │   │
│  │        └────┬────┘          └────┬────┘                             │   │
│  │             │                    │                                   │   │
│  │             └────────┬───────────┘                                   │   │
│  │                      ▼                                               │   │
│  │               ┌─────────┐                                           │   │
│  │               │ Agent C │                                           │   │
│  │               │ (Review)│                                           │   │
│  │               └─────────┘                                           │   │
│  │                                                                      │   │
│  │  ✓ No single point of failure                                       │   │
│  │  ✓ Flexible collaboration                                           │   │
│  │  ✗ Coordination overhead                                            │   │
│  │  ✗ Potential for deadlocks                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  3. PIPELINE (Sequential)                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Input ──► Agent A ──► Agent B ──► Agent C ──► Output               │   │
│  │           (Parse)     (Process)    (Format)                         │   │
│  │                                                                      │   │
│  │  ✓ Simple data flow                                                 │   │
│  │  ✓ Easy to test each stage                                          │   │
│  │  ✗ Sequential (slow)                                                │   │
│  │  ✗ One failure blocks all                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  4. BLACKBOARD (Shared Workspace)                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │        ┌─────────┐   ┌─────────┐   ┌─────────┐                      │   │
│  │        │ Agent A │   │ Agent B │   │ Agent C │                      │   │
│  │        └────┬────┘   └────┬────┘   └────┬────┘                      │   │
│  │             │             │             │                            │   │
│  │             ▼             ▼             ▼                            │   │
│  │        ╔═════════════════════════════════════╗                      │   │
│  │        ║         BLACKBOARD                  ║                      │   │
│  │        ║  • Problem statement                ║                      │   │
│  │        ║  • Partial solutions                ║                      │   │
│  │        ║  • Knowledge contributions          ║                      │   │
│  │        ╚═════════════════════════════════════╝                      │   │
│  │                                                                      │   │
│  │  ✓ Agents work independently                                        │   │
│  │  ✓ Incremental problem solving                                      │   │
│  │  ✗ Coordination complexity                                          │   │
│  │  ✗ Potential conflicts                                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera Multi-Agent System

### 1. Agent Base Class

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Any, Callable
from enum import Enum
import asyncio
import uuid

class AgentRole(Enum):
    MANAGER = "manager"
    WORKER = "worker"
    REVIEWER = "reviewer"
    SPECIALIST = "specialist"

@dataclass
class Message:
    sender: str
    receiver: str
    content: Any
    message_type: str = "request"  # request, response, broadcast
    correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    reply_to: Optional[str] = None

class BaseAgent(ABC):
    \"\"\"Base class for all agents in multi-agent system.\"\"\"

    def __init__(self, agent_id: str, role: AgentRole):
        self.agent_id = agent_id
        self.role = role
        self.inbox: asyncio.Queue = asyncio.Queue()
        self.message_handlers: dict[str, Callable] = {}
        self._running = False

    @property
    @abstractmethod
    def capabilities(self) -> list[str]:
        \"\"\"List of things this agent can do.\"\"\"
        pass

    @abstractmethod
    async def process(self, message: Message) -> Optional[Message]:
        \"\"\"Process an incoming message.\"\"\"
        pass

    async def send(self, message: Message, router: 'MessageRouter'):
        \"\"\"Send a message through the router.\"\"\"
        await router.route(message)

    async def receive(self) -> Message:
        \"\"\"Receive a message from inbox.\"\"\"
        return await self.inbox.get()

    async def run(self, router: 'MessageRouter'):
        \"\"\"Main agent loop.\"\"\"
        self._running = True
        while self._running:
            try:
                message = await asyncio.wait_for(self.receive(), timeout=1.0)
                response = await self.process(message)
                if response:
                    await self.send(response, router)
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(f"Agent {self.agent_id} error: {e}")

    def stop(self):
        self._running = False
```

### 2. Message Router

```python
class MessageRouter:
    \"\"\"Routes messages between agents.\"\"\"

    def __init__(self):
        self.agents: dict[str, BaseAgent] = {}
        self.topic_subscribers: dict[str, list[str]] = {}

    def register(self, agent: BaseAgent):
        self.agents[agent.agent_id] = agent

    def subscribe(self, agent_id: str, topic: str):
        if topic not in self.topic_subscribers:
            self.topic_subscribers[topic] = []
        self.topic_subscribers[topic].append(agent_id)

    async def route(self, message: Message):
        if message.message_type == "broadcast":
            # Send to all agents
            for agent in self.agents.values():
                if agent.agent_id != message.sender:
                    await agent.inbox.put(message)

        elif message.receiver.startswith("topic:"):
            # Topic-based routing
            topic = message.receiver.replace("topic:", "")
            for agent_id in self.topic_subscribers.get(topic, []):
                await self.agents[agent_id].inbox.put(message)

        elif message.receiver in self.agents:
            # Direct routing
            await self.agents[message.receiver].inbox.put(message)

        else:
            print(f"Unknown receiver: {message.receiver}")

    async def run_all(self):
        \"\"\"Run all agents concurrently.\"\"\"
        tasks = [
            asyncio.create_task(agent.run(self))
            for agent in self.agents.values()
        ]
        await asyncio.gather(*tasks)
```

### 3. Hierarchical Team

```python
from openai import OpenAI

class ManagerAgent(BaseAgent):
    \"\"\"Coordinates worker agents.\"\"\"

    def __init__(self, agent_id: str, workers: list[str]):
        super().__init__(agent_id, AgentRole.MANAGER)
        self.workers = workers
        self.client = OpenAI()
        self.pending_tasks: dict[str, dict] = {}

    @property
    def capabilities(self) -> list[str]:
        return ["planning", "delegation", "coordination"]

    async def process(self, message: Message) -> Optional[Message]:
        if message.message_type == "request":
            # Plan and delegate
            plan = await self._create_plan(message.content)

            # Assign tasks to workers
            for task in plan["tasks"]:
                worker = self._select_worker(task)
                task_message = Message(
                    sender=self.agent_id,
                    receiver=worker,
                    content=task,
                    message_type="request",
                    correlation_id=message.correlation_id
                )
                self.pending_tasks[task["id"]] = {
                    "task": task,
                    "status": "pending",
                    "worker": worker
                }
                return task_message

        elif message.message_type == "response":
            # Worker completed task
            task_id = message.content.get("task_id")
            if task_id in self.pending_tasks:
                self.pending_tasks[task_id]["status"] = "complete"
                self.pending_tasks[task_id]["result"] = message.content

                # Check if all tasks done
                if all(t["status"] == "complete" for t in self.pending_tasks.values()):
                    return self._compile_results(message.reply_to)

        return None

    async def _create_plan(self, task: str) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": \"\"\"
                You are a project manager. Break down tasks into subtasks.
                Return JSON: {"tasks": [{"id": "1", "type": "code|test|deploy", "description": "..."}]}
                \"\"\"},
                {"role": "user", "content": task}
            ]
        )
        import json
        return json.loads(response.choices[0].message.content)

    def _select_worker(self, task: dict) -> str:
        # Simple selection based on task type
        task_type = task.get("type", "code")
        for worker in self.workers:
            if task_type in worker:
                return worker
        return self.workers[0]

    def _compile_results(self, reply_to: str) -> Message:
        results = [t["result"] for t in self.pending_tasks.values()]
        return Message(
            sender=self.agent_id,
            receiver=reply_to,
            content={"status": "complete", "results": results},
            message_type="response"
        )


class WorkerAgent(BaseAgent):
    \"\"\"Executes specific tasks.\"\"\"

    def __init__(self, agent_id: str, specialty: str):
        super().__init__(agent_id, AgentRole.WORKER)
        self.specialty = specialty
        self.client = OpenAI()

    @property
    def capabilities(self) -> list[str]:
        return [self.specialty]

    async def process(self, message: Message) -> Optional[Message]:
        if message.message_type == "request":
            task = message.content
            result = await self._execute_task(task)

            return Message(
                sender=self.agent_id,
                receiver=message.sender,
                content={
                    "task_id": task["id"],
                    "result": result,
                    "status": "complete"
                },
                message_type="response",
                reply_to=message.correlation_id
            )
        return None

    async def _execute_task(self, task: dict) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a {self.specialty} expert. Execute the task and return results."},
                {"role": "user", "content": task["description"]}
            ]
        )
        return {"output": response.choices[0].message.content}


# Usage
async def run_hierarchical_team():
    router = MessageRouter()

    # Create workers
    coder = WorkerAgent("worker_code", "coding")
    tester = WorkerAgent("worker_test", "testing")

    # Create manager
    manager = ManagerAgent("manager", ["worker_code", "worker_test"])

    # Register all
    router.register(manager)
    router.register(coder)
    router.register(tester)

    # Send task to manager
    task = Message(
        sender="user",
        receiver="manager",
        content="Build a REST API endpoint for user registration"
    )
    await router.route(task)

    # Run for a while
    await asyncio.wait_for(router.run_all(), timeout=60)
```

### 4. Peer-to-Peer Collaboration

```python
class CollaborativeAgent(BaseAgent):
    \"\"\"Agent that collaborates with peers.\"\"\"

    def __init__(self, agent_id: str, specialty: str, peers: list[str]):
        super().__init__(agent_id, AgentRole.SPECIALIST)
        self.specialty = specialty
        self.peers = peers
        self.client = OpenAI()
        self.contributions: dict[str, list] = {}  # correlation_id -> contributions

    @property
    def capabilities(self) -> list[str]:
        return [self.specialty, "collaborate"]

    async def process(self, message: Message) -> Optional[Message]:
        if message.message_type == "request":
            # Generate my contribution
            my_contribution = await self._contribute(message.content)

            # Store it
            cid = message.correlation_id
            if cid not in self.contributions:
                self.contributions[cid] = []
            self.contributions[cid].append({
                "from": self.agent_id,
                "content": my_contribution
            })

            # Share with peers
            for peer in self.peers:
                return Message(
                    sender=self.agent_id,
                    receiver=peer,
                    content={
                        "type": "contribution",
                        "contribution": my_contribution,
                        "original_task": message.content
                    },
                    message_type="broadcast",
                    correlation_id=cid
                )

        elif message.message_type == "broadcast":
            # Received peer's contribution
            content = message.content
            cid = message.correlation_id

            if cid not in self.contributions:
                self.contributions[cid] = []

            self.contributions[cid].append({
                "from": message.sender,
                "content": content["contribution"]
            })

            # Check if we have all contributions
            if len(self.contributions[cid]) >= len(self.peers) + 1:
                # Synthesize final answer
                return await self._synthesize(cid, content["original_task"])

        return None

    async def _contribute(self, task: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a {self.specialty} expert. Contribute your perspective."},
                {"role": "user", "content": task}
            ]
        )
        return response.choices[0].message.content

    async def _synthesize(self, correlation_id: str, task: str) -> Message:
        contributions = self.contributions[correlation_id]
        contrib_text = "\\n\\n".join([
            f"**{c['from']}**: {c['content']}" for c in contributions
        ])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Synthesize these expert contributions into a unified answer."},
                {"role": "user", "content": f"Task: {task}\\n\\nContributions:\\n{contrib_text}"}
            ]
        )

        return Message(
            sender=self.agent_id,
            receiver="user",
            content=response.choices[0].message.content,
            message_type="response",
            correlation_id=correlation_id
        )
```

### 5. Blackboard System

```python
from dataclasses import dataclass, field
from typing import Any
import asyncio

@dataclass
class BlackboardEntry:
    key: str
    value: Any
    author: str
    timestamp: float
    entry_type: str  # "fact", "hypothesis", "solution"

class Blackboard:
    \"\"\"Shared workspace for agents.\"\"\"

    def __init__(self):
        self.entries: list[BlackboardEntry] = []
        self.lock = asyncio.Lock()
        self.subscribers: list[asyncio.Queue] = []

    async def write(self, entry: BlackboardEntry):
        async with self.lock:
            self.entries.append(entry)
            # Notify subscribers
            for queue in self.subscribers:
                await queue.put(entry)

    async def read(self, entry_type: str = None) -> list[BlackboardEntry]:
        async with self.lock:
            if entry_type:
                return [e for e in self.entries if e.entry_type == entry_type]
            return self.entries.copy()

    def subscribe(self) -> asyncio.Queue:
        queue = asyncio.Queue()
        self.subscribers.append(queue)
        return queue


class BlackboardAgent(BaseAgent):
    \"\"\"Agent that works on a shared blackboard.\"\"\"

    def __init__(self, agent_id: str, specialty: str, blackboard: Blackboard):
        super().__init__(agent_id, AgentRole.SPECIALIST)
        self.specialty = specialty
        self.blackboard = blackboard
        self.client = OpenAI()
        self.notification_queue = blackboard.subscribe()

    @property
    def capabilities(self) -> list[str]:
        return [self.specialty]

    async def run(self, router: 'MessageRouter'):
        \"\"\"Watch blackboard and contribute when relevant.\"\"\"
        self._running = True
        while self._running:
            try:
                # Wait for blackboard updates
                entry = await asyncio.wait_for(
                    self.notification_queue.get(),
                    timeout=1.0
                )

                # Check if I can contribute
                if self._is_relevant(entry):
                    contribution = await self._generate_contribution(entry)
                    if contribution:
                        await self.blackboard.write(BlackboardEntry(
                            key=f"{self.agent_id}_contribution",
                            value=contribution,
                            author=self.agent_id,
                            timestamp=asyncio.get_event_loop().time(),
                            entry_type="hypothesis" if entry.entry_type == "fact" else "solution"
                        ))

            except asyncio.TimeoutError:
                continue

    def _is_relevant(self, entry: BlackboardEntry) -> bool:
        # Check if this entry is relevant to my specialty
        return self.specialty.lower() in str(entry.value).lower()

    async def _generate_contribution(self, entry: BlackboardEntry) -> Optional[str]:
        all_entries = await self.blackboard.read()
        context = "\\n".join([f"[{e.entry_type}] {e.value}" for e in all_entries[-5:]])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f\"\"\"
                You are a {self.specialty} expert working on a shared problem.
                Based on the current state, contribute your expertise.
                Only respond if you have something valuable to add.
                \"\"\"},
                {"role": "user", "content": f"Current blackboard state:\\n{context}"}
            ]
        )

        content = response.choices[0].message.content
        if "nothing to add" in content.lower():
            return None
        return content

    async def process(self, message: Message) -> Optional[Message]:
        # Blackboard agents primarily watch the blackboard
        return None
```

## Vanliga problem

### Problem: "Agenter pratar förbi varandra"

```python
# Lösning: Structured message format
@dataclass
class StructuredMessage:
    intent: str  # "request_help", "provide_info", "ask_clarification"
    topic: str
    content: str
    requires_response: bool
    deadline: Optional[float] = None
```

### Problem: "Deadlock mellan agenter"

```python
# Lösning: Timeout och fallback
async def safe_collaborate(self, message: Message, timeout: float = 30.0):
    try:
        return await asyncio.wait_for(
            self._collaborate(message),
            timeout=timeout
        )
    except asyncio.TimeoutError:
        return self._fallback_response(message)
```

## Praktisk övning

**Uppgift:** Bygg ett DevOps Agent Team

Se Node 16 för full implementation.

## Sammanfattning

- ✅ **Hierarchical** för clear command chains
- ✅ **Peer-to-peer** för collaborative problem solving
- ✅ **Pipeline** för sequential processing
- ✅ **Blackboard** för incremental problem solving

## Nästa steg

- **Node 16:** Agent Orchestration Patterns
- **Node 17:** Production Deployment

---
*Pro tip: Börja med 2 agenter och lägg till fler när du förstår dynamiken!*
"""
    },
    {
        "id": "ai-agents-16",
        "slug": "agent-orchestration",
        "title": "Agent Orchestration Patterns",
        "order_index": 16,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["ai-agents-15"],
        "content": """# Agent Orchestration Patterns

## Varför detta är viktigt

Att ha flera agenter är bara halva utmaningen — den verkliga komplexiteten
ligger i att orkestrera dem effektivt. Dålig orchestration leder till:

- **Ineffektivitet** — Agenter gör dubbelt arbete
- **Konflikter** — Agenter motarbetar varandra
- **Deadlocks** — Agenter väntar på varandra i evighet
- **Kaos** — Svårt att förstå vad som händer

Denna modul ger dig battle-tested patterns för agent orchestration.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Implementera conversation flow patterns
- ✅ Hantera agent consensus och konfliktlösning
- ✅ Bygga supervisor patterns för oversight
- ✅ Designa failover och recovery mechanisms
- ✅ Monitorera multi-agent systems

## Kärnkoncept

### Orchestration Patterns

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  ORCHESTRATION PATTERNS                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. ROUND ROBIN                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │       ┌───► Agent A ───┐                                             │   │
│  │       │                │                                             │   │
│  │  Task ┼───► Agent B ───┼──► Next Task                               │   │
│  │       │                │                                             │   │
│  │       └───► Agent C ───┘                                             │   │
│  │                                                                      │   │
│  │  Use when: All agents have same capabilities, load balancing        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  2. CAPABILITY-BASED ROUTING                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                  ┌─────────────────┐                                 │   │
│  │                  │     Router      │                                 │   │
│  │                  │  (LLM-based)    │                                 │   │
│  │                  └────────┬────────┘                                 │   │
│  │                           │                                          │   │
│  │         "code task" ──────┼────► Code Agent                         │   │
│  │         "test task" ──────┼────► Test Agent                         │   │
│  │         "deploy task" ────┼────► DevOps Agent                       │   │
│  │                                                                      │   │
│  │  Use when: Agents have different specialties                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  3. SUPERVISOR                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                  ┌─────────────────┐                                 │   │
│  │                  │   Supervisor    │                                 │   │
│  │                  │  (Monitors all) │                                 │   │
│  │                  └────────┬────────┘                                 │   │
│  │                           │ Watches                                  │   │
│  │         ┌─────────────────┼─────────────────┐                       │   │
│  │         ▼                 ▼                 ▼                        │   │
│  │    ┌─────────┐       ┌─────────┐       ┌─────────┐                  │   │
│  │    │ Agent A │       │ Agent B │       │ Agent C │                  │   │
│  │    └─────────┘       └─────────┘       └─────────┘                  │   │
│  │                                                                      │   │
│  │  Supervisor kan:                                                     │   │
│  │  • Stoppa runaway agents                                            │   │
│  │  • Redistribute work                                                │   │
│  │  • Intervene on conflicts                                           │   │
│  │  • Ensure quality                                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  4. CONSENSUS                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │     Agent A ───┐                                                     │   │
│  │                │      ┌───────────────┐                              │   │
│  │     Agent B ───┼────► │   Consensus   │ ────► Final Decision        │   │
│  │                │      │   Algorithm   │                              │   │
│  │     Agent C ───┘      └───────────────┘                              │   │
│  │                                                                      │   │
│  │  Consensus types:                                                   │   │
│  │  • Voting (majority wins)                                           │   │
│  │  • Weighted voting (some agents count more)                         │   │
│  │  • Debate until agreement                                           │   │
│  │  • Leader decides after hearing all                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera Orchestration

### 1. Capability-Based Router

```python
from openai import OpenAI
from dataclasses import dataclass
from typing import Optional

@dataclass
class AgentCapability:
    agent_id: str
    name: str
    capabilities: list[str]
    description: str

class CapabilityRouter:
    \"\"\"Routes tasks to the most capable agent.\"\"\"

    def __init__(self):
        self.client = OpenAI()
        self.agents: dict[str, AgentCapability] = {}

    def register(self, capability: AgentCapability):
        self.agents[capability.agent_id] = capability

    async def route(self, task: str) -> str:
        \"\"\"Select the best agent for a task.\"\"\"
        agents_desc = "\\n".join([
            f"- {a.name} ({a.agent_id}): {a.description}. "
            f"Capabilities: {', '.join(a.capabilities)}"
            for a in self.agents.values()
        ])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f\"\"\"
                Select the best agent for the given task.
                Return only the agent_id.

                Available agents:
                {agents_desc}
                \"\"\"},
                {"role": "user", "content": task}
            ]
        )

        selected = response.choices[0].message.content.strip()

        # Validate selection
        if selected not in self.agents:
            # Fallback to keyword matching
            for agent in self.agents.values():
                for cap in agent.capabilities:
                    if cap.lower() in task.lower():
                        return agent.agent_id
            return list(self.agents.keys())[0]

        return selected

# Usage
router = CapabilityRouter()

router.register(AgentCapability(
    agent_id="coder",
    name="Code Expert",
    capabilities=["python", "javascript", "code review"],
    description="Writes and reviews code"
))

router.register(AgentCapability(
    agent_id="devops",
    name="DevOps Engineer",
    capabilities=["kubernetes", "docker", "ci/cd", "deployment"],
    description="Handles infrastructure and deployments"
))

router.register(AgentCapability(
    agent_id="security",
    name="Security Specialist",
    capabilities=["security audit", "vulnerabilities", "compliance"],
    description="Reviews security aspects"
))

# Route a task
selected_agent = await router.route("Deploy the new version to production")
print(f"Selected: {selected_agent}")  # "devops"
```

### 2. Supervisor Pattern

```python
import asyncio
from dataclasses import dataclass
from datetime import datetime
from typing import Callable

@dataclass
class AgentStatus:
    agent_id: str
    state: str  # "idle", "working", "stuck", "error"
    current_task: Optional[str] = None
    started_at: Optional[datetime] = None
    last_activity: datetime = None

class Supervisor:
    \"\"\"Monitors and manages worker agents.\"\"\"

    def __init__(self,
                 max_task_duration: float = 60.0,
                 health_check_interval: float = 5.0):
        self.agents: dict[str, BaseAgent] = {}
        self.status: dict[str, AgentStatus] = {}
        self.max_task_duration = max_task_duration
        self.health_check_interval = health_check_interval
        self._running = False

    def register(self, agent: BaseAgent):
        self.agents[agent.agent_id] = agent
        self.status[agent.agent_id] = AgentStatus(
            agent_id=agent.agent_id,
            state="idle",
            last_activity=datetime.now()
        )

    async def assign_task(self, agent_id: str, task: str):
        \"\"\"Assign a task to an agent.\"\"\"
        if agent_id not in self.agents:
            raise ValueError(f"Unknown agent: {agent_id}")

        self.status[agent_id] = AgentStatus(
            agent_id=agent_id,
            state="working",
            current_task=task,
            started_at=datetime.now(),
            last_activity=datetime.now()
        )

        # Send task to agent
        await self.agents[agent_id].inbox.put(Message(
            sender="supervisor",
            receiver=agent_id,
            content=task,
            message_type="request"
        ))

    async def health_check_loop(self):
        \"\"\"Periodically check agent health.\"\"\"
        while self._running:
            await asyncio.sleep(self.health_check_interval)

            for agent_id, status in self.status.items():
                if status.state == "working" and status.started_at:
                    duration = (datetime.now() - status.started_at).total_seconds()

                    if duration > self.max_task_duration:
                        print(f"⚠️ Agent {agent_id} stuck on task for {duration:.0f}s")
                        await self._handle_stuck_agent(agent_id)

    async def _handle_stuck_agent(self, agent_id: str):
        \"\"\"Handle a stuck agent.\"\"\"
        print(f"🔧 Attempting to recover agent {agent_id}")

        # Option 1: Cancel and reassign
        status = self.status[agent_id]
        task = status.current_task

        # Stop the agent
        self.agents[agent_id].stop()

        # Mark as error
        self.status[agent_id].state = "error"

        # Find another agent to take over
        for other_id, other_agent in self.agents.items():
            if other_id != agent_id and self.status[other_id].state == "idle":
                print(f"📤 Reassigning task to {other_id}")
                await self.assign_task(other_id, task)
                return

        print(f"❌ No available agents to take over task")

    def report_completion(self, agent_id: str, result: Any):
        \"\"\"Agent reports task completion.\"\"\"
        self.status[agent_id] = AgentStatus(
            agent_id=agent_id,
            state="idle",
            last_activity=datetime.now()
        )
        print(f"✅ Agent {agent_id} completed task")

    async def run(self, router: MessageRouter):
        \"\"\"Run supervisor alongside agents.\"\"\"
        self._running = True

        # Start all agents
        agent_tasks = [
            asyncio.create_task(agent.run(router))
            for agent in self.agents.values()
        ]

        # Start health check
        health_task = asyncio.create_task(self.health_check_loop())

        await asyncio.gather(*agent_tasks, health_task)
```

### 3. Consensus Algorithm

```python
from enum import Enum

class ConsensusType(Enum):
    MAJORITY_VOTE = "majority"
    WEIGHTED_VOTE = "weighted"
    UNANIMOUS = "unanimous"
    LEADER_DECIDES = "leader"

@dataclass
class Vote:
    agent_id: str
    decision: str
    confidence: float
    reasoning: str

class ConsensusEngine:
    \"\"\"Reach consensus among agents.\"\"\"

    def __init__(self, consensus_type: ConsensusType = ConsensusType.MAJORITY_VOTE):
        self.consensus_type = consensus_type
        self.weights: dict[str, float] = {}
        self.leader: Optional[str] = None

    def set_weight(self, agent_id: str, weight: float):
        self.weights[agent_id] = weight

    def set_leader(self, agent_id: str):
        self.leader = agent_id

    def reach_consensus(self, votes: list[Vote]) -> tuple[str, float]:
        \"\"\"Determine consensus from votes.\"\"\"
        if not votes:
            raise ValueError("No votes to process")

        if self.consensus_type == ConsensusType.MAJORITY_VOTE:
            return self._majority_vote(votes)
        elif self.consensus_type == ConsensusType.WEIGHTED_VOTE:
            return self._weighted_vote(votes)
        elif self.consensus_type == ConsensusType.UNANIMOUS:
            return self._unanimous_vote(votes)
        elif self.consensus_type == ConsensusType.LEADER_DECIDES:
            return self._leader_decides(votes)

    def _majority_vote(self, votes: list[Vote]) -> tuple[str, float]:
        from collections import Counter
        decisions = [v.decision for v in votes]
        counter = Counter(decisions)
        winner, count = counter.most_common(1)[0]
        confidence = count / len(votes)
        return winner, confidence

    def _weighted_vote(self, votes: list[Vote]) -> tuple[str, float]:
        scores: dict[str, float] = {}
        total_weight = 0

        for vote in votes:
            weight = self.weights.get(vote.agent_id, 1.0)
            weighted_score = weight * vote.confidence

            if vote.decision not in scores:
                scores[vote.decision] = 0
            scores[vote.decision] += weighted_score
            total_weight += weight

        winner = max(scores, key=scores.get)
        confidence = scores[winner] / total_weight
        return winner, confidence

    def _unanimous_vote(self, votes: list[Vote]) -> tuple[str, float]:
        decisions = set(v.decision for v in votes)
        if len(decisions) == 1:
            return list(decisions)[0], 1.0
        else:
            # No consensus
            return "NO_CONSENSUS", 0.0

    def _leader_decides(self, votes: list[Vote]) -> tuple[str, float]:
        if not self.leader:
            raise ValueError("No leader set")

        for vote in votes:
            if vote.agent_id == self.leader:
                return vote.decision, vote.confidence

        raise ValueError("Leader did not vote")


class ConsensusOrchestrator:
    \"\"\"Orchestrate agents to reach consensus.\"\"\"

    def __init__(self, agents: list[BaseAgent], engine: ConsensusEngine):
        self.agents = {a.agent_id: a for a in agents}
        self.engine = engine
        self.client = OpenAI()

    async def deliberate(self, question: str, max_rounds: int = 3) -> dict:
        \"\"\"Run deliberation until consensus or max rounds.\"\"\"
        round_num = 0
        history = []

        while round_num < max_rounds:
            round_num += 1

            # Collect votes from all agents
            votes = await self._collect_votes(question, history)
            history.append({"round": round_num, "votes": votes})

            # Check for consensus
            decision, confidence = self.engine.reach_consensus(votes)

            if confidence >= 0.8:  # Strong consensus
                return {
                    "decision": decision,
                    "confidence": confidence,
                    "rounds": round_num,
                    "history": history
                }

            # If no consensus, share reasoning for next round
            print(f"Round {round_num}: No consensus (confidence={confidence:.2f})")

        # Return best effort after max rounds
        return {
            "decision": decision,
            "confidence": confidence,
            "rounds": max_rounds,
            "note": "Max rounds reached without strong consensus",
            "history": history
        }

    async def _collect_votes(self, question: str, history: list) -> list[Vote]:
        \"\"\"Collect votes from all agents.\"\"\"
        votes = []

        history_context = ""
        if history:
            last_round = history[-1]
            history_context = "\\n\\nPrevious round votes:\\n" + "\\n".join([
                f"- {v.agent_id}: {v.decision} ({v.reasoning})"
                for v in last_round["votes"]
            ])

        for agent_id, agent in self.agents.items():
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f\"\"\"
                    You are {agent_id}. Vote on the question.
                    Return JSON: {{"decision": "...", "confidence": 0.0-1.0, "reasoning": "..."}}
                    \"\"\"},
                    {"role": "user", "content": f"Question: {question}{history_context}"}
                ]
            )

            import json
            vote_data = json.loads(response.choices[0].message.content)

            votes.append(Vote(
                agent_id=agent_id,
                decision=vote_data["decision"],
                confidence=vote_data["confidence"],
                reasoning=vote_data["reasoning"]
            ))

        return votes
```

### 4. Complete DevOps Team Example

```python
class DevOpsTeam:
    \"\"\"Complete multi-agent DevOps team.\"\"\"

    def __init__(self):
        self.router = MessageRouter()
        self.supervisor = Supervisor(max_task_duration=120)

        # Create specialized agents
        self.architect = WorkerAgent("architect", "system architecture")
        self.coder = WorkerAgent("coder", "python programming")
        self.tester = WorkerAgent("tester", "testing and QA")
        self.devops = WorkerAgent("devops", "kubernetes and deployment")
        self.security = WorkerAgent("security", "security review")

        # Register all
        for agent in [self.architect, self.coder, self.tester,
                      self.devops, self.security]:
            self.router.register(agent)
            self.supervisor.register(agent)

        # Setup capability router
        self.capability_router = CapabilityRouter()
        self.capability_router.register(AgentCapability(
            "architect", "Architect",
            ["design", "architecture", "planning"],
            "Designs system architecture"
        ))
        self.capability_router.register(AgentCapability(
            "coder", "Developer",
            ["code", "python", "implement"],
            "Writes code"
        ))
        self.capability_router.register(AgentCapability(
            "tester", "QA Engineer",
            ["test", "qa", "verify"],
            "Tests code"
        ))
        self.capability_router.register(AgentCapability(
            "devops", "DevOps Engineer",
            ["deploy", "kubernetes", "infrastructure"],
            "Handles deployments"
        ))
        self.capability_router.register(AgentCapability(
            "security", "Security Expert",
            ["security", "audit", "vulnerabilities"],
            "Reviews security"
        ))

    async def handle_request(self, request: str) -> dict:
        \"\"\"Handle a user request using the team.\"\"\"
        # Route to appropriate agent
        agent_id = await self.capability_router.route(request)
        print(f"🎯 Routing to: {agent_id}")

        # Assign task
        await self.supervisor.assign_task(agent_id, request)

        # Wait for completion (simplified)
        # In real impl: wait for response message
        await asyncio.sleep(5)

        return {"status": "complete", "assigned_to": agent_id}

    async def run(self):
        await self.supervisor.run(self.router)

# Usage
team = DevOpsTeam()
result = await team.handle_request("Deploy auth-service to production with security review")
```

## Praktisk övning

**Uppgift:** Lägg till Code Review Pipeline

```python
\"\"\"
TODO: Utöka DevOpsTeam med en code review pipeline:

1. Coder skriver kod
2. Reviewer granskar (kan vara flera)
3. Security gör security review
4. Om alla godkänner -> merge
5. Om någon underkänner -> tillbaka till coder

Implementera:
- ReviewPipeline klass
- Voting/consensus för godkännande
- Feedback loop till coder
- Max 3 review rounds
\"\"\"

class ReviewPipeline:
    def __init__(self, team: DevOpsTeam):
        # Din kod här
        pass

    async def submit_for_review(self, code: str) -> dict:
        # Din kod här
        pass

# Test
pipeline = ReviewPipeline(team)
result = await pipeline.submit_for_review("def hello(): print('world')")
```

## Sammanfattning

- ✅ **Capability routing** för smart task assignment
- ✅ **Supervisor** för monitoring och recovery
- ✅ **Consensus** för group decisions
- ✅ **Complete teams** kombinerar alla patterns

## Nästa steg

- **Node 17:** Production Deployment
- **Node 18:** Monitoring & Observability

---
*Pro tip: Börja med supervisor pattern — det löser de flesta problemen!*
"""
    }
]
