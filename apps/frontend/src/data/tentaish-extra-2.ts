/**
 * TENTAISH EXPANSION - 200 NYA QUIZ-FRÅGOR
 * Moment 2: Pakethantering & SSH/Brandvägg
 *
 * Skapad: 2026-01-06
 */

import { TentaishQuestion } from './tentaish-quiz'

// =============================================================================
// MOMENT 2A: PAKETHANTERING - NYA FRÅGOR (30 st)
// =============================================================================

export const PAKET_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-pkg-ex-1',
        question: 'Vad gör "apt update"?',
        options: [
            'Uppdaterar alla paket',
            'Uppdaterar paketlistorna/index från repositories',
            'Tar bort gamla paket',
            'Installerar säkerhetsuppdateringar'
        ],
        correctIndex: 1,
        explanation: 'apt update hämtar senaste paketlistorna. apt upgrade installerar faktiska uppdateringar.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-2',
        question: 'Vad är skillnaden mellan "apt upgrade" och "apt full-upgrade"?',
        options: [
            'Ingen skillnad',
            'full-upgrade kan ta bort paket om nödvändigt för uppgradering',
            'upgrade är snabbare',
            'full-upgrade uppdaterar endast kernel'
        ],
        correctIndex: 1,
        explanation: 'full-upgrade (tidigare dist-upgrade) hanterar beroende-ändringar och kan ta bort paket.',
        difficulty: 'VG',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-3',
        question: 'Hur tar du bort ett paket och dess konfigurationsfiler?',
        options: [
            'apt remove paket',
            'apt purge paket',
            'apt delete paket',
            'apt uninstall paket'
        ],
        correctIndex: 1,
        explanation: 'remove tar bort paket men sparar config. purge tar bort allt inklusive konfiguration.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-4',
        question: 'Vad gör "apt autoremove"?',
        options: [
            'Tar bort alla paket',
            'Tar bort oönskade beroenden som inte längre behövs',
            'Reparerar trasiga paket',
            'Uppdaterar paket automatiskt'
        ],
        correctIndex: 1,
        explanation: 'autoremove städar upp paket som installerades som beroenden men inte längre krävs.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-5',
        question: 'Var konfigureras APT repositories?',
        options: [
            '/etc/apt/apt.conf',
            '/etc/apt/sources.list och /etc/apt/sources.list.d/',
            '/var/apt/repos',
            '/usr/share/apt'
        ],
        correctIndex: 1,
        explanation: 'sources.list innehåller repo-URLs. sources.list.d/ för extra repos som .list-filer.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-6',
        question: 'Hur söker du efter ett paket i APT?',
        options: [
            'apt find paket',
            'apt search sökord',
            'apt locate paket',
            'apt query sökord'
        ],
        correctIndex: 1,
        explanation: 'apt search söker i paketnamn och beskrivningar. apt show ger detaljerad info.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-7',
        question: 'Vad gör "apt list --installed"?',
        options: [
            'Listar tillgängliga paket',
            'Listar alla installerade paket',
            'Listar uppdateringar',
            'Installerar från lista'
        ],
        correctIndex: 1,
        explanation: '--installed visar installerade paket. --upgradable visar paket med uppdateringar.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-8',
        question: 'Vad är DNF?',
        options: [
            'En textredigerare',
            'Pakethanterare för RHEL/Fedora (ersatte YUM)',
            'En brandvägg',
            'En filsystemstyp'
        ],
        correctIndex: 1,
        explanation: 'DNF (Dandified YUM) är pakethanterare för Red Hat-baserade distros. Snabbare än yum.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-9',
        question: 'Vad gör "dnf check-update"?',
        options: [
            'Installerar uppdateringar',
            'Listar tillgängliga uppdateringar utan att installera',
            'Validerar systemet',
            'Uppdaterar DNF'
        ],
        correctIndex: 1,
        explanation: 'check-update visar vilka paket som har uppdateringar. dnf upgrade installerar dem.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-10',
        question: 'Hur installerar du ett lokalt RPM-paket med DNF?',
        options: [
            'dnf install paket.rpm',
            'dnf localinstall paket.rpm',
            'rpm -i paket.rpm',
            'Alla ovanstående fungerar'
        ],
        correctIndex: 3,
        explanation: 'dnf install hanterar lokala .rpm-filer. rpm -i fungerar också men löser inte beroenden.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-11',
        question: 'Vad är en RPM-fil?',
        options: [
            'En textfil',
            'Red Hat Package Manager - paketformat för RHEL/Fedora',
            'En loggfil',
            'En konfigurationsfil'
        ],
        correctIndex: 1,
        explanation: 'RPM är paketformatet för Red Hat-baserade system. Innehåller program + metadata.',
        difficulty: 'G',
        category: 'Paketformat'
    },
    {
        id: 'tent-pkg-ex-12',
        question: 'Vad är en DEB-fil?',
        options: [
            'Debug-logg',
            'Debian-paketformat för Debian/Ubuntu',
            'Database-fil',
            'Device-fil'
        ],
        correctIndex: 1,
        explanation: 'DEB är paketformatet för Debian-baserade distros. Installeras med dpkg eller apt.',
        difficulty: 'G',
        category: 'Paketformat'
    },
    {
        id: 'tent-pkg-ex-13',
        question: 'Vad gör "dpkg -i paket.deb"?',
        options: [
            'Visar paketinfo',
            'Installerar ett lokalt .deb-paket',
            'Tar bort paket',
            'Listar filer i paket'
        ],
        correctIndex: 1,
        explanation: 'dpkg -i installerar .deb-filer. OBS: Löser inte beroenden, använd apt för det.',
        difficulty: 'G',
        category: 'DPKG'
    },
    {
        id: 'tent-pkg-ex-14',
        question: 'Hur reparerar du trasiga beroenden i APT?',
        options: [
            'apt clean',
            'apt --fix-broken install',
            'apt repair',
            'apt check'
        ],
        correctIndex: 1,
        explanation: '--fix-broken försöker lösa dependency-problem genom att installera saknade paket.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-15',
        question: 'Vad gör "apt clean"?',
        options: [
            'Tar bort installerade paket',
            'Rensar APT-cache (nedladdade .deb-filer)',
            'Reparerar system',
            'Uppdaterar repositories'
        ],
        correctIndex: 1,
        explanation: 'clean tar bort cachade paket från /var/cache/apt/archives. Frigör diskutrymme.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-16',
        question: 'Vad är PPA i Ubuntu?',
        options: [
            'Personal Package Archive - tredjepartskällor',
            'Primary Package Application',
            'Protected Package Area',
            'Public Package Access'
        ],
        correctIndex: 0,
        explanation: 'PPA är personal repositories på Launchpad. Lägg till med add-apt-repository.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-17',
        question: 'Vad gör "dnf group install \"Development Tools\""?',
        options: [
            'Installerar ett enskilt paket',
            'Installerar en grupp av relaterade paket',
            'Skapar en ny grupp',
            'Visar gruppinfo'
        ],
        correctIndex: 1,
        explanation: 'DNF groups är samlingar av paket. "Development Tools" innehåller gcc, make, etc.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-18',
        question: 'Hur listar du vilka filer ett installerat paket innehåller?',
        options: [
            'dpkg -L paket (Debian) / rpm -ql paket (RHEL)',
            'apt files paket',
            'dnf contents paket',
            'pkg list paket'
        ],
        correctIndex: 0,
        explanation: 'dpkg -L för Debian-system, rpm -ql för RPM-baserade. Visar alla installerade filer.',
        difficulty: 'VG',
        category: 'Paketinfo'
    },
    {
        id: 'tent-pkg-ex-19',
        question: 'Hur tar du reda på vilket paket en fil tillhör?',
        options: [
            'dpkg -S /path/to/file (Debian) / rpm -qf /path/to/file (RHEL)',
            'apt owner file',
            'dnf owner file',
            'which package file'
        ],
        correctIndex: 0,
        explanation: 'dpkg -S och rpm -qf söker vilket paket som äger en specifik fil på systemet.',
        difficulty: 'VG',
        category: 'Paketinfo'
    },
    {
        id: 'tent-pkg-ex-20',
        question: 'Vad gör "dnf history"?',
        options: [
            'Visar bash-historik',
            'Visar DNF-transaktionshistorik (installationer/borttagningar)',
            'Visar systemloggar',
            'Visar uppdateringshistorik'
        ],
        correctIndex: 1,
        explanation: 'dnf history visar alla paketoperationer. Man kan även ångra med "dnf history undo".',
        difficulty: 'VG',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-21',
        question: 'Vad är EPEL?',
        options: [
            'En Linux-distribution',
            'Extra Packages for Enterprise Linux - tilläggsrepo för RHEL',
            'En pakethanterare',
            'En säkerhetssvit'
        ],
        correctIndex: 1,
        explanation: 'EPEL ger tillgång till fler paket för RHEL/CentOS som inte finns i default repos.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-22',
        question: 'Hur låser du ett paket från uppgradering i APT?',
        options: [
            'apt lock paket',
            'apt-mark hold paket',
            'apt freeze paket',
            'apt pin paket'
        ],
        correctIndex: 1,
        explanation: 'apt-mark hold förhindrar uppgradering. apt-mark unhold tar bort låset.',
        difficulty: 'VG',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-23',
        question: 'Vad gör "dnf provides */kommando"?',
        options: [
            'Kör kommandot',
            'Söker vilket paket som tillhandahåller ett kommando/fil',
            'Visar kommandohistorik',
            'Installerar kommandot'
        ],
        correctIndex: 1,
        explanation: 'provides söker i alla repos efter paket som innehåller specifik fil eller kommando.',
        difficulty: 'VG',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-24',
        question: 'Var sparas nedladdade .deb-filer temporärt?',
        options: [
            '/tmp/apt',
            '/var/cache/apt/archives',
            '/var/lib/apt',
            '/etc/apt/cache'
        ],
        correctIndex: 1,
        explanation: 'APT cachar nedladdade paket i /var/cache/apt/archives. Rensas med apt clean.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-25',
        question: 'Vad gör "apt-get -d upgrade"?',
        options: [
            'Tar bort uppgraderingar',
            'Laddar ner paket utan att installera',
            'Debug-läge',
            'Dry-run av uppgradering'
        ],
        correctIndex: 1,
        explanation: '-d (download-only) laddar ner till cache utan installation. Användbart för förberedelse.',
        difficulty: 'VG',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-26',
        question: 'Hur verifierar du integriteten på installerade paket?',
        options: [
            'apt verify',
            'debsums (Debian) / rpm -V (RHEL)',
            'dpkg --check',
            'dnf verify'
        ],
        correctIndex: 1,
        explanation: 'debsums kontrollerar MD5-summor på Debian. rpm -V verifierar på RPM-system.',
        difficulty: 'VG',
        category: 'Säkerhet'
    },
    {
        id: 'tent-pkg-ex-27',
        question: 'Vad är skillnaden mellan apt och apt-get?',
        options: [
            'Ingen skillnad',
            'apt är nyare med bättre UX, apt-get är mer skriptvänlig',
            'apt-get är snabbare',
            'apt-get är deprecated'
        ],
        correctIndex: 1,
        explanation: 'apt har progress bars och färger. apt-get är stabil för scripts. Samma backend.',
        difficulty: 'G',
        category: 'APT'
    },
    {
        id: 'tent-pkg-ex-28',
        question: 'Vad gör "dnf makecache"?',
        options: [
            'Skapar backup',
            'Bygger lokal metadata-cache från repos',
            'Reparerar cache',
            'Tar bort cache'
        ],
        correctIndex: 1,
        explanation: 'makecache laddar ner och cachar repo-metadata. Snabbar upp framtida operationer.',
        difficulty: 'G',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-29',
        question: 'Hur aktiverar/inaktiverar du ett repository tillfälligt i DNF?',
        options: [
            '--enablerepo=namn / --disablerepo=namn',
            '--repo=namn',
            '--use=namn',
            '--source=namn'
        ],
        correctIndex: 0,
        explanation: 'Dessa flaggor aktiverar/inaktiverar repos för en enskild operation.',
        difficulty: 'VG',
        category: 'DNF'
    },
    {
        id: 'tent-pkg-ex-30',
        question: 'Vad gör "apt-cache depends paket"?',
        options: [
            'Installerar beroenden',
            'Visar paketets beroenden (dependencies)',
            'Tar bort beroenden',
            'Uppdaterar beroenden'
        ],
        correctIndex: 1,
        explanation: 'depends visar vad paketet kräver. rdepends visar vad som kräver paketet.',
        difficulty: 'VG',
        category: 'APT'
    }
]

