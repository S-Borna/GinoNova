# =============================================================================
# BLOCK 2: LLM CONFIGURATION (Noder 5-8)
# =============================================================================

NODE_05_SAMPLING = {
    "node_id": 5,
    "title": "Sampling Parameters",
    "slug": "sampling-params",
    "estimated_minutes": 45,
    "xp_reward": 125,
    "prerequisites": [2],
    "content": '''
# Sampling Parameters

Kontrollera hur LLM genererar text.

## Hur LLM genererar text

```text
LLM predikterar nästa token genom att ge
sannolikheter till varje möjligt ord:

Prompt: "The cat sat on the"

Nästa token-sannolikheter:
  mat     -> 0.35 (35%)
  floor   -> 0.25 (25%)
  couch   -> 0.15 (15%)
  roof    -> 0.10 (10%)
  table   -> 0.08 (8%)
  ...     -> 0.07 (7%)

Sampling-parametrar styr hur vi väljer från dessa.
```

## Temperature

```yaml
Definition:
  Styr slumpmässighet i output.
  Högre = mer kreativt, lägre = mer förutsägbart.

Skala: 0.0 - 2.0 (typiskt)

temperature: 0.0
  - Alltid välj högst sannolikhet
  - Deterministiskt (samma input -> samma output)
  - Bra för: fakta, kod, matematik

temperature: 0.7 (default ofta)
  - Balans mellan kreativitet och koherens
  - Bra för: allmän konversation

temperature: 1.0+
  - Mer slumpmässigt
  - Kan bli inkonsekvent
  - Bra för: brainstorming, kreativt skrivande
```

```python
# OpenAI exempel
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Skriv en dikt"}],
    temperature=1.2  # Kreativt
)

# Kod-generering
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Skriv en Python-funktion"}],
    temperature=0.0  # Exakt, deterministiskt
)
```

## Top-P (Nucleus Sampling)

```yaml
Definition:
  Begränsar urvalet till tokens som tillsammans
  utgör P% av sannolikhetsmassan.

Exempel med top_p: 0.9 (90%):
  mat     -> 0.35  ✓ (kumulativ: 0.35)
  floor   -> 0.25  ✓ (kumulativ: 0.60)
  couch   -> 0.15  ✓ (kumulativ: 0.75)
  roof    -> 0.10  ✓ (kumulativ: 0.85)
  table   -> 0.08  ✓ (kumulativ: 0.93 > 0.90 -> stopp)
  övriga  -> ❌ (exkluderas)

Värden:
  top_p: 1.0 -> alla tokens (default)
  top_p: 0.9 -> säkra val
  top_p: 0.5 -> mycket begränsat
```

## Top-K

```yaml
Definition:
  Begränsar till de K mest sannolika tokens.

Exempel med top_k: 3:
  mat     -> 0.35  ✓
  floor   -> 0.25  ✓
  couch   -> 0.15  ✓
  övriga  -> ❌

Typiska värden:
  top_k: 50  -> standard för många modeller
  top_k: 10  -> mer fokuserad
  top_k: 1   -> greedy decoding (alltid bästa)
```

## Temperature vs Top-P vs Top-K

```yaml
Kombinera dem:
  - Temperature styr hur "platt" distributionen är
  - Top-P/Top-K begränsar urvalet

Rekommendationer:
  OpenAI: Använd temperature ELLER top_p, inte båda
  Anthropic: Stöder båda

Best practices:
  - Kreativt: temperature=1.0, top_p=0.95
  - Balanserat: temperature=0.7
  - Exakt: temperature=0.0
```

## Praktiskt exempel

```python
from openai import OpenAI
client = OpenAI()

def generate_with_params(prompt, temp=0.7, top_p=1.0):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp,
        top_p=top_p
    )
    return response.choices[0].message.content

# Test olika settings
prompt = "Föreslå ett projektnamn"

# Deterministiskt
print(generate_with_params(prompt, temp=0))

# Kreativt
print(generate_with_params(prompt, temp=1.2))

# Fokuserat men med variation
print(generate_with_params(prompt, temp=0.7, top_p=0.9))
```

| Parameter | Lågt värde | Högt värde |
|-----------|------------|------------|
| Temperature | Fokuserat, repetitivt | Kreativt, kaotiskt |
| Top-P | Säkra val | Mer variation |
| Top-K | Begränsat | Bredare urval |

**Nästa steg:** Node 6 - Output Control
''',
}

