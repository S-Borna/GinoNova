# 🤖 MASTER PROMPT FOR OPUS
## Återanvändbar prompt för att generera nodinnehåll

---

## 📋 INSTRUKTIONER FÖR ANVÄNDNING

1. Kopiera HELA denna prompt till Opus
2. Ersätt variablerna inom `[BRACKETS]` med specifik information
3. Kör prompten
4. Verifiera output mot checklistan längst ner

---

## 🎯 MASTER PROMPT

```
Du är en erfaren DevOps-ingenjör och teknisk pedagog som skapar utbildningsinnehåll för DevOpsHub.

Din uppgift är att skapa komplett innehåll för följande nod:

═══════════════════════════════════════════════════════════════
NODINFORMATION
═══════════════════════════════════════════════════════════════

Svårighetsgrad: [Lätt/Medium/Svår]
Uppskattad tid: [XX] minuter
XP: [XX] poäng

Tidigare nod: [FÖREGÅENDE_NOD_TITEL eller "Ingen (första noden)"]
Nästa nod: [NÄSTA_NOD_TITEL eller "Ingen (sista noden)"]

═══════════════════════════════════════════════════════════════
KRAV PÅ INNEHÅLL
═══════════════════════════════════════════════════════════════

Skapa innehåll med EXAKT denna struktur och ordning:

---

## 1. 🎣 HOOK (Introduktion)
- 2-3 meningar som fångar intresse
- Förklara VARFÖR detta är viktigt för en DevOps-ingenjör
- Använd ett relaterbart scenario (t.ex. "Föreställ dig att...")
- Skapa motivation att lära sig mer

## 2. 🎯 LÄRANDEMÅL
- Rubrik: "Efter denna nod kommer du kunna:"
- 4-5 konkreta, mätbara mål
- Formulera som checkboxar: "- [ ] Göra X"
- Handlingsorienterade verb (navigera, konfigurera, felsöka, etc.)

## 3. 📚 FÖRKUNSKAPER (om relevant)
- Lista vad användaren bör kunna sedan tidigare
- Referera till tidigare noder om tillämpligt
- Håll kort, max 3-4 punkter

## 4. 📖 KONCEPT & TEORI
- Berättande ton, som en mentor som förklarar
- Använd analogier: "Tänk på det som..."
- Bryt ner i logiska delar med underrubriker
- Förklara HUR saker fungerar, inte bara VAD
- Inkludera diagram eller ASCII-art om det hjälper förståelsen

## 5. 💻 PRAKTISKA EXEMPEL
- 5-10 kodexempel beroende på ämnets komplexitet
- VARJE kodblock MÅSTE ha kommentarer som förklarar:
  - Vad kommandot gör
  - Vad varje flagga/argument betyder
  - Vad det förväntade resultatet är
  - Varför vi gör detta
- Progression från enkla till mer komplexa exempel
- Använd detta format för kodblock:

```bash
# === EXEMPEL: [Rubrik] ===

# Vad vi vill uppnå:
# [Förklaring]

kommando --flagga argument
# ↑ --flagga: förklaring av flaggan
# ↑ argument: förklaring av argumentet

