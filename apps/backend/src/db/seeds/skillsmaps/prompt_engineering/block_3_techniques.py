# =============================================================================
# BLOCK 3: PROMPTING TECHNIQUES (Noder 9-12)
# =============================================================================

NODE_09_SYSTEM = {
    "node_id": 9,
    "title": "System & Role Prompting",
    "slug": "system-role",
    "estimated_minutes": 45,
    "xp_reward": 125,
    "prerequisites": [8],
    "content": '''
# System & Role Prompting

Definiera AI:s personlighet och beteende.

## System Prompt

```yaml
Definition:
  En speciell instruktion som sätter kontext
  för hela konversationen.

Placering:
  - Först i message-listan
  - role: "system"
  - Påverkar alla följande meddelanden
```

```python
messages = [
    {
        "role": "system",
        "content": """Du är en senior DevOps-ingenjör med 15 års erfarenhet.

Du svarar alltid:
- Koncist och tekniskt korrekt
- Med praktiska kodexempel
- Med säkerhetsperspektiv i åtanke

Du undviker:
- Onödigt prat
- Föråldrade metoder
- Osäkra konfigurationer"""
    },
    {
        "role": "user",
        "content": "Hur sätter jag upp CI/CD?"
    }
]
```

## Role Prompting

```yaml
Definition:
  Be AI agera som en specifik person/roll
  för att få expertis inom ett område.

Fördelar:
  - Mer fokuserade svar
  - Rätt terminologi
  - Lämplig detaljnivå
```

```text
Exempel på roller:

🧑‍💻 "Du är en senior Python-utvecklare..."
👨‍🏫 "Du är en pedagogisk lärare som förklarar för nybörjare..."
🔒 "Du är en cybersäkerhetsexpert..."
📊 "Du är en dataanalytiker..."
✍️ "Du är en teknisk skribent..."
🧑‍⚖️ "Du är en juridisk rådgivare specialiserad på IT-rätt..."
```

## Effektiva System Prompts

```python
system_prompt = """
# Roll
Du är en AI-assistent specialiserad på Kubernetes.

# Kompetenser
- Containerorkestrering
- YAML-konfiguration
- Felsökning av kluster
- Säkerhetshärdning

# Stil
- Teknisk men pedagogisk
- Använd kodexempel
- Förklara varför, inte bara hur

# Begränsningar
- Föreslå aldrig osäkra konfigurationer
- Var ärlig om begränsningar
- Hänvisa till officiell dokumentation

# Format
- Använd Markdown
- Kod i kodblock med syntax highlighting
- Viktiga punkter som bullet lists
"""
```

## Contextual Prompting

```yaml
Definition:
  Ge specifik kontext om situationen
  för mer relevanta svar.

Element:
  - Användarens bakgrund
  - Projektets constraints
  - Teknisk miljö
  - Affärskrav
```

```python
context_prompt = """
# Kontext
- Projekt: E-handelsplattform
- Stack: Python FastAPI, PostgreSQL, Docker
- Team: 3 utvecklare, 1 DevOps
- Fas: MVP development
- Budget: Begränsad (startup)

# Nuvarande situation
Vi har problem med långsamma API-svar under hög last.
Genomsnittlig responstid är 2 sekunder.

# Mål
Minska till under 200ms för 95th percentile.

# Begränsningar
- Kan inte byta databas
- Max 1 veckas utvecklingstid
"""
```

## Kombinera System + Role + Context

```python
messages = [
    {
        "role": "system",
        "content": """# Roll
Du är en senior performance-ingenjör.

# Kontext
Klienten har en Python FastAPI-app med PostgreSQL.

# Uppgift
Analysera performance-problem och föreslå lösningar.

# Format
1. Diagnos
2. Quick wins (samma dag)
3. Medium-term (1 vecka)
4. Long-term (1 månad)

# Ton
Pragmatisk. Fokusera på ROI."""
    },
    {
        "role": "user",
        "content": "Våra API-svar tar 2 sekunder. Här är vår kod: [kod]"
    }
]
```

## System Prompt Best Practices

```yaml
DO:
  ✅ Var specifik om roll och expertis
  ✅ Definiera output-format
  ✅ Sätt gränser och begränsningar
  ✅ Inkludera exempel på önskad stil
  ✅ Håll det under ~500 tokens

DON'T:
  ❌ Skriv romaner (för lång → ignoreras)
  ❌ Motsägelsefulla instruktioner
  ❌ Vag eller tvetydig formulering
  ❌ Upprepa samma sak
```

## Persona Library

```python
PERSONAS = {
    "code_reviewer": """Du är en strikt kodgranskare.
    - Hitta buggar och säkerhetsproblem
    - Föreslå förbättringar
    - Referera till best practices
    - Betygsätt koden 1-10""",

    "teacher": """Du är en tålmodig programmeringslärare.
    - Förklara koncept steg för steg
    - Använd analogier
    - Ge övningar
    - Uppmuntra frågor""",

    "architect": """Du är en systemarkitekt.
    - Fokusera på skalbarhet
    - Diskutera trade-offs
    - Rita ASCII-diagram
    - Tänk långsiktigt"""
}

def chat_with_persona(persona, user_message):
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": PERSONAS[persona]},
            {"role": "user", "content": user_message}
        ]
    )
```

| Teknik | Användning |
|--------|------------|
| System Prompt | Övergripande beteende |
| Role Prompting | Expertis/perspektiv |
| Contextual | Situationsspecifik info |

**Nästa steg:** Node 10 - Chain of Thought
''',
}

