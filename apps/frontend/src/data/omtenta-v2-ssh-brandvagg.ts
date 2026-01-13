/**
 * OMTENTA V2 - SSH & Brandvägg (110 frågor)
 * EXAKT spegling av Omtenta/SSH_Brandvagg_Quiz_110.md
 *
 * OBS: Inkluderar multi-select frågor (choose X)
 */

export type OmtentaV2Topic =
    | 'ssh-brandvagg'
    | 'pakethantering-bash'
    | 'docker-containers'
    | 'blockstorage-kryptering'
    | 'subnetting-natverk'
    | 'anvandarhantering'
    | 'filsystem'

export interface OmtentaV2Question {
    id: string
    question: string
    options: string[]
    correctIndices: number[]  // Multi-select stöd
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    topic: OmtentaV2Topic
}

export const SSH_BRANDVAGG_V2_QUESTIONS: OmtentaV2Question[] = [
    {
        id: 'omtenta-v2-ssh-1',
        question: 'SSH stands for...',
        options: ['System Shell Host', 'Safe Shell Handler', 'Secure Shell', 'Server Shell Host'],
        correctIndices: [2],
        explanation: 'SSH = Secure Shell',
        difficulty: 'G',
        category: 'SSH Grundläggande',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-2',
        question: 'SSH default port is...',
        options: ['21', '22', '23', '80'],
        correctIndices: [1],
        explanation: 'SSH använder port 22 som standard.',
        difficulty: 'G',
        category: 'SSH Grundläggande',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-3',
        question: 'SSH config file on server is...',
        options: ['/etc/ssh/ssh.conf', '/etc/ssh/config', '/etc/ssh/sshd_config', '/etc/sshd.conf'],
        correctIndices: [2],
        explanation: '/etc/ssh/sshd_config är serverns konfigurationsfil.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-4',
        question: 'SSH config file on client is...',
        options: ['/etc/ssh/sshd_config', '/etc/ssh/ssh_config', '/etc/ssh/config', '~/.ssh/sshd_config'],
        correctIndices: [1],
        explanation: '/etc/ssh/ssh_config är klientens globala konfigurationsfil.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-5',
        question: 'User SSH config is in...',
        options: ['~/ssh/config', '~/.ssh/config', '~/.sshconfig', '~/.ssh/ssh_config'],
        correctIndices: [1],
        explanation: '~/.ssh/config är användarens SSH-konfiguration.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-6',
        question: 'To connect to remote host, use...',
        options: ['ssh host@user', 'ssh user@host', 'connect user@host', 'remote user@host'],
        correctIndices: [1],
        explanation: 'ssh user@host är standardkommandot.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-7',
        question: 'SSH keys are stored in...',
        options: ['~/ssh/', '~/.ssh/', '/etc/ssh/keys/', '~/.keys/'],
        correctIndices: [1],
        explanation: '~/.ssh/ är standardkatalogen för SSH-nycklar.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-8',
        question: 'Private key default name is...',
        options: ['id_rsa.pub', 'id_rsa', 'private_key', 'ssh_key'],
        correctIndices: [1],
        explanation: 'id_rsa är standardnamnet för privat nyckel.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-9',
        question: 'Public key default name is...',
        options: ['id_rsa', 'id_rsa.pub', 'public_key', 'ssh_key.pub'],
        correctIndices: [1],
        explanation: 'id_rsa.pub är standardnamnet för publik nyckel.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-10',
        question: 'To generate SSH key, use...',
        options: ['ssh-key', 'ssh-gen', 'ssh-keygen', 'keygen-ssh'],
        correctIndices: [2],
        explanation: 'ssh-keygen genererar SSH-nyckelpar.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-11',
        question: 'Authorized keys file is...',
        options: ['~/.ssh/authorized', '~/.ssh/keys', '~/.ssh/authorized_keys', '~/.ssh/allowed_keys'],
        correctIndices: [2],
        explanation: '~/.ssh/authorized_keys innehåller tillåtna publika nycklar.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-12',
        question: 'To copy key to server, use...',
        options: ['ssh-key-copy', 'copy-ssh-key', 'ssh-copy-id', 'scp-key'],
        correctIndices: [2],
        explanation: 'ssh-copy-id kopierar publik nyckel till servern.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-13',
        question: 'To disable password login, set...',
        options: ['PasswordLogin no', 'PasswordAuthentication no', 'AllowPassword no', 'DisablePassword yes'],
        correctIndices: [1],
        explanation: 'PasswordAuthentication no stänger av lösenordsinloggning.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-14',
        question: 'To disable root login, set...',
        options: ['RootLogin no', 'AllowRoot no', 'PermitRootLogin no', 'DisableRoot yes'],
        correctIndices: [2],
        explanation: 'PermitRootLogin no blockerar root-inloggning.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-15',
        question: 'To restart SSH service, use...',
        options: ['ssh restart', 'restart sshd', 'systemctl restart sshd', 'service ssh start'],
        correctIndices: [2],
        explanation: 'systemctl restart sshd startar om SSH-tjänsten.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-16',
        question: 'To copy file via SSH, use...',
        options: ['ssh-copy', 'scp', 'ssh-transfer', 'copy-ssh'],
        correctIndices: [1],
        explanation: 'scp (secure copy) kopierar filer via SSH.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-17',
        question: 'scp syntax is...',
        options: ['scp host:file local', 'scp source destination', 'scp file host', 'scp -f file host'],
        correctIndices: [1],
        explanation: 'scp source destination är grundsyntaxen.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-18',
        question: 'To copy directory via scp, use flag...',
        options: ['-d', '-r', '-a', '-dir'],
        correctIndices: [1],
        explanation: '-r kopierar rekursivt (hela kataloger).',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-19',
        question: 'sftp stands for...',
        options: ['Safe File Transfer Protocol', 'SSH File Transfer Protocol', 'Secure FTP', 'System File Transfer'],
        correctIndices: [1],
        explanation: 'SFTP = SSH File Transfer Protocol.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-20',
        question: 'The command to start sftp session is...',
        options: ['sftp host@user', 'sftp user@host', 'connect sftp host', 'ssh -ftp host'],
        correctIndices: [1],
        explanation: 'sftp user@host startar en SFTP-session.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-21',
        question: 'Ed25519 is...',
        options: ['A protocol', 'A key type', 'A port number', 'A cipher'],
        correctIndices: [1],
        explanation: 'Ed25519 är en modern och säker nyckeltyp.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-22',
        question: 'To generate Ed25519 key, use...',
        options: ['ssh-keygen -e ed25519', 'ssh-keygen -t ed25519', 'ssh-keygen -ed25519', 'ssh-keygen --ed25519'],
        correctIndices: [1],
        explanation: 'ssh-keygen -t ed25519 skapar Ed25519-nyckel.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-23',
        question: 'RSA recommended key size is...',
        options: ['1024 bits', '2048 bits', '4096 bits', '512 bits'],
        correctIndices: [2],
        explanation: '4096 bits rekommenderas för RSA-nycklar.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-24',
        question: '~/.ssh directory permission should be...',
        options: ['777', '755', '700', '644'],
        correctIndices: [2],
        explanation: '700 (rwx------) för ~/.ssh katalogen.',
        difficulty: 'G',
        category: 'SSH Rättigheter',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-25',
        question: 'Private key permission should be...',
        options: ['700', '644', '600', '755'],
        correctIndices: [2],
        explanation: '600 (rw-------) för privata nycklar.',
        difficulty: 'G',
        category: 'SSH Rättigheter',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-26',
        question: 'Public key permission should be...',
        options: ['600', '700', '644', '755'],
        correctIndices: [2],
        explanation: '644 (rw-r--r--) för publika nycklar.',
        difficulty: 'G',
        category: 'SSH Rättigheter',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-27',
        question: 'authorized_keys permission should be...',
        options: ['700', '600', '644', '755'],
        correctIndices: [1],
        explanation: '600 (rw-------) för authorized_keys.',
        difficulty: 'G',
        category: 'SSH Rättigheter',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-28',
        question: 'SSH agent is used to...',
        options: ['Monitor SSH', 'Cache private keys', 'Block attacks', 'Log connections'],
        correctIndices: [1],
        explanation: 'SSH-agent cachar privata nycklar i minnet.',
        difficulty: 'G',
        category: 'SSH Agent',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-29',
        question: 'To start SSH agent, use...',
        options: ['ssh-agent start', 'start ssh-agent', 'eval $(ssh-agent)', 'agent-ssh'],
        correctIndices: [2],
        explanation: 'eval $(ssh-agent) startar agenten och sätter miljövariabler.',
        difficulty: 'G',
        category: 'SSH Agent',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-30',
        question: 'To add key to agent, use...',
        options: ['ssh-key add', 'agent-add', 'ssh-add', 'add-key'],
        correctIndices: [2],
        explanation: 'ssh-add lägger till nycklar i agenten.',
        difficulty: 'G',
        category: 'SSH Agent',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-31',
        question: 'Select all valid SSH key types (choose 4):',
        options: ['rsa', 'aes', 'ed25519', 'sha256', 'ecdsa', 'md5', 'dsa', 'ssl', 'tls', 'pgp'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Giltiga SSH-nyckeltyper: rsa, ed25519, ecdsa, dsa.',
        difficulty: 'VG',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-32',
        question: 'UFW stands for...',
        options: ['Unix FireWall', 'Uncomplicated Firewall', 'Ubuntu Firewall', 'Unified Firewall'],
        correctIndices: [1],
        explanation: 'UFW = Uncomplicated Firewall.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-33',
        question: 'To enable UFW, use...',
        options: ['ufw start', 'ufw on', 'ufw enable', 'ufw activate'],
        correctIndices: [2],
        explanation: 'ufw enable aktiverar brandväggen.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-34',
        question: 'To disable UFW, use...',
        options: ['ufw stop', 'ufw off', 'ufw disable', 'ufw deactivate'],
        correctIndices: [2],
        explanation: 'ufw disable inaktiverar brandväggen.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-35',
        question: 'To check UFW status, use...',
        options: ['ufw check', 'ufw show', 'ufw status', 'ufw info'],
        correctIndices: [2],
        explanation: 'ufw status visar brandväggens status.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-36',
        question: 'To allow SSH in UFW, use...',
        options: ['ufw add ssh', 'ufw open 22', 'ufw allow ssh', 'ufw permit ssh'],
        correctIndices: [2],
        explanation: 'ufw allow ssh tillåter SSH-trafik.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-37',
        question: 'To allow port 80, use...',
        options: ['ufw add 80', 'ufw open 80', 'ufw allow 80', 'ufw permit 80'],
        correctIndices: [2],
        explanation: 'ufw allow 80 tillåter HTTP-trafik.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-38',
        question: 'To deny port 23, use...',
        options: ['ufw block 23', 'ufw reject 23', 'ufw deny 23', 'ufw close 23'],
        correctIndices: [2],
        explanation: 'ufw deny 23 blockerar Telnet-porten.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-39',
        question: 'To delete a rule, use...',
        options: ['ufw remove', 'ufw erase', 'ufw delete', 'ufw clear'],
        correctIndices: [2],
        explanation: 'ufw delete tar bort en regel.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-40',
        question: 'To allow from specific IP, use...',
        options: ['ufw allow ip 1.2.3.4', 'ufw allow from 1.2.3.4', 'ufw allow source 1.2.3.4', 'ufw allow 1.2.3.4'],
        correctIndices: [1],
        explanation: 'ufw allow from IP tillåter trafik från specifik IP.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-41',
        question: 'UFW default policy for incoming is...',
        options: ['allow', 'deny', 'reject', 'drop'],
        correctIndices: [1],
        explanation: 'Default policy för incoming är deny.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-42',
        question: 'To set default deny incoming, use...',
        options: ['ufw default deny in', 'ufw default deny incoming', 'ufw deny default incoming', 'ufw incoming deny'],
        correctIndices: [1],
        explanation: 'ufw default deny incoming sätter default policy.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-43',
        question: 'firewalld is used on...',
        options: ['Debian/Ubuntu', 'RHEL/CentOS/Fedora', 'Arch', 'Alpine'],
        correctIndices: [1],
        explanation: 'firewalld används på RHEL/CentOS/Fedora.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-44',
        question: 'firewalld command is...',
        options: ['firewalld', 'fwcmd', 'firewall-cmd', 'fwd'],
        correctIndices: [2],
        explanation: 'firewall-cmd är kommandot för firewalld.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-45',
        question: 'To list firewalld zones, use...',
        options: ['firewall-cmd --zones', 'firewall-cmd --list-zone', 'firewall-cmd --get-zones', 'firewall-cmd --show-zones'],
        correctIndices: [2],
        explanation: 'firewall-cmd --get-zones listar zoner.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-46',
        question: 'To add service permanently in firewalld, use...',
        options: ['firewall-cmd --add-service --save', 'firewall-cmd --permanent --service', 'firewall-cmd --permanent --add-service', 'firewall-cmd --add --permanent'],
        correctIndices: [2],
        explanation: '--permanent --add-service lägger till permanent.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-47',
        question: 'To reload firewalld, use...',
        options: ['firewall-cmd --restart', 'firewall-cmd --refresh', 'firewall-cmd --reload', 'firewall-cmd --update'],
        correctIndices: [2],
        explanation: 'firewall-cmd --reload laddar om regler.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-48',
        question: 'iptables is...',
        options: ['A frontend for UFW', 'The underlying Linux firewall', 'A Windows firewall', 'A router config'],
        correctIndices: [1],
        explanation: 'iptables är den underliggande Linux-brandväggen.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-49',
        question: 'To list iptables rules, use...',
        options: ['iptables --show', 'iptables --rules', 'iptables -L', 'iptables --list-all'],
        correctIndices: [2],
        explanation: 'iptables -L listar regler.',
        difficulty: 'G',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-50',
        question: 'Select all that are firewall tools (choose 4):',
        options: ['ufw', 'ssh', 'firewalld', 'scp', 'iptables', 'netstat', 'nftables', 'ping', 'curl', 'wget'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Brandväggsverktyg: ufw, firewalld, iptables, nftables.',
        difficulty: 'VG',
        category: 'Brandvägg',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-51',
        question: 'SSH tunnel local port forward uses flag...',
        options: ['-R', '-L', '-D', '-T'],
        correctIndices: [1],
        explanation: '-L skapar lokal port forwarding.',
        difficulty: 'G',
        category: 'SSH Tunnel',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-52',
        question: 'SSH tunnel remote port forward uses flag...',
        options: ['-L', '-R', '-D', '-T'],
        correctIndices: [1],
        explanation: '-R skapar remote port forwarding.',
        difficulty: 'G',
        category: 'SSH Tunnel',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-53',
        question: 'SSH dynamic port forward (SOCKS) uses flag...',
        options: ['-L', '-R', '-D', '-S'],
        correctIndices: [2],
        explanation: '-D skapar dynamisk SOCKS-proxy.',
        difficulty: 'G',
        category: 'SSH Tunnel',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-54',
        question: 'To run SSH in background, use flag...',
        options: ['-b', '-f', '-d', '-bg'],
        correctIndices: [1],
        explanation: '-f kör SSH i bakgrunden.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-55',
        question: 'To prevent SSH from executing command, use...',
        options: ['-n', '-N', '-x', '-X'],
        correctIndices: [1],
        explanation: '-N förhindrar kommandoexekvering.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-56',
        question: 'SSH X11 forwarding uses flag...',
        options: ['-x', '-X', '-Y', '-W'],
        correctIndices: [1],
        explanation: '-X aktiverar X11 forwarding.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-57',
        question: 'To use specific SSH key, use flag...',
        options: ['-k', '-i', '-key', '-f'],
        correctIndices: [1],
        explanation: '-i anger specifik identitetsfil.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-58',
        question: 'To use specific port, use flag...',
        options: ['-P', '-p', '-port', '-o port'],
        correctIndices: [1],
        explanation: '-p anger port.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-59',
        question: 'To enable verbose mode, use flag...',
        options: ['-d', '-v', '-verbose', '-V'],
        correctIndices: [1],
        explanation: '-v aktiverar verbose-läge.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-60',
        question: 'SSH jump host uses flag...',
        options: ['-j', '-J', '-jump', '-proxy'],
        correctIndices: [1],
        explanation: '-J anger jump host.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-61',
        question: 'fail2ban is used to...',
        options: ['Manage passwords', 'Encrypt traffic', 'Block repeated failed logins', 'Monitor bandwidth'],
        correctIndices: [2],
        explanation: 'fail2ban blockerar upprepade misslyckade inloggningsförsök.',
        difficulty: 'G',
        category: 'Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-62',
        question: 'fail2ban config is in...',
        options: ['/etc/fail2ban.conf', '/etc/fail2ban/config', '/etc/fail2ban/jail.local', '/etc/security/fail2ban'],
        correctIndices: [2],
        explanation: '/etc/fail2ban/jail.local är konfigurationsfilen.',
        difficulty: 'G',
        category: 'Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-63',
        question: 'To check fail2ban status, use...',
        options: ['fail2ban status', 'fail2ban-status', 'fail2ban-client status', 'systemctl fail2ban'],
        correctIndices: [2],
        explanation: 'fail2ban-client status visar status.',
        difficulty: 'G',
        category: 'Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-64',
        question: 'To unban IP in fail2ban, use...',
        options: ['fail2ban unban IP', 'fail2ban-client remove IP', 'fail2ban-client unban IP', 'fail2ban release IP'],
        correctIndices: [2],
        explanation: 'fail2ban-client unban IP avblockerar en IP.',
        difficulty: 'G',
        category: 'Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-65',
        question: 'SSH host key is stored in...',
        options: ['~/.ssh/host_key', '/etc/ssh/keys/', '/etc/ssh/ssh_host_*', '/var/ssh/host'],
        correctIndices: [2],
        explanation: '/etc/ssh/ssh_host_* innehåller serverns hostnycklar.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-66',
        question: 'known_hosts file contains...',
        options: ['Allowed users', 'Server fingerprints', 'Private keys', 'Passwords'],
        correctIndices: [1],
        explanation: 'known_hosts innehåller serverfingeravtryck.',
        difficulty: 'G',
        category: 'SSH Nycklar',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-67',
        question: 'To remove host from known_hosts, use...',
        options: ['ssh-keygen -d host', 'ssh-keygen -R host', 'ssh-remove host', 'ssh -remove host'],
        correctIndices: [1],
        explanation: 'ssh-keygen -R host tar bort en host från known_hosts.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-68',
        question: 'StrictHostKeyChecking controls...',
        options: ['Key strength', 'Unknown host prompts', 'Password policy', 'Connection timeout'],
        correctIndices: [1],
        explanation: 'StrictHostKeyChecking styr hur okända hosts hanteras.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-69',
        question: 'To specify SSH user in config, use...',
        options: ['Username', 'User', 'Login', 'Account'],
        correctIndices: [1],
        explanation: 'User anger användarnamn i config.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-70',
        question: 'To specify identity file in config, use...',
        options: ['Key', 'IdentityFile', 'PrivateKey', 'KeyFile'],
        correctIndices: [1],
        explanation: 'IdentityFile anger sökväg till nyckel.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-71',
        question: 'Select valid ~/.ssh/config options (choose 4):',
        options: ['Host', 'Server', 'User', 'Account', 'Port', 'Number', 'IdentityFile', 'KeyPath', 'Remote', 'Connect'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Giltiga config-alternativ: Host, User, Port, IdentityFile.',
        difficulty: 'VG',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-72',
        question: 'ClientAliveInterval setting...',
        options: ['Limits connection time', 'Sends keepalive packets', 'Sets timeout', 'Logs activity'],
        correctIndices: [1],
        explanation: 'ClientAliveInterval skickar keepalive-paket.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-73',
        question: 'MaxAuthTries setting limits...',
        options: ['Connections per IP', 'Users per session', 'Authentication attempts', 'Keys per user'],
        correctIndices: [2],
        explanation: 'MaxAuthTries begränsar autentiseringsförsök.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-74',
        question: 'AllowUsers setting...',
        options: ['Restricts SSH to specific users', 'Allows all users', 'Sets user permissions', 'Creates users'],
        correctIndices: [0],
        explanation: 'AllowUsers begränsar vilka användare som kan SSH:a.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-75',
        question: 'DenyUsers setting...',
        options: ['Denies all users', 'Blocks specific users', 'Disables SSH', 'Logs denied users'],
        correctIndices: [1],
        explanation: 'DenyUsers blockerar specifika användare.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-76',
        question: 'To check SSH connection without login, use...',
        options: ['ssh -check host', 'ssh -test host', 'ssh -T host', 'ssh -verify host'],
        correctIndices: [2],
        explanation: 'ssh -T testar anslutning utan terminal.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-77',
        question: 'SSH escape character is...',
        options: ['Ctrl+C', '~', '^', 'ESC'],
        correctIndices: [1],
        explanation: '~ är SSH:s escape-tecken.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-78',
        question: 'To terminate stuck SSH, type...',
        options: ['~c', '~.', '~q', '~x'],
        correctIndices: [1],
        explanation: '~. avslutar en hängd SSH-session.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-79',
        question: 'To check open ports, use...',
        options: ['ports', 'open', 'ss -tuln', 'netstat'],
        correctIndices: [2],
        explanation: 'ss -tuln visar öppna TCP/UDP-portar.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-80',
        question: 'ss stands for...',
        options: ['System Status', 'Socket Statistics', 'Server Status', 'Secure Shell'],
        correctIndices: [1],
        explanation: 'ss = Socket Statistics.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-81',
        question: 'Select all ss flags (choose 4):',
        options: ['-t', '-x', '-u', '-y', '-l', '-z', '-n', '-w', '-q', '-v'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Giltiga ss-flaggor: -t (TCP), -u (UDP), -l (listening), -n (numeric).',
        difficulty: 'VG',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-82',
        question: 'ss -t shows...',
        options: ['Total connections', 'TCP connections', 'Time info', 'TLS info'],
        correctIndices: [1],
        explanation: 'ss -t visar TCP-anslutningar.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-83',
        question: 'ss -u shows...',
        options: ['User connections', 'UDP connections', 'Unix sockets', 'Upstream'],
        correctIndices: [1],
        explanation: 'ss -u visar UDP-anslutningar.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-84',
        question: 'ss -l shows...',
        options: ['Long format', 'Listening ports', 'Local only', 'Logged users'],
        correctIndices: [1],
        explanation: 'ss -l visar lyssnande portar.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-85',
        question: 'ss -n shows...',
        options: ['Network info', 'Node info', 'Numeric ports (no resolve)', 'New connections'],
        correctIndices: [2],
        explanation: 'ss -n visar numeriska portar utan namnupplösning.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-86',
        question: 'netstat is...',
        options: ['Newer than ss', 'Older than ss', 'Same as ss', 'Different purpose'],
        correctIndices: [1],
        explanation: 'netstat är äldre än ss.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-87',
        question: 'To see who is using a port, use...',
        options: ['portuser', 'lsof -i :port', 'who -p port', 'ps -p port'],
        correctIndices: [1],
        explanation: 'lsof -i :port visar vilken process som använder porten.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-88',
        question: 'lsof stands for...',
        options: ['List Socket Files', 'List Open Files', 'List System Files', 'Linux Socket Files'],
        correctIndices: [1],
        explanation: 'lsof = List Open Files.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-89',
        question: 'To ping with specific count, use...',
        options: ['ping -n 5', 'ping -c 5', 'ping -count 5', 'ping -5'],
        correctIndices: [1],
        explanation: 'ping -c 5 skickar 5 ping-paket.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-90',
        question: 'To see route to host, use...',
        options: ['route host', 'path host', 'traceroute host', 'follow host'],
        correctIndices: [2],
        explanation: 'traceroute visar rutten till en host.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-91',
        question: 'Select ports that should typically be blocked (choose 3):',
        options: ['22', '23', '80', '3389', '443', '21', '53', '25', '143', '993'],
        correctIndices: [1, 3, 5],
        explanation: 'Blockera: 23 (Telnet), 3389 (RDP), 21 (FTP) - osäkra eller onödiga.',
        difficulty: 'VG',
        category: 'Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-92',
        question: 'Port 23 is for...',
        options: ['SSH', 'Telnet', 'FTP', 'HTTP'],
        correctIndices: [1],
        explanation: 'Port 23 är Telnet.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-93',
        question: 'Telnet is insecure because...',
        options: ["It's slow", 'Traffic is unencrypted', 'It uses wrong port', 'It needs root'],
        correctIndices: [1],
        explanation: 'Telnet är osäkert för att trafiken är okrypterad.',
        difficulty: 'G',
        category: 'Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-94',
        question: 'To test if port is open, use...',
        options: ['test port', 'check port', 'nc -zv host port', 'open port'],
        correctIndices: [2],
        explanation: 'nc -zv host port testar om en port är öppen.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-95',
        question: 'nc stands for...',
        options: ['Network Check', 'Netcat', 'Net Connect', 'Network Cat'],
        correctIndices: [1],
        explanation: 'nc = Netcat.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-96',
        question: 'nmap is used for...',
        options: ['Network mapping', 'Port scanning', 'Both', 'Neither'],
        correctIndices: [2],
        explanation: 'nmap används för både nätverksmappning och portskanning.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-97',
        question: 'To scan ports with nmap, use...',
        options: ['nmap --scan host', 'nmap host', 'nmap -ports host', 'nmap -p host'],
        correctIndices: [1],
        explanation: 'nmap host skannar en host.',
        difficulty: 'G',
        category: 'Nätverk',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-98',
        question: 'Default SSH timeout is...',
        options: ['30 seconds', 'No timeout (depends on config)', '60 seconds', '5 minutes'],
        correctIndices: [1],
        explanation: 'SSH har ingen fast timeout - beror på konfiguration.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-99',
        question: 'TCPKeepAlive setting...',
        options: ['Limits connections', 'Prevents connection drop', 'Logs traffic', 'Encrypts data'],
        correctIndices: [1],
        explanation: 'TCPKeepAlive förhindrar att anslutningen tappar.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-100',
        question: 'SSH compression uses flag...',
        options: ['-z', '-C', '-compress', '-Z'],
        correctIndices: [1],
        explanation: '-C aktiverar komprimering.',
        difficulty: 'G',
        category: 'SSH Flaggor',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-101',
        question: 'To forward local 8080 to remote 80...',
        options: ['ssh -R 8080:localhost:80', 'ssh -L 8080:localhost:80', 'ssh -L 80:8080', 'ssh -R 80:8080'],
        correctIndices: [1],
        explanation: '-L 8080:localhost:80 gör lokal port forwarding.',
        difficulty: 'G',
        category: 'SSH Tunnel',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-102',
        question: 'Public key authentication is...',
        options: ['Less secure than password', 'More secure than password', 'Same as password', 'Not recommended'],
        correctIndices: [1],
        explanation: 'Nyckelautentisering är säkrare än lösenord.',
        difficulty: 'G',
        category: 'SSH Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-103',
        question: 'AuthorizedKeysFile setting specifies...',
        options: ['Private key location', 'Public key location', 'Host key location', 'Known hosts location'],
        correctIndices: [1],
        explanation: 'AuthorizedKeysFile anger var publika nycklar lagras.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-104',
        question: 'PubkeyAuthentication must be...',
        options: ['no', 'yes', 'disabled', 'optional'],
        correctIndices: [1],
        explanation: 'PubkeyAuthentication yes för att aktivera nyckelauth.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-105',
        question: 'To use bastion/jump host...',
        options: ['ssh -j host1 host2', 'ssh -J host1 host2', 'ssh -jump host1 host2', 'ssh host1 -then host2'],
        correctIndices: [1],
        explanation: '-J anger jump/bastion host.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-106',
        question: 'Select all that harden SSH (choose 4):',
        options: ['PasswordAuthentication no', 'PasswordAuthentication yes', 'PermitRootLogin no', 'PermitRootLogin yes', 'MaxAuthTries 3', 'MaxAuthTries 100', 'AllowUsers specific', 'AllowUsers all', 'Port 22', 'PermitEmptyPasswords yes'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'SSH-härdning: PasswordAuthentication no, PermitRootLogin no, MaxAuthTries 3, AllowUsers specific.',
        difficulty: 'VG',
        category: 'SSH Säkerhet',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-107',
        question: 'SSH protocol version is...',
        options: ['1', '2', '3', '1.5'],
        correctIndices: [1],
        explanation: 'SSH protokollversion 2 är standard.',
        difficulty: 'G',
        category: 'SSH Grundläggande',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-108',
        question: 'SSH protocol 1 is...',
        options: ['Recommended', 'Current', 'Deprecated/insecure', 'Fastest'],
        correctIndices: [2],
        explanation: 'SSH protokoll 1 är deprecated och osäkert.',
        difficulty: 'G',
        category: 'SSH Grundläggande',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-109',
        question: 'To see SSH version, use...',
        options: ['ssh --version', 'ssh -V', 'ssh -v', 'ssh version'],
        correctIndices: [1],
        explanation: 'ssh -V visar version.',
        difficulty: 'G',
        category: 'SSH Kommandon',
        topic: 'ssh-brandvagg'
    },
    {
        id: 'omtenta-v2-ssh-110',
        question: 'Banner setting in sshd_config...',
        options: ['Shows system info', 'Displays message before login', 'Hides hostname', 'Logs connections'],
        correctIndices: [1],
        explanation: 'Banner visar ett meddelande före inloggning.',
        difficulty: 'G',
        category: 'SSH Konfiguration',
        topic: 'ssh-brandvagg'
    }
]
