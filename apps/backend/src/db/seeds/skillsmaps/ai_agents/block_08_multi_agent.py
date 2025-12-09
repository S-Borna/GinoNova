# =============================================================================
# AI AGENTS - BLOCK 08: MULTI-AGENT (Noder 15-16) - V3 FORMAT
# =============================================================================

NODE_15_MULTI_AGENT_DESIGN = {
    "node_id": 15,
    "title": "Multi-Agent Design",
    "slug": "multi-agent-design",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [14],
    "content": '''
# Multi-Agent Design

Designa system dar flera agenter samarbetar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Multi-Agent Systems?

Multi-agent systems bestar av flera specialiserade agenter som samarbetar for att losa komplexa uppgifter.

| Pattern | Beskrivning |
|---------|-------------|
| Sequential | Agenter i kedja |
| Parallel | Samtidig exekvering |
| Hierarchical | Manager-worker |
| Collaborative | Peer-to-peer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Specialisering | Varje agent expert pa sitt |
| Skalbarhet | Lagg till fler agenter |
| Redundans | Backup om en agent failar |
| Parallellism | Snabbare exekvering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Multi-Agent Patterns

| Pattern | Bast for | Komplexitet |
|---------|----------|-------------|
| Pipeline | Sekventiella tasks | Lag |
| Fan-out/in | Parallella subtasks | Medium |
| Supervisor | Komplexa workflows | Hog |
| Debate | Kritisk analys | Medium |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multi-Agent Patterns

```
┌─────────────────────────────────────────────────────────────────┐
│                  MULTI-AGENT PATTERNS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PIPELINE (Sequential)        FAN-OUT/FAN-IN (Parallel)         │
│  ┌─────┐  ┌─────┐  ┌─────┐   ┌─────┐                           │
│  │  A  │─>│  B  │─>│  C  │   │  A  │                            │
│  └─────┘  └─────┘  └─────┘   └──┬──┘                            │
│                                 │                                │
│                          ┌──────┼──────┐                        │
│                          v      v      v                         │
│                       ┌────┐ ┌────┐ ┌────┐                      │
│                       │ B1 │ │ B2 │ │ B3 │                      │
│                       └──┬─┘ └──┬─┘ └──┬─┘                      │
│                          │      │      │                         │
│                          └──────┼──────┘                        │
│                                 v                                │
│                              ┌─────┐                            │
│                              │  C  │                            │
│                              └─────┘                            │
│                                                                  │
│  SUPERVISOR (Hierarchical)    DEBATE (Collaborative)           │
│       ┌─────────┐                ┌─────┐                        │
│       │SUPERVISOR│               │Judge│                        │
│       └────┬────┘                └──┬──┘                        │
│            │                       │                             │
│    ┌───────┼───────┐           ┌───┴───┐                        │
│    v       v       v           v       v                         │
│ ┌────┐ ┌────┐ ┌────┐      ┌────┐   ┌────┐                      │
│ │ W1 │ │ W2 │ │ W3 │      │Pro │<->│Con │                      │
│ └────┘ └────┘ └────┘      └────┘   └────┘                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Agent Definition

```python
from dataclasses import dataclass
from typing import Callable, Any, Protocol
from abc import ABC, abstractmethod

@dataclass
class AgentConfig:
    name: str
    role: str
    system_prompt: str
    tools: list = None
    model: str = "gpt-4o-mini"

class BaseAgent(ABC):
    """Base class for all agents."""

    def __init__(self, config: AgentConfig, client):
        self.config = config
        self.client = client

    @abstractmethod
    def run(self, input_data: dict) -> dict:
        pass

    def _call_llm(self, messages: list) -> str:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {"role": "system", "content": self.config.system_prompt},
                *messages
            ]
        )
        return response.choices[0].message.content

class SimpleAgent(BaseAgent):
    """Enkel agent utan tools."""

    def run(self, input_data: dict) -> dict:
        result = self._call_llm([
            {"role": "user", "content": input_data.get("message", "")}
        ])
        return {"output": result, "agent": self.config.name}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pipeline Pattern

```python
class Pipeline:
    """Sequential agent pipeline."""

    def __init__(self, agents: list[BaseAgent]):
        self.agents = agents

    def run(self, initial_input: dict) -> dict:
        current_data = initial_input
        results = []

        for agent in self.agents:
            result = agent.run(current_data)
            results.append(result)

            # Naesta agent far output fran foregalende
            current_data = {
                "message": result["output"],
                "previous_agent": result["agent"]
            }

        return {
            "final_output": results[-1]["output"],
            "pipeline_results": results
        }

# Exempel: Analys-pipeline
researcher = SimpleAgent(AgentConfig(
    name="researcher",
    role="Forskare",
    system_prompt="Du ar en forskare. Samla fakta om amnet."
))

analyst = SimpleAgent(AgentConfig(
    name="analyst",
    role="Analytiker",
    system_prompt="Du ar en analytiker. Analysera informationen."
))

writer = SimpleAgent(AgentConfig(
    name="writer",
    role="Skribent",
    system_prompt="Du ar en skribent. Skriv en sammanfattning."
))

pipeline = Pipeline([researcher, analyst, writer])
result = pipeline.run({"message": "Undersok AI i DevOps"})
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Fan-Out/Fan-In Pattern

```python
import asyncio
from typing import List

class FanOutFanIn:
    """Parallel agent execution with aggregation."""

    def __init__(self, fan_out_agents: list[BaseAgent], aggregator: BaseAgent):
        self.fan_out_agents = fan_out_agents
        self.aggregator = aggregator

    async def run(self, input_data: dict) -> dict:
        # Fan-out: Kor alla agenter parallellt
        tasks = [
            asyncio.to_thread(agent.run, input_data)
            for agent in self.fan_out_agents
        ]
        parallel_results = await asyncio.gather(*tasks)

        # Fan-in: Aggregera resultat
        combined = "\n\n".join([
            f"[{r['agent']}]: {r['output']}"
            for r in parallel_results
        ])

        final_result = self.aggregator.run({
            "message": f"Sammanfatta dessa perspektiv:\n{combined}"
        })

        return {
            "parallel_results": parallel_results,
            "final_output": final_result["output"]
        }

# Exempel: Olika perspektiv
technical = SimpleAgent(AgentConfig(
    name="technical",
    role="Tekniker",
    system_prompt="Analysera fran tekniskt perspektiv."
))

business = SimpleAgent(AgentConfig(
    name="business",
    role="Affar",
    system_prompt="Analysera fran affarsperspektiv."
))

security = SimpleAgent(AgentConfig(
    name="security",
    role="Sakerhet",
    system_prompt="Analysera fran sakerhetsperspektiv."
))

aggregator = SimpleAgent(AgentConfig(
    name="aggregator",
    role="Sammanfattare",
    system_prompt="Syntetisera olika perspektiv till en helhetsbild."
))

fan_system = FanOutFanIn([technical, business, security], aggregator)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Supervisor Pattern

```python
class Supervisor:
    """Supervisor som delegerar till workers."""

    def __init__(self, supervisor_agent: BaseAgent, workers: dict[str, BaseAgent]):
        self.supervisor = supervisor_agent
        self.workers = workers

    def run(self, task: str, max_rounds: int = 5) -> dict:
        context = []

        for round_num in range(max_rounds):
            decision = self._get_supervisor_decision(task, context)

            if decision["action"] == "COMPLETE":
                return {
                    "output": decision.get("final_answer", ""),
                    "rounds": round_num + 1,
                    "context": context
                }

            worker_name = decision.get("delegate_to")
            if worker_name and worker_name in self.workers:
                worker_result = self.workers[worker_name].run({
                    "message": decision.get("instruction", task)
                })
                context.append({
                    "worker": worker_name,
                    "result": worker_result["output"]
                })

        return {"output": "Max rounds reached", "context": context}

    def _get_supervisor_decision(self, task: str, context: list) -> dict:
        context_str = "\n".join([
            f"{c['worker']}: {c['result']}" for c in context
        ])

        prompt = f"""
        Task: {task}

        Tidigare resultat:
        {context_str}

        Tillgangliga workers: {list(self.workers.keys())}

        Beslut (JSON):
        {{"action": "DELEGATE|COMPLETE", "delegate_to": "worker_name", "instruction": "...", "final_answer": "..."}}
        """

        response = self.supervisor._call_llm([{"role": "user", "content": prompt}])
        import json
        return json.loads(response)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Debate Pattern

```python
class DebateSystem:
    """Tva agenter debatterar, en tredje domare."""

    def __init__(self, pro_agent: BaseAgent, con_agent: BaseAgent, judge: BaseAgent):
        self.pro = pro_agent
        self.con = con_agent
        self.judge = judge

    def run(self, topic: str, rounds: int = 3) -> dict:
        debate_history = []

        for round_num in range(rounds):
            # Pro argument
            pro_context = self._format_history(debate_history, "pro")
            pro_arg = self.pro.run({
                "message": f"Amma: {topic}\n\nTidigare:\n{pro_context}\n\nGe ditt argument."
            })
            debate_history.append({"side": "pro", "content": pro_arg["output"]})

            # Con argument
            con_context = self._format_history(debate_history, "con")
            con_arg = self.con.run({
                "message": f"Amma: {topic}\n\nTidigare:\n{con_context}\n\nBemot och argumentera."
            })
            debate_history.append({"side": "con", "content": con_arg["output"]})

        # Judge decision
        full_debate = self._format_history(debate_history, "all")
        verdict = self.judge.run({
            "message": f"Amma: {topic}\n\nDebatt:\n{full_debate}\n\nGe din dom."
        })

        return {
            "debate": debate_history,
            "verdict": verdict["output"]
        }
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Kommunikationsfel | Inkonsistent format | Standardisera message format |
| Oandlig loop | Ingen termination | Max rounds |
| Token overflow | Lang historik | Sammanfatta kontext |
| Langsam | Sequential i onadan | Anvand parallel |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Pattern | Anvandning |
|---------|------------|
| Pipeline | Sekventiell processing |
| Fan-out/in | Parallella perspektiv |
| Supervisor | Dynamisk delegering |
| Debate | Kritisk analys |

Kom ihag:
- Valj pattern baserat pa uppgiften
- Standardisera kommunikationsformat
- Implementera timeout och max rounds
- Logga all agent-kommunikation
'''
}

