# =============================================================================
# BLOCK 5: APPLICATIONS (Noder 17-20)
# =============================================================================

NODE_17_EVALUATION = {
    "node_id": 17,
    "title": "Evaluation & Testing",
    "slug": "evaluation",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [8, 13],
    "content": '''
# Evaluation & Testing

Mät och förbättra prompt-prestanda.

## Varför utvärdera?

```yaml
Problem:
  - "Känns bra" är inte tillräckligt
  - Prompts kan degradera över tid
  - Modelluppdateringar ändrar beteende

Lösning:
  - Systematisk utvärdering
  - Reproducerbara tester
  - Metrics som speglar verkliga mål
```

## Evaluation Metrics

```python
# 1. Exakthet (för klassificering)
def accuracy(predictions, labels):
    correct = sum(p == l for p, l in zip(predictions, labels))
    return correct / len(labels)

# 2. F1-Score
from sklearn.metrics import f1_score
f1 = f1_score(labels, predictions, average='weighted')

# 3. BLEU (för översättning/generering)
from nltk.translate.bleu_score import sentence_bleu
score = sentence_bleu([reference.split()], candidate.split())

# 4. ROUGE (för sammanfattning)
from rouge_score import rouge_scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'])
scores = scorer.score(reference, generated)

# 5. Custom metric
def custom_metric(response, expected):
    """Kontrollera om svaret innehåller rätt info"""
    required_elements = ["price", "features", "availability"]
    found = sum(1 for el in required_elements if el in response.lower())
    return found / len(required_elements)
```

## Test Dataset

```python
# Skapa test dataset
test_cases = [
    {
        "input": "Klassificera: Produkten är fantastisk!",
        "expected": "POSITIV",
        "category": "sentiment"
    },
    {
        "input": "Klassificera: Helt värdelös, pengarna tillbaka!",
        "expected": "NEGATIV",
        "category": "sentiment"
    },
    # ... fler cases
]

def run_evaluation(prompt_template, test_cases):
    results = []

    for case in test_cases:
        prompt = prompt_template.format(input=case["input"])
        response = generate(prompt, temperature=0)

        is_correct = response.strip().upper() == case["expected"]
        results.append({
            "input": case["input"],
            "expected": case["expected"],
            "actual": response,
            "correct": is_correct
        })

    accuracy = sum(r["correct"] for r in results) / len(results)
    return accuracy, results
```

## LLM-as-Judge

```python
def llm_judge(response, criteria):
    """Använd LLM för att utvärdera kvalitet"""

    judge_prompt = f"""Du är en objektiv utvärderare.

Utvärdera följande svar mot kriterierna.

SVAR ATT UTVÄRDERA:
{response}

KRITERIER:
{criteria}

Ge poäng 1-10 för varje kriterium och motivera kort.

Format:
Kriterium 1: [poäng] - [motivering]
Kriterium 2: [poäng] - [motivering]
...
Totalpoäng: [genomsnitt]
"""

    return generate(judge_prompt, temperature=0)

# Användning
criteria = """
1. Korrekthet: Är informationen faktamässigt korrekt?
2. Fullständighet: Besvaras frågan fullständigt?
3. Tydlighet: Är svaret lätt att förstå?
4. Relevans: Håller sig svaret till ämnet?
"""

score = llm_judge(ai_response, criteria)
```

## Evaluation Framework

```python
class PromptEvaluator:
    def __init__(self, test_cases):
        self.test_cases = test_cases
        self.results = {}

    def evaluate_prompt(self, prompt_name, prompt_template,
                        metrics=['accuracy', 'llm_judge']):
        scores = {}
        predictions = []

        # Generera svar
        for case in self.test_cases:
            response = generate(
                prompt_template.format(**case),
                temperature=0
            )
            predictions.append({
                **case,
                "prediction": response
            })

        # Beräkna metrics
        if 'accuracy' in metrics:
            correct = sum(
                p["prediction"].strip() == p["expected"]
                for p in predictions
            )
            scores['accuracy'] = correct / len(predictions)

        if 'llm_judge' in metrics:
            judge_scores = []
            for p in predictions:
                score = self.llm_evaluate(p["prediction"])
                judge_scores.append(score)
            scores['llm_judge'] = sum(judge_scores) / len(judge_scores)

        self.results[prompt_name] = scores
        return scores

    def compare_prompts(self):
        """Jämför alla utvärderade prompts"""
        return pd.DataFrame(self.results).T

# Användning
evaluator = PromptEvaluator(test_cases)

evaluator.evaluate_prompt("v1", prompt_v1)
evaluator.evaluate_prompt("v2", prompt_v2)
evaluator.evaluate_prompt("v3", prompt_v3)

comparison = evaluator.compare_prompts()
print(comparison)
```

## Regression Testing

```python
def regression_test(prompt, baseline_results, threshold=0.95):
    """Kontrollera att prompt inte degraderat"""

    current_results = run_evaluation(prompt, test_cases)

    baseline_accuracy = baseline_results['accuracy']
    current_accuracy = current_results['accuracy']

    if current_accuracy < baseline_accuracy * threshold:
        raise RegressionError(
            f"Accuracy dropped from {baseline_accuracy:.2%} "
            f"to {current_accuracy:.2%}"
        )

    # Jämför individuella cases
    failures = []
    for base, curr in zip(baseline_results['cases'],
                          current_results['cases']):
        if base['correct'] and not curr['correct']:
            failures.append({
                'input': curr['input'],
                'was': base['actual'],
                'now': curr['actual']
            })

    return {
        'passed': len(failures) == 0,
        'accuracy_change': current_accuracy - baseline_accuracy,
        'regressions': failures
    }
```

## CI/CD Integration

```yaml
# .github/workflows/prompt-tests.yml
name: Prompt Regression Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run prompt tests
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python -m pytest tests/prompts/ -v

      - name: Compare with baseline
        run: python scripts/compare_baseline.py
```

| Metric | Användning |
|--------|------------|
| Accuracy | Klassificering |
| F1 Score | Obalanserade dataset |
| BLEU/ROUGE | Generering |
| LLM-as-Judge | Subjektiv kvalitet |
| Latency | Prestanda |
| Cost | Token-effektivitet |

**Nästa steg:** Node 18 - Production Patterns
''',
}

