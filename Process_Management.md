# Process Management & System Performance

Fokus: Övervakning och felsökning av sega system

## Process Lifecycle: States

Processer kan vara i olika tillstånd:

- **Running (R)**: Körs aktivt eller väntar på CPU
- **Sleeping (S)**: Väntar på en händelse (I/O, signal, etc.)
- **Zombie (Z)**: Processen är död men väntar på att föräldern läser exit-status
- **Stopped (T)**: Processen är stoppad (t.ex. med Ctrl+Z)

```bash
# Visa process states
ps aux | head
# STAT kolumnen visar tillstånd:
# R = Running
# S = Sleeping
# Z = Zombie
# T = Stopped
# D = Uninterruptible sleep (väntar på I/O)
```

### Process States i detalj

```bash
# Running processer
ps aux | grep " R "

# Sleeping processer
ps aux | grep " S "

# Zombie processer (bör rensas)
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
- 4.0: Systemet är 100% belastat (alla kärnor används)
- 8.0: Systemet är 200% belastat (dubbelt så många processer som kärnor)

```bash
# Visa load average
uptime
# 14:30:00 up 10 days, load average: 1.25, 0.85, 0.60

# Eller
cat /proc/loadavg
# 1.25 0.85 0.60 2/500 12345

# Räkna CPU-kärnor
nproc
# eller
grep -c processor /proc/cpuinfo
```

**Regel**: Om load average > antal CPU-kärnor, är systemet överbelastat.

## Signals: SIGTERM vs SIGKILL

### SIGTERM (15) - Snygg avstängning

Processen får möjlighet att stänga av sig själv på ett kontrollerat sätt.

```bash
# Skicka SIGTERM
kill PID
kill -15 PID
kill -TERM PID

# Processen kan:
# - Spara data
# - Stänga filer
# - Rensa resurser
```

### SIGKILL (9) - Omedelbar död

Processen dödas omedelbart, ingen chans att stänga av sig själv.

```bash
# Skicka SIGKILL (sista utvägen!)
kill -9 PID
kill -KILL PID

# Processen kan INTE:
# - Spara data
# - Stänga filer ordentligt
# - Rensa resurser
```

**Best practice**: Försök alltid SIGTERM först, använd SIGKILL bara om processen inte svarar.

```bash
# Snygg avstängning
kill PID
sleep 5
# Om processen fortfarande körs
kill -9 PID
```

### Andra viktiga signals

```bash
SIGHUP (1)   # Hang up - ofta används för att ladda om konfiguration
SIGINT (2)   # Interrupt - samma som Ctrl+C
SIGSTOP (19) # Stoppa processen (kan återupptas)
SIGCONT (18) # Återuppta stoppad process
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

## Job Control: jobs, fg, bg, Ctrl+Z

### Pausa processer med Ctrl+Z

När du kör ett program i terminalen kan du pausa det:

```bash
# Kör ett program
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

### bg - Kör i bakgrunden

```bash
# Starta om ett pausat jobb i bakgrunden
bg %1
# eller bara
bg

# Starta process direkt i bakgrunden
long_task &
```

### fg - Ta tillbaka till förgrunden

```bash
# Ta tillbaka jobb 1 till förgrunden
fg %1
# eller bara
fg

# Nu kan du interagera med processen igen
```

### nohup - Kör processer som överlever logout

```bash
# Kör process i bakgrunden som överlever logout
nohup long_task &

# Output sparas i nohup.out
# Processen fortsätter även om du loggar ut

# Med egen output-fil
nohup long_task > output.log 2>&1 &
```

**Användning**: När du vill köra långvariga processer som ska fortsätta även om du stänger terminalen.

## Context Switching

Context Switching är när CPU:n byter från att köra en process till att köra en annan.

### Hur det fungerar

1. CPU:n sparar tillståndet för den nuvarande processen (register, stack, etc.)
2. CPU:n laddar in tillståndet för nästa process
3. CPU:n fortsätter köra den nya processen

**Varför det händer**: För att ge intrycket av att flera processer körs samtidigt (multitasking).

```bash
# Visa context switches
vmstat 1
# cs kolumnen visar antal context switches per sekund
```

**Prestanda**: För många context switches kan påverka prestanda negativt eftersom det tar tid att spara/ladda process-tillstånd.

## Resource Analysis: Verktyg för övervakning

### top - Realtidsöversikt

```bash
top
# Tryck:
# M = Sortera efter minne
# P = Sortera efter CPU
# q = Quit
# k = Kill process (ange PID)
```

### htop - Förbättrad top

```bash
htop
# Mer användarvänlig, färgkodad
# F5 = Tree view
# F6 = Sortera
# F9 = Kill
```

### free -m - Minnesanvändning

```bash
free -m
# Visar minne i MB
# -h = human readable
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
# Visar diskutrymme för alla mount points
# -h = human readable
# -i = visa inodes istället

