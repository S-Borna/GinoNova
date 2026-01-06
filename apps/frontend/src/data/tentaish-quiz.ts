/**
 * TENTAISH - Linux DevOps Tenta Quiz
 * 100 quiz-frågor baserade på verklig tentamaterial
 * Täcker: Filsystem, Användare, Paket, SSH, Docker, Disk, Subnetting
 *
 * Skapad: 2026-01-06
 */

export interface TentaishQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    scenario?: string
}

export interface TentaishQuizSet {
    taskId: string
    taskTitle: string
    questions: TentaishQuestion[]
}

// =============================================================================
// FILSYSTEM & GRUNDLÄGGANDE (15 frågor)
// =============================================================================

const FILSYSTEM_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-fs-1',
        question: 'Vad visar kommandot "pwd"?',
        options: ['Användarlistan', 'Nuvarande mapp (working directory)', 'Disk-utrymme', 'Process-lista'],
        correctIndex: 1,
        explanation: 'pwd = Print Working Directory, visar den aktuella katalogen du befinner dig i.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'tent-fs-2',
        question: 'Vad är skillnaden mellan absolut och relativ sökväg?',
        options: [
            'Ingen skillnad',
            'Absolut börjar med /, relativ utgår från nuvarande position',
            'Relativ börjar med /, absolut använder ~',
            'Absolut är längre'
        ],
        correctIndex: 1,
        explanation: 'Absolut path börjar från root (/), t.ex. /home/user. Relativ utgår från där du är, t.ex. ./folder.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'tent-fs-3',
        question: 'Vad gör "cd .."?',
        options: ['Går till hemkatalogen', 'Går upp en nivå i katalogstrukturen', 'Visar dolda filer', 'Skapar en mapp'],
        correctIndex: 1,
        explanation: '.. refererar till föräldrakatalogen (parent directory). cd .. går alltså upp en nivå.',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'tent-fs-4',
        question: 'Vad gör "ls -la"?',
        options: [
            'Listar bara dolda filer',
            'Listar alla filer inklusive dolda med detaljer',
            'Listar bara kataloger',
            'Sorterar efter storlek'
        ],
        correctIndex: 1,
        explanation: '-l = long format (detaljer), -a = all (inklusive dolda filer som börjar med .).',
        difficulty: 'G',
        category: 'Navigering'
    },
    {
        id: 'tent-fs-5',
        question: 'Var finns konfigurationsfiler i Linux?',
        options: ['/home', '/etc', '/tmp', '/var'],
        correctIndex: 1,
        explanation: '/etc innehåller systemkonfigurationsfiler. Exempel: /etc/ssh/sshd_config.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'tent-fs-6',
        question: 'Var lagras loggfiler i Linux?',
        options: ['/log', '/var/log', '/etc/log', '/home/log'],
        correctIndex: 1,
        explanation: '/var/log innehåller systemloggar som syslog, auth.log, messages.',
        difficulty: 'G',
        category: 'Viktiga Paths'
    },
    {
        id: 'tent-fs-7',
        question: 'Vad gör "mkdir -p a/b/c"?',
        options: [
            'Skapar bara mappen c',
            'Skapar hela katalogstrukturen rekursivt',
            'Ger fel om a inte finns',
            'Tar bort mapparna'
        ],
        correctIndex: 1,
        explanation: '-p (parents) skapar alla föräldrakataloger som behövs. Utan -p får du fel om a/ inte finns.',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-8',
        question: 'Vad gör "rm -rf"?',
        options: [
            'Raderar en fil med bekräftelse',
            'Raderar rekursivt och tvingar utan bekräftelse',
            'Flyttar till papperskorgen',
            'Byter namn på filer'
        ],
        correctIndex: 1,
        explanation: '-r = recursive (inkl mappar), -f = force (ingen bekräftelse). VARNING: Mycket farligt!',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-9',
        question: 'Hur kopierar du en fil?',
        options: ['mv src dst', 'cp src dst', 'copy src dst', 'duplicate src dst'],
        correctIndex: 1,
        explanation: 'cp (copy) kopierar filer. mv flyttar/byter namn. cp -r för kataloger.',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-10',
        question: 'Vad gör "touch filename"?',
        options: [
            'Tar bort filen',
            'Skapar en tom fil eller uppdaterar tidsstämpel',
            'Visar filinnehåll',
            'Ändrar filrättigheter'
        ],
        correctIndex: 1,
        explanation: 'touch skapar en tom fil om den inte finns, eller uppdaterar tidsstämpeln om den finns.',
        difficulty: 'G',
        category: 'Filhantering'
    },
    {
        id: 'tent-fs-11',
        question: 'I Vim, hur går du till insert mode?',
        options: ['Tryck ESC', 'Tryck i', 'Tryck :w', 'Tryck q'],
        correctIndex: 1,
        explanation: 'i = insert mode för att skriva. ESC = tillbaka till normal mode.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'tent-fs-12',
        question: 'I Vim, hur sparar och avslutar du?',
        options: [':q', ':w', ':wq', ':x!'],
        correctIndex: 2,
        explanation: ':wq = write (spara) + quit (avsluta). :q! avslutar utan att spara.',
        difficulty: 'G',
        category: 'Vim'
    },
    {
        id: 'tent-fs-13',
        question: 'Vad visar "man ls"?',
        options: ['Alla filer', 'Manualsidan för ls-kommandot', 'Diskutrymme', 'Systeminfo'],
        correctIndex: 1,
        explanation: 'man (manual) visar dokumentation för kommandon. Använd q för att avsluta.',
        difficulty: 'G',
        category: 'Dokumentation'
    },
    {
        id: 'tent-fs-14',
        question: 'Vad är skillnaden mellan "cat" och "less"?',
        options: [
            'Ingen skillnad',
            'cat visar allt på en gång, less låter dig bläddra',
            'less är snabbare',
            'cat fungerar bara på små filer'
        ],
        correctIndex: 1,
        explanation: 'cat dumpar hela filen. less är en pager som låter dig scrolla (q för quit).',
        difficulty: 'G',
        category: 'Läsa filer'
    },
    {
        id: 'tent-fs-15',
        question: 'Hur söker du efter filer med namn som slutar på .txt?',
        options: [
            'search *.txt',
            'find -name "*.txt"',
            'grep .txt',
            'locate txt'
        ],
        correctIndex: 1,
        explanation: 'find -name "*.txt" söker efter filer med .txt-extension. Glöm inte citattecken!',
        difficulty: 'G',
        category: 'Sökning'
    }
]

