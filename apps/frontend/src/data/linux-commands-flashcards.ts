/**
 * Linux Commands Flashcards
 * Konverterade från quiz-frågor till flashcard-format
 * ~350 flashcards för praktiska terminal-kommandon
 */

export interface CommandFlashcard {
    id: string;
    front: string;
    back: string;
    category: string;
    difficulty: 'G' | 'VG';
}

export interface CommandFlashcardSet {
    taskId: string;
    taskTitle: string;
    flashcards: CommandFlashcard[];
}

// ============================================================================
// NAVIGATION & FILSYSTEM FLASHCARDS
// ============================================================================
const NAVIGATION_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-nav-1", front: "Vilket kommando visar nuvarande katalog?", back: "pwd (print working directory)", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-2", front: "Hur byter du till din hemkatalog?", back: "cd ~ eller bara cd utan argument", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-3", front: "Hur går du en katalognivå upp?", back: "cd ..", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-4", front: "Hur går du till rotkatalogen?", back: "cd /", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-5", front: "Hur återgår du till föregående katalog?", back: "cd - (bindestreck)", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-6", front: "Hur listar du filer med detaljerad info?", back: "ls -l (long format)", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-7", front: "Hur visar du dolda filer?", back: "ls -a (all)", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-8", front: "Hur listar du med human-readable storlekar?", back: "ls -lh", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-9", front: "Hur sorterar du efter storlek?", back: "ls -lS (stort S)", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-10", front: "Hur sorterar du efter tid (nyast först)?", back: "ls -lt", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-11", front: "Hur skapar du en ny katalog?", back: "mkdir katalognamn", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-12", front: "Hur skapar du katalogstruktur på en gång?", back: "mkdir -p /a/b/c (parent)", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-13", front: "Hur tar du bort tom katalog?", back: "rmdir katalognamn", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-14", front: "Hur kopierar du en fil?", back: "cp källa mål", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-15", front: "Hur kopierar du katalog rekursivt?", back: "cp -r källa mål", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-16", front: "Hur flyttar/byter namn på fil?", back: "mv gammalt_namn nytt_namn", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-17", front: "Hur tar du bort en fil?", back: "rm filnamn", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-18", front: "Hur tar du bort katalog rekursivt?", back: "rm -r katalog", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-19", front: "Hur tar du bort med bekräftelse?", back: "rm -i fil (interactive)", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-20", front: "Hur skapar du tom fil?", back: "touch filnamn", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-21", front: "Hur hittar du filer rekursivt?", back: "find /path -name 'filnamn'", category: "Sökning", difficulty: "G" },
    { id: "fc-nav-22", front: "Hur hittar du alla .txt filer?", back: "find . -name '*.txt'", category: "Sökning", difficulty: "G" },
    { id: "fc-nav-23", front: "Hur hittar du filer större än 100MB?", back: "find . -size +100M", category: "Sökning", difficulty: "VG" },
    { id: "fc-nav-24", front: "Hur hittar du filer modifierade senaste 24h?", back: "find . -mtime -1", category: "Sökning", difficulty: "VG" },
    { id: "fc-nav-25", front: "Vad gör find -exec?", back: "Kör kommando på varje funnen fil", category: "Sökning", difficulty: "VG" },
    { id: "fc-nav-26", front: "Hur skapar du symbolisk länk?", back: "ln -s källa länknamn", category: "Filhantering", difficulty: "VG" },
    { id: "fc-nav-27", front: "Skillnad mellan hård och mjuk länk?", back: "Hård: samma inode. Mjuk: pekar på path (kan bli broken)", category: "Filhantering", difficulty: "VG" },
    { id: "fc-nav-28", front: "Hur tar du bort utan bekräftelse (farligt)?", back: "rm -rf (recursive force) - VARNING!", category: "Filhantering", difficulty: "G" },
    { id: "fc-nav-29", front: "Vad gör tree-kommandot?", back: "Visar katalogstruktur grafiskt", category: "Navigation", difficulty: "G" },
    { id: "fc-nav-30", front: "Hur visar du filstorleken?", back: "ls -lh eller du -h fil", category: "Filhantering", difficulty: "G" },
];

