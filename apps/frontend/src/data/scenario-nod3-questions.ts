/**
 * NOD 3: Processhantering - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD3_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod3-s1',
        question: 'Du kör ett långt kompileringskommando och inser att du behöver kolla något annat i terminalen. Hur pausar du processen tillfälligt?',
        options: ['Ctrl+C', 'Ctrl+Z', 'Ctrl+D', 'Ctrl+X'],
        correctIndices: [1],
        explanation: 'Ctrl+Z skickar SIGTSTP och pausar (stoppar) processen. Den kan återupptas med fg eller bg.',
        difficulty: 'G',
        category: 'Job Control',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s2',
        question: 'Du har stoppat en process med Ctrl+Z. Hur kör du den vidare i bakgrunden?',
        options: ['fg', 'bg', 'resume', 'continue'],
        correctIndices: [1],
        explanation: 'bg (background) återupptar stoppad process i bakgrunden. fg (foreground) tar tillbaka den till förgrunden.',
        difficulty: 'G',
        category: 'Job Control',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s3',
        question: 'Nginx svarar inte och du behöver tvångsstänga den. Du vet PID är 1234. Vilket kommando är mest brutalt?',
        options: ['kill 1234', 'kill -15 1234', 'kill -9 1234', 'killall nginx'],
        correctIndices: [2],
        explanation: 'kill -9 (SIGKILL) kan inte ignoreras - dödar processen omedelbart. -15 (SIGTERM) ger processen chans att städa upp.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s4',
        question: 'Du kör `top` och ser att load average är "4.50, 3.20, 2.10" på en server med 2 CPU-kärnor. Vad betyder det?',
        options: ['Servern är underbelastad', 'Servern är överbelastad - köer finns', 'RAM-minnet är slut', 'Nätverket är överbelastat'],
        correctIndices: [1],
        explanation: 'Load average > antal kärnor = processer köar. 4.50 på 2-kärnsystem = 2.25x överbelastat senaste minuten.',
        difficulty: 'VG',
        category: 'Load Average',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s5',
        question: 'Du vill hitta PID för alla nginx-processer. Vilket kommando är snabbast?',
        options: ['ps aux | grep nginx', 'pgrep nginx', 'pidof nginx', 'Alla fungerar men B och C är snabbare'],
        correctIndices: [3],
        explanation: 'pgrep och pidof är designade för detta och ger direkt PID. ps aux | grep visar mer info men är långsammare.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s6',
        question: 'Du behöver köra en backup som tar lång tid utan att blockera terminalen. Hur startar du den i bakgrunden direkt?',
        options: ['backup.sh &', 'bg backup.sh', 'nohup backup.sh', 'background backup.sh'],
        correctIndices: [0],
        explanation: '& i slutet startar kommandot direkt i bakgrunden. Du kan fortsätta använda terminalen.',
        difficulty: 'G',
        category: 'Job Control',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s7',
        question: 'Du SSH:ar till en server och startar en lång process. Vad händer om din SSH-session tappas?',
        options: ['Processen fortsätter', 'Processen får SIGHUP och dör', 'Processen pausas', 'Ingenting speciellt'],
        correctIndices: [1],
        explanation: 'När terminalen stängs skickas SIGHUP till barn-processer. Använd nohup eller screen/tmux för att undvika detta.',
        difficulty: 'VG',
        category: 'Signaler',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s8',
        question: 'Du kör `ps aux` och ser en process med state "Z". Vad betyder det?',
        options: ['Processen zoomar (hög CPU)', 'Zombie - avslutad men väntar på parent', 'Processen är zippad', 'Zero resources används'],
        correctIndices: [1],
        explanation: 'Z = Zombie. Processen har avslutats men parent har inte hämtat exit-status. Försvinner när parent gör wait().',
        difficulty: 'VG',
        category: 'Processtillstånd',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s9',
        question: 'En process äter för mycket CPU. Du vill sänka dess prioritet utan att döda den. Vilket kommando?',
        options: ['nice processname', 'renice 10 -p PID', 'kill -STOP PID', 'priority --low PID'],
        correctIndices: [1],
        explanation: 'renice ändrar nice-värde på körande process. Högre nice = lägre prioritet. Nice-värden: -20 till 19.',
        difficulty: 'VG',
        category: 'Nice',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s10',
        question: 'Du vill starta ett kommando med lägre prioritet direkt. Vilket prefix använder du?',
        options: ['low command', 'nice command', 'slow command', 'priority -l command'],
        correctIndices: [1],
        explanation: 'nice command startar med nice-värde 10 (lägre prio). nice -n 19 command = lägsta prioritet.',
        difficulty: 'G',
        category: 'Nice',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s11',
        question: 'Vilken signal skickas default när du kör `kill PID` utan att ange signalnummer?',
        options: ['SIGKILL (9)', 'SIGTERM (15)', 'SIGHUP (1)', 'SIGSTOP (19)'],
        correctIndices: [1],
        explanation: 'kill utan signal skickar SIGTERM (15) - en "snäll" begäran att avsluta. Processen kan hantera den.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s12',
        question: 'Du vill se alla processer som körs av användaren "deploy". Vilket kommando?',
        options: ['ps -u deploy', 'ps aux | grep deploy', 'top -u deploy', 'Alla fungerar'],
        correctIndices: [3],
        explanation: 'ps -u filtrerar per användare, grep söker i output, top -u filtrerar i interaktivt läge. Alla fungerar.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s13',
        question: 'Du behöver lista alla bakgrundsjobb i current shell. Vilket kommando?',
        options: ['ps aux', 'bg -l', 'jobs', 'background --list'],
        correctIndices: [2],
        explanation: 'jobs visar bakgrundsjobb för aktuell shell-session. ps visar alla processer systemwide.',
        difficulty: 'G',
        category: 'Job Control',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s14',
        question: 'Du kör `kill -0 1234`. Processen dör inte. Vad gör kill -0?',
        options: ['Skickar null-signal - testar bara om processen finns', 'Soft kill - väntar tills processen är klar', 'Freeze - pausar processen', 'Reset - startar om processen'],
        correctIndices: [0],
        explanation: 'Signal 0 skickar ingenting - den testar bara om du har permission att signalera processen och om den finns.',
        difficulty: 'VG',
        category: 'Signaler',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s15',
        question: 'Du vill att ett skript ska fortsätta köra även om du loggar ut. Hur startar du det?',
        options: ['start script.sh', 'nohup script.sh &', 'forever script.sh', 'daemon script.sh'],
        correctIndices: [1],
        explanation: 'nohup ignorerar SIGHUP så processen överlever logout. & kör i bakgrunden. Kombinationen är standard.',
        difficulty: 'G',
        category: 'Job Control',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s16',
        question: 'Du behöver döda alla processer som heter "node". Vilket kommando dödar alla på en gång?',
        options: ['kill node', 'killall node', 'pkill node', 'Både B och C fungerar'],
        correctIndices: [3],
        explanation: 'killall och pkill dödar processer efter namn. killall matchar exakt, pkill stödjer regex.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s17',
        question: 'Du ser "D" state på en process i ps output. Vad betyder det och kan du döda den?',
        options: ['Dead - redan död', 'Disk sleep - väntar på I/O, kan inte dödas med SIGKILL', 'Daemon - bakgrundsprocess', 'Debug - i debugläge'],
        correctIndices: [1],
        explanation: 'D = Uninterruptible sleep (disk). Processen väntar på I/O och kan INTE dödas - måste vänta ut.',
        difficulty: 'VG',
        category: 'Processtillstånd',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s18',
        question: 'Du vill övervaka minnesanvändning i realtid och se vilka processer som använder mest RAM. Vilket verktyg?',
        options: ['ps aux --sort=-%mem', 'top och tryck M', 'htop', 'Alla fungerar men htop är smidigast'],
        correctIndices: [3],
        explanation: 'htop är interaktivt med färger och scrollning. top+M sorterar på minne. ps är one-shot utan realtid.',
        difficulty: 'G',
        category: 'Övervakning',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s19',
        question: 'Vad är skillnaden mellan en process och en tråd?',
        options: ['Samma sak', 'Trådar delar minne inom samma process', 'Processer är snabbare', 'Trådar kan bara finnas på multi-core'],
        correctIndices: [1],
        explanation: 'Trådar delar minnesrymd med sin process. Processer har isolerat minne. Trådar är "lättare" att skapa.',
        difficulty: 'VG',
        category: 'Koncept',
        topic: 'nod3-processhantering',
        type: 'scenario'
    },
    {
        id: 'nod3-s20',
        question: 'Du behöver skicka SIGHUP till nginx för att ladda om config utan att starta om. Vilket kommando?',
        options: ['kill -1 $(pgrep nginx)', 'kill -HUP $(pidof nginx)', 'nginx -s reload', 'Alla gör samma sak'],
        correctIndices: [3],
        explanation: 'SIGHUP (signal 1) används ofta för config reload. nginx -s reload gör samma sak internt.',
        difficulty: 'VG',
        category: 'Signaler',
        topic: 'nod3-processhantering',
        type: 'scenario'
    }
]