NODE_10_COT = {
    "node_id": 10,
    "title": "Chain of Thought (CoT)",
    "slug": "chain-of-thought",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [7],
    "content": '''
# Chain of Thought (CoT)

Få AI att visa sitt resonemang.

## Vad är Chain of Thought?

```yaml
Definition:
  Prompt-teknik som ber modellen att
  "tänka högt" och visa mellansteg.

Ursprung:
  Google Research 2022
  "Chain-of-Thought Prompting Elicits Reasoning"

Resultat:
  Dramatisk förbättring på logik/matematik
```

## Zero-Shot CoT

```text
Den enklaste CoT: lägg till "Let's think step by step"

❌ Utan CoT:
"Om Anna har 3 äpplen och köper 5 till, sedan ger
bort hälften, hur många har hon kvar?"

→ "4" (kan vara fel)

✅ Med CoT:
"Om Anna har 3 äpplen och köper 5 till, sedan ger
bort hälften, hur många har hon kvar?

Let's think step by step."

→ "1. Anna börjar med 3 äpplen
   2. Hon köper 5 till: 3 + 5 = 8
   3. Hon ger bort hälften: 8 / 2 = 4
   4. Svar: Anna har 4 äpplen kvar"
```

## Few-Shot CoT

```text
Visa exempel med resonemang:

Q: Det finns 15 träd. Skogsarbetare hugger ned 10.
   Hur många träd finns kvar?

A: Låt mig tänka steg för steg.
   - Vi börjar med 15 träd
   - 10 träd huggs ned
   - 15 - 10 = 5 träd kvar
   Svaret är 5.

Q: Det finns 3 bilar. Varje bil har 4 hjul.
   Hur många hjul finns totalt?

A: Låt mig tänka steg för steg.
   - Vi har 3 bilar
   - Varje bil har 4 hjul
   - 3 × 4 = 12 hjul totalt
   Svaret är 12.

Q: En affär har 20 äpplen. 8 säljs på morgonen och
   5 på eftermiddagen. Hur många finns kvar?

A:
```

## CoT för kod

```python
prompt = """Analysera denna funktion och hitta buggen.
Tänk steg för steg genom koden.

```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
```

Analys steg för steg:
1. Vad gör varje rad?
2. Vilka edge cases finns?
3. Var är buggen?
4. Hur fixar vi den?
"""

# AI kommer gå genom varje steg och hitta
# division-by-zero för tom lista
```

## Self-Consistency

```yaml
Definition:
  Generera flera CoT-resonemang och välj
  det vanligaste svaret.

Process:
  1. Kör samma prompt N gånger (t.ex. 5)
  2. Samla alla svar
  3. Välj det svar som förekommer oftast

Varför:
  - Olika resonemang → samma korrekta svar
  - Minskar slumpmässiga fel
```

```python
def self_consistency(prompt, n=5):
    answers = []

    for _ in range(n):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": prompt + "\\n\\nThink step by step, then give final answer."
            }],
            temperature=0.7  # Viss variation
        )
        # Extrahera svar från slutet
        answer = extract_final_answer(response)
        answers.append(answer)

    # Returnera vanligaste svaret
    return most_common(answers)
```

## Step-Back Prompting

```yaml
Definition:
  Fråga först om den övergripande principen,
  sedan applicera på det specifika problemet.

Steg:
  1. "Vilken generell princip gäller här?"
  2. "Applicera principen på det specifika fallet"
```

```text
❌ Direkt:
"Beräkna kinetisk energi för en bil på 1000 kg
som kör 100 km/h"

✅ Step-back:
"Steg 1: Vad är formeln för kinetisk energi och
när används den?

Steg 2: Applicera formeln på en bil (m=1000 kg,
v=100 km/h). Glöm inte enhetskonvertering."

→ AI förklarar E = ½mv², konverterar till m/s,
   och beräknar korrekt
```

## CoT för debugging

```python
debug_prompt = """Jag har en bugg i min kod. Hjälp mig hitta den.

Kod:
```python
def find_duplicates(lst):
    seen = []
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.append(item)
    return duplicates
```

Error: AttributeError: 'list' object has no attribute 'add'

Debugga steg för steg:
1. Läs felmeddelandet
2. Identifiera vilken rad som orsakar felet
3. Analysera vad koden försöker göra
4. Förklara vad som är fel
5. Ge en fix
"""
```

## När använda CoT?

```yaml
Bra för:
  ✅ Matematik och logik
  ✅ Kodanalys och debugging
  ✅ Flerstegsberäkningar
  ✅ Komplexa beslut
  ✅ Problemlösning

Mindre nödvändigt för:
  ❌ Enkla faktafrågor
  ❌ Kreativt skrivande
  ❌ Översättning
  ❌ Sammanfattning
```

| Teknik | Beskrivning |
|--------|-------------|
| Zero-Shot CoT | "Think step by step" |
| Few-Shot CoT | Visa exempel med resonemang |
| Self-Consistency | Kör flera gånger, välj vanligaste |
| Step-Back | Fråga om princip först |

**Nästa steg:** Node 11 - Tree of Thoughts
''',
}