NODE_06_OUTPUT = {
    "node_id": 6,
    "title": "Output Control",
    "slug": "output-control",
    "estimated_minutes": 40,
    "xp_reward": 115,
    "prerequisites": [5],
    "content": '''
# Output Control

Styr längd och format på AI:s svar.

## Max Tokens

```yaml
Definition:
  Maximalt antal tokens i output.
  Stoppar generering när gränsen nås.

Användning:
  - Begränsa kostnad
  - Få koncisa svar
  - Passa in i UI-begränsningar

Obs:
  - Kan klippa av mitt i en mening
  - Räknas mot context window
```

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Skriv en lång berättelse"}],
    max_tokens=100  # Begränsa till ~75 ord
)

# Kolla om output blev avklippt
if response.choices[0].finish_reason == "length":
    print("Output truncated!")
```

## Stop Sequences

```yaml
Definition:
  Tecken/ord som stoppar generering.
  Användbart för att kontrollera format.

Exempel:
  stop=["\\n\\n"]  -> Stoppa vid dubbel newline
  stop=["END"]    -> Stoppa vid ordet END
  stop=["```"]    -> Stoppa efter kodblock
```

```python
# Extrahera endast första paragrafen
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Förklara Python"}],
    stop=["\\n\\n"]  # Stoppa efter första stycket
)

# Generera lista - stoppa när klar
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Lista 5 frukt, en per rad. Skriv END när klar."
    }],
    stop=["END"]
)
```

## Repetition Penalties

```yaml
Frequency Penalty:
  - Minskar sannolikhet för tokens baserat på
    hur ofta de redan förekommit
  - Värde: -2.0 till 2.0
  - Högre = mindre upprepning

Presence Penalty:
  - Minskar sannolikhet för ALLA tokens som
    redan använts (oavsett hur ofta)
  - Värde: -2.0 till 2.0
  - Uppmuntrar nya ämnen
```

```python
# Undvik upprepning
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Skriv en kreativ berättelse"
    }],
    frequency_penalty=0.5,  # Undvik samma ord
    presence_penalty=0.5    # Uppmuntra nya ämnen
)

# För kod - låg penalty (upprepning är OK)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Skriv en CRUD API"
    }],
    frequency_penalty=0.0,
    presence_penalty=0.0
)
```

## Structured Outputs (JSON Mode)

```yaml
JSON Mode:
  - Garanterar valid JSON output
  - Tillgängligt i GPT-4o och Claude
  - Perfekt för API-responses
```

```python
# OpenAI JSON mode
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "system",
        "content": "Returnera alltid valid JSON"
    }, {
        "role": "user",
        "content": "Lista 3 programmeringsspråk med år de skapades"
    }],
    response_format={"type": "json_object"}
)

import json
data = json.loads(response.choices[0].message.content)
print(data)
# {"languages": [{"name": "Python", "year": 1991}, ...]}
```

## Structured Outputs med Schema

```python
from pydantic import BaseModel

class Language(BaseModel):
    name: str
    year: int
    creator: str

class LanguageList(BaseModel):
    languages: list[Language]

# Med OpenAI Structured Outputs
response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Lista 3 programmeringsspråk"
    }],
    response_format=LanguageList
)

# Automatiskt parsad till Pydantic-objekt
languages = response.choices[0].message.parsed
for lang in languages.languages:
    print(f"{lang.name} ({lang.year}) by {lang.creator}")
```

## Best Practices

```yaml
För konversation:
  max_tokens: 500-1000
  frequency_penalty: 0.3
  presence_penalty: 0.3

För kod:
  max_tokens: 2000+
  temperature: 0
  frequency_penalty: 0

För kreativt skrivande:
  max_tokens: 1500
  temperature: 0.8-1.2
  frequency_penalty: 0.5

För strukturerad data:
  response_format: json_object
  temperature: 0
```

| Parameter | Effekt |
|-----------|--------|
| max_tokens | Begränsar output-längd |
| stop | Stoppar vid specifika tecken |
| frequency_penalty | Minskar ordupprepning |
| presence_penalty | Uppmuntrar nya ämnen |
| response_format | Tvingar specifikt format |

**Nästa steg:** Node 7 - Zero-Shot Prompting
''',
}

