/**
 * TENTAISH EXPANSION - 200 NYA QUIZ-FRÅGOR
 * Moment 1: Filsystem & Användarhantering
 * 
 * Skapad: 2026-01-06
 */

import { TentaishQuestion } from './tentaish-quiz'

// =============================================================================
// MOMENT 1A: FILSYSTEM - NYA FRÅGOR (30 st)
// =============================================================================

export const FILSYSTEM_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-fs-ex-1',
        question: 'Vad gör kommandot "find /home -name "*.log" -mtime +7"?',
        options: [
            'Hittar alla loggfiler i /home',
            'Hittar loggfiler äldre än 7 dagar i /home',
            'Tar bort loggfiler äldre än 7 dagar',
            'Skapar nya loggfiler'
        ],
        correctIndex: 1,
        explanation: '-mtime +7 betyder filer modifierade för mer än 7 dagar sedan. find söker rekursivt.',
        difficulty: 'G',
        category: 'Sökning'
    },
    {
        id: 'tent-fs-ex-2',
        question: 'Vad är syftet med /tmp-katalogen?',
        options: [
            'Permanent lagring av användarfiler',
            'Temporära filer som kan raderas vid omstart',
            'Systemkonfiguration',
            'Användarhemkataloger'
        ],
        correctIndex: 1,
        explanation: '/tmp är för temporära filer. Innehållet kan rensas automatiskt vid omstart.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'tent-fs-ex-3',
        question: 'Hur visar du de 20 sista raderna i en fil kontinuerligt?',
        options: ['head -20 fil', 'tail -f -n 20 fil', 'cat -20 fil', 'less -20 fil'],
        correctIndex: 1,
        explanation: 'tail -f följer filen i realtid (-f = follow), -n 20 visar 20 rader.',
        difficulty: 'G',
        category: 'Filvisning'
    },
    {
        id: 'tent-fs-ex-4',
        question: 'Vad gör "grep -r "error" /var/log"?',
        options: [
            'Söker efter "error" endast i /var/log',
            'Söker rekursivt efter "error" i alla filer under /var/log',
            'Tar bort rader med "error"',
            'Räknar förekomster av "error"'
        ],
        correctIndex: 1,
        explanation: '-r (recursive) söker i alla filer och undermappar. Mycket användbart för loggsökning.',
        difficulty: 'G',
        category: 'Sökning'
    },
    {
        id: 'tent-fs-ex-5',
        question: 'Vad är skillnaden mellan hard link och symbolic link?',
        options: [
            'Ingen skillnad',
            'Hard link pekar på samma inode, symlink är en pekare till filnamnet',
            'Symlink är snabbare',
            'Hard link fungerar över filsystem'
        ],
        correctIndex: 1,
        explanation: 'Hard link delar inode (fungerar bara inom samma filsystem). Symlink är en pekare som kan gå över filsystem.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'tent-fs-ex-6',
        question: 'Hur skapar du en symbolisk länk?',
        options: ['ln source target', 'ln -s source target', 'link source target', 'symlink source target'],
        correctIndex: 1,
        explanation: 'ln -s (symbolic) skapar en mjuk länk. Utan -s skapas en hard link.',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-ex-7',
        question: 'Vad visar "df -h"?',
        options: [
            'Minnesanvändning',
            'Diskutrymme per monterat filsystem i läsbart format',
            'Filstorlekar',
            'Processlista'
        ],
        correctIndex: 1,
        explanation: 'df (disk free) visar ledigt utrymme. -h (human-readable) ger MB/GB istället för bytes.',
        difficulty: 'G',
        category: 'Diskhantering'
    },
    {
        id: 'tent-fs-ex-8',
        question: 'Vad gör "du -sh /home/user"?',
        options: [
            'Visar diskutrymme för hela systemet',
            'Visar total storlek på katalogen i läsbart format',
            'Tar bort katalogen',
            'Kopierar katalogen'
        ],
        correctIndex: 1,
        explanation: 'du (disk usage) -s (summary) -h (human-readable) visar total storlek på en katalog.',
        difficulty: 'G',
        category: 'Diskhantering'
    },
    {
        id: 'tent-fs-ex-9',
        question: 'Var finns körbara systemprogram i Linux?',
        options: ['/bin och /usr/bin', '/home/bin', '/etc/bin', '/var/bin'],
        correctIndex: 0,
        explanation: '/bin innehåller essentiella kommandon, /usr/bin innehåller användarprogram.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'tent-fs-ex-10',
        question: 'Vad gör "wc -l fil.txt"?',
        options: [
            'Räknar ord i filen',
            'Räknar antal rader i filen',
            'Räknar tecken i filen',
            'Visar filstorlek'
        ],
        correctIndex: 1,
        explanation: 'wc (word count) -l räknar rader. -w räknar ord, -c räknar bytes.',
        difficulty: 'G',
        category: 'Filvisning'
    },
    {
        id: 'tent-fs-ex-11',
        question: 'Vad gör pipe-operatorn "|"?',
        options: [
            'Skriver till fil',
            'Skickar output från ett kommando som input till nästa',
            'Kör kommandon parallellt',
            'Kommenterar ut kod'
        ],
        correctIndex: 1,
        explanation: 'Pipe (|) kedjar kommandon. T.ex. cat fil | grep "text" | wc -l',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 'tent-fs-ex-12',
        question: 'Vad gör ">" och ">>" för skillnad?',
        options: [
            'Ingen skillnad',
            '> skriver över filen, >> lägger till i slutet',
            '> lägger till, >> skriver över',
            '>> är snabbare'
        ],
        correctIndex: 1,
        explanation: '> redirect och skriver över. >> append och lägger till utan att radera.',
        difficulty: 'G',
        category: 'Grundläggande'
    },
    {
        id: 'tent-fs-ex-13',
        question: 'Vad betyder "2>&1" i bash?',
        options: [
            'Kör kommando 2 gånger',
            'Omdirigerar stderr (2) till samma som stdout (1)',
            'Startar 2 processer',
            'Väntar 2 sekunder'
        ],
        correctIndex: 1,
        explanation: 'File descriptor 1 = stdout, 2 = stderr. 2>&1 skickar båda till samma destination.',
        difficulty: 'VG',
        category: 'Redirect'
    },
    {
        id: 'tent-fs-ex-14',
        question: 'Hur hittar du var ett kommando finns?',
        options: ['find command', 'which command', 'locate command', 'search command'],
        correctIndex: 1,
        explanation: 'which visar sökvägen till ett körbart kommando. T.ex. which python -> /usr/bin/python',
        difficulty: 'G',
        category: 'Sökning'
    },
    {
        id: 'tent-fs-ex-15',
        question: 'Vad gör "cat fil1 fil2 > kombinerad.txt"?',
        options: [
            'Kopierar fil1 till fil2',
            'Konkatenerar fil1 och fil2 till en ny fil',
            'Jämför filerna',
            'Tar bort filerna'
        ],
        correctIndex: 1,
        explanation: 'cat (concatenate) slår ihop filer. Med > skrivs resultatet till en ny fil.',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-ex-16',
        question: 'Vad gör kommandot "tee"?',
        options: [
            'Pausar output',
            'Läser input och skriver till både stdout och fil samtidigt',
            'Krypterar data',
            'Komprimerar filer'
        ],
        correctIndex: 1,
        explanation: 'tee delar output: "command | tee output.txt" visar på skärmen OCH sparar till fil.',
        difficulty: 'VG',
        category: 'Redirect'
    },
    {
        id: 'tent-fs-ex-17',
        question: 'Vad är /dev/null?',
        options: [
            'En tom enhet',
            'En "black hole" som slänger all data som skickas dit',
            'Systemloggar',
            'Nätverksenheter'
        ],
        correctIndex: 1,
        explanation: '/dev/null är en special device som kasserar all data. Används för att tysta output.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'tent-fs-ex-18',
        question: 'Hur kör du ett kommando i bakgrunden?',
        options: [
            'Lägg till & i slutet',
            'Lägg till bg före kommandot',
            'Använd sudo',
            'Lägg till -b flaggan'
        ],
        correctIndex: 0,
        explanation: '& i slutet startar processen i bakgrunden. T.ex. "sleep 100 &"',
        difficulty: 'G',
        category: 'Processer'
    },
    {
        id: 'tent-fs-ex-19',
        question: 'Vad gör Ctrl+Z i terminalen?',
        options: [
            'Avslutar processen',
            'Pausar processen och lägger den i bakgrunden (suspended)',
            'Kopierar text',
            'Ångrar senaste kommando'
        ],
        correctIndex: 1,
        explanation: 'Ctrl+Z suspenderar processen. Använd "fg" för att återuppta eller "bg" för bakgrund.',
        difficulty: 'G',
        category: 'Processer'
    },
    {
        id: 'tent-fs-ex-20',
        question: 'Vad gör "sort -u fil.txt"?',
        options: [
            'Sorterar och visar endast unika rader',
            'Sorterar i omvänd ordning',
            'Sorterar numeriskt',
            'Sorterar efter filstorlek'
        ],
        correctIndex: 0,
        explanation: 'sort -u (unique) sorterar och tar bort dubbletter. Liknande "sort | uniq".',
        difficulty: 'G',
        category: 'Textbearbetning'
    },
    {
        id: 'tent-fs-ex-21',
        question: 'Vad gör "cut -d: -f1 /etc/passwd"?',
        options: [
            'Tar bort första kolumnen',
            'Extraherar första fältet (användarnamn) med : som delimiter',
            'Klipper ut rader',
            'Visar filstorlek'
        ],
        correctIndex: 1,
        explanation: 'cut -d (delimiter) -f (field) extraherar specifika kolumner. /etc/passwd använder : som separator.',
        difficulty: 'VG',
        category: 'Textbearbetning'
    },
    {
        id: 'tent-fs-ex-22',
        question: 'Vad gör "awk \'{print $1}\' fil.txt"?',
        options: [
            'Skriver ut hela filen',
            'Skriver ut första kolumnen (whitespace-separerad)',
            'Räknar rader',
            'Söker efter mönster'
        ],
        correctIndex: 1,
        explanation: 'awk är kraftfullt för textbearbetning. $1 = första fältet, $2 = andra, osv.',
        difficulty: 'VG',
        category: 'Textbearbetning'
    },
    {
        id: 'tent-fs-ex-23',
        question: 'Vad gör "sed \'s/old/new/g\' fil.txt"?',
        options: [
            'Tar bort "old" från filen',
            'Ersätter alla "old" med "new" i filen',
            'Söker efter "old"',
            'Lägger till "new" i slutet'
        ],
        correctIndex: 1,
        explanation: 'sed (stream editor) s = substitute, g = global (alla förekomster, inte bara första).',
        difficulty: 'VG',
        category: 'Textbearbetning'
    },
    {
        id: 'tent-fs-ex-24',
        question: 'Vad gör "xargs" kommandot?',
        options: [
            'Visar argumentlista',
            'Bygger och kör kommandon från standard input',
            'Exporterar variabler',
            'Komprimerar filer'
        ],
        correctIndex: 1,
        explanation: 'xargs tar input och skickar som argument. T.ex. "find . -name \"*.txt\" | xargs rm"',
        difficulty: 'VG',
        category: 'Avancerat'
    },
    {
        id: 'tent-fs-ex-25',
        question: 'Vad är en inode i Linux?',
        options: [
            'En nätverksenhet',
            'En datastruktur som lagrar metadata om filer',
            'En typ av partition',
            'En loggfil'
        ],
        correctIndex: 1,
        explanation: 'Inode innehåller filens metadata (permissions, ägare, storlek, etc.) men inte filnamnet.',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'tent-fs-ex-26',
        question: 'Hur visar du inode-nummer för filer?',
        options: ['ls -l', 'ls -i', 'ls -n', 'ls -a'],
        correctIndex: 1,
        explanation: 'ls -i visar inode-nummer. Användbart för att se hard links (samma inode).',
        difficulty: 'VG',
        category: 'Filsystem'
    },
    {
        id: 'tent-fs-ex-27',
        question: 'Vad gör "file kommando"?',
        options: [
            'Skapar en fil',
            'Identifierar filtypen baserat på innehållet',
            'Visar filstorlek',
            'Öppnar filen'
        ],
        correctIndex: 1,
        explanation: 'file analyserar filens "magic number" och innehåll för att avgöra typ.',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-ex-28',
        question: 'Vad gör "stat fil.txt"?',
        options: [
            'Visar filinnehåll',
            'Visar detaljerad filinformation (inode, timestamps, etc.)',
            'Startar en process',
            'Visar systemstatus'
        ],
        correctIndex: 1,
        explanation: 'stat visar Access time, Modify time, Change time, inode, block count, etc.',
        difficulty: 'VG',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-ex-29',
        question: 'Vad är skillnaden mellan /var och /tmp?',
        options: [
            'Ingen skillnad',
            '/var är för variabel data som loggar, /tmp för temporära filer',
            '/tmp är permanent',
            '/var rensas vid omstart'
        ],
        correctIndex: 1,
        explanation: '/var (variable) innehåller loggar, mail, databaser. /tmp rensas ofta vid omstart.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'tent-fs-ex-30',
        question: 'Var finns enhetsfiler i Linux?',
        options: ['/etc/devices', '/dev', '/sys/devices', '/mnt'],
        correctIndex: 1,
        explanation: '/dev innehåller device files som /dev/sda (disk), /dev/null, /dev/tty.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    }
]