// =============================================================================
// ANVÄNDARHANTERING (15 frågor)
// =============================================================================

const ANVANDARE_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-usr-1',
        question: 'Hur skapar du en ny användare?',
        options: ['adduser user', 'useradd user', 'newuser user', 'createuser user'],
        correctIndex: 1,
        explanation: 'useradd är det grundläggande kommandot. adduser är en mer interaktiv wrapper (Debian).',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'tent-usr-2',
        question: 'Hur lägger du till en användare i en grupp?',
        options: [
            'groupadd user group',
            'usermod -aG grupp användare',
            'addgroup user group',
            'useradd -g user group'
        ],
        correctIndex: 1,
        explanation: 'usermod -aG är korrekt. -a = append (lägg till), -G = supplementary groups. Utan -a ersätts grupperna!',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'tent-usr-3',
        question: 'Varför är flaggan -a viktig i "usermod -aG"?',
        options: [
            'Den är inte viktig',
            'Utan -a ersätts alla befintliga gruppmedlemskap',
            'Den gör kommandot snabbare',
            'Den aktiverar användaren'
        ],
        correctIndex: 1,
        explanation: '-a = append. Utan den raderas användarens befintliga gruppmedlemskap!',
        difficulty: 'VG',
        category: 'Användare'
    },
    {
        id: 'tent-usr-4',
        question: 'Hur sätter du lösenord för en användare?',
        options: ['setpasswd user', 'passwd user', 'password user', 'chpasswd user'],
        correctIndex: 1,
        explanation: 'passwd user sätter eller ändrar lösenord. passwd --expire tvingar byte vid nästa inloggning.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'tent-usr-5',
        question: 'Vad visar kommandot "id user"?',
        options: [
            'Användarens hemkatalog',
            'UID, GID och gruppmedlemskap',
            'Senaste inloggning',
            'Lösenordets ålder'
        ],
        correctIndex: 1,
        explanation: 'id visar användarens UID, primär GID och alla gruppmedlemskap.',
        difficulty: 'G',
        category: 'Användare'
    },
    {
        id: 'tent-usr-6',
        question: 'Vad betyder chmod 770?',
        options: [
            'rwx för alla',
            'rwx för owner och group, inget för other',
            'rw för alla',
            'Endast läsning'
        ],
        correctIndex: 1,
        explanation: '7=rwx (4+2+1), 7=rwx, 0=--- Alltså: owner och group får full access, andra inget.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-usr-7',
        question: 'Vad gör SGID (Set Group ID) på en katalog?',
        options: [
            'Ger alla fulla rättigheter',
            'Filer skapade i katalogen ärver katalogensgrupp',
            'Krypterar katalogen',
            'Gör katalogen skrivskyddad'
        ],
        correctIndex: 1,
        explanation: 'SGID (chmod g+s) gör att nya filer/mappar ärver gruppägandet istället för skaparens primära grupp.',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'tent-usr-8',
        question: 'Hur sätter du SGID med oktalt läge?',
        options: ['chmod 770', 'chmod 2770', 'chmod 4770', 'chmod 1770'],
        correctIndex: 1,
        explanation: '2xxx = SGID. chmod 2770 = SGID + rwxrwx---. (4xxx = SUID, 1xxx = sticky bit)',
        difficulty: 'VG',
        category: 'Permissions'
    },
    {
        id: 'tent-usr-9',
        question: 'Vad gör "chown user:group file"?',
        options: [
            'Ändrar bara ägare',
            'Ändrar både ägare och grupp',
            'Ändrar bara grupp',
            'Ändrar permissions'
        ],
        correctIndex: 1,
        explanation: 'chown user:group ändrar både ägare och gruppägare. Använd chgrp för bara grupp.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-usr-10',
        question: 'Vad betyder siffran 6 i chmod?',
        options: ['r-x (read + execute)', 'rw- (read + write)', 'rwx (allt)', '-wx (write + execute)'],
        correctIndex: 1,
        explanation: '6 = 4 + 2 = r + w = rw-. (4=read, 2=write, 1=execute)',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-usr-11',
        question: 'Vilken siffra betyder "read + execute"?',
        options: ['3', '5', '6', '7'],
        correctIndex: 1,
        explanation: '5 = 4 + 1 = read + execute = r-x.',
        difficulty: 'G',
        category: 'Permissions'
    },
    {
        id: 'tent-usr-12',
        question: 'Hur tvingar du en användare att byta lösenord vid nästa inloggning?',
        options: [
            'passwd --force user',
            'passwd --expire user',
            'usermod --expire user',
            'chage -f user'
        ],
        correctIndex: 1,
        explanation: 'passwd --expire user eller chage -d 0 user tvingar lösenordsbyte vid nästa inloggning.',
        difficulty: 'VG',
        category: 'Användare'
    },
    {
        id: 'tent-usr-13',
        question: 'Hur skapar du en ny grupp?',
        options: ['addgroup grp', 'groupadd grp', 'newgroup grp', 'mkgroup grp'],
        correctIndex: 1,
        explanation: 'groupadd skapar en ny grupp. gpasswd -a user group lägger till användare.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'tent-usr-14',
        question: 'Vad visar "groups user"?',
        options: [
            'Alla grupper i systemet',
            'Vilka grupper användaren tillhör',
            'Gruppens medlemmar',
            'Senast skapade grupper'
        ],
        correctIndex: 1,
        explanation: 'groups user listar alla grupper som användaren är medlem i.',
        difficulty: 'G',
        category: 'Grupper'
    },
    {
        id: 'tent-usr-15',
        question: 'Vad betyder "d" i början av "drwxr-xr-x"?',
        options: ['Disk', 'Directory (katalog)', 'Device', 'Default'],
        correctIndex: 1,
        explanation: 'd = directory. - = vanlig fil, l = symbolic link, b = block device.',
        difficulty: 'G',
        category: 'Permissions'
    }
]