// ============================================================================
// TEXTBEARBETNING & SÖKNING FLASHCARDS
// ============================================================================
const TEXT_PROCESSING_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-txt-1", front: "Hur visar du hela filens innehåll?", back: "cat filnamn", category: "Text", difficulty: "G" },
    { id: "fc-txt-2", front: "Hur visar du de första 10 raderna?", back: "head -10 fil (eller head -n 10)", category: "Text", difficulty: "G" },
    { id: "fc-txt-3", front: "Hur visar du de sista 20 raderna?", back: "tail -20 fil (eller tail -n 20)", category: "Text", difficulty: "G" },
    { id: "fc-txt-4", front: "Hur följer du en loggfil i realtid?", back: "tail -f logfil.log", category: "Loggar", difficulty: "G" },
    { id: "fc-txt-5", front: "Hur söker du text i fil?", back: "grep 'sökterm' fil", category: "Sökning", difficulty: "G" },
    { id: "fc-txt-6", front: "Hur söker du case-insensitive?", back: "grep -i 'term' fil", category: "Sökning", difficulty: "G" },
    { id: "fc-txt-7", front: "Hur söker du rekursivt i kataloger?", back: "grep -r 'term' /path/", category: "Sökning", difficulty: "G" },
    { id: "fc-txt-8", front: "Hur visar du radnummer i grep?", back: "grep -n 'term' fil", category: "Sökning", difficulty: "G" },
    { id: "fc-txt-9", front: "Hur inverterar du grep (visar icke-matchande)?", back: "grep -v 'term' fil", category: "Sökning", difficulty: "G" },
    { id: "fc-txt-10", front: "Vad gör pipe (|)?", back: "Skickar output från ett kommando som input till nästa", category: "Pipes", difficulty: "G" },
    { id: "fc-txt-11", front: "Hur räknar du rader i fil?", back: "wc -l fil (wordcount -lines)", category: "Text", difficulty: "G" },
    { id: "fc-txt-12", front: "Hur räknar du ord i fil?", back: "wc -w fil (wordcount -words)", category: "Text", difficulty: "G" },
    { id: "fc-txt-13", front: "Hur sorterar du innehåll?", back: "sort fil", category: "Text", difficulty: "G" },
    { id: "fc-txt-14", front: "Hur sorterar du numeriskt?", back: "sort -n fil", category: "Text", difficulty: "G" },
    { id: "fc-txt-15", front: "Hur tar du bort dubletter?", back: "uniq (efter sort)", category: "Text", difficulty: "G" },
    { id: "fc-txt-16", front: "Hur räknar du förekomster med uniq?", back: "sort | uniq -c", category: "Text", difficulty: "VG" },
    { id: "fc-txt-17", front: "Hur extraherar du kolumner med cut?", back: "cut -d',' -f1,3 fil (delimiter, fields)", category: "Text", difficulty: "VG" },
    { id: "fc-txt-18", front: "Hur ersätter du text med sed?", back: "sed 's/gammal/ny/g' fil", category: "Text", difficulty: "VG" },
    { id: "fc-txt-19", front: "Hur skriver du ut specifik kolumn med awk?", back: "awk '{print $2}' fil", category: "Text", difficulty: "VG" },
    { id: "fc-txt-20", front: "Hur filtrerar du rader med awk?", back: "awk '/mönster/ {print $0}' fil", category: "Text", difficulty: "VG" },
    { id: "fc-txt-21", front: "Skillnad mellan > och >>?", back: "> skriver över, >> appendar", category: "Redirect", difficulty: "G" },
    { id: "fc-txt-22", front: "Hur omdirigerar du stderr?", back: "2> error.log", category: "Redirect", difficulty: "VG" },
    { id: "fc-txt-23", front: "Hur omdirigerar du stdout och stderr?", back: "&> output.log eller 2>&1", category: "Redirect", difficulty: "VG" },
    { id: "fc-txt-24", front: "Vad gör tee-kommandot?", back: "Skriver till både fil och stdout samtidigt", category: "Redirect", difficulty: "VG" },
    { id: "fc-txt-25", front: "Hur scrollar du genom fil interaktivt?", back: "less fil (q för att avsluta)", category: "Text", difficulty: "G" },
];

