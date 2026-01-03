// Hands-On Lab Task Flashcards - 30 per task = 210 totalt

export interface TaskFlashcard {
    id: string;
    front: string;
    back: string;
    category: string;
    difficulty: 'easy' | 'medium' | 'hard';
}

export interface TaskFlashcardSet {
    taskId: string;
    taskTitle: string;
    flashcards: TaskFlashcard[];
}

export const HANDSON_TASK_FLASHCARDS: TaskFlashcardSet[] = [
    // ============================================
    // TASK 1: ONBOARDING - FILSYSTEM & TEXTEDITORER (30)
    // ============================================
    {
        taskId: "handson-1-onboarding",
        taskTitle: "Onboarding - Filsystem & Texteditorer",
        flashcards: [
            { id: "ho1-1", front: "Vilket kommando visar aktuell katalog?", back: "pwd (print working directory)", category: "Navigering", difficulty: "easy" },
            { id: "ho1-2", front: "Hur navigerar du till din hemmapp?", back: "cd ~ eller bara cd", category: "Navigering", difficulty: "easy" },
            { id: "ho1-3", front: "Hur listar du ALLA filer inkl dolda?", back: "ls -la eller ls -a", category: "Navigering", difficulty: "easy" },
            { id: "ho1-4", front: "Vad gör flaggan -p i mkdir?", back: "Skapar parent-kataloger automatiskt (mkdir -p a/b/c)", category: "Filhantering", difficulty: "easy" },
            { id: "ho1-5", front: "Hur skapar du en tom fil?", back: "touch filnamn.txt", category: "Filhantering", difficulty: "easy" },
            { id: "ho1-6", front: "Skillnad mellan > och >> vid omdirigering?", back: "> skriver över, >> lägger till (append)", category: "Filhantering", difficulty: "medium" },
            { id: "ho1-7", front: "Hur kopierar du en katalog rekursivt?", back: "cp -r källa/ mål/", category: "Filhantering", difficulty: "easy" },
            { id: "ho1-8", front: "Hur döper du om en fil?", back: "mv gammalt_namn nytt_namn", category: "Filhantering", difficulty: "easy" },
            { id: "ho1-9", front: "Varning: vad gör rm -rf?", back: "Tar bort ALLT rekursivt utan frågor - FARLIGT!", category: "Filhantering", difficulty: "medium" },
            { id: "ho1-10", front: "Hur visar du de första 10 raderna i en fil?", back: "head -10 fil.txt", category: "Filvisning", difficulty: "easy" },
            { id: "ho1-11", front: "Hur visar du de sista 20 raderna?", back: "tail -20 fil.txt", category: "Filvisning", difficulty: "easy" },
            { id: "ho1-12", front: "Hur följer du en loggfil i realtid?", back: "tail -f logfil.log", category: "Filvisning", difficulty: "medium" },
            { id: "ho1-13", front: "Vilket kommando visar fil interaktivt med scroll?", back: "less fil.txt (q för att avsluta)", category: "Filvisning", difficulty: "easy" },
            { id: "ho1-14", front: "Hur öppnar du en fil i Nano?", back: "nano filnamn.txt", category: "Nano", difficulty: "easy" },
            { id: "ho1-15", front: "Nano: Hur sparar du?", back: "Ctrl+O", category: "Nano", difficulty: "easy" },
            { id: "ho1-16", front: "Nano: Hur avslutar du?", back: "Ctrl+X", category: "Nano", difficulty: "easy" },
            { id: "ho1-17", front: "Nano: Hur söker du i texten?", back: "Ctrl+W", category: "Nano", difficulty: "medium" },
            { id: "ho1-18", front: "Nano: Hur klipper du en rad?", back: "Ctrl+K", category: "Nano", difficulty: "medium" },
            { id: "ho1-19", front: "Nano: Hur klistrar du in?", back: "Ctrl+U", category: "Nano", difficulty: "medium" },
            { id: "ho1-20", front: "Vilka två lägen har Vim?", back: "Normal mode (navigera) och Insert mode (skriva)", category: "Vim", difficulty: "easy" },
            { id: "ho1-21", front: "Vim: Hur går du till Insert mode?", back: "Tryck i", category: "Vim", difficulty: "easy" },
            { id: "ho1-22", front: "Vim: Hur går du tillbaka till Normal mode?", back: "Tryck Esc", category: "Vim", difficulty: "easy" },
            { id: "ho1-23", front: "Vim: Hur sparar du?", back: ":w", category: "Vim", difficulty: "easy" },
            { id: "ho1-24", front: "Vim: Hur avslutar du utan att spara?", back: ":q!", category: "Vim", difficulty: "medium" },
            { id: "ho1-25", front: "Vim: Hur sparar och avslutar du?", back: ":wq", category: "Vim", difficulty: "easy" },
            { id: "ho1-26", front: "Hur gör du ett script körbart?", back: "chmod +x script.sh", category: "Script", difficulty: "easy" },
            { id: "ho1-27", front: "Vad ska första raden i ett bash-script vara?", back: "#!/bin/bash (shebang)", category: "Script", difficulty: "medium" },
            { id: "ho1-28", front: "Hur kör du ett script i aktuell katalog?", back: "./script.sh", category: "Script", difficulty: "easy" },
            { id: "ho1-29", front: "Hur ser du vilken typ en fil har?", back: "file filnamn", category: "Filhantering", difficulty: "medium" },
            { id: "ho1-30", front: "Vad representerar ~ i Linux?", back: "Din hemmapp (/home/användarnamn)", category: "Navigering", difficulty: "easy" }
        ]
    },
    // ============================================
    // TASK 2: PAKETHANTERING & SSH-NYCKLAR (30)
    // ============================================
    {
        taskId: "handson-2-pakethantering",
        taskTitle: "Pakethantering & SSH-nycklar",
        flashcards: [
            { id: "ho2-1", front: "Vad ska du ALLTID köra innan apt install?", back: "sudo apt update", category: "APT", difficulty: "easy" },
            { id: "ho2-2", front: "Hur uppgraderar du alla paket?", back: "sudo apt upgrade -y", category: "APT", difficulty: "easy" },
            { id: "ho2-3", front: "Hur söker du efter ett paket?", back: "apt search paketnamn", category: "APT", difficulty: "easy" },
            { id: "ho2-4", front: "Hur visar du info om ett paket?", back: "apt show paketnamn", category: "APT", difficulty: "easy" },
            { id: "ho2-5", front: "Skillnad mellan apt remove och apt purge?", back: "remove behåller config, purge tar bort allt", category: "APT", difficulty: "medium" },
            { id: "ho2-6", front: "Vad gör apt autoremove?", back: "Tar bort oanvända beroenden", category: "APT", difficulty: "medium" },
            { id: "ho2-7", front: "Rekommenderad SSH-nyckeltyp?", back: "ed25519 (ssh-keygen -t ed25519)", category: "SSH-nycklar", difficulty: "easy" },
            { id: "ho2-8", front: "Var sparas din privata SSH-nyckel?", back: "~/.ssh/id_ed25519", category: "SSH-nycklar", difficulty: "easy" },
            { id: "ho2-9", front: "Var sparas din publika SSH-nyckel?", back: "~/.ssh/id_ed25519.pub", category: "SSH-nycklar", difficulty: "easy" },
            { id: "ho2-10", front: "Vilken nyckel ska ALDRIG delas?", back: "Den privata nyckeln", category: "SSH-nycklar", difficulty: "easy" },
            { id: "ho2-11", front: "Hur kopierar du din nyckel till en server?", back: "ssh-copy-id user@server", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-12", front: "Var på servern hamnar publika nycklar?", back: "~/.ssh/authorized_keys", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-13", front: "Vilken rättighet ska ~/.ssh ha?", back: "700 (chmod 700 ~/.ssh)", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-14", front: "Vilken rättighet ska privata nyckeln ha?", back: "600 (chmod 600 ~/.ssh/id_ed25519)", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-15", front: "Vilken rättighet ska authorized_keys ha?", back: "600", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-16", front: "Hur skapar du SSH config?", back: "nano ~/.ssh/config", category: "SSH Config", difficulty: "easy" },
            { id: "ho2-17", front: "Vad är Host i SSH config?", back: "Ett alias/genväg du definierar", category: "SSH Config", difficulty: "medium" },
            { id: "ho2-18", front: "Vad är HostName i SSH config?", back: "Den verkliga IP-adressen eller domänen", category: "SSH Config", difficulty: "medium" },
            { id: "ho2-19", front: "Hur anger du användare i SSH config?", back: "User användarnamn", category: "SSH Config", difficulty: "easy" },
            { id: "ho2-20", front: "Hur anger du specifik nyckel i SSH config?", back: "IdentityFile ~/.ssh/min_nyckel", category: "SSH Config", difficulty: "medium" },
            { id: "ho2-21", front: "Hur anger du annan port i SSH config?", back: "Port 2222", category: "SSH Config", difficulty: "medium" },
            { id: "ho2-22", front: "Om du har Host prod, hur ansluter du?", back: "ssh prod", category: "SSH Config", difficulty: "easy" },
            { id: "ho2-23", front: "Vad är en passphrase på SSH-nyckel?", back: "Lösenord för att använda nyckeln (extra säkerhet)", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-24", front: "Varför är SSH-nycklar säkrare än lösenord?", back: "Omöjligt att gissa, ingen brute-force möjlig", category: "SSH-nycklar", difficulty: "easy" },
            { id: "ho2-25", front: "Hur genererar du nyckel med kommentar?", back: "ssh-keygen -t ed25519 -C 'kommentar'", category: "SSH-nycklar", difficulty: "medium" },
            { id: "ho2-26", front: "Vilket paket ger htop?", back: "htop (sudo apt install htop)", category: "APT", difficulty: "easy" },
            { id: "ho2-27", front: "Vad visar tree-kommandot?", back: "Katalogstruktur som träd", category: "APT", difficulty: "easy" },
            { id: "ho2-28", front: "Hur laddar du ner en fil med kommandot?", back: "wget URL eller curl -O URL", category: "APT", difficulty: "medium" },
            { id: "ho2-29", front: "Hur visar du SSH-nyckelns fingerprint?", back: "ssh-keygen -lf ~/.ssh/id_ed25519.pub", category: "SSH-nycklar", difficulty: "hard" },
            { id: "ho2-30", front: "Vad är ssh-agent?", back: "Program som håller nycklar i minnet så du slipper ange passphrase", category: "SSH-nycklar", difficulty: "hard" }
        ]
    },
    // ============================================
    // TASK 3: SSH & BRANDVÄGG (30)
    // ============================================
    {
        taskId: "handson-3-ssh-brandvagg",
        taskTitle: "SSH & Brandvägg",
        flashcards: [
            { id: "ho3-1", front: "Var finns SSH-serverns konfiguration?", back: "/etc/ssh/sshd_config", category: "SSH Server", difficulty: "easy" },
            { id: "ho3-2", front: "Hur blockerar du root-login via SSH?", back: "PermitRootLogin no", category: "SSH Server", difficulty: "easy" },
            { id: "ho3-3", front: "Hur inaktiverar du lösenords-inloggning?", back: "PasswordAuthentication no", category: "SSH Server", difficulty: "medium" },
            { id: "ho3-4", front: "Hur aktiverar du nyckel-autentisering?", back: "PubkeyAuthentication yes", category: "SSH Server", difficulty: "medium" },
            { id: "ho3-5", front: "Hur begränsar du vilka användare som får SSH:a?", back: "AllowUsers user1 user2", category: "SSH Server", difficulty: "medium" },
            { id: "ho3-6", front: "Vilken är default SSH-port?", back: "22", category: "SSH Server", difficulty: "easy" },
            { id: "ho3-7", front: "Hur byter du SSH-port?", back: "Port 2222 (i sshd_config)", category: "SSH Server", difficulty: "easy" },
            { id: "ho3-8", front: "Hur validerar du sshd_config innan omstart?", back: "sudo sshd -t", category: "SSH Server", difficulty: "medium" },
            { id: "ho3-9", front: "Hur startar du om SSH-tjänsten?", back: "sudo systemctl restart sshd", category: "SSH Server", difficulty: "easy" },
            { id: "ho3-10", front: "VIKTIGT: Vad ska du göra efter SSH-ändringar?", back: "Testa i NY terminal innan du stänger gamla!", category: "SSH Server", difficulty: "easy" },
            { id: "ho3-11", front: "Vad står UFW för?", back: "Uncomplicated Firewall", category: "UFW", difficulty: "easy" },
            { id: "ho3-12", front: "Hur ser du UFW-status?", back: "sudo ufw status", category: "UFW", difficulty: "easy" },
            { id: "ho3-13", front: "Hur sätter du default: blockera inkommande?", back: "sudo ufw default deny incoming", category: "UFW", difficulty: "medium" },
            { id: "ho3-14", front: "Hur sätter du default: tillåt utgående?", back: "sudo ufw default allow outgoing", category: "UFW", difficulty: "medium" },
            { id: "ho3-15", front: "Hur tillåter du SSH i UFW?", back: "sudo ufw allow ssh", category: "UFW", difficulty: "easy" },
            { id: "ho3-16", front: "Hur tillåter du specifik port?", back: "sudo ufw allow 2222/tcp", category: "UFW", difficulty: "medium" },
            { id: "ho3-17", front: "Hur tillåter du HTTP och HTTPS?", back: "sudo ufw allow 80/tcp && sudo ufw allow 443/tcp", category: "UFW", difficulty: "medium" },
            { id: "ho3-18", front: "Hur aktiverar du UFW?", back: "sudo ufw enable", category: "UFW", difficulty: "easy" },
            { id: "ho3-19", front: "KRITISKT: Vad måste du göra INNAN ufw enable?", back: "Tillåta SSH-porten!", category: "UFW", difficulty: "easy" },
            { id: "ho3-20", front: "Hur ser du UFW-regler med nummer?", back: "sudo ufw status numbered", category: "UFW", difficulty: "medium" },
            { id: "ho3-21", front: "Hur tar du bort regel nummer 3?", back: "sudo ufw delete 3", category: "UFW", difficulty: "medium" },
            { id: "ho3-22", front: "Hur tillåter du från specifik IP?", back: "sudo ufw allow from 192.168.1.100", category: "UFW", difficulty: "hard" },
            { id: "ho3-23", front: "Hur tillåter du port-range?", back: "sudo ufw allow 3000:3010/tcp", category: "UFW", difficulty: "hard" },
            { id: "ho3-24", front: "Hur inaktiverar du UFW tillfälligt?", back: "sudo ufw disable", category: "UFW", difficulty: "easy" },
            { id: "ho3-25", front: "Var finns UFW-loggar?", back: "/var/log/ufw.log", category: "UFW", difficulty: "medium" },
            { id: "ho3-26", front: "Hur ser du SSH-loggar live?", back: "sudo journalctl -u sshd -f", category: "Felsökning", difficulty: "medium" },
            { id: "ho3-27", front: "Hur testar du SSH verbose?", back: "ssh -v user@server", category: "Felsökning", difficulty: "medium" },
            { id: "ho3-28", front: "Hur ser du vad som lyssnar på portar?", back: "sudo ss -tlnp", category: "Felsökning", difficulty: "medium" },
            { id: "ho3-29", front: "ClientAliveInterval 300 gör vad?", back: "Skickar keepalive var 300:e sekund", category: "SSH Server", difficulty: "hard" },
            { id: "ho3-30", front: "Hur ansluter du till SSH på annan port?", back: "ssh -p 2222 user@server", category: "SSH Server", difficulty: "easy" }
        ]
    },
    // ============================================
    // TASK 4: ANVÄNDARHANTERING (30)
    // ============================================
    {
        taskId: "handson-4-anvandarhantering",
        taskTitle: "Användarhantering",
        flashcards: [
            { id: "ho4-1", front: "Hur skapar du användare med hemmapp?", back: "sudo useradd -m användarnamn", category: "Användare", difficulty: "easy" },
            { id: "ho4-2", front: "Vad gör flaggan -m i useradd?", back: "Skapar hemmapp automatiskt", category: "Användare", difficulty: "easy" },
            { id: "ho4-3", front: "Hur sätter du shell vid skapande?", back: "useradd -s /bin/bash användarnamn", category: "Användare", difficulty: "medium" },
            { id: "ho4-4", front: "Hur lägger du till beskrivning?", back: "useradd -c 'Full Name' användarnamn", category: "Användare", difficulty: "medium" },
            { id: "ho4-5", front: "Hur sätter du lösenord för användare?", back: "sudo passwd användarnamn", category: "Användare", difficulty: "easy" },
            { id: "ho4-6", front: "Hur tar du bort användare MED hemmapp?", back: "sudo userdel -r användarnamn", category: "Användare", difficulty: "medium" },
            { id: "ho4-7", front: "Hur lägger du till användare i grupp?", back: "sudo usermod -aG gruppnamn användarnamn", category: "Grupper", difficulty: "easy" },
            { id: "ho4-8", front: "Vad gör -a i usermod -aG?", back: "Append - lägger till utan att ta bort från andra grupper", category: "Grupper", difficulty: "medium" },
            { id: "ho4-9", front: "Hur ändrar du en användares shell?", back: "sudo usermod -s /bin/zsh användarnamn", category: "Användare", difficulty: "medium" },
            { id: "ho4-10", front: "Hur ser du vilka grupper en användare tillhör?", back: "groups användarnamn", category: "Grupper", difficulty: "easy" },
            { id: "ho4-11", front: "Hur skapar du en ny grupp?", back: "sudo groupadd gruppnamn", category: "Grupper", difficulty: "easy" },
            { id: "ho4-12", front: "Hur tar du bort en grupp?", back: "sudo groupdel gruppnamn", category: "Grupper", difficulty: "easy" },
            { id: "ho4-13", front: "Hur ser du medlemmar i en grupp?", back: "getent group gruppnamn", category: "Grupper", difficulty: "medium" },
            { id: "ho4-14", front: "Hur tar du bort användare från grupp?", back: "sudo gpasswd -d användarnamn gruppnamn", category: "Grupper", difficulty: "hard" },
            { id: "ho4-15", front: "Hur ger du sudo-rättigheter?", back: "sudo usermod -aG sudo användarnamn", category: "Sudo", difficulty: "easy" },
            { id: "ho4-16", front: "Hur redigerar du sudoers säkert?", back: "sudo visudo", category: "Sudo", difficulty: "medium" },
            { id: "ho4-17", front: "Var kan du lägga sudoers-filer?", back: "/etc/sudoers.d/", category: "Sudo", difficulty: "medium" },
            { id: "ho4-18", front: "Vilken rättighet ska sudoers-filer ha?", back: "440 (chmod 440)", category: "Sudo", difficulty: "hard" },
            { id: "ho4-19", front: "Hur ger du sudo utan lösenord?", back: "user ALL=(ALL) NOPASSWD: ALL", category: "Sudo", difficulty: "hard" },
            { id: "ho4-20", front: "Hur begränsar du sudo till specifika kommandon?", back: "user ALL=(ALL) NOPASSWD: /usr/bin/rsync", category: "Sudo", difficulty: "hard" },
            { id: "ho4-21", front: "Hur ger du en grupp sudo?", back: "%gruppnamn ALL=(ALL:ALL) ALL", category: "Sudo", difficulty: "hard" },
            { id: "ho4-22", front: "Var finns användarlistan?", back: "/etc/passwd", category: "Filer", difficulty: "easy" },
            { id: "ho4-23", front: "Var finns krypterade lösenord?", back: "/etc/shadow", category: "Filer", difficulty: "medium" },
            { id: "ho4-24", front: "Var finns grupplistan?", back: "/etc/group", category: "Filer", difficulty: "easy" },
            { id: "ho4-25", front: "Hur listar du användare med bash-shell?", back: "cat /etc/passwd | grep bash", category: "Filer", difficulty: "medium" },
            { id: "ho4-26", front: "Vad är primär grupp?", back: "Användarens huvudgrupp (äger filer som skapas)", category: "Grupper", difficulty: "medium" },
            { id: "ho4-27", front: "Hur ändrar du primär grupp?", back: "sudo usermod -g gruppnamn användarnamn", category: "Grupper", difficulty: "hard" },
            { id: "ho4-28", front: "Vad gör chmod g+s på en katalog?", back: "SGID - nya filer ärver gruppägaren", category: "Rättigheter", difficulty: "hard" },
            { id: "ho4-29", front: "Hur ser du all info om en användare?", back: "id användarnamn", category: "Användare", difficulty: "easy" },
            { id: "ho4-30", front: "Hur byter du till annan användare?", back: "su - användarnamn", category: "Användare", difficulty: "easy" }
        ]
    },
    // ============================================
    // TASK 5: SUBNETTING (30)
    // ============================================
    {
        taskId: "handson-5-subnetting",
        taskTitle: "Subnetting",
        flashcards: [
            { id: "ho5-1", front: "Hur många bitar har en IPv4-adress?", back: "32 bitar", category: "Grunder", difficulty: "easy" },
            { id: "ho5-2", front: "Hur många oktetter har en IPv4-adress?", back: "4 oktetter (8 bitar var)", category: "Grunder", difficulty: "easy" },
            { id: "ho5-3", front: "Vad anger prefixet i /24?", back: "24 bitar för nätverksdelen", category: "Grunder", difficulty: "easy" },
            { id: "ho5-4", front: "Formel: Host-bitar = ?", back: "32 - prefix", category: "Beräkning", difficulty: "easy" },
            { id: "ho5-5", front: "Formel: Blockstorlek = ?", back: "2^(host-bitar)", category: "Beräkning", difficulty: "medium" },
            { id: "ho5-6", front: "Formel: Antal hosts = ?", back: "Blockstorlek - 2", category: "Beräkning", difficulty: "medium" },
            { id: "ho5-7", front: "Varför -2 vid antal hosts?", back: "Nätverksadress + broadcast kan inte användas", category: "Beräkning", difficulty: "medium" },
            { id: "ho5-8", front: "/24 ger hur många host-bitar?", back: "8 (32-24=8)", category: "Prefix", difficulty: "easy" },
            { id: "ho5-9", front: "/24 ger hur många hosts?", back: "254 (2^8 - 2 = 256-2)", category: "Prefix", difficulty: "medium" },
            { id: "ho5-10", front: "/26 ger hur många host-bitar?", back: "6 (32-26=6)", category: "Prefix", difficulty: "medium" },
            { id: "ho5-11", front: "/26 ger hur många hosts?", back: "62 (2^6 - 2 = 64-2)", category: "Prefix", difficulty: "medium" },
            { id: "ho5-12", front: "/28 ger hur många hosts?", back: "14 (2^4 - 2 = 16-2)", category: "Prefix", difficulty: "medium" },
            { id: "ho5-13", front: "/30 ger hur många hosts?", back: "2 (2^2 - 2 = 4-2)", category: "Prefix", difficulty: "hard" },
            { id: "ho5-14", front: "Subnätmask för /24?", back: "255.255.255.0", category: "Subnätmask", difficulty: "easy" },
            { id: "ho5-15", front: "Subnätmask för /26?", back: "255.255.255.192", category: "Subnätmask", difficulty: "medium" },
            { id: "ho5-16", front: "Subnätmask för /28?", back: "255.255.255.240", category: "Subnätmask", difficulty: "hard" },
            { id: "ho5-17", front: "Blockstorlek för /26?", back: "64", category: "Blockstorlek", difficulty: "medium" },
            { id: "ho5-18", front: "Blockstorlek för /27?", back: "32", category: "Blockstorlek", difficulty: "medium" },
            { id: "ho5-19", front: "Blockstorlek för /28?", back: "16", category: "Blockstorlek", difficulty: "medium" },
            { id: "ho5-20", front: "192.168.1.147/26 - nätverksadress?", back: "192.168.1.128 (block: 0,64,128,192)", category: "Beräkning", difficulty: "hard" },
            { id: "ho5-21", front: "192.168.1.147/26 - broadcast?", back: "192.168.1.191 (128+64-1)", category: "Beräkning", difficulty: "hard" },
            { id: "ho5-22", front: "10.0.0.200/27 - nätverksadress?", back: "10.0.0.192 (block: 0,32,64,...,192,224)", category: "Beräkning", difficulty: "hard" },
            { id: "ho5-23", front: "Lådmetoden värden?", back: "128, 64, 32, 16, 8, 4, 2, 1", category: "Lådmetoden", difficulty: "easy" },
            { id: "ho5-24", front: "Hur räknar du ut subnätmask för /27?", back: "3 nätverksbitar i sista oktetten: 128+64+32=224", category: "Subnätmask", difficulty: "hard" },
            { id: "ho5-25", front: "Vilket verktyg verifierar subnetting?", back: "ipcalc", category: "Verktyg", difficulty: "easy" },
            { id: "ho5-26", front: "Hur installerar du ipcalc?", back: "sudo apt install ipcalc", category: "Verktyg", difficulty: "easy" },
            { id: "ho5-27", front: "Vad är en broadcast-adress?", back: "Sista adressen i subnätet - skickar till alla", category: "Grunder", difficulty: "medium" },
            { id: "ho5-28", front: "Vad är nätverksadressen?", back: "Första adressen i subnätet - identifierar nätverket", category: "Grunder", difficulty: "medium" },
            { id: "ho5-29", front: "Vilka IP kan användas som hosts i 192.168.1.0/24?", back: "192.168.1.1 - 192.168.1.254", category: "Beräkning", difficulty: "medium" },
            { id: "ho5-30", front: "Hur ser du din IP och subnät i Linux?", back: "ip addr show eller ip a", category: "Verktyg", difficulty: "easy" }
        ]
    },
    // ============================================
    // TASK 6: DOCKER & CONTAINERS (30)
    // ============================================
    {
        taskId: "handson-6-docker",
        taskTitle: "Docker & Containers",
        flashcards: [
            { id: "ho6-1", front: "Hur installerar du Docker snabbt?", back: "curl -fsSL https://get.docker.com | sh", category: "Installation", difficulty: "easy" },
            { id: "ho6-2", front: "Hur kör du Docker utan sudo?", back: "sudo usermod -aG docker \$USER && newgrp docker", category: "Installation", difficulty: "medium" },
            { id: "ho6-3", front: "Hur kör du en container interaktivt?", back: "docker run -it ubuntu bash", category: "Containers", difficulty: "easy" },
            { id: "ho6-4", front: "Vad gör -d flaggan i docker run?", back: "Detached - kör i bakgrunden", category: "Containers", difficulty: "easy" },
            { id: "ho6-5", front: "Vad gör -p 8080:80?", back: "Mappar host-port 8080 till container-port 80", category: "Containers", difficulty: "medium" },
            { id: "ho6-6", front: "Hur namnger du en container?", back: "--name mittnamn", category: "Containers", difficulty: "easy" },
            { id: "ho6-7", front: "Hur listar du körande containers?", back: "docker ps", category: "Containers", difficulty: "easy" },
            { id: "ho6-8", front: "Hur listar du ALLA containers?", back: "docker ps -a", category: "Containers", difficulty: "easy" },
            { id: "ho6-9", front: "Hur stoppar du en container?", back: "docker stop containernamn", category: "Containers", difficulty: "easy" },
            { id: "ho6-10", front: "Hur startar du en stoppad container?", back: "docker start containernamn", category: "Containers", difficulty: "easy" },
            { id: "ho6-11", front: "Hur tar du bort en container?", back: "docker rm containernamn", category: "Containers", difficulty: "easy" },
            { id: "ho6-12", front: "Hur tar du bort en KÖRANDE container?", back: "docker rm -f containernamn", category: "Containers", difficulty: "medium" },
            { id: "ho6-13", front: "Hur listar du images?", back: "docker images", category: "Images", difficulty: "easy" },
            { id: "ho6-14", front: "Hur laddar du ner en image?", back: "docker pull nginx:latest", category: "Images", difficulty: "easy" },
            { id: "ho6-15", front: "Hur tar du bort en image?", back: "docker rmi imagename", category: "Images", difficulty: "easy" },
            { id: "ho6-16", front: "Hur städar du oanvända resurser?", back: "docker system prune -a", category: "Images", difficulty: "medium" },
            { id: "ho6-17", front: "Första raden i Dockerfile?", back: "FROM basimage", category: "Dockerfile", difficulty: "easy" },
            { id: "ho6-18", front: "Vad gör WORKDIR i Dockerfile?", back: "Sätter arbetskatalog i containern", category: "Dockerfile", difficulty: "medium" },
            { id: "ho6-19", front: "Vad gör COPY i Dockerfile?", back: "Kopierar filer från host till image", category: "Dockerfile", difficulty: "easy" },
            { id: "ho6-20", front: "Vad gör RUN i Dockerfile?", back: "Kör kommando vid image-byggning", category: "Dockerfile", difficulty: "medium" },
            { id: "ho6-21", front: "Vad gör CMD i Dockerfile?", back: "Sätter default-kommando när container startar", category: "Dockerfile", difficulty: "medium" },
            { id: "ho6-22", front: "Hur bygger du en image?", back: "docker build -t namn:tag .", category: "Dockerfile", difficulty: "medium" },
            { id: "ho6-23", front: "Hur ser du loggar för en container?", back: "docker logs containernamn", category: "Felsökning", difficulty: "easy" },
            { id: "ho6-24", front: "Hur går du in i en körande container?", back: "docker exec -it containernamn bash", category: "Felsökning", difficulty: "medium" },
            { id: "ho6-25", front: "Hur startar du docker-compose stack?", back: "docker compose up -d", category: "Compose", difficulty: "easy" },
            { id: "ho6-26", front: "Hur stoppar du docker-compose stack?", back: "docker compose down", category: "Compose", difficulty: "easy" },
            { id: "ho6-27", front: "Hur tar du bort volumes med compose?", back: "docker compose down -v", category: "Compose", difficulty: "medium" },
            { id: "ho6-28", front: "Hur ser du compose-loggar?", back: "docker compose logs -f", category: "Compose", difficulty: "easy" },
            { id: "ho6-29", front: "Vad gör depends_on i compose?", back: "Definierar start-ordning mellan tjänster", category: "Compose", difficulty: "medium" },
            { id: "ho6-30", front: "Hur ser du resursanvändning för containers?", back: "docker stats", category: "Felsökning", difficulty: "medium" }
        ]
    },
    // ============================================
    // TASK 7: BLOCK STORAGE & KRYPTERING (30)
    // ============================================
    {
        taskId: "handson-7-storage",
        taskTitle: "Block Storage & Kryptering",
        flashcards: [
            { id: "ho7-1", front: "Hur listar du block devices?", back: "lsblk", category: "Diskar", difficulty: "easy" },
            { id: "ho7-2", front: "Hur ser du detaljerad diskinfo?", back: "sudo fdisk -l", category: "Diskar", difficulty: "easy" },
            { id: "ho7-3", front: "Hur ser du diskutrymme?", back: "df -h", category: "Diskar", difficulty: "easy" },
            { id: "ho7-4", front: "Vilket verktyg partitionerar diskar?", back: "fdisk (sudo fdisk /dev/sdb)", category: "Partitioner", difficulty: "easy" },
            { id: "ho7-5", front: "fdisk: Hur skapar du ny partition?", back: "n (new)", category: "Partitioner", difficulty: "medium" },
            { id: "ho7-6", front: "fdisk: Hur sparar du och avslutar?", back: "w (write)", category: "Partitioner", difficulty: "medium" },
            { id: "ho7-7", front: "Hur skapar du ext4-filsystem?", back: "sudo mkfs.ext4 /dev/sdb1", category: "Filsystem", difficulty: "easy" },
            { id: "ho7-8", front: "Hur skapar du xfs-filsystem?", back: "sudo mkfs.xfs /dev/sdb1", category: "Filsystem", difficulty: "medium" },
            { id: "ho7-9", front: "Hur mountar du en partition?", back: "sudo mount /dev/sdb1 /mnt/data", category: "Mount", difficulty: "easy" },
            { id: "ho7-10", front: "Var konfigureras permanent mount?", back: "/etc/fstab", category: "Mount", difficulty: "medium" },
            { id: "ho7-11", front: "Vad står LVM för?", back: "Logical Volume Manager", category: "LVM", difficulty: "easy" },
            { id: "ho7-12", front: "Tre LVM-lager i ordning?", back: "PV → VG → LV", category: "LVM", difficulty: "medium" },
            { id: "ho7-13", front: "Vad är PV i LVM?", back: "Physical Volume - fysisk disk/partition", category: "LVM", difficulty: "medium" },
            { id: "ho7-14", front: "Vad är VG i LVM?", back: "Volume Group - pool av PVs", category: "LVM", difficulty: "medium" },
            { id: "ho7-15", front: "Vad är LV i LVM?", back: "Logical Volume - virtuell partition", category: "LVM", difficulty: "medium" },
            { id: "ho7-16", front: "Hur skapar du Physical Volume?", back: "sudo pvcreate /dev/sdb1", category: "LVM", difficulty: "medium" },
            { id: "ho7-17", front: "Hur skapar du Volume Group?", back: "sudo vgcreate vg_namn /dev/sdb1", category: "LVM", difficulty: "hard" },
            { id: "ho7-18", front: "Hur skapar du Logical Volume?", back: "sudo lvcreate -L 5G -n lv_namn vg_namn", category: "LVM", difficulty: "hard" },
            { id: "ho7-19", front: "Hur visar du PV-info?", back: "sudo pvs", category: "LVM", difficulty: "medium" },
            { id: "ho7-20", front: "Hur visar du VG-info?", back: "sudo vgs", category: "LVM", difficulty: "medium" },
            { id: "ho7-21", front: "Hur visar du LV-info?", back: "sudo lvs", category: "LVM", difficulty: "medium" },
            { id: "ho7-22", front: "Hur utökar du ett LV?", back: "sudo lvextend -L +2G /dev/vg/lv", category: "LVM", difficulty: "hard" },
            { id: "ho7-23", front: "Hur utökar du ext4 efter lvextend?", back: "sudo resize2fs /dev/vg/lv", category: "LVM", difficulty: "hard" },
            { id: "ho7-24", front: "Hur utökar du xfs efter lvextend?", back: "sudo xfs_growfs /mountpoint", category: "LVM", difficulty: "hard" },
            { id: "ho7-25", front: "Vad står LUKS för?", back: "Linux Unified Key Setup", category: "LUKS", difficulty: "easy" },
            { id: "ho7-26", front: "Hur formaterar du med LUKS?", back: "sudo cryptsetup luksFormat /dev/sdb1", category: "LUKS", difficulty: "medium" },
            { id: "ho7-27", front: "Hur öppnar du LUKS-volym?", back: "sudo cryptsetup luksOpen /dev/sdb1 namn", category: "LUKS", difficulty: "medium" },
            { id: "ho7-28", front: "Var hamnar öppnad LUKS-volym?", back: "/dev/mapper/namn", category: "LUKS", difficulty: "hard" },
            { id: "ho7-29", front: "Hur stänger du LUKS-volym?", back: "sudo cryptsetup luksClose namn", category: "LUKS", difficulty: "medium" },
            { id: "ho7-30", front: "Var konfigureras automatisk LUKS-mount?", back: "/etc/crypttab + /etc/fstab", category: "LUKS", difficulty: "hard" }
        ]
    }
];

// Helper function
export function getHandsOnFlashcardsByTaskId(taskId: string): TaskFlashcardSet | undefined {
    return HANDSON_TASK_FLASHCARDS.find(set => set.taskId === taskId);
}

export function getAllHandsOnFlashcards(): TaskFlashcardSet[] {
    return HANDSON_TASK_FLASHCARDS;
}

export function getTotalHandsOnFlashcardCount(): number {
    return HANDSON_TASK_FLASHCARDS.reduce((total, set) => total + set.flashcards.length, 0);
}