// =============================================================================
// PAKETHANTERING (12 frågor)
// =============================================================================

const PAKET_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-pkg-1',
        question: 'Vad gör "apt update" i Ubuntu?',
        options: [
            'Uppgraderar alla paket',
            'Uppdaterar paketlistorna (metadata)',
            'Installerar uppdateringar',
            'Tar bort gamla paket'
        ],
        correctIndex: 1,
        explanation: 'apt update laddar ner senaste paketlistorna. apt upgrade installerar uppdateringar.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-2',
        question: 'Vad är skillnaden mellan APT och DPKG?',
        options: [
            'Ingen skillnad',
            'APT hanterar dependencies automatiskt, DPKG gör inte det',
            'DPKG är nyare',
            'APT är bara för Fedora'
        ],
        correctIndex: 1,
        explanation: 'APT är högnivå (löser dependencies). DPKG är lågnivå (hanterar .deb-filer direkt).',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-3',
        question: 'Hur installerar du en .deb-fil manuellt?',
        options: ['apt install file.deb', 'dpkg -i file.deb', 'install file.deb', 'deb -install file.deb'],
        correctIndex: 1,
        explanation: 'dpkg -i (--install) installerar .deb-filer. Löser INTE dependencies automatiskt!',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-4',
        question: 'Vilken pakethanterare används i Fedora?',
        options: ['APT', 'DNF', 'Pacman', 'Zypper'],
        correctIndex: 1,
        explanation: 'DNF (Dandified YUM) är pakethanteraren för Fedora/RHEL. Hanterar .rpm-filer.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-5',
        question: 'Vad gör "dnf check-upgrade"?',
        options: [
            'Installerar uppgraderingar',
            'Visar tillgängliga uppgraderingar',
            'Tar bort gamla paket',
            'Uppdaterar metadata'
        ],
        correctIndex: 1,
        explanation: 'dnf check-upgrade visar vilka paket som kan uppgraderas. dnf upgrade installerar dem.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-6',
        question: 'Hur installerar du en .rpm-fil manuellt?',
        options: ['dnf install file.rpm', 'rpm -ivh file.rpm', 'yum file.rpm', 'install file.rpm'],
        correctIndex: 1,
        explanation: 'rpm -ivh: -i = install, -v = verbose, -h = progress hash. Löser INTE dependencies!',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-7',
        question: 'Vad visar "echo $?"?',
        options: ['Senaste kommandot', 'Exit code från senaste kommando', 'Processens PID', 'Användarnamn'],
        correctIndex: 1,
        explanation: '$? innehåller exit code. 0 = success, annat = fel. Viktigt för skriptning!',
        difficulty: 'G',
        category: 'Allmänt'
    },
    {
        id: 'tent-pkg-8',
        question: 'Vad gör "apt autoremove"?',
        options: [
            'Tar bort alla paket',
            'Tar bort oanvända dependencies',
            'Uppdaterar paket',
            'Visar paketinfo'
        ],
        correctIndex: 1,
        explanation: 'autoremove städar bort dependencies som inte längre behövs av något installerat paket.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-9',
        question: 'Hur listar du alla installerade paket i Debian/Ubuntu?',
        options: ['apt list', 'dpkg -l', 'rpm -qa', 'pkg list'],
        correctIndex: 1,
        explanation: 'dpkg -l listar alla installerade paket. apt list --installed fungerar också.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-10',
        question: 'Hur listar du alla installerade paket i Fedora?',
        options: ['dnf list', 'rpm -qa', 'yum list', 'dpkg -l'],
        correctIndex: 1,
        explanation: 'rpm -qa (query all) listar alla installerade RPM-paket.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-11',
        question: 'Efter vilken typ av uppgradering BÖR du starta om?',
        options: ['Applikationsuppgradering', 'Kernel-uppgradering', 'Biblioteksuppgradering', 'Aldrig'],
        correctIndex: 1,
        explanation: 'Kernel-uppgraderingar kräver omstart för att den nya kerneln ska laddas.',
        difficulty: 'VG',
        category: 'Allmänt'
    },
    {
        id: 'tent-pkg-12',
        question: 'Vad gör "dnf -y upgrade"?',
        options: [
            'Frågar om bekräftelse',
            'Uppgraderar utan att fråga (auto-yes)',
            'Visar bara vad som skulle uppgraderas',
            'Avbryter uppgradering'
        ],
        correctIndex: 1,
        explanation: '-y = automatic yes. Användbart i skript men var försiktig!',
        difficulty: 'G',
        category: 'DNF'
    }
]