// ============================================================================
// PROCESSHANTERING FLASHCARDS
// ============================================================================
const PROCESS_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-proc-1", front: "Hur visar du körande processer?", back: "ps aux eller ps -ef", category: "Process", difficulty: "G" },
    { id: "fc-proc-2", front: "Hur visar du processer i realtid?", back: "top (q för att avsluta)", category: "Process", difficulty: "G" },
    { id: "fc-proc-3", front: "Vad är htop?", back: "Förbättrad interaktiv processvisare", category: "Process", difficulty: "G" },
    { id: "fc-proc-4", front: "Hur dödar du process med PID?", back: "kill PID", category: "Process", difficulty: "G" },
    { id: "fc-proc-5", front: "Hur tvångsdödar du en process?", back: "kill -9 PID (SIGKILL)", category: "Process", difficulty: "G" },
    { id: "fc-proc-6", front: "Hur dödar du alla processer med namn?", back: "killall processnamn", category: "Process", difficulty: "G" },
    { id: "fc-proc-7", front: "Hur hittar du PID för processnamn?", back: "pgrep processnamn", category: "Process", difficulty: "G" },
    { id: "fc-proc-8", front: "Vad är skillnad mellan SIGTERM och SIGKILL?", back: "SIGTERM (15) ger chans att avsluta, SIGKILL (9) tvångsdödar", category: "Process", difficulty: "VG" },
    { id: "fc-proc-9", front: "Hur kör du kommando i bakgrunden?", back: "kommando & (ampersand)", category: "Process", difficulty: "G" },
    { id: "fc-proc-10", front: "Hur listar du bakgrundsjobb?", back: "jobs", category: "Process", difficulty: "G" },
    { id: "fc-proc-11", front: "Hur tar du bakgrundsjobb till förgrunden?", back: "fg %jobid", category: "Process", difficulty: "G" },
    { id: "fc-proc-12", front: "Hur skickar du förgrundsjobb till bakgrunden?", back: "bg (efter Ctrl+Z)", category: "Process", difficulty: "VG" },
    { id: "fc-proc-13", front: "Hur pausar du ett körande kommando?", back: "Ctrl+Z (suspend)", category: "Process", difficulty: "G" },
    { id: "fc-proc-14", front: "Vad gör nohup?", back: "Låter process fortsätta efter logout", category: "Process", difficulty: "VG" },
    { id: "fc-proc-15", front: "Vad gör nice och renice?", back: "Ändrar process-prioritet (-20 högst, 19 lägst)", category: "Process", difficulty: "VG" },
];

