# =============================================================================
# AI AGENTS - BLOCK 01: LLM FUNDAMENTALS (Noder 1-2) - V3 FORMAT
# =============================================================================

NODE_01_TRANSFORMER_MODELS = {
    "node_id": 1,
    "title": "Transformer Models och LLMs",
    "slug": "transformer-models-and-llms",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [],
    "content": '''
# Transformer Models och LLMs

Forsta grunderna i Large Language Models och transformer-arkitekturen.

------------------------------------------------------------

## Vad ar Transformer Models?

Transformers ar den arkitektur som driver alla moderna LLMs. Introducerades 2017 och revolutionerade NLP genom self-attention mekanismen.

| Komponent | Funktion |
|-----------|----------|
| Self-Attention | Relaterar ord till varandra i sekvensen |
| Feed-Forward | Processar varje position individuellt |
| Layer Norm | Stabiliserar traningen |
| Positional Encoding | Ger positionsinformation |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| AI-agenter | LLMs ar hjarnan i moderna AI-agenter |
| Automation | Forsta begransningar for batter automation |
| Kostnad | Modellval paverkar kostnader dramatiskt |
| Felskning | Forsta hallucinationer och hur man undviker dem |

------------------------------------------------------------

## Snabbreferens

| Modelltyp | Arkitektur | Exempel | Anvandning |
|-----------|------------|---------|------------|
| Decoder-only | GPT-stil | GPT-4, Claude, Llama | Text generation, chatbots |
| Encoder-only | BERT-stil | BERT, RoBERTa | Classification, embeddings |
| Encoder-Decoder | T5-stil | T5, BART | Translation, summarization |

------------------------------------------------------------

## Transformer Arkitektur

```
+-----------------------------------------------------------------+
|                   TRANSFORMER ARCHITECTURE                       |
+-----------------------------------------------------------------+
|                                                                  |
|  INPUT: "The cat sat on the"                                    |
|           |                                                      |
|           v                                                      |
|  +---------------------------------------------------------+   |
|  |                   TOKENIZATION                           |   |
|  |  "The" -> 464 | "cat" -> 2278 | "sat" -> 3421           |   |
|  +---------------------------------------------------------+   |
|           |                                                      |
|           v                                                      |
|  +---------------------------------------------------------+   |
|  |                 EMBEDDING LAYER                          |   |
|  |  Token IDs -> Dense Vectors (768-12288 dimensions)       |   |
|  |  + Positional Encoding                                   |   |
|  +---------------------------------------------------------+   |
|           |                                                      |
|           v                                                      |
|  +---------------------------------------------------------+   |
|  |           TRANSFORMER BLOCKS (xN layers)                 |   |
|  |  +---------------------------------------------------+  |   |
|  |  |  Multi-Head Self-Attention                        |  |   |
|  |  |  Query (Q): Vad letar jag efter?                  |  |   |
|  |  |  Key (K): Vad har jag att erbjuda?                |  |   |
|  |  |  Value (V): Vad ar mitt innehall?                 |  |   |
|  |  +---------------------------------------------------+  |   |
|  |  +---------------------------------------------------+  |   |
|  |  |  Feed-Forward Network (FFN)                       |  |   |
|  |  |  Linear -> GELU/ReLU -> Linear                    |  |   |
|  |  +---------------------------------------------------+  |   |
|  +---------------------------------------------------------+   |
|           |                                                      |
|           v                                                      |
|  +---------------------------------------------------------+   |
|  |                   OUTPUT LAYER                           |   |
|  |  Logits -> Softmax -> Next Token Probability             |   |
|  +---------------------------------------------------------+   |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Populara LLMs for Agenter (2024)

| Modell | Provider | Context | Kostnad/1M | Bast for |
|--------|----------|---------|------------|----------|
| GPT-4 Turbo | OpenAI | 128K | $10/$30 | Komplex resonnering |
| GPT-4o | OpenAI | 128K | $5/$15 | Multimodala agenter |
| Claude 3 Opus | Anthropic | 200K | $15/$75 | Lang kontext |
| Claude 3.5 Sonnet | Anthropic | 200K | $3/$15 | Kodningsagenter |
| Llama 3.1 405B | Meta | 128K | Self-host | Integritetskanslig |

------------------------------------------------------------

## Enkel LLM-interaktion

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Du ar en hjalpsam assistent."},
        {"role": "user", "content": "Forklara transformer-arkitekturen."}
    ],
    max_tokens=200,
    temperature=0.7
)

print(response.choices[0].message.content)
print(f"Tokens anvanda: {response.usage.total_tokens}")
```

------------------------------------------------------------

## Jamfor Modeller

```python
def compare_models(prompt: str, models: list[str]) -> dict:
    """Jamfor svar och kostnad mellan olika modeller."""
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

models = ["gpt-4o-mini", "gpt-4o"]
results = compare_models("Vad ar 2+2?", models)

for model, data in results.items():
    print(f"=== {model} ===")
    print(f"Tokens: {data['tokens']}")
```

------------------------------------------------------------

## Hantera Rate Limits

```python
import time
from openai import RateLimitError

def safe_completion(prompt: str, max_retries: int = 3) -> str:
    """Hanterar rate limits med exponential backoff."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError:
            wait_time = 2 ** attempt
            print(f"Rate limited. Vantar {wait_time}s...")
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| API-nyckel fungerar inte | Felaktig nyckel | Kontrollera OPENAI_API_KEY |
| Rate limit exceeded | For manga anrop | Implementera exponential backoff |
| Hallucinationer | Modellen gar fel svar | Anvand lagre temperature |
| Context overflow | For lang prompt | Trunkera aldre meddelanden |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Transformers | Anvander self-attention for parallell processing |
| Decoder-only | Standard for generativa agenter (GPT-stil) |
| Modellval | Paverkar kostnad, latens och kvalitet |
| Temperature | Kontrollerar kreativitet vs determinism |

Kom ihag:
- Spara alltid API-nycklar i environment variables
- Valj modell baserat pa use case, inte bara kvalitet
- Rate limits ar verkliga, planera for dem
- Temperature=0 for deterministiska svar
'''
}