// =============================================================================
// SSH & BRANDVÄGG (15 frågor)
// =============================================================================

const SSH_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-ssh-1',
        question: 'Hur genererar du en Ed25519 SSH-nyckel?',
        options: [
            'ssh-create -t ed25519',
            'ssh-keygen -t ed25519',
            'generate-key ed25519',
            'openssl keygen ed25519'
        ],
        correctIndex: 1,
        explanation: 'ssh-keygen -t ed25519 skapar ett Ed25519-nyckelpar. Modernare och säkrare än RSA.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'tent-ssh-2',
        question: 'Vilken fil innehåller din PRIVATA SSH-nyckel?',
        options: ['~/.ssh/id_ed25519.pub', '~/.ssh/id_ed25519', '~/.ssh/authorized_keys', '~/.ssh/known_hosts'],
        correctIndex: 1,
        explanation: 'Privata nyckeln har INGET .pub suffix. DELA ALDRIG den privata nyckeln!',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'tent-ssh-3',
        question: 'Var lagras godkända publika nycklar på servern?',
        options: [
            '~/.ssh/id_ed25519.pub',
            '~/.ssh/authorized_keys',
            '/etc/ssh/public_keys',
            '~/.ssh/known_hosts'
        ],
        correctIndex: 1,
        explanation: 'authorized_keys innehåller publika nycklar som får logga in. En nyckel per rad.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'tent-ssh-4',
        question: 'Hur kopierar du din nyckel till en server?',
        options: [
            'scp ~/.ssh/id_ed25519 user@host:',
            'ssh-copy-id user@host',
            'ssh-import user@host',
            'copy-key user@host'
        ],
        correctIndex: 1,
        explanation: 'ssh-copy-id kopierar din publika nyckel till serverns authorized_keys automatiskt.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'tent-ssh-5',
        question: 'Vilka permissions ska ~/.ssh-mappen ha?',
        options: ['755', '777', '700', '644'],
        correctIndex: 2,
        explanation: '~/.ssh ska ha 700 (rwx------). authorized_keys ska ha 600. SSH vägrar annars!',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'tent-ssh-6',
        question: 'Vad är en passphrase för SSH-nycklar?',
        options: [
            'Serverns lösenord',
            'Extra lösenord som krypterar den privata nyckeln',
            'Användarnamnet',
            'Nätverkslösenord'
        ],
        correctIndex: 1,
        explanation: 'Passphrase krypterar den privata nyckeln. Extra säkerhetslager om nyckeln stjäls.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'tent-ssh-7',
        question: 'Var konfigurerar du SSH-serverns inställningar?',
        options: [
            '~/.ssh/config',
            '/etc/ssh/sshd_config',
            '/etc/ssh/ssh_config',
            '~/.ssh/server.conf'
        ],
        correctIndex: 1,
        explanation: 'sshd_config = server daemon config. ssh_config = client config. ~/.ssh/config = per-user client.',
        difficulty: 'G',
        category: 'SSH Config'
    },
    {
        id: 'tent-ssh-8',
        question: 'Vilken inställning inaktiverar lösenordsinloggning?',
        options: [
            'DisablePassword yes',
            'PasswordAuthentication no',
            'NoPassword true',
            'PasswordLogin off'
        ],
        correctIndex: 1,
        explanation: 'PasswordAuthentication no i sshd_config tvingar nyckelbaserad inloggning.',
        difficulty: 'G',
        category: 'SSH Hardening'
    },
    {
        id: 'tent-ssh-9',
        question: 'Hur startar du om SSH-tjänsten i Ubuntu?',
        options: [
            'systemctl restart sshd.service',
            'systemctl restart ssh.service',
            'service ssh reload',
            '/etc/init.d/ssh restart'
        ],
        correctIndex: 1,
        explanation: 'Ubuntu använder ssh.service. Fedora/RHEL använder sshd.service.',
        difficulty: 'G',
        category: 'SSH Config'
    },
    {
        id: 'tent-ssh-10',
        question: 'Hur kontrollerar du vilken port SSH lyssnar på?',
        options: [
            'ssh --port',
            'ss -tulpn | grep ssh',
            'port ssh',
            'netstat ssh'
        ],
        correctIndex: 1,
        explanation: 'ss -tulpn visar lyssnandeportar. grep ssh filtrerar SSH-tjänsten.',
        difficulty: 'G',
        category: 'SSH Config'
    },
    {
        id: 'tent-ssh-11',
        question: 'Hur tillåter du port 22 i UFW (Ubuntu)?',
        options: ['ufw enable 22', 'ufw allow 22', 'ufw open 22', 'ufw add 22'],
        correctIndex: 1,
        explanation: 'ufw allow 22 tillåter trafik på port 22. VIKTIGT: Gör detta INNAN ufw enable!',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-12',
        question: 'Vad MÅSTE du göra innan "ufw enable"?',
        options: [
            'Starta om servern',
            'Tillåta SSH-port (ufw allow 22)',
            'Inaktivera SELinux',
            'Logga ut'
        ],
        correctIndex: 1,
        explanation: 'Om du aktiverar UFW utan att tillåta SSH låser du ut dig själv!',
        difficulty: 'VG',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-13',
        question: 'Hur lägger du till en port i firewalld (Fedora)?',
        options: [
            'firewalld add 22',
            'firewall-cmd --add-port=22/tcp --permanent',
            'firewall allow 22',
            'iptables -A 22'
        ],
        correctIndex: 1,
        explanation: '--permanent gör regeln bestående. Glöm inte firewall-cmd --reload efteråt!',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-14',
        question: 'Vad gör "firewall-cmd --reload"?',
        options: [
            'Startar om brandväggen helt',
            'Laddar om konfiguration utan att tappa connections',
            'Återställer till default',
            'Visar status'
        ],
        correctIndex: 1,
        explanation: '--reload applicerar nya permanenta regler utan att avbryta befintliga anslutningar.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-15',
        question: 'Vad är bästa praxis vid SSH-portbyte?',
        options: [
            'Ändra och starta om direkt',
            'Öppna ny port i brandvägg, testa, stäng sedan gammal port',
            'Stäng gammal port först',
            'Inaktivera brandväggen'
        ],
        correctIndex: 1,
        explanation: 'Öppna nya porten FÖRST, testa att det fungerar, stäng sedan gamla. Annars låses du ute!',
        difficulty: 'VG',
        category: 'Brandvägg'
    }
]