NODE_11_TOT = {
    "node_id": 11,
    "title": "Tree of Thoughts (ToT)",
    "slug": "tree-of-thoughts",
    "estimated_minutes": 45,
    "xp_reward": 135,
    "prerequisites": [10],
    "content": '''
# Tree of Thoughts (ToT)

Utforska flera lösningsvägar parallellt.

## Vad är Tree of Thoughts?

```yaml
Definition:
  En prompting-teknik som utforskar flera
  resonemang parallellt och utvärderar dem.

Skillnad från CoT:
  CoT: En linjär kedja av tankar
  ToT: Förgrenat träd av möjliga vägar

Ursprung:
  Princeton & Google DeepMind 2023
```

## ToT Struktur

```text
              [Problem]
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
    [Idé A]   [Idé B]   [Idé C]
        │         │         │
     [Eval]    [Eval]    [Eval]
        │         │         │
   Lovande?   Lovande?   Lovande?
        │         ✗         │
        ▼                   ▼
  [Fördjupa]          [Fördjupa]
        │                   │
        └───────┬───────────┘
                ▼
          [Bästa lösning]
```

## Basic ToT Prompt

```text
Problem: Planera en migreringsprocess från on-prem till cloud.

Generera 3 olika strategier:

STRATEGI 1: [Beskriv strategi]
- Fördelar:
- Nackdelar:
- Risker:
- Uppskattad tid:

STRATEGI 2: [Beskriv strategi]
- Fördelar:
- Nackdelar:
- Risker:
- Uppskattad tid:

STRATEGI 3: [Beskriv strategi]
- Fördelar:
- Nackdelar:
- Risker:
- Uppskattad tid:

---
UTVÄRDERING:
Vilken strategi är bäst givet:
- Budget: Begränsad
- Tidsram: 6 månader
- Riskaptit: Låg

REKOMMENDATION med motivering:
```

## ToT för problemlösning

```python
def tree_of_thoughts(problem, num_thoughts=3):
    # Steg 1: Generera flera idéer
    ideas_prompt = f"""Problem: {problem}

Generera {num_thoughts} olika lösningsansatser.
För varje ansats, beskriv:
1. Huvudidén
2. Första steget
3. Potentiella problem

Ansats 1:
"""

    ideas = generate(ideas_prompt)

    # Steg 2: Utvärdera varje idé
    eval_prompt = f"""Utvärdera dessa lösningsansatser:

{ideas}

För varje ansats, ge poäng 1-10 på:
- Genomförbarhet
- Effektivitet
- Risk

Vilken är mest lovande och varför?"""

    evaluation = generate(eval_prompt)

    # Steg 3: Utveckla bästa idén
    develop_prompt = f"""Baserat på utvärderingen:

{evaluation}

Utveckla den mest lovande lösningen i detalj:
- Steg-för-steg plan
- Potentiella hinder och lösningar
- Verifiering av framgång"""

    solution = generate(develop_prompt)

    return solution
```

## ToT för kreativa uppgifter

```text
Uppgift: Skriv en fängslande introduktion till en artikel om AI.

BRAINSTORM 3 ALTERNATIV:

Alt 1 (Personlig historia):
[Skriv intro som börjar med en personlig anekdot]
Styrka:
Svaghet:

Alt 2 (Chockerande statistik):
[Skriv intro som börjar med överraskande data]
Styrka:
Svaghet:

Alt 3 (Framtidsscenario):
[Skriv intro som målar upp en framtidsvision]
Styrka:
Svaghet:

---
VÄLJ & FÖRBÄTTRA:
Vilken fungerar bäst för målgruppen (tech professionals)?
Kombinera styrkor från de andra för att förbättra.

FINAL VERSION:
```

## ToT för tekniska beslut

```text
BESLUT: Vilken databas ska vi använda?

Kontext:
- E-handelsplattform
- 100K produkter
- 10M kunder
- Komplex sökning
- Real-time inventory

ALTERNATIV:

PostgreSQL:
+ Relationell, ACID, mogen
+ Bra query-planner
- Skalning kräver mer arbete
Poäng: ?/10

MongoDB:
+ Flexibel schema
+ Horisontell skalning
- Eventual consistency
Poäng: ?/10

PostgreSQL + Elasticsearch:
+ Bäst av båda världar
- Mer komplexitet
- Synkronisering
Poäng: ?/10

---
ANALYS:
Givet våra krav, rangordna alternativen med motivering.

REKOMMENDATION:
```

## Automatiserad ToT

```python
import asyncio

async def automated_tot(problem, depth=2, breadth=3):
    """Tree of Thoughts med automatisk sökning"""

    async def expand_thought(thought, level):
        if level >= depth:
            return thought

        # Generera child thoughts
        prompt = f"Given this thought: {thought}\\n\\n"
        prompt += f"Generate {breadth} ways to develop this further:"

        children = await generate_async(prompt)

        # Utvärdera varje child
        scores = []
        for child in children:
            score = await evaluate_thought(child)
            scores.append((score, child))

        # Välj bästa och expandera vidare
        best_child = max(scores, key=lambda x: x[0])[1]
        return await expand_thought(best_child, level + 1)

    # Starta med initial thoughts
    initial = await generate_initial_thoughts(problem, breadth)

    # Expandera parallellt
    results = await asyncio.gather(*[
        expand_thought(t, 0) for t in initial
    ])

    # Välj bästa slutresultat
    return await select_best(results)
```

| Aspekt | CoT | ToT |
|--------|-----|-----|
| Struktur | Linjär | Förgrenad |
| Utforskning | En väg | Flera vägar |
| Tokens | Färre | Fler |
| Komplexitet | Enkel | Avancerad |
| Bäst för | Stegvis logik | Komplexa beslut |

**Nästa steg:** Node 12 - ReAct Prompting
''',
}

