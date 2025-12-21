# 📘 MASTER NODE TEMPLATE v1.0
## DevOpsHub - Standardstruktur för alla utbildningsnoder

---

## 🎯 Mallens syfte

Denna mall definierar den exakta strukturen för ALLA noder i DevOpsHub. 
Varje nod ska följa detta flöde för att säkerställa:
- Konsekvent användarupplevelse
- Pedagogisk progression
- Praktisk tillämpning
- Mätbart lärande

---

## 📐 NODSTRUKTUR

```
┌─────────────────────────────────────────────────────────────┐
│  1. HOOK (2-3 meningar)                                     │
│     → Fånga intresse, varför detta spelar roll              │
├─────────────────────────────────────────────────────────────┤
│  2. LÄRANDEMÅL (3-5 punkter)                                │
│     → Konkreta saker användaren kan efteråt                 │
├─────────────────────────────────────────────────────────────┤
│  3. FÖRKUNSKAPER (om relevant)                              │
│     → Vad behöver man kunna innan?                          │
├─────────────────────────────────────────────────────────────┤
│  4. KONCEPT & TEORI                                         │
│     → Förklaring med analogier och "tänk på det som..."     │
├─────────────────────────────────────────────────────────────┤
│  5. PRAKTISKA EXEMPEL                                       │
│     → Kommandon med förklarande kommentarer                 │
├─────────────────────────────────────────────────────────────┤
│  6. HANDS-ON ÖVNINGAR (3 st)                                │
│     → Grundläggande → Tillämpad → Utmanande                 │
├─────────────────────────────────────────────────────────────┤
│  7. VANLIGA MISSTAG & FELSÖKNING                            │
│     → "Om du ser X, gör Y"                                  │
├─────────────────────────────────────────────────────────────┤
│  8. BEST PRACTICES & TIPS                                   │
│     → Alias, shortcuts, produktivitetstips                  │
├─────────────────────────────────────────────────────────────┤
│  9. DEVOPS I PRAKTIKEN                                      │
│     → Verkliga scenarion där detta används                  │
├─────────────────────────────────────────────────────────────┤
│  10. SAMMANFATTNING                                         │
│      → Bullet points med det viktigaste                     │
├─────────────────────────────────────────────────────────────┤
│  11. NÄSTA STEG                                             │
│      → Vad bygger på detta? Vart går resan?                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 DETALJERAD MALLBESKRIVNING

### 1. 🎣 HOOK (Introduktion)
**Längd:** 2-3 meningar  
**Ton:** Engagerande, relaterbar  
**Innehåll:** 
- Varför detta ämne är viktigt
- Ett scenario där detta spelar roll
- Väck nyfikenhet

**Exempel:**
> Föreställ dig att du blir uppringd klockan 3 på natten - produktionsservern har 
> kraschat och du har 15 minuter på dig att hitta felet. Om du inte vet var 
> loggfilerna ligger, var konfigurationen finns, eller hur filsystemet är 
> organiserat, kommer de minuterna kännas som en evighet.

---

### 2. 🎯 LÄRANDEMÅL
**Format:** Bullet points (3-5 st)  
**Formulering:** "Efter denna nod kommer du kunna..."  
**Krav:** Konkreta, mätbara, handlingsorienterade

**Exempel:**
```markdown
## 🎯 Efter denna nod kommer du kunna:
- [ ] Navigera till rätt katalog på första försöket när du felsöker
- [ ] Hitta konfigurationsfiler för vilken tjänst som helst
- [ ] Förstå var loggar sparas och hur du läser dem i realtid
- [ ] Organisera egna scripts enligt Linux-konventioner
```

---

### 3. 📚 FÖRKUNSKAPER (om relevant)
**Format:** Kort lista  
**Syfte:** Säkerställa rätt nivå, länka till tidigare noder

**Exempel:**
```markdown
## 📚 Förkunskaper
- Grundläggande terminalnavigering (cd, ls, pwd)
- Förståelse för vad en fil och katalog är
- [Rekommenderas: Nod X - Grundläggande terminalkommandon]
```

---

### 4. 📖 KONCEPT & TEORI
**Stil:** Berättande, använd analogier  
**Struktur:** 
- Introducera koncept med "Tänk på det som..."
- Bryt ner i logiska delar
- Använd visuella representationer där möjligt

**Krav på kodblock:**
```bash
kommando argument
# ↑ Förklaring av vad kommandot gör
# ↑ Varför vi använder just detta argument
# ↑ Vad vi förväntar oss se som resultat
```

---

### 5. 💻 PRAKTISKA EXEMPEL
**Antal:** 5-10 exempel beroende på komplexitet  
**Format:** Kodblock med utförliga kommentarer  
**Progression:** Enkla → Komplexa

**Mall för kodblock:**
```bash
# === EXEMPEL: [Beskrivande rubrik] ===

# Vad vi vill uppnå:
# [Förklara målet med exemplet]

kommando --flagga argument
# Förväntat resultat:
# [Visa vad användaren bör se]

