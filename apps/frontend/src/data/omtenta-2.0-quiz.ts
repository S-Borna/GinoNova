/**
 * OMTENTA 2.0 - Komplett frågebank från alla 10 NOD-moduler
 *
 * INNEHÅLL:
 * - Nod 1: Linux Filsystem & Grunder (50 quiz + 30 scenarios)
 * - Nod 2: Rättigheter & Säkerhet (50 quiz + 30 scenarios)
 * - Nod 3: Processhantering (50 quiz + 30 scenarios)
 * - Nod 4: Nätverk & Server (50 quiz + 30 scenarios)
 * - Nod 5: SSH & Kommunikation (50 quiz + 30 scenarios)
 * - Nod 6: Bash Skriptprogrammering (50 quiz + 30 scenarios)
 * - Nod 7: Bash Verktyg (50 quiz + 30 scenarios)
 * - Nod 8: Docker Isolering & Images (50 quiz + 30 scenarios)
 * - Nod 9: Docker Nätverk & Lagring (50 quiz + 30 scenarios)
 * - Nod 10: Docker Compose & IaC (50 quiz + 30 scenarios)
 *
 * TOTAL: ~800 frågor
 */

// Import NOD3-10 från auto-genererad fil
import {
    NOD3_PROCESSHANTERING_QUESTIONS,
    NOD4_NATVERK_QUESTIONS,
    NOD5_SSH_QUESTIONS,
    NOD6_BASH_SKRIPT_QUESTIONS,
    NOD7_BASH_VERKTYG_QUESTIONS,
    NOD8_DOCKER_ISOLERING_QUESTIONS,
    NOD9_DOCKER_NATVERK_QUESTIONS,
    NOD10_DOCKER_COMPOSE_QUESTIONS
} from './nod3-10-questions'

export type Omtenta2Topic =
    | 'nod1-filsystem'
    | 'nod2-rattigheter'
    | 'nod3-processhantering'
    | 'nod4-natverk'
    | 'nod5-ssh'
    | 'nod6-bash-skript'
    | 'nod7-bash-verktyg'
    | 'nod8-docker-isolering'
    | 'nod9-docker-natverk'
    | 'nod10-docker-compose'

export interface Omtenta2Question {
    id: string
    question: string
    options: string[]
    correctIndices: number[]
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    topic: Omtenta2Topic
    type: 'quiz' | 'scenario'
}

export const OMTENTA2_TOPIC_INFO: Record<Omtenta2Topic, { name: string; description: string }> = {
    'nod1-filsystem': { name: 'Nod 1: Filsystem & Grunder', description: 'FHS, kataloger, inodes, länkar, mount points' },
    'nod2-rattigheter': { name: 'Nod 2: Rättigheter & Säkerhet', description: 'chmod, chown, sudo, SSH-nycklar, UFW' },
    'nod3-processhantering': { name: 'Nod 3: Processhantering', description: 'Processer, signaler, jobs, load average' },
    'nod4-natverk': { name: 'Nod 4: Nätverk & Server', description: 'IP, subnetting, TCP/UDP, DNS, routing' },
    'nod5-ssh': { name: 'Nod 5: SSH & Kommunikation', description: 'SSH-nycklar, agent, forwarding, tunnlar' },
    'nod6-bash-skript': { name: 'Nod 6: Bash Skript', description: 'Variabler, loopar, villkor, funktioner' },
    'nod7-bash-verktyg': { name: 'Nod 7: Bash Verktyg', description: 'grep, sed, awk, sort, pipes, redirections' },
    'nod8-docker-isolering': { name: 'Nod 8: Docker & Isolering', description: 'Containers vs VMs, images, Dockerfile' },
    'nod9-docker-natverk': { name: 'Nod 9: Docker Nätverk & Lagring', description: 'Volumes, bind mounts, networks' },
    'nod10-docker-compose': { name: 'Nod 10: Docker Compose & IaC', description: 'docker-compose.yml, services, IaC' }
}