NODE_16_ORCHESTRATION = {
    "node_id": 16,
    "title": "Agent Orchestration",
    "slug": "agent-orchestration",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [15],
    "content": '''
# Agent Orchestration

Avancerad koordinering av multi-agent system.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Agent Orchestration?

Orchestration ar processen att koordinera, schemalägga och hantera flera agenter for att uppna komplexa mal.

| Komponent | Funktion |
|-----------|----------|
| Scheduler | Bestammer ordning |
| Router | Dirigerar meddelanden |
| Monitor | Overvakar hälsa |
| Recovery | Hanterar fel |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Kontroll | Centraliserad hantering |
| Skalbarhet | Dynamisk agent-allokering |
| Resiliens | Automatisk felhantering |
| Observability | Full insyn i systemet |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Orchestration Components

| Komponent | Implementation | Ansvar |
|-----------|----------------|--------|
| Message Queue | Redis/RabbitMQ | Kommunikation |
| Scheduler | Celery/Custom | Timing |
| Registry | Dict/DB | Agent tracking |
| Monitor | Prometheus | Metrics |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Orchestration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  ORCHESTRATION SYSTEM                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    ORCHESTRATOR                            │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐      │ │
│  │  │Scheduler│  │ Router  │  │ Monitor │  │Recovery │      │ │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘      │ │
│  └───────────────────────────────────────────────────────────┘ │
│                           │                                      │
│                           v                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                   MESSAGE QUEUE                            │ │
│  └───────────────────────────────────────────────────────────┘ │
│           │           │           │           │                  │
│           v           v           v           v                  │
│       ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐             │
│       │Agent1│    │Agent2│    │Agent3│    │AgentN│             │
│       └──────┘    └──────┘    └──────┘    └──────┘             │
│           │           │           │           │                  │
│           └───────────┴───────────┴───────────┘                 │
│                           │                                      │
│                           v                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                   RESULT STORE                             │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Agent Registry

```python
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enum import Enum

class AgentStatus(Enum):
    IDLE = "idle"
    BUSY = "busy"
    ERROR = "error"
    OFFLINE = "offline"

@dataclass
class RegisteredAgent:
    agent: BaseAgent
    status: AgentStatus = AgentStatus.IDLE
    current_task: Optional[str] = None
    last_heartbeat: datetime = field(default_factory=datetime.now)
    tasks_completed: int = 0
    errors: int = 0

class AgentRegistry:
    """Central registry for all agents."""

    def __init__(self):
        self.agents: dict[str, RegisteredAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self.agents[agent.config.name] = RegisteredAgent(agent=agent)

    def unregister(self, name: str) -> None:
        if name in self.agents:
            del self.agents[name]

    def get_available(self, role: str = None) -> list[RegisteredAgent]:
        available = [
            a for a in self.agents.values()
            if a.status == AgentStatus.IDLE
        ]
        if role:
            available = [a for a in available if a.agent.config.role == role]
        return available

    def update_status(self, name: str, status: AgentStatus, task: str = None) -> None:
        if name in self.agents:
            self.agents[name].status = status
            self.agents[name].current_task = task
            self.agents[name].last_heartbeat = datetime.now()

    def get_stats(self) -> dict:
        return {
            "total": len(self.agents),
            "idle": len([a for a in self.agents.values() if a.status == AgentStatus.IDLE]),
            "busy": len([a for a in self.agents.values() if a.status == AgentStatus.BUSY]),
            "error": len([a for a in self.agents.values() if a.status == AgentStatus.ERROR])
        }
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Message Router

```python
from dataclasses import dataclass
from typing import Any
import asyncio
from collections import defaultdict

@dataclass
class Message:
    sender: str
    recipient: str
    content: Any
    message_type: str = "task"
    priority: int = 0
    timestamp: datetime = field(default_factory=datetime.now)

class MessageRouter:
    """Routes messages between agents."""

    def __init__(self):
        self.queues: dict[str, asyncio.Queue] = defaultdict(asyncio.Queue)
        self.broadcast_subscribers: dict[str, list[str]] = defaultdict(list)

    async def send(self, message: Message) -> None:
        await self.queues[message.recipient].put(message)

    async def broadcast(self, channel: str, message: Message) -> None:
        for subscriber in self.broadcast_subscribers[channel]:
            msg = Message(
                sender=message.sender,
                recipient=subscriber,
                content=message.content,
                message_type="broadcast"
            )
            await self.send(msg)

    def subscribe(self, agent_name: str, channel: str) -> None:
        self.broadcast_subscribers[channel].append(agent_name)

    async def receive(self, agent_name: str, timeout: float = None) -> Optional[Message]:
        try:
            if timeout:
                return await asyncio.wait_for(
                    self.queues[agent_name].get(),
                    timeout=timeout
                )
            return await self.queues[agent_name].get()
        except asyncio.TimeoutError:
            return None
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Task Scheduler

```python
from dataclasses import dataclass
from typing import Callable
import heapq
from datetime import datetime

@dataclass
class ScheduledTask:
    task_id: str
    agent_name: str
    input_data: dict
    priority: int = 0
    scheduled_time: datetime = field(default_factory=datetime.now)
    dependencies: list[str] = field(default_factory=list)

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority > other.priority  # Hogre prioritet forst
        return self.scheduled_time < other.scheduled_time

class TaskScheduler:
    """Schedules and manages task execution."""

    def __init__(self, registry: AgentRegistry, router: MessageRouter):
        self.registry = registry
        self.router = router
        self.pending_tasks: list[ScheduledTask] = []
        self.completed_tasks: dict[str, Any] = {}
        self.running_tasks: dict[str, ScheduledTask] = {}

    def schedule(self, task: ScheduledTask) -> None:
        heapq.heappush(self.pending_tasks, task)

    async def run(self) -> None:
        while self.pending_tasks or self.running_tasks:
            # Kolla dependencies
            ready_tasks = [
                t for t in self.pending_tasks
                if all(d in self.completed_tasks for d in t.dependencies)
            ]

            for task in ready_tasks:
                agent = self._get_available_agent(task.agent_name)
                if agent:
                    self.pending_tasks.remove(task)
                    self.running_tasks[task.task_id] = task

                    await self.router.send(Message(
                        sender="scheduler",
                        recipient=agent.agent.config.name,
                        content=task.input_data,
                        message_type="task"
                    ))

                    self.registry.update_status(
                        agent.agent.config.name,
                        AgentStatus.BUSY,
                        task.task_id
                    )

            await asyncio.sleep(0.1)

    def _get_available_agent(self, preferred: str = None) -> Optional[RegisteredAgent]:
        if preferred:
            agent = self.registry.agents.get(preferred)
            if agent and agent.status == AgentStatus.IDLE:
                return agent

        available = self.registry.get_available()
        return available[0] if available else None
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Orchestrator

```python
class Orchestrator:
    """Central orchestrator for multi-agent system."""

    def __init__(self, client):
        self.client = client
        self.registry = AgentRegistry()
        self.router = MessageRouter()
        self.scheduler = TaskScheduler(self.registry, self.router)
        self.results = {}

    def add_agent(self, config: AgentConfig) -> None:
        agent = SimpleAgent(config, self.client)
        self.registry.register(agent)

    async def execute_workflow(self, workflow: dict) -> dict:
        # Skapa tasks fran workflow
        for step in workflow["steps"]:
            task = ScheduledTask(
                task_id=step["id"],
                agent_name=step["agent"],
                input_data=step["input"],
                priority=step.get("priority", 0),
                dependencies=step.get("depends_on", [])
            )
            self.scheduler.schedule(task)

        # Starta agent workers
        agent_tasks = [
            self._run_agent_loop(name)
            for name in self.registry.agents.keys()
        ]

        # Kor scheduler och agents
        await asyncio.gather(
            self.scheduler.run(),
            *agent_tasks
        )

        return self.results

    async def _run_agent_loop(self, agent_name: str) -> None:
        while True:
            message = await self.router.receive(agent_name, timeout=5.0)
            if not message:
                if not self.scheduler.pending_tasks:
                    break
                continue

            agent = self.registry.agents[agent_name].agent
            result = agent.run(message.content)

            self.results[message.content.get("task_id", agent_name)] = result
            self.scheduler.completed_tasks[message.content.get("task_id", "")] = result

            self.registry.update_status(agent_name, AgentStatus.IDLE)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Deadlock | Cirkulara dependencies | Dependency validation |
| Starvation | Priority inversion | Fair scheduling |
| Message loss | Ingen persistence | Message queue |
| Zombie tasks | Ingen timeout | Task timeout |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Registry | Central agent management |
| Router | Message-based communication |
| Scheduler | Dependency-aware execution |
| Orchestrator | Koordinerar hela systemet |

Kom ihag:
- Registry for att spara agent-tillstand
- Async router for skalbarhet
- Scheduler med dependency handling
- Monitorering ar kritiskt
'''
}

BLOCK_08_NODES = [NODE_15_MULTI_AGENT_DESIGN, NODE_16_ORCHESTRATION]
