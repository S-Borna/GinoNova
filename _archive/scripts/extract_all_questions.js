/**
 * Extraherar alla Omtenta 2.0 frågor till en granskningsfil
 */
const fs = require('fs');

let output = `# OMTENTA 2.0 - ALLA FRÅGOR FÖR GRANSKNING

Genererad: ${new Date().toISOString().split('T')[0]}

**Totalt: 700 frågor (500 quiz + 200 scenarios)**

Markera frågor du vill ta bort med ❌ så fixar jag det.

---

`;

const nodNames = {
    'nod1-filsystem': 'Filsystem & Grunder',
    'nod2-rattigheter': 'Rättigheter & Säkerhet',
    'nod3-processhantering': 'Processhantering',
    'nod4-natverk': 'Nätverk & Server',
    'nod5-ssh': 'SSH & Kommunikation',
    'nod6-bash-skript': 'Bash Skript',
    'nod7-bash-verktyg': 'Bash Verktyg',
    'nod8-docker-isolering': 'Docker & Isolering',
    'nod9-docker-natverk': 'Docker Nätverk & Lagring',
    'nod10-docker-compose': 'Docker Compose & IaC'
};

// Process each nod
for (let nod = 1; nod <= 10; nod++) {
    const topicKey = `nod${nod}-${['filsystem', 'rattigheter', 'processhantering', 'natverk', 'ssh', 'bash-skript', 'bash-verktyg', 'docker-isolering', 'docker-natverk', 'docker-compose'][nod - 1]}`;
    const topicName = nodNames[topicKey] || `Nod ${nod}`;

    output += `## NOD ${nod}: ${topicName}\n\n`;

    // QUIZ questions
    try {
        const examFile = fs.readFileSync(`./apps/frontend/src/data/exam-nod${nod}-questions.ts`, 'utf8');

        // Simple regex to extract questions
        const questionRegex = /\{\s*id:\s*'([^']+)'[\s\S]*?question:\s*'([^']*(?:\\.[^']*)*)'[\s\S]*?difficulty:\s*'([^']+)'/g;

        output += `### Quiz (50 frågor)\n\n`;
        let match;
        let qNum = 1;
        while ((match = questionRegex.exec(examFile)) !== null) {
            const [_, id, question, difficulty] = match;
            // Unescape the question
            const cleanQ = question.replace(/\\'/g, "'").replace(/\\n/g, ' ');
            output += `${qNum}. **[${difficulty}]** ${cleanQ}\n`;
            qNum++;
        }
        output += `\n`;
    } catch (e) {
        output += `*Kunde inte läsa exam-nod${nod}-questions.ts*\n\n`;
    }

    // SCENARIO questions
    try {
        const scenFile = fs.readFileSync(`./apps/frontend/src/data/scenario-nod${nod}-questions.ts`, 'utf8');

        const questionRegex = /\{\s*id:\s*'([^']+)'[\s\S]*?question:\s*'([^']*(?:\\.[^']*)*)'[\s\S]*?difficulty:\s*'([^']+)'/g;

        output += `### Scenarios (20 frågor)\n\n`;
        let match;
        let sNum = 1;
        while ((match = questionRegex.exec(scenFile)) !== null) {
            const [_, id, question, difficulty] = match;
            const cleanQ = question.replace(/\\'/g, "'").replace(/\\n/g, ' ');
            output += `${sNum}. **[${difficulty}]** ${cleanQ}\n`;
            sNum++;
        }
        output += `\n`;
    } catch (e) {
        output += `*Kunde inte läsa scenario-nod${nod}-questions.ts*\n\n`;
    }

    output += `---\n\n`;
}

fs.writeFileSync('./OMTENTA_2_FRAGOR_GRANSKNING.md', output);
console.log('✅ Fil skapad: OMTENTA_2_FRAGOR_GRANSKNING.md');
console.log('Öppna filen och markera frågor du vill ta bort med ❌');