// ============================================================================
// SYSTEMINFORMATION FLASHCARDS
// ============================================================================
const SYSTEM_INFO_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-sys-1", front: "Hur ser du diskutrymme?", back: "df -h (disk free, human-readable)", category: "System", difficulty: "G" },
    { id: "fc-sys-2", front: "Hur ser du katalogstorlek?", back: "du -sh /path (disk usage, summary, human)", category: "System", difficulty: "G" },
    { id: "fc-sys-3", front: "Hur ser du minnesanvändning?", back: "free -h", category: "System", difficulty: "G" },
    { id: "fc-sys-4", front: "Hur ser du CPU-info?", back: "lscpu eller cat /proc/cpuinfo", category: "System", difficulty: "G" },
    { id: "fc-sys-5", front: "Hur ser du kernel-version?", back: "uname -r", category: "System", difficulty: "G" },
    { id: "fc-sys-6", front: "Hur ser du fullständig systeminfo?", back: "uname -a (all)", category: "System", difficulty: "G" },
    { id: "fc-sys-7", front: "Hur ser du uptime?", back: "uptime", category: "System", difficulty: "G" },
    { id: "fc-sys-8", front: "Hur listar du blockenheter?", back: "lsblk", category: "Storage", difficulty: "G" },
    { id: "fc-sys-9", front: "Hur ser du nätverksgränssnitt?", back: "ip addr eller ip a", category: "Nätverk", difficulty: "G" },
    { id: "fc-sys-10", front: "Hur ser du öppna portar?", back: "ss -tulnp eller netstat -tulnp", category: "Nätverk", difficulty: "G" },
    { id: "fc-sys-11", front: "Hur testar du nätverksanslutning?", back: "ping host", category: "Nätverk", difficulty: "G" },
    { id: "fc-sys-12", front: "Hur spårar du nätverksväg?", back: "traceroute host", category: "Nätverk", difficulty: "G" },
    { id: "fc-sys-13", front: "Hur gör du DNS-uppslag?", back: "nslookup domain eller dig domain", category: "Nätverk", difficulty: "G" },
    { id: "fc-sys-14", front: "Hur ser du användarens grupper?", back: "groups [användarnamn]", category: "System", difficulty: "G" },
    { id: "fc-sys-15", front: "Hur ser du vem som är inloggad?", back: "who eller w", category: "System", difficulty: "G" },
];

// ============================================================================
// LOGGHANTERING FLASHCARDS
// ============================================================================
const LOG_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-log-1", front: "Hur ser du systemloggar med journald?", back: "journalctl", category: "Loggar", difficulty: "G" },
    { id: "fc-log-2", front: "Hur ser du loggar för specifik tjänst?", back: "journalctl -u tjänstnamn", category: "Loggar", difficulty: "G" },
    { id: "fc-log-3", front: "Hur följer du loggar i realtid?", back: "journalctl -f (follow)", category: "Loggar", difficulty: "G" },
    { id: "fc-log-4", front: "Hur ser du loggar från senaste booten?", back: "journalctl -b", category: "Loggar", difficulty: "G" },
    { id: "fc-log-5", front: "Hur ser du endast error-loggar?", back: "journalctl -p err", category: "Loggar", difficulty: "VG" },
    { id: "fc-log-6", front: "Hur ser du loggar sedan specifik tid?", back: "journalctl --since '1 hour ago'", category: "Loggar", difficulty: "VG" },
    { id: "fc-log-7", front: "Hur ser du kernel-loggar?", back: "dmesg eller journalctl -k", category: "Loggar", difficulty: "VG" },
    { id: "fc-log-8", front: "Var finns systemloggar traditionellt?", back: "/var/log/ (syslog, auth.log, etc.)", category: "Loggar", difficulty: "G" },
    { id: "fc-log-9", front: "Hur tömmer du journald-loggar?", back: "journalctl --vacuum-time=7d", category: "Loggar", difficulty: "VG" },
    { id: "fc-log-10", front: "Hur visar du logg-storlek?", back: "journalctl --disk-usage", category: "Loggar", difficulty: "VG" },
];