// =============================================================================
// DOCKER (15 frågor)
// =============================================================================

const DOCKER_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-docker-1',
        question: 'Vad är skillnaden mellan en Docker image och container?',
        options: [
            'Ingen skillnad',
            'Image är mall/blueprint, container är körande instans',
            'Container är större',
            'Image körs, container lagras'
        ],
        correctIndex: 1,
        explanation: 'Image = statisk mall. Container = körande process baserad på imagen.',
        difficulty: 'G',
        category: 'Koncept'
    },
    {
        id: 'tent-docker-2',
        question: 'Vad gör "docker run -it ubuntu"?',
        options: [
            'Laddar ner Ubuntu',
            'Startar interaktiv container med terminal',
            'Bygger en image',
            'Listar containers'
        ],
        correctIndex: 1,
        explanation: '-i = interactive (stdin öppen), -t = TTY (terminal). Tillsammans ger det en shell-session.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-3',
        question: 'Vad gör flaggan --rm i docker run?',
        options: [
            'Tar bort imagen',
            'Tar bort containern automatiskt när den avslutas',
            'Startar om containern',
            'Körs som root'
        ],
        correctIndex: 1,
        explanation: '--rm = auto-remove. Containern raderas när den stoppar. Bra för test!',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-4',
        question: 'Vad gör "docker ps"?',
        options: [
            'Visar alla images',
            'Visar körande containers',
            'Visar processer i container',
            'Visar portar'
        ],
        correctIndex: 1,
        explanation: 'docker ps visar körande containers. docker ps -a visar ALLA (även stoppade).',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-5',
        question: 'Hur kör du en container i bakgrunden (detached)?',
        options: ['docker run -b', 'docker run -d', 'docker run --background', 'docker run &'],
        correctIndex: 1,
        explanation: '-d = detached mode. Containern körs i bakgrunden, du får tillbaka prompten.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-6',
        question: 'Hur mappar du port 80 i container till port 8080 på host?',
        options: [
            'docker run -p 80:8080',
            'docker run -p 8080:80',
            'docker run --port 80=8080',
            'docker run -P 8080'
        ],
        correctIndex: 1,
        explanation: 'Format: -p HOST:CONTAINER. Så -p 8080:80 mappar host 8080 till container 80.',
        difficulty: 'VG',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-7',
        question: 'Hur tar du bort alla stoppade containers?',
        options: [
            'docker rm --all',
            'docker container prune',
            'docker clean',
            'docker purge containers'
        ],
        correctIndex: 1,
        explanation: 'docker container prune tar bort alla stoppade containers. Bekräftelse krävs.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-8',
        question: 'Hur tar du bort en image?',
        options: ['docker delete img', 'docker rmi img:tag', 'docker remove img', 'docker image rm img'],
        correctIndex: 1,
        explanation: 'docker rmi (remove image) tar bort images. docker image rm fungerar också.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-9',
        question: 'Vad måste du göra efter "usermod -aG docker $USER"?',
        options: [
            'Starta om docker',
            'Logga ut och in igen',
            'Köra sudo',
            'Ingenting'
        ],
        correctIndex: 1,
        explanation: 'Gruppändringar träder i kraft först vid nästa inloggning!',
        difficulty: 'VG',
        category: 'Installation'
    },
    {
        id: 'tent-docker-10',
        question: 'Vad är en Docker tag?',
        options: [
            'Container-namn',
            'Versionsbeteckning för image (t.ex. python:3.12)',
            'Metadata',
            'Länk till registry'
        ],
        correctIndex: 1,
        explanation: 'Tag anger version. python:3.12-alpine. latest är default om ingen anges.',
        difficulty: 'G',
        category: 'Koncept'
    },
    {
        id: 'tent-docker-11',
        question: 'Vad delar Docker containers med host-systemet?',
        options: ['Inget', 'Kernel', 'Filsystem', 'Användare'],
        correctIndex: 1,
        explanation: 'Containers delar Linux-kerneln med host. Därför är Docker lättare än VM.',
        difficulty: 'VG',
        category: 'Koncept'
    },
    {
        id: 'tent-docker-12',
        question: 'Vad är Docker layers?',
        options: [
            'Säkerhetsnivåer',
            'Delade filsystemlager mellan images',
            'Nätverkslager',
            'Användarnivåer'
        ],
        correctIndex: 1,
        explanation: 'Images byggs i lager. Gemensamma baslager delas mellan images = sparar utrymme.',
        difficulty: 'VG',
        category: 'Koncept'
    },
    {
        id: 'tent-docker-13',
        question: 'Hur ger du en container ett specifikt namn?',
        options: [
            'docker run -n myname',
            'docker run --name myname',
            'docker run myname:image',
            'docker run --label myname'
        ],
        correctIndex: 1,
        explanation: '--name sätter ett specifikt namn istället för slumpmässigt genererat.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-docker-14',
        question: 'Hur kollar du status på Docker-tjänsten?',
        options: [
            'docker status',
            'systemctl status docker.service',
            'docker --status',
            'service docker info'
        ],
        correctIndex: 1,
        explanation: 'systemctl status docker.service visar om Docker daemon körs.',
        difficulty: 'G',
        category: 'Installation'
    },
    {
        id: 'tent-docker-15',
        question: 'Vad betyder "latest" tag?',
        options: [
            'Den senaste stabila versionen alltid',
            'Default tag om ingen anges, inte nödvändigtvis senaste',
            'Betaversion',
            'Äldsta versionen'
        ],
        correctIndex: 1,
        explanation: 'latest är bara default-namn. Det är upp till image-skaparen vad den pekar på!',
        difficulty: 'VG',
        category: 'Koncept'
    }
]

