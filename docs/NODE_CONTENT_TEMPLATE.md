# NODE CONTENT TEMPLATE - Den Heliga Modern

═══════════════════════════════════════════════════════════════

## Översikt

Detta är **mallen** för hur alla noder i alla moduler ska struktureras.
Baserad på Docker Node 1 "Docker Fundamentals & Architecture".

---

## Strukturkrav

### 1. Titel (utan emoji)

```markdown
# Docker Fundamentals & Architecture
```

### 2. Visuella Separatorer

Använd denna linje mellan ALLA huvudsektioner:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3. Obligatoriska Sektioner (i denna ordning)

1. **Varför viktigt för DevOps?** - Tabell med scenarios
2. **Huvudinnehåll** - Teori med ASCII-diagram
3. **Kommandon/Syntax** - Tabeller + kodblock
4. **Praktiska exempel** - Kodblock med kommentarer
5. **Snabbreferens** - Tabell med viktiga termer
6. **Vanliga fel och lösningar** - Troubleshooting-tabell
7. **Key Takeaways** - Sammanfattning i tabell

---

## Formatregler

### Tabeller

Använd för:

- Kommandon och beskrivningar
- Jämförelser
- Parametrar och värden
- Fel och lösningar

```markdown
| Kommando | Beskrivning |
|----------|-------------|
| `docker ps` | Lista körande containers |
| `docker images` | Lista lokala images |
```

### ASCII-diagram

Använd för:

- Arkitektur
- Flöden
- Jämförelser
- Processer

```
┌─────────────────────────────────────────────────────────────┐
│                      RUBRIK                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Innehåll här                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Kodblock

```bash
# Kommentar som förklarar
kommando --flagga värde
# Output:
# förväntad output
```

### Markeringar (UTAN emojis)

- **Fetstil** för viktiga begrepp
- `backticks` för kommandon, filer, variabler
- *kursiv* för betoning

---

## Exempelmall

```python
{
    "title": "Ämne Här",
    "slug": "amne-har",
    "difficulty": "easy|medium|hard",
    "estimated_minutes": 45,
    "xp_reward": 75,
    "content": """# Ämne Här

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför detta är viktigt |
|----------|------------------------|
| **Scenario 1** | Förklaring |
| **Scenario 2** | Förklaring |

Du måste förstå:

- **Punkt 1** - varför
- **Punkt 2** - varför
- **Punkt 3** - varför

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundläggande Koncept

[ASCII-diagram här]

### Detaljerad förklaring

| Term | Beskrivning |
|------|-------------|
| **Term 1** | Vad det är |
| **Term 2** | Vad det är |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kommandon och Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `kommando1` | Vad det gör |
| `kommando2` | Vad det gör |

```bash
# Praktiskt exempel
kommando --flagga
# Output förklaring
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt Exempel

```bash
# Steg 1: Beskrivning
kommando1

# Steg 2: Beskrivning
kommando2

# Resultat:
# Vad som händer
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Term** | Kort förklaring |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `error message` | Varför det händer | Hur man fixar |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Koncept 1** | Sammanfattning |
| **Koncept 2** | Sammanfattning |

**Kom ihåg:**

- Punkt 1
- Punkt 2
- Punkt 3
""",
}

```

---

## Checklista för nya noder

- [ ] Titel utan emoji
- [ ] Separatorer (━━━) mellan alla sektioner
- [ ] "Varför viktigt för DevOps?" först
- [ ] Minst 1 tabell för kommandon
- [ ] Minst 1 ASCII-diagram
- [ ] Kodblock med kommentarer
- [ ] Snabbreferens-tabell
- [ ] Vanliga fel-tabell
- [ ] Key Takeaways-tabell
- [ ] Ingen emoji i texten

---

## Referens

**Originalnod:** Docker Fundamentals & Architecture
**Skapad:** 2024-11-28
**Version:** 1.0