NODE_12_REACT = {
    "node_id": 12,
    "title": "ReAct Prompting",
    "slug": "react-prompting",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [10],
    "content": '''
# ReAct Prompting

Kombinera resonemang med handlingar.

## Vad är ReAct?

```yaml
Definition:
  ReAct = Reasoning + Acting
  AI resonerar OCH utför handlingar för att
  lösa uppgifter.

Ursprung:
  Princeton & Google 2022
  "ReAct: Synergizing Reasoning and Acting in LLMs"

Användning:
  - Interagera med verktyg
  - Söka information
  - Utföra beräkningar
```

## ReAct Loop

```text
┌──────────────────────────────────────────────┐
│                 ReAct LOOP                   │
│                                              │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │ THOUGHT │ → │ ACTION  │ → │OBSERVE  │  │
│  │         │    │         │    │         │  │
│  │ Vad bör │    │ Gör det │    │ Se      │  │
│  │ jag     │    │         │    │ resultat│  │
│  │ göra?   │    │         │    │         │  │
│  └─────────┘    └─────────┘    └─────────┘  │
│       ▲                              │       │
│       └──────────────────────────────┘       │
│              (upprepa tills klart)           │
└──────────────────────────────────────────────┘
```

## ReAct Format

```text
Question: Vad är det nuvarande vädret i Stockholm
och behöver jag paraply?

Thought 1: Jag behöver kolla vädret i Stockholm först.
Action 1: search[väder Stockholm idag]
Observation 1: Det är molnigt, 8°C, 60% chans för regn.

Thought 2: Med 60% chans för regn bör jag rekommendera paraply.
Action 2: finish[Ja, ta med paraply. Det är 60% risk för regn.]
```

## Tillgängliga Actions

```yaml
Typiska verktyg:
  search[query]: Sök på internet
  calculate[expression]: Matematisk beräkning
  lookup[term]: Slå upp i databas/wiki
  code[python_code]: Kör Python-kod
  finish[answer]: Ge slutsvar
```

## ReAct Prompt Template

```python
REACT_PROMPT = """Svara på frågan med hjälp av följande verktyg:

Tillgängliga verktyg:
- search[query]: Sök på internet
- calculate[expr]: Beräkna matematiskt uttryck
- finish[answer]: Ge ditt slutsvar

Format:
Thought: [ditt resonemang]
Action: [verktyg][input]

Question: {question}

Thought 1:"""

def react_agent(question):
    prompt = REACT_PROMPT.format(question=question)

    while True:
        response = generate(prompt)

        # Parse action
        action_match = parse_action(response)

        if action_match.tool == "finish":
            return action_match.input

        # Execute action
        observation = execute_tool(
            action_match.tool,
            action_match.input
        )

        # Add observation and continue
        prompt += f"""
{response}
Observation: {observation}

Thought:"""
```

## ReAct för research

```text
Question: Hur mycket ökade NVIDIA:s aktie 2024 och varför?

Thought 1: Jag behöver hitta NVIDIAs aktiepris i början
och slutet av 2024.

Action 1: search[NVIDIA stock price January 1 2024]
Observation 1: NVIDIA (NVDA) öppnade 2024 på ~$495.

Thought 2: Nu behöver jag det nuvarande priset.
Action 2: search[NVIDIA stock price December 2024]
Observation 2: NVIDIA handlas på ~$140 (efter 10:1 split).

Thought 3: Jag måste justera för splitten. $140 × 10 = $1400
jämfört med $495. Det är en ökning på ca 183%.

Thought 4: Nu behöver jag förstå varför.
Action 4: search[why NVIDIA stock up 2024]
Observation 4: AI-boom, datacenter-efterfrågan, Blackwell-chips...

Thought 5: Nu kan jag sammanfatta.
Action 5: finish[NVIDIA ökade ~183% under 2024, drivet av
explosiv AI-efterfrågan och deras dominans inom GPU:er för
AI-träning, särskilt med lanseringen av Blackwell-arkitekturen.]
```

## ReAct med LangChain

```python
from langchain.agents import create_react_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

# Definiera verktyg
tools = [
    Tool(
        name="Search",
        func=search_function,
        description="Sök på internet"
    ),
    Tool(
        name="Calculator",
        func=calculator,
        description="Gör matematiska beräkningar"
    )
]

# Skapa agent
llm = ChatOpenAI(model="gpt-4o")
agent = create_react_agent(llm, tools, prompt)

# Kör
result = agent.invoke({
    "input": "Vad är genomsnittspriset på BTC den senaste månaden?"
})
```

## ReAct vs andra tekniker

```yaml
ReAct fördelar:
  ✅ Kan interagera med omvärlden
  ✅ Självkorrigerande (se observation, justera)
  ✅ Förklarbart (synliga steg)
  ✅ Flexibelt (lägg till verktyg)

Nackdelar:
  ❌ Fler API-anrop
  ❌ Kräver tool-implementation
  ❌ Kan loopa
  ❌ Långsammare
```

## Error handling

```python
def react_with_retry(question, max_retries=3):
    prompt = REACT_PROMPT.format(question=question)
    retries = 0

    while retries < max_retries:
        try:
            response = generate(prompt)
            action = parse_action(response)

            if action.tool == "finish":
                return action.input

            observation = execute_tool(action.tool, action.input)
            prompt += f"\\n{response}\\nObservation: {observation}\\nThought:"

        except ToolError as e:
            prompt += f"\\n{response}\\nObservation: ERROR - {e}\\nThought: I need to try a different approach.\\nThought:"
            retries += 1

    return "Could not complete the task"
```

| Komponent | Roll |
|-----------|------|
| Thought | Resonemang, planering |
| Action | Verktygsanrop |
| Observation | Verktygets output |
| Finish | Slutsvar |

**Nästa steg:** Node 13 - Prompt Chaining
''',
}

PROMPT_BLOCK_3 = [
    NODE_09_SYSTEM,
    NODE_10_COT,
    NODE_11_TOT,
    NODE_12_REACT,
]