// =============================================================================
// DISK & KRYPTERING (13 frågor)
// =============================================================================

const DISK_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-disk-1',
        question: 'Vilken är korrekt ordning för disk-setup?',
        options: [
            'Mount → Filsystem → Partition',
            'Disk → Partition → Kryptering → Filsystem → Mount',
            'Filsystem → Mount → Partition',
            'Kryptering → Disk → Mount'
        ],
        correctIndex: 1,
        explanation: 'Ordningen är fix: 1. Disk 2. Partition 3. LUKS 4. Filsystem 5. Mount',
        difficulty: 'VG',
        category: 'Hierarki'
    },
    {
        id: 'tent-disk-2',
        question: 'Vilket kommando partitionerar en disk?',
        options: ['partition /dev/sdb', 'fdisk /dev/sdb', 'mkpart /dev/sdb', 'diskpart /dev/sdb'],
        correctIndex: 1,
        explanation: 'fdisk är standard för partitionering. Interaktivt: g=GPT, n=new, w=write.',
        difficulty: 'G',
        category: 'Partitionering'
    },
    {
        id: 'tent-disk-3',
        question: 'I fdisk, vad gör kommandot "w"?',
        options: [
            'Visar partitioner',
            'Skriver ändringar till disk',
            'Skapar ny partition',
            'Avslutar utan att spara'
        ],
        correctIndex: 1,
        explanation: 'w = write. VIKTIGT! Utan w sparas ingenting. q = quit utan att spara.',
        difficulty: 'G',
        category: 'Partitionering'
    },
    {
        id: 'tent-disk-4',
        question: 'Hur krypterar du en partition med LUKS?',
        options: [
            'luks encrypt /dev/sdb1',
            'cryptsetup luksFormat /dev/sdb1',
            'encrypt --luks /dev/sdb1',
            'mkfs.luks /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'cryptsetup luksFormat skapar LUKS-kryptering. VARNING: Raderar all data!',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-5',
        question: 'Hur öppnar du en LUKS-krypterad partition?',
        options: [
            'luks open /dev/sdb1',
            'cryptsetup open /dev/sdb1 namn',
            'mount /dev/sdb1',
            'decrypt /dev/sdb1'
        ],
        correctIndex: 1,
        explanation: 'cryptsetup open dekrypterar och skapar /dev/mapper/namn som du kan montera.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-6',
        question: 'Var dyker en öppnad LUKS-enhet upp?',
        options: ['/dev/sdb1', '/dev/mapper/namn', '/mnt/luks', '/etc/luks'],
        correctIndex: 1,
        explanation: 'Öppnade LUKS-enheter finns i /dev/mapper/ med det namn du angav.',
        difficulty: 'G',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-7',
        question: 'Hur skapar du ett ext4-filsystem?',
        options: [
            'format ext4 /dev/mapper/namn',
            'mkfs.ext4 /dev/mapper/namn',
            'create-fs ext4 /dev/mapper/namn',
            'filesystem ext4 /dev/mapper/namn'
        ],
        correctIndex: 1,
        explanation: 'mkfs.ext4 (make filesystem) skapar ett ext4-filsystem.',
        difficulty: 'G',
        category: 'Filsystem'
    },
    {
        id: 'tent-disk-8',
        question: 'Hur monterar du en enhet?',
        options: [
            'attach /dev/mapper/namn /mnt',
            'mount /dev/mapper/namn /mnt',
            'connect /dev/mapper/namn /mnt',
            'link /dev/mapper/namn /mnt'
        ],
        correctIndex: 1,
        explanation: 'mount kopplar filsystem till en mount point (katalog).',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'tent-disk-9',
        question: 'Vad MÅSTE du göra innan "cryptsetup close"?',
        options: [
            'Skapa backup',
            'Avmontera (umount) först',
            'Stänga alla filer',
            'Synka databasen'
        ],
        correctIndex: 1,
        explanation: 'ALLTID umount innan close! Annars riskerar du dataförlust.',
        difficulty: 'VG',
        category: 'LUKS'
    },
    {
        id: 'tent-disk-10',
        question: 'Vad visar "lsblk"?',
        options: [
            'Filsystemsstatus',
            'Block devices (diskar och partitioner) i trädvy',
            'Monterade enheter',
            'Diskutrymme'
        ],
        correctIndex: 1,
        explanation: 'lsblk listar block devices som diskar, partitioner och LUKS-enheter.',
        difficulty: 'G',
        category: 'Kommandon'
    },
    {
        id: 'tent-disk-11',
        question: 'Vad gör kommandot "sync"?',
        options: [
            'Synkar tid',
            'Tvingar cachade skrivningar till disk',
            'Kopierar filer',
            'Synkar användare'
        ],
        correctIndex: 1,
        explanation: 'sync tvingar kernel att skriva buffrat data till disk. Bra före umount.',
        difficulty: 'VG',
        category: 'Kommandon'
    },
    {
        id: 'tent-disk-12',
        question: 'Var monteras USB-enheter automatiskt oftast?',
        options: ['/mnt', '/media', '/usb', '/dev'],
        correctIndex: 1,
        explanation: '/media används för auto-mount (USB, CD). /mnt för manuella mounts.',
        difficulty: 'G',
        category: 'Mount'
    },
    {
        id: 'tent-disk-13',
        question: 'Kan du återställa ett LUKS-lösenord om du glömt det?',
        options: [
            'Ja, med recovery-key',
            'Nej, data är permanent otillgänglig',
            'Ja, kontakta support',
            'Ja, via /etc/luks'
        ],
        correctIndex: 1,
        explanation: 'LUKS-lösenord kan INTE återställas. Glömt lösenord = förlorad data!',
        difficulty: 'VG',
        category: 'LUKS'
    }
]