NODE_02_TOKENIZATION = {
    "node_id": 2,
    "title": "Tokenization och Context Windows",
    "slug": "tokenization-and-context-windows",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "prerequisites": [1],
    "content": '''
# Tokenization och Context Windows

Forsta hur text konverteras till tokens och hur context windows fungerar.

------------------------------------------------------------

## Vad ar Tokenization?

Tokenization ar processen som konverterar text till numeriska tokens som LLM kan processa. Varje token kostar pengar och tar plats i context window.

| Tokenizer | Metod | Anvands av |
|-----------|-------|------------|
| BPE | Byte Pair Encoding | GPT-modeller |
| WordPiece | Liknande BPE | BERT |
| SentencePiece | Unigram | T5, Llama |

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Kostnad | Varje token kostar pengar |
| Context | Bestammer hur mycket agenten minns |
| Optimering | Kortare prompts = lagre kostnad |
| Trunkering | Nodvandigt for langa konversationer |

------------------------------------------------------------

## Snabbreferens

| Tumregel | Varde |
|----------|-------|
| 1 token | ca 4 tecken (engelska) |
| 1 token | ca 0.75 ord |
| 1 sida | ca 500-700 tokens |
| 1 bok | ca 80,000-100,000 tokens |

------------------------------------------------------------

## Tokenization Process

```
+-----------------------------------------------------------------+
|                   TOKENIZATION PROCESS                           |
+-----------------------------------------------------------------+
|                                                                  |
|  INPUT TEXT: "Hello, I'm learning about AI agents!"             |
|                                                                  |
|  BPE (Byte Pair Encoding):                                      |
|  +-----------------------------------------------------------+ |
|  |  'Hello'    -> [15496]     (common word = 1 token)        | |
|  |  ','        -> [11]        (punctuation = 1 token)        | |
|  |  ' I'       -> [314]       (space + I = 1 token)          | |
|  |  "'m"       -> [1101]      (contraction = 1 token)        | |
|  |  ' learning'-> [4673]      (space + word = 1 token)       | |
|  |  ' about'   -> [546]       (common = 1 token)             | |
|  |  ' AI'      -> [9552]      (space + AI = 1 token)         | |
|  |  ' agents'  -> [15906]     (space + word = 1 token)       | |
|  |  '!'        -> [0]         (punctuation = 1 token)        | |
|  +-----------------------------------------------------------+ |
|                                                                  |
|  TOTAL: 9 tokens                                                |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Context Windows (2024)

| Modell | Context | Sidor | Anvandning |
|--------|---------|-------|------------|
| GPT-3.5 Turbo | 16K | ca 25 | Enkla chatbots |
| GPT-4 Turbo | 128K | ca 200 | Dokumentanalys |
| Claude 3 Opus | 200K | ca 300 | Lang research |
| Gemini 1.5 Pro | 1,000K | ca 1,500 | Hela kodbaser |

------------------------------------------------------------

## Rakna Tokens med tiktoken

```python
import tiktoken

def get_encoding(model: str):
    """Returnerar ratt tokenizer for given modell."""
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    encoding = get_encoding(model)
    return len(encoding.encode(text))

text = "Hello, I'm learning about AI agents!"
print(f"Text: {text}")
print(f"Tokens (GPT-4): {count_tokens(text, 'gpt-4o')}")
```

------------------------------------------------------------

## Kostnadskalkylering

```python
from dataclasses import dataclass

@dataclass
class CostEstimate:
    input_tokens: int
    output_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float

PRICING = {
    "gpt-4o": {"input": 5.0 / 1_000_000, "output": 15.0 / 1_000_000},
    "gpt-4o-mini": {"input": 0.15 / 1_000_000, "output": 0.60 / 1_000_000},
}

def estimate_cost(prompt: str, model: str, output_tokens: int = 500):
    input_tokens = count_tokens(prompt, model)
    pricing = PRICING.get(model, PRICING["gpt-4o"])

    input_cost = input_tokens * pricing["input"]
    output_cost = output_tokens * pricing["output"]

    return CostEstimate(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=input_cost + output_cost
    )
```

------------------------------------------------------------

## Hantera Context Overflow

```python
def truncate_to_fit(text: str, max_tokens: int, model: str = "gpt-4o"):
    """Trunkerar text for att passa inom token-limit."""
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    if len(tokens) <= max_tokens:
        return text

    truncated_tokens = tokens[:max_tokens]
    return encoding.decode(truncated_tokens)

def prepare_prompt_with_context(
    system_prompt: str,
    context: str,
    user_query: str,
    max_context_tokens: int = 100_000
):
    """Forbereder prompt med trunkerad context."""
    fixed_tokens = count_tokens(system_prompt + user_query)
    available = max_context_tokens - fixed_tokens - 1000

    truncated_context = truncate_to_fit(context, available)

    return {
        "system": system_prompt,
        "context": truncated_context,
        "query": user_query,
        "total_tokens": count_tokens(
            system_prompt + truncated_context + user_query
        )
    }
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Context length exceeded | For lang prompt | Trunkera aldre meddelanden |
| Tokens raknas fel | Unicode/svenska | Anvand tiktoken for exakt rakning |
| Output avbryts | max_tokens for lagt | Oka max_tokens eller dela upp |
| Hog kostnad | Ineffektiva prompts | Optimera prompts, valj billigare modell |

------------------------------------------------------------

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| BPE | Standard tokenization for GPT-modeller |
| Context window | Bestammer hur mycket LLM kan processa |
| Kostnad | Input och output tokens prissatts separat |
| tiktoken | Bibliotek for att rakna tokens lokalt |

Kom ihag:
- Rakna alltid tokens INNAN API-anrop
- Svenska tar fler tokens an engelska
- Trunkera smart - behall viktigaste informationen
- Valj modell baserat pa context-behov
'''
}

BLOCK_01_NODES = [NODE_01_TRANSFORMER_MODELS, NODE_02_TOKENIZATION]
