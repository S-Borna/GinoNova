/**
 * NOD 7: Bash Verktyg - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD7_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod7-s1',
        question: 'Du behöver hitta alla rader i /var/log/syslog som innehåller "error". Kommando?',
        options: ['find "error" /var/log/syslog', 'grep "error" /var/log/syslog', 'search "error" /var/log/syslog', 'cat /var/log/syslog | filter "error"'],
        correctIndices: [1],
        explanation: 'grep (Global Regular Expression Print) söker efter mönster i text. Grundläggande Linux-verktyg.',
        difficulty: 'G',
        category: 'grep',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s2',
        question: 'Du vill söka efter "ERROR" case-insensitive (matcha error, Error, ERROR). Grep-flagga?',
        options: ['grep -s', 'grep -i', 'grep -c', 'grep -I'],
        correctIndices: [1],
        explanation: '-i = ignore case. Matchar oavsett stora/små bokstäver. Mycket användbart i loggsökning.',
        difficulty: 'G',
        category: 'grep',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s3',
        question: 'Du vill ersätta alla "http" med "https" i en config-fil. Vilket verktyg?',
        options: ['grep', 'sed', 'awk', 'tr'],
        correctIndices: [1],
        explanation: 'sed (Stream Editor) är perfekt för text-substitution. sed "s/http/https/g" fil.',
        difficulty: 'G',
        category: 'sed',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s4',
        question: 'Du har en CSV-fil och behöver extrahera bara kolumn 3 (komma-separerad). Kommando?',
        options: ['cut -d"," -f3 fil.csv', 'awk -F"," \'{print $3}\' fil.csv', 'sed -n "3p" fil.csv', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: 'cut -d -f och awk -F båda hanterar fält-extraktion. awk är kraftfullare för komplex logik.',
        difficulty: 'VG',
        category: 'awk/cut',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s5',
        question: 'Du vill hitta alla .conf filer under /etc rekursivt. Kommando?',
        options: ['ls -R /etc/*.conf', 'find /etc -name "*.conf"', 'grep -r ".conf" /etc', 'search /etc *.conf'],
        correctIndices: [1],
        explanation: 'find söker filer baserat på kriterier. -name för namn-mönster, -type f för filer.',
        difficulty: 'G',
        category: 'find',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s6',
        question: 'Du vill sortera en fil med IP-adresser numeriskt (inte alfabetiskt). Flagga för sort?',
        options: ['sort -n fil', 'sort -V fil', 'sort -t. -k1,1n -k2,2n -k3,3n -k4,4n fil', 'Både B och C fungerar för IP'],
        correctIndices: [3],
        explanation: '-V = version sort (smart för IP). Alternativt specificera varje oktett som numerisk key.',
        difficulty: 'VG',
        category: 'sort',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s7',
        question: 'Du har en loggfil med dubbletter och vill bara se unika rader. Kommando?',
        options: ['unique logfil', 'uniq logfil', 'distinct logfil', 'dedup logfil'],
        correctIndices: [1],
        explanation: 'uniq filtrerar bort intilliggande dubbletter. OBS: filen måste vara sorterad först! sort fil | uniq.',
        difficulty: 'G',
        category: 'uniq',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s8',
        question: 'Du vill räkna antal rader i en fil. Snabbaste kommando?',
        options: ['cat fil | count', 'wc -l fil', 'count -lines fil', 'grep -c "" fil'],
        correctIndices: [1],
        explanation: 'wc (word count) med -l räknar rader. -w = ord, -c = bytes, -m = tecken.',
        difficulty: 'G',
        category: 'wc',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s9',
        question: 'Du vill se de 50 senaste raderna i en loggfil. Kommando?',
        options: ['head -50 logfil', 'tail -50 logfil', 'last 50 logfil', 'bottom -50 logfil'],
        correctIndices: [1],
        explanation: 'tail visar slutet av fil (default 10 rader). tail -n 50 eller tail -50 för 50 rader.',
        difficulty: 'G',
        category: 'head/tail',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s10',
        question: 'Du vill konvertera alla gemener till versaler i en fil. Vilket verktyg?',
        options: ['sed "y/a-z/A-Z/"', 'tr "a-z" "A-Z"', 'awk "{print toupper($0)}"', 'Alla fungerar'],
        correctIndices: [3],
        explanation: 'tr translitererar tecken. sed y/ gör samma. awk toupper() för strings. Alla uppnår målet.',
        difficulty: 'VG',
        category: 'tr',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s11',
        question: 'Du vill hitta filer större än 100MB under /var. Find-syntax?',
        options: ['find /var -size 100M', 'find /var -size +100M', 'find /var -larger 100M', 'find /var --min-size 100M'],
        correctIndices: [1],
        explanation: '-size +100M = större än 100MB. -100M = mindre än. 100M exakt (sällsynt). M/G/k för enhet.',
        difficulty: 'G',
        category: 'find',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s12',
        question: 'Du vill söka efter "error" i alla filer under /var/log rekursivt. Grep-flagga?',
        options: ['grep "error" /var/log/*', 'grep -r "error" /var/log/', 'grep -R "error" /var/log/', 'Både B och C fungerar'],
        correctIndices: [3],
        explanation: '-r och -R är rekursiv sökning. -R följer symlinks, -r gör det inte (beroende på version).',
        difficulty: 'G',
        category: 'grep',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s13',
        question: 'Du vill visa radnummer i grep-output. Flagga?',
        options: ['grep -l', 'grep -n', 'grep -c', 'grep -v'],
        correctIndices: [1],
        explanation: '-n = line number. -l = endast filnamn, -c = count, -v = invert (visa INTE matchande).',
        difficulty: 'G',
        category: 'grep',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s14',
        question: 'Du vill editera fil in-place med sed (ändra direkt i filen). Flagga?',
        options: ['sed -i "s/old/new/" fil', 'sed -e "s/old/new/" fil', 'sed -w "s/old/new/" fil', 'sed --inplace "s/old/new/" fil'],
        correctIndices: [0],
        explanation: '-i = in-place edit. VARNING: gör backup först! Eller sed -i.bak för automatisk backup.',
        difficulty: 'VG',
        category: 'sed',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s15',
        question: 'Du vill hitta och radera alla .tmp filer under /var/tmp. Find + exec syntax?',
        options: ['find /var/tmp -name "*.tmp" -delete', 'find /var/tmp -name "*.tmp" -exec rm {} \\;', 'find /var/tmp -name "*.tmp" | rm', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: '-delete är enklast. -exec rm {} \\; kör rm på varje fil. {} = filnamnet.',
        difficulty: 'VG',
        category: 'find',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s16',
        question: 'Du vill extrahera bara IP-adresser från en loggfil. Bästa verktyg?',
        options: ['grep med regex', 'awk', 'sed', 'Alla kan göra det, grep -oE är enklast'],
        correctIndices: [3],
        explanation: 'grep -oE "[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+" visar bara matchande IP:er. -o = only matching.',
        difficulty: 'VG',
        category: 'grep',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s17',
        question: 'Du vill jämföra två config-filer och se skillnaderna. Kommando?',
        options: ['cmp fil1 fil2', 'diff fil1 fil2', 'compare fil1 fil2', 'Både A och B (men diff ger mer info)'],
        correctIndices: [3],
        explanation: 'diff visar skillnader rad för rad. cmp kollar bara OM de skiljer sig (första skillnaden).',
        difficulty: 'G',
        category: 'diff',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s18',
        question: 'Du vill köra kommando för varje rad i en fil. Vilken pipe-konstruktion?',
        options: ['cat fil | for line; do cmd; done', 'while read line; do cmd; done < fil', 'xargs cmd < fil', 'Både B och C beroende på behov'],
        correctIndices: [3],
        explanation: 'while read loopar med shell-variabler. xargs bygger kommandorader från input. Båda är kraftfulla.',
        difficulty: 'VG',
        category: 'xargs',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s19',
        question: 'Du vill sortera unikt OCH räkna förekomster. Pipeline?',
        options: ['sort fil | unique -c', 'sort fil | uniq -c', 'uniq fil | sort -c', 'count fil | sort'],
        correctIndices: [1],
        explanation: 'sort | uniq -c räknar förekomster av varje unik rad. -c = count prefix.',
        difficulty: 'G',
        category: 'uniq',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    },
    {
        id: 'nod7-s20',
        question: 'Du vill ta bort tomma rader från en fil. Sed-kommando?',
        options: ['sed "/^$/d" fil', 'sed "s/^$//g" fil', 'sed -empty fil', 'sed --delete-blank fil'],
        correctIndices: [0],
        explanation: '/^$/d raderar rader som matchar ^$ (tom rad). d = delete. Regex ^$ = start följt av slut = tom.',
        difficulty: 'VG',
        category: 'sed',
        topic: 'nod7-bash-verktyg',
        type: 'scenario'
    }
]