NODE_18_PRODUCTION = {
    "node_id": 18,
    "title": "Production Patterns",
    "slug": "production",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [13, 15, 17],
    "content": '''
# Production Patterns

Bygg robusta AI-system för produktion.

## Prompt Management

```python
# Prompt versioning och management
class PromptRegistry:
    def __init__(self):
        self.prompts = {}
        self.versions = {}

    def register(self, name, prompt, version="1.0.0"):
        key = f"{name}:{version}"
        self.prompts[key] = prompt

        if name not in self.versions:
            self.versions[name] = []
        self.versions[name].append(version)

    def get(self, name, version="latest"):
        if version == "latest":
            version = max(self.versions[name])
        return self.prompts[f"{name}:{version}"]

    def rollback(self, name, version):
        """Rollback till tidigare version"""
        return self.get(name, version)

registry = PromptRegistry()

registry.register("classifier", classifier_v1, "1.0.0")
registry.register("classifier", classifier_v2, "1.1.0")  # Ny version

# I produktion
prompt = registry.get("classifier")  # Senaste
```

## Caching

```python
import hashlib
import redis
import json

class PromptCache:
    def __init__(self, redis_client, ttl=3600):
        self.redis = redis_client
        self.ttl = ttl

    def _cache_key(self, prompt, params):
        """Generera unik nyckel"""
        content = json.dumps({"prompt": prompt, "params": params})
        return f"llm:{hashlib.sha256(content.encode()).hexdigest()}"

    def get(self, prompt, params):
        key = self._cache_key(prompt, params)
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None

    def set(self, prompt, params, response):
        key = self._cache_key(prompt, params)
        self.redis.setex(key, self.ttl, json.dumps(response))

cache = PromptCache(redis.Redis())

def cached_generate(prompt, **params):
    # Kolla cache
    cached = cache.get(prompt, params)
    if cached:
        return cached

    # Generera
    response = generate(prompt, **params)

    # Cacha
    cache.set(prompt, params, response)

    return response
```

## Rate Limiting & Retry

```python
import time
from tenacity import retry, stop_after_attempt, wait_exponential

class RateLimiter:
    def __init__(self, requests_per_minute=60):
        self.rpm = requests_per_minute
        self.requests = []

    def wait_if_needed(self):
        now = time.time()
        self.requests = [r for r in self.requests if now - r < 60]

        if len(self.requests) >= self.rpm:
            sleep_time = 60 - (now - self.requests[0])
            time.sleep(sleep_time)

        self.requests.append(time.time())

limiter = RateLimiter(requests_per_minute=50)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=60)
)
def robust_generate(prompt, **params):
    limiter.wait_if_needed()

    try:
        return client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            **params
        )
    except openai.RateLimitError:
        raise  # Retry via tenacity
    except openai.APIError as e:
        logger.error(f"API Error: {e}")
        raise
```

## Fallback Strategies

```python
class LLMWithFallback:
    def __init__(self, primary, fallbacks):
        self.primary = primary
        self.fallbacks = fallbacks

    def generate(self, prompt, **params):
        # Försök primary
        try:
            return self.primary.generate(prompt, **params)
        except Exception as e:
            logger.warning(f"Primary failed: {e}")

        # Försök fallbacks i ordning
        for fallback in self.fallbacks:
            try:
                return fallback.generate(prompt, **params)
            except Exception as e:
                logger.warning(f"Fallback failed: {e}")

        raise RuntimeError("All LLM providers failed")

llm = LLMWithFallback(
    primary=OpenAIClient(),
    fallbacks=[AnthropicClient(), GeminiClient()]
)
```

## Monitoring & Observability

```python
import time
from prometheus_client import Counter, Histogram, start_http_server

# Metrics
llm_requests = Counter(
    'llm_requests_total',
    'Total LLM requests',
    ['model', 'status']
)

llm_latency = Histogram(
    'llm_request_duration_seconds',
    'LLM request latency',
    ['model']
)

llm_tokens = Counter(
    'llm_tokens_total',
    'Total tokens used',
    ['model', 'type']  # input/output
)

def monitored_generate(prompt, model="gpt-4o", **params):
    start = time.time()

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **params
        )

        # Record metrics
        llm_requests.labels(model=model, status='success').inc()
        llm_latency.labels(model=model).observe(time.time() - start)
        llm_tokens.labels(model=model, type='input').inc(
            response.usage.prompt_tokens
        )
        llm_tokens.labels(model=model, type='output').inc(
            response.usage.completion_tokens
        )

        return response

    except Exception as e:
        llm_requests.labels(model=model, status='error').inc()
        raise
```

## Logging Best Practices

```python
import logging
import structlog

logger = structlog.get_logger()

def logged_generate(prompt, **params):
    request_id = generate_request_id()

    logger.info(
        "llm_request_started",
        request_id=request_id,
        model=params.get("model", "gpt-4o"),
        prompt_length=len(prompt)
    )

    try:
        response = generate(prompt, **params)

        logger.info(
            "llm_request_completed",
            request_id=request_id,
            tokens_used=response.usage.total_tokens,
            finish_reason=response.choices[0].finish_reason
        )

        return response

    except Exception as e:
        logger.error(
            "llm_request_failed",
            request_id=request_id,
            error=str(e),
            error_type=type(e).__name__
        )
        raise
```

## Cost Control

```python
class CostController:
    def __init__(self, daily_limit_usd=100):
        self.daily_limit = daily_limit_usd
        self.daily_cost = 0
        self.last_reset = datetime.now().date()

    def check_budget(self, estimated_tokens):
        # Reset dagligen
        if datetime.now().date() > self.last_reset:
            self.daily_cost = 0
            self.last_reset = datetime.now().date()

        estimated_cost = self.estimate_cost(estimated_tokens)

        if self.daily_cost + estimated_cost > self.daily_limit:
            raise BudgetExceededError(
                f"Would exceed daily limit: ${self.daily_limit}"
            )

    def record_usage(self, usage):
        cost = self.calculate_cost(usage)
        self.daily_cost += cost

    def estimate_cost(self, tokens, model="gpt-4o"):
        prices = {
            "gpt-4o": {"input": 0.005, "output": 0.015},
            "gpt-4o-mini": {"input": 0.00015, "output": 0.0006}
        }
        return (tokens / 1000) * prices[model]["input"]
```

| Pattern | Syfte |
|---------|-------|
| Prompt Registry | Versionshantering |
| Caching | Kostnad, latency |
| Rate Limiting | API-skydd |
| Fallbacks | Tillgänglighet |
| Monitoring | Observerbarhet |
| Cost Control | Budget |

**Nästa steg:** Node 19 - Building AI Agents
''',
}