// =============================================================================
// SUBNETTING (15 frågor)
// =============================================================================

const SUBNETTING_QUIZ: TentaishQuestion[] = [
    {
        id: 'tent-sub-1',
        question: 'Hur många hosts finns i ett /24-nätverk?',
        options: ['256', '254', '255', '252'],
        correctIndex: 1,
        explanation: '2^(32-24) - 2 = 256 - 2 = 254. Minus nätverks- och broadcast-adress.',
        difficulty: 'G',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-2',
        question: 'Vad är subnätmasken för /26?',
        options: ['255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240'],
        correctIndex: 1,
        explanation: '/26 = 26 ettor = 255.255.255.11000000 = 255.255.255.192',
        difficulty: 'G',
        category: 'CIDR'
    },
    {
        id: 'tent-sub-3',
        question: 'Hur många hosts i /27?',
        options: ['32', '30', '28', '62'],
        correctIndex: 1,
        explanation: '2^(32-27) - 2 = 32 - 2 = 30 hosts.',
        difficulty: 'G',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-4',
        question: 'Vad är nätverksadressen för 192.168.1.100/26?',
        options: ['192.168.1.0', '192.168.1.64', '192.168.1.96', '192.168.1.100'],
        correctIndex: 1,
        explanation: '/26 ger 64 adresser per subnät. 100 ligger i blocket 64-127, så network = .64',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-5',
        question: 'Vad är broadcast för 192.168.1.100/26?',
        options: ['192.168.1.126', '192.168.1.127', '192.168.1.128', '192.168.1.255'],
        correctIndex: 1,
        explanation: 'Subnät 64-127, broadcast = sista adressen = 192.168.1.127',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-6',
        question: 'Hur konverterar du 192 till binärt?',
        options: ['10000000', '11000000', '11100000', '10100000'],
        correctIndex: 1,
        explanation: '192 = 128 + 64 = 11000000. Subtrahera från vänster: 192-128=64, 64-64=0.',
        difficulty: 'VG',
        category: 'Binär'
    },
    {
        id: 'tent-sub-7',
        question: 'Vad är 11100000 i decimal?',
        options: ['192', '224', '240', '248'],
        correctIndex: 1,
        explanation: '128 + 64 + 32 = 224',
        difficulty: 'VG',
        category: 'Binär'
    },
    {
        id: 'tent-sub-8',
        question: 'Hur många subnät får du om du delar /24 i /26?',
        options: ['2', '4', '8', '16'],
        correctIndex: 1,
        explanation: '2^(26-24) = 2^2 = 4 subnät.',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-9',
        question: 'Vad är first host för 10.0.0.0/8?',
        options: ['10.0.0.0', '10.0.0.1', '10.0.0.255', '10.1.0.0'],
        correctIndex: 1,
        explanation: 'First host = network address + 1 = 10.0.0.1',
        difficulty: 'G',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-10',
        question: 'Vad är last host för 10.0.0.0/8?',
        options: ['10.255.255.254', '10.255.255.255', '10.0.0.254', '10.0.255.255'],
        correctIndex: 0,
        explanation: 'Last host = broadcast - 1 = 10.255.255.255 - 1 = 10.255.255.254',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-11',
        question: 'Vad används /30 typiskt till?',
        options: [
            'Stora nätverk',
            'Punkt-till-punkt-länkar (2 hosts)',
            'Wifi-nätverk',
            'Serverrum'
        ],
        correctIndex: 1,
        explanation: '/30 ger endast 2 hosts - perfekt för WAN-länkar mellan två routrar.',
        difficulty: 'VG',
        category: 'Koncept'
    },
    {
        id: 'tent-sub-12',
        question: 'Vilken prefix behövs för minst 500 hosts?',
        options: ['/24 (254 hosts)', '/23 (510 hosts)', '/22 (1022 hosts)', '/25 (126 hosts)'],
        correctIndex: 1,
        explanation: '/23 ger 2^9 - 2 = 510 hosts. /24 räcker inte (254).',
        difficulty: 'VG',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-13',
        question: 'Vad är network-delen i 192.168.1.50/24?',
        options: ['192.168.1.50', '192.168.1.0', '192.168.0.0', '192.0.0.0'],
        correctIndex: 1,
        explanation: '/24 betyder första 24 bitar är network = 192.168.1.0',
        difficulty: 'G',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-14',
        question: 'Hur många host-bitar har /28?',
        options: ['28', '4', '8', '16'],
        correctIndex: 1,
        explanation: '32 - 28 = 4 host-bitar. Ger 2^4 - 2 = 14 hosts.',
        difficulty: 'G',
        category: 'Beräkning'
    },
    {
        id: 'tent-sub-15',
        question: 'Vad är nästa subnät efter 192.168.1.0/26?',
        options: ['192.168.1.32', '192.168.1.64', '192.168.1.128', '192.168.2.0'],
        correctIndex: 1,
        explanation: '/26 = 64 adresser per subnät. 0 + 64 = nästa subnät börjar på .64',
        difficulty: 'VG',
        category: 'Beräkning'
    }
]

