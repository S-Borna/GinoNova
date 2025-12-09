# =============================================================================
# AI AGENTS - BLOCK 02: MODEL MECHANICS (Noder 3-4) - V3 FORMAT
# =============================================================================

NODE_03_GENERATION_CONTROLS = {
    "node_id": 3,
    "title": "Generation Controls",
    "slug": "generation-controls",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "prerequisites": [2],
    "content": '''
# Generation Controls

Kontrollera hur LLMs genererar text med temperature, top-p och andra parametrar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Generation Controls?

Generation controls ar parametrar som paverkar hur LLM valjer nasta token. De bestammer balansen mellan kreativitet och konsistens.

| Parameter | Funktion |
|-----------|----------|
| Temperature | Kontrollerar randomness |
| Top-p | Nucleus sampling |
| Frequency penalty | Straffar upprepade tokens |
| Presence penalty | Uppmanar nya amnen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Konsistens | Code agents behover deterministiska svar |
| Kreativitet | Brainstorming behover variation |
| Debugging | Inkonsistenta svar ar svara att fixa |
| Kvalitet | Ratt settings = batter output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Parameter | Range | Default | Beskrivning |
|-----------|-------|---------|-------------|
| temperature | 0.0-2.0 | 1.0 | Lagre = mer fokuserat |
| top_p | 0.0-1.0 | 1.0 | Nucleus sampling threshold |
| frequency_penalty | -2.0-2.0 | 0.0 | Straffa upprepade tokens |
| presence_penalty | -2.0-2.0 | 0.0 | Uppmana nya amnen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hur Temperature Fungerar

```
┌─────────────────────────────────────────────────────────────────┐
│                   TEMPERATURE EFFECT                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT: "The capital of France is"                              │
│                                                                  │
│  Model outputs LOGITS (raw scores):                             │
│  "Paris": 8.5 │ "Lyon": 3.2 │ "Berlin": 1.1 │ "London": 0.8    │
│                                                                  │
│  After TEMPERATURE division:                                     │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Temp = 0.5 (mer fokuserat):                              │ │
│  │    "Paris" 99.9% │ "Lyon" 0.1% │ others ~0%               │ │
│  │                                                            │ │
│  │  Temp = 1.0 (default):                                    │ │
│  │    "Paris" 95% │ "Lyon" 4% │ others ~1%                   │ │
│  │                                                            │ │
│  │  Temp = 2.0 (mer random):                                 │ │
│  │    "Paris" 70% │ "Lyon" 15% │ others ~15%                 │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                  │
│  temp=0 -> Alltid hogsta sannolikhet (deterministisk)           │
│  temp=2 -> Mer uniform, allt kan handa                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rekommenderade Installningar

| Use Case | Temp | Top-p | Freq Penalty |
|----------|------|-------|--------------|
| Kod | 0.0-0.2 | 0.95 | 0 |
| Data extraction | 0.0 | 1.0 | 0 |
| Q&A / Fakta | 0.3 | 0.9 | 0 |
| Sammanfattning | 0.5 | 0.9 | 0.3 |
| Kreativ skrivning | 0.8-1.0 | 0.95 | 0.5 |
| Brainstorming | 1.0-1.2 | 1.0 | 0.7 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Experimentera med Temperature

```python
from openai import OpenAI

client = OpenAI()

def generate(
    prompt: str,
    temperature: float = 1.0,
    top_p: float = 1.0,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    max_tokens: int = 200,
    n: int = 1
) -> list[str]:
    """Generera text med specificerade controls."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        max_tokens=max_tokens,
        n=n
    )
    return [choice.message.content for choice in response.choices]

# Jamfor olika temperatures
for temp in [0.0, 0.5, 1.0, 1.5]:
    outputs = generate("Skriv ett foretagsnamn:", temperature=temp, n=3)
    unique = len(set(outputs))
    print(f"Temp {temp}: {unique}/3 unika svar")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deterministiska Svar

```python
# For maximal konsistens
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Vad ar 2+2?"}],
    temperature=0,
    seed=42  # Reproducerbarhet
)

DETERMINISTIC_CONFIG = {
    "temperature": 0,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "seed": 12345
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anti-Repetition

```python
# For att undvika upprepningar
ANTI_REPETITION_CONFIG = {
    "temperature": 0.7,
    "frequency_penalty": 0.8,
    "presence_penalty": 0.6,
}

# For listor och brainstorming
DIVERSITY_CONFIG = {
    "temperature": 1.0,
    "frequency_penalty": 1.2,
    "presence_penalty": 1.0,
    "top_p": 0.95
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stop Sequences

```python
# Kontrollera var output slutar
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": "Vad ar huvudstaden i Sverige?"
    }],
    temperature=0,
    stop=[".", "\\n", ","],
    max_tokens=50
)

print(f"Svar: '{response.choices[0].message.content}'")
print(f"Stop reason: {response.choices[0].finish_reason}")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Olika svar varje gang | Hog temperature | Sank till 0 |
| For repetitivt | Inga penalties | Oka frequency_penalty |
| For random/nonsens | For hog temp | Sank temperature och top_p |
| Inkonsistent JSON | Temperature > 0 | Anvand temperature=0 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Temperature | Kontrollerar randomness (0=deterministisk, 2=kaos) |
| Top-p | Filtrerar tokens baserat pa sannolikhet |
| Penalties | Minskar upprepning |
| Stop sequences | Kontrollerad output-langd |

Kom ihag:
- Borja med default-varden och justera vid behov
- Temperature=0 for kod och fakta
- Penalties for kreativa uppgifter
- Testa alltid flera kombinationer
'''
}

