/**
 * NOD 5: SSH & Kommunikation - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD5_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod5-s1',
        question: 'Du ska generera ett SSH-nyckelpar för säker inloggning till prod-servrar. Vilket kommando?',
        options: ['ssh-keygen', 'ssh-create', 'openssl genkey', 'ssh --generate-key'],
        correctIndices: [0],
        explanation: 'ssh-keygen genererar nyckelpar. Default är RSA men du kan ange -t ed25519 för modernare algoritm.',
        difficulty: 'G',
        category: 'SSH-nycklar',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s2',
        question: 'Du har genererat en publik nyckel. Var på målservern ska den läggas för att fungera?',
        options: ['/etc/ssh/keys', '~/.ssh/authorized_keys', '~/.ssh/known_hosts', '/root/ssh_keys'],
        correctIndices: [1],
        explanation: 'Publika nycklar läggs i ~/.ssh/authorized_keys på servern. known_hosts innehåller servrar du anslutit till.',
        difficulty: 'G',
        category: 'SSH-nycklar',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s3',
        question: 'Du vill kopiera din publika nyckel till en ny server. Vilket kommando gör det automatiskt?',
        options: ['scp ~/.ssh/id_rsa.pub user@server:', 'ssh-copy-id user@server', 'ssh-add user@server', 'cp ~/.ssh/id_rsa.pub user@server'],
        correctIndices: [1],
        explanation: 'ssh-copy-id kopierar automatiskt din publika nyckel till serverns authorized_keys och sätter rätt permissions.',
        difficulty: 'G',
        category: 'SSH-nycklar',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s4',
        question: 'Du behöver kopiera en fil från lokal maskin till server. Kommando?',
        options: ['cp file.txt user@server:/path/', 'scp file.txt user@server:/path/', 'ssh cp file.txt /path/', 'copy file.txt user@server:/path/'],
        correctIndices: [1],
        explanation: 'scp (secure copy) använder SSH för säker filöverföring. Syntax: scp källa mål.',
        difficulty: 'G',
        category: 'SCP',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s5',
        question: 'Du vill synka en katalog till servern och bara kopiera ändrade filer. Vilket verktyg?',
        options: ['scp -r', 'rsync -avz', 'sync -r', 'mirror --incremental'],
        correctIndices: [1],
        explanation: 'rsync är effektivare än scp - kopierar bara ändringar. -a=archive, -v=verbose, -z=compress.',
        difficulty: 'VG',
        category: 'Rsync',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s6',
        question: 'Du skriver ssh user@server och får "Permission denied (publickey)". Vad är troligen fel?',
        options: ['Servern är nere', 'Din publika nyckel finns inte i serverns authorized_keys', 'Du har fel SSH-version', 'Porten är blockerad'],
        correctIndices: [1],
        explanation: 'Meddelandet säger att server kräver nyckelauth men din nyckel finns inte/matchar inte på servern.',
        difficulty: 'G',
        category: 'Felsökning',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s7',
        question: 'Du vill ansluta till en databas på 10.0.0.5:5432 genom en SSH-tunnel via jump-server. Hur?',
        options: ['ssh -L 5432:10.0.0.5:5432 user@jumpserver', 'ssh -R 5432:10.0.0.5:5432 user@jumpserver', 'ssh --tunnel 5432 user@jumpserver', 'ssh -D 5432 user@jumpserver'],
        correctIndices: [0],
        explanation: '-L skapar lokal port forwarding. localhost:5432 tunnlas till 10.0.0.5:5432 via jumpserver.',
        difficulty: 'VG',
        category: 'SSH-tunnel',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s8',
        question: 'Du vill slippa skriva hela "ssh deploy@prod.example.com" varje gång. Var konfigurerar du alias?',
        options: ['/etc/ssh/ssh_config', '~/.ssh/config', '~/.bashrc', '/etc/hosts'],
        correctIndices: [1],
        explanation: '~/.ssh/config innehåller per-user SSH-config. Du kan definiera Host prod med alla detaljer.',
        difficulty: 'VG',
        category: 'SSH-config',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s9',
        question: 'Din privata nyckel har permissions 644. SSH vägrar använda den. Vilka permissions behövs?',
        options: ['777', '644', '600', '755'],
        correctIndices: [2],
        explanation: 'SSH kräver att privata nycklar är 600 (bara ägaren kan läsa). För lösa permissions = säkerhetsrisk.',
        difficulty: 'G',
        category: 'SSH-nycklar',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s10',
        question: 'Du använder ssh-agent för att slippa skriva passphrase varje gång. Hur lägger du till din nyckel?',
        options: ['ssh-add ~/.ssh/id_rsa', 'ssh-agent add ~/.ssh/id_rsa', 'ssh --add-key ~/.ssh/id_rsa', 'agent-add ~/.ssh/id_rsa'],
        correctIndices: [0],
        explanation: 'ssh-add lägger till nycklar i körande ssh-agent. Agenten håller dekrypterade nycklar i minnet.',
        difficulty: 'G',
        category: 'SSH-agent',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s11',
        question: 'Du behöver köra ett kommando på servern utan interaktiv session. Hur?',
        options: ['ssh user@server && kommando', 'ssh user@server "kommando"', 'ssh --exec kommando user@server', 'ssh user@server | kommando'],
        correctIndices: [1],
        explanation: 'ssh user@server "kommando" kör kommandot direkt och stänger sedan anslutningen. Perfekt för automation.',
        difficulty: 'G',
        category: 'SSH',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s12',
        question: 'Du får varning "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!". Vad betyder det?',
        options: ['Du har fel lösenord', 'Serverns host key har ändrats - möjlig man-in-the-middle', 'SSH-versionen är för gammal', 'Din nyckel har gått ut'],
        correctIndices: [1],
        explanation: 'Host key ändring kan betyda att servern ominstallerades (OK) eller attack (farligt). Verifiera innan du accepterar.',
        difficulty: 'VG',
        category: 'Säkerhet',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s13',
        question: 'Du vill testa SSH-anslutning med verbose output för felsökning. Flagga?',
        options: ['ssh -v user@server', 'ssh --debug user@server', 'ssh -verbose user@server', 'ssh -d user@server'],
        correctIndices: [0],
        explanation: '-v = verbose. Kan upprepas: -vv eller -vvv för mer detaljer. Visar hela handshake-processen.',
        difficulty: 'G',
        category: 'Felsökning',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s14',
        question: 'SSH körs på port 22 default. Om servern kör SSH på port 2222 istället?',
        options: ['ssh user@server:2222', 'ssh -p 2222 user@server', 'ssh user@server --port 2222', 'ssh user@server/2222'],
        correctIndices: [1],
        explanation: '-p anger port. I ~/.ssh/config kan du sätta Port 2222 för specifik host.',
        difficulty: 'G',
        category: 'SSH',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s15',
        question: 'Du vill inaktivera root login via SSH på en server. Var gör du det?',
        options: ['/etc/passwd', '/etc/ssh/sshd_config', '~/.ssh/config', '/root/.ssh/authorized_keys'],
        correctIndices: [1],
        explanation: 'sshd_config (server-config) har PermitRootLogin no. ~/.ssh/config är klient-config.',
        difficulty: 'VG',
        category: 'SSH-config',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s16',
        question: 'Vilken algoritm rekommenderas för nya SSH-nycklar 2024+?',
        options: ['RSA 1024', 'DSA', 'Ed25519', 'RSA 512'],
        correctIndices: [2],
        explanation: 'Ed25519 är snabb, säker och modern. RSA funkar med minst 2048 bitar. DSA är deprecated.',
        difficulty: 'VG',
        category: 'SSH-nycklar',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s17',
        question: 'Du vill hoppa via en bastion/jump-host för att nå intern server. Kommando?',
        options: ['ssh -J bastion user@internal', 'ssh -o "ProxyJump bastion" user@internal', 'ssh bastion ssh internal', 'Alla fungerar'],
        correctIndices: [3],
        explanation: '-J (ProxyJump) är modernast. Kan också konfigureras i ~/.ssh/config med ProxyJump.',
        difficulty: 'VG',
        category: 'SSH-tunnel',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s18',
        question: 'Du behöver ladda ner en katalog rekursivt från server med scp. Flagga?',
        options: ['scp -r user@server:/path /local/', 'scp -R user@server:/path /local/', 'scp --recursive user@server:/path /local/', 'scp -a user@server:/path /local/'],
        correctIndices: [0],
        explanation: '-r = recursive för kataloger med scp. Kopierar hela katalogstrukturen.',
        difficulty: 'G',
        category: 'SCP',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s19',
        question: 'Du vill att SSH-agent vidarebefordras till servern så du kan hoppa vidare därifrån. Flagga?',
        options: ['ssh -A user@server', 'ssh --forward-agent user@server', 'ssh -F user@server', 'ssh -X user@server'],
        correctIndices: [0],
        explanation: '-A aktiverar agent forwarding. Var försiktig - root på mellanservern kan använda dina nycklar!',
        difficulty: 'VG',
        category: 'SSH-agent',
        topic: 'nod5-ssh',
        type: 'scenario'
    },
    {
        id: 'nod5-s20',
        question: 'Du behöver radera en gammal host key från known_hosts efter serverominstallation. Kommando?',
        options: ['rm ~/.ssh/known_hosts', 'ssh-keygen -R hostname', 'ssh --remove-key hostname', 'known_hosts -d hostname'],
        correctIndices: [1],
        explanation: 'ssh-keygen -R tar bort specifik host. rm raderar ALLA kända hosts vilket är onödigt.',
        difficulty: 'G',
        category: 'SSH-nycklar',
        topic: 'nod5-ssh',
        type: 'scenario'
    }
]
