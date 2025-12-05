"""
AI Agents SkillsMap - Block 02: Model Mechanics
Nodes 3-4: Generation Controls, Open vs Closed Models
"""

BLOCK_02_NODES = [
    {
        "id": "ai-agents-03",
        "slug": "generation-controls",
        "title": "Generation Controls",
        "order_index": 3,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-02"],
        "content": """# Generation Controls: Temperature, Top-p och Mer

## Varför detta är viktigt

Dina AI-agenter kommer bete sig helt olika beroende på generation controls. En agent med
temperature=1.0 är kreativ men opålitlig. En agent med temperature=0.0 är konsekvent men
tråkig. Att förstå dessa parametrar är skillnaden mellan:

- En code-agent som ger **samma korrekta svar** varje gång
- En creative writing agent som **genererar unika** texter
- En data extraction agent som **aldrig hallucinerar**

Majoriteten av utvecklare använder default-värden och undrar varför deras agenter är inkonsistenta.
Du kommer inte göra samma misstag.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Förstå hur temperature påverkar token-sannolikheter
- ✅ Använda top-p (nucleus sampling) för kontrollerad variation
- ✅ Optimera frequency_penalty och presence_penalty för repetition
- ✅ Välja rätt inställningar för olika use cases
- ✅ Debugga inkonsistenta agent-beteenden

## Kärnkoncept

### Hur generation fungerar

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TOKEN GENERATION PROCESS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT: "The capital of France is"                                          │
│                                                                              │
│  STEP 1: Model outputs LOGITS (raw scores)                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  "Paris": 8.5  | "Lyon": 3.2  | "Berlin": 1.1  | "London": 0.8 | ...│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  STEP 2: Apply TEMPERATURE (divide logits)                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Temperature = 0.5 (more confident):                                 │   │
│  │    "Paris": 17.0 | "Lyon": 6.4 | "Berlin": 2.2 | "London": 1.6      │   │
│  │                                                                      │   │
│  │  Temperature = 1.0 (default):                                        │   │
│  │    "Paris": 8.5  | "Lyon": 3.2 | "Berlin": 1.1 | "London": 0.8      │   │
│  │                                                                      │   │
│  │  Temperature = 2.0 (more random):                                    │   │
│  │    "Paris": 4.25 | "Lyon": 1.6 | "Berlin": 0.55 | "London": 0.4     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  STEP 3: SOFTMAX → Probabilities                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Temp=0.5: "Paris" 99.9% | "Lyon" 0.1%  | others ~0%                │   │
│  │  Temp=1.0: "Paris" 95%   | "Lyon" 4%    | others ~1%                │   │
│  │  Temp=2.0: "Paris" 70%   | "Lyon" 15%   | others ~15%               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  STEP 4: SAMPLE from distribution                                           │
│  • temp=0 → Always pick highest (greedy/deterministic)                      │
│  • temp=1 → Sample according to probabilities                               │
│  • temp=2 → More uniform, anything can happen                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Generation Parameters

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    GENERATION PARAMETERS                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TEMPERATURE (0.0 - 2.0)                                                   │
│  ├─ 0.0: Deterministic (alltid samma output)                               │
│  ├─ 0.3: Low creativity (bra för kod, fakta)                               │
│  ├─ 0.7: Balanced (default för de flesta)                                  │
│  ├─ 1.0: Creative (stories, brainstorming)                                 │
│  └─ 2.0: Very random (experimental, ofta nonsens)                          │
│                                                                             │
│  TOP_P (0.0 - 1.0) - Nucleus Sampling                                      │
│  ├─ Väljer från tokens som utgör top P% av sannolikheten                   │
│  ├─ 0.1: Endast top tokens (extremt fokuserat)                             │
│  ├─ 0.9: De flesta tokens (default)                                        │
│  └─ 1.0: Alla tokens (ingen filtrering)                                    │
│                                                                             │
│  TOP_K (integer) - Inte alltid tillgängligt                                │
│  ├─ Väljer från top K tokens oavsett sannolikhet                           │
│  └─ 40-100 är vanliga värden                                               │
│                                                                             │
│  FREQUENCY_PENALTY (-2.0 - 2.0)                                            │
│  ├─ Straffar tokens baserat på hur ofta de redan använts                   │
│  ├─ 0.0: Ingen penalty (default)                                           │
│  ├─ 0.5: Mild anti-repetition                                              │
│  └─ 2.0: Stark anti-repetition (kan bli konstigt)                          │
│                                                                             │
│  PRESENCE_PENALTY (-2.0 - 2.0)                                             │
│  ├─ Straffar tokens som redan förekommit (oavsett frekvens)                │
│  ├─ 0.0: Ingen penalty                                                      │
│  └─ 1.0: Uppmuntrar nya ämnen                                              │
│                                                                             │
│  MAX_TOKENS (integer)                                                       │
│  ├─ Maximalt antal tokens i output                                         │
│  └─ Sätts ofta för att kontrollera kostnad                                 │
│                                                                             │
│  STOP_SEQUENCES (list[str])                                                │
│  ├─ Stoppar generation vid dessa strängar                                  │
│  └─ Användbart för strukturerad output                                     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### Rekommenderade inställningar per use case

| Use Case | Temperature | Top-p | Freq Penalty | Notes |
|----------|-------------|-------|--------------|-------|
| **Code generation** | 0.0-0.2 | 0.95 | 0 | Deterministic |
| **Data extraction** | 0.0 | 1.0 | 0 | Strict |
| **Q&A / Facts** | 0.3 | 0.9 | 0 | Slight variation OK |
| **Summarization** | 0.5 | 0.9 | 0.3 | Avoid repetition |
| **Creative writing** | 0.8-1.0 | 0.95 | 0.5 | More variation |
| **Brainstorming** | 1.0-1.2 | 1.0 | 0.7 | Maximum diversity |
| **Role-play/Chat** | 0.7-0.9 | 0.9 | 0.3 | Natural conversation |

## Steg-för-steg: Experimentera med controls

### 1. Setup

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate(
    prompt: str,
    temperature: float = 1.0,
    top_p: float = 1.0,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    max_tokens: int = 200,
    n: int = 1
) -> list[str]:
    \"\"\"Generera text med specificerade controls.\"\"\"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        max_tokens=max_tokens,
        n=n  # Antal completions att generera
    )
    return [choice.message.content for choice in response.choices]
```

### 2. Jämför temperature

```python
def compare_temperatures(prompt: str, temperatures: list[float], samples: int = 3):
    \"\"\"Visa hur temperature påverkar output.\"\"\"
    print(f"Prompt: {prompt}\\n")
    print("=" * 60)

    for temp in temperatures:
        print(f"\\n🌡️ Temperature = {temp}")
        print("-" * 40)

        # Generera flera samples för att visa variation
        outputs = generate(prompt, temperature=temp, n=samples)

        for i, output in enumerate(outputs, 1):
            print(f"  [{i}] {output[:100]}...")

        # Räkna unika outputs
        unique = len(set(outputs))
        print(f"  → Unika svar: {unique}/{samples}")

# Test
compare_temperatures(
    "Skriv ett företagsnamn för en AI-startup:",
    temperatures=[0.0, 0.5, 1.0, 1.5],
    samples=5
)
```

### 3. Top-p vs Temperature

```python
def compare_top_p(prompt: str):
    \"\"\"Visa skillnaden mellan top_p och temperature.\"\"\"
    print(f"Prompt: {prompt}\\n")

    configs = [
        {"temp": 1.0, "top_p": 0.1, "desc": "High temp, Low top_p"},
        {"temp": 1.0, "top_p": 0.9, "desc": "High temp, High top_p"},
        {"temp": 0.3, "top_p": 0.1, "desc": "Low temp, Low top_p"},
        {"temp": 0.3, "top_p": 0.9, "desc": "Low temp, High top_p"},
    ]

    for cfg in configs:
        outputs = generate(
            prompt,
            temperature=cfg["temp"],
            top_p=cfg["top_p"],
            n=3
        )
        unique = len(set(outputs))
        print(f"\\n{cfg['desc']}:")
        print(f"  Sample: {outputs[0][:80]}...")
        print(f"  Unique: {unique}/3")

compare_top_p("Komplettera meningen: Framtidens AI kommer att...")
```

### 4. Anti-repetition penalties

```python
def test_repetition_penalties(prompt: str):
    \"\"\"Visa effekten av frequency och presence penalty.\"\"\"

    # Prompt som tenderar att repetera sig
    repetitive_prompt = \"\"\"
    Skriv en lista med 10 anledningar till varför Python är bra.
    Var kreativ och undvik upprepningar.
    \"\"\"

    configs = [
        {"freq": 0.0, "pres": 0.0, "desc": "No penalties"},
        {"freq": 1.0, "pres": 0.0, "desc": "Frequency penalty only"},
        {"freq": 0.0, "pres": 1.0, "desc": "Presence penalty only"},
        {"freq": 0.5, "pres": 0.5, "desc": "Both penalties"},
    ]

    for cfg in configs:
        output = generate(
            repetitive_prompt,
            temperature=0.7,
            frequency_penalty=cfg["freq"],
            presence_penalty=cfg["pres"],
            max_tokens=300
        )[0]

        # Räkna upprepade ord
        words = output.lower().split()
        unique_ratio = len(set(words)) / len(words) if words else 0

        print(f"\\n{cfg['desc']} (unique word ratio: {unique_ratio:.1%}):")
        print(f"  {output[:200]}...")

test_repetition_penalties("Lista anledningar till att Python är bra")
```

### 5. Stop sequences

```python
def structured_output_with_stops():
    \"\"\"Använd stop sequences för kontrollerad output.\"\"\"

    # Extrahera bara svaret, inte förklaringen
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": "Vad är huvudstaden i Sverige? Svara med bara stadsnamnet."
        }],
        temperature=0,
        stop=[".", "\\n", ","],  # Stoppa vid punkt, newline eller komma
        max_tokens=50
    )

    print(f"Clean answer: '{response.choices[0].message.content}'")
    print(f"Stop reason: {response.choices[0].finish_reason}")

    # Mer avancerat: JSON-liknande output
    response2 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": \"\"\"
            Extrahera information som JSON:
            Text: "John är 25 år och bor i Stockholm"
            Format: {"name": "...", "age": ..., "city": "..."}
            \"\"\"
        }],
        temperature=0,
        stop=["\\n\\n", "```"],  # Stoppa före extra output
        max_tokens=100
    )

    print(f"\\nJSON output: {response2.choices[0].message.content}")

structured_output_with_stops()
```

## Vanliga problem

### Problem 1: "Olika svar varje gång (jag vill konsistens)"

```python
# Lösning: Använd temperature=0 och sätt seed
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Vad är 2+2?"}],
    temperature=0,
    seed=42  # Reproducerbarhet (beta feature)
)

# För maximal konsistens
DETERMINISTIC_CONFIG = {
    "temperature": 0,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "seed": 12345
}
```

### Problem 2: "Output är för repetitiv"

```python
# Lösning: Öka penalties
ANTI_REPETITION_CONFIG = {
    "temperature": 0.7,
    "frequency_penalty": 0.8,  # Straffa upprepade tokens
    "presence_penalty": 0.6,  # Uppmuntra nya ämnen
}

# För listor och brainstorming
DIVERSITY_CONFIG = {
    "temperature": 1.0,
    "frequency_penalty": 1.2,
    "presence_penalty": 1.0,
    "top_p": 0.95
}
```

### Problem 3: "Output är för wild/nonsens"

```python
# Lösning: Sänk temperature OCH top_p
FOCUSED_CONFIG = {
    "temperature": 0.3,
    "top_p": 0.8,  # Filtrera bort osannolika tokens
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

# Om det fortfarande är för random
STRICT_CONFIG = {
    "temperature": 0.1,
    "top_p": 0.5,
}
```

## Praktisk övning

**Uppgift:** Bygg en konfigurationsväljare

```python
from enum import Enum
from dataclasses import dataclass

class UseCase(Enum):
    CODE = "code"
    CREATIVE = "creative"
    FACTUAL = "factual"
    CHAT = "chat"
    EXTRACTION = "extraction"

@dataclass
class GenerationConfig:
    temperature: float
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    max_tokens: int

def get_config_for_use_case(use_case: UseCase) -> GenerationConfig:
    \"\"\"
    TODO: Returnera optimal konfiguration för varje use case.

    Implementera logik baserat på tabellen tidigare i modulen.
    \"\"\"
    configs = {
        UseCase.CODE: GenerationConfig(
            temperature=0.0,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            max_tokens=2000
        ),
        # Fyll i resten...
    }
    return configs.get(use_case)

# Test
for use_case in UseCase:
    config = get_config_for_use_case(use_case)
    print(f"{use_case.value}: temp={config.temperature}, top_p={config.top_p}")
```

## Sammanfattning

- ✅ **Temperature** kontrollerar randomness (0=deterministic, 2=chaos)
- ✅ **Top-p** filtrerar tokens baserat på kumulativ sannolikhet
- ✅ **Frequency/Presence penalty** minskar repetition
- ✅ **Stop sequences** ger kontrollerad output-längd
- ✅ **Seed** (beta) kan ge reproducerbara resultat

## Nästa steg

Nu när du behärskar generation controls, fortsätt till:

- **Node 4:** Open vs Closed Models — Välja mellan GPT, Claude, Llama
- **Node 5:** What are AI Agents? — Från LLM till Agent

---
*Pro tip: Börja alltid med default-värden och justera baserat på resultat!*
"""
    },
    {
        "id": "ai-agents-04",
        "slug": "open-vs-closed-models",
        "title": "Open vs Closed Models",
        "order_index": 4,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-03"],
        "content": """# Open vs Closed Weight Models

## Varför detta är viktigt

Valet mellan open-weight (Llama, Mistral) och closed (GPT-4, Claude) modeller kan betyda
skillnaden mellan $100/månad och $10,000/månad i driftskostnader. Det påverkar också:

- **Dataintegritet** — Lämnar din data ditt nätverk?
- **Latens** — 50ms lokalt vs 500ms API
- **Customization** — Kan du fine-tuna för din domän?
- **Vendor lock-in** — Vad händer om OpenAI höjer priserna 10x?

2024 såg en explosion av high-quality open models. Llama 3.1 405B matchar GPT-4 på många
benchmarks. Att förstå trade-offs är kritiskt för produktionsbeslut.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Kategorisera modeller som open-weight, open-source eller closed
- ✅ Jämföra prestanda, kostnad och latens för populära modeller
- ✅ Välja rätt deployment-strategi (API vs self-host)
- ✅ Förstå licenser (Apache 2.0, Llama License, etc.)
- ✅ Uppskatta infrastrukturkrav för self-hosting

## Kärnkoncept

### Modell-kategorier

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MODEL OPENNESS SPECTRUM                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CLOSED (Proprietary)                                                        │
│  ├─ Weights: ❌ Not available                                               │
│  ├─ Training data: ❌ Unknown                                               │
│  ├─ Code: ❌ Closed                                                         │
│  └─ Examples: GPT-4, Claude 3, Gemini Pro                                   │
│                                                                              │
│  OPEN-WEIGHT (Weights available, restricted use)                            │
│  ├─ Weights: ✅ Downloadable                                                │
│  ├─ Training data: ❌ Not released                                          │
│  ├─ Code: Partial                                                           │
│  └─ Examples: Llama 3, Gemma, Phi-3                                         │
│                                                                              │
│  OPEN-SOURCE (Fully open)                                                    │
│  ├─ Weights: ✅ Downloadable                                                │
│  ├─ Training data: ✅ Released or documented                                │
│  ├─ Code: ✅ Full training code                                             │
│  └─ Examples: OLMo, BLOOM, Pythia                                           │
│                                                                              │
│  SPECTRUM:                                                                   │
│  │                                                                           │
│  │  Closed ◄──────────────────────────────────────────────► Open            │
│  │    │                                                        │             │
│  │  GPT-4  Claude  Gemini  Llama3  Mixtral  Falcon  OLMo  BLOOM│             │
│  │                                                                           │
│  │  More control ◄──────────────────────────────────► More freedom          │
│  │  Better support                                    More customization    │
│  │  Easier to use                                     Can self-host         │
│  │                                                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Model Comparison (December 2024)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    TOP MODELS COMPARISON                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MODEL            TYPE     PARAMS   MMLU    MT-Bench  Context  License     │
│  ───────────────  ───────  ───────  ─────   ────────  ───────  ─────────  │
│  GPT-4o           Closed   ~1.8T?   90.0%   9.1       128K     Proprietary │
│  Claude 3 Opus    Closed   ~?       88.7%   9.0       200K     Proprietary │
│  Gemini 1.5 Pro   Closed   ~?       85.9%   8.8       1M       Proprietary │
│  Llama 3.1 405B   Open-W   405B     88.6%   8.9       128K     Llama 3.1   │
│  Llama 3.1 70B    Open-W   70B      86.0%   8.5       128K     Llama 3.1   │
│  Mixtral 8x22B    Open-W   141B     77.8%   8.1       64K      Apache 2.0  │
│  Qwen2 72B        Open-W   72B      84.2%   8.4       128K     Qwen License│
│  Claude 3.5 Son   Closed   ~?       88.7%   8.9       200K     Proprietary │
│                                                                             │
│  MMLU = General knowledge benchmark                                         │
│  MT-Bench = Multi-turn conversation quality (max 10)                       │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### Cost & Infrastructure Comparison

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    COST COMPARISON (1M tokens/day)                          │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  OPTION 1: Closed Model API (GPT-4o)                                       │
│  ├─ Input:  500K × $5/1M = $2.50/day                                       │
│  ├─ Output: 500K × $15/1M = $7.50/day                                      │
│  ├─ Total: ~$300/month                                                      │
│  ├─ Pros: No infra, instant scaling, always latest                         │
│  └─ Cons: Data leaves network, vendor lock-in, rate limits                 │
│                                                                             │
│  OPTION 2: Managed Open Model API (Together.ai, Fireworks)                 │
│  ├─ Llama 3.1 70B: ~$0.90/1M input, ~$0.90/1M output                       │
│  ├─ Total: ~$27/month for same usage                                        │
│  ├─ Pros: 10x cheaper, fast, no GPU management                             │
│  └─ Cons: Still API calls, some data concerns                              │
│                                                                             │
│  OPTION 3: Self-hosted (Llama 3.1 70B)                                     │
│  ├─ GPU: 2× A100 80GB (~$4/hour × 24 × 30 = $2,880/month)                  │
│  │   or: 8× A10G (~$3/hour × 24 × 30 = $2,160/month)                       │
│  ├─ Ops overhead: ~$500/month (engineer time, monitoring)                  │
│  ├─ Total: ~$2,500-3,500/month                                              │
│  ├─ Pros: Full control, no data leaves, fine-tuning possible               │
│  └─ Cons: High fixed cost, ops burden, GPU availability                    │
│                                                                             │
│  BREAK-EVEN ANALYSIS:                                                       │
│  ├─ API cheaper if: < 30M tokens/day (GPT-4o) or < 100M tokens/day (Llama) │
│  └─ Self-host cheaper if: > 100M tokens/day and need data privacy          │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### License Comparison

| License | Commercial Use | Modify | Redistribute | Fine-tune | Examples |
|---------|---------------|--------|--------------|-----------|----------|
| **Apache 2.0** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | Mistral, Falcon |
| **MIT** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | Some small models |
| **Llama 3.1** | ✅ Yes* | ✅ Yes | ✅ Yes | ✅ Yes | Llama 3.x |
| **Gemma** | ✅ Yes* | ✅ Yes | ✅ Yes | ✅ Yes | Gemma 2 |
| **Proprietary** | ✅ Via API | ❌ No | ❌ No | ❌ No | GPT-4, Claude |

*Restrictions: Llama 3.1 har MAU-gräns (700M), Gemma har vissa begränsningar.

## Steg-för-steg: Använd open models

### 1. Via managed API (enklast)

```python
# Together.ai - Llama 3.1 70B
from openai import OpenAI

together_client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

response = together_client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Vad är fördelarna med open-source AI?"}],
    max_tokens=500
)
print(response.choices[0].message.content)

# Fireworks.ai - Mixtral
fireworks_client = OpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

response = fireworks_client.chat.completions.create(
    model="accounts/fireworks/models/mixtral-8x22b-instruct",
    messages=[{"role": "user", "content": "Förklara transformer-arkitekturen"}],
    max_tokens=500
)
```

### 2. Lokal inference med Ollama

```bash
# Installera Ollama (macOS/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Ladda ner modell
ollama pull llama3.1:8b  # 8B version för laptops
ollama pull mistral       # Mistral 7B

# Kör interaktivt
ollama run llama3.1:8b "Vad är machine learning?"
```

```python
# Python SDK för Ollama
import ollama

response = ollama.chat(
    model='llama3.1:8b',
    messages=[
        {'role': 'user', 'content': 'Skriv en Python-funktion för fibonacci'}
    ]
)
print(response['message']['content'])

# Streaming
for chunk in ollama.chat(
    model='llama3.1:8b',
    messages=[{'role': 'user', 'content': 'Förklara recursion'}],
    stream=True
):
    print(chunk['message']['content'], end='', flush=True)
```

### 3. OpenAI-compatible API med vLLM

```bash
# Installera vLLM
pip install vllm

# Starta server
python -m vllm.entrypoints.openai.api_server \\
    --model meta-llama/Meta-Llama-3.1-8B-Instruct \\
    --host 0.0.0.0 \\
    --port 8000

# Nu fungerar OpenAI SDK mot lokal server!
```

```python
# Använd samma kod som för OpenAI
local_client = OpenAI(
    api_key="not-needed",  # Lokalt = ingen nyckel
    base_url="http://localhost:8000/v1"
)

response = local_client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": "Test"}]
)
```

### 4. Jämför modeller programmatiskt

```python
from dataclasses import dataclass
from typing import Callable
import time

@dataclass
class ModelConfig:
    name: str
    client: OpenAI
    model_id: str
    cost_per_1m_input: float
    cost_per_1m_output: float

def benchmark_models(
    configs: list[ModelConfig],
    prompts: list[str],
    num_runs: int = 3
) -> dict:
    \"\"\"Benchmarka flera modeller.\"\"\"
    results = {}

    for config in configs:
        model_results = {
            "latencies": [],
            "responses": [],
            "total_tokens": 0,
            "estimated_cost": 0
        }

        for prompt in prompts:
            for _ in range(num_runs):
                start = time.perf_counter()

                response = config.client.chat.completions.create(
                    model=config.model_id,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=200
                )

                latency = time.perf_counter() - start
                model_results["latencies"].append(latency)
                model_results["responses"].append(
                    response.choices[0].message.content
                )
                model_results["total_tokens"] += response.usage.total_tokens

        # Beräkna kostnad
        input_tokens = sum(len(p.split()) * 1.3 for p in prompts) * num_runs
        output_tokens = model_results["total_tokens"] - input_tokens
        model_results["estimated_cost"] = (
            (input_tokens * config.cost_per_1m_input / 1_000_000) +
            (output_tokens * config.cost_per_1m_output / 1_000_000)
        )

        results[config.name] = model_results

    return results

# Exempel på användning
configs = [
    ModelConfig("GPT-4o-mini", openai_client, "gpt-4o-mini", 0.15, 0.60),
    ModelConfig("Llama-3.1-70B", together_client, "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo", 0.88, 0.88),
]

results = benchmark_models(configs, ["Vad är Python?", "Förklara OOP"])
for model, data in results.items():
    avg_latency = sum(data["latencies"]) / len(data["latencies"])
    print(f"{model}: {avg_latency:.2f}s avg, ${data['estimated_cost']:.4f}")
```

## Vanliga problem

### Problem 1: "Llama ger sämre svar än GPT-4"

```python
# Lösning: Bättre system prompt för open models
# Open models behöver ofta mer explicit instruktion

LLAMA_SYSTEM_PROMPT = \"\"\"
Du är en hjälpsam, korrekt och koncis assistent.

REGLER:
1. Svara ENDAST på frågan som ställs
2. Om du inte vet, säg "Jag vet inte"
3. Undvik att repetera frågan
4. Ge konkreta exempel när möjligt
5. Håll svaret under 200 ord om inte annat anges
\"\"\"

# Använd explicit format
response = client.chat.completions.create(
    model="llama-3.1-70b",
    messages=[
        {"role": "system", "content": LLAMA_SYSTEM_PROMPT},
        {"role": "user", "content": "Vad är rekursion i programmering?"}
    ]
)
```

### Problem 2: "Ollama är långsamt på min maskin"

```bash
# Lösning 1: Använd mindre modell
ollama pull phi3:mini  # 3.8B parametrar
ollama pull llama3.2:1b  # 1B parametrar

# Lösning 2: Kvantisera (automatiskt i Ollama)
ollama pull llama3.1:8b-q4_0  # 4-bit quantization

# Lösning 3: Kontrollera GPU-användning
# macOS: Activity Monitor → GPU History
# Linux: nvidia-smi
```

### Problem 3: "Licensfrågor för produktion"

```python
# Kontrollera alltid licens innan deployment!
LICENSE_CHECK = {
    "llama-3.1": {
        "commercial": True,
        "restriction": "MAU < 700M",
        "link": "https://ai.meta.com/llama/license/"
    },
    "mixtral": {
        "commercial": True,
        "restriction": None,  # Apache 2.0
        "link": "https://mistral.ai/terms/"
    },
    "gpt-4": {
        "commercial": True,
        "restriction": "API Terms of Service",
        "link": "https://openai.com/policies/terms-of-use"
    }
}

def check_license(model: str) -> dict:
    return LICENSE_CHECK.get(model, {"warning": "Unknown license"})
```

## Praktisk övning

**Uppgift:** Bygg en model router

```python
from enum import Enum

class Priority(Enum):
    COST = "cost"
    QUALITY = "quality"
    LATENCY = "latency"
    PRIVACY = "privacy"

def select_model(
    task: str,
    priority: Priority,
    budget_per_request: float = 0.01,
    max_latency_ms: int = 2000,
    data_sensitive: bool = False
) -> str:
    \"\"\"
    TODO: Implementera smart model selection

    Regler:
    - COST: Välj billigaste som klarar uppgiften
    - QUALITY: Välj bästa oavsett kostnad
    - LATENCY: Välj snabbaste
    - PRIVACY: Välj self-hosted/open model

    Task types: "code", "chat", "analysis", "creative"
    \"\"\"
    # Din implementation här
    pass

# Test
print(select_model("code", Priority.QUALITY))  # → "gpt-4o"
print(select_model("chat", Priority.COST))      # → "llama-3.1-8b"
print(select_model("analysis", Priority.PRIVACY)) # → "local-llama"
```

## Sammanfattning

- ✅ **Open-weight** modeller ger kontroll men kräver infrastruktur
- ✅ **Closed models** är enklast att använda men dyra och beroende
- ✅ **Managed APIs** (Together, Fireworks) är en bra mellanväg
- ✅ **Licenser** varierar — kontrollera alltid före produktion
- ✅ **Self-hosting** lönar sig vid > 100M tokens/dag eller strikt privacy

## Nästa steg

Nu när du förstår modell-landskapet, fortsätt till:

- **Node 5:** What are AI Agents? — Från passiv LLM till aktiv agent
- **Node 6:** Agent Tools — Hur agenter interagerar med världen

---
*Pro tip: Starta alltid med managed API, migrera till self-host när det är ekonomiskt motiverat!*
"""
    }
]
