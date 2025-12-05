"""
AI Agents SkillsMap - Block 01: LLM Fundamentals
Nodes 1-2: Transformer Models, Tokenization & Context Windows
"""

BLOCK_01_NODES = [
    {
        "id": "ai-agents-01",
        "slug": "transformer-models-and-llms",
        "title": "Transformer Models och LLMs",
        "order_index": 1,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": [],
        "content": """# Transformer Models och LLMs

## Varför detta är viktigt

Large Language Models (LLMs) är grunden för alla moderna AI-agenter. Utan en djup förståelse
för hur transformers fungerar kommer du aldrig kunna bygga effektiva agenter, felsöka
hallucinationer, eller optimera kostnader. 2024 spenderades över $50 miljarder på AI-infrastruktur
— och majoriteten drivs av transformer-arkitekturen som introducerades 2017.

Företag som OpenAI, Anthropic, Google och Meta konkurrerar alla om att bygga bättre
LLMs, men arkitekturen under huven är remarkabelt liknande. Förstår du transformers,
förstår du 90% av modern AI.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Förklara hur transformer-arkitekturen fungerar (attention, layers, etc.)
- ✅ Skilja mellan encoder-only, decoder-only och encoder-decoder modeller
- ✅ Förstå vad "pre-training" och "fine-tuning" innebär
- ✅ Välja rätt modell för din use case (GPT-4, Claude, Llama, etc.)
- ✅ Förstå trade-offs mellan modellstorlek, kostnad och kvalitet

## Kärnkoncept

### Transformer-arkitekturen

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TRANSFORMER ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT: "The cat sat on the"                                                │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      TOKENIZATION                                    │   │
│  │  "The" → 464 | "cat" → 2278 | "sat" → 3421 | "on" → 319 | "the" → 262│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    EMBEDDING LAYER                                   │   │
│  │  Token IDs → Dense Vectors (768-12288 dimensions)                    │   │
│  │  + Positional Encoding (var i sekvensen är token?)                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │              TRANSFORMER BLOCKS (×N layers)                          │   │
│  │  ┌─────────────────────────────────────────────────────────┐        │   │
│  │  │  Multi-Head Self-Attention                               │        │   │
│  │  │  • Query (Q): Vad letar jag efter?                       │        │   │
│  │  │  • Key (K): Vad har jag att erbjuda?                     │        │   │
│  │  │  • Value (V): Vad är mitt innehåll?                      │        │   │
│  │  │  • Attention = softmax(QK^T / √d) × V                    │        │   │
│  │  └─────────────────────────────────────────────────────────┘        │   │
│  │  ┌─────────────────────────────────────────────────────────┐        │   │
│  │  │  Feed-Forward Network (FFN)                              │        │   │
│  │  │  • Linear → GELU/ReLU → Linear                           │        │   │
│  │  │  • Expansion ratio: 4× (768 → 3072 → 768)                │        │   │
│  │  └─────────────────────────────────────────────────────────┘        │   │
│  │  + Layer Normalization + Residual Connections                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     OUTPUT LAYER                                     │   │
│  │  Logits → Softmax → Next Token Probability Distribution              │   │
│  │  "mat" (0.42) | "floor" (0.18) | "couch" (0.12) | ...               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Modelltyper och användningsområden

| Typ | Arkitektur | Exempel | Användning |
|-----|------------|---------|------------|
| **Decoder-only** | GPT-stil | GPT-4, Claude, Llama | Text generation, chatbots, agents |
| **Encoder-only** | BERT-stil | BERT, RoBERTa | Classification, NER, embeddings |
| **Encoder-Decoder** | T5-stil | T5, BART | Translation, summarization |

### Populära LLMs för agenter (2024)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    LLM COMPARISON FOR AGENTS                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MODEL           PROVIDER    CONTEXT    COST/1M      BEST FOR              │
│  ─────────────   ─────────   ───────    ────────     ────────────────────  │
│  GPT-4 Turbo     OpenAI      128K       $10/$30      Complex reasoning     │
│  GPT-4o          OpenAI      128K       $5/$15       Multimodal agents     │
│  Claude 3 Opus   Anthropic   200K       $15/$75      Long context tasks    │
│  Claude 3.5 Son  Anthropic   200K       $3/$15       Coding agents         │
│  Llama 3.1 405B  Meta        128K       Self-host    Privacy-sensitive     │
│  Gemini 1.5 Pro  Google      1M+        $3.50/$10.50 Ultra-long context    │
│  Mixtral 8x22B   Mistral     64K        $2/$6        Cost-effective        │
│                                                                             │
│  Note: Costs are input/output per million tokens (December 2024)           │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Utforska en LLM

### 1. Installera OpenAI SDK

```bash
# Skapa virtuell miljö
python -m venv agent-env
source agent-env/bin/activate  # Windows: agent-env\\Scripts\\activate

# Installera dependencies
pip install openai tiktoken
```

### 2. Enkel LLM-interaktion

```python
from openai import OpenAI
import os

# Sätt API-nyckel (använd environment variable i produktion!)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Enkel completion
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Du är en hjälpsam assistent."},
        {"role": "user", "content": "Förklara transformer-arkitekturen på 3 meningar."}
    ],
    max_tokens=200,
    temperature=0.7
)

print(response.choices[0].message.content)
print(f"\\nTokens used: {response.usage.total_tokens}")
print(f"Cost: ${response.usage.total_tokens * 0.00015:.4f}")  # gpt-4o-mini pricing
```

### 3. Jämför modeller

```python
def compare_models(prompt: str, models: list[str]) -> dict:
    \"\"\"Jämför svar och kostnad mellan olika modeller.\"\"\"
    results = {}

    for model in models:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        results[model] = {
            "response": response.choices[0].message.content,
            "tokens": response.usage.total_tokens,
            "finish_reason": response.choices[0].finish_reason
        }

    return results

# Testa
models = ["gpt-4o-mini", "gpt-4o"]
results = compare_models("Vad är 2+2? Förklara steg för steg.", models)

for model, data in results.items():
    print(f"\\n=== {model} ===")
    print(f"Response: {data['response'][:200]}...")
    print(f"Tokens: {data['tokens']}")
```

### 4. Undersök attention patterns (avancerat)

```python
# För att visualisera attention behöver vi en open-source modell
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Ladda en liten modell lokalt
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    output_attentions=True
)

# Tokenisera input
text = "The cat sat on the mat"
inputs = tokenizer(text, return_tensors="pt")

# Kör forward pass
with torch.no_grad():
    outputs = model(**inputs)

# Attention weights: (layers, batch, heads, seq_len, seq_len)
attention = outputs.attentions
print(f"Number of layers: {len(attention)}")
print(f"Attention shape: {attention[0].shape}")
# Visar hur varje token "attendar" till andra tokens
```

## Vanliga problem

### Problem 1: "API-nyckel fungerar inte"

```bash
# Lösning 1: Kontrollera att nyckeln är korrekt
echo $OPENAI_API_KEY | head -c 10  # Bör visa "sk-..."

# Lösning 2: Sätt explicit i Python
import os
os.environ["OPENAI_API_KEY"] = "sk-..."  # Bara för test!

# Lösning 3: Använd .env fil
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()  # Läser från .env fil
```

### Problem 2: "Rate limit exceeded"

```python
import time
from openai import RateLimitError

def safe_completion(prompt: str, max_retries: int = 3) -> str:
    \"\"\"Hanterar rate limits med exponential backoff.\"\"\"
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError:
            wait_time = 2 ** attempt  # 1, 2, 4 seconds
            print(f"Rate limited. Waiting {wait_time}s...")
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
```

### Problem 3: "Modellen ger fel svar / hallucinerar"

```python
# Lösning: Använd lägre temperature och system prompts
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "Du svarar ENDAST baserat på fakta. Om du är osäker, säg 'Jag vet inte'."
        },
        {"role": "user", "content": "Vem vann VM i fotboll 2030?"}
    ],
    temperature=0.1  # Låg = mer deterministisk
)
```

## Praktisk övning

**Uppgift:** Bygg en modell-jämförare

1. Skapa en funktion som tar en prompt och lista av modeller
2. Mät latens, tokens och kostnad för varje modell
3. Returnera en "rekommendation" baserat på use case

```python
import time
from dataclasses import dataclass

@dataclass
class ModelResult:
    model: str
    response: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    cost_usd: float

# Priser per 1M tokens (input/output)
PRICING = {
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-4o": (5.0, 15.0),
    "gpt-4-turbo": (10.0, 30.0),
}

def benchmark_models(prompt: str, models: list[str]) -> list[ModelResult]:
    \"\"\"
    TODO: Implementera benchmarking

    1. Loopa genom varje modell
    2. Mät tiden med time.perf_counter()
    3. Beräkna kostnad baserat på PRICING dict
    4. Returnera sorterad lista (billigast först)
    \"\"\"
    results = []
    # Din kod här...
    return results

# Test
results = benchmark_models(
    "Skriv en haiku om programmering",
    ["gpt-4o-mini", "gpt-4o"]
)
for r in results:
    print(f"{r.model}: {r.latency_ms:.0f}ms, ${r.cost_usd:.4f}")
```

## Sammanfattning

- ✅ **Transformers** använder self-attention för att processa sekvenser parallellt
- ✅ **Decoder-only** (GPT-stil) är standard för generativa agenter
- ✅ **Modellval** påverkar kostnad, latens och kvalitet dramatiskt
- ✅ **Temperature** kontrollerar kreativitet vs determinism
- ✅ **Rate limits** hanteras med exponential backoff

## Nästa steg

Nu när du förstår transformer-grunden, fortsätt till:

- **Node 2:** Tokenization & Context Windows — Hur text blir tokens
- **Node 3:** Model Mechanics — Temperature, top-p och andra kontroller

---
*Pro tip: Spara alltid API-nycklar i environment variables, aldrig i kod!*
"""
    },
    {
        "id": "ai-agents-02",
        "slug": "tokenization-and-context-windows",
        "title": "Tokenization och Context Windows",
        "order_index": 2,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-01"],
        "content": """# Tokenization och Context Windows

## Varför detta är viktigt

Tokenization är den osynliga kostnaden som kan göra eller knäcka din AI-agent. Varje token
kostar pengar, och context window bestämmer hur mycket "minne" din agent har. En agent som
inte förstår tokenization kommer:

1. **Överskrida budgeten** — GPT-4 kostar $30/miljon output tokens
2. **Krascha mid-konversation** — Context overflow är en vanlig bug
3. **Ge dåliga svar** — Trunkerad kontext = hallucinationer

I 2024 har context windows exploderat från 4K till 1M+ tokens, men principerna är desamma.
Förstår du tokenization, kan du optimera kostnader med 50-80%.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Förklara hur text konverteras till tokens (BPE, WordPiece)
- ✅ Beräkna tokenkostnader innan API-anrop
- ✅ Optimera prompts för att minimera tokens
- ✅ Hantera context window limits i produktionsagenter
- ✅ Välja rätt modell baserat på context-behov

## Kärnkoncept

### Hur tokenization fungerar

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TOKENIZATION PROCESS                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT TEXT: "Hello, I'm learning about AI agents!"                         │
│                                                                              │
│  STEP 1: Character-level                                                    │
│  ['H','e','l','l','o',',',' ','I',"'",'m',' ','l','e','a','r','n',...]      │
│  → Too granular (50+ tokens för kort mening)                                │
│                                                                              │
│  STEP 2: Word-level                                                         │
│  ['Hello', ',', 'I', "'m", 'learning', 'about', 'AI', 'agents', '!']        │
│  → Problem: "unhappiness" = unknown word                                    │
│                                                                              │
│  STEP 3: BPE (Byte Pair Encoding) - Modern approach                         │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │  'Hello'  → [15496]                (common word = 1 token)        │     │
│  │  ','      → [11]                   (punctuation = 1 token)        │     │
│  │  ' I'     → [314]                  (space + I = 1 token)          │     │
│  │  "'m"     → [1101]                 (contraction = 1 token)        │     │
│  │  ' learning' → [4673]              (space + word = 1 token)       │     │
│  │  ' about' → [546]                  (common = 1 token)             │     │
│  │  ' AI'    → [9552]                 (space + AI = 1 token)         │     │
│  │  ' agents' → [15906]               (space + word = 1 token)       │     │
│  │  '!'      → [0]                    (punctuation = 1 token)        │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                              │
│  TOTAL: 9 tokens (efficient!)                                               │
│                                                                              │
│  COMPARISON - Same text in different tokenizers:                            │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │  GPT-4 (cl100k_base):    9 tokens                                │       │
│  │  GPT-3 (p50k_base):      11 tokens                               │       │
│  │  BERT (WordPiece):       12 tokens                               │       │
│  │  Character-level:        41 tokens                               │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Context Windows jämförelse

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    CONTEXT WINDOW COMPARISON (2024)                         │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MODEL              CONTEXT    ≈ PAGES    ≈ BOOKS    USE CASE              │
│  ─────────────────  ─────────  ─────────  ─────────  ─────────────────     │
│  GPT-3.5 Turbo      16K        ~25        ~0.1       Simple chatbots       │
│  GPT-4 Turbo        128K       ~200       ~0.5       Document analysis     │
│  Claude 3 Opus      200K       ~300       ~0.8       Long research         │
│  Gemini 1.5 Pro     1,000K     ~1,500     ~4         Entire codebases      │
│  Claude 3.5 Sonnet  200K       ~300       ~0.8       Coding + docs         │
│                                                                             │
│  RULE OF THUMB:                                                             │
│  • 1 token ≈ 4 characters (English)                                        │
│  • 1 token ≈ 0.75 words                                                    │
│  • 1 page ≈ 500-700 tokens                                                 │
│  • 1 book ≈ 80,000-100,000 tokens                                          │
│                                                                             │
│  COST IMPLICATIONS (GPT-4 Turbo at 128K):                                  │
│  ┌──────────────────────────────────────────────────────────────────┐     │
│  │  Full context (128K input):  $1.28 per request (!)               │     │
│  │  Typical chat (2K input):    $0.02 per request                   │     │
│  │  Optimized prompt (500):     $0.005 per request                  │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### Token-baserad prissättning

| Modell | Input/1M tokens | Output/1M tokens | 1K requests (avg 2K tokens) |
|--------|-----------------|------------------|----------------------------|
| GPT-4o-mini | $0.15 | $0.60 | $1.50 |
| GPT-4o | $5.00 | $15.00 | $40.00 |
| Claude 3.5 Sonnet | $3.00 | $15.00 | $36.00 |
| Claude 3 Opus | $15.00 | $75.00 | $180.00 |

## Steg-för-steg: Arbeta med tokens

### 1. Installera tiktoken

```bash
pip install tiktoken
```

### 2. Räkna tokens

```python
import tiktoken

# Välj encoding baserat på modell
def get_encoding(model: str) -> tiktoken.Encoding:
    \"\"\"Returnerar rätt tokenizer för given modell.\"\"\"
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")  # Default för GPT-4

# Räkna tokens i text
def count_tokens(text: str, model: str = "gpt-4o") -> int:
    encoding = get_encoding(model)
    return len(encoding.encode(text))

# Exempel
text = "Hello, I'm learning about AI agents!"
print(f"Text: {text}")
print(f"Tokens (GPT-4): {count_tokens(text, 'gpt-4o')}")
print(f"Tokens (GPT-3.5): {count_tokens(text, 'gpt-3.5-turbo')}")
```

### 3. Visualisera tokens

```python
def visualize_tokens(text: str, model: str = "gpt-4o") -> None:
    \"\"\"Visar hur text bryts ner till tokens.\"\"\"
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    print(f"Original: {text}")
    print(f"Token count: {len(tokens)}")
    print(f"Token IDs: {tokens}")
    print("\\nToken breakdown:")

    for token_id in tokens:
        token_str = encoding.decode([token_id])
        # Visa whitespace explicit
        display_str = repr(token_str) if token_str.strip() != token_str else token_str
        print(f"  {token_id:>6} → {display_str}")

# Test
visualize_tokens("Hello, I'm learning about AI!")
```

### 4. Beräkna kostnad före API-anrop

```python
from dataclasses import dataclass

@dataclass
class CostEstimate:
    input_tokens: int
    estimated_output_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float

# Prissättning (per token)
PRICING = {
    "gpt-4o": {"input": 5.0 / 1_000_000, "output": 15.0 / 1_000_000},
    "gpt-4o-mini": {"input": 0.15 / 1_000_000, "output": 0.60 / 1_000_000},
    "gpt-4-turbo": {"input": 10.0 / 1_000_000, "output": 30.0 / 1_000_000},
    "claude-3-opus": {"input": 15.0 / 1_000_000, "output": 75.0 / 1_000_000},
    "claude-3-5-sonnet": {"input": 3.0 / 1_000_000, "output": 15.0 / 1_000_000},
}

def estimate_cost(
    prompt: str,
    model: str = "gpt-4o",
    estimated_output_tokens: int = 500
) -> CostEstimate:
    \"\"\"Estimerar kostnad före API-anrop.\"\"\"
    input_tokens = count_tokens(prompt, model)

    pricing = PRICING.get(model, PRICING["gpt-4o"])
    input_cost = input_tokens * pricing["input"]
    output_cost = estimated_output_tokens * pricing["output"]

    return CostEstimate(
        input_tokens=input_tokens,
        estimated_output_tokens=estimated_output_tokens,
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=input_cost + output_cost
    )

# Användning
prompt = "Förklara quantum computing i detalj med exempel och kod."
for model in ["gpt-4o-mini", "gpt-4o", "claude-3-opus"]:
    estimate = estimate_cost(prompt, model, estimated_output_tokens=1000)
    print(f"{model}: ${estimate.total_cost:.4f} "
          f"({estimate.input_tokens} in, ~{estimate.estimated_output_tokens} out)")
```

### 5. Hantera context overflow

```python
def truncate_to_fit(
    text: str,
    max_tokens: int,
    model: str = "gpt-4o",
    keep_end: bool = False
) -> str:
    \"\"\"Trunkerar text för att passa inom token-limit.\"\"\"
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    if len(tokens) <= max_tokens:
        return text

    if keep_end:
        # Behåll slutet (bra för konversationer)
        truncated_tokens = tokens[-max_tokens:]
    else:
        # Behåll början (default)
        truncated_tokens = tokens[:max_tokens]

    return encoding.decode(truncated_tokens)

# Exempel: Förbereda prompt med context
def prepare_prompt_with_context(
    system_prompt: str,
    context: str,
    user_query: str,
    model: str = "gpt-4o",
    max_context_tokens: int = 100_000
) -> dict:
    \"\"\"Förbereder prompt med trunkerad context.\"\"\"
    # Räkna fasta tokens
    fixed_tokens = count_tokens(system_prompt + user_query, model)
    available_for_context = max_context_tokens - fixed_tokens - 1000  # Buffer

    # Trunkera context om nödvändigt
    truncated_context = truncate_to_fit(
        context,
        available_for_context,
        model,
        keep_end=True  # Behåll senaste info
    )

    return {
        "system": system_prompt,
        "context": truncated_context,
        "query": user_query,
        "total_tokens": count_tokens(
            system_prompt + truncated_context + user_query,
            model
        )
    }

# Test med lång context
long_context = "Viktig information... " * 5000  # Simulera lång dokument
result = prepare_prompt_with_context(
    "Du är en hjälpsam assistent.",
    long_context,
    "Sammanfatta dokumentet.",
    max_context_tokens=4000
)
print(f"Final prompt tokens: {result['total_tokens']}")
```

## Vanliga problem

### Problem 1: "Context length exceeded"

```python
from openai import BadRequestError

def safe_completion(messages: list, model: str = "gpt-4o") -> str:
    \"\"\"Hanterar context overflow automatiskt.\"\"\"
    # Beräkna total tokens
    total_content = " ".join([m["content"] for m in messages])
    tokens = count_tokens(total_content, model)

    # Context limits per modell
    limits = {
        "gpt-4o": 128_000,
        "gpt-4o-mini": 128_000,
        "gpt-4-turbo": 128_000,
        "gpt-3.5-turbo": 16_385,
    }
    max_tokens = limits.get(model, 128_000)

    if tokens > max_tokens * 0.9:  # 90% threshold
        print(f"Warning: {tokens} tokens approaching limit ({max_tokens})")
        # Trunkera meddelanden från början (behåll system + senaste)
        while tokens > max_tokens * 0.8 and len(messages) > 2:
            messages.pop(1)  # Ta bort äldsta user/assistant meddelandet
            total_content = " ".join([m["content"] for m in messages])
            tokens = count_tokens(total_content, model)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=4000
        )
        return response.choices[0].message.content
    except BadRequestError as e:
        if "context_length" in str(e):
            # Fallback: Använd modell med större context
            return safe_completion(messages, "gpt-4-turbo")
        raise
```

### Problem 2: "Tokens räknas fel för svenska/unicode"

```python
# Svenska och unicode kan ta fler tokens
texts = [
    "Hello world",           # English
    "Hej världen",           # Swedish
    "こんにちは世界",          # Japanese
    "🚀🎉✨",                 # Emojis
]

for text in texts:
    tokens = count_tokens(text, "gpt-4o")
    chars = len(text)
    ratio = tokens / chars
    print(f"{text:20} | chars: {chars:3} | tokens: {tokens:3} | ratio: {ratio:.2f}")

# Output visar att icke-ASCII tar fler tokens per tecken
```

### Problem 3: "Output avbryts mitt i mening"

```python
# Sätt max_tokens tillräckligt högt, men inte för högt (kostnad!)
def smart_completion(prompt: str, model: str = "gpt-4o") -> str:
    \"\"\"Dynamiskt max_tokens baserat på prompt.\"\"\"
    input_tokens = count_tokens(prompt, model)

    # Heuristik: Output är ofta 0.5-2x input för Q&A
    estimated_output = min(input_tokens * 1.5, 4000)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=int(estimated_output)
    )

    # Kontrollera om output trunkerades
    if response.choices[0].finish_reason == "length":
        print("Warning: Output was truncated. Consider increasing max_tokens.")

    return response.choices[0].message.content
```

## Praktisk övning

**Uppgift:** Bygg en Token Budget Manager

```python
class TokenBudgetManager:
    \"\"\"
    Hantera token-budget för en session.

    TODO: Implementera följande funktioner:
    1. track_usage() - Logga varje API-anrop
    2. get_remaining_budget() - Tokens/kostnad kvar
    3. should_use_cheaper_model() - Rekommendera billigare modell om nära budget
    4. get_session_summary() - Statistik över sessionen
    \"\"\"

    def __init__(self, max_tokens: int = 100_000, max_cost_usd: float = 1.0):
        self.max_tokens = max_tokens
        self.max_cost_usd = max_cost_usd
        self.usage_log = []

    def track_usage(self, model: str, input_tokens: int, output_tokens: int):
        # Din kod här...
        pass

    def get_remaining_budget(self) -> dict:
        # Din kod här...
        pass

    def should_use_cheaper_model(self) -> bool:
        # Din kod här...
        pass

    def get_session_summary(self) -> str:
        # Din kod här...
        pass

# Test
budget = TokenBudgetManager(max_tokens=50_000, max_cost_usd=0.50)
budget.track_usage("gpt-4o", 1000, 500)
budget.track_usage("gpt-4o", 2000, 1000)
print(budget.get_session_summary())
```

## Sammanfattning

- ✅ **Tokenization** (BPE) konverterar text till tokens — ~4 chars/token för engelska
- ✅ **Context windows** varierar 16K-1M+ tokens beroende på modell
- ✅ **Kostnad** beräknas separat för input och output tokens
- ✅ **tiktoken** library låter dig räkna tokens lokalt innan API-anrop
- ✅ **Trunkering** är nödvändigt för långa konversationer/dokument

## Nästa steg

Nu när du behärskar tokens, fortsätt till:

- **Node 3:** Generation Controls — Temperature, top-p, frequency penalty
- **Node 4:** Open vs Closed Models — Välja mellan GPT, Claude, Llama

---
*Pro tip: Räkna alltid tokens INNAN du gör API-anrop för att undvika överraskningar!*
"""
    }
]
