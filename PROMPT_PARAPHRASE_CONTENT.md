# PROMPT: Omarbeta studiematerial till originalinnehåll

## Uppdrag

Gå igenom de 10 studiefilerna i projektets root-katalog och **parafrasera allt innehåll** så att det blir originalt. Texten ska sedan ersätta innehållet i modulen **DOE25 Tentaplugg**.

## ⚠️ KRITISKA REGLER

### Vad som SKA göras

- ✅ Skriv om ALLA rubriker till nya formuleringar (behåll samma betydelse)
- ✅ Parafrasera ALL brödtext till egna ord
- ✅ Omformulera förklaringar med egna meningar
- ✅ Behåll EXAKT samma faktainnehåll och kunskap
- ✅ Behåll samma struktur och upplägg
- ✅ Behåll alla kodexempel (kommandon är kommandon - de kan inte ändras)
- ✅ Skriv om kommentarer i kodblock till egna formuleringar

### Vad som INTE får göras

- ❌ Ta bort information
- ❌ Ändra fakta eller teknisk korrekthet
- ❌ Förkorta eller sammanfatta innehållet
- ❌ Lägga till ny information som inte fanns
- ❌ Ändra kommandon eller syntax (bara förklarande text)

## Filer att omarbeta (root-katalogen)

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

## Destination

Ersätt ALLT befintligt innehåll i: `content-source/modules/doe25-tentaplugg/`

## Exempel på omarbetning

### ORIGINAL (kopierat)

```markdown
# Docker Fundamentals – Isolation & Images

Fokus: Containrar vs Virtuella Maskiner

## Container Architecture: Namespaces och Cgroups

Docker använder Linux-kärnans inbyggda funktioner för isolering:
```

### OMARBETAT (eget)

```markdown
# Docker-grunder – Isolering och Images

Fokus: Skillnaden mellan containrar och virtuella maskiner

## Containerarkitektur: Namespaces och Cgroups

Docker utnyttjar funktioner som är inbyggda i Linux-kärnan för att åstadkomma isolering:
```

### ORIGINAL kodkommentar

```bash
# Se namespaces för en container
docker inspect <container_id> | grep -i namespace
```

### OMARBETAT kodkommentar

```bash
# Visa namespace-information för en specifik container
docker inspect <container_id> | grep -i namespace
```

## Arbetsflöde

För varje fil (1-10):

```
1. Läs hela filen
2. Skriv om huvudrubriken (H1)
3. Skriv om alla underrubriker (H2, H3, etc.)
4. Parafrasera all brödtext stycke för stycke
5. Behåll kodblock men skriv om kommentarer
6. Behåll "Viktiga takeaways" men omformulera punkterna
7. Spara som ny fil i doe25-tentaplugg med lämpligt node-namn
```

## Filnamnskonvertering

| Original fil | DOE25 node-namn |
|--------------|-----------------|
| Linux_Filesystem_Deep_Dive.md | `01-filsystem-grunder.md` |
| Permissions_Security.md | `02-rattigheter-sakerhet.md` |
| Process_Management.md | `03-processhantering.md` |
| Networking_Server.md | `04-natverk-server.md` |
| SSH_Communication.md | `05-ssh-kommunikation.md` |
| Bash_Scripting.md | `06-bash-skript.md` |
| Bash_Power_Tools.md | `07-bash-verktyg.md` |
| Docker_Fundamentals.md | `08-docker-grunder.md` |
| Docker_Networking_Storage.md | `09-docker-natverk-lagring.md` |
| Docker_Compose_IaC.md | `10-docker-compose.md` |

## Kvalitetskontroll

Efter omarbetning, verifiera för varje fil:

- [ ] Alla rubriker är omformulerade
- [ ] All brödtext är parafraserad
- [ ] Kodexempel är intakta (bara kommentarer ändrade)
- [ ] Ingen information har tagits bort
- [ ] Samma kunskap förmedlas
- [ ] Texten känns naturlig på svenska

## Node-format för DOE25

Varje fil ska ha korrekt frontmatter:

```yaml
---
title: "[Omarbetad titel]"
description: "[Kort beskrivning]"
order: [1-10]
---
```

## Viktigt om upphovsrätt

Syftet är att skapa **originalt kursmaterial** baserat på samma kunskapsinnehåll.

- Fakta och kunskap kan inte skyddas av upphovsrätt
- Men specifika formuleringar och uttryck kan det
- Därför ska ALL text skrivas om till egna ord
- Kommandon och syntax är tekniska standarder - de behöver inte ändras

## Ta bort gammalt innehåll

INNAN de nya filerna skapas:

1. Lista alla befintliga filer i `content-source/modules/doe25-tentaplugg/`
2. Ta bort ALLA befintliga node-filer (behåll bara _meta.json om den finns)
3. Skapa de 10 nya filerna med omarbetat innehåll
4. Uppdatera _meta.json med nya node-referenser

---

*Prompt skapad: 14 januari 2026*
*Syfte: Skapa originalt kursmaterial för DOE25 Tentaplugg-modulen*