// =============================================================================
// MOMENT 1B: ANVÄNDARHANTERING - NYA FRÅGOR (30 st)
// =============================================================================

export const ANVANDARE_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-user-ex-1',
        question: 'Vad gör kommandot "id"?',
        options: [
            'Visar system-ID',
            'Visar aktuell användares UID, GID och grupptillhörigheter',
            'Skapar ny användare',
            'Visar process-ID'
        ],
        correctIndex: 1,
        explanation: 'id visar användar-ID (UID), grupp-ID (GID) och alla grupper användaren tillhör.',
        difficulty: 'G',
        category: 'Användarinfo'
    },
    {
        id: 'tent-user-ex-2',
        question: 'Vad betyder UID 0?',
        options: [
            'Första vanliga användaren',
            'Root-användaren (superuser)',
            'Systemanvändare',
            'Gästanvändare'
        ],
        correctIndex: 1,
        explanation: 'UID 0 är alltid root. UID 1-999 är ofta systemanvändare, 1000+ är vanliga användare.',
        difficulty: 'G',
        category: 'Användarinfo'
    },
    {
        id: 'tent-user-ex-3',
        question: 'Vad gör "useradd -m -s /bin/bash newuser"?',
        options: [
            'Skapar användare utan hemkatalog',
            'Skapar användare med hemkatalog och bash som shell',
            'Tar bort användare',
            'Ändrar användarens shell'
        ],
        correctIndex: 1,
        explanation: '-m skapar hemkatalog, -s anger default shell. Utan -m skapas ingen hemkatalog.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'tent-user-ex-4',
        question: 'Vad är skillnaden mellan useradd och adduser?',
        options: [
            'Ingen skillnad',
            'adduser är interaktivt och mer användarvänligt, useradd är low-level',
            'useradd är nyare',
            'adduser finns bara på Red Hat'
        ],
        correctIndex: 1,
        explanation: 'adduser är ett script som frågar efter lösenord, namn etc. useradd kräver alla flaggor.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'tent-user-ex-5',
        question: 'Var lagras användarnas lösenordshashar?',
        options: ['/etc/passwd', '/etc/shadow', '/etc/group', '/etc/security'],
        correctIndex: 1,
        explanation: '/etc/shadow innehåller krypterade lösenord. /etc/passwd innehåller användarinfo utan lösenord.',
        difficulty: 'G',
        category: 'Systemfiler'
    },
    {
        id: 'tent-user-ex-6',
        question: 'Vad gör "passwd -l user"?',
        options: [
            'Listar användarens lösenord',
            'Låser användarkontot',
            'Låser upp kontot',
            'Visar lösenordspolicy'
        ],
        correctIndex: 1,
        explanation: '-l (lock) låser kontot genom att sätta ! framför lösenordshashen i /etc/shadow.',
        difficulty: 'G',
        category: 'Lösenord'
    },
    {
        id: 'tent-user-ex-7',
        question: 'Hur tar du bort en användare och dess hemkatalog?',
        options: [
            'userdel user',
            'userdel -r user',
            'deluser user',
            'rmuser user'
        ],
        correctIndex: 1,
        explanation: 'userdel -r (remove) tar bort användaren OCH hemkatalogen. Utan -r finns hemkatalogen kvar.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'tent-user-ex-8',
        question: 'Vad gör "usermod -aG docker user"?',
        options: [
            'Tar bort användare från docker-gruppen',
            'Lägger till användare i docker-gruppen utan att ta bort andra grupper',
            'Skapar docker-gruppen',
            'Ändrar primär grupp till docker'
        ],
        correctIndex: 1,
        explanation: '-a (append) -G (groups) lägger till utan att ta bort befintliga grupper. VIKTIGT: utan -a ersätts alla grupper!',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'tent-user-ex-9',
        question: 'Hur skapar du en ny grupp?',
        options: ['newgroup grp', 'groupadd grp', 'addgroup grp', 'mkgroup grp'],
        correctIndex: 1,
        explanation: 'groupadd skapar en ny grupp. På Debian/Ubuntu fungerar även addgroup.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'tent-user-ex-10',
        question: 'Vad betyder "x" i andra fältet i /etc/passwd?',
        options: [
            'Användaren är inaktiv',
            'Lösenordet finns i /etc/shadow',
            'Inget lösenord satt',
            'Användaren är root'
        ],
        correctIndex: 1,
        explanation: 'x indikerar att lösenordshashen lagras i /etc/shadow för säkerhet.',
        difficulty: 'VG',
        category: 'Systemfiler'
    },
    {
        id: 'tent-user-ex-11',
        question: 'Vad gör "getent passwd user"?',
        options: [
            'Skapar användare',
            'Hämtar användarens entry från namn-tjänster',
            'Visar lösenord',
            'Validerar användare'
        ],
        correctIndex: 1,
        explanation: 'getent (get entries) hämtar från passwd, group, hosts etc. Fungerar även med LDAP.',
        difficulty: 'VG',
        category: 'Användarinfo'
    },
    {
        id: 'tent-user-ex-12',
        question: 'Vad betyder permission 644 på en fil?',
        options: [
            'rwx för alla',
            'rw för ägare, r för grupp och andra',
            'rwx för ägare, inget för andra',
            'Endast läsbar för alla'
        ],
        correctIndex: 1,
        explanation: '6=rw- (ägare), 4=r-- (grupp), 4=r-- (andra). 6=4+2 (read+write).',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-user-ex-13',
        question: 'Vad gör setuid-biten (chmod u+s)?',
        options: [
            'Gör filen osynlig',
            'Kör filen med ägarens rättigheter istället för användarens',
            'Låser filen',
            'Tar bort execute-permission'
        ],
        correctIndex: 1,
        explanation: 'setuid kör programmet med ägarens rättigheter. Exempel: /usr/bin/passwd har setuid för att kunna ändra /etc/shadow.',
        difficulty: 'VG',
        category: 'Special Permissions'
    },
    {
        id: 'tent-user-ex-14',
        question: 'Vad gör setgid-biten på en katalog?',
        options: [
            'Tar bort katalogen',
            'Nya filer ärver katalogens grupp istället för skaparens primära grupp',
            'Låser katalogen',
            'Gör katalogen skrivskyddad'
        ],
        correctIndex: 1,
        explanation: 'setgid på katalog är användbart för delat arbete - alla filer får samma grupp.',
        difficulty: 'VG',
        category: 'Special Permissions'
    },
    {
        id: 'tent-user-ex-15',
        question: 'Vad gör sticky bit på /tmp?',
        options: [
            'Gör katalogen snabbare',
            'Endast filägaren kan ta bort sina egna filer',
            'Alla kan ta bort alla filer',
            'Filer blir permanenta'
        ],
        correctIndex: 1,
        explanation: 'Sticky bit (chmod +t) förhindrar att användare tar bort andras filer i delade kataloger.',
        difficulty: 'VG',
        category: 'Special Permissions'
    },
    {
        id: 'tent-user-ex-16',
        question: 'Vad visar permission "drwxrwxrwt"?',
        options: [
            'En vanlig fil med alla rättigheter',
            'En katalog med sticky bit satt',
            'En symbolisk länk',
            'En krypterad fil'
        ],
        correctIndex: 1,
        explanation: 'd = directory, t = sticky bit. Exempel: /tmp har ofta denna permission.',
        difficulty: 'VG',
        category: 'Special Permissions'
    },
    {
        id: 'tent-user-ex-17',
        question: 'Hur sätter du rekursiva rättigheter på en katalog?',
        options: [
            'chmod 755 dir',
            'chmod -R 755 dir',
            'chmod --all 755 dir',
            'chmod 755 dir/*'
        ],
        correctIndex: 1,
        explanation: '-R (recursive) ändrar rättigheter på katalogen och allt innehåll.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-user-ex-18',
        question: 'Vad gör "chown user:group fil"?',
        options: [
            'Ändrar endast ägare',
            'Ändrar både ägare och grupp',
            'Ändrar endast grupp',
            'Tar bort ägandeskap'
        ],
        correctIndex: 1,
        explanation: 'user:group ändrar båda. chown user ändrar bara ägare, chgrp ändrar bara grupp.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-user-ex-19',
        question: 'Vad är umask 022?',
        options: [
            'Default permissions är 777',
            'Nya filer skapas med 644 (666-022) och kataloger med 755 (777-022)',
            'Alla filer blir read-only',
            'Umask har ingen effekt'
        ],
        correctIndex: 1,
        explanation: 'umask subtraheras från default (666 för filer, 777 för kataloger). 022 ger skrivskydd för grupp/other.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'tent-user-ex-20',
        question: 'Vad gör "su - user"?',
        options: [
            'Byter användare utan att läsa in environment',
            'Byter användare och simulerar full login (läser in profil)',
            'Kör ett kommando som user',
            'Visar användarinfo'
        ],
        correctIndex: 1,
        explanation: 'su - (med bindestreck) simulerar full login. Utan - behålls nuvarande environment.',
        difficulty: 'G',
        category: 'Användarbyte'
    },
    {
        id: 'tent-user-ex-21',
        question: 'Vad gör "sudo -i"?',
        options: [
            'Kör ett kommando som root',
            'Öppnar ett interaktivt root-shell med roots miljö',
            'Visar sudo-historik',
            'Installerar sudo'
        ],
        correctIndex: 1,
        explanation: 'sudo -i (interactive) ger ett root shell. Liknar "su -" men använder sudo.',
        difficulty: 'G',
        category: 'Sudo'
    },
    {
        id: 'tent-user-ex-22',
        question: 'Var konfigureras sudo-rättigheter?',
        options: ['/etc/passwd', '/etc/sudoers', '/etc/sudo.conf', '/etc/security/sudo'],
        correctIndex: 1,
        explanation: '/etc/sudoers redigeras med "visudo" som validerar syntaxen innan sparning.',
        difficulty: 'G',
        category: 'Sudo'
    },
    {
        id: 'tent-user-ex-23',
        question: 'Vad betyder raden "user ALL=(ALL:ALL) ALL" i sudoers?',
        options: [
            'User kan inte använda sudo',
            'User kan köra alla kommandon som alla användare på alla hosts',
            'User kan bara köra specifika kommandon',
            'User kan endast använda sudo lokalt'
        ],
        correctIndex: 1,
        explanation: 'ALL=(ALL:ALL) ALL = på alla hosts, som alla users/groups, alla kommandon.',
        difficulty: 'VG',
        category: 'Sudo'
    },
    {
        id: 'tent-user-ex-24',
        question: 'Hur ger du en grupp sudo-rättigheter?',
        options: [
            'Lägg till användare i gruppen "sudo" eller "wheel"',
            'Redigera /etc/passwd',
            'Använd chmod',
            'Skapa ny grupp med groupadd sudo'
        ],
        correctIndex: 0,
        explanation: 'På Debian/Ubuntu: gruppen sudo. På RHEL/CentOS: gruppen wheel. Konfigureras i /etc/sudoers.',
        difficulty: 'G',
        category: 'Sudo'
    },
    {
        id: 'tent-user-ex-25',
        question: 'Vad gör "groups user"?',
        options: [
            'Skapar nya grupper för användaren',
            'Visar vilka grupper användaren tillhör',
            'Tar bort användaren från grupper',
            'Ändrar primär grupp'
        ],
        correctIndex: 1,
        explanation: 'groups visar alla grupper en användare är medlem i.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'tent-user-ex-26',
        question: 'Vad är skillnaden mellan primär och sekundär grupp?',
        options: [
            'Ingen skillnad',
            'Primär grupp används för nya filer, sekundära ger extra behörigheter',
            'Sekundär grupp används för nya filer',
            'Man kan bara ha en grupp'
        ],
        correctIndex: 1,
        explanation: 'Filer skapas med primär grupp (GID i /etc/passwd). Sekundära grupper ger tillgång till resurser.',
        difficulty: 'VG',
        category: 'Grupper'
    },
    {
        id: 'tent-user-ex-27',
        question: 'Vad gör "newgrp docker"?',
        options: [
            'Skapar docker-gruppen',
            'Byter temporärt primär grupp till docker för aktuell session',
            'Tar bort docker-gruppen',
            'Lägger till användare i docker'
        ],
        correctIndex: 1,
        explanation: 'newgrp startar ett nytt shell med angiven grupp som primär. Användbart efter usermod utan utloggning.',
        difficulty: 'VG',
        category: 'Grupper'
    },
    {
        id: 'tent-user-ex-28',
        question: 'Hur tvingar du användare att byta lösenord vid nästa inloggning?',
        options: [
            'passwd -e user',
            'passwd -l user',
            'chage -d 0 user',
            'Både A och C fungerar'
        ],
        correctIndex: 3,
        explanation: 'passwd -e (expire) och chage -d 0 (lastchange=0) tvingar båda fram lösenordsbyte.',
        difficulty: 'VG',
        category: 'Lösenord'
    },
    {
        id: 'tent-user-ex-29',
        question: 'Vad visar "chage -l user"?',
        options: [
            'Användarens lösenord',
            'Lösenordspolicy och aging-information',
            'Användarens grupper',
            'Senaste inloggning'
        ],
        correctIndex: 1,
        explanation: 'chage -l visar när lösenord senast ändrades, när det går ut, varningsperiod, etc.',
        difficulty: 'VG',
        category: 'Lösenord'
    },
    {
        id: 'tent-user-ex-30',
        question: 'Vad är nologin shell (/sbin/nologin)?',
        options: [
            'Ett vanligt shell',
            'Ett shell som förhindrar interaktiv inloggning för systemanvändare',
            'Ett shell för root',
            'Ett grafiskt shell'
        ],
        correctIndex: 1,
        explanation: '/sbin/nologin eller /bin/false används för tjänstekonton som inte ska kunna logga in.',
        difficulty: 'G',
        category: 'Systemfiler'
    }
]
