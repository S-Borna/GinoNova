/**
 * Linux 24/7 Module - Premium Learning Content
 * 20 tasks from basics to advanced Linux system administration
 */

export interface ContentBlock {
  type: 'intro' | 'concept' | 'code' | 'quiz' | 'checkpoint' | 'tip' | 'warning'
  title?: string
  content?: string
  code?: string
  language?: string
  question?: string
  options?: string[]
  correctIndex?: number
  explanation?: string
  objectives?: string[]
  diagram?: string
}

export interface Linux247Task {
  id: string
  order: number
  title: string
  slug: string
  description: string
  difficulty: 'easy' | 'medium' | 'hard'
  estimatedMinutes: number
  xpReward: number
  category: string
  icon: string
  content_blocks: ContentBlock[]
}

export interface Linux247Module {
  id: string
  slug: string
  title: string
  description: string
  icon: string
  totalTasks: number
  estimatedHours: number
  tasks: Linux247Task[]
}

export const LINUX247_MODULE: Linux247Module = {
  id: 'linux-247',
  slug: 'linux-247',
  title: 'Linux 24/7',
  description: 'Komplett Linux för DevOps - från grunden till produktion',
  icon: 'terminal',
  totalTasks: 20,
  estimatedHours: 40,
  tasks: [
    // ========================================================================
    // TASK 1: File System Essentials
    // ========================================================================
    {
      id: 'linux247-1-filesystem',
      order: 1,
      title: 'File System Essentials',
      slug: 'file-system-essentials',
      description: 'Navigera, kopiera, flytta och hantera filer i Linux',
      difficulty: 'easy',
      estimatedMinutes: 45,
      xpReward: 100,
      category: 'Grundläggande',
      icon: '📁',
      content_blocks: [
        {
          type: 'intro',
          title: 'Lärandemål',
          objectives: [
            'Navigera i filsystemet med cd, pwd och ls',
            'Kopiera och flytta filer med cp och mv',
            'Ta bort filer säkert med rm',
            'Hitta filer med find och which',
            'Förstå Linux filsystemets struktur'
          ]
        },
        {
          type: 'concept',
          title: 'Varför viktigt för DevOps?',
          content: 'Som DevOps-ingenjör arbetar du konstant med filer. Konfigurationsfiler i /etc, loggar i /var/log, scripts i /opt eller /home, och applikationer i /var/www. Dessa kommandon använder du flera gånger per dag.',
          diagram: 'file-tree'
        },
        {
          type: 'concept',
          title: 'Navigation - De viktiga kommandona',
          content: '**cd** (change directory) - Byt katalog\n**pwd** (print working directory) - Visa var du är\n**ls** (list) - Lista innehåll'
        },
        {
          type: 'code',
          title: 'cd - Byt katalog',
          language: 'bash',
          code: `# Gå till specifik katalog
cd /var/log

# Gå upp en nivå
cd ..

# Gå till hemkatalogen
cd ~

# ⭐ PRO-TIPS: Tillbaka till förra katalogen
cd -`
        },
        {
          type: 'code',
          title: 'ls - Lista filer (MEMORERA DETTA!)',
          language: 'bash',
          code: `# Enkel lista
ls

# Lång lista med detaljer
ls -l

# Inkludera dolda filer
ls -la

# ⭐ FAVORITEN - Human-readable med allt
ls -lah

# Sorterat efter tid (nyaste först)
ls -lht`
        },
        {
          type: 'quiz',
          question: 'Vilket kommando visar ALLA filer (inkl. dolda) med human-readable storlekar?',
          options: ['ls -l', 'ls -la', 'ls -lah', 'ls -h'],
          correctIndex: 2,
          explanation: 'ls -lah kombinerar: -l (lång lista), -a (alla filer inkl. dolda), -h (human-readable storlekar som KB, MB, GB)'
        },
        {
          type: 'concept',
          title: 'Filoperationer',
          content: '**cp** (copy) - Kopiera filer\n**mv** (move) - Flytta eller byt namn\n**rm** (remove) - Ta bort filer\n**mkdir** (make directory) - Skapa kataloger'
        },
        {
          type: 'code',
          title: 'cp - Kopiera filer',
          language: 'bash',
          code: `# Kopiera fil
cp fil.txt kopia.txt

# ⭐ VIKTIGT: -r för kataloger (rekursivt)
cp -r katalog/ backup/

# DevOps-mönster: Backup innan ändring
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%Y%m%d)`
        },
        {
          type: 'code',
          title: 'rm - Ta bort (FÖRSIKTIGT!)',
          language: 'bash',
          code: `# Ta bort fil
rm fil.txt

# Ta bort katalog rekursivt
rm -r katalog/

# ⚠️ FARLIGT - Force delete (dubbelkolla!)
rm -rf katalog/

# Säkrare: Interaktiv (frågar först)
rm -i fil.txt`
        },
        {
          type: 'warning',
          title: 'VARNING: rm -rf',
          content: 'rm -rf tar bort ALLT utan att fråga. Dubbelkolla ALLTID sökvägen innan du kör detta kommando. Ett misstag kan radera hela systemet!'
        },
        {
          type: 'code',
          title: 'find - Sök efter filer',
          language: 'bash',
          code: `# Hitta .log-filer
find /var/log -name "*.log"

# Hitta stora filer (>100MB)
find . -type f -size +100M

# Hitta nyligen ändrade filer (senaste 7 dagarna)
find /etc -mtime -7

# ⭐ PRO: Hitta och ta bort gamla temp-filer
find /tmp -type f -mtime +30 -delete`
        },
        {
          type: 'quiz',
          question: 'Du ska kopiera hela katalogen "projekt" till "backup". Vilket kommando är korrekt?',
          options: ['cp projekt backup', 'cp -r projekt/ backup/', 'mv projekt backup', 'copy projekt backup'],
          correctIndex: 1,
          explanation: 'cp -r behövs för att kopiera kataloger rekursivt. Utan -r kopieras bara filer, inte underkataloger.'
        },
        {
          type: 'tip',
          title: 'DevOps Pro-Tips',
          content: '1. Gör ALLTID backup innan du ändrar config-filer\n2. Använd ls -la innan rm för att verifiera\n3. Lär dig tab-completion - det sparar tid och förhindrar stavfel'
        },
        {
          type: 'checkpoint',
          title: 'Checkpoint: File System Essentials',
          content: 'Du kan nu navigera i Linux filsystemet, kopiera/flytta/ta bort filer, och hitta filer med find. Dessa kommandon är grunden för allt DevOps-arbete!'
        }
      ]
    },

    // ========================================================================
    // TASK 2: Text Processing & Search
    // ========================================================================
    {
      id: 'linux247-2-text',
      order: 2,
      title: 'Text Processing & Search',
      slug: 'text-processing',
      description: 'Visa, sök och manipulera textfiler effektivt',
      difficulty: 'easy',
      estimatedMinutes: 50,
      xpReward: 120,
      category: 'Grundläggande',
      icon: '📝',
      content_blocks: [
        {
          type: 'intro',
          title: 'Lärandemål',
          objectives: [
            'Visa filinnehåll med cat, less och head/tail',
            'Söka i filer med grep och dess flaggor',
            'Kombinera kommandon med pipes (|)',
            'Räkna rader/ord med wc',
            'Sortera och filtrera data'
          ]
        },
        {
          type: 'concept',
          title: 'Varför texthantering är kritiskt',
          content: 'I Linux är ALLT filer - konfiguration, loggar, data. Som DevOps läser du loggar, söker efter fel, och filtrerar data dagligen. Att behärska grep och pipes gör dig 10x snabbare.',
          diagram: 'pipe-flow'
        },
        {
          type: 'code',
          title: 'Visa filer - cat, less, head, tail',
          language: 'bash',
          code: `# Visa hela filen
cat fil.txt

# Visa med radnummer
cat -n fil.txt

# ⭐ less - Bläddra i stora filer (q för avsluta)
less /var/log/syslog

# Första 10 raderna
head fil.txt
head -20 fil.txt    # Första 20

# Sista 10 raderna
tail fil.txt

# ⭐ SUPERVIKTIGT: Följ logg i realtid
tail -f /var/log/nginx/access.log`
        },
        {
          type: 'quiz',
          question: 'Du vill se nya loggmeddelanden i realtid. Vilket kommando använder du?',
          options: ['cat -f logfil', 'tail -f logfil', 'less -f logfil', 'watch logfil'],
          correctIndex: 1,
          explanation: 'tail -f "följer" filen och visar nya rader när de läggs till. Perfekt för att övervaka loggar i realtid!'
        },
        {
          type: 'concept',
          title: 'grep - Din bästa vän',
          content: 'grep (Global Regular Expression Print) söker efter mönster i filer. Det är det mest använda kommandot för att hitta information i loggar och konfigurationsfiler.'
        },
        {
          type: 'code',
          title: 'grep - Sök i filer',
          language: 'bash',
          code: `# Enkel sökning
grep "error" /var/log/syslog

# Case-insensitive (-i)
grep -i "ERROR" logfil.txt

# Visa radnummer (-n)
grep -n "failed" /var/log/auth.log

# Rekursiv sökning i alla filer (-r)
grep -r "password" /etc/

# ⭐ KOMBINERA FLAGGOR
grep -rni "connection refused" /var/log/

# Invertera - visa rader som INTE matchar (-v)
grep -v "^#" /etc/ssh/sshd_config  # Ignorera kommentarer`
        },
        {
          type: 'code',
          title: 'Pipes - Kombinera kommandon',
          language: 'bash',
          code: `# Sök i output från annat kommando
cat /var/log/syslog | grep "error"

# Räkna antal fel
grep "error" /var/log/syslog | wc -l

# ⭐ PRAKTISKT: Hitta de 10 vanligaste felen
grep "error" /var/log/syslog | sort | uniq -c | sort -rn | head -10

# Filtrera och visa specifika kolumner
ps aux | grep nginx | awk '{print $2, $11}'`
        },
        {
          type: 'quiz',
          question: 'Vad gör kommandot: grep -rni "error" /var/log/',
          options: [
            'Söker "error" endast i en fil',
            'Söker rekursivt, case-insensitive, med radnummer',
            'Tar bort rader med "error"',
            'Räknar antal "error"'
          ],
          correctIndex: 1,
          explanation: '-r = rekursivt (alla filer), -n = visa radnummer, -i = case-insensitive. Perfekt för att hitta fel i loggar!'
        },
        {
          type: 'code',
          title: 'wc, sort, uniq - Analysera data',
          language: 'bash',
          code: `# Räkna rader, ord, tecken
wc fil.txt
wc -l fil.txt      # Endast rader

# Sortera
sort fil.txt
sort -n numbers.txt    # Numerisk sortering
sort -r fil.txt        # Omvänd ordning

# Unika rader (kräver sorterad input!)
sort fil.txt | uniq
sort fil.txt | uniq -c   # Med antal`
        },
        {
          type: 'tip',
          title: 'DevOps Pro-Tips: Log Analysis',
          content: '**Snabb felanalys:**\n```bash\ngrep -i error /var/log/syslog | tail -50\n```\n\n**Räkna unika IP-adresser:**\n```bash\nawk \'{print $1}\' access.log | sort | uniq -c | sort -rn | head\n```'
        },
        {
          type: 'checkpoint',
          title: 'Checkpoint: Text Processing',
          content: 'Du behärskar nu grunderna i texthantering! grep, pipes, och tail -f är dina nya bästa vänner för att analysera loggar och hitta problem snabbt.'
        }
      ]
    },

    // ========================================================================
    // TASK 3: Process Management
    // ========================================================================
    {
      id: 'linux247-3-processes',
      order: 3,
      title: 'Process Management',
      slug: 'process-management',
      description: 'Hantera processer, övervaka systemet och felsök',
      difficulty: 'easy',
      estimatedMinutes: 45,
      xpReward: 110,
      category: 'Grundläggande',
      icon: '⚙️',
      content_blocks: [
        {
          type: 'intro',
          title: 'Lärandemål',
          objectives: [
            'Lista processer med ps och top/htop',
            'Avsluta processer med kill och pkill',
            'Köra processer i bakgrunden',
            'Förstå process-states och PID',
            'Övervaka systemresurser'
          ]
        },
        {
          type: 'concept',
          title: 'Processer i Linux',
          content: 'En process är ett körande program. Varje process har ett unikt Process ID (PID). Som DevOps måste du kunna hitta problematiska processer, avsluta dem, och övervaka resurser.',
          diagram: 'process-tree'
        },
        {
          type: 'code',
          title: 'ps - Lista processer',
          language: 'bash',
          code: `# Visa dina processer
ps

# ⭐ VIKTIGAST: Alla processer med detaljer
ps aux

# Hitta specifik process
ps aux | grep nginx

# Trädvy (visa parent-child)
ps auxf

# Endast PID för en process
pgrep nginx`
        },
        {
          type: 'quiz',
          question: 'Du vill se alla körande processer på systemet. Vilket kommando?',
          options: ['ps', 'ps -a', 'ps aux', 'ps --all'],
          correctIndex: 2,
          explanation: 'ps aux visar ALLA processer för ALLA användare med detaljerad info (CPU%, MEM%, kommando etc.)'
        },
        {
          type: 'code',
          title: 'top / htop - Realtidsövervakning',
          language: 'bash',
          code: `# Grundläggande övervakning
top

# ⭐ BÄTTRE: htop (installera med apt install htop)
htop

# Tangenter i top/htop:
# q = avsluta
# k = kill process
# M = sortera efter minne
# P = sortera efter CPU
# / = sök`
        },
        {
          type: 'code',
          title: 'kill - Avsluta processer',
          language: 'bash',
          code: `# Avsluta med PID (SIGTERM - snällt)
kill 1234

# Tvinga avslut (SIGKILL - hårt)
kill -9 1234

# ⭐ ENKLARE: Avsluta via namn
pkill nginx

# Avsluta ALLA med namn
killall nginx

# Skicka HUP-signal (reload config)
kill -HUP $(pgrep nginx)`
        },
        {
          type: 'warning',
          title: 'kill -9 vs kill',
          content: 'kill (SIGTERM) ger processen chans att städa upp. kill -9 (SIGKILL) avslutar omedelbart utan cleanup. Använd -9 endast om vanlig kill inte fungerar!'
        },
        {
          type: 'quiz',
          question: 'Nginx svarar inte. Du vill avsluta och låta den städa upp. Vad kör du först?',
          options: ['kill -9 $(pgrep nginx)', 'pkill nginx', 'killall -9 nginx', 'rm nginx'],
          correctIndex: 1,
          explanation: 'pkill nginx skickar SIGTERM vilket ger nginx chans att stänga connections och spara state innan den avslutas.'
        },
        {
          type: 'code',
          title: 'Bakgrundsprocesser',
          language: 'bash',
          code: `# Kör i bakgrunden med &
./long_script.sh &

# Se bakgrundsjobb
jobs

# Ta fram till förgrunden
fg %1

# Pausa körande process: Ctrl+Z
# Fortsätt i bakgrunden:
bg

# ⭐ Kör kommando som överlever logout
nohup ./script.sh &`
        },
        {
          type: 'tip',
          title: 'DevOps Pro-Tips',
          content: '**Hitta vad som äter CPU:**\n```bash\nps aux --sort=-%cpu | head -10\n```\n\n**Hitta vad som äter RAM:**\n```bash\nps aux --sort=-%mem | head -10\n```'
        },
        {
          type: 'checkpoint',
          title: 'Checkpoint: Process Management',
          content: 'Du kan nu övervaka systemet, hitta problematiska processer, och hantera dem effektivt. ps aux och htop är dina go-to verktyg!'
        }
      ]
    },

    // ========================================================================
    // TASK 4: System Information & Monitoring
    // ========================================================================
    {
      id: 'linux247-4-sysinfo',
      order: 4,
      title: 'System Information & Monitoring',
      slug: 'system-info',
      description: 'Samla systeminformation och övervaka prestanda',
      difficulty: 'easy',
      estimatedMinutes: 40,
      xpReward: 100,
      category: 'Grundläggande',
      icon: '📊',
      content_blocks: [
        {
          type: 'intro',
          title: 'Lärandemål',
          objectives: [
            'Visa systeminfo med uname och hostnamectl',
            'Kontrollera disk med df och du',
            'Övervaka minne med free',
            'Se nätverkskonfiguration',
            'Förstå system-metrics'
          ]
        },
        {
          type: 'code',
          title: 'Systeminformation',
          language: 'bash',
          code: `# Kernel och OS
uname -a

# ⭐ Detaljerad systeminfo
hostnamectl

# CPU-info
lscpu
cat /proc/cpuinfo | grep "model name" | head -1

# Minne
cat /proc/meminfo | head -5`
        },
        {
          type: 'code',
          title: 'df - Diskutrymme',
          language: 'bash',
          code: `# ⭐ Human-readable diskutrymme
df -h

# Endast lokala filsystem
df -h --local

# Specifik mount
df -h /var

# Visa filsystemtyp
df -Th`
        },
        {
          type: 'quiz',
          question: 'Disken är full. Vilket kommando ger snabbast överblick?',
          options: ['du -sh /', 'df -h', 'ls -la /', 'free -h'],
          correctIndex: 1,
          explanation: 'df -h visar snabbt hur mycket utrymme som används på varje partition. du tar längre tid då det räknar allt.'
        },
        {
          type: 'code',
          title: 'du - Katalogstorlekar',
          language: 'bash',
          code: `# Storlek på katalog
du -sh /var/log

# Top 10 största kataloger
du -h /var | sort -rh | head -10

# ⭐ PRO: Hitta var disken fylls
du -h --max-depth=1 / 2>/dev/null | sort -rh | head -20`
        },
        {
          type: 'code',
          title: 'free - Minnesanvändning',
          language: 'bash',
          code: `# ⭐ Human-readable minne
free -h

# Output:
#               total   used   free   shared  buff/cache  available
# Mem:           16Gi   4.2Gi  8.1Gi   512Mi      3.7Gi      11Gi
# Swap:          2.0Gi  0B     2.0Gi

# OBS: "available" är det viktiga, inte "free"!`
        },
        {
          type: 'concept',
          title: 'Förstå free output',
          content: '**total**: Totalt RAM\n**used**: Aktivt använt minne\n**free**: Helt oanvänt (oftast lågt)\n**buff/cache**: Minne för disk-cache\n**available**: ⭐ Det som faktiskt kan användas! Cache frigörs vid behov.'
        },
        {
          type: 'code',
          title: 'Nätverksinformation',
          language: 'bash',
          code: `# IP-adresser
ip a

# Äldre variant (fortfarande vanlig)
ifconfig

# Routing-tabell
ip route

# DNS-servers
cat /etc/resolv.conf

# ⭐ Lyssnade portar
ss -tuln
# eller
netstat -tuln`
        },
        {
          type: 'quiz',
          question: 'Du behöver se vilka portar som lyssnar på servern. Vad kör du?',
          options: ['ps aux', 'netstat -tuln', 'df -h', 'free -h'],
          correctIndex: 1,
          explanation: 'netstat -tuln (eller ss -tuln) visar alla TCP/UDP-portar som lyssnar. -t=TCP, -u=UDP, -l=listening, -n=numeriskt'
        },
        {
          type: 'tip',
          title: 'One-liner Dashboard',
          content: '```bash\necho "=== SYSTEM ===" && uname -n && echo "=== DISK ===" && df -h / && echo "=== MEM ===" && free -h && echo "=== LOAD ===" && uptime\n```'
        },
        {
          type: 'checkpoint',
          title: 'Checkpoint: System Monitoring',
          content: 'Du kan nu snabbt diagnostisera ett system: kontrollera disk (df -h), minne (free -h), nätverk (ip a, ss -tuln), och systeminformation!'
        }
      ]
    },

    // ========================================================================
    // TASK 5: Log Management
    // ========================================================================
    {
      id: 'linux247-5-logs',
      order: 5,
      title: 'Log Management',
      slug: 'log-management',
      description: 'Förstå, läsa och analysera systemloggar',
      difficulty: 'easy',
      estimatedMinutes: 45,
      xpReward: 110,
      category: 'Grundläggande',
      icon: '📋',
      content_blocks: [
        {
          type: 'intro',
          title: 'Lärandemål',
          objectives: [
            'Förstå Linux logg-struktur (/var/log)',
            'Läsa journalctl för systemd-loggar',
            'Analysera auth.log för säkerhet',
            'Söka effektivt i loggar',
            'Hantera loggrotation'
          ]
        },
        {
          type: 'concept',
          title: 'Linux Loggar',
          content: 'Loggar är din bästa vän vid felsökning. Nästan alla Linux-system loggar till /var/log. Moderna system med systemd använder journalctl för centraliserad logging.',
          diagram: 'log-flow'
        },
        {
          type: 'code',
          title: 'Viktiga loggfiler',
          language: 'bash',
          code: `# Systemloggar
/var/log/syslog        # Generella systemloggar (Debian/Ubuntu)
/var/log/messages      # Generella systemloggar (RHEL/CentOS)

# Säkerhet & autentisering
/var/log/auth.log      # SSH-logins, sudo, etc.

# Applikationer
/var/log/nginx/        # Nginx access + error logs
/var/log/apache2/      # Apache logs
/var/log/mysql/        # MySQL logs

# Boot & kernel
/var/log/kern.log      # Kernel messages
/var/log/dmesg         # Boot messages`
        },
        {
          type: 'code',
          title: 'journalctl - Systemd-loggar',
          language: 'bash',
          code: `# Alla loggar
journalctl

# ⭐ Följ i realtid
journalctl -f

# Loggar för specifik service
journalctl -u nginx
journalctl -u ssh

# Endast fel
journalctl -p err

# Sedan boot
journalctl -b

# Senaste timmen
journalctl --since "1 hour ago"

# Kombinera!
journalctl -u nginx --since "1 hour ago" -p err`
        },
        {
          type: 'quiz',
          question: 'Du vill se nginx-fel i realtid. Vilket kommando?',
          options: [
            'tail -f /var/log/nginx/error.log',
            'journalctl -u nginx -f',
            'Båda fungerar!',
            'cat /var/log/nginx/error.log'
          ],
          correctIndex: 2,
          explanation: 'Både tail -f och journalctl -f fungerar! tail -f är för filer, journalctl -f för systemd-services.'
        },
        {
          type: 'code',
          title: 'Praktisk logganalys',
          language: 'bash',
          code: `# Senaste SSH-inloggningar
grep "Accepted" /var/log/auth.log | tail -20

# Misslyckade inloggningsförsök
grep "Failed password" /var/log/auth.log

# ⭐ Top 10 IP-adresser som försökt logga in
grep "Failed password" /var/log/auth.log | \\
  awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -10

# Räkna 404-fel i nginx
grep " 404 " /var/log/nginx/access.log | wc -l`
        },
        {
          type: 'code',
          title: 'Loggrotation',
          language: 'bash',
          code: `# Logrotate konfiguration
cat /etc/logrotate.conf
ls /etc/logrotate.d/

# Exempel: nginx logrotation
cat /etc/logrotate.d/nginx

# Manuell rotation (testa config)
logrotate -d /etc/logrotate.conf

# Tvinga rotation
logrotate -f /etc/logrotate.conf`
        },
        {
          type: 'tip',
          title: 'Quick Troubleshooting Cheat Sheet',
          content: '**Service startar inte:**\n```bash\njournalctl -u servicename -n 50 --no-pager\n```\n\n**Senaste systemfel:**\n```bash\njournalctl -p err --since "10 min ago"\n```\n\n**Disk full? Hitta stora loggar:**\n```bash\ndu -sh /var/log/* | sort -rh | head -10\n```'
        },
        {
          type: 'checkpoint',
          title: 'Checkpoint: Log Management',
          content: 'Du kan nu navigera Linux loggsystemet, använda journalctl effektivt, och analysera loggar för felsökning. Detta är en av de viktigaste DevOps-skills!'
        }
      ]
    },

    // ========================================================================
    // TASK 6-20: Placeholder - will be added in next parts
    // ========================================================================
    {
      id: 'linux247-6-ssh',
      order: 6,
      title: 'SSH & Remote Access',
      slug: 'ssh-remote-access',
      description: 'Säker fjärråtkomst och SSH-nyckelhantering',
      difficulty: 'medium',
      estimatedMinutes: 50,
      xpReward: 130,
      category: 'Nätverk',
      icon: '🔐',
      content_blocks: [
        {
          type: 'intro',
          title: 'Lärandemål',
          objectives: [
            'Ansluta till servrar med SSH',
            'Skapa och hantera SSH-nycklar',
            'Konfigurera SSH-klient (~/.ssh/config)',
            'Förstå SSH-säkerhet',
            'Använda SCP och rsync för filöverföring'
          ]
        },
        {
          type: 'concept',
          title: 'SSH - Secure Shell',
          content: 'SSH är standarden för säker fjärråtkomst till Linux-servrar. Istället för lösenord använder proffs SSH-nycklar för autentisering - säkrare och bekvämare.',
          diagram: 'ssh-flow'
        },
        {
          type: 'code',
          title: 'Grundläggande SSH',
          language: 'bash',
          code: `# Anslut till server
ssh user@server.com

# Specifik port
ssh -p 2222 user@server.com

# Kör kommando direkt
ssh user@server "uptime && df -h"`
        },
        {
          type: 'code',
          title: 'SSH-nycklar (VIKTIGT!)',
          language: 'bash',
          code: `# ⭐ Skapa SSH-nyckelpar
ssh-keygen -t ed25519 -C "din.email@example.com"

# Kopiera publik nyckel till server
ssh-copy-id user@server.com

# Eller manuellt:
cat ~/.ssh/id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"`
        },
        {
          type: 'quiz',
          question: 'Vilken fil innehåller din PRIVATA SSH-nyckel som ALDRIG ska delas?',
          options: ['~/.ssh/id_ed25519.pub', '~/.ssh/id_ed25519', '~/.ssh/authorized_keys', '~/.ssh/known_hosts'],
          correctIndex: 1,
          explanation: 'id_ed25519 (utan .pub) är din privata nyckel. Den publika (.pub) kopieras till servrar, men den privata stannar på din maskin!'
        },
        {
          type: 'code',
          title: 'SSH Config - Gör livet enklare',
          language: 'bash',
          code: `# ~/.ssh/config
Host prod
    HostName prod.example.com
    User deploy
    Port 22
    IdentityFile ~/.ssh/prod_key

Host staging
    HostName staging.example.com
    User deploy
    Port 2222

# Nu kan du köra:
ssh prod
ssh staging`
        },
        {
          type: 'code',
          title: 'Filöverföring - SCP & rsync',
          language: 'bash',
          code: `# SCP - Kopiera filer
scp fil.txt user@server:/path/
scp -r katalog/ user@server:/path/

# ⭐ rsync - Smartare synkronisering
rsync -avz katalog/ user@server:/path/
# -a = archive (behåll permissions)
# -v = verbose
# -z = compress

# Synka och ta bort borttagna filer
rsync -avz --delete src/ user@server:/dest/`
        },
        {
          type: 'checkpoint',
          title: 'Checkpoint: SSH & Remote Access',
          content: 'Du kan nu ansluta säkert till servrar, skapa SSH-nycklar, och överföra filer. SSH-config gör ditt liv mycket enklare!'
        }
      ]
    },

    {
      id: 'linux247-7-firewall',
      order: 7,
      title: 'Firewall Essentials',
      slug: 'firewall-essentials',
      description: 'Konfigurera brandvägg med ufw och iptables',
      difficulty: 'medium',
      estimatedMinutes: 45,
      xpReward: 120,
      category: 'Säkerhet',
      icon: '🛡️',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['Förstå Linux brandvägg', 'Konfigurera ufw', 'Grundläggande iptables', 'Öppna/stänga portar'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Firewall Essentials' }
      ]
    },

    {
      id: 'linux247-8-network',
      order: 8,
      title: 'Network Basics',
      slug: 'network-basics',
      description: 'Nätverkskonfiguration och felsökning',
      difficulty: 'medium',
      estimatedMinutes: 50,
      xpReward: 130,
      category: 'Nätverk',
      icon: '🌐',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['IP-konfiguration', 'DNS', 'Nätverksdiagnostik', 'curl och wget'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Network Basics' }
      ]
    },

    {
      id: 'linux247-9-packages',
      order: 9,
      title: 'Package Management',
      slug: 'package-management',
      description: 'Installera och hantera programpaket',
      difficulty: 'easy',
      estimatedMinutes: 40,
      xpReward: 100,
      category: 'System',
      icon: '📦',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['apt/yum grundläggande', 'Installera/ta bort paket', 'Uppdatera system', 'Repositories'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Package Management' }
      ]
    },

    {
      id: 'linux247-10-systemd',
      order: 10,
      title: 'System Services & systemd',
      slug: 'systemd-services',
      description: 'Hantera tjänster med systemctl',
      difficulty: 'medium',
      estimatedMinutes: 50,
      xpReward: 140,
      category: 'System',
      icon: '🔧',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['systemctl grundläggande', 'Starta/stoppa services', 'Skapa egna services', 'Felsök services'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'systemd Services' }
      ]
    },

    {
      id: 'linux247-11-permissions',
      order: 11,
      title: 'File Permissions & Security',
      slug: 'file-permissions',
      description: 'Linux rättigheter och säkerhet',
      difficulty: 'medium',
      estimatedMinutes: 45,
      xpReward: 120,
      category: 'Säkerhet',
      icon: '🔒',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['chmod och chown', 'Förstå rwx', 'SUID/SGID', 'umask'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Permissions' }
      ]
    },

    {
      id: 'linux247-12-compression',
      order: 12,
      title: 'Compression & Archives',
      slug: 'compression-archives',
      description: 'Komprimera och packa filer',
      difficulty: 'easy',
      estimatedMinutes: 35,
      xpReward: 90,
      category: 'Grundläggande',
      icon: '🗜️',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['tar grundläggande', 'gzip och gunzip', 'zip och unzip', 'Vanliga mönster'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Archives' }
      ]
    },

    {
      id: 'linux247-13-environment',
      order: 13,
      title: 'Environment & Variables',
      slug: 'environment-variables',
      description: 'Miljövariabler och konfiguration',
      difficulty: 'medium',
      estimatedMinutes: 40,
      xpReward: 110,
      category: 'System',
      icon: '🌍',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['export och env', 'PATH-variabeln', '.bashrc och .profile', 'Persistenta variabler'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Environment' }
      ]
    },

    {
      id: 'linux247-14-disk',
      order: 14,
      title: 'Disk Management',
      slug: 'disk-management',
      description: 'Hantera diskar och partitioner',
      difficulty: 'hard',
      estimatedMinutes: 55,
      xpReward: 150,
      category: 'System',
      icon: '💿',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['lsblk och fdisk', 'Mount och umount', 'fstab', 'LVM grundläggande'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Disks' }
      ]
    },

    {
      id: 'linux247-15-reference',
      order: 15,
      title: 'Quick Reference & Workflows',
      slug: 'quick-reference',
      description: 'Snabbreferens och arbetsflöden',
      difficulty: 'easy',
      estimatedMinutes: 30,
      xpReward: 80,
      category: 'Reference',
      icon: '📚',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['Vanliga kommando-mönster', 'Felsökningsworkflows', 'Cheat sheets'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Reference' }
      ]
    },

    {
      id: 'linux247-16-productivity',
      order: 16,
      title: 'Terminal Productivity',
      slug: 'terminal-productivity',
      description: 'Bli effektiv i terminalen',
      difficulty: 'medium',
      estimatedMinutes: 45,
      xpReward: 120,
      category: 'Produktivitet',
      icon: '⚡',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['Keyboard shortcuts', 'History och aliases', 'tmux grundläggande', 'Effektiva workflows'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Productivity' }
      ]
    },

    {
      id: 'linux247-17-users',
      order: 17,
      title: 'User & Group Management',
      slug: 'user-management',
      description: 'Hantera användare och grupper',
      difficulty: 'medium',
      estimatedMinutes: 45,
      xpReward: 120,
      category: 'Säkerhet',
      icon: '👥',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['useradd och usermod', 'Grupper', 'sudo-konfiguration', '/etc/passwd och /etc/shadow'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Users' }
      ]
    },

    {
      id: 'linux247-18-cron',
      order: 18,
      title: 'Cron Jobs & Scheduling',
      slug: 'cron-scheduling',
      description: 'Schemalägg uppgifter automatiskt',
      difficulty: 'medium',
      estimatedMinutes: 40,
      xpReward: 110,
      category: 'Automation',
      icon: '⏰',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['crontab syntax', 'Skapa cron jobs', 'Felsök cron', 'at och systemd timers'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Cron' }
      ]
    },

    {
      id: 'linux247-19-scripting',
      order: 19,
      title: 'Shell Scripting Fundamentals',
      slug: 'shell-scripting',
      description: 'Grundläggande Bash-scripting',
      difficulty: 'hard',
      estimatedMinutes: 60,
      xpReward: 160,
      category: 'Automation',
      icon: '📜',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['Script-struktur', 'Variabler och input', 'if/else och loopar', 'Funktioner'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Scripting' }
      ]
    },

    {
      id: 'linux247-20-troubleshooting',
      order: 20,
      title: 'Troubleshooting & Debugging',
      slug: 'troubleshooting',
      description: 'Systematisk felsökning',
      difficulty: 'hard',
      estimatedMinutes: 55,
      xpReward: 150,
      category: 'Avancerat',
      icon: '🔍',
      content_blocks: [
        { type: 'intro', title: 'Lärandemål', objectives: ['Felsökningsmetodik', 'Vanliga problem', 'strace och debug-verktyg', 'Performance-analys'] },
        { type: 'concept', title: 'Kommer snart', content: 'Detaljerat innehåll läggs till...' },
        { type: 'checkpoint', title: 'Checkpoint', content: 'Troubleshooting' }
      ]
    }
  ]
}

// Helper functions
export function getLinux247TaskById(taskId: string): Linux247Task | undefined {
  return LINUX247_MODULE.tasks.find(t => t.id === taskId || t.slug === taskId)
}

export function getLinux247TaskByOrder(order: number): Linux247Task | undefined {
  return LINUX247_MODULE.tasks.find(t => t.order === order)
}

export function getLinux247TaskBySlug(slug: string): Linux247Task | undefined {
  return LINUX247_MODULE.tasks.find(t => t.slug === slug)
}

export function getAllLinux247Tasks(): Linux247Task[] {
  return LINUX247_MODULE.tasks
}

// Group tasks by category
export function getLinux247TasksByCategory(): Record<string, Linux247Task[]> {
  const grouped: Record<string, Linux247Task[]> = {}
  for (const task of LINUX247_MODULE.tasks) {
    if (!grouped[task.category]) {
      grouped[task.category] = []
    }
    grouped[task.category].push(task)
  }
  return grouped
}