// ===== NOD 1: FILSYSTEM & GRUNDER =====
export const NOD1_QUESTIONS: Omtenta2Question[] = [
    // QUIZ FRÅGOR
    {
        id: 'nod1-q1',
        question: 'Vilken av följande kataloger ska endast innehålla binärer som krävs för att starta systemet i single-user mode?',
        options: ['/bin', '/usr/bin', '/boot/bin', '/opt/bin'],
        correctIndices: [0],
        explanation: '/bin innehåller essentiella binärer som krävs för systemstart och single-user mode.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q2',
        question: 'Du söker efter konfigurationsfilen för SSH-servern. Var letar du först?',
        options: ['/etc/ssh/sshd_config', '/var/ssh/sshd_config', '/usr/local/ssh/config', '/home/root/ssh_config'],
        correctIndices: [0],
        explanation: '/etc/ssh/sshd_config är standardplatsen för SSH-serverkonfiguration.',
        difficulty: 'G',
        category: 'Konfiguration',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q3',
        question: 'Vad är det primära syftet med katalogen /tmp?',
        options: ['Att lagra temporära filer som kan raderas vid omstart.', 'Att lagra användarnas personliga dokument.', 'Att lagra säkerhetskopior av systemet.', 'Att installera tillfälliga applikationer.'],
        correctIndices: [0],
        explanation: '/tmp är avsedd för temporära filer som rensas vid omstart.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q4',
        question: 'Vilket uttalande stämmer bäst överens med Linux-filosofin angående hårdvara?',
        options: ['Hårdvara representeras ofta som filer i /dev.', 'Hårdvara styrs enbart via grafiska drivrutiner.', 'Hårdvara är helt dolt från filsystemet.', 'Hårdvara hanteras via systemregistret i /reg.'],
        correctIndices: [0],
        explanation: 'I Linux representeras hårdvara som filer i /dev-katalogen.',
        difficulty: 'G',
        category: 'Linux-filosofi',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q5',
        question: 'Om du vill se hur mycket diskutrymme som är ledigt på filsystemet, vilket kommando kör du?',
        options: ['df -h', 'du -h', 'ls -size', 'top memory'],
        correctIndices: [0],
        explanation: 'df -h visar ledigt diskutrymme i human-readable format.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q6',
        question: 'Vilken flagga till rm krävs för att radera en katalog som innehåller filer?',
        options: ['-r', '-f', '-d', '-all'],
        correctIndices: [0],
        explanation: 'rm -r raderar katalogen rekursivt med allt innehåll.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q7',
        question: 'Vad är skillnaden mellan en "Hard Link" och en "Symbolic Link"?',
        options: ['Symbolic links fungerar över olika partitioner, det gör inte hard links.', 'Hard links kan peka på kataloger, det kan inte symbolic links.', 'Symbolic links är snabbare att läsa än hard links.', 'Hard links tar mer plats på disken än symbolic links.'],
        correctIndices: [0],
        explanation: 'Hard links pekar på samma inode och fungerar bara inom samma partition.',
        difficulty: 'VG',
        category: 'Länkar',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q8',
        question: 'Vilket kommando skapar en symbolisk länk från data.txt till link.txt?',
        options: ['ln -s data.txt link.txt', 'ln data.txt link.txt', 'cp -s data.txt link.txt', 'link -soft data.txt link.txt'],
        correctIndices: [0],
        explanation: 'ln -s skapar en symbolisk länk.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q9',
        question: 'Du vill gå direkt till din hemkatalog. Vilket kommando fungerar INTE?',
        options: ['cd /root', 'cd', 'cd ~', 'cd $HOME'],
        correctIndices: [0],
        explanation: '/root är root-användarens hem, inte din egen hemkatalog.',
        difficulty: 'G',
        category: 'Navigation',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q10',
        question: 'Vad visar kommandot pwd?',
        options: ['Sökvägen till katalogen du står i (Print Working Directory).', 'Ditt nuvarande lösenord (Print Working Data).', 'Namnet på din användare (Print Working Developer).', 'Prestandastatus för hårddisken (Performance Working Disk).'],
        correctIndices: [0],
        explanation: 'pwd = Print Working Directory, visar nuvarande arbetskatalog.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q11',
        question: 'Vilken fil används för att definiera vilka diskar som ska monteras automatiskt?',
        options: ['/etc/fstab', '/etc/mtab', '/boot/mounts', '/etc/disks'],
        correctIndices: [0],
        explanation: '/etc/fstab konfigurerar automatisk montering av filsystem.',
        difficulty: 'G',
        category: 'Konfiguration',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q12',
        question: 'Vad är en "Mount Point" i Linux?',
        options: ['En katalog där ett filsystem görs tillgängligt.', 'En fysisk kontakt på moderkortet.', 'En typ av hårddiskpartition.', 'En säkerhetsnyckel för kryptering.'],
        correctIndices: [0],
        explanation: 'Mount point är katalogen där ett filsystem kopplas in.',
        difficulty: 'G',
        category: 'Filsystem',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q13',
        question: 'Vilket kommando visar innehållet i en stor textfil sida för sida?',
        options: ['less filen.txt', 'echo filen.txt', 'grep filen.txt', 'cat filen.txt'],
        correctIndices: [0],
        explanation: 'less visar filen sida för sida med scroll-möjlighet.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q14',
        question: 'Vad betyder . (punkt) i början av ett filnamn (t.ex. .bashrc)?',
        options: ['Att filen är "dold" och inte visas av standard ls.', 'Att filen är en systemfil och inte får raderas.', 'Att filen är skadad.', 'Att filen är en körbar binärfil.'],
        correctIndices: [0],
        explanation: 'Filer som börjar med punkt är dolda i Linux.',
        difficulty: 'G',
        category: 'Filer',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q15',
        question: 'Vilket tecken används för att separera kataloger i en sökväg i Linux?',
        options: ['Forward slash /', 'Backslash \\', 'Kolon :', 'Pipe |'],
        correctIndices: [0],
        explanation: 'Linux använder forward slash (/) som sökvägsavgränsare.',
        difficulty: 'G',
        category: 'Grundläggande',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q16',
        question: 'Vad gör kommandot touch minfil.txt om filen redan finns?',
        options: ['Det uppdaterar filens tidsstämpel (modifierad tid).', 'Det raderar filens innehåll.', 'Det skapar en kopia som heter minfil.txt.bak.', 'Det ger ett felmeddelande och avslutas.'],
        correctIndices: [0],
        explanation: 'touch uppdaterar tidsstämpeln på existerande filer.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q17',
        question: 'Vilken katalog innehåller information om körande processer?',
        options: ['/proc', '/sys/active', '/var/run', '/dev/procs'],
        correctIndices: [0],
        explanation: '/proc är ett virtuellt filsystem med process- och systeminformation.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q18',
        question: 'Du vill kopiera en fil och samtidigt byta namn på kopian. Vilket kommando?',
        options: ['Både A och C fungerar tekniskt sett.', 'cp fil.txt nyfil.txt', 'mv fil.txt nyfil.txt', 'cat fil.txt > nyfil.txt'],
        correctIndices: [0],
        explanation: 'Både cp och cat > kan skapa en kopia med nytt namn.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q19',
        question: 'Vad är /dev/null?',
        options: ['En enhet som kastar all data som skrivs till den.', 'En fil som innehåller nollor.', 'Root-användarens papperskorg.', 'En loggfil för systemfel.'],
        correctIndices: [0],
        explanation: '/dev/null är ett "svart hål" - all data som skrivs dit försvinner.',
        difficulty: 'G',
        category: 'Enheter',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q20',
        question: 'Vilket kommando listar filer med detaljerad information (rättigheter, storlek, ägare)?',
        options: ['ls -l', 'ls -a', 'ls -d', 'ls -x'],
        correctIndices: [0],
        explanation: 'ls -l visar en detaljerad lista med metadata.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q21',
        question: 'Vad är en "absolut sökväg"?',
        options: ['En sökväg som börjar från roten /.', 'En sökväg som börjar från nuvarande katalog.', 'En sökväg som innehåller specialtecken.', 'En sökväg som bara root kan komma åt.'],
        correctIndices: [0],
        explanation: 'Absolut sökväg börjar alltid från rotkatalogen (/).',
        difficulty: 'G',
        category: 'Navigation',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q22',
        question: 'I vilken ordning skapar du en krypterad volym korrekt?',
        options: ['Partition -> LUKS -> Filsystem.', 'Filsystem -> LUKS -> Partition.', 'LUKS -> Partition -> Filsystem.', 'Partition -> Filsystem -> Montering.'],
        correctIndices: [0],
        explanation: 'Först partition, sedan LUKS-kryptering, sedan filsystem.',
        difficulty: 'VG',
        category: 'Kryptering',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q23',
        question: 'Vilken katalog är avsedd för "variable data" som loggar och spool-filer?',
        options: ['/var', '/etc', '/lib', '/opt'],
        correctIndices: [0],
        explanation: '/var står för variable och innehåller data som ändras under drift.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q24',
        question: 'Vad händer om du flyttar (mv) en fil från en partition till en annan?',
        options: ['Linux kopierar datan och tar sedan bort originalet (långsammare).', 'Linux uppdaterar bara inoden (snabbt).', 'Det går inte att flytta filer mellan partitioner.', 'Filen konverteras till en symbolisk länk.'],
        correctIndices: [0],
        explanation: 'Mellan partitioner måste data kopieras fysiskt.',
        difficulty: 'VG',
        category: 'Filsystem',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q25',
        question: 'Vad är ext4?',
        options: ['Det vanligaste filsystemet för Linux-partitioner.', 'Ett protokoll för nätverksöverföring.', 'En typ av kryptering.', 'Ett program för att packa upp zip-filer.'],
        correctIndices: [0],
        explanation: 'ext4 är det vanligaste Linux-filsystemet.',
        difficulty: 'G',
        category: 'Filsystem',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q26',
        question: 'Vilket kommando visar de sista raderna i en fil?',
        options: ['tail', 'head', 'bottom', 'end'],
        correctIndices: [0],
        explanation: 'tail visar de sista raderna (default 10).',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q27',
        question: 'Du har råkat ta bort en fil med rm. Hur återställer du den enklast?',
        options: ['Normalt sett går det inte att ångra rm i terminalen.', 'Går till papperskorgen i /home/.trash.', 'Kör rm -undo.', 'Startar om datorn.'],
        correctIndices: [0],
        explanation: 'rm raderar permanent - det finns ingen papperskorg i CLI.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q28',
        question: 'Vilken katalog innehåller vanligen hemkataloger för "vanliga" användare?',
        options: ['/home', '/usr/users', '/root', '/users'],
        correctIndices: [0],
        explanation: '/home innehåller hemkataloger för vanliga användare.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q29',
        question: 'Vad innebär .. i kommandot cd ..?',
        options: ['Föräldrakatalogen (en nivå upp).', 'Hemkatalogen.', 'Rotkatalogen.', 'Senaste katalogen.'],
        correctIndices: [0],
        explanation: '.. refererar alltid till föräldrakatalogen.',
        difficulty: 'G',
        category: 'Navigation',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q30',
        question: 'Vilket kommando skapar en hel katalogstruktur på en gång (t.ex. år/månad/dag)?',
        options: ['mkdir -p år/månad/dag', 'mkdir -r år/månad/dag', 'mkdir -all år/månad/dag', 'create dir år/månad/dag'],
        correctIndices: [0],
        explanation: 'mkdir -p skapar hela sökvägen inklusive föräldrakataloger.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    // Fler Nod1 quiz-frågor...
    {
        id: 'nod1-q31',
        question: 'Vad är syftet med /opt?',
        options: ['"Optional" mjukvara, ofta stora tredjepartspaket.', '"Options" för systemkonfiguration.', '"Operators" hemkataloger.', '"Optimal" systemprestanda-filer.'],
        correctIndices: [0],
        explanation: '/opt används för manuellt installerad tredjepartsmjukvara.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q32',
        question: 'Vilken fil används för namnupplösning (hosts) innan DNS tillfrågas?',
        options: ['/etc/hosts', '/etc/dns', '/etc/resolv.conf', '/etc/networks'],
        correctIndices: [0],
        explanation: '/etc/hosts kollas före DNS för namnupplösning.',
        difficulty: 'G',
        category: 'Konfiguration',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q33',
        question: 'Vad betyder det om en katalog har behörigheten r-x för en användare?',
        options: ['Användaren får läsa (ls) och gå in i (cd) katalogen.', 'Användaren får bara läsa, men inte gå in i katalogen.', 'Användaren får skapa filer i katalogen.', 'Behörigheten är ogiltig för kataloger.'],
        correctIndices: [0],
        explanation: 'r = läsa innehåll, x = kunna gå in (cd).',
        difficulty: 'VG',
        category: 'Rättigheter',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q34',
        question: 'Vilket kommando kan visa hur mycket minne (RAM) som används?',
        options: ['free -h', 'df -h', 'du -h', 'mem -show'],
        correctIndices: [0],
        explanation: 'free visar RAM-användning, -h för human readable.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q35',
        question: 'Vad händer om du skriver cd utan argument och trycker enter?',
        options: ['Du flyttas till din hemkatalog.', 'Du får ett felmeddelande.', 'Du stannar kvar i samma katalog.', 'Du flyttas till rotkatalogen.'],
        correctIndices: [0],
        explanation: 'cd utan argument tar dig till din hemkatalog.',
        difficulty: 'G',
        category: 'Navigation',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q36',
        question: 'Vilken katalog brukar innehålla delade biblioteksfiler (.so) för program?',
        options: ['/lib eller /usr/lib', '/bin', '/dll', '/src'],
        correctIndices: [0],
        explanation: '/lib och /usr/lib innehåller delade bibliotek.',
        difficulty: 'G',
        category: 'FHS',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q37',
        question: 'Hur ser du vilka partitioner som är monterade just nu?',
        options: ['cat /proc/mounts eller mount', 'cat /etc/fstab', 'ls -l /dev/disk', 'show mounts'],
        correctIndices: [0],
        explanation: 'mount eller /proc/mounts visar aktiva mounts.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q38',
        question: 'Vad är skillnaden på cat och tac?',
        options: ['tac skriver ut filen baklänges (sista raden först).', 'Det är samma kommando.', 'cat är för text, tac är för binärer.', 'tac är en textredigerare.'],
        correctIndices: [0],
        explanation: 'tac = cat baklänges, skriver ut filen i omvänd ordning.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q39',
        question: 'Vilket kommando används för att hitta var en binär (t.ex. python) ligger?',
        options: ['which python', 'find python', 'search python', 'map python'],
        correctIndices: [0],
        explanation: 'which visar sökvägen till en binär i PATH.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    {
        id: 'nod1-q40',
        question: 'Vad är en "Device Node" (t.ex. /dev/sda)?',
        options: ['En fysisk hårdvara som ser ut som en fil för systemet.', 'En mapp med drivrutiner.', 'En konfigurationsfil för skärmen.', 'En nätverkskoppling.'],
        correctIndices: [0],
        explanation: 'Device nodes representerar hårdvara som filer.',
        difficulty: 'G',
        category: 'Enheter',
        topic: 'nod1-filsystem',
        type: 'quiz'
    },
    // Scenarios för Nod 1
    {
        id: 'nod1-s1',
        question: 'SCENARIO: Du försöker spara en fil men får felmeddelandet "No space left on device". Du kör df -h och ser att disken bara är 50% full. Vad kan felet vara?',
        options: ['Du har slut på Inodes (många små filer har ätit upp alla index-noder).', 'Disken är trasig.', 'RAM-minnet är fullt.', 'Du har inte root-rättigheter.'],
        correctIndices: [0],
        explanation: 'Inode-brist kan uppstå vid många små filer även om diskutrymme finns.',
        difficulty: 'VG',
        category: 'Felsökning',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s2',
        question: 'SCENARIO: Du har precis laddat ner en .zip-fil till din server (SSH). Du vet inte var den hamnade. Du står i /. Hur hittar du den om den laddades till hemkatalogen?',
        options: ['Kör cd ~ för att gå hem och ls för att leta.', 'cd / sedan cat.', 'find / -name zip.', 'pwd visar filerna.'],
        correctIndices: [0],
        explanation: 'cd ~ tar dig till hemkatalogen där downloads ofta hamnar.',
        difficulty: 'G',
        category: 'Navigation',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s3',
        question: 'SCENARIO: En applikation kraschar och utvecklaren ber dig skicka "loggarna". Du vet inte exakt var appen lägger sina loggar. Var letar du först?',
        options: ['I /var/log.', '/etc/logs.', '/home/app/log.', '/bin/logs.'],
        correctIndices: [0],
        explanation: '/var/log är standardplatsen för loggar i Linux.',
        difficulty: 'G',
        category: 'Loggar',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s4',
        question: 'SCENARIO: Du ska installera en ny disk. Du har kopplat in den fysiskt. Vad är det första logiska steget?',
        options: ['Skapa en partition (med fdisk/parted).', 'Formatera med mkfs.', 'Montera den.', 'Redigera fstab.'],
        correctIndices: [0],
        explanation: 'Först skapar man partition, sedan formaterar, sedan monterar.',
        difficulty: 'G',
        category: 'Diskhantering',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s5',
        question: 'SCENARIO: Du har skapat en partition och formaterat den med ext4. Du försöker cd in men hittar den inte. Vad har du glömt?',
        options: ['Att montera (mount) partitionen mot en katalog.', 'Att starta om datorn.', 'Att köra touch.', 'Att ge root-rättigheter.'],
        correctIndices: [0],
        explanation: 'Partitioner måste monteras för att vara åtkomliga.',
        difficulty: 'G',
        category: 'Montering',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s6',
        question: 'SCENARIO: Du redigerar /etc/fstab för att montera en disk automatiskt, men skriver fel. Vad händer nästa gång du startar om servern?',
        options: ['Servern kan misslyckas med att boota eller hamna i "emergency mode".', 'Ingenting, Linux ignorerar fel.', 'Disken raderas.', 'Den loggar in som root automatiskt.'],
        correctIndices: [0],
        explanation: 'Fel i fstab kan förhindra systemet från att starta normalt.',
        difficulty: 'VG',
        category: 'Boot',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s7',
        question: 'SCENARIO: Du ska flytta en hel katalogstruktur projekt/ från din hemkatalog till /var/www/html/. Vilket kommando är säkrast/bäst?',
        options: ['mv ~/projekt /var/www/html/ (eller sudo mv...)', 'cp projekt /var/www/html', 'rm -r projekt', 'cat projekt > /var/www/html'],
        correctIndices: [0],
        explanation: 'mv flyttar hela strukturen på ett kommando.',
        difficulty: 'G',
        category: 'Flytta filer',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s8',
        question: 'SCENARIO: Du kör ett skript och får felet "Permission denied" när skriptet försöker skriva till /etc/myconfig.conf. Varför?',
        options: ['Vanliga användare har inte skrivrättigheter till /etc.', 'Filen är låst.', 'Disken är full.', 'Skriptet är felkodat.'],
        correctIndices: [0],
        explanation: '/etc kräver root-rättigheter för skrivning.',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s9',
        question: 'SCENARIO: Du vill se vad din kollega "lisa" har i sin hemkatalog. Du kör ls /home/lisa men får "Permission denied". Vad innebär detta?',
        options: ['Du saknar läs/exekveringsrättigheter på hennes katalog.', 'Hennes katalog finns inte.', 'Hon är inloggad så den är låst.', 'Det är en dold katalog.'],
        correctIndices: [0],
        explanation: 'Katalogen har rättigheter som hindrar dig att se innehållet.',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod1-filsystem',
        type: 'scenario'
    },
    {
        id: 'nod1-s10',
        question: 'SCENARIO: Du ser en fil server_key.pem. Du vill veta om det är en "riktig" fil eller bara en länk. Hur kollar du enklast?',
        options: ['ls -l och tittar efter -> eller l i början av raden.', 'cat server_key.pem.', 'open server_key.pem.', 'whois server_key.pem.'],
        correctIndices: [0],
        explanation: 'ls -l visar filtyp och länkar markeras med -> och l i början.',
        difficulty: 'G',
        category: 'Filer',
        topic: 'nod1-filsystem',
        type: 'scenario'
    }
]

// ===== NOD 2: RÄTTIGHETER & SÄKERHET =====
export const NOD2_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod2-q1',
        question: 'Vilket numeriskt värde motsvarar rättigheterna rwxr-xr--?',
        options: ['754', '751', '764', '755'],
        correctIndices: [0],
        explanation: 'rwx=7, r-x=5, r--=4, alltså 754.',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q2',
        question: 'Vad är syftet med filen /etc/shadow?',
        options: ['Att lagra krypterade lösenord säkert.', 'Att lagra användarnamn.', 'Att lagra nätverkskonfiguration.', 'Att skugga hårddisken för backup.'],
        correctIndices: [0],
        explanation: '/etc/shadow innehåller hashade lösenord med begränsad läsåtkomst.',
        difficulty: 'G',
        category: 'Systemfiler',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q3',
        question: 'Vilket kommando ger gruppen (group) skrivrättigheter på filen data.txt?',
        options: ['chmod g+w data.txt', 'chmod +w data.txt', 'chown g=w data.txt', 'groupadd write data.txt'],
        correctIndices: [0],
        explanation: 'chmod g+w lägger till write för gruppen.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q4',
        question: 'Du vill köra ett kommando som root men är inloggad som vanlig användare. Vad skriver du först?',
        options: ['sudo', 'admin', 'please', 'root'],
        correctIndices: [0],
        explanation: 'sudo kör kommandot med förhöjda rättigheter.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q5',
        question: 'Vilken rättighet krävs för att kunna köra ett skript (./script.sh)?',
        options: ['Execute (x)', 'Read (r)', 'Write (w)', 'Admin (a)'],
        correctIndices: [0],
        explanation: 'Execute-rättighet krävs för att köra filer.',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q6',
        question: 'Vad gör kommandot chown root:root fil.txt?',
        options: ['Ändrar ägare och grupp till root.', 'Ger root alla rättigheter.', 'Flyttar filen till root-katalogen.', 'Raderar filen.'],
        correctIndices: [0],
        explanation: 'chown user:group ändrar både ägare och grupp.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q7',
        question: 'Vem får läsa filen om rättigheterna är -rw-------?',
        options: ['Bara ägaren.', 'Alla.', 'Ägaren och gruppen.', 'Ingen.'],
        correctIndices: [0],
        explanation: 'rw------- ger bara ägaren läs- och skrivrättigheter.',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q8',
        question: 'Vad är en "Sticky Bit"?',
        options: ['En rättighet som gör att bara ägaren får radera sin fil i en delad mapp.', 'En bit tape på servern.', 'En virus-typ.', 'En inställning för att göra datorn långsammare.'],
        correctIndices: [0],
        explanation: 'Sticky bit förhindrar andra från att radera filer de inte äger.',
        difficulty: 'VG',
        category: 'Specialrättigheter',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q9',
        question: 'Vilket kommando visar vem du är inloggad som just nu?',
        options: ['whoami', 'me', 'ls user', 'checkuser'],
        correctIndices: [0],
        explanation: 'whoami visar användarnamnet du är inloggad som.',
        difficulty: 'G',
        category: 'Kommandon',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q10',
        question: 'Varför anses det säkrare att använda SSH-nycklar än lösenord?',
        options: ['Nycklar är immuna mot Brute Force-attacker (i praktiken).', 'Nycklar är kortare.', 'Lösenord skickas i klartext.', 'Det är ingen skillnad.'],
        correctIndices: [0],
        explanation: 'SSH-nycklar är kryptografiskt starka och kan inte gissas.',
        difficulty: 'G',
        category: 'SSH',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q11',
        question: 'Vilken katalog måste ha rättigheterna 700 (rwx------) för att SSH ska fungera korrekt?',
        options: ['~/.ssh', '/etc/ssh', '/var/www', '/home'],
        correctIndices: [0],
        explanation: '~/.ssh måste vara 700 för säkerhetens skull.',
        difficulty: 'G',
        category: 'SSH',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q12',
        question: 'Vad gör usermod -aG sudo kalle?',
        options: ['Lägger till kalle i gruppen sudo utan att ta bort andra grupper.', 'Gör kalle till root.', 'Raderar kalle från sudo-gruppen.', 'Byter namn på sudo-gruppen till kalle.'],
        correctIndices: [0],
        explanation: '-aG lägger till användaren i gruppen utan att påverka andra grupper.',
        difficulty: 'G',
        category: 'Användarhantering',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q13',
        question: 'Vilken fil redigerar du för att ändra SSH-porten?',
        options: ['/etc/ssh/sshd_config', '/etc/ssh_config', '/etc/ssh/sshd_settings', '~/.ssh/config'],
        correctIndices: [0],
        explanation: 'sshd_config är serverns konfigurationsfil.',
        difficulty: 'G',
        category: 'SSH',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q14',
        question: 'Vad betyder UFW?',
        options: ['Uncomplicated Firewall.', 'Ubuntu File Writer.', 'Universal Fire Wall.', 'User Fire Wall.'],
        correctIndices: [0],
        explanation: 'UFW = Uncomplicated Firewall, en enkel brandvägg för Ubuntu/Debian.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q15',
        question: 'Om du glömt root-lösenordet, hur kan du återställa det (om du har fysisk tillgång)?',
        options: ['Boota i "Single User Mode" (eller recovery mode) och kör passwd.', 'Du kan inte, installera om.', 'Gissa dig fram.', 'Hacka BIOS.'],
        correctIndices: [0],
        explanation: 'Recovery mode ger root-access för lösenordsåterställning.',
        difficulty: 'VG',
        category: 'Återställning',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q16',
        question: 'Vad är id_rsa.pub?',
        options: ['Din publika nyckel.', 'Din privata nyckel.', 'En konfigurationsfil.', 'En loggfil.'],
        correctIndices: [0],
        explanation: '.pub-filen innehåller den publika nyckeln.',
        difficulty: 'G',
        category: 'SSH',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q17',
        question: 'Vilket kommando låser upp ett konto?',
        options: ['usermod -U', 'passwd -unlock', 'open user', 'account --enable'],
        correctIndices: [0],
        explanation: 'usermod -U (eller passwd -u) låser upp kontot.',
        difficulty: 'G',
        category: 'Användarhantering',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q18',
        question: 'Vad innebär rättigheten drwxr-xr-x?',
        options: ['Det är en katalog (d).', 'Det är en fil.', 'Det är en länk.', 'Det är en enhet.'],
        correctIndices: [0],
        explanation: 'd i början indikerar att det är en katalog (directory).',
        difficulty: 'G',
        category: 'Rättigheter',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q19',
        question: 'Vem kan använda sudo?',
        options: ['Bara användare som finns i filen /etc/sudoers (eller sudo-gruppen).', 'Alla användare.', 'Endast användaren med ID 1000.', 'Ingen.'],
        correctIndices: [0],
        explanation: 'sudo-rättigheter konfigureras i /etc/sudoers.',
        difficulty: 'G',
        category: 'Sudo',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    {
        id: 'nod2-q20',
        question: 'Vilket kommando tar bort en grupp?',
        options: ['delgroup eller groupdel', 'rmgroup', 'ungroup', 'groupremove'],
        correctIndices: [0],
        explanation: 'groupdel eller delgroup tar bort en grupp.',
        difficulty: 'G',
        category: 'Användarhantering',
        topic: 'nod2-rattigheter',
        type: 'quiz'
    },
    // Scenarios för Nod 2
    {
        id: 'nod2-s1',
        question: 'SCENARIO: Du ska redigera en webbsida i /var/www/html men får "Permission denied". Du är inte owner. Hur löser du det snyggast?',
        options: ['Lägg till i gruppen och sätt g+w.', 'Kör chmod 777.', 'Bli root för alltid.', 'Flytta mappen till /tmp.'],
        correctIndices: [0],
        explanation: 'Gruppmedlemskap med grupprättigheter är säkrare än 777.',
        difficulty: 'VG',
        category: 'Felsökning',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s2',
        question: 'SCENARIO: Du kör ls -l och ser rwsr-xr-x på /usr/bin/passwd. Varför finns där ett "s"?',
        options: ['Det är SUID (körs som ägaren).', 'Det betyder "Secure".', 'Filen är skadad.', 'Det är en länk.'],
        correctIndices: [0],
        explanation: 'SUID-biten gör att programmet körs med ägarens rättigheter.',
        difficulty: 'VG',
        category: 'Specialrättigheter',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s3',
        question: 'SCENARIO: Du försöker SSH:a till en server men får "Permission denied (publickey)". Du vet att du har rätt nyckel. Vad är troligtvis fel?',
        options: ['Fel rättigheter på ~/.ssh-mappen.', 'Servern är nere.', 'Internet är trasigt.', 'Du måste starta om.'],
        correctIndices: [0],
        explanation: 'SSH kräver korrekta rättigheter på .ssh-katalogen och nyckelfiler.',
        difficulty: 'VG',
        category: 'SSH-felsökning',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s4',
        question: 'SCENARIO: Du vill att alla nya filer i /data automatiskt ska ägas av gruppen developers. Hur?',
        options: ['chmod g+s /data (Set Group ID).', 'Använd cronjob.', 'chown -R.', 'Det går inte.'],
        correctIndices: [0],
        explanation: 'SGID på katalogen gör att nya filer ärver gruppägare.',
        difficulty: 'VG',
        category: 'Specialrättigheter',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s5',
        question: 'SCENARIO: UFW blockerar din webbtrafik på port 80 trots att du kört "ufw allow 80". Vad kan vara fel?',
        options: ['ufw enable saknas.', 'Brandväggen är trasig.', 'Du måste starta om.', 'Port 80 finns inte.'],
        correctIndices: [0],
        explanation: 'UFW måste vara aktiverad med "ufw enable" för att regler ska gälla.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    }
]

// Re-exportera NOD3-10 med enkla namn för bakåtkompatibilitet
export const NOD3_QUESTIONS: Omtenta2Question[] = NOD3_PROCESSHANTERING_QUESTIONS as Omtenta2Question[]
export const NOD4_QUESTIONS: Omtenta2Question[] = NOD4_NATVERK_QUESTIONS as Omtenta2Question[]
export const NOD5_QUESTIONS: Omtenta2Question[] = NOD5_SSH_QUESTIONS as Omtenta2Question[]
export const NOD6_QUESTIONS: Omtenta2Question[] = NOD6_BASH_SKRIPT_QUESTIONS as Omtenta2Question[]
export const NOD7_QUESTIONS: Omtenta2Question[] = NOD7_BASH_VERKTYG_QUESTIONS as Omtenta2Question[]
export const NOD8_QUESTIONS: Omtenta2Question[] = NOD8_DOCKER_ISOLERING_QUESTIONS as Omtenta2Question[]
export const NOD9_QUESTIONS: Omtenta2Question[] = NOD9_DOCKER_NATVERK_QUESTIONS as Omtenta2Question[]
export const NOD10_QUESTIONS: Omtenta2Question[] = NOD10_DOCKER_COMPOSE_QUESTIONS as Omtenta2Question[]

// ===== AGGREGERAD EXPORT =====
export const ALL_OMTENTA_2_QUESTIONS: Omtenta2Question[] = [
    ...NOD1_QUESTIONS,
    ...NOD2_QUESTIONS,
    ...NOD3_QUESTIONS,
    ...NOD4_QUESTIONS,
    ...NOD5_QUESTIONS,
    ...NOD6_QUESTIONS,
    ...NOD7_QUESTIONS,
    ...NOD8_QUESTIONS,
    ...NOD9_QUESTIONS,
    ...NOD10_QUESTIONS
]

export const OMTENTA2_TOPICS: Omtenta2Topic[] = [
    'nod1-filsystem',
    'nod2-rattigheter',
    'nod3-processhantering',
    'nod4-natverk',
    'nod5-ssh',
    'nod6-bash-skript',
    'nod7-bash-verktyg',
    'nod8-docker-isolering',
    'nod9-docker-natverk',
    'nod10-docker-compose'
]

// ===== HJÄLPFUNKTIONER =====
export function shuffleArray<T>(array: T[]): T[] {
    const shuffled = [...array]
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
            ;[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
    }
    return shuffled
}

export function getQuestionsByTopics(topics: Omtenta2Topic[]): Omtenta2Question[] {
    if (topics.length === 0) return ALL_OMTENTA_2_QUESTIONS
    return ALL_OMTENTA_2_QUESTIONS.filter(q => topics.includes(q.topic))
}

export function getQuizQuestions(count: number, topics?: Omtenta2Topic[]): Omtenta2Question[] {
    const pool = topics && topics.length > 0
        ? getQuestionsByTopics(topics)
        : ALL_OMTENTA_2_QUESTIONS

    const shuffled = shuffleArray(pool)
    return shuffled.slice(0, Math.min(count, shuffled.length))
}

export function getQuestionsByType(type: 'quiz' | 'scenario', topics?: Omtenta2Topic[]): Omtenta2Question[] {
    let pool = topics && topics.length > 0
        ? getQuestionsByTopics(topics)
        : ALL_OMTENTA_2_QUESTIONS

    return pool.filter(q => q.type === type)
}
