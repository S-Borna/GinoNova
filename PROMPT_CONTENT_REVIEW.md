# PROMPT: Innehållsgranskning - Studiematerial vs Kursmoduler

## Uppdrag

Jämför de 10 studiefiler som ligger i projektets root-katalog med de befintliga kursmodulerna **Linux 24/7** och **DOE25 Tentaplugg**.

## Filer att granska (root-katalogen)

1. `Linux_Filesystem_Deep_Dive.md`
2. `Permissions_Security.md`
3. `Process_Management.md`
4. `Networking_Server.md`
5. `SSH_Communication.md`
6. `Bash_Scripting.md`
7. `Bash_Power_Tools.md`
8. `Docker_Fundamentals.md`
9. `Docker_Networking_Storage.md`
10. `Docker_Compose_IaC.md`

## Kursmoduler att jämföra mot

- **Linux 24/7**: `content-source/modules/linux-247/`
- **DOE25 Tentaplugg**: `content-source/modules/doe25-tentaplugg/`

## Bedömningskriterier

### Kriterium 1: Svårighetsgrad

**Målgrupp**: DevOps-studenter som nyss påbörjat sin utbildning och har en Linux-tenta att skriva.

Bedöm för varje fil:
- [ ] Är språket begripligt för nybörjare?
- [ ] Förklaras koncept från grunden innan avancerade ämnen?
- [ ] Finns det tillräckligt med konkreta exempel?
- [ ] Är progressionen logisk (enkelt → svårt)?
- [ ] Undviks onödig komplexitet som kan förvirra?

**Skala**: 
- ⭐ För svårt för nybörjare
- ⭐⭐ Något för avancerat
- ⭐⭐⭐ Lagom nivå
- ⭐⭐⭐⭐ Perfekt anpassat
- ⭐⭐⭐⭐⭐ Utmärkt pedagogiskt upplägg

### Kriterium 2: Tentaberedskap

**Krav**: Har man läst igenom modulerna ska man per automatik kunna klara av prov på Linux-kursen.

Bedöm för varje fil:
- [ ] Täcks alla kärnkoncept som förväntas på tentan?
- [ ] Finns praktiska kommandon och syntax tydligt förklarade?
- [ ] Inkluderas vanliga tentafrågor/scenarion?
- [ ] Finns "viktiga takeaways" eller sammanfattningar?
- [ ] Är innehållet tillräckligt djupt för att förstå "varför", inte bara "hur"?

**Skala**:
- 🔴 Otillräckligt för tenta
- 🟡 Behöver komplettering
- 🟢 Täcker grunderna
- 🔵 Bra tentaförberedelse
- 🟣 Excellent - garanterar godkänt

## Önskat output

### 1. Översiktstabell

| Fil | Svårighetsgrad | Tentaberedskap | Täckning vs Linux 24/7 | Täckning vs DOE25 |
|-----|----------------|----------------|------------------------|-------------------|
| ... | ⭐⭐⭐ | 🟢 | 80% | 95% |

### 2. Detaljerad analys per fil

För varje fil, ange:
- **Styrkor**: Vad är bra?
- **Svagheter**: Vad saknas eller kan förbättras?
- **Jämförelse**: Hur förhåller sig innehållet till Linux 24/7 och DOE25?
- **Rekommendation**: Behövs ändringar?

### 3. Gap-analys

Identifiera:
- Ämnen som saknas helt i studiefilerna men finns i kursmodulerna
- Ämnen som är bättre täckta i studiefilerna än i kursmodulerna
- Överlappningar och redundans

### 4. Slutsats och rekommendation

Besvara:
1. **Kan en student klara Linux-tentan genom att endast läsa dessa 10 filer?**
2. **Vilka filer bör prioriteras för tentaplugg?**
3. **Vilka kompletteringar behövs (om några)?**
4. **Rekommenderad läsordning för optimal inlärning?**

## Instruktioner för genomförande

```
1. Läs igenom alla 10 studiefiler i root
2. Läs igenom alla noder i Linux 24/7 modulen
3. Läs igenom alla noder i DOE25 Tentaplugg modulen
4. Jämför innehåll, djup och pedagogik
5. Fyll i tabellen och analysera enligt kriterierna
6. Ge en ärlig och konstruktiv bedömning
```

## Viktigt

- Var **ärlig** - om något är dåligt, säg det
- Var **specifik** - undvik vaga omdömen
- Var **konstruktiv** - ge konkreta förbättringsförslag
- Fokusera på **studentens behov** - inte teknisk perfektion

---

*Prompt skapad: 14 januari 2026*
*Syfte: Kvalitetssäkring av studiematerial inför Linux-tenta*