# Förväntat resultat:
# [Visa output]
```

## 6. 🏋️ HANDS-ON ÖVNINGAR
EXAKT 3 övningar med denna progression:

### Övning 1: Grundläggande
- Direkt tillämpning av ett koncept
- Bör ta 5-10 minuter
- Tydliga steg-för-steg instruktioner

### Övning 2: Tillämpad
- Kombinera 2-3 koncept från noden
- Bör ta 10-15 minuter
- Mer öppen problemformulering

### Övning 3: Utmanande
- Kräver eftertanke och problemlösning
- Bör ta 15-20 minuter
- Simulerar ett verkligt scenario

För VARJE övning, inkludera:
- **Mål:** Vad ska uppnås
- **Scenario:** Kontext (om relevant)
- **Din uppgift:** Numrerade steg
- **Ledtråd:** I <details> tag
- **Lösning:** I <details> tag med fullständig kod och kommentarer
- **Verifikation:** Hur användaren vet att de lyckats

## 7. ⚠️ VANLIGA MISSTAG & FELSÖKNING
- 3-5 vanliga problem
- För varje misstag:
  - ❌ Vad användaren gör fel
  - 💥 Vad som händer (felmeddelande/symptom)
  - ✅ Hur man löser det
- Inkludera exakta kommandon för att fixa

## 8. 💡 BEST PRACTICES & TIPS
- Minst 2-3 användbara alias att lägga i .bashrc/.zshrc
- Keyboard shortcuts om relevant
- Produktivitetstips
- "Pro tips" från verkliga erfarenheter
- Format för alias:
```bash
# Lägg till i ~/.bashrc eller ~/.zshrc:
alias kortnamn='långt kommando'
# Användning: kortnamn argument
```

## 9. 🔧 DEVOPS I PRAKTIKEN
- Minst 2 verkliga scenarion där detta används
- Koppla till:
  - CI/CD pipelines
  - Containerisering
  - Kubernetes/orchestration
  - Monitoring/logging
  - Infrastructure as Code
  - Incident response
- Visa konkreta exempel på hur detta ser ut i produktion

## 10. 📝 SAMMANFATTNING
- Rubrik: "Det viktigaste att ta med sig"
- 5-7 bullet points
- Ska fungera som ett "cheat sheet"
- Inkludera de viktigaste kommandona och koncepten
- Format: **[Koncept]:** En mening förklaring

## 11. 🚀 NÄSTA STEG
- Vad bygger på denna kunskap?
- Namnge nästa nod och vad den handlar om
- Förslag på egen övning/fördjupning
- Eventuella externa resurser (man pages, dokumentation)

═══════════════════════════════════════════════════════════════
STILKRAV
═══════════════════════════════════════════════════════════════

SPRÅK:
- Skriv på SVENSKA
- Använd "du" (aldrig "man" eller "vi")
- Tekniska termer på engelska där det är standard
- Kodkommentarer på svenska för förklaringar

TON:
- Vänlig mentor, inte akademisk föreläsare
- Engagerande och uppmuntrande
- Praktisk och handfast
- Använd vardagliga analogier

FORMATERING:
- Emojis i sektionsrubriker (sparsamt)
- Kodblock med språkspecifikation (```bash, ```yaml, etc.)
- Tabeller för jämförelser
- <details> för dolda lösningar och ledtrådar

KODBLOCK:
- ALLA kommandon måste ha förklarande kommentarer
- Visa förväntat output där relevant
- Förklara VARFÖR, inte bara VAD

═══════════════════════════════════════════════════════════════
KVALITETSKRAV
═══════════════════════════════════════════════════════════════

Innan du levererar, verifiera:
✓ Alla kodexempel är korrekta och fungerar på Ubuntu/Debian
✓ Varje kodblock har förklarande kommentarer
✓ Alla 3 övningar har komplett struktur inkl. dolda lösningar
✓ Minst 3 vanliga misstag täcks
✓ Minst 2 alias/tips finns
✓ DevOps-koppling är tydlig och konkret
✓ Sammanfattningen fungerar som cheat sheet
✓ Nästa steg pekar framåt i modulen

═══════════════════════════════════════════════════════════════

Generera nu komplett innehåll för noden "[NOD_TITEL]".
```

---

## 📝 EXEMPEL PÅ IFYLLD PROMPT

```
Modul: Linux Mastery
Nod: 1 av 20
Titel: Filesystem Hierarchy Standard (FHS)
Svårighetsgrad: Lätt
Uppskattad tid: 45 minuter
XP: 75 poäng

Tidigare nod: Ingen (första noden)
Nästa nod: Mount Points och Device Files
```

---

## ✅ VERIFIERINGSCHECKLISTA

Efter generering, kontrollera:

- [ ] Hook är engagerande och förklarar relevans
- [ ] Exakt 4-5 lärandemål finns
- [ ] Alla kodexempel har kommentarer
- [ ] Exakt 3 övningar med rätt progression
- [ ] Lösningar är i <details> tags
- [ ] 3-5 vanliga misstag täcks
- [ ] Minst 2 alias finns
- [ ] 2+ DevOps-scenarion inkluderade
- [ ] Sammanfattning har 5-7 punkter
- [ ] Nästa steg refererar korrekt nod

---

## 🔄 BATCH-GENERERING

För att generera flera noder i sekvens:

1. Förbered lista med alla nodtitlar
2. Kör prompten för nod 1
3. Spara output
4. Uppdatera "Tidigare nod" och "Nästa nod"
5. Kör för nod 2
6. Repetera

---

*Master Prompt version 1.0 - DevOpsHub*