// ============================================================================
// SSH & NÄTVERK FLASHCARDS
// ============================================================================
const SSH_NETWORK_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-ssh-1", front: "Hur ansluter du via SSH?", back: "ssh användare@host", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-2", front: "Hur SSH:ar du med specifik port?", back: "ssh -p PORT användare@host", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-3", front: "Hur SSH:ar du med nyckel?", back: "ssh -i ~/.ssh/privat_nyckel användare@host", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-4", front: "Hur genererar du SSH-nycklar?", back: "ssh-keygen -t ed25519 (eller -t rsa -b 4096)", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-5", front: "Hur kopierar du nyckel till server?", back: "ssh-copy-id användare@host", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-6", front: "Var finns SSH-konfiguration?", back: "~/.ssh/config för klient, /etc/ssh/sshd_config för server", category: "SSH", difficulty: "VG" },
    { id: "fc-ssh-7", front: "Hur kopierar du fil via SSH?", back: "scp källa användare@host:/mål", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-8", front: "Hur kopierar du katalog med scp?", back: "scp -r katalog användare@host:/mål", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-9", front: "Vad är rsync bra för?", back: "Effektiv synkronisering - kopierar bara ändringar", category: "SSH", difficulty: "G" },
    { id: "fc-ssh-10", front: "Hur synkar du med rsync över SSH?", back: "rsync -avz källa användare@host:/mål", category: "SSH", difficulty: "VG" },
    { id: "fc-ssh-11", front: "Hur skapar du SSH-tunnel (port forwarding)?", back: "ssh -L lokalport:host:remotport server", category: "SSH", difficulty: "VG" },
    { id: "fc-ssh-12", front: "Hur laddar du ner fil med curl?", back: "curl -O URL", category: "Nätverk", difficulty: "G" },
    { id: "fc-ssh-13", front: "Hur laddar du ner med wget?", back: "wget URL", category: "Nätverk", difficulty: "G" },
    { id: "fc-ssh-14", front: "Hur testar du om port är öppen?", back: "nc -zv host port (netcat)", category: "Nätverk", difficulty: "VG" },
    { id: "fc-ssh-15", front: "Hur ser du routing-tabell?", back: "ip route eller route -n", category: "Nätverk", difficulty: "VG" },
];

// ============================================================================
// ANVÄNDARE & BEHÖRIGHETER FLASHCARDS
// ============================================================================
const USER_PERMISSIONS_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-usr-1", front: "Hur skapar du ny användare?", back: "useradd -m användarnamn (-m skapar hemkatalog)", category: "Användare", difficulty: "G" },
    { id: "fc-usr-2", front: "Hur sätter du lösenord?", back: "passwd användarnamn", category: "Användare", difficulty: "G" },
    { id: "fc-usr-3", front: "Hur tar du bort användare?", back: "userdel användarnamn (userdel -r tar bort hemkatalog)", category: "Användare", difficulty: "G" },
    { id: "fc-usr-4", front: "Hur lägger du till användare i grupp?", back: "usermod -aG grupp användare", category: "Användare", difficulty: "G" },
    { id: "fc-usr-5", front: "Hur skapar du en grupp?", back: "groupadd gruppnamn", category: "Användare", difficulty: "G" },
    { id: "fc-usr-6", front: "Hur byter du till annan användare?", back: "su - användarnamn", category: "Användare", difficulty: "G" },
    { id: "fc-usr-7", front: "Hur kör du kommando som root?", back: "sudo kommando", category: "Permissions", difficulty: "G" },
    { id: "fc-usr-8", front: "Hur ändrar du filägare?", back: "chown användare:grupp fil", category: "Permissions", difficulty: "G" },
    { id: "fc-usr-9", front: "Hur ändrar du filrättigheter?", back: "chmod permissions fil (ex: chmod 755 fil)", category: "Permissions", difficulty: "G" },
    { id: "fc-usr-10", front: "Vad betyder 755 i chmod?", back: "rwx för ägare (7), rx för grupp (5), rx för andra (5)", category: "Permissions", difficulty: "G" },
    { id: "fc-usr-11", front: "Vad betyder rwx?", back: "r=read(4), w=write(2), x=execute(1)", category: "Permissions", difficulty: "G" },
    { id: "fc-usr-12", front: "Hur gör du fil körbar?", back: "chmod +x fil", category: "Permissions", difficulty: "G" },
    { id: "fc-usr-13", front: "Var konfigureras sudo-access?", back: "/etc/sudoers (redigera med visudo)", category: "Permissions", difficulty: "VG" },
    { id: "fc-usr-14", front: "Var finns användarinfo?", back: "/etc/passwd", category: "Användare", difficulty: "G" },
    { id: "fc-usr-15", front: "Var finns gruppinfo?", back: "/etc/group", category: "Användare", difficulty: "G" },
];