// =============================================================================
// MOMENT 2B: SSH & BRANDVÄGG - NYA FRÅGOR (30 st)
// =============================================================================

export const SSH_EXTRA: TentaishQuestion[] = [
    {
        id: 'tent-ssh-ex-1',
        question: 'Vad är standardporten för SSH?',
        options: ['21', '22', '23', '80'],
        correctIndex: 1,
        explanation: 'SSH använder port 22 som standard. FTP är 21, Telnet är 23, HTTP är 80.',
        difficulty: 'G',
        category: 'SSH Grundläggande'
    },
    {
        id: 'tent-ssh-ex-2',
        question: 'Var finns SSH-serverns konfiguration?',
        options: [
            '/etc/ssh/ssh_config',
            '/etc/ssh/sshd_config',
            '/etc/sshd.conf',
            '~/.ssh/config'
        ],
        correctIndex: 1,
        explanation: 'sshd_config är för SSH-daemon (server). ssh_config är för klient-default.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    {
        id: 'tent-ssh-ex-3',
        question: 'Hur genererar du ett SSH-nyckelpar?',
        options: [
            'ssh-keygen',
            'ssh-genkey',
            'ssh-create',
            'ssh-new'
        ],
        correctIndex: 0,
        explanation: 'ssh-keygen skapar nyckelpar. Default är RSA, använd -t ed25519 för modernare algoritm.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    {
        id: 'tent-ssh-ex-4',
        question: 'Var lagras din publika SSH-nyckel?',
        options: [
            '~/.ssh/id_rsa',
            '~/.ssh/id_rsa.pub',
            '~/.ssh/authorized_keys',
            '/etc/ssh/keys'
        ],
        correctIndex: 1,
        explanation: 'id_rsa är privata nyckeln, id_rsa.pub är publika. authorized_keys innehåller tillåtna nycklar på servern.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    {
        id: 'tent-ssh-ex-5',
        question: 'Var placeras andras publika nycklar för att tillåta SSH-inloggning?',
        options: [
            '~/.ssh/id_rsa.pub',
            '~/.ssh/authorized_keys',
            '/etc/ssh/authorized_keys',
            '~/.ssh/known_hosts'
        ],
        correctIndex: 1,
        explanation: 'authorized_keys i användarens ~/.ssh/ innehåller publika nycklar som får logga in.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    {
        id: 'tent-ssh-ex-6',
        question: 'Vad innehåller ~/.ssh/known_hosts?',
        options: [
            'Dina egna nycklar',
            'Fingerprints för servrar du har anslutit till',
            'Lösenord',
            'Konfiguration'
        ],
        correctIndex: 1,
        explanation: 'known_hosts sparar server-fingerprints för att upptäcka man-in-the-middle-attacker.',
        difficulty: 'G',
        category: 'SSH Säkerhet'
    },
    {
        id: 'tent-ssh-ex-7',
        question: 'Vad gör "ssh-copy-id user@server"?',
        options: [
            'Kopierar filer via SSH',
            'Kopierar din publika nyckel till serverns authorized_keys',
            'Kopierar serverns nyckel',
            'Kopierar SSH-konfiguration'
        ],
        correctIndex: 1,
        explanation: 'ssh-copy-id automatiserar att lägga till din pubkey i serverns authorized_keys.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    {
        id: 'tent-ssh-ex-8',
        question: 'Vilken permission ska ~/.ssh/authorized_keys ha?',
        options: ['777', '755', '644', '600'],
        correctIndex: 3,
        explanation: '600 (rw för ägare, inget för andra). SSH vägrar använda filen med för öppna permissions.',
        difficulty: 'G',
        category: 'SSH Säkerhet'
    },
    {
        id: 'tent-ssh-ex-9',
        question: 'Hur inaktiverar du lösenordsinloggning för SSH?',
        options: [
            'NoPassword yes',
            'PasswordAuthentication no',
            'DisablePassword yes',
            'Password off'
        ],
        correctIndex: 1,
        explanation: 'Sätt PasswordAuthentication no i /etc/ssh/sshd_config. Kräver nyckel-autentisering.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    {
        id: 'tent-ssh-ex-10',
        question: 'Hur förhindrar du root-inloggning via SSH?',
        options: [
            'RootLogin no',
            'PermitRootLogin no',
            'AllowRoot no',
            'DisableRoot yes'
        ],
        correctIndex: 1,
        explanation: 'PermitRootLogin no i sshd_config. Bästa praxis: Använd vanlig user + sudo.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    {
        id: 'tent-ssh-ex-11',
        question: 'Hur startar du om SSH-tjänsten efter config-ändring?',
        options: [
            'ssh restart',
            'systemctl restart sshd',
            'service ssh reload',
            'Både B och C fungerar'
        ],
        correctIndex: 3,
        explanation: 'systemctl restart sshd (RHEL) eller service ssh restart (Debian). Reload laddar config utan att droppa anslutningar.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    {
        id: 'tent-ssh-ex-12',
        question: 'Vad gör "ssh -p 2222 user@server"?',
        options: [
            'Använder protokoll version 2',
            'Ansluter till SSH på port 2222',
            'Kör med password-prompt',
            'Proxy-läge'
        ],
        correctIndex: 1,
        explanation: '-p anger icke-standard port. Användbart när SSH kör på annan port för säkerhet.',
        difficulty: 'G',
        category: 'SSH Grundläggande'
    },
    {
        id: 'tent-ssh-ex-13',
        question: 'Vad gör "ssh -L 8080:localhost:80 user@server"?',
        options: [
            'Listar portar',
            'Skapar en lokal port forward (tunnel)',
            'Lyssnar på port 8080',
            'Laddar konfiguration'
        ],
        correctIndex: 1,
        explanation: '-L skapar lokal tunnel. Din lokala port 8080 tunnlas till serverns localhost:80.',
        difficulty: 'VG',
        category: 'SSH Tunneling'
    },
    {
        id: 'tent-ssh-ex-14',
        question: 'Vad gör "ssh -R 8080:localhost:80 user@server"?',
        options: [
            'Remote port forward - exponerar din lokala port på servern',
            'Reconnect-läge',
            'Read-only läge',
            'Reverse DNS-lookup'
        ],
        correctIndex: 0,
        explanation: '-R skapar remote tunnel. Serverns port 8080 går till din lokala port 80.',
        difficulty: 'VG',
        category: 'SSH Tunneling'
    },
    {
        id: 'tent-ssh-ex-15',
        question: 'Vad är SSH agent forwarding (-A)?',
        options: [
            'Automatisk anslutning',
            'Vidarebefordrar din lokala SSH-agent till servern för hop-anslutningar',
            'Accelererad överföring',
            'Anonymt läge'
        ],
        correctIndex: 1,
        explanation: 'Med -A kan du SSHa vidare från servern med din lokala nyckel utan att kopiera den.',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    {
        id: 'tent-ssh-ex-16',
        question: 'Hur kopierar du filer via SSH?',
        options: [
            'cp remote:file local',
            'scp user@server:fil destination',
            'ssh cp file',
            'ssh-transfer file'
        ],
        correctIndex: 1,
        explanation: 'scp (secure copy) eller rsync över SSH. scp fil user@server:/path kopierar dit.',
        difficulty: 'G',
        category: 'SSH Filöverföring'
    },
    {
        id: 'tent-ssh-ex-17',
        question: 'Vad är fördelen med rsync över scp?',
        options: [
            'Snabbare alltid',
            'Överför endast ändringar (delta), bättre för synkronisering',
            'Mer säkert',
            'Ingen fördel'
        ],
        correctIndex: 1,
        explanation: 'rsync gör delta-sync, överför bara skillnader. Perfekt för backup och synk.',
        difficulty: 'G',
        category: 'SSH Filöverföring'
    },
    {
        id: 'tent-ssh-ex-18',
        question: 'Vad gör "ssh -N -f -L 3306:localhost:3306 user@server"?',
        options: [
            'Ansluter interaktivt',
            'Skapar en bakgrunds-tunnel utan shell',
            'Testar anslutning',
            'Visar nätverksstatus'
        ],
        correctIndex: 1,
        explanation: '-N = no command, -f = bakgrund. Perfekt för att skapa persistenta tunnlar.',
        difficulty: 'VG',
        category: 'SSH Tunneling'
    },
    {
        id: 'tent-ssh-ex-19',
        question: 'Vad är UFW?',
        options: [
            'Unix File Watcher',
            'Uncomplicated Firewall - användarvänligt brandväggsgränssnitt',
            'User Function Wrapper',
            'Unified Format Wizard'
        ],
        correctIndex: 1,
        explanation: 'UFW är en frontend för iptables som gör brandväggshantering enklare i Ubuntu.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-20',
        question: 'Hur tillåter du SSH genom UFW?',
        options: [
            'ufw open ssh',
            'ufw allow ssh',
            'ufw enable ssh',
            'ufw permit 22'
        ],
        correctIndex: 1,
        explanation: 'ufw allow ssh eller ufw allow 22. SSH är fördefinierad service i UFW.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-21',
        question: 'Hur aktiverar du UFW?',
        options: [
            'ufw start',
            'ufw enable',
            'systemctl start ufw',
            'ufw on'
        ],
        correctIndex: 1,
        explanation: 'ufw enable aktiverar brandväggen. VARNING: Tillåt SSH först annars låser du ute dig!',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-22',
        question: 'Vad visar "ufw status verbose"?',
        options: [
            'Endast aktiva regler',
            'Detaljerad status med default policies och alla regler',
            'Loggade händelser',
            'Systemstatus'
        ],
        correctIndex: 1,
        explanation: 'verbose ger mer info: default incoming/outgoing policy, aktiva regler med nummer.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-23',
        question: 'Vad är firewalld?',
        options: [
            'En loggdemon',
            'Dynamisk brandvägg för RHEL/Fedora med zoner',
            'En backup-tjänst',
            'DNS-server'
        ],
        correctIndex: 1,
        explanation: 'firewalld är Red Hats brandvägg med zoner (public, home, work, etc.) och permanenta regler.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-24',
        question: 'Hur öppnar du en port permanent i firewalld?',
        options: [
            'firewall-cmd --open-port=80',
            'firewall-cmd --permanent --add-port=80/tcp',
            'firewalld add 80',
            'firewall-cmd --port 80'
        ],
        correctIndex: 1,
        explanation: '--permanent sparar över omstart. Utan --permanent gäller bara till nästa restart.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-25',
        question: 'Vad gör "firewall-cmd --reload"?',
        options: [
            'Startar om firewalld',
            'Laddar om konfigurationen utan att droppa anslutningar',
            'Återställer default',
            'Visar status'
        ],
        correctIndex: 1,
        explanation: '--reload läser in permanenta regler. Krävs efter ändringar med --permanent.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-26',
        question: 'Vad är en brandväggszon i firewalld?',
        options: [
            'En geografisk plats',
            'En uppsättning regler för olika nätverkssituationer',
            'En loggkategori',
            'En tidzon'
        ],
        correctIndex: 1,
        explanation: 'Zoner som "public", "home", "work" har olika säkerhetsnivåer. Interface tilldelas zoner.',
        difficulty: 'VG',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-27',
        question: 'Hur blockerar du en specifik IP i UFW?',
        options: [
            'ufw block 192.168.1.100',
            'ufw deny from 192.168.1.100',
            'ufw reject 192.168.1.100',
            'ufw ban 192.168.1.100'
        ],
        correctIndex: 1,
        explanation: 'ufw deny from IP blockerar all trafik från den IP-adressen.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    {
        id: 'tent-ssh-ex-28',
        question: 'Vad är fail2ban?',
        options: [
            'En backup-lösning',
            'Automatiserad IP-bannning vid upprepade misslyckade inloggningar',
            'En VPN-tjänst',
            'En lösenordshanterare'
        ],
        correctIndex: 1,
        explanation: 'fail2ban övervakar loggar och bannar IP-adresser med för många misslyckade försök.',
        difficulty: 'G',
        category: 'Säkerhet'
    },
    {
        id: 'tent-ssh-ex-29',
        question: 'Hur visar du aktiva SSH-sessioner?',
        options: [
            'ssh list',
            'w eller who',
            'ssh sessions',
            'ps ssh'
        ],
        correctIndex: 1,
        explanation: '"w" och "who" visar inloggade användare. "ss -tnp | grep ssh" visar SSH-anslutningar.',
        difficulty: 'G',
        category: 'SSH Grundläggande'
    },
    {
        id: 'tent-ssh-ex-30',
        question: 'Vad är Ed25519 i SSH-kontext?',
        options: [
            'Ett protokoll',
            'En modern, säker algoritm för SSH-nycklar',
            'En port',
            'En loggfil'
        ],
        correctIndex: 1,
        explanation: 'Ed25519 är en elliptisk kurva-algoritm. Snabbare och säkrare än RSA. Använd ssh-keygen -t ed25519.',
        difficulty: 'VG',
        category: 'SSH Säkerhet'
    }
]
