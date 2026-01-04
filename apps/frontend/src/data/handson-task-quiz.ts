// Hands-On Lab Task Quiz - 20 frågor per task = 140 totalt

export interface TaskQuizQuestion {
    id: string;
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
    category?: string;
    difficulty?: 'G' | 'VG';
}

export interface TaskQuizSet {
    taskId: string;
    taskTitle: string;
    questions: TaskQuizQuestion[];
}

export const HANDSON_TASK_QUIZ: TaskQuizSet[] = [
    // ============================================
    // TASK 1: ONBOARDING - FILSYSTEM & TEXTEDITORER (20)
    // ============================================
    {
        taskId: "handson-1-onboarding",
        taskTitle: "Onboarding - Filsystem & Texteditorer",
        questions: [
            {
                id: "ho1-q1",
                question: "Vilket kommando visar din nuvarande katalog?",
                options: ["cd", "pwd", "ls", "dir"],
                correctIndex: 1,
                explanation: "pwd (print working directory) visar den fullständiga sökvägen till din nuvarande katalog."
            },
            {
                id: "ho1-q2",
                question: "Hur skapar du katalogen /projekt/src/components i ett kommando?",
                options: ["mkdir projekt src components", "mkdir -p projekt/src/components", "mkdir -r projekt/src/components", "create -p projekt/src/components"],
                correctIndex: 1,
                explanation: "mkdir -p skapar alla parent-kataloger automatiskt om de inte finns."
            },
            {
                id: "ho1-q3",
                question: "Vad gör kommandot 'echo Hello > fil.txt'?",
                options: ["Lägger till Hello i slutet av fil.txt", "Skriver över fil.txt med Hello", "Visar Hello och fil.txt", "Skapar en länk mellan Hello och fil.txt"],
                correctIndex: 1,
                explanation: "> skriver över filen helt. Använd >> för att lägga till (append)."
            },
            {
                id: "ho1-q4",
                question: "Hur kopierar du en katalog med allt innehåll?",
                options: ["cp katalog/ ny/", "cp -a katalog/ ny/", "cp -r katalog/ ny/", "copy katalog/ ny/"],
                correctIndex: 2,
                explanation: "cp -r (recursive) kopierar katalogen och allt innehåll rekursivt."
            },
            {
                id: "ho1-q5",
                question: "Vad visar 'ls -la'?",
                options: ["Bara dolda filer", "Alla filer i lång format", "Alla filer inkl dolda i lång format", "Filstorleken"],
                correctIndex: 2,
                explanation: "-l är lång format och -a visar alla filer (inkl dolda som börjar med .)."
            },
            {
                id: "ho1-q6",
                question: "Hur sparar du i Nano?",
                options: ["Ctrl+S", "Ctrl+O", ":w", "F2"],
                correctIndex: 1,
                explanation: "I Nano sparar du med Ctrl+O (WriteOut)."
            },
            {
                id: "ho1-q7",
                question: "Hur avslutar du Nano?",
                options: ["Ctrl+Q", "Ctrl+X", ":q", "Esc"],
                correctIndex: 1,
                explanation: "Ctrl+X avslutar Nano. Den frågar om du vill spara om det finns osparade ändringar."
            },
            {
                id: "ho1-q8",
                question: "I Vim, hur går du från Normal mode till Insert mode?",
                options: ["Tryck Enter", "Tryck i", "Skriv :insert", "Tryck Tab"],
                correctIndex: 1,
                explanation: "i sätter Vim i Insert mode så du kan skriva text."
            },
            {
                id: "ho1-q9",
                question: "Hur sparar och avslutar du i Vim?",
                options: [":wq", ":sq", "Ctrl+S + Ctrl+Q", ":exit"],
                correctIndex: 0,
                explanation: ":wq (write quit) sparar och avslutar. Du kan också använda :x."
            },
            {
                id: "ho1-q10",
                question: "Hur gör du ett script körbart?",
                options: ["run script.sh", "exec script.sh", "chmod +x script.sh", "enable script.sh"],
                correctIndex: 2,
                explanation: "chmod +x lägger till execute-permission så scriptet kan köras."
            },
            {
                id: "ho1-q11",
                question: "Vad kallas första raden '#!/bin/bash' i ett script?",
                options: ["Header", "Shebang", "Magic number", "Shell directive"],
                correctIndex: 1,
                explanation: "Shebang (#!) talar om vilken interpretator som ska köra scriptet."
            },
            {
                id: "ho1-q12",
                question: "Hur följer du en loggfil i realtid?",
                options: ["cat -f logfile.log", "tail -f logfile.log", "watch logfile.log", "follow logfile.log"],
                correctIndex: 1,
                explanation: "tail -f (follow) visar nya rader som läggs till i filen."
            },
            {
                id: "ho1-q13",
                question: "Vilket kommando visar fil innehåll med scroll-möjlighet?",
                options: ["cat", "more", "less", "view"],
                correctIndex: 2,
                explanation: "less är en pager som låter dig scrolla upp/ner. Tryck q för att avsluta."
            },
            {
                id: "ho1-q14",
                question: "Hur navigerar du till din hemmapp?",
                options: ["cd home", "cd /", "cd ~", "cd .."],
                correctIndex: 2,
                explanation: "~ representerar din hemmapp. 'cd' utan argument gör samma sak."
            },
            {
                id: "ho1-q15",
                question: "Hur tar du bort en katalog och allt innehåll?",
                options: ["rm katalog", "del -r katalog", "rm -r katalog", "rmdir -f katalog"],
                correctIndex: 2,
                explanation: "rm -r (recursive) tar bort katalogen och allt innehåll."
            },
            {
                id: "ho1-q16",
                question: "Vad gör >> vid omdirigering?",
                options: ["Skriver över filen", "Lägger till i slutet", "Skapar backup", "Läser från fil"],
                correctIndex: 1,
                explanation: ">> append:ar (lägger till) i slutet av filen istället för att skriva över."
            },
            {
                id: "ho1-q17",
                question: "Hur avslutar du Vim UTAN att spara ändringar?",
                options: [":q", ":q!", ":exit", ":wq!"],
                correctIndex: 1,
                explanation: ":q! tvingar avslut utan att spara (! överskrider varningen)."
            },
            {
                id: "ho1-q18",
                question: "Hur söker du i Nano?",
                options: ["Ctrl+F", "Ctrl+W", "/sökterm", "Ctrl+S"],
                correctIndex: 1,
                explanation: "Ctrl+W (Where is) öppnar sökfunktionen i Nano."
            },
            {
                id: "ho1-q19",
                question: "Vad representerar . (punkt) i Linux?",
                options: ["Root-katalogen", "Förra katalogen", "Nuvarande katalog", "Hemmappen"],
                correctIndex: 2,
                explanation: ". är nuvarande katalog, .. är parent-katalogen."
            },
            {
                id: "ho1-q20",
                question: "Hur kör du ett script i nuvarande katalog?",
                options: ["script.sh", "./script.sh", "run script.sh", "bash -e script.sh"],
                correctIndex: 1,
                explanation: "./ anger explicit att scriptet finns i nuvarande katalog."
            }
        ]
    },
    // ============================================
    // TASK 2: PAKETHANTERING & SSH-NYCKLAR (20)
    // ============================================
    {
        taskId: "handson-2-pakethantering",
        taskTitle: "Pakethantering & SSH-nycklar",
        questions: [
            {
                id: "ho2-q1",
                question: "Vad ska du köra INNAN 'apt install'?",
                options: ["apt upgrade", "apt update", "apt refresh", "apt sync"],
                correctIndex: 1,
                explanation: "apt update hämtar senaste paketlistorna så du installerar rätt version."
            },
            {
                id: "ho2-q2",
                question: "Skillnaden mellan 'apt remove' och 'apt purge'?",
                options: ["Ingen skillnad", "purge är snabbare", "remove behåller config, purge tar bort allt", "purge bara tar bort loggar"],
                correctIndex: 2,
                explanation: "remove behåller konfigurationsfiler, purge tar bort allt inklusive config."
            },
            {
                id: "ho2-q3",
                question: "Vilken SSH-nyckeltyp rekommenderas?",
                options: ["RSA 1024", "DSA", "ed25519", "RSA 512"],
                correctIndex: 2,
                explanation: "ed25519 är modernast och säkrast. RSA 4096 är också OK."
            },
            {
                id: "ho2-q4",
                question: "Var sparas din PRIVATA SSH-nyckel?",
                options: ["~/.ssh/id_ed25519.pub", "~/.ssh/id_ed25519", "/etc/ssh/id_ed25519", "~/.ssh/authorized_keys"],
                correctIndex: 1,
                explanation: "Den privata nyckeln sparas utan .pub-ändelse."
            },
            {
                id: "ho2-q5",
                question: "Vilken nyckel ska ALDRIG delas?",
                options: ["Publika nyckeln", "Privata nyckeln", "Båda", "Ingen av dem"],
                correctIndex: 1,
                explanation: "Den privata nyckeln måste hållas hemlig. Publika kan delas fritt."
            },
            {
                id: "ho2-q6",
                question: "Hur kopierar du din publika nyckel till en server?",
                options: ["scp ~/.ssh/id_ed25519.pub user@server:", "ssh-copy-id user@server", "ssh-add user@server", "ssh-keygen -copy user@server"],
                correctIndex: 1,
                explanation: "ssh-copy-id kopierar automatiskt din publika nyckel till serverns authorized_keys."
            },
            {
                id: "ho2-q7",
                question: "Vilken rättighet ska ~/.ssh/ ha?",
                options: ["777", "644", "700", "755"],
                correctIndex: 2,
                explanation: "700 (rwx------) - bara ägaren får läsa, skriva och gå in i katalogen."
            },
            {
                id: "ho2-q8",
                question: "Vilken rättighet ska privata nyckeln ha?",
                options: ["644", "600", "700", "400"],
                correctIndex: 1,
                explanation: "600 (rw-------) - bara ägaren får läsa och skriva."
            },
            {
                id: "ho2-q9",
                question: "Vad är 'Host' i SSH config?",
                options: ["Serverns IP", "Ett alias du väljer", "Användarnamnet", "Port-numret"],
                correctIndex: 1,
                explanation: "Host är ett alias du definierar för att förenkla anslutning."
            },
            {
                id: "ho2-q10",
                question: "Om du har 'Host prod' i config, hur ansluter du?",
                options: ["ssh Host prod", "ssh prod", "ssh -H prod", "connect prod"],
                correctIndex: 1,
                explanation: "Du skriver bara 'ssh prod' och SSH läser resten från config."
            },
            {
                id: "ho2-q11",
                question: "Vad gör 'apt autoremove'?",
                options: ["Tar bort alla paket", "Tar bort oanvända beroenden", "Avinstallerar APT", "Rensar cache"],
                correctIndex: 1,
                explanation: "autoremove tar bort paket som installerades som beroenden men inte längre behövs."
            },
            {
                id: "ho2-q12",
                question: "Hur genererar du SSH-nyckel med kommentar?",
                options: ["ssh-keygen -c 'text'", "ssh-keygen -C 'text'", "ssh-keygen --comment 'text'", "ssh-keygen -m 'text'"],
                correctIndex: 1,
                explanation: "-C lägger till en kommentar (ofta email) i slutet av publika nyckeln."
            },
            {
                id: "ho2-q13",
                question: "Var på servern hamnar auktoriserade nycklar?",
                options: ["/etc/ssh/keys", "~/.ssh/authorized_keys", "~/.ssh/known_hosts", "/var/ssh/keys"],
                correctIndex: 1,
                explanation: "authorized_keys innehåller publika nycklar som får logga in."
            },
            {
                id: "ho2-q14",
                question: "Vad är en passphrase på SSH-nyckel?",
                options: ["Serverns lösenord", "Extra lösenord för att använda nyckeln", "Användarnamnet", "Nyckelns namn"],
                correctIndex: 1,
                explanation: "Passphrase krypterar den privata nyckeln lokalt för extra säkerhet."
            },
            {
                id: "ho2-q15",
                question: "Hur anger du specifik nyckel i SSH config?",
                options: ["Key ~/.ssh/key", "IdentityFile ~/.ssh/key", "KeyFile ~/.ssh/key", "SSHKey ~/.ssh/key"],
                correctIndex: 1,
                explanation: "IdentityFile anger vilken privat nyckel som ska användas."
            },
            {
                id: "ho2-q16",
                question: "Vad gör 'apt show nginx'?",
                options: ["Installerar nginx", "Visar info om nginx-paketet", "Startar nginx", "Söker efter nginx"],
                correctIndex: 1,
                explanation: "apt show visar detaljerad information om ett paket."
            },
            {
                id: "ho2-q17",
                question: "Hur laddar du ner en fil med curl?",
                options: ["curl URL", "curl -O URL", "curl -d URL", "curl --save URL"],
                correctIndex: 1,
                explanation: "-O sparar filen med samma namn som på servern."
            },
            {
                id: "ho2-q18",
                question: "Vad är ssh-agent?",
                options: ["En SSH-server", "Program som håller nycklar i minnet", "SSH-konfigurationsverktyg", "Backup för SSH-nycklar"],
                correctIndex: 1,
                explanation: "ssh-agent cachar dina nycklar så du slipper ange passphrase varje gång."
            },
            {
                id: "ho2-q19",
                question: "Hur söker du efter paket?",
                options: ["apt find nginx", "apt search nginx", "apt lookup nginx", "apt query nginx"],
                correctIndex: 1,
                explanation: "apt search söker i paketnamn och beskrivningar."
            },
            {
                id: "ho2-q20",
                question: "Vilken fil redigerar du för SSH-genvägar?",
                options: ["/etc/ssh/config", "~/.ssh/config", "~/.ssh/hosts", "/etc/ssh/ssh_config"],
                correctIndex: 1,
                explanation: "~/.ssh/config är din personliga SSH-konfigurationsfil."
            }
        ]
    },
    // ============================================
    // TASK 3: SSH & BRANDVÄGG (20)
    // ============================================
    {
        taskId: "handson-3-ssh-brandvagg",
        taskTitle: "SSH & Brandvägg",
        questions: [
            {
                id: "ho3-q1",
                question: "Var finns SSH-serverns konfiguration?",
                options: ["~/.ssh/config", "/etc/ssh/sshd_config", "/etc/sshd.conf", "~/.sshd_config"],
                correctIndex: 1,
                explanation: "sshd_config (med d för daemon) är serverns konfiguration."
            },
            {
                id: "ho3-q2",
                question: "Hur blockerar du root-login via SSH?",
                options: ["BlockRoot yes", "PermitRootLogin no", "DenyRoot yes", "RootAccess no"],
                correctIndex: 1,
                explanation: "PermitRootLogin no förhindrar direktinloggning som root."
            },
            {
                id: "ho3-q3",
                question: "Vilken är default SSH-port?",
                options: ["21", "22", "23", "80"],
                correctIndex: 1,
                explanation: "SSH lyssnar på port 22 som standard."
            },
            {
                id: "ho3-q4",
                question: "Hur validerar du sshd_config innan omstart?",
                options: ["sshd -c", "sshd -t", "sshd -v", "sshd -check"],
                correctIndex: 1,
                explanation: "sshd -t (test) validerar syntaxen utan att starta om tjänsten."
            },
            {
                id: "ho3-q5",
                question: "KRITISKT: Vad måste du göra INNAN du aktiverar UFW?",
                options: ["Starta om servern", "Tillåta SSH-porten", "Installera nginx", "Skapa backup"],
                correctIndex: 1,
                explanation: "Om du inte tillåter SSH innan du aktiverar UFW låser du dig ute!"
            },
            {
                id: "ho3-q6",
                question: "Hur sätter du UFW att blockera allt inkommande?",
                options: ["ufw deny all", "ufw default deny incoming", "ufw block incoming", "ufw incoming deny"],
                correctIndex: 1,
                explanation: "default deny incoming blockerar allt inkommande som inte explicit tillåts."
            },
            {
                id: "ho3-q7",
                question: "Hur tillåter du SSH i UFW?",
                options: ["ufw allow ssh", "ufw open 22", "ufw permit ssh", "ufw enable ssh"],
                correctIndex: 0,
                explanation: "ufw allow ssh eller ufw allow 22 tillåter SSH-trafik."
            },
            {
                id: "ho3-q8",
                question: "Hur aktiverar du UFW?",
                options: ["ufw start", "ufw enable", "ufw on", "ufw activate"],
                correctIndex: 1,
                explanation: "ufw enable aktiverar brandväggen."
            },
            {
                id: "ho3-q9",
                question: "Hur ser du UFW-regler med nummer?",
                options: ["ufw list", "ufw status numbered", "ufw show rules", "ufw -n status"],
                correctIndex: 1,
                explanation: "ufw status numbered visar regler med nummer för enkel borttagning."
            },
            {
                id: "ho3-q10",
                question: "Hur tar du bort UFW-regel nummer 3?",
                options: ["ufw remove 3", "ufw delete 3", "ufw drop 3", "ufw disable 3"],
                correctIndex: 1,
                explanation: "ufw delete 3 tar bort regel nummer 3."
            },
            {
                id: "ho3-q11",
                question: "Hur tillåter du port 443/tcp?",
                options: ["ufw allow 443", "ufw allow 443/tcp", "ufw open 443/tcp", "ufw permit 443"],
                correctIndex: 1,
                explanation: "ufw allow 443/tcp tillåter HTTPS-trafik."
            },
            {
                id: "ho3-q12",
                question: "VIKTIGT efter SSH-ändringar: Vad ska du göra?",
                options: ["Starta om datorn", "Testa i NY terminal", "Vänta 5 minuter", "Köra apt update"],
                correctIndex: 1,
                explanation: "Testa alltid SSH i en ny terminal innan du stänger den gamla!"
            },
            {
                id: "ho3-q13",
                question: "Hur inaktiverar du lösenords-autentisering?",
                options: ["PasswordLogin no", "PasswordAuthentication no", "DisablePassword yes", "NoPassword yes"],
                correctIndex: 1,
                explanation: "PasswordAuthentication no tvingar nyckel-autentisering."
            },
            {
                id: "ho3-q14",
                question: "Hur ser du SSH-loggar i realtid?",
                options: ["tail -f /var/log/ssh.log", "journalctl -u sshd -f", "cat /var/log/sshd", "sshd --logs"],
                correctIndex: 1,
                explanation: "journalctl -u sshd -f följer systemd-loggarna för SSH."
            },
            {
                id: "ho3-q15",
                question: "Hur tillåter du trafik från specifik IP?",
                options: ["ufw allow from 192.168.1.100", "ufw whitelist 192.168.1.100", "ufw add 192.168.1.100", "ufw trust 192.168.1.100"],
                correctIndex: 0,
                explanation: "ufw allow from IP tillåter all trafik från den IPn."
            },
            {
                id: "ho3-q16",
                question: "Hur ansluter du via SSH på port 2222?",
                options: ["ssh user@server -port 2222", "ssh -p 2222 user@server", "ssh user@server:2222", "ssh --port 2222 user@server"],
                correctIndex: 1,
                explanation: "-p anger porten att ansluta till."
            },
            {
                id: "ho3-q17",
                question: "Var finns UFW-loggar?",
                options: ["/var/log/firewall.log", "/var/log/ufw.log", "/etc/ufw/log", "~/.ufw/log"],
                correctIndex: 1,
                explanation: "UFW loggar till /var/log/ufw.log."
            },
            {
                id: "ho3-q18",
                question: "Hur begränsar du SSH till specifika användare?",
                options: ["Users user1 user2", "AllowUsers user1 user2", "PermitUsers user1 user2", "SSHUsers user1 user2"],
                correctIndex: 1,
                explanation: "AllowUsers whitelistar vilka användare som får SSH:a in."
            },
            {
                id: "ho3-q19",
                question: "Hur startar du om SSH-tjänsten?",
                options: ["service sshd reload", "systemctl restart sshd", "sshd restart", "/etc/init.d/ssh start"],
                correctIndex: 1,
                explanation: "systemctl restart sshd startar om SSH-demonen."
            },
            {
                id: "ho3-q20",
                question: "Hur testar du SSH med verbose output?",
                options: ["ssh -v user@server", "ssh --debug user@server", "ssh -d user@server", "ssh user@server -verbose"],
                correctIndex: 0,
                explanation: "-v ger verbose output för felsökning. -vv och -vvv ger ännu mer."
            }
        ]
    },
    // ============================================
    // TASK 4: ANVÄNDARHANTERING (20)
    // ============================================
    {
        taskId: "handson-4-anvandarhantering",
        taskTitle: "Användarhantering",
        questions: [
            {
                id: "ho4-q1",
                question: "Hur skapar du användare med hemmapp?",
                options: ["useradd user", "useradd -m user", "adduser -h user", "createuser -m user"],
                correctIndex: 1,
                explanation: "-m skapar hemmapp automatiskt."
            },
            {
                id: "ho4-q2",
                question: "Vad gör -aG i 'usermod -aG grupp user'?",
                options: ["Tar bort från grupp", "Lägger till utan att ta bort från andra grupper", "Skapar ny grupp", "Aktiverar grupp"],
                correctIndex: 1,
                explanation: "-a är append (lägg till), -G är supplementary groups."
            },
            {
                id: "ho4-q3",
                question: "Hur ger du en användare sudo-rättigheter?",
                options: ["chmod +sudo user", "usermod -aG sudo user", "adduser user admin", "grant sudo user"],
                correctIndex: 1,
                explanation: "Lägg till i sudo-gruppen med usermod -aG sudo."
            },
            {
                id: "ho4-q4",
                question: "Hur redigerar du sudoers-filen säkert?",
                options: ["nano /etc/sudoers", "vim /etc/sudoers", "visudo", "edit-sudoers"],
                correctIndex: 2,
                explanation: "visudo validerar syntaxen innan sparning för att undvika att låsa sig ute."
            },
            {
                id: "ho4-q5",
                question: "Var finns användarlistan?",
                options: ["/etc/users", "/etc/passwd", "/var/users", "~/.users"],
                correctIndex: 1,
                explanation: "/etc/passwd innehåller alla användare (men inte lösenord)."
            },
            {
                id: "ho4-q6",
                question: "Var finns krypterade lösenord?",
                options: ["/etc/passwd", "/etc/shadow", "/etc/secrets", "/var/passwords"],
                correctIndex: 1,
                explanation: "/etc/shadow innehåller krypterade lösenord (endast root kan läsa)."
            },
            {
                id: "ho4-q7",
                question: "Hur tar du bort användare MED hemmapp?",
                options: ["userdel user", "userdel -r user", "deluser -h user", "removeuser -m user"],
                correctIndex: 1,
                explanation: "-r tar bort hemmappen också."
            },
            {
                id: "ho4-q8",
                question: "Hur ser du vilka grupper en användare tillhör?",
                options: ["usergroups user", "groups user", "getgroups user", "showgroups user"],
                correctIndex: 1,
                explanation: "groups user visar alla grupper användaren tillhör."
            },
            {
                id: "ho4-q9",
                question: "Hur skapar du en ny grupp?",
                options: ["newgroup name", "groupadd name", "addgroup name", "creategroup name"],
                correctIndex: 1,
                explanation: "groupadd skapar en ny grupp."
            },
            {
                id: "ho4-q10",
                question: "Hur ger du sudo utan lösenord?",
                options: ["user ALL=(ALL) NOPASSWD: ALL", "user NOPASSWD ALL", "user sudo-nopass", "user ALL NOPASS"],
                correctIndex: 0,
                explanation: "NOPASSWD: ALL i sudoers låter användaren köra sudo utan lösenord."
            },
            {
                id: "ho4-q11",
                question: "Vilken rättighet ska sudoers.d-filer ha?",
                options: ["644", "600", "440", "400"],
                correctIndex: 2,
                explanation: "440 (r--r-----) - endast root kan läsa, ingen kan skriva."
            },
            {
                id: "ho4-q12",
                question: "Hur ändrar du en användares shell?",
                options: ["chsh -s /bin/zsh user", "usermod -s /bin/zsh user", "setshell user /bin/zsh", "Båda A och B fungerar"],
                correctIndex: 3,
                explanation: "Både chsh och usermod -s fungerar för att ändra shell."
            },
            {
                id: "ho4-q13",
                question: "Hur ser du alla medlemmar i en grupp?",
                options: ["groupmembers name", "getent group name", "members name", "cat /etc/group | grep name"],
                correctIndex: 1,
                explanation: "getent group name visar gruppinfo inklusive medlemmar."
            },
            {
                id: "ho4-q14",
                question: "Vad gör chmod g+s på en katalog?",
                options: ["Tar bort läsrättighet", "Sätter SGID - nya filer ärver gruppen", "Ger execute-permission", "Låser katalogen"],
                correctIndex: 1,
                explanation: "SGID (Set Group ID) gör att nya filer ärver katalogen grupp istället för användarens primära grupp."
            },
            {
                id: "ho4-q15",
                question: "Hur tar du bort användare från grupp?",
                options: ["usermod -d group user", "gpasswd -d user group", "groupdel user group", "deluser user group"],
                correctIndex: 1,
                explanation: "gpasswd -d user group tar bort användaren från gruppen."
            },
            {
                id: "ho4-q16",
                question: "Hur visar du all info om en användare?",
                options: ["userinfo user", "id user", "whoami user", "getuser user"],
                correctIndex: 1,
                explanation: "id user visar UID, GID och alla grupper."
            },
            {
                id: "ho4-q17",
                question: "Hur byter du till annan användare?",
                options: ["switch user", "su - user", "login user", "become user"],
                correctIndex: 1,
                explanation: "su - user byter till användaren med dennes miljövariabler."
            },
            {
                id: "ho4-q18",
                question: "Hur sätter du lösenord för en användare?",
                options: ["setpasswd user", "passwd user", "password user", "usermod -p user"],
                correctIndex: 1,
                explanation: "passwd user låter dig sätta/ändra användarens lösenord."
            },
            {
                id: "ho4-q19",
                question: "Hur ger du en GRUPP sudo-rättigheter?",
                options: ["grupp ALL=(ALL:ALL) ALL", "%grupp ALL=(ALL:ALL) ALL", "@grupp ALL=(ALL:ALL) ALL", "group:grupp ALL=(ALL:ALL) ALL"],
                correctIndex: 1,
                explanation: "% före gruppnamnet i sudoers anger en grupp."
            },
            {
                id: "ho4-q20",
                question: "Vad är primär grupp?",
                options: ["Första gruppen i /etc/group", "Användarens huvudgrupp som äger nya filer", "Admin-gruppen", "Root-gruppen"],
                correctIndex: 1,
                explanation: "Primär grupp är den grupp som automatiskt äger filer användaren skapar."
            }
        ]
    },
    // ============================================
    // TASK 5: SUBNETTING (20)
    // ============================================
    {
        taskId: "handson-5-subnetting",
        taskTitle: "Subnetting",
        questions: [
            {
                id: "ho5-q1",
                question: "Hur många bitar har en IPv4-adress?",
                options: ["16", "24", "32", "64"],
                correctIndex: 2,
                explanation: "IPv4 har 32 bitar (4 oktetter × 8 bitar)."
            },
            {
                id: "ho5-q2",
                question: "/24 betyder hur många host-bitar?",
                options: ["24", "8", "16", "32"],
                correctIndex: 1,
                explanation: "32 - 24 = 8 host-bitar."
            },
            {
                id: "ho5-q3",
                question: "Hur många hosts kan ett /26-nätverk ha?",
                options: ["64", "62", "32", "30"],
                correctIndex: 1,
                explanation: "2^6 - 2 = 64 - 2 = 62 hosts (minus nätverksadress och broadcast)."
            },
            {
                id: "ho5-q4",
                question: "Vad är subnätmasken för /24?",
                options: ["255.255.0.0", "255.255.255.0", "255.255.255.128", "255.255.255.192"],
                correctIndex: 1,
                explanation: "/24 = 24 ettor = 255.255.255.0"
            },
            {
                id: "ho5-q5",
                question: "192.168.1.147/26 - vilken är nätverksadressen?",
                options: ["192.168.1.0", "192.168.1.128", "192.168.1.144", "192.168.1.192"],
                correctIndex: 1,
                explanation: "/26 = blockstorlek 64. 147 faller i blocket 128-191."
            },
            {
                id: "ho5-q6",
                question: "Vad är broadcast-adressen för 192.168.1.147/26?",
                options: ["192.168.1.191", "192.168.1.255", "192.168.1.127", "192.168.1.63"],
                correctIndex: 0,
                explanation: "Nätverket börjar på 128, broadcast = 128 + 64 - 1 = 191."
            },
            {
                id: "ho5-q7",
                question: "Vad är blockstorlek för /28?",
                options: ["8", "16", "32", "64"],
                correctIndex: 1,
                explanation: "32 - 28 = 4 host-bitar. 2^4 = 16."
            },
            {
                id: "ho5-q8",
                question: "Varför drar man bort 2 från antal adresser?",
                options: ["Router behöver 2 adresser", "Nätverksadress + broadcast kan inte användas", "Säkerhetsmarginal", "DNS behöver 2 adresser"],
                correctIndex: 1,
                explanation: "Nätverksadress (första) och broadcast (sista) kan inte tilldelas hosts."
            },
            {
                id: "ho5-q9",
                question: "Lådmetodens värden i ordning?",
                options: ["1, 2, 4, 8, 16, 32, 64, 128", "128, 64, 32, 16, 8, 4, 2, 1", "256, 128, 64, 32, 16, 8, 4, 2", "64, 32, 16, 8, 4, 2, 1, 0"],
                correctIndex: 1,
                explanation: "128, 64, 32, 16, 8, 4, 2, 1 (från vänster till höger i oktetten)."
            },
            {
                id: "ho5-q10",
                question: "Vad är subnätmasken för /27?",
                options: ["255.255.255.192", "255.255.255.224", "255.255.255.240", "255.255.255.248"],
                correctIndex: 1,
                explanation: "/27 = 3 nätverksbitar i sista oktetten. 128+64+32 = 224."
            },
            {
                id: "ho5-q11",
                question: "10.0.0.200/27 - nätverksadress?",
                options: ["10.0.0.192", "10.0.0.160", "10.0.0.224", "10.0.0.128"],
                correctIndex: 0,
                explanation: "Block: 0, 32, 64, 96, 128, 160, 192, 224. 200 faller i 192-223."
            },
            {
                id: "ho5-q12",
                question: "Vilket verktyg räknar subnät i Linux?",
                options: ["subnet", "netcalc", "ipcalc", "ipconfig"],
                correctIndex: 2,
                explanation: "ipcalc visar nätverksinfo baserat på IP och prefix."
            },
            {
                id: "ho5-q13",
                question: "/30 ger hur många användbara hosts?",
                options: ["4", "2", "6", "1"],
                correctIndex: 1,
                explanation: "2^2 - 2 = 4 - 2 = 2 hosts. Används ofta för point-to-point-länkar."
            },
            {
                id: "ho5-q14",
                question: "Hur räknar du ut subnätmask för /26?",
                options: ["32 - 26 = 6, 2^6 = 64", "26 bitar ettor = 255.255.255.192", "6 host-bitar = 192 i sista oktetten", "Alla tre är korrekta"],
                correctIndex: 3,
                explanation: "/26 har 2 nätverksbitar i sista oktetten: 128+64 = 192."
            },
            {
                id: "ho5-q15",
                question: "Hur ser du din IP och subnätmask i Linux?",
                options: ["ifconfig", "ip addr show", "netstat -i", "Både A och B"],
                correctIndex: 3,
                explanation: "Både ifconfig och ip addr show visar IP-konfiguration."
            },
            {
                id: "ho5-q16",
                question: "Vad är 172.16.10.100/25:s nätverksadress?",
                options: ["172.16.10.0", "172.16.10.128", "172.16.10.64", "172.16.10.100"],
                correctIndex: 0,
                explanation: "/25 = blockstorlek 128. 100 < 128, så nätverket börjar på 0."
            },
            {
                id: "ho5-q17",
                question: "Vad är broadcast för 172.16.10.100/25?",
                options: ["172.16.10.126", "172.16.10.127", "172.16.10.255", "172.16.10.128"],
                correctIndex: 1,
                explanation: "Nätverket är 0-127, broadcast = 127."
            },
            {
                id: "ho5-q18",
                question: "Hur installerar du ipcalc?",
                options: ["apt install calc", "apt install ipcalc", "apt install nettools", "apt install iputils"],
                correctIndex: 1,
                explanation: "sudo apt install ipcalc installerar verktyget."
            },
            {
                id: "ho5-q19",
                question: "/22 spänner över hur många oktett-värden i tredje oktetten?",
                options: ["1", "2", "4", "8"],
                correctIndex: 2,
                explanation: "/22 = 10 host-bitar = 1024 adresser = 4 × 256 (4 värden i tredje oktetten)."
            },
            {
                id: "ho5-q20",
                question: "Vad är en nätverksadress?",
                options: ["Sista adressen i subnätet", "Första adressen - identifierar nätverket", "En slumpmässig adress", "Routerns adress"],
                correctIndex: 1,
                explanation: "Nätverksadressen är första adressen och identifierar hela nätverket."
            }
        ]
    },
    // ============================================
    // TASK 6: DOCKER & CONTAINERS (20)
    // ============================================
    {
        taskId: "handson-6-docker",
        taskTitle: "Docker & Containers",
        questions: [
            {
                id: "ho6-q1",
                question: "Hur kör du en container i bakgrunden?",
                options: ["docker run -b", "docker run -d", "docker run --bg", "docker run -background"],
                correctIndex: 1,
                explanation: "-d (detached) kör containern i bakgrunden."
            },
            {
                id: "ho6-q2",
                question: "Vad gör -p 8080:80?",
                options: ["Mappar container-port 8080 till host-port 80", "Mappar host-port 8080 till container-port 80", "Öppnar port 8080 och 80", "Begränsar till port 8080-80"],
                correctIndex: 1,
                explanation: "host:container - host-porten 8080 mappas till container-porten 80."
            },
            {
                id: "ho6-q3",
                question: "Hur kör du Docker utan sudo?",
                options: ["docker --no-sudo", "chmod +s docker", "usermod -aG docker $USER", "sudo docker enable"],
                correctIndex: 2,
                explanation: "Lägg till din användare i docker-gruppen."
            },
            {
                id: "ho6-q4",
                question: "Hur listar du ALLA containers?",
                options: ["docker ps", "docker ps -a", "docker list", "docker containers"],
                correctIndex: 1,
                explanation: "docker ps -a visar alla containers, även stoppade."
            },
            {
                id: "ho6-q5",
                question: "Hur går du in i en körande container?",
                options: ["docker enter container bash", "docker exec -it container bash", "docker attach container bash", "docker shell container"],
                correctIndex: 1,
                explanation: "docker exec -it kör ett kommando (bash) interaktivt i containern."
            },
            {
                id: "ho6-q6",
                question: "Första raden i en Dockerfile?",
                options: ["IMAGE", "BASE", "FROM", "START"],
                correctIndex: 2,
                explanation: "FROM anger basimagen att bygga från."
            },
            {
                id: "ho6-q7",
                question: "Hur bygger du en image?",
                options: ["docker create -t namn .", "docker build -t namn .", "docker make -t namn .", "docker image create namn ."],
                correctIndex: 1,
                explanation: "docker build -t taggar imagen med ett namn."
            },
            {
                id: "ho6-q8",
                question: "Vad gör docker compose up -d?",
                options: ["Visar compose-filen", "Startar tjänster i bakgrunden", "Laddar ner images", "Stoppar alla tjänster"],
                correctIndex: 1,
                explanation: "up startar tjänsterna, -d kör dem i bakgrunden."
            },
            {
                id: "ho6-q9",
                question: "Hur stoppar du compose och tar bort volumes?",
                options: ["docker compose stop -v", "docker compose down -v", "docker compose rm -v", "docker compose destroy"],
                correctIndex: 1,
                explanation: "docker compose down -v stoppar och tar bort containers och volumes."
            },
            {
                id: "ho6-q10",
                question: "Hur ser du loggar för en container?",
                options: ["docker show logs container", "docker logs container", "docker output container", "docker cat container"],
                correctIndex: 1,
                explanation: "docker logs visar stdout/stderr från containern."
            },
            {
                id: "ho6-q11",
                question: "Vad gör CMD i Dockerfile?",
                options: ["Kör kommando vid byggning", "Sätter default-kommando vid start", "Kopierar filer", "Installerar paket"],
                correctIndex: 1,
                explanation: "CMD körs när containern startar (kan överskridas)."
            },
            {
                id: "ho6-q12",
                question: "Vad gör RUN i Dockerfile?",
                options: ["Startar containern", "Kör kommando vid image-byggning", "Definierar runtime-kommando", "Kör bakgrundsprocess"],
                correctIndex: 1,
                explanation: "RUN kör kommandon när imagen byggs (skapar nytt lager)."
            },
            {
                id: "ho6-q13",
                question: "Hur städar du oanvända Docker-resurser?",
                options: ["docker clean all", "docker system prune", "docker gc", "docker remove unused"],
                correctIndex: 1,
                explanation: "docker system prune tar bort oanvända containers, nätverk och images."
            },
            {
                id: "ho6-q14",
                question: "Hur tar du bort en KÖRANDE container?",
                options: ["docker rm container", "docker rm -f container", "docker kill container", "docker stop && rm container"],
                correctIndex: 1,
                explanation: "-f (force) tvingar bort även körande containers."
            },
            {
                id: "ho6-q15",
                question: "Vad gör depends_on i compose?",
                options: ["Installerar dependencies", "Definierar start-ordning", "Kopierar filer mellan containers", "Delar nätverk"],
                correctIndex: 1,
                explanation: "depends_on säger att en tjänst ska starta efter en annan."
            },
            {
                id: "ho6-q16",
                question: "Hur ser du resursanvändning för containers?",
                options: ["docker usage", "docker stats", "docker top", "docker resources"],
                correctIndex: 1,
                explanation: "docker stats visar CPU, minne, nätverk etc för körande containers."
            },
            {
                id: "ho6-q17",
                question: "Vad gör WORKDIR i Dockerfile?",
                options: ["Skapar temporär fil", "Sätter arbetskatalog i containern", "Definierar host-mapp", "Mountar volym"],
                correctIndex: 1,
                explanation: "WORKDIR sätter arbetskatalog för efterföljande RUN, CMD, COPY etc."
            },
            {
                id: "ho6-q18",
                question: "Hur kör du container interaktivt?",
                options: ["docker run -it image bash", "docker run -i image bash", "docker run --interactive image", "docker attach image bash"],
                correctIndex: 0,
                explanation: "-i interactive, -t allocate TTY. Tillsammans ger de terminal-access."
            },
            {
                id: "ho6-q19",
                question: "Hur namnger du en container?",
                options: ["docker run -n name image", "docker run --name name image", "docker run name: image", "docker run -label name image"],
                correctIndex: 1,
                explanation: "--name ger containern ett eget namn istället för slumpmässigt."
            },
            {
                id: "ho6-q20",
                question: "Hur ser du compose-tjänsternas status?",
                options: ["docker compose status", "docker compose ps", "docker compose list", "docker compose show"],
                correctIndex: 1,
                explanation: "docker compose ps visar status för tjänster i compose-projektet."
            }
        ]
    },
    // ============================================
    // TASK 7: BLOCK STORAGE & KRYPTERING (20)
    // ============================================
    {
        taskId: "handson-7-storage",
        taskTitle: "Block Storage & Kryptering",
        questions: [
            {
                id: "ho7-q1",
                question: "Hur listar du block devices?",
                options: ["fdisk -l", "lsblk", "diskutil list", "Både A och B"],
                correctIndex: 3,
                explanation: "Både fdisk -l och lsblk visar diskar och partitioner."
            },
            {
                id: "ho7-q2",
                question: "Hur partitionerar du en disk?",
                options: ["parted /dev/sdb", "fdisk /dev/sdb", "diskpart /dev/sdb", "Både A och B"],
                correctIndex: 3,
                explanation: "Både fdisk och parted kan partitionera diskar."
            },
            {
                id: "ho7-q3",
                question: "Hur skapar du ext4-filsystem?",
                options: ["format /dev/sdb1 ext4", "mkfs.ext4 /dev/sdb1", "mkext4 /dev/sdb1", "create-fs ext4 /dev/sdb1"],
                correctIndex: 1,
                explanation: "mkfs.ext4 formaterar partitionen med ext4-filsystem."
            },
            {
                id: "ho7-q4",
                question: "Vad står LVM för?",
                options: ["Linux Virtual Machine", "Logical Volume Manager", "Linux Volume Mount", "Local Virtual Memory"],
                correctIndex: 1,
                explanation: "LVM = Logical Volume Manager för flexibel diskhantering."
            },
            {
                id: "ho7-q5",
                question: "Rätt ordning för LVM-lager?",
                options: ["LV → VG → PV", "PV → VG → LV", "VG → PV → LV", "PV → LV → VG"],
                correctIndex: 1,
                explanation: "Physical Volume → Volume Group → Logical Volume."
            },
            {
                id: "ho7-q6",
                question: "Hur skapar du Physical Volume?",
                options: ["lvcreate /dev/sdb1", "pvcreate /dev/sdb1", "vgcreate /dev/sdb1", "mklvm /dev/sdb1"],
                correctIndex: 1,
                explanation: "pvcreate initierar en partition för LVM."
            },
            {
                id: "ho7-q7",
                question: "Hur skapar du Volume Group?",
                options: ["vgcreate vg_namn /dev/sdb1", "vgadd vg_namn /dev/sdb1", "vgnew vg_namn /dev/sdb1", "createvg vg_namn /dev/sdb1"],
                correctIndex: 0,
                explanation: "vgcreate skapar en Volume Group från Physical Volumes."
            },
            {
                id: "ho7-q8",
                question: "Hur skapar du 5GB Logical Volume?",
                options: ["lvcreate -s 5G -n lv vg", "lvcreate -L 5G -n lv vg", "lvnew -L 5G -n lv vg", "mklv -L 5G -n lv vg"],
                correctIndex: 1,
                explanation: "lvcreate -L (size) -n (name) skapar LV."
            },
            {
                id: "ho7-q9",
                question: "Hur utökar du ett LV med 2GB?",
                options: ["lvresize +2G /dev/vg/lv", "lvextend -L +2G /dev/vg/lv", "lvadd 2G /dev/vg/lv", "lvgrow +2G /dev/vg/lv"],
                correctIndex: 1,
                explanation: "lvextend -L +2G lägger till 2GB till volymen."
            },
            {
                id: "ho7-q10",
                question: "Efter lvextend på ext4, vad kör du?",
                options: ["e2fsck", "resize2fs", "ext4resize", "fsexpand"],
                correctIndex: 1,
                explanation: "resize2fs utökar ext4-filsystemet till den nya storleken."
            },
            {
                id: "ho7-q11",
                question: "Vad står LUKS för?",
                options: ["Linux Unified Key System", "Linux Unified Key Setup", "Logical Unix Key Storage", "Linux User Key Security"],
                correctIndex: 1,
                explanation: "LUKS = Linux Unified Key Setup för diskkryptering."
            },
            {
                id: "ho7-q12",
                question: "Hur formaterar du partition med LUKS?",
                options: ["luks format /dev/sdb1", "cryptsetup luksFormat /dev/sdb1", "encrypt /dev/sdb1", "mkluks /dev/sdb1"],
                correctIndex: 1,
                explanation: "cryptsetup luksFormat initierar LUKS-kryptering."
            },
            {
                id: "ho7-q13",
                question: "Hur öppnar du LUKS-volym?",
                options: ["luks open /dev/sdb1 namn", "cryptsetup luksOpen /dev/sdb1 namn", "decrypt /dev/sdb1 namn", "unlock /dev/sdb1 namn"],
                correctIndex: 1,
                explanation: "luksOpen dekrypterar och skapar /dev/mapper/namn."
            },
            {
                id: "ho7-q14",
                question: "Var hamnar öppnad LUKS-volym?",
                options: ["/dev/luks/namn", "/dev/mapper/namn", "/dev/crypt/namn", "/mnt/luks/namn"],
                correctIndex: 1,
                explanation: "Dekrypterade volymer skapas under /dev/mapper/."
            },
            {
                id: "ho7-q15",
                question: "Hur stänger du LUKS-volym?",
                options: ["cryptsetup close namn", "cryptsetup luksClose namn", "luks unmount namn", "Både A och B"],
                correctIndex: 3,
                explanation: "Både close och luksClose fungerar för att stänga."
            },
            {
                id: "ho7-q16",
                question: "Var konfigureras automatisk mount?",
                options: ["/etc/mounts", "/etc/fstab", "/etc/disks", "/etc/mount.conf"],
                correctIndex: 1,
                explanation: "/etc/fstab innehåller filsystem som mountas vid boot."
            },
            {
                id: "ho7-q17",
                question: "Var konfigureras automatisk LUKS-upplåsning?",
                options: ["/etc/luks.conf", "/etc/crypttab", "/etc/decrypt", "/etc/keys"],
                correctIndex: 1,
                explanation: "/etc/crypttab konfigurerar krypterade volymer."
            },
            {
                id: "ho7-q18",
                question: "Hur visar du LVM Logical Volumes?",
                options: ["lvlist", "lvs", "lvscan", "Både B och C"],
                correctIndex: 3,
                explanation: "lvs och lvscan visar Logical Volumes."
            },
            {
                id: "ho7-q19",
                question: "Hur ser du diskutrymme?",
                options: ["du -h", "df -h", "disk -h", "space -h"],
                correctIndex: 1,
                explanation: "df -h (disk free) visar ledigt utrymme per filsystem."
            },
            {
                id: "ho7-q20",
                question: "Efter lvextend på XFS, vad kör du?",
                options: ["resize2fs", "xfs_growfs /mountpoint", "xfs_resize", "xfsexpand"],
                correctIndex: 1,
                explanation: "XFS använder xfs_growfs istället för resize2fs."
            }
        ]
    }
];

// Helper functions
export function getHandsOnQuizByTaskId(taskId: string): TaskQuizSet | undefined {
    return HANDSON_TASK_QUIZ.find(set => set.taskId === taskId);
}

// Returns individual questions (flattened) - same format as DOE25
export function getAllHandsOnQuiz(): TaskQuizQuestion[] {
    return HANDSON_TASK_QUIZ.flatMap(set => set.questions);
}

// Returns quiz sets grouped by task
export function getAllHandsOnQuizSets(): TaskQuizSet[] {
    return HANDSON_TASK_QUIZ;
}

export function getTotalHandsOnQuizCount(): number {
    return HANDSON_TASK_QUIZ.reduce((total, set) => total + set.questions.length, 0);
}