// ============================================================================
// DOCKER FLASHCARDS
// ============================================================================
const DOCKER_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-doc-1", front: "Hur startar du container från image?", back: "docker run image", category: "Docker", difficulty: "G" },
    { id: "fc-doc-2", front: "Hur listar du körande containers?", back: "docker ps", category: "Docker", difficulty: "G" },
    { id: "fc-doc-3", front: "Hur listar du ALLA containers?", back: "docker ps -a (all)", category: "Docker", difficulty: "G" },
    { id: "fc-doc-4", front: "Hur stoppar du container?", back: "docker stop ID/NAME", category: "Docker", difficulty: "G" },
    { id: "fc-doc-5", front: "Hur tar du bort container?", back: "docker rm ID/NAME", category: "Docker", difficulty: "G" },
    { id: "fc-doc-6", front: "Hur listar du images?", back: "docker images eller docker image ls", category: "Docker", difficulty: "G" },
    { id: "fc-doc-7", front: "Hur laddar du ner image?", back: "docker pull image:tag", category: "Docker", difficulty: "G" },
    { id: "fc-doc-8", front: "Hur kör du container i bakgrunden?", back: "docker run -d image (detached)", category: "Docker", difficulty: "G" },
    { id: "fc-doc-9", front: "Hur ser du container-loggar?", back: "docker logs ID/NAME", category: "Docker", difficulty: "G" },
    { id: "fc-doc-10", front: "Hur tar du bort image?", back: "docker rmi image", category: "Docker", difficulty: "G" },
    { id: "fc-doc-11", front: "Hur kör du kommando i körande container?", back: "docker exec -it ID/NAME kommando", category: "Docker", difficulty: "G" },
    { id: "fc-doc-12", front: "Vad gör -it i docker exec/run?", back: "-i=interactive, -t=tty (terminal)", category: "Docker", difficulty: "G" },
    { id: "fc-doc-13", front: "Hur publicerar du port?", back: "docker run -p hostport:containerport", category: "Docker", difficulty: "G" },
    { id: "fc-doc-14", front: "Hur monterar du volym?", back: "docker run -v /host:/container", category: "Docker", difficulty: "G" },
    { id: "fc-doc-15", front: "Hur bygger du image från Dockerfile?", back: "docker build -t namn:tag .", category: "Docker", difficulty: "G" },
    { id: "fc-doc-16", front: "Vad gör docker-compose up?", back: "Startar alla tjänster i docker-compose.yml", category: "Docker", difficulty: "G" },
    { id: "fc-doc-17", front: "Hur startar du compose i bakgrunden?", back: "docker-compose up -d", category: "Docker", difficulty: "G" },
    { id: "fc-doc-18", front: "Hur stoppar du compose?", back: "docker-compose down", category: "Docker", difficulty: "G" },
    { id: "fc-doc-19", front: "Hur ser du container resursanvändning?", back: "docker stats", category: "Docker", difficulty: "G" },
    { id: "fc-doc-20", front: "Hur rensar du oanvända resurser?", back: "docker system prune", category: "Docker", difficulty: "VG" },
    { id: "fc-doc-21", front: "Hur skapar du named volume?", back: "docker volume create namn", category: "Docker", difficulty: "VG" },
    { id: "fc-doc-22", front: "Hur skapar du nätverk?", back: "docker network create namn", category: "Docker", difficulty: "VG" },
    { id: "fc-doc-23", front: "Vad gör --rm flaggan?", back: "Tar bort container automatiskt efter stopp", category: "Docker", difficulty: "VG" },
    { id: "fc-doc-24", front: "Hur inspekterar du container?", back: "docker inspect ID/NAME", category: "Docker", difficulty: "VG" },
    { id: "fc-doc-25", front: "Hur kopierar du fil från container?", back: "docker cp container:/path /host/path", category: "Docker", difficulty: "VG" },
];

