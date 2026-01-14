"""
NOD: SSH och säker kommunikation
================================
Fjärrstyrning och nyckelhantering för säker serverkommunikation
"""

SSH_KOMMUNIKATION_NODE = {
    "title": "SSH och säker kommunikation",
    "slug": "ssh-kommunikation",
    "description": "Fjärrstyrning och nyckelhantering för säker serverkommunikation",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 110,
    "order_index": 5,
    "content": r"""# SSH och säker kommunikation

Fokus: Fjärrstyrning och nyckelhantering

## SSH-nyckelpar: Skapa med ssh-keygen

SSH använder public key-kryptografi för säker autentisering. Du skapar ett nyckelpar:

- **Privat nyckel**: Hålls hemlig, finns på din klient
- **Publik nyckel**: Delas med servrar, läggs i ~/.ssh/authorized_keys

```bash
# Skapa nyckelpar
ssh-keygen -t ed25519 -C "your_email@example.com"

# Eller med RSA (äldre, men fortfarande vanligt)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Med specifikt filnamn
ssh-keygen -t ed25519 -f ~/.ssh/my_server_key
```

**Frågor som ställs**:
- Fil att spara nyckeln i: ~/.ssh/id_ed25519 (standard)
- Lösenfras: Valfritt lösenord för att skydda privat nyckel

### Vad händer om du tappar bort lösenfrasen?

**Kritiskt**: Om du tappar bort lösenfrasen till din privata nyckel kan du INTE återställa den. Lösenfrasen används för att kryptera den privata nyckeln lokalt.

```bash
# Om lösenfrasen tappas bort:
# 1. Du kan inte dekryptera den privata nyckeln
# 2. Nyckeln blir oanvändbar
# 3. Du måste skapa en ny nyckel och distribuera den igen

# Lösning: Använd lösenordshanterare för att spara lösenfras
# eller skapa nycklar utan lösenfras (mindre säkert, men användbart för automation)
```

### Första anslutning och known_hosts

Vid första anslutning till en okänd SSH-server:

```bash
# Första anslutning
ssh user@newserver.com
# The authenticity of host 'newserver.com (192.0.2.1)' can't be established.
# ECDSA key fingerprint is SHA256:abc123...
# Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

# Serverns publika nyckel (fingeravtryck) sparas i ~/.ssh/known_hosts
```

**Vad händer**: SSH-servern skickar sin publika nyckel för identitetsverifiering. Om du accepterar sparas den i ~/.ssh/known_hosts.

```bash
# Visa known_hosts
cat ~/.ssh/known_hosts

# Om serverns nyckel ändras (t.ex. efter ominstallation):
# WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
# Detta kan betyda att någon försöker göra man-in-the-middle-attack
# eller att servern faktiskt har ändrats

# Radera gammal post
ssh-keygen -R newserver.com
```

```bash
# Nycklar skapas i ~/.ssh/
ls -la ~/.ssh/
# id_ed25519      # Privat nyckel (HEMLIG!)
# id_ed25519.pub  # Publik nyckel (kan delas)
```

**Kritiskt**: Skydda privat nyckel

```bash
# Korrekta behörigheter
chmod 600 ~/.ssh/id_ed25519      # Privat nyckel: endast ägare kan läsa
chmod 644 ~/.ssh/id_ed25519.pub  # Publik nyckel: kan delas
chmod 700 ~/.ssh                 # .ssh-katalog: endast ägare
```

## Distribuera med ssh-copy-id

Det enklaste sättet att kopiera din publika nyckel till en server:

```bash
# Kopiera publik nyckel till server
ssh-copy-id user@server.com

# Med specifik nyckel
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server.com

# Med specifik port
ssh-copy-id -p 2222 user@server.com
```

**Vad händer**: ssh-copy-id lägger till din publika nyckel i ~/.ssh/authorized_keys på servern.

### Manuell distribution

```bash
# 1. Visa publik nyckel
cat ~/.ssh/id_ed25519.pub

# 2. Kopiera innehållet

# 3. På servern, lägg till i authorized_keys
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "public_key_content" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

## SSH Agent: Använda ssh-add för att slippa lösenfras

SSH Agent håller dina privata nycklar i minnet så du inte behöver skriva lösenfras varje gång.

```bash
# Starta SSH-agent (om inte redan igång)
eval "$(ssh-agent -s)"

# Lägg till nyckel till agent
ssh-add ~/.ssh/id_ed25519

# Lista nycklar i agent
ssh-add -l
# 256 SHA256:abc123... user@host (ED25519)
# Visar: nyckelstorlek, fingeravtryck, kommentar, typ

# Visa detaljerad information
ssh-add -L
# Visar den publika nyckeln för varje nyckel i agenten

# Radera nyckel från agent
ssh-add -d ~/.ssh/id_ed25519

# Radera alla nycklar
ssh-add -D
```

### Agent Forwarding

Agent Forwarding låter din lokala SSH-agent användas för att nå servrar via en hoppserver.

```bash
# Aktivera agent forwarding
ssh -A user@jumpserver.com
# -A = Aktivera agent forwarding

# Nu kan du från hoppserver använda din lokala agent
# för att ansluta till andra servrar utan att kopiera nycklar

# I ~/.ssh/config:
Host jumpserver
    HostName jumpserver.com
    ForwardAgent yes
```

**Användning**: När du behöver nå servrar via en hoppserver (bastion host) utan att kopiera nycklar till hoppservern.

**Säkerhetsvarning**: Agent forwarding kan vara en säkerhetsrisk om hoppservern komprometteras - använd bara på betrodda servrar.

### Automatisk start av SSH-agent

Lägg till i ~/.bashrc eller ~/.zshrc:

```bash
# Starta SSH-agent om den inte redan exekveras
if [ -z "$SSH_AUTH_SOCK" ]; then
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
fi
```

## Säkerhet: Inaktivera lösenordsinloggning i /etc/ssh/sshd_config

När du har konfigurerat SSH-nycklar bör du inaktivera lösenordsinloggning för extra säkerhet.

```bash
# Redigera SSH-serverkonfiguration
sudo nano /etc/ssh/sshd_config

# Ändra dessa rader:
PasswordAuthentication no
PubkeyAuthentication yes
PermitRootLogin no  # Förhindra root-inloggning (rekommenderat)
MaxAuthTries 3      # Max antal inloggningsförsök per anslutning
```

### Starta om SSH-tjänst

```bash
sudo systemctl restart sshd
# eller
sudo systemctl restart ssh
```

**Varning**: Kontrollera att du kan logga in med nyckel INNAN du stänger av lösenordsinloggning!

### Testa konfiguration innan omstart

```bash
# Testa konfiguration (ingen omstart)
sudo sshd -t

# Om inga fel, starta om
sudo systemctl restart sshd
```

### Återställning om du blir utelåst

Om du stänger av lösenordsinloggning och inte kan logga in med nyckel:

1. Logga in via konsol/KVM (fysisk åtkomst)
2. Eller via cloud provider's konsol
3. Återställ konfigurationen

## Tunnlar: Grunderna i SSH-tunnling

SSH-tunnling låter dig skicka trafik genom en säker SSH-anslutning.

### Lokal portvidarebefordran

Skicka lokal trafik till fjärrserver via SSH.

```bash
# Format: ssh -L [lokal_port]:[destination]:[destinations_port] user@ssh_server
ssh -L 8080:localhost:80 user@server.com

# Nu kan du nå server:80 via localhost:8080
curl http://localhost:8080
```

**Användningsfall**: Nå en databas på fjärrserver som bara lyssnar på localhost.

```bash
# Exempel: Nå MySQL på fjärrserver
ssh -L 3306:localhost:3306 user@server.com
# Nu kan du ansluta till MySQL som om den vore lokal
mysql -h 127.0.0.1 -P 3306
```

### Fjärrportvidarebefordran

Skicka fjärrtrafik tillbaka till din lokala maskin.

```bash
# Format: ssh -R [fjärr_port]:[lokal_destination]:[lokal_port] user@ssh_server
ssh -R 8080:localhost:3000 user@server.com

# Nu kan någon på server.com nå din lokala port 3000 via server:8080
```

**Användningsfall**: Exponera lokal utvecklingsserver till internet via fjärrserver.

```bash
# Exempel: Exponera lokal webbserver
ssh -R 8080:localhost:3000 user@server.com
# Nu kan någon nå http://server.com:8080 och se din lokala server

# Fjärrvidarebefordran exponerar en lokal port till användare på fjärrservern
# Användbart för:
# - Utveckling och testning
# - Temporär exponering av lokala tjänster
# - Debugging av fjärrapplikationer som behöver nå lokala resurser
```

**Notera**: Fjärrvidarebefordran kräver ofta `GatewayPorts yes` i sshd_config på servern för att exponera porten externt (inte bara localhost).

### SOCKS-proxy (-D-flaggan)

Skapa en dynamisk SOCKS-proxy via SSH.

```bash
# Skapa SOCKS-proxy på lokal port 1080
ssh -D 1080 user@server.com

# Nu kan du konfigurera applikationer att använda SOCKS-proxyn
# Exempel: webbläsare, curl, etc.

# Med curl:
curl --socks5 127.0.0.1:1080 http://example.com

# I bakgrunden:
ssh -f -N -D 1080 user@server.com
```

**Användning**:
- Bypassa brandväggar/restriktioner
- Kryptera all trafik via SSH-tunnel
- Användbar för säker surfning på osäkra nätverk

**Skillnad från portvidarebefordran**: SOCKS-proxy är dynamisk - den kan hantera flera destinationer, medan portvidarebefordran är statisk (en specifik destination).

### Tunnling med bakgrundsprocess

```bash
# Exekvera tunnel i bakgrunden
ssh -f -N -L 8080:localhost:80 user@server.com
# -f = bakgrund
# -N = inget fjärrkommando

# Stäng tunnel
ps aux | grep ssh
kill PID
```

## SSH Config: Förenkla anslutningar

Skapa ~/.ssh/config för att förenkla SSH-användning:

```bash
# ~/.ssh/config
Host myserver
    HostName server.com
    User myuser
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
    LocalForward 8080 localhost:80

Host production
    HostName prod.example.com
    User deploy
    IdentityFile ~/.ssh/prod_key
    ProxyJump jump.example.com
```

Nu kan du ansluta enkelt:

```bash
# Istället för: ssh -p 2222 -i ~/.ssh/id_ed25519 myuser@server.com
ssh myserver

# Tunnel startas automatiskt om konfigurerad
```

## Praktiska säkerhetstips

### Rotera SSH-nycklar regelbundet

```bash
# Generera ny nyckel
ssh-keygen -t ed25519 -f ~/.ssh/new_key

# Distribuera ny nyckel
ssh-copy-id -i ~/.ssh/new_key.pub user@server.com

# Testa att det fungerar
ssh -i ~/.ssh/new_key user@server.com

# Radera gamla nyckeln från server
ssh user@server.com
nano ~/.ssh/authorized_keys
# Radera gamla nyckeln
```

### Begränsa SSH-åtkomst

```bash
# I /etc/ssh/sshd_config
AllowUsers user1 user2        # Bara dessa användare
AllowGroups sshusers          # Bara denna grupp
DenyUsers baduser             # Blockera specifik användare
```

### Använd fail2ban för att skydda mot brute force

```bash
# Installera fail2ban
sudo apt install fail2ban

# Konfigurera för SSH
sudo nano /etc/fail2ban/jail.local
# [sshd]
# enabled = true
# maxretry = 3
# bantime = 3600
```

## scp - Säker kopiering

scp kopierar filer via SSH (säkert).

```bash
# Kopiera fil från lokal till fjärr
scp file.txt user@server.com:/path/to/destination/

# Kopiera fil från fjärr till lokal
scp user@server.com:/path/to/file.txt .

# Kopiera katalog rekursivt
scp -r folder/ user@server.com:/path/to/destination/

# Med specifik port
scp -P 2222 file.txt user@server.com:/path/

# Med specifik nyckel
scp -i ~/.ssh/my_key file.txt user@server.com:/path/

# Visa framsteg
scp -v file.txt user@server.com:/path/
```

**Användning**: Säker filöverföring via SSH, alternativ till FTP.

**Skillnad från rsync**: scp är enklare men rsync är mer effektivt för stora kataloger (kopierar bara ändringar).

## Viktiga lärdomar

- **SSH-nyckelpar**: Privat nyckel (hemlig) + Publik nyckel (delas)
- **Lösenfras**: Om den tappas bort kan nyckeln inte återställas - skapa ny nyckel
- **known_hosts**: Sparar serverfingeravtryck för att förhindra man-in-the-middle-attacker
- **ssh-copy-id**: Enklaste sättet att distribuera publik nyckel
- **SSH Agent**: Håller nycklar i minnet, slipp skriva lösenfras
- **ssh-add -l**: Lista nycklar i agenten
- **Agent Forwarding**: Använd lokal agent via hoppserver (ForwardAgent yes)
- **Säkerhet**: Inaktivera lösenordsinloggning när nycklar fungerar
- **MaxAuthTries**: Begränsa antal inloggningsförsök per anslutning
- **Lokal vidarebefordran**: `-L` = skicka lokal trafik till fjärr
- **Fjärrvidarebefordran**: `-R` = skicka fjärrtrafik till lokal (exponera lokal port)
- **SOCKS-proxy**: `-D` = skapa dynamisk proxy för all trafik
- **scp**: Säker filöverföring via SSH
- **SSH Config**: Förenkla anslutningar med ~/.ssh/config

"""
}