NODE_19_AGENTS = {
    "node_id": 19,
    "title": "Building AI Agents",
    "slug": "agents",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [12, 13],
    "content": '''
# Building AI Agents

Skapa autonoma AI-system som utför uppgifter.

## Vad är en AI Agent?

```yaml
Definition:
  Ett AI-system som kan:
  - Fatta beslut autonomt
  - Använda verktyg
  - Iterera mot ett mål
  - Lära sig från feedback

Komponenter:
  1. LLM (hjärnan)
  2. Verktyg (händerna)
  3. Minne (erfarenhet)
  4. Planner (strategi)
```

## Basic Agent Architecture

```text
┌─────────────────────────────────────────────────────┐
│                    USER QUERY                       │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│                    PLANNER                          │
│  "Hur ska jag lösa detta?"                          │
└─────────────────────────────────────────────────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ TOOL 1  │   │ TOOL 2  │   │ TOOL 3  │
    │ Search  │   │ Code    │   │ Write   │
    └─────────┘   └─────────┘   └─────────┘
          │             │             │
          └─────────────┼─────────────┘
                        ▼
┌─────────────────────────────────────────────────────┐
│                    EXECUTOR                         │
│  Kör verktyg, samla resultat                        │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│                    MEMORY                           │
│  Tidigare actions, observations, reflections       │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
                   [REPEAT UNTIL DONE]
```

## Simple Agent Implementation

```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class Tool:
    name: str
    description: str
    function: Callable

class SimpleAgent:
    def __init__(self, tools: list[Tool]):
        self.tools = {t.name: t for t in tools}
        self.memory = []

    def run(self, task: str, max_iterations: int = 10):
        self.memory.append({"role": "user", "content": task})

        for i in range(max_iterations):
            # Be LLM planera nästa steg
            action = self._plan()

            if action["type"] == "finish":
                return action["output"]

            # Kör verktyg
            result = self._execute(action)

            # Lägg till i minne
            self.memory.append({
                "role": "observation",
                "content": f"{action['tool']}: {result}"
            })

        return "Max iterations reached"

    def _plan(self):
        tools_desc = "\\n".join([
            f"- {t.name}: {t.description}"
            for t in self.tools.values()
        ])

        prompt = f"""Du är en AI-agent med dessa verktyg:
{tools_desc}
- finish: Ge slutsvar

Konversationshistorik:
{self._format_memory()}

Vad är nästa steg? Svara i JSON:
{{"type": "tool" eller "finish", "tool": "verktygsnamn", "input": "...", "output": "..."}}
"""

        response = generate(prompt, temperature=0)
        return json.loads(response)

    def _execute(self, action):
        tool = self.tools.get(action["tool"])
        if not tool:
            return f"Unknown tool: {action['tool']}"
        return tool.function(action["input"])
```

## OpenAI Function Calling

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Sök på internet efter information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Sökfrågan"
                    }
                },
                "required": ["query"]
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
                        "description": "Matematiskt uttryck"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def run_agent(query):
    messages = [{"role": "user", "content": query}]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools
        )

        msg = response.choices[0].message

        # Klar?
        if msg.tool_calls is None:
            return msg.content

        # Kör verktyg
        messages.append(msg)

        for tool_call in msg.tool_calls:
            result = execute_function(
                tool_call.function.name,
                json.loads(tool_call.function.arguments)
            )

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
```

## LangChain Agent

```python
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain import hub

# Verktyg
tools = [
    Tool(
        name="Search",
        func=search_function,
        description="Sök på internet"
    ),
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="Matematiska beräkningar"
    )
]

# Prompt
prompt = hub.pull("hwchase17/openai-functions-agent")

# LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Agent
agent = create_openai_functions_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Kör
result = executor.invoke({
    "input": "Vad är 15% av Amazon's nuvarande aktiekurs?"
})
```

## Memory Types

```python
# 1. Conversation Memory
class ConversationMemory:
    def __init__(self, max_messages=20):
        self.messages = []
        self.max_messages = max_messages

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

# 2. Semantic Memory (RAG)
class SemanticMemory:
    def __init__(self, vector_store):
        self.store = vector_store

    def remember(self, text):
        embedding = get_embedding(text)
        self.store.add(text, embedding)

    def recall(self, query, top_k=5):
        embedding = get_embedding(query)
        return self.store.search(embedding, top_k)

# 3. Entity Memory
class EntityMemory:
    def __init__(self):
        self.entities = {}

    def update(self, entity, info):
        if entity not in self.entities:
            self.entities[entity] = {}
        self.entities[entity].update(info)
```

## Agent Best Practices

```yaml
Design:
  - Tydliga verktyg med bra descriptions
  - Begränsa antal verktyg (5-10 max)
  - Strukturerade outputs
  - Tydliga stop-conditions

Safety:
  - Sandboxed execution
  - Human-in-the-loop för kritiska actions
  - Rate limiting
  - Action logging

Performance:
  - Cachea verktygsresultat
  - Parallella tool calls när möjligt
  - Lämplig modell för varje steg
```

| Framework | Styrka |
|-----------|--------|
| LangChain | Flexibelt, många integrationer |
| LlamaIndex | Bäst för RAG |
| Autogen | Multi-agent |
| CrewAI | Rollbaserade agents |
| OpenAI Assistants | Managed, enkelt |

**Nästa steg:** Node 20 - Future of Prompting
''',
}