NODE_07_ZERO_SHOT = {
    "node_id": 7,
    "title": "Zero-Shot Prompting",
    "slug": "zero-shot",
    "estimated_minutes": 35,
    "xp_reward": 110,
    "prerequisites": [1],
    "content": '''
# Zero-Shot Prompting

Be AI lösa uppgifter utan exempel.

## Vad är Zero-Shot?

```yaml
Definition:
  Ge instruktioner utan att visa några exempel.
  Modellen förlitar sig på sin träningsdata.

Zero-Shot = "Noll exempel"
  -> Beskriv bara vad du vill ha
  -> Lita på modellens förkunskap
```

## Basic Zero-Shot

```text
❌ Dålig zero-shot:
"Klassificera"

✅ Bra zero-shot:
"Klassificera följande recension som POSITIV, NEGATIV
eller NEUTRAL:

Recension: Produkten var okej, inget speciellt.

Klassificering:"
```

## Tydliga instruktioner

```yaml
Nyckelelement:
  1. Vad ska göras (verb)
  2. Input-data
  3. Önskat format
  4. Begränsningar

Exempel:
  "Översätt följande text till svenska.
   Behåll formell ton.

   Text: Hello, how may I assist you today?

   Översättning:"
```

## Zero-Shot för olika uppgifter

```text
📝 Textsummarisering:
"Sammanfatta följande artikel i 3 punkter:

[Artikeltext]

Sammanfattning:"

---

🏷️ Klassificering:
"Kategorisera följande email som:
- URGENT
- NORMAL
- SPAM

Email: Vi har ett tidskritiskt ärende...

Kategori:"

---

🔍 Extraktion:
"Extrahera alla datum från texten nedan.
Format: YYYY-MM-DD

Text: Mötet är den 15 mars 2024 och deadline är 1 april.

Datum:"

---

💻 Kod:
"Skriv en Python-funktion som:
- Tar en sträng som input
- Returnerar strängen baklänges
- Inkludera type hints

Funktion:"
```

## Zero-Shot Chain of Thought

```text
Lägg till "Let's think step by step" för
att förbättra reasoning:

"En bonde har 17 äpplen. Han säljer 5 och ger
bort hälften av resten. Hur många har han kvar?

Let's think step by step:"

Output:
1. Börjar med 17 äpplen
2. Säljer 5: 17 - 5 = 12
3. Hälften av 12: 12 / 2 = 6
4. Svar: 6 äpplen
```

## När fungerar Zero-Shot bra?

```yaml
Bra för:
  ✅ Enkla, väldefinierade uppgifter
  ✅ Vanliga uppgifter (översättning, summaering)
  ✅ När modellen har bra förträning
  ✅ Snabba prototyper

Mindre bra för:
  ❌ Komplexa, domänspecifika uppgifter
  ❌ Ovanliga format
  ❌ Uppgifter som kräver specifik stil
  ❌ Höga krav på konsistens
```

## Tips för bättre Zero-Shot

```yaml
1. Var specifik:
   ❌ "Skriv om texten"
   ✅ "Skriv om texten för en 10-åring"

2. Definiera format:
   ❌ "Lista fördelar"
   ✅ "Lista 5 fördelar som bullet points"

3. Sätt begränsningar:
   ❌ "Förklara AI"
   ✅ "Förklara AI i max 50 ord"

4. Ge kontext:
   ❌ "Svara på frågan"
   ✅ "Du är en expert på DevOps. Svara på frågan..."
```

## Praktiskt exempel

```python
def zero_shot_classify(text, categories):
    prompt = f"""Klassificera följande text i en av dessa kategorier:
{', '.join(categories)}

Text: {text}

Svara med endast kategorinamnet, inget annat.

Kategori:"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=20
    )

    return response.choices[0].message.content.strip()

# Användning
result = zero_shot_classify(
    "Jag älskar den här produkten! Bästa köpet jag gjort!",
    ["POSITIV", "NEGATIV", "NEUTRAL"]
)
print(result)  # POSITIV
```

| Aspekt | Zero-Shot |
|--------|-----------|
| Exempel krävs | Nej |
| Tokens används | Få |
| Flexibilitet | Hög |
| Konsistens | Varierande |
| Komplexitet | Låg-Medium |

**Nästa steg:** Node 8 - Few-Shot Prompting
''',
}

