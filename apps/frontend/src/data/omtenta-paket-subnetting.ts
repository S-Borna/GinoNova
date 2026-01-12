/**
 * INFÖR OMTENTA - Pakethantering & SSH-nycklar + Subnetting
 * 100 frågor (50 + 50)
 * 
 * Baserat på:
 * - Handson - Pakethantering & SSH-nycklar.md
 * - Handson - Subnetting.md
 */

import { OmtentaQuestion } from './omtenta-ssh-brandvagg'

// ============================================
// PAKETHANTERING & SSH-NYCKLAR (50 frågor)
// ============================================

export const PAKETHANTERING_QUESTIONS: OmtentaQuestion[] = [
    // APT grundläggande
    {
        id: 'paket-001',
        question: 'Vilket kommando uppdaterar listan över tillgängliga paket i APT?',
        options: ['apt update', 'apt upgrade', 'apt refresh', 'apt sync'],
        correctIndex: 0,
        explanation: 'apt update hämtar den senaste paketlistan från repositories utan att installera något.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-002',
        question: 'Vad gör kommandot "apt upgrade"?',
        options: [
            'Uppdaterar paketlistan',
            'Uppgraderar alla installerade paket till senaste version',
            'Tar bort gamla paket',
            'Installerar nya paket'
        ],
        correctIndex: 1,
        explanation: 'apt upgrade uppgraderar alla installerade paket till senaste tillgängliga version.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-003',
        question: 'Vilket kommando installerar ett paket med APT?',
        options: ['apt get nginx', 'apt install nginx', 'apt add nginx', 'apt setup nginx'],
        correctIndex: 1,
        explanation: 'apt install <paketnamn> installerar det angivna paketet.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-004',
        question: 'Hur tar du bort ett paket MED dess konfigurationsfiler?',
        options: ['apt remove nginx', 'apt purge nginx', 'apt delete nginx', 'apt uninstall nginx'],
        correctIndex: 1,
        explanation: 'apt purge tar bort paketet OCH dess konfigurationsfiler, till skillnad från remove som behåller config.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-005',
        question: 'Vad är skillnaden mellan "apt remove" och "apt purge"?',
        options: [
            'Ingen skillnad',
            'remove tar bort paket, purge tar bort paket + konfigurationsfiler',
            'purge är snabbare',
            'remove kräver sudo, purge gör det inte'
        ],
        correctIndex: 1,
        explanation: 'apt remove behåller konfigurationsfilerna, apt purge tar bort allt inklusive config.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-006',
        question: 'Vilket kommando tar bort oanvända beroenden (orphan packages)?',
        options: ['apt clean', 'apt autoremove', 'apt autoclean', 'apt orphan'],
        correctIndex: 1,
        explanation: 'apt autoremove tar bort paket som installerats som beroenden men inte längre behövs.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-007',
        question: 'Vad gör "apt search nginx"?',
        options: [
            'Installerar nginx',
            'Söker efter paket som matchar "nginx"',
            'Visar nginx-version',
            'Uppdaterar nginx'
        ],
        correctIndex: 1,
        explanation: 'apt search söker i paketdatabasen efter paket som matchar söksträngen.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-008',
        question: 'Hur visar du information om ett specifikt paket?',
        options: ['apt info nginx', 'apt show nginx', 'apt describe nginx', 'apt details nginx'],
        correctIndex: 1,
        explanation: 'apt show visar detaljerad information om ett paket.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-009',
        question: 'Var lagras APT:s paketlistor?',
        options: ['/etc/apt/', '/var/lib/apt/lists/', '/var/cache/apt/', '/usr/share/apt/'],
        correctIndex: 1,
        explanation: '/var/lib/apt/lists/ innehåller nedladdade paketlistor från repositories.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-010',
        question: 'Var definieras APT repositories?',
        options: ['/etc/apt/sources.list', '/var/apt/repos', '/etc/repos.conf', '/usr/apt/sources'],
        correctIndex: 0,
        explanation: '/etc/apt/sources.list och /etc/apt/sources.list.d/ definierar repositories.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    // SSH-nycklar
    {
        id: 'paket-011',
        question: 'Vilket kommando genererar ett SSH-nyckelpar?',
        options: ['ssh-create', 'ssh-keygen', 'ssh-newkey', 'ssh-generate'],
        correctIndex: 1,
        explanation: 'ssh-keygen genererar ett nytt SSH-nyckelpar (privat och publik nyckel).',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-012',
        question: 'Var lagras den privata SSH-nyckeln som standard?',
        options: ['~/.ssh/id_rsa', '~/.ssh/id_rsa.pub', '/etc/ssh/private_key', '~/.keys/private'],
        correctIndex: 0,
        explanation: 'Den privata nyckeln lagras i ~/.ssh/id_rsa (eller id_ed25519 för nyare algoritmer).',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-013',
        question: 'Vilken fil innehåller den publika SSH-nyckeln?',
        options: ['~/.ssh/id_rsa', '~/.ssh/id_rsa.pub', '~/.ssh/known_hosts', '~/.ssh/config'],
        correctIndex: 1,
        explanation: 'Den publika nyckeln har filtillägget .pub (t.ex. id_rsa.pub).',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-014',
        question: 'Vilken fil på servern måste innehålla din publika nyckel för SSH-inloggning?',
        options: ['~/.ssh/known_hosts', '~/.ssh/authorized_keys', '~/.ssh/public_keys', '~/.ssh/allowed'],
        correctIndex: 1,
        explanation: 'authorized_keys innehåller publika nycklar som får logga in på kontot.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-015',
        question: 'Vilket kommando kopierar din publika nyckel till en server?',
        options: ['ssh-copy-key', 'ssh-copy-id', 'scp ~/.ssh/id_rsa.pub', 'ssh-add'],
        correctIndex: 1,
        explanation: 'ssh-copy-id kopierar automatiskt din publika nyckel till serverns authorized_keys.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-016',
        question: 'Vilka rättigheter ska ~/.ssh/-mappen ha?',
        options: ['777', '755', '700', '644'],
        correctIndex: 2,
        explanation: '~/.ssh/ ska ha 700 (drwx------) - endast ägaren får läsa/skriva/exekvera.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-017',
        question: 'Vilka rättigheter ska den privata SSH-nyckeln ha?',
        options: ['644', '700', '600', '400'],
        correctIndex: 2,
        explanation: 'Privata nycklar ska ha 600 (-rw-------) - endast ägaren får läsa/skriva.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-018',
        question: 'Vad gör kommandot "ssh-add"?',
        options: [
            'Lägger till en SSH-server',
            'Lägger till en nyckel till SSH-agenten',
            'Skapar en ny nyckel',
            'Lägger till en användare'
        ],
        correctIndex: 1,
        explanation: 'ssh-add lägger till privata nycklar till SSH-agenten för automatisk autentisering.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-019',
        question: 'Vilken SSH-nyckelalgoritm rekommenderas idag?',
        options: ['RSA 1024', 'DSA', 'Ed25519', 'RSA 512'],
        correctIndex: 2,
        explanation: 'Ed25519 är den rekommenderade algoritmen - snabb, säker och med korta nycklar.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-020',
        question: 'Hur genererar du en Ed25519-nyckel?',
        options: [
            'ssh-keygen -t ed25519',
            'ssh-keygen -t rsa -b 25519',
            'ssh-keygen --ed25519',
            'ssh-create ed25519'
        ],
        correctIndex: 0,
        explanation: 'ssh-keygen -t ed25519 skapar en Ed25519-nyckel.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    // Mer pakethantering
    {
        id: 'paket-021',
        question: 'Vad gör "apt list --installed"?',
        options: [
            'Listar tillgängliga paket',
            'Listar alla installerade paket',
            'Installerar paket från lista',
            'Visar senaste installationer'
        ],
        correctIndex: 1,
        explanation: 'apt list --installed visar alla paket som är installerade på systemet.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-022',
        question: 'Vilket kommando visar vilka filer ett paket har installerat?',
        options: ['apt files nginx', 'dpkg -L nginx', 'apt show --files nginx', 'rpm -ql nginx'],
        correctIndex: 1,
        explanation: 'dpkg -L <paket> listar alla filer som installerats av paketet.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-023',
        question: 'Hur tar du reda på vilket paket en fil tillhör?',
        options: ['apt which /usr/bin/nginx', 'dpkg -S /usr/bin/nginx', 'apt owner /usr/bin/nginx', 'which-pkg /usr/bin/nginx'],
        correctIndex: 1,
        explanation: 'dpkg -S <filsökväg> visar vilket paket som äger filen.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-024',
        question: 'Vad gör "apt-cache policy nginx"?',
        options: [
            'Visar säkerhetspolicy',
            'Visar installerad och tillgänglig version samt repository',
            'Ändrar installationspolicy',
            'Blockerar paketet'
        ],
        correctIndex: 1,
        explanation: 'apt-cache policy visar versioner och från vilket repository paketet kommer.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-025',
        question: 'Hur installerar du en specifik version av ett paket?',
        options: [
            'apt install nginx --version=1.18',
            'apt install nginx=1.18.0-0ubuntu1',
            'apt install nginx-1.18',
            'apt version nginx 1.18'
        ],
        correctIndex: 1,
        explanation: 'apt install paket=version installerar en specifik version.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-026',
        question: 'Vad gör "apt-mark hold nginx"?',
        options: [
            'Pausar nginx-tjänsten',
            'Förhindrar att nginx uppgraderas',
            'Låser nginx-konfigurationen',
            'Sätter nginx på väntelista'
        ],
        correctIndex: 1,
        explanation: 'apt-mark hold förhindrar att paketet uppgraderas vid apt upgrade.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-027',
        question: 'Hur tar du bort "hold" från ett paket?',
        options: ['apt-mark release nginx', 'apt-mark unhold nginx', 'apt-mark free nginx', 'apt-mark unlock nginx'],
        correctIndex: 1,
        explanation: 'apt-mark unhold tar bort hold-markeringen så paketet kan uppgraderas igen.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-028',
        question: 'Vad är ett PPA (Personal Package Archive)?',
        options: [
            'En privat backup',
            'Ett tredjepartsrepository för Ubuntu',
            'En paketarkivkomprimering',
            'En säkerhetskopia av paket'
        ],
        correctIndex: 1,
        explanation: 'PPA är ett tredjepartsrepository på Launchpad för Ubuntu-paket.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-029',
        question: 'Hur lägger du till ett PPA?',
        options: [
            'apt add ppa:user/repo',
            'add-apt-repository ppa:user/repo',
            'ppa-add user/repo',
            'apt-add ppa:user/repo'
        ],
        correctIndex: 1,
        explanation: 'add-apt-repository ppa:user/repo lägger till ett PPA.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-030',
        question: 'Vad gör "apt clean"?',
        options: [
            'Rensar paketdatabasen',
            'Tar bort nedladdade .deb-filer från cache',
            'Avinstallerar alla paket',
            'Rensar systemloggar'
        ],
        correctIndex: 1,
        explanation: 'apt clean tar bort alla nedladdade paketfiler från /var/cache/apt/archives/.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    // SSH-nycklar fortsättning
    {
        id: 'paket-031',
        question: 'Vad innehåller ~/.ssh/known_hosts?',
        options: [
            'Tillåtna publika nycklar',
            'Fingeravtryck för servrar du anslutit till',
            'Dina privata nycklar',
            'SSH-konfiguration'
        ],
        correctIndex: 1,
        explanation: 'known_hosts lagrar servernycklar för att förhindra man-in-the-middle-attacker.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-032',
        question: 'Vad händer om serverns nyckel ändras efter att du sparat den i known_hosts?',
        options: [
            'Anslutningen fungerar normalt',
            'SSH varnar och vägrar ansluta',
            'Nyckeln uppdateras automatiskt',
            'SSH frågar om nytt lösenord'
        ],
        correctIndex: 1,
        explanation: 'SSH varnar för potentiell man-in-the-middle-attack om servernyckeln ändrats.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-033',
        question: 'Hur tar du bort en gammal servernyckel från known_hosts?',
        options: [
            'ssh-keygen -R hostname',
            'ssh-remove hostname',
            'rm ~/.ssh/known_hosts',
            'ssh-clean hostname'
        ],
        correctIndex: 0,
        explanation: 'ssh-keygen -R hostname tar bort en specifik host från known_hosts.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-034',
        question: 'Vad är en SSH-agent?',
        options: [
            'En SSH-server',
            'Ett program som håller nycklar i minnet för automatisk autentisering',
            'En SSH-klient',
            'En nätverksmonitor'
        ],
        correctIndex: 1,
        explanation: 'SSH-agenten lagrar dekrypterade privata nycklar i minnet.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-035',
        question: 'Hur startar du SSH-agenten i bash?',
        options: [
            'ssh-agent start',
            'eval $(ssh-agent)',
            'start ssh-agent',
            'agent-ssh run'
        ],
        correctIndex: 1,
        explanation: 'eval $(ssh-agent) startar agenten och sätter miljövariabler.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-036',
        question: 'Hur visar du nycklar som laddats i SSH-agenten?',
        options: ['ssh-add -l', 'ssh-list', 'ssh-agent --list', 'ssh-keys'],
        correctIndex: 0,
        explanation: 'ssh-add -l listar fingeravtryck för alla laddade nycklar.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-037',
        question: 'Vad gör "ssh-add -D"?',
        options: [
            'Visar debuginfo',
            'Tar bort alla nycklar från agenten',
            'Laddar standardnyckeln',
            'Duplicerar nycklar'
        ],
        correctIndex: 1,
        explanation: 'ssh-add -D tar bort alla nycklar från SSH-agenten.',
        difficulty: 'VG',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-038',
        question: 'Var konfigurerar du SSH-klienten för olika hostar?',
        options: ['/etc/ssh/ssh_config', '~/.ssh/config', '~/.ssh/hosts', '/etc/hosts'],
        correctIndex: 1,
        explanation: '~/.ssh/config innehåller användarspecifika SSH-klientinställningar.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-039',
        question: 'Hur anger du en specifik nyckel vid SSH-anslutning?',
        options: [
            'ssh -k ~/.ssh/mykey user@host',
            'ssh -i ~/.ssh/mykey user@host',
            'ssh --key ~/.ssh/mykey user@host',
            'ssh -key mykey user@host'
        ],
        correctIndex: 1,
        explanation: 'ssh -i <keyfile> anger vilken privat nyckel som ska användas.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    {
        id: 'paket-040',
        question: 'Vad gör passphrase på en SSH-nyckel?',
        options: [
            'Identifierar nyckeln',
            'Krypterar den privata nyckeln',
            'Sätter lösenord på servern',
            'Ökar nyckelstyrkan'
        ],
        correctIndex: 1,
        explanation: 'Passphrase krypterar den privata nyckeln så den inte kan användas om den stjäls.',
        difficulty: 'G',
        category: 'SSH-nycklar'
    },
    // Mer pakethantering
    {
        id: 'paket-041',
        question: 'Vad gör "dpkg -i package.deb"?',
        options: [
            'Visar info om paketet',
            'Installerar ett lokalt .deb-paket',
            'Indexerar paketet',
            'Inspekterar paketinnehåll'
        ],
        correctIndex: 1,
        explanation: 'dpkg -i installerar ett nedladdat .deb-paket manuellt.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-042',
        question: 'Vad är problemet med "dpkg -i" jämfört med apt?',
        options: [
            'dpkg är långsammare',
            'dpkg hanterar inte beroenden automatiskt',
            'dpkg kräver root',
            'dpkg fungerar bara lokalt'
        ],
        correctIndex: 1,
        explanation: 'dpkg installerar paketet men löser inte beroenden - apt gör det.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-043',
        question: 'Hur fixar du saknade beroenden efter dpkg -i?',
        options: [
            'dpkg --fix-depends',
            'apt install -f',
            'apt --fix-missing',
            'dpkg-reconfigure'
        ],
        correctIndex: 1,
        explanation: 'apt install -f (--fix-broken) installerar saknade beroenden.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-044',
        question: 'Vad gör "apt full-upgrade"?',
        options: [
            'Samma som apt upgrade',
            'Uppgraderar och kan ta bort paket om det krävs',
            'Uppgraderar OS-version',
            'Uppgraderar bara viktiga paket'
        ],
        correctIndex: 1,
        explanation: 'apt full-upgrade (tidigare dist-upgrade) kan ta bort paket för att lösa beroenden.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-045',
        question: 'Hur simulerar du en installation utan att faktiskt installera?',
        options: [
            'apt install nginx --test',
            'apt install -s nginx',
            'apt install nginx --dry-run',
            'apt simulate nginx'
        ],
        correctIndex: 1,
        explanation: 'apt install -s (--simulate) visar vad som skulle hända utan att göra det.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-046',
        question: 'Vad gör "apt download nginx"?',
        options: [
            'Installerar nginx',
            'Laddar ner .deb-filen utan att installera',
            'Uppdaterar nginx',
            'Laddar ner nginx-dokumentation'
        ],
        correctIndex: 1,
        explanation: 'apt download laddar ner paketet som .deb-fil till aktuell katalog.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-047',
        question: 'Hur visar du changelogen för ett paket?',
        options: [
            'apt changelog nginx',
            'apt show --changelog nginx',
            'apt log nginx',
            'dpkg --changelog nginx'
        ],
        correctIndex: 0,
        explanation: 'apt changelog visar paketets ändringslogg.',
        difficulty: 'VG',
        category: 'Pakethantering'
    },
    {
        id: 'paket-048',
        question: 'Vad är Snap-paket?',
        options: [
            'En äldre paketstandard',
            'Containeriserade paket med alla beroenden inkluderade',
            'Komprimerade .deb-filer',
            'Temporära paket'
        ],
        correctIndex: 1,
        explanation: 'Snap är ett universellt paketformat med inbyggda beroenden och sandboxing.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-049',
        question: 'Vilket kommando installerar ett Snap-paket?',
        options: ['apt install --snap nginx', 'snap install nginx', 'snapd install nginx', 'install-snap nginx'],
        correctIndex: 1,
        explanation: 'snap install <paket> installerar ett Snap-paket.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'paket-050',
        question: 'Hur listar du installerade Snap-paket?',
        options: ['snap list', 'snap show', 'snapd --list', 'apt list --snap'],
        correctIndex: 0,
        explanation: 'snap list visar alla installerade Snap-paket.',
        difficulty: 'G',
        category: 'Pakethantering'
    }
]

// ============================================
// SUBNETTING (50 frågor)
// ============================================

export const SUBNETTING_QUESTIONS: OmtentaQuestion[] = [
    // Grundläggande IP och subnät
    {
        id: 'subnet-001',
        question: 'Hur många bitar har en IPv4-adress?',
        options: ['16 bitar', '32 bitar', '64 bitar', '128 bitar'],
        correctIndex: 1,
        explanation: 'IPv4-adresser är 32 bitar långa, uppdelade i 4 oktetter (8 bitar var).',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-002',
        question: 'Vad representerar en subnätmask?',
        options: [
            'Serverns adress',
            'Vilken del av IP-adressen som är nätverks-ID vs host-ID',
            'Antal enheter i nätverket',
            'Gateway-adressen'
        ],
        correctIndex: 1,
        explanation: 'Subnätmasken visar var gränsen går mellan nätverks- och hostdelen.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-003',
        question: 'Vad är CIDR-notation /24 i subnätmask?',
        options: ['255.255.255.128', '255.255.255.0', '255.255.0.0', '255.0.0.0'],
        correctIndex: 1,
        explanation: '/24 betyder 24 nätverksbitar = 255.255.255.0',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-004',
        question: 'Hur många användbara hostar finns i ett /24-nät?',
        options: ['256', '255', '254', '252'],
        correctIndex: 2,
        explanation: '2^8 - 2 = 254 hostar (nätverksadress och broadcast räknas bort).',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-005',
        question: 'Vad är nätverksadressen i 192.168.1.50/24?',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.50', '192.168.0.0'],
        correctIndex: 0,
        explanation: 'Med /24 är nätverksadressen .0 (alla hostbitar satta till 0).',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-006',
        question: 'Vad är broadcast-adressen i 192.168.1.0/24?',
        options: ['192.168.1.0', '192.168.1.1', '192.168.1.254', '192.168.1.255'],
        correctIndex: 3,
        explanation: 'Broadcast-adressen har alla hostbitar satta till 1 = .255 för /24.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-007',
        question: 'Vilket subnät tillhör en klass A-adress som standard?',
        options: ['/8', '/16', '/24', '/32'],
        correctIndex: 0,
        explanation: 'Klass A (1.0.0.0-126.255.255.255) har standard subnätmask /8.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-008',
        question: 'Vilket subnät tillhör en klass B-adress som standard?',
        options: ['/8', '/16', '/24', '/32'],
        correctIndex: 1,
        explanation: 'Klass B (128.0.0.0-191.255.255.255) har standard subnätmask /16.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-009',
        question: 'Vilket subnät tillhör en klass C-adress som standard?',
        options: ['/8', '/16', '/24', '/32'],
        correctIndex: 2,
        explanation: 'Klass C (192.0.0.0-223.255.255.255) har standard subnätmask /24.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-010',
        question: 'Vad är 255.255.255.0 i CIDR-notation?',
        options: ['/8', '/16', '/24', '/32'],
        correctIndex: 2,
        explanation: '255.255.255.0 har 24 ettor (3×8) = /24.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    // Subnetting-beräkningar
    {
        id: 'subnet-011',
        question: 'Hur många subnät skapas om du lånar 2 bitar från hostdelen?',
        options: ['2', '4', '6', '8'],
        correctIndex: 1,
        explanation: '2^2 = 4 subnät när du lånar 2 bitar.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-012',
        question: 'Ett /26-nät - hur många användbara hostar?',
        options: ['64', '62', '30', '32'],
        correctIndex: 1,
        explanation: '/26 ger 6 hostbitar: 2^6 - 2 = 62 användbara hostar.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-013',
        question: 'Vad är subnätmasken för /26?',
        options: ['255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224'],
        correctIndex: 2,
        explanation: '/26 = 26 bitar = 255.255.255.192 (192 = 11000000 binärt).',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-014',
        question: 'Om du har /28, hur många hostar per subnät?',
        options: ['16', '14', '8', '6'],
        correctIndex: 1,
        explanation: '/28 ger 4 hostbitar: 2^4 - 2 = 14 användbara hostar.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-015',
        question: 'Vilken adress är första användbara hosten i 10.0.0.0/8?',
        options: ['10.0.0.0', '10.0.0.1', '10.0.0.254', '10.0.0.255'],
        correctIndex: 1,
        explanation: 'Första användbara host = nätverksadress + 1 = 10.0.0.1.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-016',
        question: 'Vilken är sista användbara hosten i 192.168.10.0/24?',
        options: ['192.168.10.254', '192.168.10.255', '192.168.10.256', '192.168.10.253'],
        correctIndex: 0,
        explanation: 'Sista användbara = broadcast - 1 = 192.168.10.254.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-017',
        question: 'Du delar upp 192.168.1.0/24 i 4 subnät. Vilken mask får du?',
        options: ['/24', '/25', '/26', '/27'],
        correctIndex: 2,
        explanation: '4 subnät kräver 2 extra bitar: 24 + 2 = /26.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-018',
        question: 'Vad är nästa subnät efter 192.168.1.0/26?',
        options: ['192.168.1.32', '192.168.1.64', '192.168.1.128', '192.168.2.0'],
        correctIndex: 1,
        explanation: '/26 = 64 hostar per block. Nästa subnät börjar på .64.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-019',
        question: 'Tillhör 192.168.1.100 och 192.168.1.200 samma /25-subnät?',
        options: [
            'Ja, båda är i första subnätet',
            'Nej, 100 är i första och 200 i andra subnätet',
            'Ja, båda är i andra subnätet',
            'Kan inte avgöras'
        ],
        correctIndex: 1,
        explanation: '/25 delar vid .128. 100 < 128 = första subnät, 200 > 128 = andra.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-020',
        question: 'Hur många /30-subnät får du från ett /24-nät?',
        options: ['16', '32', '64', '128'],
        correctIndex: 2,
        explanation: '24 till 30 = 6 extra bitar = 2^6 = 64 subnät.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    // Privata IP-adresser
    {
        id: 'subnet-021',
        question: 'Vilket av dessa är ett privat IP-adressintervall?',
        options: ['8.8.8.0/24', '192.168.0.0/16', '200.100.50.0/24', '100.0.0.0/8'],
        correctIndex: 1,
        explanation: '192.168.0.0/16 är ett av tre privata intervall (RFC 1918).',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-022',
        question: 'Vilka är de tre privata IPv4-intervallen?',
        options: [
            '10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16',
            '10.0.0.0/8, 172.0.0.0/8, 192.0.0.0/8',
            '127.0.0.0/8, 169.254.0.0/16, 224.0.0.0/4',
            '10.0.0.0/16, 172.16.0.0/16, 192.168.0.0/24'
        ],
        correctIndex: 0,
        explanation: 'RFC 1918 definierar: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-023',
        question: 'Vad är 127.0.0.1?',
        options: ['Standard gateway', 'Loopback/localhost', 'Broadcast-adress', 'DNS-server'],
        correctIndex: 1,
        explanation: '127.0.0.1 är loopback-adressen som alltid pekar på den egna datorn.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-024',
        question: 'Vilken adress är en APIPA-adress (automatisk privat)?',
        options: ['192.168.1.1', '10.0.0.1', '169.254.100.50', '172.16.0.1'],
        correctIndex: 2,
        explanation: '169.254.0.0/16 är APIPA - används när DHCP misslyckas.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-025',
        question: 'Vad är 0.0.0.0 i nätverkssammanhang?',
        options: [
            'Ogiltig adress',
            'Standardroute/alla nätverk',
            'Loopback',
            'Broadcast'
        ],
        correctIndex: 1,
        explanation: '0.0.0.0 representerar alla nätverk, används ofta för default route.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    // Binära konverteringar
    {
        id: 'subnet-026',
        question: 'Vad är 192 i binärt?',
        options: ['10000000', '11000000', '11100000', '11110000'],
        correctIndex: 1,
        explanation: '192 = 128 + 64 = 11000000 binärt.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-027',
        question: 'Vad är binärt 11111111 i decimal?',
        options: ['254', '255', '256', '128'],
        correctIndex: 1,
        explanation: '11111111 = 128+64+32+16+8+4+2+1 = 255.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-028',
        question: 'Vad är binärt 10000000 i decimal?',
        options: ['64', '128', '192', '256'],
        correctIndex: 1,
        explanation: '10000000 = 128 (bara den första biten satt).',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-029',
        question: 'Vilken oktettvärde representerar /25 i sista oktetten?',
        options: ['0', '128', '192', '224'],
        correctIndex: 1,
        explanation: '/25 = 10000000 i sista oktetten = 128.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-030',
        question: 'Vad är subnätblock-storleken för /27?',
        options: ['16', '32', '64', '128'],
        correctIndex: 1,
        explanation: '/27 har 5 hostbitar: 2^5 = 32 adresser per block.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    // Praktiska frågor
    {
        id: 'subnet-031',
        question: 'Du behöver 100 hostar. Vilket är minsta subnät?',
        options: ['/24', '/25', '/26', '/27'],
        correctIndex: 1,
        explanation: '/25 ger 126 hostar, /26 bara 62. Du behöver minst /25.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-032',
        question: 'Du behöver 500 hostar. Vilket är minsta subnät?',
        options: ['/22', '/23', '/24', '/25'],
        correctIndex: 1,
        explanation: '/23 ger 510 hostar (2^9-2), /24 bara 254.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-033',
        question: 'Vad används ett /30-subnät typiskt till?',
        options: [
            'Stora servernätverk',
            'Punkt-till-punkt-länkar mellan routrar',
            'Klientnätverk',
            'Wi-Fi-nätverk'
        ],
        correctIndex: 1,
        explanation: '/30 ger 2 användbara adresser - perfekt för router-till-router-länkar.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-034',
        question: 'Vad betyder /32 i CIDR?',
        options: [
            'Ett nät med 256 hostar',
            'Ett helt klass C-nät',
            'En enda hostadress',
            'Ogiltigt subnät'
        ],
        correctIndex: 2,
        explanation: '/32 = alla bitar är nätverksbitar = exakt en adress (host route).',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-035',
        question: 'I vilket subnät är 172.16.45.200/20?',
        options: ['172.16.32.0', '172.16.40.0', '172.16.48.0', '172.16.45.0'],
        correctIndex: 0,
        explanation: '/20 = subnätblock om 4096. 45 ligger i intervallet 32-47 = 172.16.32.0.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-036',
        question: 'Hur beräknar du broadcast-adressen för 10.10.10.0/22?',
        options: [
            'Sätt alla hostbitar till 1',
            'Sätt alla hostbitar till 0',
            'Lägg till 255',
            'Ta bort sista oktetten'
        ],
        correctIndex: 0,
        explanation: 'Broadcast = alla hostbitar satta till 1. /22 = 10.10.11.255.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-037',
        question: 'Vad är broadcast för 10.10.10.0/22?',
        options: ['10.10.10.255', '10.10.11.255', '10.10.13.255', '10.10.255.255'],
        correctIndex: 1,
        explanation: '/22 ger 1024 adresser (4 block om 256). 10.10.8.0-10.10.11.255.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-038',
        question: 'Vilken oktettvärde representerar /20 i tredje oktetten?',
        options: ['0', '128', '192', '240'],
        correctIndex: 3,
        explanation: '/20 = 20 bitar = 255.255.240.0. Tredje oktetten = 240 (11110000).',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-039',
        question: 'Hur många /24-nät kan du skapa från ett /16-nät?',
        options: ['64', '128', '256', '512'],
        correctIndex: 2,
        explanation: '/16 till /24 = 8 extra bitar = 2^8 = 256 subnät.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-040',
        question: 'Vad är supernetting/CIDR-aggregering?',
        options: [
            'Dela upp stora nät i mindre',
            'Slå ihop mindre nät till ett större',
            'Skapa VPN-tunnlar',
            'Kryptera nätverkstrafik'
        ],
        correctIndex: 1,
        explanation: 'Supernetting sammanslår flera mindre nät till en större route.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    // VLSM och mer avancerat
    {
        id: 'subnet-041',
        question: 'Vad står VLSM för?',
        options: [
            'Variable Length Subnet Mask',
            'Virtual Local Subnet Mode',
            'Very Large Subnet Manager',
            'Variable Link Speed Monitoring'
        ],
        correctIndex: 0,
        explanation: 'VLSM = Variable Length Subnet Mask, olika subnätstorlekar i samma nät.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-042',
        question: 'Vilken fördel har VLSM?',
        options: [
            'Snabbare routing',
            'Effektivare användning av IP-adresser',
            'Bättre säkerhet',
            'Enklare konfiguration'
        ],
        correctIndex: 1,
        explanation: 'VLSM minimerar slöseri genom att anpassa subnätstorlek efter behov.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-043',
        question: 'Vad är en wildcard-mask?',
        options: [
            'Inverterad subnätmask',
            'Samma som subnätmask',
            'En typ av broadcast-adress',
            'En säkerhetsmask'
        ],
        correctIndex: 0,
        explanation: 'Wildcard-mask är inverterad subnätmask, används i ACL:er och routing.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-044',
        question: 'Vad är wildcard-masken för /24?',
        options: ['255.255.255.0', '0.0.0.255', '0.0.0.0', '255.255.255.255'],
        correctIndex: 1,
        explanation: 'Wildcard = 255 - subnätmask. 255.255.255.0 → 0.0.0.255.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-045',
        question: 'Vilket kommando visar IP-konfiguration i Linux?',
        options: ['ifconfig', 'ip addr', 'ipconfig', 'netstat -i'],
        correctIndex: 1,
        explanation: 'ip addr (eller ip a) är moderna sättet att visa IP-konfiguration i Linux.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-046',
        question: 'Hur visar du routingtabellen i Linux?',
        options: ['route -n', 'ip route', 'netstat -r', 'Alla dessa'],
        correctIndex: 3,
        explanation: 'Alla dessa visar routingtabellen: route -n, ip route, netstat -r.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-047',
        question: 'Vad gör kommandot "ip route add 10.0.0.0/8 via 192.168.1.1"?',
        options: [
            'Tar bort en route',
            'Lägger till en statisk route',
            'Visar routingtabell',
            'Testar nätverksanslutning'
        ],
        correctIndex: 1,
        explanation: 'ip route add skapar en statisk route till 10.0.0.0/8 via gateway 192.168.1.1.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'subnet-048',
        question: 'Vad är gateway i ett nätverk?',
        options: [
            'DNS-server',
            'Router som leder till andra nätverk',
            'DHCP-server',
            'Brandvägg'
        ],
        correctIndex: 1,
        explanation: 'Gateway är routern som hanterar trafik till/från andra nätverk.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-049',
        question: 'Vad måste vara sant för att två hostar ska kommunicera utan router?',
        options: [
            'Samma gateway',
            'Samma subnät',
            'Samma DNS',
            'Samma MAC-adress'
        ],
        correctIndex: 1,
        explanation: 'Hostar i samma subnät kan kommunicera direkt på Layer 2 utan router.',
        difficulty: 'G',
        category: 'Subnetting'
    },
    {
        id: 'subnet-050',
        question: 'Vad visar kommandot "ping -c 4 8.8.8.8"?',
        options: [
            'DNS-uppslag',
            'Testar anslutning med 4 paket',
            'Visar 4 hostar',
            'Öppnar 4 portar'
        ],
        correctIndex: 1,
        explanation: 'ping -c 4 skickar 4 ICMP-paket för att testa nätverksanslutning.',
        difficulty: 'G',
        category: 'Subnetting'
    }
]

// Statistik
export const PAKET_SUBNETTING_STATS = {
    pakethantering: PAKETHANTERING_QUESTIONS.length,
    subnetting: SUBNETTING_QUESTIONS.length,
    total: PAKETHANTERING_QUESTIONS.length + SUBNETTING_QUESTIONS.length
}
