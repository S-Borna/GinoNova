/**
 * INFÖR OMTENTA LINUX - Del 1: SSH & Brandvägg
 * 50 quiz-frågor baserade på SSH & Brandvägg materialet
 * 
 * Skapad: 2026-01-12
 */

export interface OmtentaQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
}

export const SSH_BRANDVAGG_QUESTIONS: OmtentaQuestion[] = [
    // Fråga 1 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-1',
        question: 'SSH står för...',
        options: ['Secure Shell Host', 'System Shell', 'Secure Shell', 'Safe Shell Handler'],
        correctIndex: 2,
        explanation: 'SSH = Secure Shell, ett protokoll för säker fjärranslutning.',
        difficulty: 'G',
        category: 'SSH Grundläggande'
    },
    // Fråga 2 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-2',
        question: 'Vilken port använder SSH som standard?',
        options: ['22', '80', '443', '8080'],
        correctIndex: 0,
        explanation: 'SSH använder port 22 som standard. HTTP=80, HTTPS=443.',
        difficulty: 'G',
        category: 'SSH Grundläggande'
    },
    // Fråga 3 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-3',
        question: 'Kommandot för att ansluta till en server via SSH är...',
        options: ['connect user@host', 'login user@host', 'remote user@host', 'ssh user@host'],
        correctIndex: 3,
        explanation: 'ssh user@host är standardkommandot för SSH-anslutning.',
        difficulty: 'G',
        category: 'SSH Kommandon'
    },
    // Fråga 4 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-4',
        question: 'Var lagras SSH-konfiguration för servern?',
        options: ['/etc/ssh/ssh.conf', '/etc/ssh/sshd_config', '/var/ssh/config', '~/.ssh/config'],
        correctIndex: 1,
        explanation: '/etc/ssh/sshd_config är serverkonfigurationen. ~/.ssh/config är klientens.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    // Fråga 5 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-5',
        question: 'Kommandot för att generera SSH-nycklar är...',
        options: ['ssh-create', 'ssh-new', 'ssh-keygen', 'ssh-generate'],
        correctIndex: 2,
        explanation: 'ssh-keygen genererar SSH-nyckelpar (publik + privat).',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    // Fråga 6 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-6',
        question: 'Var lagras din publika SSH-nyckel?',
        options: ['~/.ssh/id_rsa.pub', '~/.ssh/id_rsa', '/etc/ssh/key.pub', '~/.ssh/public_key'],
        correctIndex: 0,
        explanation: 'id_rsa.pub är den publika nyckeln, id_rsa är den privata.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    // Fråga 7 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-7',
        question: 'Kommandot för att kopiera publik nyckel till server är...',
        options: ['ssh-send', 'ssh-copy-id', 'scp-key', 'ssh-upload'],
        correctIndex: 1,
        explanation: 'ssh-copy-id kopierar din publika nyckel till serverns authorized_keys.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    // Fråga 8 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-8',
        question: 'Vilken fil på servern innehåller tillåtna publika nycklar?',
        options: ['~/.ssh/keys', '~/.ssh/public_keys', '~/.ssh/allowed', '~/.ssh/authorized_keys'],
        correctIndex: 3,
        explanation: 'authorized_keys innehåller alla publika nycklar som får logga in.',
        difficulty: 'G',
        category: 'SSH Nycklar'
    },
    // Fråga 9 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-9',
        question: 'Kommandot ufw står för...',
        options: ['Unix FireWall', 'User FireWall', 'Uncomplicated Firewall', 'Unified FireWall'],
        correctIndex: 2,
        explanation: 'UFW = Uncomplicated Firewall, ett enkelt gränssnitt för iptables.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 10 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-10',
        question: 'Hur aktiverar du ufw?',
        options: ['ufw enable', 'ufw start', 'ufw on', 'ufw activate'],
        correctIndex: 0,
        explanation: 'ufw enable aktiverar brandväggen.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 11 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-11',
        question: 'Kommandot för att tillåta SSH genom ufw är...',
        options: ['ufw open ssh', 'ufw allow ssh', 'ufw permit ssh', 'ufw accept ssh'],
        correctIndex: 1,
        explanation: 'ufw allow ssh (eller ufw allow 22) tillåter SSH-trafik.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 12 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-12',
        question: 'Hur visar du ufw-status?',
        options: ['ufw show', 'ufw list', 'ufw info', 'ufw status'],
        correctIndex: 3,
        explanation: 'ufw status visar aktiva regler och om brandväggen är aktiv.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 13 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-13',
        question: 'Vad gör SSH-agent?',
        options: ['Spionerar på trafik', 'Skapar nycklar', 'Håller nycklar i minnet för enkel autentisering', 'Blockerar attacker'],
        correctIndex: 2,
        explanation: 'SSH-agent cachar din privata nyckel så du slipper skriva passphrase varje gång.',
        difficulty: 'G',
        category: 'SSH Agent'
    },
    // Fråga 14 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-14',
        question: 'Kommandot för att lägga till nyckel till ssh-agent är...',
        options: ['ssh-add', 'ssh-agent add', 'ssh-key add', 'agent-add'],
        correctIndex: 0,
        explanation: 'ssh-add lägger till din privata nyckel i ssh-agent.',
        difficulty: 'G',
        category: 'SSH Agent'
    },
    // Fråga 15 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-15',
        question: 'Vilken parameter i sshd_config inaktiverar lösenordsautentisering?',
        options: ['NoPassword yes', 'PasswordAuthentication no', 'DisablePassword yes', 'PasswordLogin no'],
        correctIndex: 1,
        explanation: 'PasswordAuthentication no tvingar användning av nycklar istället.',
        difficulty: 'VG',
        category: 'SSH Säkerhet'
    },
    // Fråga 16 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-16',
        question: 'Vilken parameter i sshd_config inaktiverar root-login?',
        options: ['NoRoot yes', 'RootLogin no', 'DisableRoot yes', 'PermitRootLogin no'],
        correctIndex: 3,
        explanation: 'PermitRootLogin no förhindrar direkt root-inloggning via SSH.',
        difficulty: 'VG',
        category: 'SSH Säkerhet'
    },
    // Fråga 17 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-17',
        question: 'Kommandot för att blockera en port i ufw är...',
        options: ['ufw block', 'ufw reject', 'ufw deny', 'ufw stop'],
        correctIndex: 2,
        explanation: 'ufw deny portnummer blockerar trafik på den porten.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 18 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-18',
        question: 'Vad gör kommandot scp?',
        options: ['Kopierar filer över SSH', 'Skapar SSH-config', 'Scannar portar', 'Kontrollerar SSH'],
        correctIndex: 0,
        explanation: 'scp = Secure Copy, kopierar filer säkert via SSH-protokollet.',
        difficulty: 'G',
        category: 'SSH Kommandon'
    },
    // Fråga 19 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-19',
        question: 'Firewalld använder konceptet...',
        options: ['Regler', 'Zoner', 'Policies', 'Nivåer'],
        correctIndex: 1,
        explanation: 'Firewalld organiserar regler i zoner (public, home, trusted, etc.).',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 20 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-20',
        question: 'Kommandot för att starta om SSH-tjänsten är...',
        options: ['ssh restart', 'service ssh start', 'sshd restart', 'systemctl restart sshd'],
        correctIndex: 3,
        explanation: 'systemctl restart sshd startar om SSH-demonen på systemd-system.',
        difficulty: 'G',
        category: 'SSH Kommandon'
    },
    // Fråga 21 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-21',
        question: 'Vilken algoritm rekommenderas för SSH-nycklar?',
        options: ['RSA 1024', 'DSA', 'Ed25519', 'MD5'],
        correctIndex: 2,
        explanation: 'Ed25519 är modern, snabb och säker. RSA 1024 är för kort, DSA är deprecated.',
        difficulty: 'VG',
        category: 'SSH Nycklar'
    },
    // Fråga 22 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-22',
        question: 'Port forwarding i SSH kallas också...',
        options: ['SSH tunneling', 'Port redirect', 'Port mapping', 'SSH bridging'],
        correctIndex: 0,
        explanation: 'SSH tunneling skapar en krypterad tunnel för att forwarda portar.',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    // Fråga 23 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-23',
        question: 'Flaggan -L i SSH skapar...',
        options: ['Log', 'Local port forward', 'Listen', 'Link'],
        correctIndex: 1,
        explanation: '-L skapar local port forward: ssh -L localport:remotehost:remoteport.',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    // Fråga 24 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-24',
        question: 'Vad gör flaggan -v i SSH?',
        options: ['Version', 'Verify', 'Virtual', 'Verbose (debug-info)'],
        correctIndex: 3,
        explanation: '-v aktiverar verbose mode för debugging. -vv och -vvv ger ännu mer info.',
        difficulty: 'G',
        category: 'SSH Kommandon'
    },
    // Fråga 25 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-25',
        question: 'Kommandot för att ta bort en ufw-regel är...',
        options: ['ufw remove', 'ufw drop', 'ufw delete', 'ufw erase'],
        correctIndex: 2,
        explanation: 'ufw delete tar bort en regel. Använd ufw status numbered först.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 26 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-26',
        question: 'Vad är bruteforce-attack?',
        options: ['Gissar lösenord genom upprepade försök', 'DDoS-attack', 'Virus', 'Phishing'],
        correctIndex: 0,
        explanation: 'Bruteforce testar tusentals lösenordskombinationer automatiskt.',
        difficulty: 'G',
        category: 'Säkerhet'
    },
    // Fråga 27 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-27',
        question: 'Fail2ban skyddar mot...',
        options: ['Virus', 'Bruteforce-attacker', 'Malware', 'Phishing'],
        correctIndex: 1,
        explanation: 'Fail2ban blockerar IP-adresser efter för många misslyckade inloggningsförsök.',
        difficulty: 'G',
        category: 'Säkerhet'
    },
    // Fråga 28 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-28',
        question: 'Vad gör ufw default deny incoming?',
        options: ['Tillåter all inkommande', 'Tillåter DNS', 'Loggar trafik', 'Blockerar all inkommande trafik som standard'],
        correctIndex: 3,
        explanation: 'default deny incoming blockerar allt som inte explicit tillåts.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 29 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-29',
        question: 'Vilken flagga i SSH anger port?',
        options: ['-P', '-port', '-p', '-n'],
        correctIndex: 2,
        explanation: 'ssh -p 2222 user@host ansluter till port 2222 istället för 22.',
        difficulty: 'G',
        category: 'SSH Kommandon'
    },
    // Fråga 30 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-30',
        question: 'Vad gör kommandot ssh-keyscan?',
        options: ['Hämtar host keys från servrar', 'Skannar nätverket', 'Skannar nycklar', 'Testar säkerhet'],
        correctIndex: 0,
        explanation: 'ssh-keyscan hämtar publika host keys för att lägga i known_hosts.',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    // Fråga 31 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-31',
        question: 'Var lagras kända hosts?',
        options: ['~/.ssh/hosts', '~/.ssh/known_hosts', '~/.ssh/servers', '/etc/hosts'],
        correctIndex: 1,
        explanation: 'known_hosts sparar fingerprints för servrar du anslutit till.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    // Fråga 32 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-32',
        question: 'Vad händer första gången du SSH:ar till en ny server?',
        options: ['Anslutning nekas', 'Automatisk accept', 'Lösenord krävs', 'Fingerprint-verifiering krävs'],
        correctIndex: 3,
        explanation: 'Du måste verifiera serverns fingerprint första gången för att förhindra MITM.',
        difficulty: 'G',
        category: 'SSH Säkerhet'
    },
    // Fråga 33 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-33',
        question: 'Kommandot iptables är...',
        options: ['IP-tabell', 'Routing-tabell', 'Linux packet filter/firewall', 'ARP-tabell'],
        correctIndex: 2,
        explanation: 'iptables är Linux lågnivå-brandvägg. UFW och firewalld är frontend för den.',
        difficulty: 'VG',
        category: 'Brandvägg'
    },
    // Fråga 34 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-34',
        question: 'I firewalld, kommandot firewall-cmd --reload...',
        options: ['Laddar om konfiguration', 'Startar om firewall', 'Visar status', 'Stänger av firewall'],
        correctIndex: 0,
        explanation: '--reload laddar om regler utan att starta om tjänsten.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 35 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-35',
        question: 'Vad gör sftp?',
        options: ['Snabb FTP', 'Secure FTP (SSH-baserat)', 'Simple FTP', 'Standard FTP'],
        correctIndex: 1,
        explanation: 'SFTP kör FTP-liknande filöverföring över SSH-protokollet.',
        difficulty: 'G',
        category: 'SSH Kommandon'
    },
    // Fråga 36 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-36',
        question: 'Vilken permission ska ~/.ssh ha?',
        options: ['777', '755', '644', '700'],
        correctIndex: 3,
        explanation: '700 = bara ägaren har tillgång. SSH vägrar använda mappen annars.',
        difficulty: 'VG',
        category: 'SSH Säkerhet'
    },
    // Fråga 37 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-37',
        question: 'Vilken permission ska private key ha?',
        options: ['644', '755', '600', '700'],
        correctIndex: 2,
        explanation: '600 = bara ägaren kan läsa/skriva. SSH vägrar använda nyckeln annars.',
        difficulty: 'VG',
        category: 'SSH Säkerhet'
    },
    // Fråga 38 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-38',
        question: 'Vad gör ufw status numbered?',
        options: ['Visar regler med nummer', 'Visar version', 'Räknar paket', 'Visar portnummer'],
        correctIndex: 0,
        explanation: 'numbered visar regelnummer så du kan referera till dem vid delete.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 39 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-39',
        question: 'Kommandot för att se vilka portar som lyssnar är...',
        options: ['portlist', 'ss -tulpn eller netstat', 'listen', 'ports'],
        correctIndex: 1,
        explanation: 'ss -tulpn (eller netstat -tulpn) visar lyssnande TCP/UDP-portar.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    // Fråga 40 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-40',
        question: 'Vad är SSH jump host/bastion?',
        options: ['Test-server', 'Backup-server', 'Load balancer', 'Mellanliggande server för åtkomst'],
        correctIndex: 3,
        explanation: 'En bastion/jump host används för att nå servrar i privata nätverk.',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    // Fråga 41 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-41',
        question: 'Flaggan -J i SSH används för...',
        options: ['Java', 'JSON', 'Jump host', 'Journal'],
        correctIndex: 2,
        explanation: 'ssh -J jumphost user@destination hoppar via jumphost.',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    // Fråga 42 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-42',
        question: 'Vad gör kommandot ss -tulpn?',
        options: ['Visar lyssnande TCP/UDP-portar', 'Startar tjänst', 'Stoppar tjänst', 'Testar anslutning'],
        correctIndex: 0,
        explanation: '-t=TCP, -u=UDP, -l=listening, -p=process, -n=numeric.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    // Fråga 43 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-43',
        question: 'I ufw, hur tillåter du specifik IP?',
        options: ['ufw allow ip', 'ufw allow from IP', 'ufw permit IP', 'ufw accept IP'],
        correctIndex: 1,
        explanation: 'ufw allow from 192.168.1.100 tillåter all trafik från den IP:n.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 44 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-44',
        question: 'Vad är default zon i firewalld?',
        options: ['trusted', 'home', 'work', 'public'],
        correctIndex: 3,
        explanation: 'public är default-zonen med restriktiva regler.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 45 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-45',
        question: 'Kommandot för permanent ändring i firewalld?',
        options: ['--save', '--persist', '--permanent', '--store'],
        correctIndex: 2,
        explanation: '--permanent sparar regeln så den överlever omstart.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 46 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-46',
        question: 'Vad gör SSH escape sequence ~.?',
        options: ['Avslutar hängd SSH-session', 'Visar hjälp', 'Startar om', 'Pausar'],
        correctIndex: 0,
        explanation: 'Enter, ~, . avslutar en hängd SSH-session. Mycket användbart!',
        difficulty: 'VG',
        category: 'SSH Avancerat'
    },
    // Fråga 47 - Rätt svar på position B (index 1)
    {
        id: 'omtenta-ssh-47',
        question: 'Var konfigurerar du SSH-klienten?',
        options: ['/etc/ssh/sshd_config', '/etc/ssh/ssh_config eller ~/.ssh/config', '/var/ssh/config', '~/.sshrc'],
        correctIndex: 1,
        explanation: 'ssh_config (utan d) är klientconfig. ~/.ssh/config är per-användare.',
        difficulty: 'G',
        category: 'SSH Konfiguration'
    },
    // Fråga 48 - Rätt svar på position D (index 3)
    {
        id: 'omtenta-ssh-48',
        question: 'Vad är host key?',
        options: ['Användarens nyckel', 'Root-nyckel', 'Krypterad data', 'Serverns identitet'],
        correctIndex: 3,
        explanation: 'Host key identifierar servern unikt och förhindrar MITM-attacker.',
        difficulty: 'G',
        category: 'SSH Säkerhet'
    },
    // Fråga 49 - Rätt svar på position C (index 2)
    {
        id: 'omtenta-ssh-49',
        question: 'Kommandot för att visa firewalld-zoner är...',
        options: ['firewall-cmd --zones', 'firewall-cmd --list-zones', 'firewall-cmd --get-zones', 'firewall-cmd --show-zones'],
        correctIndex: 2,
        explanation: '--get-zones visar alla tillgängliga zoner.',
        difficulty: 'G',
        category: 'Brandvägg'
    },
    // Fråga 50 - Rätt svar på position A (index 0)
    {
        id: 'omtenta-ssh-50',
        question: 'Vad gör AllowUsers i sshd_config?',
        options: ['Begränsar vilka användare som får logga in', 'Tillåter alla', 'Skapar användare', 'Loggar användare'],
        correctIndex: 0,
        explanation: 'AllowUsers user1 user2 tillåter BARA dessa användare att SSH:a in.',
        difficulty: 'VG',
        category: 'SSH Säkerhet'
    }
]

export const SSH_BRANDVAGG_STATS = {
    totalQuestions: SSH_BRANDVAGG_QUESTIONS.length,
    gQuestions: SSH_BRANDVAGG_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgQuestions: SSH_BRANDVAGG_QUESTIONS.filter(q => q.difficulty === 'VG').length
}