# Varför detta fungerar:
# [Kort förklaring av mekanismen]
```

---

### 6. 🏋️ HANDS-ON ÖVNINGAR
**Antal:** Exakt 3 övningar  
**Progression:**
1. **Grundläggande** - Direkt tillämpning av det man lärt sig
2. **Tillämpad** - Kombinera flera koncept
3. **Utmanande** - Problemlösning, kräver eftertanke

**Mall för övning:**
```markdown
### Övning [X]: [Rubrik]
**Mål:** [Vad ska uppnås]
**Scenario:** [Kontext/bakgrund]

**Din uppgift:**
1. [Steg 1]
2. [Steg 2]
3. [Steg 3]

<details>
<summary>💡 Ledtråd</summary>
[Ledtråd utan att ge bort svaret]
</details>

<details>
<summary>✅ Lösning</summary>
```bash
[Komplett lösning med kommentarer]
```
</details>

**Verifikation:** [Hur vet användaren att de lyckats?]
```

---

### 7. ⚠️ VANLIGA MISSTAG & FELSÖKNING
**Format:** Problem → Orsak → Lösning  
**Antal:** 3-5 vanliga misstag

**Mall:**
```markdown
### ❌ Misstag: [Beskrivning]
**Symptom:** [Vad användaren ser]
**Orsak:** [Varför det händer]
**Lösning:**
```bash
[Kommando för att fixa]
```
```

---

### 8. 💡 BEST PRACTICES & TIPS
**Innehåll:**
- Användbara alias
- Keyboard shortcuts
- Produktivitetstips
- "Pro tips"

**Mall för alias:**
```bash
# Lägg till i din ~/.bashrc eller ~/.zshrc:
alias kortnamn='långt kommando med flaggor'

# Exempel på användning:
kortnamn argument
```

---

### 9. 🔧 DEVOPS I PRAKTIKEN
**Syfte:** Koppla till verkliga arbetsscenarier  
**Innehåll:**
- Var i CI/CD-pipeline används detta?
- Hur ser detta ut i produktion?
- Verkliga exempel från industrin

**Mall:**
```markdown
### Scenario: [Verkligt användningsfall]
**Kontext:** [Beskrivning av situation]
**Hur [ämnet] används:**
[Konkret beskrivning med eventuella kodexempel]
```

---

### 10. 📝 SAMMANFATTNING
**Format:** Bullet points  
**Antal:** 5-7 punkter  
**Krav:** Ska kunna användas som "cheat sheet"

```markdown
## 📝 Sammanfattning - Det viktigaste att ta med sig

- **[Koncept 1]:** [En mening]
- **[Koncept 2]:** [En mening]
- **[Kommando]:** [Vad det gör]
```

---

### 11. 🚀 NÄSTA STEG
**Syfte:** Skapa progression, motivation  
**Innehåll:**
- Vad bygger på denna kunskap?
- Vilken nod kommer härnäst?
- Vad kan användaren utforska på egen hand?

```markdown
## 🚀 Nästa steg

Nu när du förstår [ämnet] är du redo att:
- **Nästa nod:** [Namn] - [Kort beskrivning]
- **Fördjupning:** [Eventuell extern resurs]
- **Öva mer:** [Förslag på egen övning]
```

---

## 🎨 TONALITET & STILGUIDE

### Språk
- **Tilltal:** "Du" (aldrig "man" eller "vi")
- **Ton:** Vänlig mentor, inte akademisk föreläsare
- **Analogier:** Använd vardagliga jämförelser
- **Humor:** Sparsamt, aldrig på bekostnad av tydlighet

### Kodkommentarer
- **Svenska** för förklaringar
- **Engelska** för tekniska termer som är standard
- **Alltid** förklara vad kommandot gör OCH varför

### Formatering
- Emojis för sektionsrubriker (sparsamt)
- Kodblock med språkspecifikation (```bash, ```yaml, etc.)
- Tabeller för jämförelser
- Collapsible sections för lösningar

---

## 📊 METADATA FÖR VARJE NOD

```yaml
node:
  id: [nummer]
  title: "[Rubrik]"
  module: "[Modulnamn]"
  difficulty: "Lätt|Medium|Svår"
  estimated_time: [minuter]
  xp: [poäng]
  prerequisites: 
    - "[Nod X]"
  tags:
    - "[tag1]"
    - "[tag2]"
  objectives:
    - "[Mål 1]"
    - "[Mål 2]"
```

---

## ✅ CHECKLISTA FÖR GODKÄND NOD

Innan en nod anses komplett, verifiera:

- [ ] Hook fångar intresse och förklarar relevans
- [ ] Lärandemål är konkreta och mätbara
- [ ] Alla kodexempel är testade och fungerar
- [ ] Varje kodblock har förklarande kommentarer
- [ ] 3 övningar med ökande svårighetsgrad finns
- [ ] Lösningar är dolda men tillgängliga
- [ ] Vanliga misstag täcks
- [ ] Minst 2 användbara alias/tips finns
- [ ] DevOps-koppling är tydlig
- [ ] Sammanfattning fungerar som cheat sheet
- [ ] Nästa steg pekar framåt

---

*Template version 1.0 - DevOpsHub Content Standard*
