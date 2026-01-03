# AI Quiz Generator - Kostnadsanalys

## Nuvarande Setup (GPT-4o-mini)

### Priser per 1M tokens:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.60 per 1M tokens

### Typisk Quiz Generation:
- **Input tokens**: ~2,500 tokens (prompt + 4000 chars content)
- **Output tokens**: ~1,800 tokens (10 MCQ med förklaringar)

**Kostnad per quiz:**
- Input: (2,500 / 1,000,000) × $0.15 = **$0.000375**
- Output: (1,800 / 1,000,000) × $0.60 = **$0.00108**
- **Total: ~$0.0015 per quiz** (0.15 cent)

---

## GPT-4-turbo (Förbättrad Kvalitet)

### Priser per 1M tokens:
- **Input**: $10 per 1M tokens
- **Output**: $30 per 1M tokens

### Typisk Quiz Generation (samma tokens):
- **Input tokens**: ~2,500 tokens
- **Output tokens**: ~1,800 tokens

**Kostnad per quiz:**
- Input: (2,500 / 1,000,000) × $10 = **$0.025**
- Output: (1,800 / 1,000,000) × $30 = **$0.054**
- **Total: ~$0.079 per quiz** (7.9 cent)

---

## Kostnadsjämförelse

| Modell | Kostnad per Quiz | Förhållande |
|--------|------------------|-------------|
| **GPT-4o-mini** (nuvarande) | $0.0015 | 1x |
| **GPT-4-turbo** | $0.079 | **53x dyrare** |

### Månadskostnad (exempel):

**Scenario 1: Låg användning (100 quiz/månad)**
- GPT-4o-mini: $0.15/månad
- GPT-4-turbo: $7.90/månad
- **Skillnad: +$7.75/månad**

**Scenario 2: Medel användning (500 quiz/månad)**
- GPT-4o-mini: $0.75/månad
- GPT-4-turbo: $39.50/månad
- **Skillnad: +$38.75/månad**

**Scenario 3: Hög användning (2000 quiz/månad)**
- GPT-4o-mini: $3.00/månad
- GPT-4-turbo: $158/månad
- **Skillnad: +$155/månad**

---

## Alternativ: GPT-4o (Balans mellan kvalitet och kostnad)

### Priser per 1M tokens:
- **Input**: $5 per 1M tokens
- **Output**: $15 per 1M tokens

**Kostnad per quiz:**
- Input: (2,500 / 1,000,000) × $5 = **$0.0125**
- Output: (1,800 / 1,000,000) × $15 = **$0.027**
- **Total: ~$0.04 per quiz** (4 cent)

### Jämförelse:
- GPT-4o-mini: $0.0015 (1x)
- GPT-4o: $0.04 (**27x dyrare**)
- GPT-4-turbo: $0.079 (53x dyrare)

---

## Rekommendationer

### Option 1: Hybrid Approach (Bäst balans)
- **Standard quiz**: GPT-4o-mini (billigt)
- **Premium quiz** (användare betalar extra): GPT-4-turbo (hög kvalitet)
- **Studyroom flashcards**: GPT-4o (balans)

### Option 2: Uppgradera till GPT-4o
- **27x dyrare** än mini, men **2x billigare** än turbo
- Betydligt bättre kvalitet än mini
- Fortfarande hanterbart för de flesta användningsscenarion

### Option 3: Smart Caching
- Cache genererade quiz per modul
- Generera en gång, använd många gånger
- Minska API-anrop med 80-90%

---

## Kostnadskontroll

### Strategier för att hålla kostnader nere:

1. **Caching**: Cache quiz per modul + difficulty + count
   - Minska kostnad med 80-90%
   - Användare får snabbare svar

2. **Rate Limiting**: 
   - Max 10 quiz per användare per dag
   - Premium: obegränsat

3. **Hybrid Model**:
   - Standard: GPT-4o-mini
   - Premium: GPT-4-turbo (användare betalar extra)

4. **Token Optimization**:
   - Öka content limit men optimera prompt
   - Använd summarization för långa moduler

---

## Sammanfattning

**GPT-4-turbo är 53x dyrare** än GPT-4o-mini, men ger betydligt bättre kvalitet.

**För 100 quiz/månad:**
- Mini: $0.15
- Turbo: $7.90
- **+$7.75 extra**

**För 1000 quiz/månad:**
- Mini: $1.50
- Turbo: $79
- **+$77.50 extra**

**Rekommendation**: Börja med **GPT-4o** (27x dyrare, men 2x billigare än turbo) och implementera caching för att minska kostnader.