// =============================================================================
// EXPORT
// =============================================================================

export const TENTAISH_QUIZ: TentaishQuizSet[] = [
    {
        taskId: 'filsystem',
        taskTitle: 'Filsystem & Grundläggande',
        questions: FILSYSTEM_QUIZ
    },
    {
        taskId: 'anvandare',
        taskTitle: 'Användarhantering & Permissions',
        questions: ANVANDARE_QUIZ
    },
    {
        taskId: 'paket',
        taskTitle: 'Pakethantering (APT/DNF)',
        questions: PAKET_QUIZ
    },
    {
        taskId: 'ssh',
        taskTitle: 'SSH & Brandvägg',
        questions: SSH_QUIZ
    },
    {
        taskId: 'docker',
        taskTitle: 'Docker & Containers',
        questions: DOCKER_QUIZ
    },
    {
        taskId: 'disk',
        taskTitle: 'Disk & LUKS-kryptering',
        questions: DISK_QUIZ
    },
    {
        taskId: 'subnetting',
        taskTitle: 'Subnetting & Nätverk',
        questions: SUBNETTING_QUIZ
    }
]

// Flat array of all questions for easy access
export const ALL_TENTAISH_QUESTIONS: TentaishQuestion[] = TENTAISH_QUIZ.flatMap(
    set => set.questions
)

// Stats
export const TENTAISH_STATS = {
    totalQuestions: ALL_TENTAISH_QUESTIONS.length,
    gQuestions: ALL_TENTAISH_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgQuestions: ALL_TENTAISH_QUESTIONS.filter(q => q.difficulty === 'VG').length,
    categories: TENTAISH_QUIZ.map(s => s.taskTitle)
}
