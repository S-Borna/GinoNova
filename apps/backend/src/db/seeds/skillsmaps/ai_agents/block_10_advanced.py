# =============================================================================
# AI AGENTS - BLOCK 10: ADVANCED (Noder 19-20) - V3 FORMAT
# =============================================================================

NODE_19_AUTONOMOUS_AGENTS = {
    "node_id": 19,
    "title": "Autonoma Agenter",
    "slug": "autonomous-agents",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [18],
    "content": '''
# Autonoma Agenter

Bygga agenter som arbetar sjalvstandigt.

------------------------------------------------------------

## Vad ar Autonoma Agenter?

Autonoma agenter arbetar sjalvstandigt mot mal utan konstant manniskointeraktion. De planerar, utfor och anpassar sig.

| Egenskap | Beskrivning |
|----------|-------------|
| Self-direction | Bestammer egna steg |
| Persistence | Fortsatter over tid |
| Learning | Anpassar sig fran feedback |
| Goal-oriented | Arbetar mot definierade mal |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Automation | Handsfree operations |
| Efficiency | 24/7 arbete utan trotthet |
| Scale | Hantera manga tasks |
| Consistency | Samma kvalitet varje gang |

------------------------------------------------------------

## Snabbreferens - Autonomy Levels

| Level | Beskrivning | Exempel |
|-------|-------------|---------|
| Level 1 | Tool use | ChatGPT med plugins |
| Level 2 | Task completion | Simple agents |
| Level 3 | Multi-step planning | AutoGPT-style |
| Level 4 | Self-improvement | Research frontier |

------------------------------------------------------------

## Autonomous Agent Architecture

```
+-----------------------------------------------------------------+
|                  AUTONOMOUS AGENT                                |
+-----------------------------------------------------------------+
|                                                                  |
|  +-----------------------------------------------------------+ |
|  |                    GOAL SYSTEM                             | |
|  |  - Long-term goals                                         | |
|  |  - Sub-goal decomposition                                  | |
|  |  - Priority management                                     | |
|  +-----------------------------------------------------------+ |
|                           |                                      |
|                           v                                      |
|  +-----------------------------------------------------------+ |
|  |                    PLANNING ENGINE                         | |
|  |  - Task breakdown                                          | |
|  |  - Dependency analysis                                     | |
|  |  - Resource estimation                                     | |
|  +-----------------------------------------------------------+ |
|                           |                                      |
|                           v                                      |
|  +-----------------------------------------------------------+ |
|  |                   EXECUTION ENGINE                         | |
|  |  - Tool execution                                          | |
|  |  - Progress tracking                                       | |
|  |  - Error recovery                                          | |
|  +-----------------------------------------------------------+ |
|                           |                                      |
|                           v                                      |
|  +-----------------------------------------------------------+ |
|  |                   LEARNING SYSTEM                          | |
|  |  - Reflection                                              | |
|  |  - Strategy adjustment                                     | |
|  |  - Knowledge accumulation                                  | |
|  +-----------------------------------------------------------+ |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Goal System

```python
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from datetime import datetime

class GoalStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"

@dataclass
class Goal:
    description: str
    priority: int = 0
    status: GoalStatus = GoalStatus.PENDING
    parent_goal: Optional[str] = None
    sub_goals: list[str] = field(default_factory=list)
    deadline: Optional[datetime] = None
    progress: float = 0.0

class GoalManager:
    """Manage hierarchical goals."""

    def __init__(self, client):
        self.client = client
        self.goals: dict[str, Goal] = {}

    def add_goal(self, goal_id: str, goal: Goal) -> None:
        self.goals[goal_id] = goal

        if goal.parent_goal and goal.parent_goal in self.goals:
            self.goals[goal.parent_goal].sub_goals.append(goal_id)

    def decompose_goal(self, goal_id: str) -> list[Goal]:
        goal = self.goals[goal_id]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Bryt ner detta mal i 3-5 konkreta sub-mal:
                {goal.description}

                Returnera JSON:
                {{"sub_goals": [{{"description": "...", "priority": 1-5}}]}}
                """
            }],
            response_format={"type": "json_object"}
        )

        import json
        data = json.loads(response.choices[0].message.content)

        sub_goals = []
        for i, sg in enumerate(data.get("sub_goals", [])):
            sub_goal = Goal(
                description=sg["description"],
                priority=sg.get("priority", goal.priority),
                parent_goal=goal_id
            )
            sub_goal_id = f"{goal_id}_sub_{i}"
            self.add_goal(sub_goal_id, sub_goal)
            sub_goals.append(sub_goal)

        return sub_goals

    def get_next_goal(self) -> Optional[tuple[str, Goal]]:
        pending = [
            (gid, g) for gid, g in self.goals.items()
            if g.status == GoalStatus.PENDING
            and all(
                self.goals[sg].status == GoalStatus.COMPLETED
                for sg in self.goals.get(g.parent_goal, Goal("")).sub_goals
                if sg != gid
            )
        ]

        if not pending:
            return None

        pending.sort(key=lambda x: x[1].priority, reverse=True)
        return pending[0]
```

------------------------------------------------------------

## Planning Engine

```python
@dataclass
class Plan:
    steps: list[dict]
    estimated_time: float
    resources_needed: list[str]
    risks: list[str]

class PlanningEngine:
    """Generate and manage execution plans."""

    def __init__(self, client, available_tools: list[str]):
        self.client = client
        self.available_tools = available_tools

    def create_plan(self, goal: Goal) -> Plan:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Skapa en plan for att uppna detta mal:
                {goal.description}

                Tillgangliga verktyg: {self.available_tools}

                Returnera JSON:
                {{
                    "steps": [
                        {{"action": "...", "tool": "...", "inputs": {{}}, "expected_output": "..."}}
                    ],
                    "estimated_minutes": N,
                    "resources": ["..."],
                    "risks": ["..."]
                }}
                """
            }],
            response_format={"type": "json_object"}
        )

        import json
        data = json.loads(response.choices[0].message.content)

        return Plan(
            steps=data.get("steps", []),
            estimated_time=data.get("estimated_minutes", 0),
            resources_needed=data.get("resources", []),
            risks=data.get("risks", [])
        )

    def replan(self, goal: Goal, failed_step: dict, error: str) -> Plan:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
                Omplanera efter fel:

                Mal: {goal.description}
                Misslyckat steg: {failed_step}
                Fel: {error}

                Returnera ny plan i samma JSON-format.
                """
            }],
            response_format={"type": "json_object"}
        )

        import json
        data = json.loads(response.choices[0].message.content)
        return Plan(
            steps=data.get("steps", []),
            estimated_time=data.get("estimated_minutes", 0),
            resources_needed=data.get("resources", []),
            risks=data.get("risks", [])
        )
```

------------------------------------------------------------

## Execution Engine

```python
import asyncio
from typing import Callable

class ExecutionEngine:
    """Execute plans with error handling and recovery."""

    def __init__(self, tool_executor: Callable, planner: PlanningEngine):
        self.tool_executor = tool_executor
        self.planner = planner
        self.execution_log = []

    async def execute_plan(self, goal: Goal, plan: Plan, max_retries: int = 3) -> dict:
        results = []

        for i, step in enumerate(plan.steps):
            retry_count = 0

            while retry_count < max_retries:
                try:
                    result = await self._execute_step(step)
                    results.append({"step": i, "result": result, "status": "success"})
                    self._log(f"Step {i} completed: {step['action']}")
                    break

                except Exception as e:
                    retry_count += 1
                    self._log(f"Step {i} failed (attempt {retry_count}): {e}")

                    if retry_count >= max_retries:
                        # Forsok omplanera
                        new_plan = self.planner.replan(goal, step, str(e))
                        return await self.execute_plan(goal, new_plan, max_retries=1)

                    await asyncio.sleep(2 ** retry_count)

        return {
            "status": "completed",
            "results": results,
            "log": self.execution_log
        }

    async def _execute_step(self, step: dict) -> dict:
        tool_name = step.get("tool")
        inputs = step.get("inputs", {})

        result = await asyncio.to_thread(
            self.tool_executor,
            tool_name,
            inputs
        )

        return result

    def _log(self, message: str) -> None:
        self.execution_log.append({
            "timestamp": datetime.now().isoformat(),
            "message": message
        })
```

------------------------------------------------------------

## Autonomous Agent

```python
class AutonomousAgent:
    """Fully autonomous agent with planning and learning."""

    def __init__(self, client, tools, tool_executor):
        self.client = client
        self.goal_manager = GoalManager(client)
        self.planner = PlanningEngine(client, list(tools.keys()))
        self.executor = ExecutionEngine(tool_executor, self.planner)
        self.knowledge_base = []
        self.running = False

    async def run(self, initial_goal: str, max_runtime_hours: float = 1.0) -> dict:
        start_time = datetime.now()
        max_runtime = timedelta(hours=max_runtime_hours)

        # Lagg till initial goal
        self.goal_manager.add_goal("main", Goal(description=initial_goal, priority=10))
        self.goal_manager.decompose_goal("main")

        self.running = True
        results = []

        while self.running:
            # Kolla timeout
            if datetime.now() - start_time > max_runtime:
                self._log("Max runtime reached")
                break

            # Hamta nasta goal
            next_item = self.goal_manager.get_next_goal()
            if not next_item:
                self._log("All goals completed")
                break

            goal_id, goal = next_item
            goal.status = GoalStatus.IN_PROGRESS

            # Planera och exekvera
            plan = self.planner.create_plan(goal)
            result = await self.executor.execute_plan(goal, plan)

            # Uppdatera status
            if result["status"] == "completed":
                goal.status = GoalStatus.COMPLETED
                goal.progress = 1.0
            else:
                goal.status = GoalStatus.FAILED

            results.append({
                "goal_id": goal_id,
                "goal": goal.description,
                "result": result
            })

            # Lardomar
            self._learn_from_execution(goal, result)

        return {
            "status": "completed",
            "results": results,
            "knowledge_gained": len(self.knowledge_base)
        }

    def _learn_from_execution(self, goal: Goal, result: dict) -> None:
        if result["status"] == "completed":
            self.knowledge_base.append({
                "goal_type": goal.description[:50],
                "successful_approach": result.get("results", [])
            })

    def stop(self) -> None:
        self.running = False
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Goal drift | Forlorar fokus | Regelbound goal review |
| Resource exhaustion | Ingen budget | Cost limits |
| Infinite loops | Datta planering | Max iterations |
| Unsafe actions | Ingen granskning | Human-in-the-loop |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Goal system | Hierarkiska mal med prioritet |
| Planning | Automatisk task breakdown |
| Execution | Robust med retries och replan |
| Learning | Ackumulera kunskap over tid |

Kom ihag:
- Satt alltid tidsgranser
- Implementera human-in-the-loop for kritiska beslut
- Logga allt for att forsta agentens beteende
- Borja med begransad autonomi
'''
}