NODE_20_FUTURE = {
    "node_id": 20,
    "title": "Future of Prompting",
    "slug": "future",
    "estimated_minutes": 40,
    "xp_reward": 130,
    "prerequisites": [1],
    "content": '''
# Future of Prompting

Vart är prompt engineering på väg?

## Aktuella trender

```yaml
1. Längre Context Windows:
   - 1M+ tokens (Gemini)
   - Hela kodbasar i context
   - "RAG-less" approaches

2. Multimodal by Default:
   - Text + bild + ljud + video
   - Native förståelse
   - Computer use (screen interaction)

3. Reasoning Models:
   - o1, o3 (OpenAI)
   - Inbyggt chain-of-thought
   - Mindre beroende av prompt-tricks

4. Tool Use & Agents:
   - Function calling standard
   - MCP (Model Context Protocol)
   - Autonoma system
```

## Prompting vs Fine-tuning vs RAG

```yaml
Framtiden:
  - Prompting: Snabb prototyping, flexibilitet
  - Fine-tuning: Domänspecifik performance
  - RAG: Uppdaterad, verifierbar info

Trend:
  Base models blir så bra att fine-tuning
  behövs mer sällan. RAG + prompting täcker
  de flesta användningsfall.
```

## Declarative Prompting

```python
# Istället för att skriva detaljerade prompts...
# ...deklarera vad du vill ha

# DSPy approach
class QuestionAnswering(dspy.Signature):
    """Answer questions based on context."""
    context = dspy.InputField()
    question = dspy.InputField()
    answer = dspy.OutputField()

# Systemet optimerar prompten automatiskt

# TypeChat approach (Microsoft)
from typechat import create_json_translator

schema = '''
interface SentimentResult {
    sentiment: "positive" | "negative" | "neutral";
    confidence: number;  // 0-1
    keywords: string[];
}
'''

translator = create_json_translator(schema)
result = translator.translate("Amazing product, love it!")
# Automatiskt korrekt JSON-output
```

## Model Context Protocol (MCP)

```yaml
MCP:
  - Standard för tool/context integration
  - Lanserad av Anthropic nov 2024
  - Separerar AI från verktyg

Fördelar:
  - Återanvändbara integrationer
  - Mindre vendor lock-in
  - Enklare agent-utveckling
```

```python
# MCP Server (verktyg)
from mcp.server import Server

server = Server("my-tools")

@server.tool("search")
def search(query: str) -> str:
    """Search the web for information"""
    return perform_search(query)

@server.resource("files")
def list_files(path: str) -> list:
    """List files in directory"""
    return os.listdir(path)

# Kan användas av vilken MCP-kompatibel klient som helst
```

## Prompt-less Interfaces

```yaml
Vision:
  Mindre explicit prompting, mer naturlig interaktion

Exempel:
  1. Agentiska interfaces:
     - "Fixa buggen" → Agent söker, förstår, fixar

  2. Implicita prompts:
     - Kontext från kodeditor
     - Automatisk förståelse av uppgift

  3. Multimodal input:
     - Peka, rita, prata
     - Mindre text-beroende
```

## Emerging Patterns

```yaml
1. Constitutional AI:
   - Modeller med inbyggda principer
   - Mindre beroende av system prompts
   - Self-correction

2. Mixture of Experts (MoE):
   - Specialiserade sub-models
   - Routing baserat på uppgift
   - Effektivare compute

3. Small Language Models:
   - On-device AI
   - Privacy-first
   - Snabbare, billigare

4. Real-time AI:
   - Streaming responses
   - Voice-first interfaces
   - Live collaboration
```

## Skills som kommer vara viktiga

```yaml
Tekniska:
  - Agent design & orchestration
  - Evaluation & testing
  - Security & safety
  - Integration patterns

Icke-tekniska:
  - Problemformulering
  - Förståelse för LLM-begränsningar
  - Etik och ansvar
  - Domain expertise
```

## Practical Advice

```yaml
Nu:
  - Lär dig grunderna noggrant
  - Experimentera med olika modeller
  - Bygg verkliga projekt
  - Följ forskningen

Framtiden:
  - Fokusera på problem, inte prompts
  - Lär dig systemdesign
  - Förstå AI-säkerhet
  - Utveckla domain expertise
```

## Resurser för fortsatt lärande

```yaml
Dokumentation:
  - platform.openai.com/docs
  - docs.anthropic.com
  - ai.google.dev

Forskning:
  - arxiv.org (cs.CL, cs.AI)
  - paperswithcode.com

Community:
  - r/LocalLLaMA
  - Hugging Face
  - AI Discord-servers

Praktik:
  - Bygg agenter
  - Bidra till open source
  - Dela dina upptäckter
```

## Prompt Engineering SkillsMap Complete! 🎉

Du har lärt dig:

1. **Fundamentals** - LLMs, tokens, providers
2. **Configuration** - Sampling, output control
3. **Techniques** - CoT, ToT, ReAct
4. **Advanced** - Chaining, APE, security
5. **Applications** - Evaluation, production, agents

Fortsätt utvecklas:
- Bygg verkliga AI-produkter
- Experimentera med nya modeller
- Dela kunskap med andra
- Stay curious! 🚀
''',
}

PROMPT_BLOCK_5 = [
    NODE_17_EVALUATION,
    NODE_18_PRODUCTION,
    NODE_19_AGENTS,
    NODE_20_FUTURE,
]
