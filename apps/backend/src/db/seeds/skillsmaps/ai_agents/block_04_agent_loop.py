"""
AI Agents SkillsMap - Block 04: Agent Loop
Nodes 7-8: The Agent Loop, Observation & Reflection
"""

BLOCK_04_NODES = [
    {
        "id": "ai-agents-07",
        "slug": "agent-loop",
        "title": "The Agent Loop: Perception, Reasoning, Action",
        "order_index": 7,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-06"],
        "content": """# The Agent Loop: Perception, Reasoning, Action

## Varför detta är viktigt

Agent Loop är hjärtat i varje AI-agent. Det är den cykliska processen som gör att en
agent kan hantera komplexa uppgifter som kräver flera steg. Utan en väldesignad loop
blir agenter antingen:

- **Fastlåsta** — kan inte komma vidare efter första steget
- **Loopar oändligt** — upprepar samma actions utan progress
- **Inkonsistenta** — glömmer vad de gjort mellan iterationer

Modeller som ReAct, Chain-of-Thought och Plan-and-Execute bygger alla på samma grund:
en strukturerad loop som alternerar mellan tänkande och handling.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Implementera en robust agent loop med felhantering
- ✅ Balansera autonomi vs kontroll i loopen
- ✅ Hantera olika stopping conditions
- ✅ Debugga när agenter fastnar eller loopar
- ✅ Välja mellan ReAct, CoT och Plan-Execute patterns

## Kärnkoncept

### The Core Agent Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         THE AGENT LOOP                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  START: User Request                                                        │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────┐                                                        │
│  │  👁️ PERCEPTION  │◄────────────────────────────────────────┐             │
│  │                 │                                          │             │
│  │ • Parse input   │                                          │             │
│  │ • Load context  │                                          │             │
│  │ • Get state     │                                          │             │
│  └────────┬────────┘                                          │             │
│           │                                                    │             │
│           ▼                                                    │             │
│  ┌─────────────────┐                                          │             │
│  │  🧠 REASONING   │                                          │             │
│  │                 │                                          │             │
│  │ • Analyze       │                                          │             │
│  │ • Plan next     │                                          │             │
│  │ • Decide action │                                          │             │
│  └────────┬────────┘                                          │             │
│           │                                                    │             │
│           ▼                                                    │             │
│     ┌───────────────┐                                         │             │
│     │ ACTION TYPE?  │                                         │             │
│     └───────┬───────┘                                         │             │
│             │                                                  │             │
│    ┌────────┼────────┐                                        │             │
│    │        │        │                                        │             │
│    ▼        ▼        ▼                                        │             │
│  TOOL    RESPOND   ERROR                                      │             │
│  CALL    TO USER   HANDLE                                     │             │
│    │        │        │                                        │             │
│    ▼        │        │                                        │             │
│  ┌─────────┐│        │                                        │             │
│  │Execute  ││        │                                        │             │
│  │ Tool    ││        │                                        │             │
│  └────┬────┘│        │                                        │             │
│       │     │        │                                        │             │
│       ▼     │        │                                        │             │
│  ┌─────────┐│        │                                        │             │
│  │OBSERVE  ││        │                                        │             │
│  │Result   │├────────┤                                        │             │
│  └────┬────┘│        │                                        │             │
│       │     │        │                                        │             │
│       └─────┼────────┘                                        │             │
│             │                                                  │             │
│             ▼                                                  │             │
│     ┌───────────────┐     YES                                 │             │
│     │  TASK DONE?   │─────────────────► END: Final Response   │             │
│     └───────┬───────┘                                         │             │
│             │ NO                                               │             │
│             └──────────────────────────────────────────────────┘             │
│                                                                              │
│  STOPPING CONDITIONS:                                                        │
│  • Task completed (LLM says "done")                                         │
│  • Max iterations reached                                                    │
│  • Error threshold exceeded                                                  │
│  • User interrupts                                                          │
│  • Timeout                                                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Agent Loop Patterns

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      AGENT LOOP PATTERNS                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. ReAct (Reasoning + Acting)                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Thought: "I need to find the weather..."                           │  │
│  │  Action: get_weather(city="Stockholm")                              │  │
│  │  Observation: "15°C, sunny"                                         │  │
│  │  Thought: "Now I have the info, I can respond"                      │  │
│  │  Answer: "The weather in Stockholm is 15°C and sunny"               │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Best for: Step-by-step tasks, debugging, explainability                   │
│                                                                             │
│  2. Plan-and-Execute                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Plan:                                                               │  │
│  │    1. Search for product info                                        │  │
│  │    2. Compare prices                                                 │  │
│  │    3. Check availability                                             │  │
│  │    4. Summarize findings                                             │  │
│  │  Execute: [run each step]                                            │  │
│  │  Replan if needed                                                    │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Best for: Complex multi-step tasks, research, analysis                    │
│                                                                             │
│  3. Reflexion                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Act → Observe → Reflect → Improve → Act again                      │  │
│  │  "That didn't work because X. Next time I'll try Y."                │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Best for: Learning from mistakes, iterative improvement                   │
│                                                                             │
│  4. Tree-of-Thoughts                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Explore multiple paths, evaluate, prune bad branches                │  │
│  │  Path A (score: 0.8) ✓                                               │  │
│  │  Path B (score: 0.3) ✗                                               │  │
│  │  Path C (score: 0.6) ~                                               │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Best for: Complex reasoning, math problems, strategy                      │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera en robust Agent Loop

### 1. Basic Agent Loop

```python
from dataclasses import dataclass, field
from typing import Optional, Callable
from enum import Enum
import time

class ActionType(Enum):
    TOOL_CALL = "tool_call"
    FINAL_RESPONSE = "final_response"
    ERROR = "error"

@dataclass
class AgentState:
    \"\"\"Current state of the agent.\"\"\"
    messages: list = field(default_factory=list)
    iteration: int = 0
    tool_calls_made: int = 0
    errors: list = field(default_factory=list)
    start_time: float = field(default_factory=time.time)

    def elapsed_time(self) -> float:
        return time.time() - self.start_time

@dataclass
class LoopConfig:
    \"\"\"Configuration for the agent loop.\"\"\"
    max_iterations: int = 10
    max_tool_calls: int = 20
    timeout_seconds: float = 60.0
    max_consecutive_errors: int = 3

class AgentLoop:
    \"\"\"Core agent loop implementation.\"\"\"

    def __init__(
        self,
        client: OpenAI,
        tools: list[dict],
        tool_executor: Callable,
        config: LoopConfig = None
    ):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor
        self.config = config or LoopConfig()

    def run(self, user_message: str, system_prompt: str = None) -> str:
        \"\"\"Run the agent loop until completion.\"\"\"

        # Initialize state
        state = AgentState()
        state.messages = [
            {
                "role": "system",
                "content": system_prompt or "You are a helpful assistant with access to tools."
            },
            {"role": "user", "content": user_message}
        ]

        consecutive_errors = 0

        while True:
            state.iteration += 1

            # Check stopping conditions
            stop_reason = self._check_stop_conditions(state)
            if stop_reason:
                return f"[Agent stopped: {stop_reason}]"

            print(f"\\n--- Iteration {state.iteration} ---")

            try:
                # Get LLM response
                response = self._call_llm(state.messages)
                message = response.choices[0].message
                state.messages.append(message)

                # Determine action type
                if message.tool_calls:
                    # Process tool calls
                    action_type = ActionType.TOOL_CALL
                    tool_results = self._process_tools(message.tool_calls, state)
                    state.messages.extend(tool_results)
                    consecutive_errors = 0

                else:
                    # Final response
                    action_type = ActionType.FINAL_RESPONSE
                    print(f"✅ Final response received")
                    return message.content

            except Exception as e:
                consecutive_errors += 1
                state.errors.append(str(e))
                print(f"❌ Error: {e}")

                if consecutive_errors >= self.config.max_consecutive_errors:
                    return f"[Agent stopped: Too many consecutive errors]"

                # Add error to messages for LLM to learn from
                state.messages.append({
                    "role": "user",
                    "content": f"Error occurred: {e}. Please try a different approach."
                })

    def _check_stop_conditions(self, state: AgentState) -> Optional[str]:
        \"\"\"Check if any stopping condition is met.\"\"\"
        if state.iteration > self.config.max_iterations:
            return f"Max iterations ({self.config.max_iterations}) exceeded"

        if state.tool_calls_made > self.config.max_tool_calls:
            return f"Max tool calls ({self.config.max_tool_calls}) exceeded"

        if state.elapsed_time() > self.config.timeout_seconds:
            return f"Timeout ({self.config.timeout_seconds}s) exceeded"

        return None

    def _call_llm(self, messages: list) -> Any:
        \"\"\"Call the LLM with current messages.\"\"\"
        return self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=self.tools,
            tool_choice="auto"
        )

    def _process_tools(self, tool_calls: list, state: AgentState) -> list:
        \"\"\"Process tool calls and return results.\"\"\"
        results = []

        for tool_call in tool_calls:
            state.tool_calls_made += 1

            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"🛠️ Tool: {name}({args})")

            # Execute tool
            result = self.tool_executor(name, args)

            print(f"   → {str(result)[:100]}...")

            results.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        return results
```

### 2. ReAct Pattern Implementation

```python
REACT_SYSTEM_PROMPT = \"\"\"
You are an AI assistant that solves tasks by thinking step-by-step.

For each step, follow this format:
THOUGHT: [Your reasoning about the current situation and what to do next]
ACTION: [The tool to use, if needed]
OBSERVATION: [What you learned from the tool's output]

When you have enough information to answer, respond with:
THOUGHT: [Final reasoning]
ANSWER: [Your complete answer to the user]

Rules:
1. Always explain your reasoning in THOUGHT before taking action
2. Only use one tool per iteration
3. After each tool use, reflect on what you learned
4. If something doesn't work, explain why and try a different approach
\"\"\"

class ReActAgent(AgentLoop):
    \"\"\"Agent using ReAct pattern for explicit reasoning.\"\"\"

    def run(self, user_message: str) -> str:
        return super().run(user_message, system_prompt=REACT_SYSTEM_PROMPT)

    def parse_thought(self, response: str) -> dict:
        \"\"\"Parse structured output from ReAct response.\"\"\"
        result = {
            "thought": None,
            "action": None,
            "observation": None,
            "answer": None
        }

        # Simple parsing (production: use regex or structured output)
        lines = response.split("\\n")
        for line in lines:
            if line.startswith("THOUGHT:"):
                result["thought"] = line.replace("THOUGHT:", "").strip()
            elif line.startswith("ACTION:"):
                result["action"] = line.replace("ACTION:", "").strip()
            elif line.startswith("OBSERVATION:"):
                result["observation"] = line.replace("OBSERVATION:", "").strip()
            elif line.startswith("ANSWER:"):
                result["answer"] = line.replace("ANSWER:", "").strip()

        return result

# Usage
react_agent = ReActAgent(
    client=client,
    tools=registry.get_schemas(),
    tool_executor=lambda n, a: registry.execute(n, a).to_string()
)

response = react_agent.run("What's the weather in Stockholm and calculate 20% tip on 450kr")
```

### 3. Plan-and-Execute Pattern

```python
class PlanExecuteAgent:
    \"\"\"Agent that plans before executing.\"\"\"

    def __init__(self, client, tools, tool_executor):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor

    def run(self, user_message: str) -> str:
        # Step 1: Create plan
        plan = self._create_plan(user_message)
        print(f"📋 Plan created with {len(plan)} steps")

        # Step 2: Execute each step
        results = []
        for i, step in enumerate(plan):
            print(f"\\n--- Step {i+1}: {step['description']} ---")

            result = self._execute_step(step, results)
            results.append({
                "step": step,
                "result": result
            })

            # Check if we need to replan
            if self._should_replan(results):
                plan = self._replan(user_message, results)

        # Step 3: Synthesize final answer
        return self._synthesize(user_message, results)

    def _create_plan(self, user_message: str) -> list:
        \"\"\"Create a plan of steps to accomplish the task.\"\"\"
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Create a step-by-step plan to accomplish this task:
                {user_message}

                Available tools: {[t['function']['name'] for t in self.tools]}

                Respond with a JSON array of steps:
                [
                    {{"description": "...", "tool": "tool_name or null", "args": {{}}}}
                ]

                Keep the plan concise (max 5 steps).
                \"\"\"
            }],
            response_format={"type": "json_object"}
        )

        plan_data = json.loads(response.choices[0].message.content)
        return plan_data.get("steps", [])

    def _execute_step(self, step: dict, previous_results: list) -> str:
        \"\"\"Execute a single step of the plan.\"\"\"
        if step.get("tool"):
            return self.tool_executor(step["tool"], step.get("args", {}))
        else:
            # Reasoning step without tool
            context = "\\n".join([r["result"] for r in previous_results])
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": f"Based on this context:\\n{context}\\n\\n{step['description']}"
                }]
            )
            return response.choices[0].message.content

    def _should_replan(self, results: list) -> bool:
        \"\"\"Check if we need to adjust the plan.\"\"\"
        # Check if last result indicates failure
        last_result = results[-1]["result"] if results else ""
        return "error" in last_result.lower() or "failed" in last_result.lower()

    def _replan(self, original_task: str, results: list) -> list:
        \"\"\"Create a new plan based on what we've learned.\"\"\"
        context = "\\n".join([f"Step: {r['step']['description']}\\nResult: {r['result']}"
                            for r in results])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Original task: {original_task}

                What we've tried:
                {context}

                The last step didn't work as expected. Create a new plan (JSON array).
                \"\"\"
            }],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content).get("steps", [])

    def _synthesize(self, original_task: str, results: list) -> str:
        \"\"\"Create final answer from all results.\"\"\"
        context = "\\n".join([f"Step: {r['step']['description']}\\nResult: {r['result']}"
                            for r in results])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Task: {original_task}

                Completed steps:
                {context}

                Provide a comprehensive answer to the original task based on these results.
                \"\"\"
            }]
        )

        return response.choices[0].message.content
```

## Vanliga problem

### Problem 1: "Agenten fastnar i loop"

```python
class LoopDetector:
    \"\"\"Detect and break infinite loops.\"\"\"

    def __init__(self, window_size: int = 5):
        self.window_size = window_size
        self.recent_actions = []

    def record_action(self, action: str) -> None:
        self.recent_actions.append(action)
        if len(self.recent_actions) > self.window_size * 2:
            self.recent_actions.pop(0)

    def is_looping(self) -> bool:
        \"\"\"Check if recent actions are repeating.\"\"\"
        if len(self.recent_actions) < self.window_size * 2:
            return False

        recent = self.recent_actions[-self.window_size:]
        previous = self.recent_actions[-self.window_size*2:-self.window_size]

        return recent == previous

    def get_loop_breaker_prompt(self) -> str:
        return \"\"\"
        You seem to be repeating the same actions. This is not making progress.
        Please try a completely different approach or explain why you're stuck.
        \"\"\"

# Usage i agent loop
loop_detector = LoopDetector()

# I loopen:
action = f"{tool_name}({args})"
loop_detector.record_action(action)

if loop_detector.is_looping():
    state.messages.append({
        "role": "user",
        "content": loop_detector.get_loop_breaker_prompt()
    })
```

### Problem 2: "Agenten gör för lite progress"

```python
class ProgressTracker:
    \"\"\"Track agent progress towards goal.\"\"\"

    def __init__(self, goal: str, client: OpenAI):
        self.goal = goal
        self.client = client
        self.checkpoints = []

    def evaluate_progress(self, current_state: str) -> float:
        \"\"\"Score progress 0.0 to 1.0.\"\"\"
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Goal: {self.goal}
                Current state: {current_state}

                On a scale of 0.0 to 1.0, how close is the agent to completing the goal?
                Respond with just a number.
                \"\"\"
            }]
        )

        try:
            return float(response.choices[0].message.content.strip())
        except:
            return 0.5

    def checkpoint(self, state: str) -> dict:
        progress = self.evaluate_progress(state)
        self.checkpoints.append({
            "state": state[:200],
            "progress": progress,
            "timestamp": time.time()
        })
        return {"progress": progress, "trend": self._get_trend()}

    def _get_trend(self) -> str:
        if len(self.checkpoints) < 2:
            return "unknown"

        recent = [c["progress"] for c in self.checkpoints[-3:]]
        if recent[-1] > recent[0]:
            return "improving"
        elif recent[-1] < recent[0]:
            return "declining"
        return "stagnant"
```

## Praktisk övning

**Uppgift:** Implementera en Reflexion Agent

```python
class ReflexionAgent:
    \"\"\"
    Agent that learns from its mistakes using reflection.

    TODO: Implementera:
    1. run_trial(): Kör ett försök att lösa uppgiften
    2. reflect(): Analysera vad som gick fel
    3. run(): Kör trials tills success eller max attempts

    Pattern:
    Trial 1 → Fail → Reflect → Trial 2 → Fail → Reflect → Trial 3 → Success
    \"\"\"

    def __init__(self, client, tools, tool_executor, max_trials: int = 3):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor
        self.max_trials = max_trials
        self.reflections = []

    def run_trial(self, task: str, reflection: str = None) -> tuple[str, bool]:
        \"\"\"
        Run one trial with optional reflection from previous attempt.
        Returns (result, success).
        \"\"\"
        # Din kod här
        pass

    def reflect(self, task: str, result: str) -> str:
        \"\"\"
        Analyze what went wrong and how to improve.
        \"\"\"
        # Din kod här
        pass

    def run(self, task: str) -> str:
        \"\"\"
        Main entry: run trials with reflection until success.
        \"\"\"
        # Din kod här
        pass

# Test
agent = ReflexionAgent(client, tools, executor)
result = agent.run("Find the capital of a country that starts with 'Z' and has more than 10M population")
```

## Sammanfattning

- ✅ **Agent Loop** = Perception → Reasoning → Action → Observe → Repeat
- ✅ **Stopping conditions** förhindrar oändliga loopar
- ✅ **ReAct** ger explicit reasoning och debugging
- ✅ **Plan-Execute** är bättre för komplexa multi-step tasks
- ✅ **Reflexion** låter agenten lära sig från misstag

## Nästa steg

- **Node 8:** Observation & Reflection — Hur agenter lär sig
- **Node 9:** Tool Design Patterns — Best practices för tools

---
*Pro tip: Logga alltid varje iteration för debugging — du kommer behöva det!*
"""
    },
    {
        "id": "ai-agents-08",
        "slug": "observation-and-reflection",
        "title": "Observation och Reflection",
        "order_index": 8,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-07"],
        "content": """# Observation och Reflection

## Varför detta är viktigt

En agent som inte kan observera resultaten av sina actions är blind. En agent som inte
kan reflektera över sina observationer är dum. Dessa två förmågor är vad som skiljer
en simpel script från en intelligent agent.

**Observation** = förmågan att förstå vad som hände
**Reflection** = förmågan att lära sig från vad som hände

2024 visade forskning att agenter med explicit reflection presterar 20-30% bättre
på komplexa uppgifter. Det är skillnaden mellan en agent som upprepar samma misstag
och en som faktiskt förbättras.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Designa observation pipelines för olika tool outputs
- ✅ Implementera reflection prompts som förbättrar agentbeteende
- ✅ Bygga self-correction mekanismer
- ✅ Skapa feedback loops för kontinuerlig förbättring
- ✅ Balansera reflection-kostnad vs performance-vinst

## Kärnkoncept

### Observation Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      OBSERVATION PIPELINE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TOOL OUTPUT (Raw)                                                          │
│  │                                                                           │
│  │  {"status": 200, "data": {"temp": 15.5, "condition": "cloudy",...}}     │
│  │                                                                           │
│  ▼                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  PARSER                                                              │   │
│  │  • Extract relevant fields                                           │   │
│  │  • Handle errors/edge cases                                          │   │
│  │  • Convert to agent-friendly format                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  │                                                                           │
│  ▼                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  SUMMARIZER (Optional)                                               │   │
│  │  • Condense long outputs                                             │   │
│  │  • Highlight key information                                         │   │
│  │  • Remove noise                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  │                                                                           │
│  ▼                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  CONTEXTUALIZER                                                      │   │
│  │  • Relate to previous observations                                   │   │
│  │  • Connect to current goal                                           │   │
│  │  • Flag anomalies                                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  │                                                                           │
│  ▼                                                                           │
│  PROCESSED OBSERVATION                                                       │
│                                                                              │
│  "Weather in Stockholm: 15.5°C, cloudy. This is relevant to user's         │
│   question about outdoor activities. Temperature is mild."                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Reflection Types

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        REFLECTION TYPES                                     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. IMMEDIATE REFLECTION (After each action)                               │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "Did this action achieve what I expected?"                          │  │
│  │  "What new information did I learn?"                                 │  │
│  │  "Should I adjust my approach?"                                      │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Cost: +1 LLM call per action                                              │
│  Benefit: Quick course correction                                          │
│                                                                             │
│  2. CHECKPOINT REFLECTION (After N actions or milestones)                  │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "How much progress have I made?"                                    │  │
│  │  "Are there patterns in what's working/not working?"                 │  │
│  │  "Should I change strategy entirely?"                                │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Cost: +1 LLM call per checkpoint                                          │
│  Benefit: Strategic adjustments                                            │
│                                                                             │
│  3. FINAL REFLECTION (At task completion/failure)                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "Did I fully answer the question?"                                  │  │
│  │  "What could I have done better?"                                    │  │
│  │  "What lessons can I apply to future tasks?"                         │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Cost: +1 LLM call per task                                                │
│  Benefit: Learning for future tasks                                        │
│                                                                             │
│  4. RETROSPECTIVE REFLECTION (Cross-task learning)                         │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "Across multiple tasks, what strategies work best?"                 │  │
│  │  "What common mistakes do I make?"                                   │  │
│  │  "How can I improve my general approach?"                            │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  Cost: Periodic batch processing                                           │
│  Benefit: Systemic improvement                                             │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera Observation & Reflection

### 1. Observation Handler

```python
from dataclasses import dataclass
from typing import Any, Optional
import json

@dataclass
class Observation:
    \"\"\"Structured observation from tool output.\"\"\"
    raw_output: Any
    parsed_data: dict
    summary: str
    relevance_score: float  # 0.0 - 1.0
    anomalies: list[str]
    timestamp: float

class ObservationHandler:
    \"\"\"Process and structure tool outputs.\"\"\"

    def __init__(self, client: OpenAI):
        self.client = client

    def process(
        self,
        tool_name: str,
        raw_output: Any,
        current_goal: str
    ) -> Observation:
        \"\"\"Convert raw tool output to structured observation.\"\"\"

        # Step 1: Parse raw output
        parsed = self._parse_output(tool_name, raw_output)

        # Step 2: Summarize for agent
        summary = self._summarize(tool_name, parsed, current_goal)

        # Step 3: Assess relevance
        relevance = self._assess_relevance(summary, current_goal)

        # Step 4: Detect anomalies
        anomalies = self._detect_anomalies(parsed)

        return Observation(
            raw_output=raw_output,
            parsed_data=parsed,
            summary=summary,
            relevance_score=relevance,
            anomalies=anomalies,
            timestamp=time.time()
        )

    def _parse_output(self, tool_name: str, raw_output: Any) -> dict:
        \"\"\"Parse raw output based on tool type.\"\"\"
        if isinstance(raw_output, dict):
            return raw_output
        elif isinstance(raw_output, str):
            try:
                return json.loads(raw_output)
            except:
                return {"text": raw_output}
        else:
            return {"value": str(raw_output)}

    def _summarize(self, tool_name: str, parsed: dict, goal: str) -> str:
        \"\"\"Create agent-friendly summary.\"\"\"
        # For simple outputs, format directly
        if len(str(parsed)) < 500:
            return f"Tool '{tool_name}' returned: {json.dumps(parsed, indent=2)}"

        # For complex outputs, use LLM to summarize
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Summarize this tool output concisely, focusing on information relevant to: {goal}

                Tool: {tool_name}
                Output: {json.dumps(parsed)[:2000]}

                Provide a 2-3 sentence summary.
                \"\"\"
            }],
            max_tokens=150
        )
        return response.choices[0].message.content

    def _assess_relevance(self, summary: str, goal: str) -> float:
        \"\"\"Score relevance of observation to current goal.\"\"\"
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Goal: {goal}
                Observation: {summary}

                How relevant is this observation to achieving the goal?
                Respond with a single number from 0.0 (irrelevant) to 1.0 (highly relevant).
                \"\"\"
            }],
            max_tokens=10
        )
        try:
            return float(response.choices[0].message.content.strip())
        except:
            return 0.5

    def _detect_anomalies(self, parsed: dict) -> list[str]:
        \"\"\"Identify unexpected or error conditions.\"\"\"
        anomalies = []

        # Check for error indicators
        if "error" in str(parsed).lower():
            anomalies.append("Error detected in output")

        if parsed.get("status") and parsed["status"] >= 400:
            anomalies.append(f"HTTP error status: {parsed['status']}")

        if parsed.get("data") == [] or parsed.get("results") == []:
            anomalies.append("Empty results returned")

        return anomalies
```

### 2. Reflection Engine

```python
@dataclass
class Reflection:
    \"\"\"Structured reflection output.\"\"\"
    assessment: str
    learnings: list[str]
    adjustments: list[str]
    confidence: float
    should_continue: bool

class ReflectionEngine:
    \"\"\"Generate reflections to improve agent behavior.\"\"\"

    def __init__(self, client: OpenAI):
        self.client = client
        self.reflection_history = []

    def immediate_reflect(
        self,
        action: str,
        observation: Observation,
        goal: str
    ) -> Reflection:
        \"\"\"Reflect immediately after an action.\"\"\"

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                You just took an action. Reflect on what happened.

                GOAL: {goal}
                ACTION: {action}
                OBSERVATION: {observation.summary}
                RELEVANCE: {observation.relevance_score:.2f}
                ANOMALIES: {observation.anomalies}

                Answer these questions:
                1. Did the action achieve what you expected?
                2. What did you learn?
                3. Should you adjust your approach?
                4. How confident are you in your progress? (0.0-1.0)
                5. Should you continue or stop?

                Format:
                ASSESSMENT: [your analysis]
                LEARNINGS: [comma-separated list]
                ADJUSTMENTS: [comma-separated list]
                CONFIDENCE: [0.0-1.0]
                CONTINUE: [yes/no]
                \"\"\"
            }]
        )

        return self._parse_reflection(response.choices[0].message.content)

    def checkpoint_reflect(
        self,
        actions_taken: list[dict],
        goal: str,
        progress_score: float
    ) -> Reflection:
        \"\"\"Reflect at a checkpoint (after N actions).\"\"\"

        action_summary = "\\n".join([
            f"- {a['action']}: {a['result'][:100]}..."
            for a in actions_taken[-5:]  # Last 5 actions
        ])

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Checkpoint reflection. Analyze your progress.

                GOAL: {goal}
                PROGRESS SCORE: {progress_score:.2f}

                RECENT ACTIONS:
                {action_summary}

                Analyze:
                1. Are you making good progress towards the goal?
                2. What patterns do you see in your actions?
                3. What's working well? What isn't?
                4. Should you change your overall strategy?

                Format same as before: ASSESSMENT, LEARNINGS, ADJUSTMENTS, CONFIDENCE, CONTINUE
                \"\"\"
            }]
        )

        reflection = self._parse_reflection(response.choices[0].message.content)
        self.reflection_history.append(reflection)
        return reflection

    def final_reflect(
        self,
        goal: str,
        result: str,
        success: bool,
        all_actions: list[dict]
    ) -> Reflection:
        \"\"\"Final reflection at task completion.\"\"\"

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Task completed. Final reflection.

                GOAL: {goal}
                SUCCESS: {success}
                FINAL RESULT: {result[:500]}
                TOTAL ACTIONS: {len(all_actions)}

                Reflect:
                1. Did you fully accomplish the goal?
                2. What went well?
                3. What could you have done better?
                4. What will you do differently next time?

                This is for learning - be honest and specific.
                \"\"\"
            }]
        )

        return self._parse_reflection(response.choices[0].message.content)

    def _parse_reflection(self, text: str) -> Reflection:
        \"\"\"Parse structured reflection output.\"\"\"
        lines = text.split("\\n")

        assessment = ""
        learnings = []
        adjustments = []
        confidence = 0.5
        should_continue = True

        for line in lines:
            line = line.strip()
            if line.startswith("ASSESSMENT:"):
                assessment = line.replace("ASSESSMENT:", "").strip()
            elif line.startswith("LEARNINGS:"):
                learnings = [l.strip() for l in line.replace("LEARNINGS:", "").split(",")]
            elif line.startswith("ADJUSTMENTS:"):
                adjustments = [a.strip() for a in line.replace("ADJUSTMENTS:", "").split(",")]
            elif line.startswith("CONFIDENCE:"):
                try:
                    confidence = float(line.replace("CONFIDENCE:", "").strip())
                except:
                    confidence = 0.5
            elif line.startswith("CONTINUE:"):
                should_continue = "yes" in line.lower()

        return Reflection(
            assessment=assessment,
            learnings=learnings,
            adjustments=adjustments,
            confidence=confidence,
            should_continue=should_continue
        )
```

### 3. Self-Correction System

```python
class SelfCorrectionSystem:
    \"\"\"Enable agent to correct its own mistakes.\"\"\"

    def __init__(self, client: OpenAI, reflection_engine: ReflectionEngine):
        self.client = client
        self.reflection_engine = reflection_engine
        self.error_patterns = []

    def check_and_correct(
        self,
        action: str,
        result: str,
        expected_outcome: str
    ) -> Optional[str]:
        \"\"\"Check if correction is needed and provide it.\"\"\"

        # Evaluate if result matches expectation
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f\"\"\"
                Action: {action}
                Expected: {expected_outcome}
                Actual result: {result}

                Does the actual result match the expected outcome?
                If NO, what went wrong and how should we correct it?

                Format:
                MATCH: [yes/no]
                ISSUE: [describe the problem if no match]
                CORRECTION: [specific action to fix it]
                \"\"\"
            }]
        )

        text = response.choices[0].message.content

        if "MATCH: no" in text.lower():
            # Extract correction
            for line in text.split("\\n"):
                if line.strip().startswith("CORRECTION:"):
                    return line.replace("CORRECTION:", "").strip()

        return None

    def learn_from_error(self, error_context: dict) -> None:
        \"\"\"Store error pattern for future avoidance.\"\"\"
        self.error_patterns.append({
            "action": error_context.get("action"),
            "error": error_context.get("error"),
            "correction": error_context.get("correction"),
            "timestamp": time.time()
        })

    def get_error_avoidance_prompt(self) -> str:
        \"\"\"Generate prompt to avoid past errors.\"\"\"
        if not self.error_patterns:
            return ""

        recent_errors = self.error_patterns[-5:]
        error_text = "\\n".join([
            f"- Avoided: {e['action']} because {e['error']}"
            for e in recent_errors
        ])

        return f\"\"\"
        LEARN FROM PAST MISTAKES:
        {error_text}

        Do not repeat these errors.
        \"\"\"
```

### 4. Integrera allt i Agent

```python
class ReflectiveAgent:
    \"\"\"Agent with full observation and reflection capabilities.\"\"\"

    def __init__(self, client, tools, tool_executor):
        self.client = client
        self.tools = tools
        self.tool_executor = tool_executor

        self.observation_handler = ObservationHandler(client)
        self.reflection_engine = ReflectionEngine(client)
        self.self_correction = SelfCorrectionSystem(client, self.reflection_engine)

        self.actions_taken = []

    def run(self, goal: str, max_iterations: int = 10) -> str:
        messages = [
            {"role": "system", "content": self._get_system_prompt()},
            {"role": "user", "content": goal}
        ]

        for i in range(max_iterations):
            # Get LLM response
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=self.tools
            )

            message = response.choices[0].message
            messages.append(message)

            if message.tool_calls:
                for tool_call in message.tool_calls:
                    # Execute tool
                    result = self.tool_executor(
                        tool_call.function.name,
                        json.loads(tool_call.function.arguments)
                    )

                    # Process observation
                    observation = self.observation_handler.process(
                        tool_call.function.name,
                        result,
                        goal
                    )

                    # Store action
                    self.actions_taken.append({
                        "action": f"{tool_call.function.name}({tool_call.function.arguments})",
                        "result": observation.summary
                    })

                    # Immediate reflection
                    reflection = self.reflection_engine.immediate_reflect(
                        self.actions_taken[-1]["action"],
                        observation,
                        goal
                    )

                    # Check for self-correction
                    if observation.anomalies:
                        correction = self.self_correction.check_and_correct(
                            self.actions_taken[-1]["action"],
                            observation.summary,
                            "successful execution"
                        )
                        if correction:
                            messages.append({
                                "role": "user",
                                "content": f"Correction needed: {correction}"
                            })

                    # Add tool result
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": observation.summary
                    })

                    # Checkpoint reflection every 3 actions
                    if len(self.actions_taken) % 3 == 0:
                        checkpoint = self.reflection_engine.checkpoint_reflect(
                            self.actions_taken,
                            goal,
                            progress_score=reflection.confidence
                        )

                        if not checkpoint.should_continue:
                            break

                        if checkpoint.adjustments:
                            messages.append({
                                "role": "user",
                                "content": f"Strategy adjustment: {', '.join(checkpoint.adjustments)}"
                            })
            else:
                # Final response
                final_reflection = self.reflection_engine.final_reflect(
                    goal,
                    message.content,
                    success=True,
                    all_actions=self.actions_taken
                )

                return message.content

        return "Max iterations reached"

    def _get_system_prompt(self) -> str:
        error_avoidance = self.self_correction.get_error_avoidance_prompt()

        return f\"\"\"
        You are a reflective AI agent. After each action:
        1. Observe the result carefully
        2. Reflect on what you learned
        3. Adjust your approach if needed

        {error_avoidance}

        Be thoughtful and learn from each step.
        \"\"\"
```

## Praktisk övning

**Uppgift:** Bygg ett Reflection Dashboard

```python
class ReflectionDashboard:
    \"\"\"
    TODO: Bygg ett dashboard som visualiserar agentens reflektioner.

    Funktioner:
    1. show_reflection_timeline(): Visa alla reflektioner i kronologisk ordning
    2. analyze_patterns(): Identifiera återkommande problem/lösningar
    3. get_improvement_suggestions(): Generera förslag baserat på historik
    4. export_learnings(): Spara lärdomar till fil för framtida sessioner
    \"\"\"

    def __init__(self, reflection_engine: ReflectionEngine):
        self.engine = reflection_engine

    def show_reflection_timeline(self) -> str:
        # Din kod här
        pass

    def analyze_patterns(self) -> dict:
        # Din kod här
        pass

    def get_improvement_suggestions(self) -> list[str]:
        # Din kod här
        pass

    def export_learnings(self, filepath: str) -> None:
        # Din kod här
        pass

# Test
dashboard = ReflectionDashboard(reflection_engine)
print(dashboard.show_reflection_timeline())
print(dashboard.analyze_patterns())
```

## Sammanfattning

- ✅ **Observation** transformerar rå tool-output till strukturerad information
- ✅ **Reflection** låter agenten lära sig från sina handlingar
- ✅ **Self-correction** fixar misstag innan de blir problem
- ✅ **Checkpoint reflections** ger strategiska justeringar
- ✅ **Balansera cost vs benefit** — inte varje action behöver reflektion

## Nästa steg

- **Node 9:** Agent Frameworks — LangChain, LlamaIndex, AutoGen
- **Node 10:** Memory Systems — Hur agenter minns

---
*Pro tip: Börja med checkpoint reflections var 3:e action, justera baserat på task complexity!*
"""
    }
]
