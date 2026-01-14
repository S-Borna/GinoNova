"""
NOD: Processhantering och systemprestanda
=========================================
Övervaka och felsöka system genom processhantering och prestandaanalys
"""

PROCESSHANTERING_NODE = {
    "title": "Processhantering och systemprestanda",
    "slug": "processhantering",
    "description": "Övervaka och felsöka system genom processhantering och prestandaanalys",
    "difficulty": "medium",
    "estimated_minutes": 60,
    "xp_reward": 120,
    "order_index": 3,
    "content": r"""# Processhantering och systemprestanda

Fokus: Övervakning och felsökning av långsamma system

## Processlivscykel: Tillstånd

Processer kan befinna sig i olika tillstånd:

- **Running (R)**: Exekveras aktivt eller väntar på CPU-tid
- **Sleeping (S)**: Inväntar händelse (I/O, signal, etc.)
- **Zombie (Z)**: Processen är avslutad men väntar på att föräldern ska läsa exit-status
- **Stopped (T)**: Processen är pausad (t.ex. med Ctrl+Z)

```bash
# Visa processtillstånd
ps aux | head
# STAT-kolumnen visar tillstånd:
# R = Running
# S = Sleeping
# Z = Zombie
# T = Stopped
# D = Uninterruptible sleep (inväntar I/O)
```

### Processtillstånd i detalj

```bash
# Exekverande processer
ps aux | grep " R "

# Sovande processer
ps aux | grep " S "

# Zombie-processer (bör rensas)
ps aux | grep " Z "
```

## Load Average: Tolka de tre siffrorna

Load average visar systemets belastning över tid:

```
load average: 1.25, 0.85, 0.60
             ↑     ↑     ↑
             1min  5min  15min
```

**Tolkning**: Om du har 4 CPU-kärnor:
- 1.25: Systemet är 31% belastat (1.25/4 = 0.31)
- 4.0: Systemet är 100% belastat (alla kärnor utnyttjas)
- 8.0: Systemet är 200% belastat (dubbelt så många processer som kärnor)

```bash
# Visa load average
uptime
# 14:30:00 up 10 days, load average: 1.25, 0.85, 0.60

# Alternativt
cat /proc/loadavg
# 1.25 0.85 0.60 2/500 12345

# Räkna CPU-kärnor
nproc
# eller
grep -c processor /proc/cpuinfo
```

**Princip**: Om load average > antal CPU-kärnor är systemet överbelastat.

## Signaler: SIGTERM vs SIGKILL

### SIGTERM (15) - Kontrollerad avslutning

Processen får möjlighet att stänga ner sig själv på ett kontrollerat sätt.

```bash
# Skicka SIGTERM
kill PID
kill -15 PID
kill -TERM PID

# Processen kan:
# - Spara data
# - Stänga filer
# - Frigöra resurser
```

### SIGKILL (9) - Omedelbar terminering

Processen termineras omedelbart, ingen möjlighet att stänga ner sig själv.

```bash
# Skicka SIGKILL (sista utvägen!)
kill -9 PID
kill -KILL PID

# Processen kan INTE:
# - Spara data
# - Stänga filer ordentligt
# - Frigöra resurser
```

**Best practice**: Försök alltid SIGTERM först, använd SIGKILL endast om processen inte svarar.

```bash
# Kontrollerad avslutning
kill PID
sleep 5
# Om processen fortfarande exekveras
kill -9 PID
```

### Andra viktiga signaler

```bash
SIGHUP (1)   # Hang up - används ofta för att ladda om konfiguration
SIGINT (2)   # Interrupt - samma som Ctrl+C
SIGSTOP (19) # Pausa processen (kan återupptas)
SIGCONT (18) # Återuppta pausad process
```

```bash
# Skicka signal till processgrupp
kill -TERM -PID  # Negativt PID = hela gruppen

# Skicka signal till alla processer med samma namn
pkill -TERM nginx
killall -TERM nginx

# pgrep - Hitta PID för processer med namn
pgrep nginx
# 1234
# 1235

# Med mer information
pgrep -l nginx
# 1234 nginx
# 1235 nginx-worker
```

## Jobbkontroll: jobs, fg, bg, Ctrl+Z

### Pausa processer med Ctrl+Z

När du exekverar ett program i terminalen kan du pausa det:

```bash
# Exekvera ett program
sleep 100

# Tryck Ctrl+Z - processen pausas (SIGSTOP)
# [1]+  Stopped                 sleep 100
```

### jobs - Lista bakgrundsjobb

```bash
# Visa alla jobb i denna session
jobs
# [1]+  Stopped                 sleep 100
# [2]-  Running                 long_task &

# Med PID
jobs -l
# [1]+ 12345 Stopped                 sleep 100
```

### bg - Exekvera i bakgrunden

```bash
# Återuppta pausat jobb i bakgrunden
bg %1
# eller endast
bg

# Starta process direkt i bakgrunden
long_task &
```

### fg - Ta tillbaka till förgrunden

```bash
# Ta tillbaka jobb 1 till förgrunden
fg %1
# eller endast
fg

# Nu kan du interagera med processen igen
```

### nohup - Exekvera processer som överlever utloggning

```bash
# Exekvera process i bakgrunden som överlever utloggning
nohup long_task &

# Utdata sparas i nohup.out
# Processen fortsätter även om du loggar ut

# Med egen utdatafil
nohup long_task > output.log 2>&1 &
```

**Användning**: När du vill exekvera långvariga processer som ska fortsätta även om du stänger terminalen.

## Kontextväxling

Kontextväxling (Context Switching) är när CPU:n byter från att exekvera en process till att exekvera en annan.

### Hur det fungerar

1. CPU:n sparar tillståndet för den nuvarande processen (register, stack, etc.)
2. CPU:n laddar in tillståndet för nästa process
3. CPU:n fortsätter exekvera den nya processen

**Varför det händer**: För att ge intrycket av att flera processer exekveras samtidigt (multitasking).

```bash
# Visa kontextväxlingar
vmstat 1
# cs-kolumnen visar antal kontextväxlingar per sekund
```

**Prestanda**: För många kontextväxlingar kan påverka prestanda negativt eftersom det tar tid att spara/ladda processtillstånd.

## Resursanalys: Verktyg för övervakning

### top - Realtidsöversikt

```bash
top
# Tryck:
# M = Sortera efter minne
# P = Sortera efter CPU
# q = Avsluta
# k = Terminera process (ange PID)
```

### htop - Förbättrad top

```bash
htop
# Mer användarvänlig, färgkodad
# F5 = Trädvy
# F6 = Sortera
# F9 = Terminera
```

### free -m - Minnesanvändning

```bash
free -m
# Visar minne i MB
# -h = läsbart format
# -g = GB

free -h
#               total        used        free      shared  buff/cache   available
# Mem:           7.8Gi       2.1Gi       4.2Gi       123Mi       1.5Gi       5.4Gi
```

**Tolkning**:
- **used**: Använt minne
- **free**: Ledigt minne
- **buff/cache**: Används för cache (kan frigöras om nödvändigt)
- **available**: Verkligt tillgängligt minne

### df -h - Diskutrymme

```bash
df -h
# Visar diskutrymme för alla monteringspunkter
# -h = läsbart format
# -i = visa inodes istället

df -h /
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1        50G   30G   18G  63% /
```

### du -sh --max-depth=1 - Diskutrymme per katalog

```bash
# Visa storlek för kataloger på första nivån
du -sh --max-depth=1 /var
# 2.5G    /var/log
# 1.2G    /var/lib
# 500M    /var/www

# Hitta största kataloger
du -h /var | sort -rh | head -10
```

### iostat - Disk-I/O-analys

```bash
# Visa diskstatistik varje sekund
iostat -x 1

# Kolumner:
# %util - Procent av tiden disken var upptagen
# %iowait - Procent av tiden CPU väntade på I/O
# r/s, w/s - Läs/skriv per sekund
# rkB/s, wkB/s - Kilobyte läst/skrivet per sekund

# Om %util är nära 100% är disken en flaskhals
```

**%IOWAIT**: Hur mycket tid CPU:n är overksam medan den inväntar att diskoperationer (läsa/skriva) ska slutföras.

### iotop - Process-I/O-analys

```bash
# Visa vilka processer som använder mest I/O
sudo iotop

# Sortera efter I/O
# Tryck o för att ändra sortering
# Tryck p för att visa processer istället för trådar
```

**Användning**: Identifiera processer som läser/skriver mycket till disken (kan göra systemet långsamt).

## Throttling av processer

Throttling innebär att systemet medvetet begränsar en process resursanvändning (t.ex. CPU) för att skydda andra tjänster.

```bash
# Begränsa CPU-användning med cgroups
# (Docker använder detta automatiskt)

# Begränsa med nice/renice (lägre prioritet)
nice -n 19 cpu_intensive_task
renice 19 -p 1234
```

**Användning**: När en process konsumerar för mycket resurser och påverkar andra tjänster negativt.

## systemd och journalctl - Avancerad logghantering

### systemctl status

```bash
# Visa status för tjänst
systemctl status nginx

# Visa detaljerad information
systemctl show nginx

# Lista alla tjänster
systemctl list-units --type=service

# Lista endast aktiva tjänster
systemctl list-units --type=service --state=running
```

### journalctl - systemd-loggar

```bash
# Visa alla loggar
journalctl

# Visa loggar för specifik tjänst
journalctl -u nginx

# Följ loggar i realtid
journalctl -u nginx -f

# Visa senaste 100 raderna
journalctl -u nginx -n 100

# Visa loggar från idag
journalctl -u nginx --since today

# Visa loggar från specifik tid
journalctl -u nginx --since "2024-01-15 10:00:00"

# Sök i loggar
journalctl -u nginx | grep "error"

# Kombinera flera tjänster
journalctl -u nginx -u apache2

# Visa kärnloggar
journalctl -k

# Visa endast fel
journalctl -p err
```

### systemctl stop vs disable

```bash
# stop - Stoppar tjänsten nu
sudo systemctl stop nginx

# disable - Förhindrar att tjänsten startar automatiskt vid boot
sudo systemctl disable nginx

# Kombinera
sudo systemctl stop nginx
sudo systemctl disable nginx

# enable - Aktivera autostart
sudo systemctl enable nginx
sudo systemctl start nginx
```

## /proc/cpuinfo - CPU-information

```bash
# Visa detaljerad CPU-information
cat /proc/cpuinfo

# Viktiga fält:
# processor - CPU-kärnnummer
# model name - CPU-modell
# cpu MHz - CPU-hastighet
# cache size - Cache-storlek
# cpu cores - Antal kärnor per socket
# siblings - Antal logiska processorer

# Räkna CPU-kärnor
grep -c processor /proc/cpuinfo
# eller
nproc

# Visa CPU-modell
grep "model name" /proc/cpuinfo | head -1
```

## /proc/[PID]/ - Processspecifik information

Varje process har sin egen katalog under /proc/:

```bash
# Exempel: Process med PID 1234
ls /proc/1234/
# cmdline    - Kommandoraden
# cwd        - Nuvarande arbetskatalog (symbolisk länk)
# environ    - Miljövariabler
# exe        - Exekverbar fil (symbolisk länk)
# fd/        - Öppna filer (filbeskrivare)
# status     - Processstatus
# stat       - Processstatistik
# maps       - Minnesmappning
# limits     - Resursbegränsningar

# Visa kommandoraden
cat /proc/1234/cmdline

# Visa miljövariabler
cat /proc/1234/environ | tr '\0' '\n'

# Visa öppna filer
ls -l /proc/1234/fd/

# Visa processstatus
cat /proc/1234/status
# Name:   nginx
# State:  S (sleeping)
# Pid:    1234
# PPid:   1
# Uid:    33    33    33    33
# Gid:    33    33    33    33
# VmSize: 100000 kB
# VmRSS:  50000 kB
```

**Användning**: Debugga processer, se vilka filer de har öppna, kontrollera resursanvändning.

## vmstat - Virtuellt minnesstatistik

```bash
# Visa statistik varje sekund
vmstat 1

# Kolumner:
# r - Antal processer som inväntar CPU
# b - Antal processer i uninterruptible sleep
# swpd - Använt swap-minne
# free - Ledigt minne
# buff - Buffer-minne
# cache - Cache-minne
# si - Swap in (från disk till RAM)
# so - Swap out (från RAM till disk)
# cs - Kontextväxlingar per sekund
# us - User CPU-tid
# sy - System CPU-tid
# id - Idle CPU-tid
# wa - I/O wait-tid
```

**Användning**: Övervaka systemresurser över tid, identifiera flaskhalsar.

## Avbrott (Interrupts)

Avbrott (Interrupts) är signaler från hårdvara (t.ex. nätverkskort, tangentbord) till CPU:n att något behöver hanteras omedelbart.

```bash
# Visa avbrott per CPU
cat /proc/interrupts

# Visa avbrott per sekund
watch -n 1 'cat /proc/interrupts | head -20'
```

**Exempel**: När du trycker en tangent skickar tangentbordet ett avbrott till CPU:n, som sedan hanterar tangenttryckningen.

## sar - System Activity Reporter

```bash
# Installera (om inte redan installerat)
sudo apt install sysstat

# Visa CPU-statistik
sar -u 1 5  # Varje sekund, 5 gånger

# Visa minnesstatistik
sar -r 1 5

# Visa I/O-statistik
sar -b 1 5

# Visa historisk data (om sysstat exekveras)
sar -u  # CPU-användning idag
sar -r  # Minne idag
```

**Användning**: Samla historisk prestandadata för analys av trender och problem.

## CPU Steal Time

CPU Steal Time (%st) är relevant i virtuella miljöer (VM:ar). Det är den tid din virtuella CPU fick vänta på resurser från den fysiska värden eftersom andra VM:ar använde dem.

```bash
# Visa i top eller htop
top
# Leta efter kolumnen "st" (steal time)

# Om steal time är hög (>10%) betyder det att:
# - Värden är överbelastad
# - Du delar CPU med för många andra VM:ar
# - Överväg att flytta till en mindre belastad värd
```

## Minnesläckor (Memory Leaks)

Minnesläckor (Memory Leak) är när ett program allokerar minne men glömmer att frigöra det, vilket gör att minnet tar slut över tid.

### Identifiera minnesläckor

```bash
# Övervaka minnesanvändning över tid
watch -n 1 'ps aux --sort=-%mem | head -10'

# Om en process växer kontinuerligt i minne utan att frigöra,
# kan det vara en minnesläcka

# Använd verktyg som valgrind för att hitta läckor i kod
valgrind --leak-check=full ./program
```

**Symptom**: Systemet blir långsammare över tid, swap-användning ökar, OOM Killer aktiveras.

## IPC (Inter-Process Communication)

Processer behöver kommunicera med varandra:

### Pipes

Unidirektionell dataström mellan processer.

```bash
# Named pipe (FIFO)
mkfifo mypipe
echo "hello" > mypipe &
cat mypipe

# Anonymous pipe
ls -l | grep ".txt"
```

### Sockets

Bidirektionell kommunikation, kan vara över nätverk.

```bash
# Unix domain socket
ls -l /var/run/*.sock

# TCP socket
ss -tlnp  # Visa lyssnande TCP-sockets
```

### Signaler

Enkla meddelanden mellan processer (se ovan).

### Semaforer

Synkronisering mellan processer (delade resurser).

## Praktiska felsökningsscenarier

### Systemet är långsamt - var börjar jag?

```bash
# 1. Kontrollera load average
uptime

# 2. Kontrollera CPU-användning
top
# Leta efter processer med hög %CPU

# 3. Kontrollera minne
free -h
# Om minnet är fullt, kontrollera swap
swapon --show

# 4. Kontrollera I/O
iostat -x 1
# Leta efter hög %util (disk är flaskhals)
iotop  # Visa processer som använder I/O

# 5. Kontrollera nätverk
iftop
# eller
nethogs
```

### Hitta resurskrävande processer

```bash
# Topp 10 CPU-konsumenter
ps aux --sort=-%cpu | head -11

# Topp 10 minneskonsumenter
ps aux --sort=-%mem | head -11

# Processer som använder mycket I/O
iotop
```

### Terminera zombie-processer

```bash
# Hitta zombie-processer
ps aux | grep " Z "

# Zombies kan inte termineras direkt
# De försvinner när föräldern läser exit-status
# Om föräldern är död blir init förälder och rensar dem
```

## Viktiga lärdomar

- **Processtillstånd**: Running, Sleeping, Zombie, Stopped
- **Load Average**: Jämför med antal CPU-kärnor för att förstå belastning
- **SIGTERM**: Kontrollerad avslutning (försök först)
- **SIGKILL**: Omedelbar terminering (sista utvägen)
- **Jobbkontroll**: Ctrl+Z pausar, `bg` exekverar i bakgrunden, `fg` tar tillbaka
- **nohup**: Exekvera processer som överlever utloggning
- **Kontextväxling**: CPU:n byter mellan processer för multitasking
- **%IOWAIT**: CPU-tid som spenderas väntande på I/O-operationer
- **iostat/iotop**: Analysera disk-I/O och identifiera flaskhalsar
- **Throttling**: Begränsa processresurser för att skydda andra tjänster
- **/proc/cpuinfo**: Detaljerad CPU-information
- **/proc/[PID]/**: Processspecifik information (cmdline, environ, fd, etc.)
- **vmstat**: Övervaka systemresurser över tid
- **Avbrott**: Hårdvarusignaler till CPU:n
- **sar**: Samla historisk prestandadata
- **CPU Steal Time**: Relevant i VM:ar - tid CPU väntade på värdresurser
- **Minnesläckor**: Program som glömmer att frigöra minne
- **journalctl**: Avancerad logghantering för systemd-tjänster
- **pgrep**: Hitta PID för processer med namn
- **Resursverktyg**: top, htop, free, df, du för olika typer av analys
- **IPC**: Pipes, Sockets, Signaler, Semaforer för processkommunikation

"""
}
