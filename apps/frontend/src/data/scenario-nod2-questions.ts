/**
 * NOD 2: Rättigheter & Säkerhet - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD2_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod2-s1',
        question: 'Du kör `ls -la /var/www/html/config.php` och ser `-rw-r--r--`. Webservern (www-data) kan inte läsa filen. Vad är problemet?',
        options: ['Filen ägs av root, inte www-data', 'Filen har inga execute-permissions', 'r-- betyder readonly för alla', 'Du behöver köra som sudo'],
        correctIndices: [0],
        explanation: 'Med -rw-r--r-- kan "others" läsa. Problemet är troligen att filen ägs av fel användare/grupp. Kör chown www-data:www-data config.php.',
        difficulty: 'G',
        category: 'Filrättigheter',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s2',
        question: 'En ny utvecklare Lisa ska kunna redigera filer i /var/www/app. Du kör `ls -la` och ser `drwxr-x--- root developers`. Lisa är med i gruppen developers. Varför kan hon inte skriva?',
        options: ['Hon behöver vara root', 'Gruppen har bara read+execute, inte write', 'Katalogen är låst', 'Hon måste logga ut och in igen'],
        correctIndices: [1],
        explanation: 'r-x för gruppen = read+execute men inte write. Lösning: chmod g+w /var/www/app',
        difficulty: 'G',
        category: 'Filrättigheter',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s3',
        question: 'Du vill att alla nya filer i /shared ska få rättigheter 644 istället för 666. Vilket umask-värde behövs?',
        options: ['umask 000', 'umask 022', 'umask 644', 'umask 133'],
        correctIndices: [1],
        explanation: 'umask subtraheras från default (666 för filer). 666 - 022 = 644. umask 022 är standard på de flesta system.',
        difficulty: 'VG',
        category: 'umask',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s4',
        question: 'Du hittar en fil med rättigheter `-rwsr-xr-x root root /usr/bin/passwd`. Vad betyder "s" istället för "x"?',
        options: ['Filen är en symlink', 'SUID-bit är satt - körs som ägaren', 'Filen är skyddad', 'Sticky bit är satt'],
        correctIndices: [1],
        explanation: 'SUID (s på owner execute) gör att programmet körs med ägarens rättigheter. passwd körs som root för att kunna ändra /etc/shadow.',
        difficulty: 'VG',
        category: 'Special permissions',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s5',
        question: 'Du vill ge användaren deploy full access till en fil utan att ändra ägare eller grupp. Vilket kommando använder du?',
        options: ['chmod 777 fil', 'chown deploy fil', 'setfacl -m u:deploy:rwx fil', 'usermod -aG filegroup deploy'],
        correctIndices: [2],
        explanation: 'ACL (Access Control List) med setfacl ger finmaskig kontroll utan att ändra traditionella Unix-permissions.',
        difficulty: 'VG',
        category: 'ACL',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s6',
        question: 'Du behöver köra `apt update` men får "Permission denied". Hur kör du kommandot som root?',
        options: ['root apt update', 'su apt update', 'sudo apt update', 'admin apt update'],
        correctIndices: [2],
        explanation: 'sudo kör ett enskilt kommando som root. su byter hela sessionen till en annan användare.',
        difficulty: 'G',
        category: 'sudo',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s7',
        question: 'Du vill snabbt ge alla (owner, group, others) read+write på en fil. Vilket chmod-kommando?',
        options: ['chmod 666 fil', 'chmod 777 fil', 'chmod +rw fil', 'chmod a+rw fil'],
        correctIndices: [3],
        explanation: 'chmod a+rw = all (+rw). 666 fungerar också men a+rw är mer explicit och lättläst.',
        difficulty: 'G',
        category: 'chmod',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s8',
        question: 'Efter att ha lagt till användare erik i gruppen docker, kan han fortfarande inte köra docker-kommandon. Vad saknas?',
        options: ['Docker måste startas om', 'Erik måste logga ut och in igen', 'Erik måste köra newgrp', 'Antingen B eller C fungerar'],
        correctIndices: [3],
        explanation: 'Gruppmedlemskap laddas vid inloggning. Erik måste antingen logga ut/in eller köra "newgrp docker" för att aktivera gruppen.',
        difficulty: 'G',
        category: 'Grupper',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s9',
        question: 'Katalogen /tmp har rättigheter drwxrwxrwt. Vad betyder "t" i slutet?',
        options: ['Temporary - filer tas bort automatiskt', 'Sticky bit - bara ägaren kan radera sina filer', 'Trust - alla kan lita på innehållet', 'Timed - filer har tidsgräns'],
        correctIndices: [1],
        explanation: 'Sticky bit på katalog = användare kan bara ta bort egna filer, även om alla kan skriva. Kritiskt för /tmp.',
        difficulty: 'VG',
        category: 'Special permissions',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s10',
        question: 'Du vill ändra ägare på alla filer i /var/www/app till www-data, rekursivt. Vilket kommando?',
        options: ['chown www-data /var/www/app/*', 'chown -R www-data /var/www/app', 'chmod -R www-data /var/www/app', 'owner -r www-data /var/www/app'],
        correctIndices: [1],
        explanation: 'chown -R = recursive. Ändrar ägare på katalogen och ALLT innehåll. chmod ändrar rättigheter, inte ägare.',
        difficulty: 'G',
        category: 'chown',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s11',
        question: 'Du ser rättigheter 750 på en katalog. Vad kan gruppen göra?',
        options: ['Läsa, skriva och gå in i katalogen', 'Bara läsa kataloginnehåll', 'Läsa och gå in, men inte skriva', 'Ingenting - 0 för gruppen'],
        correctIndices: [2],
        explanation: '750 = rwx|r-x|--- = owner: allt, group: read+execute (kan läsa och cd:a in), others: inget.',
        difficulty: 'G',
        category: 'Filrättigheter',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s12',
        question: 'En kollega kör `sudo su -` och frågar vad skillnaden är mot bara `sudo su`. Vad svarar du?',
        options: ['Ingen skillnad', 'su - laddar roots hela miljö (login shell)', 'su - är säkrare', 'su - kräver roots lösenord'],
        correctIndices: [1],
        explanation: 'su - (eller su -l) startar en login shell som laddar roots .profile/.bashrc. Utan - behålls din miljö.',
        difficulty: 'VG',
        category: 'sudo',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s13',
        question: 'Du vill se vilka ACL-rättigheter som finns på en fil. Vilket kommando?',
        options: ['ls -la fil', 'getfacl fil', 'showacl fil', 'cat /etc/acl/fil'],
        correctIndices: [1],
        explanation: 'getfacl visar Access Control Lists. ls -la visar bara traditionella Unix-permissions (plus + om ACL finns).',
        difficulty: 'VG',
        category: 'ACL',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s14',
        question: 'Du vill att användaren backup ska kunna köra rsync med sudo UTAN lösenord. Var konfigurerar du detta?',
        options: ['/etc/passwd', '/etc/shadow', '/etc/sudoers eller /etc/sudoers.d/', '/etc/sudo.conf'],
        correctIndices: [2],
        explanation: '/etc/sudoers (redigeras med visudo) kontrollerar sudo-rättigheter. NOPASSWD: tillåter utan lösenord.',
        difficulty: 'VG',
        category: 'sudo',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s15',
        question: 'Du kör `id erik` och ser: uid=1001(erik) gid=1001(erik) groups=1001(erik),27(sudo),999(docker). Vad betyder detta?',
        options: ['Erik är root-användare', 'Erik tillhör 3 grupper: erik, sudo och docker', 'Erik har 3 aktiva sessioner', 'Erik är inaktiverad'],
        correctIndices: [1],
        explanation: 'groups visar alla grupper användaren tillhör. sudo = kan köra sudo, docker = kan köra docker utan sudo.',
        difficulty: 'G',
        category: 'Grupper',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s16',
        question: 'Du skapar en ny användare med `useradd -m anna`. Vad gör -m flaggan?',
        options: ['Skapar mail-inbox', 'Skapar hemkatalog (/home/anna)', 'Gör användaren till medlem i main-gruppen', 'Sätter max password-age'],
        correctIndices: [1],
        explanation: '-m (--create-home) skapar användarens hemkatalog. Utan -m skapas ingen hemkatalog.',
        difficulty: 'G',
        category: 'Användarhantering',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s17',
        question: 'Du vill ta bort execute-permission för others på ett skript. Vilket chmod-kommando?',
        options: ['chmod o-x script.sh', 'chmod -x script.sh', 'chmod 770 script.sh', 'Alla tre fungerar'],
        correctIndices: [0],
        explanation: 'o-x tar bort execute endast för others. -x tar bort för alla. 770 sätter hela permissions (kan påverka mer).',
        difficulty: 'G',
        category: 'chmod',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s18',
        question: 'Ett skript ska kunna köras av vem som helst men alltid köras med gruppen "backup"s rättigheter. Vilken special permission?',
        options: ['SUID', 'SGID', 'Sticky bit', 'ACL'],
        correctIndices: [1],
        explanation: 'SGID (Set Group ID) på en fil gör att den körs med filens grupprättigheter, inte användarens grupp.',
        difficulty: 'VG',
        category: 'Special permissions',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s19',
        question: 'Du kör `chmod 4755 /usr/local/bin/myapp`. Vad gör siffran 4?',
        options: ['Sätter read för owner', 'Sätter SUID-bit', 'Sätter sticky bit', 'Gör filen immutable'],
        correctIndices: [1],
        explanation: 'Special permissions: 4=SUID, 2=SGID, 1=Sticky. 4755 = SUID + rwxr-xr-x.',
        difficulty: 'VG',
        category: 'Special permissions',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    },
    {
        id: 'nod2-s20',
        question: 'Du behöver byta grupp på en fil från "users" till "developers". Vilket kommando?',
        options: ['chown :developers fil', 'chgrp developers fil', 'groupmod fil developers', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: 'chgrp byter grupp. chown :grupp (kolon före) byter också bara grupp. Båda fungerar.',
        difficulty: 'G',
        category: 'chgrp',
        topic: 'nod2-rattigheter',
        type: 'scenario'
    }
]