// ============================================================================
// BLOCK STORAGE & LVM FLASHCARDS
// ============================================================================
const STORAGE_LVM_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-sto-1", front: "Hur listar du blockenheter?", back: "lsblk", category: "Storage", difficulty: "G" },
    { id: "fc-sto-2", front: "Vad är /dev/sda?", back: "Första SATA/SCSI-disken", category: "Storage", difficulty: "G" },
    { id: "fc-sto-3", front: "Vad är /dev/sda1?", back: "Första partitionen på disk sda", category: "Storage", difficulty: "G" },
    { id: "fc-sto-4", front: "Hur partitionerar du disk?", back: "fdisk /dev/sdX", category: "Storage", difficulty: "G" },
    { id: "fc-sto-5", front: "Hur skapar du ext4-filsystem?", back: "mkfs.ext4 /dev/sdX1", category: "Storage", difficulty: "G" },
    { id: "fc-sto-6", front: "Hur monterar du partition?", back: "mount /dev/sdX1 /mnt", category: "Storage", difficulty: "G" },
    { id: "fc-sto-7", front: "Hur avmonterar du?", back: "umount /mnt (utan n!)", category: "Storage", difficulty: "G" },
    { id: "fc-sto-8", front: "Var konfigureras automatisk mount?", back: "/etc/fstab", category: "Storage", difficulty: "G" },
    { id: "fc-sto-9", front: "Hur hittar du UUID?", back: "blkid eller lsblk -f", category: "Storage", difficulty: "G" },
    { id: "fc-sto-10", front: "Vad är LVM?", back: "Logical Volume Manager - flexibel volymhantering", category: "LVM", difficulty: "G" },
    { id: "fc-sto-11", front: "LVM-hierarkin?", back: "PV (Physical Volume) → VG (Volume Group) → LV (Logical Volume)", category: "LVM", difficulty: "G" },
    { id: "fc-sto-12", front: "Hur skapar du Physical Volume?", back: "pvcreate /dev/sdX", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-13", front: "Hur skapar du Volume Group?", back: "vgcreate vgnamn /dev/sdX", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-14", front: "Hur skapar du Logical Volume?", back: "lvcreate -n lvnamn -L 10G vgnamn", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-15", front: "Hur utökar du LV?", back: "lvextend -L +5G /dev/vg/lv", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-16", front: "Vad måste du göra efter lvextend?", back: "Utöka filsystemet: resize2fs (ext4) eller xfs_growfs", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-17", front: "Hur visar du PVs?", back: "pvs eller pvdisplay", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-18", front: "Hur visar du VGs?", back: "vgs eller vgdisplay", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-19", front: "Hur visar du LVs?", back: "lvs eller lvdisplay", category: "LVM", difficulty: "VG" },
    { id: "fc-sto-20", front: "Hur krypterar du partition med LUKS?", back: "cryptsetup luksFormat /dev/sdX", category: "Kryptering", difficulty: "VG" },
    { id: "fc-sto-21", front: "Hur öppnar du LUKS-krypterad enhet?", back: "cryptsetup open /dev/sdX namn", category: "Kryptering", difficulty: "VG" },
    { id: "fc-sto-22", front: "Var finns öppnade LUKS-enheter?", back: "/dev/mapper/namn", category: "Kryptering", difficulty: "VG" },
];