NODE_20_FUTURE_AGENTS = {
    "node_id": 20,
    "title": "Framtidens AI-Agenter",
    "slug": "future-ai-agents",
    "estimated_minutes": 40,
    "xp_reward": 100,
    "prerequisites": [19],
    "content": '''
# Framtidens AI-Agenter

Utforska vad som kommer nast inom AI-agenter.

------------------------------------------------------------

## Vad kommer nast?

AI-agenter utvecklas snabbt. Har ar de viktigaste trenderna att folja.

| Trend | Tidshorisont |
|-------|--------------|
| Multimodal agents | Nu - 1 ar |
| Specialized agents | 1-2 ar |
| Agent ecosystems | 2-3 ar |
| AGI-level agents | 5+ ar |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Framtidssaker | Forbereda for nya mojligheter |
| Karriar | Efterfragade kompetenser |
| Innovation | Forsta vad som ar mojligt |
| Strategi | Planera long-term |

------------------------------------------------------------

## Snabbreferens - Emerging Technologies

| Teknologi | Beskrivning | Impact |
|-----------|-------------|--------|
| Computer use | Agenter som anvander UI | Hog |
| MCP | Model Context Protocol | Hog |
| Reasoning models | O1, O3 | Transformativ |
| Agent protocols | Standardisering | Medium |

------------------------------------------------------------

## Evolution of AI Agents

```
+-----------------------------------------------------------------+
|                  AGENT EVOLUTION                                 |
+-----------------------------------------------------------------+
|                                                                  |
|  2023: Basic Tool Use                                           |
|  +----------------------------------------------------------+  |
|  |  LLM + Simple Tools (search, calculator)                  |  |
|  +----------------------------------------------------------+  |
|                           |                                      |
|                           v                                      |
|  2024: Agentic Workflows                                        |
|  +----------------------------------------------------------+  |
|  |  Multi-step reasoning, Planning, Memory                   |  |
|  +----------------------------------------------------------+  |
|                           |                                      |
|                           v                                      |
|  2025: Multi-Agent Systems                                      |
|  +----------------------------------------------------------+  |
|  |  Specialized agents, Collaboration, Orchestration         |  |
|  +----------------------------------------------------------+  |
|                           |                                      |
|                           v                                      |
|  2026+: Autonomous Systems                                      |
|  +----------------------------------------------------------+  |
|  |  Self-improving, Long-term memory, Complex reasoning      |  |
|  +----------------------------------------------------------+  |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Multimodal Agents

```python
# Framtida multimodal agent
class MultimodalAgent:
    """Agent som hanterar text, bild, ljud och video."""

    def __init__(self, client):
        self.client = client
        self.modalities = ["text", "image", "audio", "video"]

    async def process(self, inputs: dict) -> dict:
        # Analysera alla modaliteter
        analyses = {}

        if "image" in inputs:
            analyses["image"] = await self._analyze_image(inputs["image"])

        if "audio" in inputs:
            analyses["audio"] = await self._transcribe_audio(inputs["audio"])

        if "text" in inputs:
            analyses["text"] = inputs["text"]

        # Kombinera insikter
        combined = await self._synthesize(analyses)

        return combined

    async def _analyze_image(self, image_data: bytes) -> str:
        # Vision API
        response = await self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Beskriv denna bild"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                ]
            }]
        )
        return response.choices[0].message.content

    async def _synthesize(self, analyses: dict) -> dict:
        prompt = "Kombinera dessa analyser till en sammanhangande forstaelse:\\n"
        for modality, analysis in analyses.items():
            prompt += f"\\n{modality}: {analysis}"

        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return {"synthesis": response.choices[0].message.content}
```

------------------------------------------------------------

## Computer Use Agents

```python
# Anthropic Computer Use style
class ComputerUseAgent:
    """Agent som kan anvanda datorns UI."""

    def __init__(self, client):
        self.client = client
        self.screen_reader = None  # Hypothetical
        self.mouse_controller = None  # Hypothetical

    async def execute_task(self, task: str) -> dict:
        steps = []
        max_steps = 20

        for _ in range(max_steps):
            # Ta screenshot
            screenshot = await self._capture_screen()

            # Analysera och bestam action
            action = await self._decide_action(task, screenshot, steps)

            if action["type"] == "complete":
                return {"status": "completed", "steps": steps}

            # Utfor action
            await self._execute_action(action)
            steps.append(action)

        return {"status": "max_steps_reached", "steps": steps}

    async def _decide_action(self, task: str, screenshot: bytes, history: list) -> dict:
        response = await self.client.chat.completions.create(
            model="computer-use-model",  # Hypothetical
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": f"Task: {task}\\nHistory: {history}\\nWhat action should I take?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{screenshot}"}}
                ]
            }]
        )

        # Parse action from response
        return {"type": "click", "x": 100, "y": 200}
```

------------------------------------------------------------

## Model Context Protocol (MCP)

```python
# MCP Server implementation
from dataclasses import dataclass

@dataclass
class MCPResource:
    uri: str
    name: str
    description: str
    mime_type: str

@dataclass
class MCPTool:
    name: str
    description: str
    input_schema: dict

class MCPServer:
    """MCP server som exponerar resurser och tools."""

    def __init__(self):
        self.resources = []
        self.tools = []

    def register_resource(self, resource: MCPResource) -> None:
        self.resources.append(resource)

    def register_tool(self, tool: MCPTool) -> None:
        self.tools.append(tool)

    async def handle_request(self, request: dict) -> dict:
        method = request.get("method")

        if method == "resources/list":
            return {"resources": [vars(r) for r in self.resources]}

        elif method == "tools/list":
            return {"tools": [vars(t) for t in self.tools]}

        elif method == "tools/call":
            tool_name = request["params"]["name"]
            args = request["params"]["arguments"]
            return await self._execute_tool(tool_name, args)

        return {"error": "Unknown method"}

    async def _execute_tool(self, name: str, args: dict) -> dict:
        # Find and execute tool
        for tool in self.tools:
            if tool.name == name:
                # Execute tool logic
                return {"result": f"Executed {name}"}
        return {"error": f"Tool {name} not found"}
```

------------------------------------------------------------

## Agent Protocols och Standards

```
+-----------------------------------------------------------------+
|                  AGENT INTEROPERABILITY                          |
+-----------------------------------------------------------------+
|                                                                  |
|  +-----------------------------------------------------------+ |
|  |                    STANDARD PROTOCOLS                      | |
|  |                                                            | |
|  |  MCP (Model Context Protocol)                             | |
|  |  - Tool definitions                                        | |
|  |  - Resource access                                         | |
|  |  - Prompt templates                                        | |
|  |                                                            | |
|  |  OpenAPI for AI                                            | |
|  |  - REST endpoints                                          | |
|  |  - Schema definitions                                      | |
|  |  - Authentication                                          | |
|  |                                                            | |
|  |  Agent Communication                                       | |
|  |  - Message formats                                         | |
|  |  - Handshake protocols                                     | |
|  |  - State synchronization                                   | |
|  +-----------------------------------------------------------+ |
|                           |                                      |
|                           v                                      |
|  +-----------------------------------------------------------+ |
|  |                   AGENT MARKETPLACE                        | |
|  |  - Discover agents                                         | |
|  |  - Compose workflows                                       | |
|  |  - Share capabilities                                      | |
|  +-----------------------------------------------------------+ |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Forbereda for Framtiden

```python
# Best practices for future-proof agents
class FutureProofAgent:
    """Agent designad for framtida utvidgning."""

    def __init__(self):
        # Modular architecture
        self.components = {
            "reasoning": None,  # Swappable
            "memory": None,     # Swappable
            "tools": [],        # Extensible
            "protocols": []     # Pluggable
        }

    def register_component(self, type: str, component) -> None:
        if type in ["reasoning", "memory"]:
            self.components[type] = component
        elif type == "tool":
            self.components["tools"].append(component)
        elif type == "protocol":
            self.components["protocols"].append(component)

    # Design principles:
    # 1. Loose coupling - components can be replaced
    # 2. Protocol-first - use standards like MCP
    # 3. Observable - everything can be monitored
    # 4. Safe by default - human approval for risky actions
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Lock-in | Proprietary APIs | Abstraktionslager |
| Sakerhetsrisk | For mycket autonomi | Gradvis okning |
| Technical debt | Snabb iteration | Clean architecture |
| Kostnad | Nya modeller dyra | Cost monitoring |

------------------------------------------------------------

## Key Takeaways

| Trend | Forberedelse |
|-------|--------------|
| Multimodal | Bygg for flera input-typer |
| Computer use | Forstall UI-baserade workflows |
| MCP | Implementera standarder nu |
| Autonomi | Gradvis okning med guardrails |

Kom ihag:
- Folj utvecklingen aktivt
- Bygg modulart for att byta komponenter
- Sakerhet forst, autonomi sen
- Standarder sparar tid pa sikt
'''
}

BLOCK_10_NODES = [NODE_19_AUTONOMOUS_AGENTS, NODE_20_FUTURE_AGENTS]
