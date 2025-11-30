# PROMPT 1: Fix [object Object] Bug

## KONTEXT

Du arbetar med DevOpsHub, en DevOps-utbildningsplattform.
Repository: S-Ebadi/saas-project
Backend: FastAPI (Railway)
Frontend: Next.js 15 (Netlify)

## PROBLEM

Kod-block i tasks visar `[object Object]` istället för faktisk kod.
Se screenshot: Bash-block och YAML-block visar bara `[object Object],` upprepat.

## ROTORSAK (trolig)

Task content lagras som objekt i databasen/seed men frontend försöker rendera det som string.
Alternativt: JSON.stringify() saknas någonstans, eller content-strukturen matchar inte frontend-förväntningar.

## UPPDRAG

### Steg 1: Hitta var content lagras
```bash
# Sök i backend efter task content struktur
grep -r "content" apps/backend/src/schemas/task.py
grep -r "code_blocks" apps/backend/src/
grep -r "TaskContent" apps/backend/src/
```

### Steg 2: Hitta var content renderas i frontend
```bash
# Sök i frontend efter kod-block rendering
grep -r "code" apps/frontend/src/components/
grep -r "CodeBlock" apps/frontend/src/
grep -r "pre>" apps/frontend/src/
```

### Steg 3: Identifiera mismatch
Jämför:
1. Hur content sparas (backend schema/seed)
2. Hur content skickas (API response)
3. Hur content renderas (frontend component)

### Steg 4: Fixa problemet
Troliga lösningar:
- Om content är objekt: `JSON.stringify(content)` eller extrahera rätt fält
- Om content är array: `.map()` och rendera varje element
- Om content har nested structure: Flatten eller traversera korrekt

### Steg 5: Verifiera
1. Starta lokal dev-miljö
2. Navigera till valfri task med kod-block
3. Verifiera att kod visas korrekt
4. Testa copy-to-clipboard funktion

## FÖRVÄNTAD OUTPUT

```typescript
// FÖRE (fel)
<pre>{content}</pre>  // Renderar [object Object]

// EFTER (rätt)
<pre>{typeof content === 'string' ? content : content.code || JSON.stringify(content, null, 2)}</pre>
```

## SUCCESS CRITERIA

- [ ] Alla kod-block visar faktisk kod
- [ ] Syntax highlighting fungerar
- [ ] Copy-button kopierar rätt innehåll
- [ ] Ingen `[object Object]` synlig någonstans

## COMMIT MESSAGE

```
fix(frontend): resolve [object Object] in code blocks

- Fixed content serialization in TaskContent component
- Added proper type checking for code block content
- Ensured code_blocks array is properly rendered

Fixes #XXX
```

## NÄSTA STEG

När denna bugg är fixad, fortsätt med PROMPT_2_content_audit.md