// ============================================================================
// BRANDVÄGG FLASHCARDS
// ============================================================================
const FIREWALL_FLASHCARDS: CommandFlashcard[] = [
    { id: "fc-fw-1", front: "Hur aktiverar du UFW?", back: "ufw enable", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-2", front: "Hur inaktiverar du UFW?", back: "ufw disable", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-3", front: "Hur ser du UFW-status?", back: "ufw status", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-4", front: "Hur tillåter du SSH?", back: "ufw allow ssh (eller ufw allow 22)", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-5", front: "Hur tillåter du specifik port?", back: "ufw allow PORT", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-6", front: "Hur blockerar du port?", back: "ufw deny PORT", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-7", front: "Hur tar du bort UFW-regel?", back: "ufw delete allow 22", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-8", front: "Hur sätter du default deny?", back: "ufw default deny incoming", category: "Firewall", difficulty: "G" },
    { id: "fc-fw-9", front: "Hur tillåter du från specifik IP?", back: "ufw allow from IP_ADDRESS", category: "Firewall", difficulty: "VG" },
    { id: "fc-fw-10", front: "Hur visar du regler med nummer?", back: "ufw status numbered", category: "Firewall", difficulty: "VG" },
    { id: "fc-fw-11", front: "Hur tar du bort regel nummer 3?", back: "ufw delete 3", category: "Firewall", difficulty: "VG" },
    { id: "fc-fw-12", front: "Vad är firewall-cmd?", back: "CLI för firewalld på RHEL/CentOS", category: "Firewall", difficulty: "VG" },
    { id: "fc-fw-13", front: "Hur öppnar du port permanent i firewalld?", back: "firewall-cmd --add-port=80/tcp --permanent", category: "Firewall", difficulty: "VG" },
    { id: "fc-fw-14", front: "Vad krävs efter --permanent?", back: "firewall-cmd --reload", category: "Firewall", difficulty: "VG" },
    { id: "fc-fw-15", front: "Hur skapar du rate limiting?", back: "ufw limit ssh", category: "Firewall", difficulty: "VG" },
];

// ============================================================================
// KOMBINERAD EXPORT
// ============================================================================

export const LINUX_COMMANDS_FLASHCARD_SETS: CommandFlashcardSet[] = [
    {
        taskId: "linux-cmd-navigation",
        taskTitle: "Navigation & Filsystem",
        flashcards: NAVIGATION_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-text",
        taskTitle: "Textbearbetning & Sökning",
        flashcards: TEXT_PROCESSING_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-process",
        taskTitle: "Processhantering",
        flashcards: PROCESS_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-system",
        taskTitle: "Systeminformation",
        flashcards: SYSTEM_INFO_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-logs",
        taskTitle: "Logghantering",
        flashcards: LOG_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-ssh",
        taskTitle: "SSH & Nätverk",
        flashcards: SSH_NETWORK_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-users",
        taskTitle: "Användare & Behörigheter",
        flashcards: USER_PERMISSIONS_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-docker",
        taskTitle: "Docker & Containers",
        flashcards: DOCKER_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-storage",
        taskTitle: "Block Storage & LVM",
        flashcards: STORAGE_LVM_FLASHCARDS,
    },
    {
        taskId: "linux-cmd-firewall",
        taskTitle: "Brandvägg & Säkerhet",
        flashcards: FIREWALL_FLASHCARDS,
    },
];

// All flashcards combined
export const ALL_LINUX_COMMAND_FLASHCARDS: CommandFlashcard[] = [
    ...NAVIGATION_FLASHCARDS,
    ...TEXT_PROCESSING_FLASHCARDS,
    ...PROCESS_FLASHCARDS,
    ...SYSTEM_INFO_FLASHCARDS,
    ...LOG_FLASHCARDS,
    ...SSH_NETWORK_FLASHCARDS,
    ...USER_PERMISSIONS_FLASHCARDS,
    ...DOCKER_FLASHCARDS,
    ...STORAGE_LVM_FLASHCARDS,
    ...FIREWALL_FLASHCARDS,
];

// Stats
export const LINUX_COMMANDS_FLASHCARD_STATS = {
    totalFlashcards: ALL_LINUX_COMMAND_FLASHCARDS.length,
    byDifficulty: {
        G: ALL_LINUX_COMMAND_FLASHCARDS.filter(f => f.difficulty === "G").length,
        VG: ALL_LINUX_COMMAND_FLASHCARDS.filter(f => f.difficulty === "VG").length,
    },
    categories: LINUX_COMMANDS_FLASHCARD_SETS.map(s => ({
        id: s.taskId,
        name: s.taskTitle,
        count: s.flashcards.length,
    })),
};