NODE_04_OPEN_VS_CLOSED = {
    "node_id": 4,
    "title": "Open vs Closed Models",
    "slug": "open-vs-closed-models",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "prerequisites": [3],
    "content": '''
# Open vs Closed Weight Models

Valj mellan proprietara och open-source modeller for dina AI-agenter.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Open vs Closed Models?

Open-weight modeller har vikter som kan laddas ner, medan closed modeller endast ar tillgangliga via API.

| Typ | Vikter | Kod | Exempel |
|-----|--------|-----|---------|
| Closed | Ej tillgangliga | Stangd | GPT-4, Claude |
| Open-weight | Nedladdningsbara | Delvis | Llama, Mistral |
| Open-source | Nedladdningsbara | Full | OLMo, BLOOM |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Kostnad | Self-hosting kan spara 90% |
| Integritet | Data lamnar aldrig ditt natverk |
| Latens | Lokalt = 50ms vs API = 500ms |
| Vendor lock-in | Undvik beroende av en leverantor |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Modeller 2024

| Modell | Typ | Params | Context | Licens |
|--------|-----|--------|---------|--------|
| GPT-4o | Closed | ? | 128K | Proprietary |
| Claude 3.5 Sonnet | Closed | ? | 200K | Proprietary |
| Llama 3.1 405B | Open-weight | 405B | 128K | Llama License |
| Llama 3.1 70B | Open-weight | 70B | 128K | Llama License |
| Mixtral 8x22B | Open-weight | 141B | 64K | Apache 2.0 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kostnadsjamforelse

```
┌─────────────────────────────────────────────────────────────────┐
│              KOSTNAD FOR 1M TOKENS/DAG                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  OPTION 1: Closed API (GPT-4o)                                  │
│  ├─ Input:  500K x $5/1M = $2.50/dag                           │
│  ├─ Output: 500K x $15/1M = $7.50/dag                          │
│  └─ Total: ~$300/manad                                          │
│                                                                  │
│  OPTION 2: Managed Open API (Together.ai)                       │
│  ├─ Llama 3.1 70B: ~$0.90/1M                                   │
│  └─ Total: ~$27/manad (10x billigare)                          │
│                                                                  │
│  OPTION 3: Self-hosted (Llama 3.1 70B)                         │
│  ├─ GPU: 2x A100 80GB = ~$2,880/manad                          │
│  ├─ Ops overhead: ~$500/manad                                   │
│  └─ Total: ~$3,000/manad (lonar sig vid > 100M tokens/dag)     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Licensjamforelse

| Licens | Kommersiellt | Modifiera | Exempel |
|--------|--------------|-----------|---------|
| Apache 2.0 | Ja | Ja | Mistral, Falcon |
| Llama 3.1 | Ja (MAU < 700M) | Ja | Llama 3.x |
| Proprietary | Via API | Nej | GPT-4, Claude |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anvand Managed API (Together.ai)

```python
from openai import OpenAI

together_client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

response = together_client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Forklara AI-agenter."}],
    max_tokens=500
)
print(response.choices[0].message.content)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lokal Inference med Ollama

```bash
# Installera Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Ladda ner modell
ollama pull llama3.1:8b

# Kor interaktivt
ollama run llama3.1:8b "Vad ar machine learning?"
```

```python
import ollama

response = ollama.chat(
    model='llama3.1:8b',
    messages=[
        {'role': 'user', 'content': 'Skriv en Python-funktion'}
    ]
)
print(response['message']['content'])
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## OpenAI-kompatibel Server med vLLM

```bash
# Installera vLLM
pip install vllm

# Starta server
python -m vllm.entrypoints.openai.api_server \\
    --model meta-llama/Meta-Llama-3.1-8B-Instruct \\
    --host 0.0.0.0 \\
    --port 8000
```

```python
# Anvand samma kod som for OpenAI
local_client = OpenAI(
    api_key="not-needed",
    base_url="http://localhost:8000/v1"
)

response = local_client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": "Test"}]
)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Batter Prompts for Open Models

```python
# Open models behover ofta mer explicit instruktion
LLAMA_SYSTEM_PROMPT = """
Du ar en hjalpsam, korrekt och koncis assistent.

REGLER:
1. Svara ENDAST pa fragan som stalls
2. Om du inte vet, sag "Jag vet inte"
3. Undvik att repetera fragan
4. Ge konkreta exempel nar mojligt
5. Hall svaret under 200 ord
"""

response = client.chat.completions.create(
    model="llama-3.1-70b",
    messages=[
        {"role": "system", "content": LLAMA_SYSTEM_PROMPT},
        {"role": "user", "content": "Vad ar rekursion?"}
    ]
)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Samre svar an GPT-4 | Default prompts | Mer explicita instruktioner |
| Ollama ar langsamt | Fel modellstorlek | Anvand mindre modell (8B) |
| Licensproblem | Fel licens for use case | Kontrollera licens innan deployment |
| GPU out of memory | For stor modell | Kvantisera eller mindre modell |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Open-weight | Ger kontroll men kraver infrastruktur |
| Closed | Enkelt men dyrt och beroende |
| Managed APIs | Bra mellanlage (Together, Fireworks) |
| Self-hosting | Lonar sig vid > 100M tokens/dag |

Kom ihag:
- Borja med managed API, migrera till self-host nar motiverat
- Kontrollera alltid licens innan produktion
- Open models kan krava mer prompt engineering
- Kostnad vs kvalitet vs integritet - valj tva
'''
}

BLOCK_02_NODES = [NODE_03_GENERATION_CONTROLS, NODE_04_OPEN_VS_CLOSED]