df -h /
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1        50G   30G   18G  63% /
```

### du -sh --max-depth=1 - Diskusage per katalog

```bash
# Visa storlek för kataloger på första nivån
du -sh --max-depth=1 /var
# 2.5G    /var/log
# 1.2G    /var/lib
# 500M    /var/www

# Hitta största kataloger
du -h /var | sort -rh | head -10
```

### iostat - Disk-I/O analys

```bash
# Visa diskstatistik varje sekund
iostat -x 1

# Kolumner:
# %util - Procent av tiden disken var upptagen
# %iowait - Procent av tiden CPU väntade på I/O
# r/s, w/s - Läs/skriv per sekund
# rkB/s, wkB/s - Kilobytes läst/skrivet per sekund

# Om %util är nära 100%, är disken en flaskhals
```

**%IOWAIT**: Hur mycket tid CPU:n är overksam medan den väntar på att disk-operationer (läsa/skriva) ska bli klara.

### iotop - Process-I/O analys

```bash
# Visa vilka processer som använder mest I/O
sudo iotop

# Sortera efter I/O
# Tryck o för att ändra sortering
# Tryck p för att visa processer istället för trådar
```

**Användning**: Hitta processer som läser/skriver mycket till disken (kan göra systemet segt).

## Throttling av processer

Throttling innebär att systemet medvetet begränsar en process resursanvändning (t.ex. CPU) för att skydda andra tjänster.

```bash
# Begränsa CPU-användning med cgroups
# (Docker använder detta automatiskt)

# Begränsa med nice/renice (lägre prioritet)
nice -n 19 cpu_intensive_task
renice 19 -p 1234
```

**Användning**: När en process tar för mycket resurser och påverkar andra tjänster negativt.

## systemd och journalctl - Avancerad logghantering

### systemctl status

```bash
# Visa status för en tjänst
systemctl status nginx

# Visa detaljerad information
systemctl show nginx

# Lista alla tjänster
systemctl list-units --type=service

# Lista endast aktiva tjänster
systemctl list-units --type=service --state=running
```

### journalctl - systemd loggar

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

# Visa kernel-loggar
journalctl -k

# Visa endast fel
journalctl -p err
```

### systemctl stop vs disable

```bash
# stop - Stoppar tjänsten nu
sudo systemctl stop nginx

# disable - Gör att tjänsten inte startar automatiskt vid boot
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
# processor - CPU-kärna nummer
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

## /proc/[PID]/ - Process-specifik information

Varje process har sin egen katalog under /proc/:

```bash
# Exempel: Process med PID 1234
ls /proc/1234/
# cmdline    - Kommandoraden
# cwd        - Nuvarande arbetskatalog (symbolic link)
# environ    - Miljövariabler
# exe        - Exekverbar fil (symbolic link)
# fd/        - Öppna filer (file descriptors)
# status     - Process status
# stat       - Process statistik
# maps       - Minnesmappning
# limits     - Resursbegränsningar

# Visa kommandoraden
cat /proc/1234/cmdline

# Visa miljövariabler
cat /proc/1234/environ | tr '\0' '\n'

# Visa öppna filer
ls -l /proc/1234/fd/

# Visa process status
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
# r - Antal processer som väntar på CPU
# b - Antal processer i uninterruptible sleep
# swpd - Använt swap-minne
# free - Ledigt minne
# buff - Buffer-minne
# cache - Cache-minne
# si - Swap in (från disk till RAM)
# so - Swap out (från RAM till disk)
# cs - Context switches per sekund
# us - User CPU-tid
# sy - System CPU-tid
# id - Idle CPU-tid
# wa - I/O wait-tid
```

**Användning**: Övervaka systemresurser över tid, identifiera flaskhalsar.

## Interrupts

Interrupts (avbrott) är signaler från hårdvara (t.ex. nätverkskort, tangentbord) till CPU:n att något behöver hanteras omedelbat.

```bash
# Visa interrupts per CPU
cat /proc/interrupts