NODE_08_FEW_SHOT = {
    "node_id": 8,
    "title": "Few-Shot Prompting",
    "slug": "few-shot",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [7],
    "content": '''
# Few-Shot Prompting

Visa exempel för att styra AI:s output.

## Vad är Few-Shot?

```yaml
Definition:
  Inkludera några exempel (shots) i prompten
  för att visa modellen exakt vad du vill ha.

One-Shot: 1 exempel
Few-Shot: 2-5+ exempel

Fördelar:
  - Mer kontroll över output-format
  - Bättre konsistens
  - Lär modellen ny "stil"
```

## Basic Few-Shot

```text
Klassificera sentiment:

Text: Fantastisk produkt, älskar den!
Sentiment: POSITIV

Text: Produkten gick sönder efter en dag.
Sentiment: NEGATIV

Text: Den fungerar som förväntat.
Sentiment: NEUTRAL

Text: Leveransen var sen men produkten är bra.
Sentiment:
```

## Strukturerade exempel

```text
Extrahera information i JSON-format:

Input: John Smith, 25 år, jobbar som utvecklare
Output: {"name": "John Smith", "age": 25, "job": "utvecklare"}

Input: Lisa Andersson är 30 och arbetar som designer
Output: {"name": "Lisa Andersson", "age": 30, "job": "designer"}

Input: Ahmed, 28 år gammal, konsult
Output:
```

## Kod-generering med Few-Shot

```python
prompt = """Konvertera naturligt språk till SQL.

Fråga: Visa alla användare
SQL: SELECT * FROM users;

Fråga: Räkna antal produkter
SQL: SELECT COUNT(*) FROM products;

Fråga: Hitta användare äldre än 30
SQL: SELECT * FROM users WHERE age > 30;

Fråga: Lista de 10 senaste beställningarna
SQL:"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)
# Output: SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;
```

## Välja bra exempel

```yaml
Regler:
  1. Representativa:
     - Täck olika edge cases
     - Visa svåra fall

  2. Korrekta:
     - Dubbelkolla alla exempel
     - Felaktiga exempel -> felaktig output

  3. Konsekventa:
     - Samma format i alla exempel
     - Samma stil och ton

  4. Relevanta:
     - Liknar uppgiften som ska lösas
     - Samma domän/kontext
```

## Antal exempel

```yaml
Tumregel:
  - 2-3 exempel: De flesta uppgifter
  - 5+ exempel: Komplexa mönster
  - 10+ exempel: Ovanliga format

Trade-off:
  Fler exempel = Bättre konsistens
  Fler exempel = Fler tokens (kostnad)
  Fler exempel = Mindre plats för input
```

## Few-Shot med roller

```python
messages = [
    {
        "role": "system",
        "content": "Du klassificerar emails."
    },
    # Exempel 1
    {
        "role": "user",
        "content": "Email: Grattis! Du har vunnit 1000000 kr!"
    },
    {
        "role": "assistant",
        "content": "SPAM"
    },
    # Exempel 2
    {
        "role": "user",
        "content": "Email: Mötet flyttat till kl 14"
    },
    {
        "role": "assistant",
        "content": "NORMAL"
    },
    # Exempel 3
    {
        "role": "user",
        "content": "Email: AKUT: Server nere, behöver hjälp NU"
    },
    {
        "role": "assistant",
        "content": "URGENT"
    },
    # Faktisk fråga
    {
        "role": "user",
        "content": "Email: Påminnelse om deadline imorgon"
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)
```

## Dynamic Few-Shot

```python
def find_similar_examples(query, examples, top_k=3):
    """Hitta mest relevanta exempel med embeddings"""
    # Skapa embedding för query
    query_embedding = get_embedding(query)

    # Räkna similarity för varje exempel
    scored = []
    for ex in examples:
        similarity = cosine_similarity(
            query_embedding,
            ex["embedding"]
        )
        scored.append((similarity, ex))

    # Returnera top-k
    scored.sort(reverse=True)
    return [ex for _, ex in scored[:top_k]]

# Bygg prompt med relevanta exempel
relevant = find_similar_examples(user_query, all_examples)
prompt = build_few_shot_prompt(relevant, user_query)
```

## Few-Shot vs Zero-Shot

| Aspekt | Zero-Shot | Few-Shot |
|--------|-----------|----------|
| Tokens | Färre | Fler |
| Kostnad | Lägre | Högre |
| Konsistens | Lägre | Högre |
| Setup | Enklare | Kräver exempel |
| Flexibilitet | Högre | Format låst |

**Nästa steg:** Node 9 - System Prompting
''',
}

PROMPT_BLOCK_2 = [
    NODE_05_SAMPLING,
    NODE_06_OUTPUT,
    NODE_07_ZERO_SHOT,
    NODE_08_FEW_SHOT,
]
