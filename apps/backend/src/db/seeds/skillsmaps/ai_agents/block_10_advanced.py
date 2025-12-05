"""
AI Agents SkillsMap - Block 10: Advanced & Future
Nodes 19-20: Autonomous Agents, The Future
"""

BLOCK_10_NODES = [
    {
        "id": "ai-agents-19",
        "slug": "autonomous-agents",
        "title": "Autonomous Agents",
        "order_index": 19,
        "estimated_minutes": 45,
        "xp_reward": 130,
        "difficulty": "expert",
        "node_type": "concept",
        "prerequisites": ["ai-agents-18"],
        "content": """# Autonomous Agents

## Varför detta är viktigt

Autonomous agents representerar nästa steg i AI-evolution — agenter som kan:

- **Planera långsiktigt** utan ständig human input
- **Lära sig** från erfarenhet och förbättras över tid
- **Hantera osäkerhet** och ta beslut under ambiguitet
- **Samarbeta** med andra agenter och människor

Men autonomi kommer med risker. Denna modul balanserar möjligheterna med säkerhet.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Förstå skillnaden mellan assistants och autonomous agents
- ✅ Implementera long-term planning systems
- ✅ Bygga self-improving agents
- ✅ Designa safety guardrails för autonoma system
- ✅ Utvärdera när autonomi är lämpligt

## Kärnkoncept

### Autonomy Spectrum

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AUTONOMY SPECTRUM                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Level 0          Level 1          Level 2          Level 3          Level 4│
│  ─────────────────────────────────────────────────────────────────────────► │
│                                                                              │
│  CHATBOT          ASSISTANT        AGENT            AUTONOMOUS       FULLY   │
│                                                     AGENT            AGI     │
│                                                                              │
│  • Responds       • Task-based     • Multi-step     • Self-directed  • ???  │
│    to prompts       execution        planning         goals                  │
│  • No memory      • Simple tools   • Tool chains    • Learning              │
│  • No planning    • Human          • Limited        • Long-term             │
│  • Stateless        approval         autonomy         planning              │
│                                                     • Self-                  │
│                                                       correction            │
│                                                                              │
│  Example:         Example:         Example:         Example:                │
│  Basic ChatGPT    GitHub Copilot   AutoGPT          Research Agent          │
│                                                                              │
│  Risk: Low        Risk: Medium     Risk: High       Risk: Very High         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Autonomous Agent Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  AUTONOMOUS AGENT ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         GOAL SYSTEM                                   │   │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐         │   │
│  │  │ Primary Goal    │ │ Sub-Goals       │ │ Constraints     │         │   │
│  │  │ (User-defined)  │ │ (Self-derived)  │ │ (Safety bounds) │         │   │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘         │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                       PLANNING SYSTEM                                 │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │   │
│  │  │  Strategic   │  │   Tactical   │  │ Operational  │                │   │
│  │  │  Planner     │  │   Planner    │  │  Planner     │                │   │
│  │  │  (Long-term) │  │  (Sessions)  │  │  (Actions)   │                │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘                │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                      EXECUTION SYSTEM                                 │   │
│  │  ┌──────────────────┐  ┌──────────────────┐                          │   │
│  │  │  Action Engine   │  │  Safety Monitor  │◄─── Guardrails           │   │
│  │  │  (Runs plans)    │  │  (Validates all) │                          │   │
│  │  └──────────────────┘  └──────────────────┘                          │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                      LEARNING SYSTEM                                  │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │   │
│  │  │   Memory     │  │  Reflection  │  │   Skill      │                │   │
│  │  │   (Long-term)│  │  (Evaluate)  │  │   Acquisition│                │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘                │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Bygga Autonomous Agent

### 1. Goal System

```python
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from datetime import datetime

class GoalStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    FAILED = "failed"

class GoalPriority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

@dataclass
class Goal:
    id: str
    description: str
    priority: GoalPriority
    status: GoalStatus = GoalStatus.PENDING
    parent_id: Optional[str] = None
    sub_goals: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    deadline: Optional[datetime] = None
    progress: float = 0.0

    def is_achievable(self, context: dict) -> bool:
        \"\"\"Check if goal can be achieved given current context.\"\"\"
        # Check constraints
        for constraint in self.constraints:
            if not self._check_constraint(constraint, context):
                return False
        return True

    def _check_constraint(self, constraint: str, context: dict) -> bool:
        # Simple constraint checking
        if "budget" in constraint:
            return context.get("remaining_budget", 0) > 0
        if "time" in constraint:
            return self.deadline is None or datetime.now() < self.deadline
        return True


class GoalManager:
    \"\"\"Manages hierarchical goals for autonomous agent.\"\"\"

    def __init__(self):
        self.goals: dict[str, Goal] = {}
        self.client = OpenAI()

    def set_primary_goal(self, description: str, constraints: list[str] = None) -> Goal:
        \"\"\"Set the agent's primary objective.\"\"\"
        goal = Goal(
            id="primary",
            description=description,
            priority=GoalPriority.CRITICAL,
            constraints=constraints or []
        )
        self.goals["primary"] = goal
        return goal

    async def decompose_goal(self, goal_id: str) -> list[Goal]:
        \"\"\"Break down a goal into sub-goals using LLM.\"\"\"
        goal = self.goals[goal_id]

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": \"\"\"
                Break down the given goal into 3-5 concrete sub-goals.
                Return JSON: {"sub_goals": [{"description": "...", "priority": "high|medium|low"}]}
                \"\"\"},
                {"role": "user", "content": f"Goal: {goal.description}\\nConstraints: {goal.constraints}"}
            ]
        )

        import json
        sub_goals_data = json.loads(response.choices[0].message.content)

        sub_goals = []
        for i, sg_data in enumerate(sub_goals_data["sub_goals"]):
            sg = Goal(
                id=f"{goal_id}_sub_{i}",
                description=sg_data["description"],
                priority=GoalPriority[sg_data["priority"].upper()],
                parent_id=goal_id,
                constraints=goal.constraints  # Inherit constraints
            )
            self.goals[sg.id] = sg
            sub_goals.append(sg)
            goal.sub_goals.append(sg.id)

        return sub_goals

    def get_next_goal(self) -> Optional[Goal]:
        \"\"\"Get the highest priority actionable goal.\"\"\"
        actionable = [
            g for g in self.goals.values()
            if g.status == GoalStatus.PENDING
            and (not g.sub_goals or all(
                self.goals[sg].status == GoalStatus.COMPLETED
                for sg in g.sub_goals
            ))
        ]

        if not actionable:
            return None

        return min(actionable, key=lambda g: g.priority.value)

    def update_progress(self, goal_id: str, progress: float, status: GoalStatus = None):
        \"\"\"Update goal progress and propagate to parent.\"\"\"
        goal = self.goals[goal_id]
        goal.progress = progress

        if status:
            goal.status = status

        # Update parent progress
        if goal.parent_id and goal.parent_id in self.goals:
            parent = self.goals[goal.parent_id]
            if parent.sub_goals:
                parent.progress = sum(
                    self.goals[sg].progress for sg in parent.sub_goals
                ) / len(parent.sub_goals)
```

### 2. Long-term Planning

```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class Plan:
    id: str
    goal_id: str
    steps: list[dict]
    estimated_duration: float
    risk_level: str
    alternatives: list['Plan'] = field(default_factory=list)

class StrategicPlanner:
    \"\"\"Creates and manages long-term plans.\"\"\"

    def __init__(self):
        self.client = OpenAI()
        self.plans: dict[str, Plan] = {}

    async def create_plan(
        self,
        goal: Goal,
        context: dict,
        available_tools: list[str]
    ) -> Plan:
        \"\"\"Create a strategic plan for achieving a goal.\"\"\"
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f\"\"\"
                Create a detailed plan to achieve the goal.
                Available tools: {available_tools}

                Return JSON:
                {{
                    "steps": [
                        {{
                            "id": "step_1",
                            "description": "...",
                            "tool": "tool_name or null",
                            "dependencies": ["step_ids"],
                            "estimated_minutes": 10,
                            "can_fail": true/false
                        }}
                    ],
                    "total_duration_minutes": 60,
                    "risk_level": "low|medium|high",
                    "success_criteria": "..."
                }}
                \"\"\"},
                {"role": "user", "content": f\"\"\"
                Goal: {goal.description}
                Constraints: {goal.constraints}
                Current context: {context}
                \"\"\"}
            ]
        )

        import json
        plan_data = json.loads(response.choices[0].message.content)

        plan = Plan(
            id=f"plan_{goal.id}",
            goal_id=goal.id,
            steps=plan_data["steps"],
            estimated_duration=plan_data["total_duration_minutes"],
            risk_level=plan_data["risk_level"]
        )

        self.plans[plan.id] = plan
        return plan

    async def adapt_plan(self, plan_id: str, failure_info: dict) -> Plan:
        \"\"\"Adapt plan based on failure or changed circumstances.\"\"\"
        plan = self.plans[plan_id]

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": \"\"\"
                The current plan encountered an issue. Adapt it.
                Return the modified plan in the same JSON format.
                \"\"\"},
                {"role": "user", "content": f\"\"\"
                Original plan: {json.dumps(plan.steps)}
                Failure info: {failure_info}
                What should we do differently?
                \"\"\"}
            ]
        )

        new_plan_data = json.loads(response.choices[0].message.content)

        adapted_plan = Plan(
            id=f"{plan.id}_v2",
            goal_id=plan.goal_id,
            steps=new_plan_data["steps"],
            estimated_duration=new_plan_data["total_duration_minutes"],
            risk_level=new_plan_data["risk_level"]
        )

        self.plans[adapted_plan.id] = adapted_plan
        return adapted_plan
```

### 3. Self-Improvement System

```python
@dataclass
class Experience:
    task: str
    approach: str
    outcome: str  # success/failure
    lessons: list[str]
    timestamp: datetime

class LearningSystem:
    \"\"\"Enables agent to learn from experience.\"\"\"

    def __init__(self):
        self.client = OpenAI()
        self.experiences: list[Experience] = []
        self.skills: dict[str, float] = {}  # skill -> proficiency (0-1)
        self.semantic_memory = SemanticMemory("learning")

    async def learn_from_outcome(
        self,
        task: str,
        approach: str,
        outcome: str,
        feedback: str = None
    ):
        \"\"\"Extract lessons from an experience.\"\"\"
        # Analyze what happened
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": \"\"\"
                Analyze this experience and extract lessons learned.
                Return JSON: {"lessons": ["lesson 1", "lesson 2"], "skills_used": ["skill1"]}
                \"\"\"},
                {"role": "user", "content": f\"\"\"
                Task: {task}
                Approach: {approach}
                Outcome: {outcome}
                Feedback: {feedback}
                \"\"\"}
            ]
        )

        analysis = json.loads(response.choices[0].message.content)

        # Store experience
        exp = Experience(
            task=task,
            approach=approach,
            outcome=outcome,
            lessons=analysis["lessons"],
            timestamp=datetime.now()
        )
        self.experiences.append(exp)

        # Store in semantic memory for future retrieval
        for lesson in analysis["lessons"]:
            self.semantic_memory.store(
                f"Lesson from {task}: {lesson}",
                task_type=task,
                outcome=outcome
            )

        # Update skill proficiency
        for skill in analysis["skills_used"]:
            if skill not in self.skills:
                self.skills[skill] = 0.1

            if outcome == "success":
                self.skills[skill] = min(1.0, self.skills[skill] + 0.1)
            else:
                self.skills[skill] = max(0.0, self.skills[skill] - 0.05)

    async def get_relevant_lessons(self, task: str) -> list[str]:
        \"\"\"Retrieve lessons relevant to a new task.\"\"\"
        memories = self.semantic_memory.search(task, top_k=5)
        return [m.content for m in memories]

    async def suggest_approach(self, task: str) -> dict:
        \"\"\"Suggest an approach based on past experiences.\"\"\"
        lessons = await self.get_relevant_lessons(task)

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": \"\"\"
                Based on past lessons, suggest the best approach for this task.
                Return JSON: {"approach": "...", "confidence": 0.0-1.0, "reasoning": "..."}
                \"\"\"},
                {"role": "user", "content": f\"\"\"
                Task: {task}
                Relevant lessons from past: {lessons}
                My skill levels: {self.skills}
                \"\"\"}
            ]
        )

        return json.loads(response.choices[0].message.content)
```

### 4. Safety Guardrails

```python
from typing import Callable
from enum import Enum

class RiskLevel(Enum):
    SAFE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class SafetyGuardrails:
    \"\"\"Safety system for autonomous agents.\"\"\"

    def __init__(self):
        self.client = OpenAI()
        self.blocked_actions: set[str] = set()
        self.require_approval: set[str] = set()
        self.action_history: list[dict] = []

        # Default dangerous actions
        self.blocked_actions = {
            "delete_production_data",
            "modify_security_settings",
            "access_financial_systems"
        }

        self.require_approval = {
            "deploy_to_production",
            "send_external_email",
            "modify_user_permissions"
        }

    async def evaluate_action(self, action: str, context: dict) -> dict:
        \"\"\"Evaluate if an action is safe to perform.\"\"\"
        # Check explicit blocks
        if action in self.blocked_actions:
            return {
                "allowed": False,
                "reason": "Action is explicitly blocked",
                "risk_level": RiskLevel.CRITICAL
            }

        # Check if approval required
        if action in self.require_approval:
            return {
                "allowed": False,
                "reason": "Action requires human approval",
                "risk_level": RiskLevel.HIGH,
                "approval_required": True
            }

        # LLM-based risk assessment
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": \"\"\"
                Evaluate the safety risk of this action.
                Return JSON: {
                    "risk_level": "safe|low|medium|high|critical",
                    "concerns": ["concern 1"],
                    "mitigation": "how to reduce risk"
                }
                \"\"\"},
                {"role": "user", "content": f\"\"\"
                Action: {action}
                Context: {context}
                Recent actions: {self.action_history[-10:]}
                \"\"\"}
            ]
        )

        assessment = json.loads(response.choices[0].message.content)
        risk = RiskLevel[assessment["risk_level"].upper()]

        # Record action
        self.action_history.append({
            "action": action,
            "risk_level": risk.name,
            "timestamp": datetime.now().isoformat()
        })

        return {
            "allowed": risk.value <= RiskLevel.MEDIUM.value,
            "risk_level": risk,
            "concerns": assessment["concerns"],
            "mitigation": assessment["mitigation"]
        }

    def detect_anomaly(self) -> Optional[str]:
        \"\"\"Detect anomalous behavior patterns.\"\"\"
        if len(self.action_history) < 10:
            return None

        recent = self.action_history[-20:]

        # Check for repeated failures
        failures = [a for a in recent if a.get("outcome") == "failure"]
        if len(failures) > 5:
            return "High failure rate detected - agent may be stuck"

        # Check for escalating risk
        risk_levels = [RiskLevel[a["risk_level"]].value for a in recent]
        if sum(risk_levels[-5:]) > sum(risk_levels[:5]):
            return "Risk level escalation detected"

        return None

    def emergency_stop(self):
        \"\"\"Emergency stop the agent.\"\"\"
        # In production: actually stop the agent
        print("🚨 EMERGENCY STOP TRIGGERED")
        raise SystemExit("Emergency stop triggered by safety system")
```

### 5. Complete Autonomous Agent

```python
class AutonomousAgent:
    \"\"\"Fully autonomous agent with goal-driven behavior.\"\"\"

    def __init__(self, name: str, tools: list):
        self.name = name
        self.tools = {t.name: t for t in tools}

        self.goal_manager = GoalManager()
        self.planner = StrategicPlanner()
        self.learning = LearningSystem()
        self.safety = SafetyGuardrails()

        self._running = False

    async def run(self, primary_goal: str, constraints: list[str] = None):
        \"\"\"Run the agent autonomously towards a goal.\"\"\"
        self._running = True

        # Set primary goal
        goal = self.goal_manager.set_primary_goal(primary_goal, constraints)

        # Decompose into sub-goals
        await self.goal_manager.decompose_goal("primary")

        while self._running:
            # Safety check
            anomaly = self.safety.detect_anomaly()
            if anomaly:
                print(f"⚠️ Anomaly detected: {anomaly}")
                # Could pause and request human review here

            # Get next goal
            current_goal = self.goal_manager.get_next_goal()

            if not current_goal:
                print("✅ All goals completed!")
                break

            print(f"📎 Working on: {current_goal.description}")

            # Get advice from past experience
            advice = await self.learning.suggest_approach(current_goal.description)
            print(f"💡 Suggested approach (confidence: {advice['confidence']:.0%})")

            # Create plan
            plan = await self.planner.create_plan(
                current_goal,
                context={"advice": advice},
                available_tools=list(self.tools.keys())
            )

            # Execute plan
            success = await self._execute_plan(plan)

            # Learn from outcome
            await self.learning.learn_from_outcome(
                task=current_goal.description,
                approach=str(plan.steps),
                outcome="success" if success else "failure"
            )

            # Update goal status
            self.goal_manager.update_progress(
                current_goal.id,
                progress=1.0 if success else current_goal.progress,
                status=GoalStatus.COMPLETED if success else GoalStatus.BLOCKED
            )

    async def _execute_plan(self, plan: Plan) -> bool:
        \"\"\"Execute a plan step by step.\"\"\"
        for step in plan.steps:
            # Safety check
            evaluation = await self.safety.evaluate_action(
                step["description"],
                {"step": step, "plan_id": plan.id}
            )

            if not evaluation["allowed"]:
                if evaluation.get("approval_required"):
                    # Request human approval
                    approved = await self._request_approval(step)
                    if not approved:
                        return False
                else:
                    print(f"❌ Action blocked: {evaluation['reason']}")
                    return False

            # Execute step
            if step.get("tool"):
                tool = self.tools.get(step["tool"])
                if tool:
                    result = await tool.execute(step.get("args", {}))
                    if not result.success and not step.get("can_fail"):
                        return False

            print(f"  ✓ Completed: {step['description']}")

        return True

    async def _request_approval(self, step: dict) -> bool:
        \"\"\"Request human approval for risky action.\"\"\"
        print(f"\\n🔐 APPROVAL REQUIRED")
        print(f"Action: {step['description']}")
        response = input("Approve? (y/n): ")
        return response.lower() == 'y'

    def stop(self):
        self._running = False

# Usage
agent = AutonomousAgent(
    name="DevOps Autonomous Agent",
    tools=[deploy_tool, monitor_tool, scale_tool]
)

await agent.run(
    primary_goal="Migrate auth-service to new Kubernetes cluster",
    constraints=[
        "Zero downtime",
        "Budget max $100",
        "Complete within 24 hours"
    ]
)
```

## Praktisk övning

**Uppgift:** Implementera Goal Prioritization

Se slutet av modulen för övningsuppgift.

## Sammanfattning

- ✅ **Goal systems** för autonomous behavior
- ✅ **Strategic planning** för long-term tasks
- ✅ **Learning systems** för improvement over time
- ✅ **Safety guardrails** — KRITISKT för autonoma agenter

## Nästa steg

- **Node 20:** The Future of AI Agents

---
*Pro tip: Autonomi är ett spektrum — börja med lite autonomi och öka gradvis!*
"""
    },
    {
        "id": "ai-agents-20",
        "slug": "future-of-ai-agents",
        "title": "The Future of AI Agents",
        "order_index": 20,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-19"],
        "content": """# The Future of AI Agents

## Varför detta är viktigt

AI-agenter utvecklas snabbare än något annat område inom tech. Att förstå
trenderna hjälper dig:

- **Förbereda** din infrastruktur för kommande capabilities
- **Investera rätt** i teknologier med staying power
- **Undvika** dead ends och hype cycles
- **Positionera** dig för framtidens möjligheter

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Identifiera emerging trends inom AI agents
- ✅ Förstå teknologiska milstolpar på vägen
- ✅ Utvärdera nya frameworks och verktyg
- ✅ Planera för framtida agent capabilities
- ✅ Förstå ethical och societal implications

## Emerging Trends

### 1. Agentic AI Wave

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENTIC AI EVOLUTION                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  2022                2023                2024                2025+          │
│  ─────────────────────────────────────────────────────────────────────────► │
│                                                                              │
│  ChatGPT             LangChain          OpenAI Swarm        Multi-Agent     │
│  (Conversational)    (Chains)           (Native agents)     Ecosystems      │
│                                                                              │
│                      AutoGPT            Claude Computer     Agent-to-Agent  │
│                      (Autonomous)       Use (UI Control)    Marketplaces    │
│                                                                              │
│                      BabyAGI            Devin               Specialized     │
│                      (Task agents)      (Coding agent)      Agent Teams     │
│                                                                              │
│  Key Shifts:                                                                │
│  • From prompts → to tools → to planning                                   │
│  • From single model → to orchestrated systems                             │
│  • From human-in-loop → to supervised autonomy                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2. Capability Roadmap

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CAPABILITY ROADMAP                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  NOW (2024)                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ✅ Function calling & tool use                                     │   │
│  │  ✅ Multi-step reasoning (ReAct, CoT)                               │   │
│  │  ✅ RAG & document understanding                                    │   │
│  │  ✅ Code generation & execution                                     │   │
│  │  ✅ Basic multi-agent coordination                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  NEAR-TERM (2025)                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🔄 Computer/browser use (clicking, typing)                         │   │
│  │  🔄 Long-term memory & personalization                              │   │
│  │  🔄 Multi-modal agents (vision + audio + text)                      │   │
│  │  🔄 Native planning without prompt engineering                      │   │
│  │  🔄 Self-debugging & correction                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  MID-TERM (2026-2027)                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🔮 True multi-agent collaboration at scale                         │   │
│  │  🔮 Domain expert agents (legal, medical, engineering)              │   │
│  │  🔮 Continuous learning without fine-tuning                         │   │
│  │  🔮 Agent-to-agent marketplaces                                     │   │
│  │  🔮 Formal verification of agent behavior                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  LONG-TERM (2028+)                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🌟 General-purpose autonomous agents                               │   │
│  │  🌟 Scientific discovery agents                                     │   │
│  │  🌟 Self-improving agent systems                                    │   │
│  │  🌟 ???                                                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Architecture Evolution

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARCHITECTURE EVOLUTION                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TODAY: Monolithic Agents                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │     ┌─────────────────────────────────────────────┐                 │   │
│  │     │               SINGLE AGENT                  │                 │   │
│  │     │   LLM + Tools + Memory + Planning          │                 │   │
│  │     │         (Everything in one)                 │                 │   │
│  │     └─────────────────────────────────────────────┘                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  EMERGING: Modular Agent Architecture                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │     ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐        │   │
│  │     │  Planner  │ │  Executor │ │  Memory   │ │  Learner  │        │   │
│  │     │  Service  │ │  Service  │ │  Service  │ │  Service  │        │   │
│  │     └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘        │   │
│  │           └─────────────┴─────────────┴─────────────┘               │   │
│  │                              │                                       │   │
│  │                    ┌─────────▼─────────┐                            │   │
│  │                    │   Orchestrator    │                            │   │
│  │                    └───────────────────┘                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  FUTURE: Agent Mesh                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │         Agent A ◄────────────────► Agent B                          │   │
│  │            ▲                           ▲                             │   │
│  │            │                           │                             │   │
│  │            │     ┌─────────────────┐   │                             │   │
│  │            └────►│   Agent Mesh    │◄──┘                             │   │
│  │                  │   (Discovery,   │                                 │   │
│  │                  │    Routing,     │                                 │   │
│  │            ┌────►│    Trust)       │◄──┐                             │   │
│  │            │     └─────────────────┘   │                             │   │
│  │            │                           │                             │   │
│  │            ▼                           ▼                             │   │
│  │         Agent C ◄────────────────► Agent D                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Technologies to Watch

### Model Context Protocol (MCP)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MODEL CONTEXT PROTOCOL (MCP)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Problem: Every agent framework has its own tool integration format        │
│                                                                              │
│  Solution: Universal protocol for LLM ↔ Tool communication                 │
│                                                                              │
│  ┌─────────────────┐    MCP     ┌─────────────────┐                        │
│  │     Claude      │◄──────────►│    Tool Server  │                        │
│  └─────────────────┘            │  (GitHub, Slack │                        │
│                                 │   Database...)  │                        │
│  ┌─────────────────┐    MCP     └─────────────────┘                        │
│  │     GPT-4       │◄──────────►│                                          │
│  └─────────────────┘            │                                          │
│                                                                              │
│  Benefits:                                                                   │
│  • Write tool once, use with any LLM                                       │
│  • Standardized security model                                             │
│  • Growing ecosystem of MCP servers                                        │
│                                                                              │
│  Example MCP Server:                                                        │
│  ```python                                                                  │
│  @mcp.tool()                                                                │
│  def search_codebase(query: str) -> list[CodeResult]:                      │
│      \"\"\"Search codebase for relevant code.\"\"\"                            │
│      return search_engine.search(query)                                    │
│  ```                                                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Computer Use / UI Agents

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPUTER USE AGENTS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Instead of: Writing code to integrate with APIs                           │
│  Future: Agent uses apps like a human would                                │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │     ┌───────────────────────────────────────────────────────────┐   │   │
│  │     │   [Chrome Browser - Jira]                                 │   │   │
│  │     │   ┌─────────────────────────────────────────────────────┐ │   │   │
│  │     │   │  Create New Issue                                   │ │   │   │
│  │     │   │  Title: [_________________]  ◄── Agent types here   │ │   │   │
│  │     │   │  Description: [___________]                         │ │   │   │
│  │     │   │  [Create Issue] ◄── Agent clicks here               │ │   │   │
│  │     │   └─────────────────────────────────────────────────────┘ │   │   │
│  │     └───────────────────────────────────────────────────────────┘   │   │
│  │                                                                      │   │
│  │     Agent Vision: "I see a form with Title and Description fields"  │   │
│  │     Agent Action: type("Title", "Fix login bug")                    │   │
│  │                   click("Create Issue")                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Implications:                                                               │
│  • No API integration needed for any app                                   │
│  • Works with legacy systems                                               │
│  • Security concerns (agent has UI access)                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Preparing Your Architecture

### Future-Proof Design Principles

```python
\"\"\"
Design principles for future-proof agent systems.
\"\"\"

# 1. MODULAR ARCHITECTURE
# Don't build monolithic agents - separate concerns

class ModularAgent:
    def __init__(self):
        self.planner = PlannerModule()      # Swappable
        self.executor = ExecutorModule()     # Swappable
        self.memory = MemoryModule()         # Swappable
        self.safety = SafetyModule()         # Swappable

    # Easy to upgrade individual components

# 2. ABSTRACTION LAYERS
# Don't couple to specific LLM providers

class LLMInterface(Protocol):
    async def complete(self, messages: list[dict]) -> str:
        ...

    async def stream(self, messages: list[dict]) -> AsyncIterator[str]:
        ...

# Can swap OpenAI for Anthropic, local models, etc.

# 3. TOOL STANDARD
# Use emerging standards like MCP

from mcp import MCPServer, tool

@tool
def my_tool(param: str) -> dict:
    \"\"\"Works with any MCP-compatible agent.\"\"\"
    pass

# 4. OBSERVABILITY FIRST
# Build in tracing, metrics, logging from day 1

class ObservableAgent:
    @traced
    @metered
    async def process(self, input: str):
        # All calls are automatically tracked
        pass

# 5. SAFETY BY DESIGN
# Don't add safety as an afterthought

class SafeAgent:
    def __init__(self):
        self.guardrails = SafetyGuardrails()  # Always on
        self.audit_log = AuditLog()           # Always logging
        self.rate_limiter = RateLimiter()     # Always enforced
```

## Ethical Considerations

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ETHICAL CONSIDERATIONS                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TRANSPARENCY                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Users should know when they're talking to an agent               │   │
│  │  • Agent decisions should be explainable                            │   │
│  │  • Audit trails for all autonomous actions                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ACCOUNTABILITY                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Who is responsible when an agent makes a mistake?                │   │
│  │  • Clear ownership of agent behavior                                │   │
│  │  • Insurance and liability frameworks                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  SAFETY                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Prevent agents from causing harm                                 │   │
│  │  • Graceful degradation when uncertain                              │   │
│  │  • Human override always available                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  JOB IMPACT                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Augment humans, don't just replace                               │   │
│  │  • Reskilling programs                                              │   │
│  │  • Thoughtful deployment                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Your Next Steps

### Learning Path Forward

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    YOUR LEARNING PATH                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. BUILD: Create a production agent                                        │
│     • Pick a real use case at work                                         │
│     • Implement with proper safety, monitoring                             │
│     • Learn from production issues                                         │
│                                                                              │
│  2. EXPERIMENT: Try new frameworks                                          │
│     • LangGraph for stateful agents                                        │
│     • CrewAI for multi-agent                                               │
│     • MCP for tool integration                                             │
│                                                                              │
│  3. CONTRIBUTE: Join the community                                          │
│     • Open source agent frameworks                                         │
│     • Share learnings via blog/talks                                       │
│     • Build tools others can use                                           │
│                                                                              │
│  4. STAY CURRENT: Follow developments                                       │
│     • LLM release notes                                                    │
│     • Research papers (especially from labs)                               │
│     • Community discussions                                                │
│                                                                              │
│  Resources:                                                                  │
│  • Simon Willison's blog (simonwillison.net)                              │
│  • Latent Space podcast                                                    │
│  • AI Engineer Summit talks                                                │
│  • Papers with Code - Agents                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Final Thoughts

AI agents represent one of the most exciting frontiers in software development.
The field is moving fast, but the fundamentals you've learned in this course will
serve you well:

- **Reasoning patterns** (ReAct, CoT) are here to stay
- **Tool use** is becoming standardized
- **Safety** will only become more important
- **Multi-agent** systems are the future

Most importantly: **Build things**. The best way to learn is by doing.

---

## 🎉 Grattis!

Du har slutfört AI Agents SkillsMap!

Du har lärt dig:
- ✅ LLM fundamentals och hur agenter tänker
- ✅ Tool design och function calling
- ✅ Agent frameworks (LangChain, LlamaIndex, AutoGen)
- ✅ Memory och state management
- ✅ Multi-agent orchestration
- ✅ Production deployment
- ✅ Monitoring och observability
- ✅ Autonomous agents och framtiden

**Vad händer nu?**

1. **Bygg en agent** för ett riktigt problem
2. **Dela dina lärdomar** med communityn
3. **Fortsätt lära** — fältet utvecklas snabbt!

---
*"The best way to predict the future is to build it." — Alan Kay*
"""
    }
]