# Visa interrupts per sekund
watch -n 1 'cat /proc/interrupts | head -20'
```

**Exempel**: När du trycker en tangent skickar tangentbordet en interrupt till CPU:n, som sedan hanterar tangenttryckningen.

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

# Visa historisk data (om sysstat körs)
sar -u  # CPU-användning idag
sar -r  # Minne idag
```

**Användning**: Samla in historisk prestandadata för analys av trender och problem.

## CPU Steal Time

CPU Steal Time (%st) är relevant i virtuella miljöer (VM:ar). Det är den tid din virtuella CPU fick vänta på resurser från den fysiska hosten eftersom andra VM:ar använde dem.

```bash
# Visa i top eller htop
top
# Leta efter kolumnen "st" (steal time)

# Om steal time är hög (>10%), betyder det att:
# - Hosten är överbelastad
# - Du delar CPU med för många andra VM:ar
# - Överväg att flytta till en mindre belastad host
```

## Memory Leaks

Memory Leak (minnesläcka) är när ett program bokar minne men glömmer att släppa tillbaka det, vilket gör att minnet tar slut över tid.

### Identifiera memory leaks

```bash
# Övervaka minnesanvändning över tid
watch -n 1 'ps aux --sort=-%mem | head -10'

# Om en process växer kontinuerligt i minne utan att släppa,
# kan det vara en memory leak

# Använd verktyg som valgrind för att hitta leaks i kod
valgrind --leak-check=full ./program
```

**Symptom**: Systemet blir segare över tid, swap-användning ökar, OOM Killer aktiveras.

## IPC (Inter-Process Communication)

Processer behöver kommunicera med varandra:

### Pipes

Enkelriktad dataström mellan processer.

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
ss -tlnp  # Visa listening TCP sockets
```

### Signals

Enkla meddelanden mellan processer (se ovan).

### Semaphores

Synkronisering mellan processer (delade resurser).

## Praktiska felsökningsscenarier

### Systemet är segt - var börjar jag?

```bash
# 1. Kolla load average
uptime

# 2. Kolla CPU-användning
top
# Leta efter processer med hög %CPU

# 3. Kolla minne
free -h
# Om minne är fullt, kolla swap
swapon --show

# 4. Kolla I/O
iostat -x 1
# Leta efter hög %util (disk är flaskhals)
iotop  # Visa processer som använder I/O

# 5. Kolla nätverk
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

### Döda zombie-processer

```bash
# Hitta zombie-processer
ps aux | grep " Z "

# Zombies kan inte dödas direkt
# De försvinner när föräldern läser exit-status
# Om föräldern är död, blir init förälder och rensar dem
```

## Viktiga takeaways

- **Process States**: Running, Sleeping, Zombie, Stopped
- **Load Average**: Jämför med antal CPU-kärnor för att förstå belastning
- **SIGTERM**: Snygg avstängning (försök först)
- **SIGKILL**: Omedelbar död (sista utvägen)
- **Job Control**: Ctrl+Z pausar, `bg` kör i bakgrunden, `fg` tar tillbaka
- **nohup**: Kör processer som överlever logout
- **Context Switching**: CPU:n byter mellan processer för multitasking
- **%IOWAIT**: CPU-tid som spenderas väntande på I/O-operationer
- **iostat/iotop**: Analysera disk-I/O och identifiera flaskhalsar
- **Throttling**: Begränsa processresurser för att skydda andra tjänster
- **/proc/cpuinfo**: Detaljerad CPU-information
- **/proc/[PID]/**: Process-specifik information (cmdline, environ, fd, etc.)
- **vmstat**: Övervaka systemresurser över tid
- **Interrupts**: Hårdvarusignaler till CPU:n
- **sar**: Samla historisk prestandadata
- **CPU Steal Time**: Relevant i VM:ar - tid CPU väntade på host-resurser
- **Memory Leaks**: Program som glömmer att släppa minne
- **journalctl**: Avancerad logghantering för systemd-tjänster
- **pgrep**: Hitta PID för processer med namn
- **Resource Tools**: top, htop, free, df, du för olika typer av analys
- **IPC**: Pipes, Sockets, Signals, Semaphores för processkommunikation
