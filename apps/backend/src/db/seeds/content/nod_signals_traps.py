"""
NOD 1.11: Signals, Traps & Job Control
======================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

SIGNALS_TRAPS_NODE = {
    "title": "Signals, Traps & Job Control",
    "slug": "signals-traps-jobcontrol",
    "description": "Linux-signaler, trap för cleanup, och job control (bg/fg/jobs).",
    "difficulty": "hard",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "order_index": 10,
    "content": r"""# Signals, Traps & Job Control

> **TL;DR:** Signaler är meddelanden till processer. `trap 'cleanup' EXIT` kör cleanup när skriptet avslutas. `Ctrl+Z` pausar, `bg` kör i bakgrunden, `fg` tar tillbaka.

---

## 📖 TEORI: Signaler

Signaler är **meddelanden som skickas till processer** för att informera om händelser.

### Viktiga signaler (LÄRA SIG DESSA!)

| Signal | Nummer | Beskrivning | Kan fångas? |
|--------|--------|-------------|-------------|
| `SIGHUP` | 1 | Hangup (terminal stängs) | ✅ Ja |
| `SIGINT` | 2 | Interrupt (Ctrl+C) | ✅ Ja |
| `SIGQUIT` | 3 | Quit (Ctrl+\\) | ✅ Ja |
| `SIGKILL` | 9 | Kill (tvingad) | ❌ NEJ! |
| `SIGTERM` | 15 | Terminate (snäll) | ✅ Ja |
| `SIGSTOP` | 19 | Stop (pausa) | ❌ NEJ! |
| `SIGCONT` | 18 | Continue (återuppta) | ✅ Ja |
| `SIGUSR1` | 10 | User-defined 1 | ✅ Ja |
| `SIGUSR2` | 12 | User-defined 2 | ✅ Ja |

### Skicka signaler med kill

```bash
# Skicka SIGTERM (default)
kill PID

# Skicka specifik signal
kill -SIGTERM PID
kill -15 PID
kill -TERM PID

# Tvinga avslut (kan ej fångas!)
kill -9 PID
kill -SIGKILL PID

# Lista alla signaler
kill -l
```

### Skicka signal till process med namn

```bash
# Avsluta alla firefox-processer
pkill firefox

# Skicka SIGHUP till nginx (reload config)
pkill -HUP nginx

# Avsluta process som matchar mönster
pkill -f "python script.py"
```

### killall - Avsluta med namn

```bash
killall firefox     # SIGTERM till alla firefox
killall -9 firefox  # SIGKILL till alla firefox
```

---

## 📖 SIGINT vs SIGTERM vs SIGKILL

| Signal | Källa | Fångas? | Användning |
|--------|-------|---------|------------|
| `SIGINT` | Ctrl+C | Ja | Användaren vill avbryta |
| `SIGTERM` | kill, systemd | Ja | Snäll shutdown-förfrågan |
| `SIGKILL` | kill -9 | **NEJ** | Sista utvägen, tvångsavslut |

### Best practice för processhantering

```bash
# 1. Försök med SIGTERM först
kill PID
sleep 2

# 2. Om fortfarande kör, SIGKILL
kill -0 PID 2>/dev/null && kill -9 PID
```

---

## 📖 trap - Fånga signaler

`trap` låter dig **fånga signaler** och köra egen kod.

### Syntax

```bash
trap 'kommandon' SIGNAL [SIGNAL...]
```

### Grundläggande exempel

```bash
#!/usr/bin/env bash

# Fånga Ctrl+C
trap 'echo "Du tryckte Ctrl+C!"' SIGINT

echo "Tryck Ctrl+C..."
while true; do
    sleep 1
done
```

### Fånga EXIT - VIKTIGAST!

`EXIT` är en speciell pseudo-signal som **alltid körs när skriptet avslutas**:

```bash
#!/usr/bin/env bash

cleanup() {
    echo "Städar upp..."
    rm -f /tmp/mytempfile.$$
}

trap cleanup EXIT

# Skapa temp-fil
echo "data" > /tmp/mytempfile.$$

# Oavsett hur skriptet avslutas körs cleanup!
# - Normal avslut
# - Ctrl+C
# - error med set -e
# - exit kommando
```

### Vanliga trap-signaler

```bash
# EXIT - När skriptet avslutas (oavsett hur)
trap 'cleanup' EXIT

# SIGINT - Ctrl+C
trap 'echo "Avbruten"' SIGINT

# SIGTERM - kill signal
trap 'echo "Terminerad"' SIGTERM

# ERR - När ett kommando misslyckas (med set -e)
trap 'echo "Fel på rad $LINENO"' ERR

# DEBUG - Innan varje kommando
trap 'echo "Kör: $BASH_COMMAND"' DEBUG
```

### Kombinera flera signaler

```bash
trap 'cleanup' EXIT SIGINT SIGTERM
```

### Ta bort trap

```bash
# Ta bort trap för SIGINT
trap - SIGINT

# Återställ default-beteende
trap '' SIGINT    # Ignorera SIGINT
trap - SIGINT     # Återställ
```

---

## 📖 Praktiska trap-mönster

### Mönster 1: Tempfil-hantering

```bash
#!/usr/bin/env bash
set -euo pipefail

TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT

# Använd tempfilen
echo "data" > "$TMPFILE"
# ...
# Filen rensas automatiskt!
```

### Mönster 2: Lås-fil (prevent concurrent runs)

```bash
#!/usr/bin/env bash

LOCKFILE="/var/run/myscript.lock"

cleanup() {
    rm -f "$LOCKFILE"
}

# Kolla om redan kör
if [[ -f "$LOCKFILE" ]]; then
    echo "Skriptet körs redan!"
    exit 1
fi

# Skapa lås och sätt cleanup
echo $$ > "$LOCKFILE"
trap cleanup EXIT

# ... resten av skriptet ...
```

### Mönster 3: Graceful shutdown

```bash
#!/usr/bin/env bash

RUNNING=true

shutdown() {
    echo "Avslutar gracefully..."
    RUNNING=false
}

trap shutdown SIGTERM SIGINT

while $RUNNING; do
    echo "Arbetar..."
    sleep 1
done

echo "Avslutad!"
```

### Mönster 4: Logga avslut

```bash
#!/usr/bin/env bash

on_exit() {
    local exit_code=$?
    if [[ $exit_code -eq 0 ]]; then
        echo "Skript avslutades normalt"
    else
        echo "Skript misslyckades med kod: $exit_code"
    fi
}

trap on_exit EXIT
```

---

## 📖 Job Control

Job control låter dig hantera **bakgrundsprocesser**.

### Starta i bakgrunden

```bash
# & i slutet = kör i bakgrunden
./long_script.sh &

# Spara PID
./long_script.sh &
PID=$!
echo "Startade process med PID: $PID"
```

### Pausa och återuppta

```bash
# Ctrl+Z = pausa aktuell process (SIGSTOP)
# Resulterar i: [1]+  Stopped    ./script.sh

# bg = fortsätt i bakgrunden
bg

# fg = ta tillbaka till förgrunden
fg

# fg/bg med jobbnummer
fg %1
bg %2
```

### jobs - Lista bakgrundsjobb

```bash
$ jobs
[1]   Running    ./download.sh &
[2]-  Stopped    vim file.txt
[3]+  Running    ./server.sh &
```

| Symbol | Betydelse |
|--------|-----------|
| `+` | Aktuellt jobb (fg/bg utan nummer) |
| `-` | Föregående jobb |

### Referera till jobb

```bash
fg %1        # Jobb nummer 1
fg %+        # Aktuellt jobb
fg %-        # Föregående jobb
fg %vim      # Jobb som börjar med "vim"
fg %?server  # Jobb som innehåller "server"
```

### wait - Vänta på bakgrundsprocess

```bash
#!/usr/bin/env bash

# Starta flera bakgrundsjobb
./job1.sh &
pid1=$!
./job2.sh &
pid2=$!
./job3.sh &
pid3=$!

# Vänta på alla
wait $pid1 $pid2 $pid3
echo "Alla jobb klara!"

# Eller vänta på alla bakgrundsjobb
wait
```

### nohup - Överlev logout

```bash
# nohup ignorerar SIGHUP (terminal stängs)
nohup ./long_running.sh &

# Output går till nohup.out
nohup ./script.sh > output.log 2>&1 &
```

### disown - Koppla loss från shell

```bash
# Starta i bakgrunden
./server.sh &

# Koppla loss (skriptet överlever om du stänger terminalen)
disown

# Eller direkt
./server.sh &
disown %1
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Robust skript med cleanup

```bash
#!/usr/bin/env bash
set -euo pipefail

# Variabler för cleanup
TMPDIR=""
LOCKFILE=""

cleanup() {
    local exit_code=$?

    # Ta bort tempkatalog
    [[ -d "$TMPDIR" ]] && rm -rf "$TMPDIR"

    # Ta bort låsfil
    [[ -f "$LOCKFILE" ]] && rm -f "$LOCKFILE"

    exit $exit_code
}

trap cleanup EXIT

# Skapa resurser
TMPDIR=$(mktemp -d)
LOCKFILE="/tmp/myscript.lock"
echo $$ > "$LOCKFILE"

# ... skriptlogik ...
echo "Arbetar i $TMPDIR"
sleep 5
```

### Exempel 2: Parallella bakgrundsjobb

```bash
#!/usr/bin/env bash

servers=(
    "server1.example.com"
    "server2.example.com"
    "server3.example.com"
)

pids=()

# Starta backup för varje server parallellt
for server in "${servers[@]}"; do
    echo "Startar backup för $server..."
    ssh "$server" "tar czf /backup/data.tar.gz /data" &
    pids+=($!)
done

# Vänta på alla och kolla status
failed=0
for pid in "${pids[@]}"; do
    if ! wait $pid; then
        (( failed++ ))
    fi
done

echo "Klart! $failed misslyckades."
```

### Exempel 3: Service-liknande skript

```bash
#!/usr/bin/env bash

PIDFILE="/var/run/myservice.pid"
RUNNING=true

start() {
    if [[ -f "$PIDFILE" ]]; then
        echo "Already running!"
        exit 1
    fi

    echo $$ > "$PIDFILE"
    trap 'stop' SIGTERM SIGINT
    trap 'rm -f "$PIDFILE"' EXIT

    echo "Service started (PID: $$)"

    while $RUNNING; do
        # Gör arbete här
        sleep 10
    done
}

stop() {
    echo "Stopping..."
    RUNNING=false
}

case "${1:-}" in
    start) start ;;
    stop)
        [[ -f "$PIDFILE" ]] && kill $(cat "$PIDFILE")
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
esac
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | SIGINT (signal 2) gör? | Interrupt - skickas vid Ctrl+C |
| 2 | SIGTERM (signal 15) gör? | Terminate - snäll shutdown-förfrågan |
| 3 | SIGKILL (signal 9) gör? | Tvångsavslut - kan EJ fångas! |
| 4 | trap 'cmd' EXIT gör? | Kör cmd när skriptet avslutas |
| 5 | Ctrl+Z gör? | Pausar process (SIGSTOP) |
| 6 | bg gör? | Fortsätter pausad process i bakgrunden |
| 7 | fg gör? | Tar bakgrundsprocess till förgrunden |
| 8 | & i slutet gör? | Kör kommando i bakgrunden |
| 9 | $! innehåller? | PID för senast bakgrundsprocess |
| 10 | wait gör? | Väntar på bakgrundsprocesser |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vilken signal skickas av Ctrl+C?**
- A) SIGTERM
- B) SIGINT ✅
- C) SIGKILL
- D) SIGHUP

**2. Vilken signal kan INTE fångas?**
- A) SIGINT
- B) SIGTERM
- C) SIGKILL ✅
- D) SIGHUP

**3. Vad gör `trap 'rm -f /tmp/file' EXIT`?**
- A) Tar bort filen direkt
- B) Tar bort filen när skriptet avslutas ✅
- C) Ignorerar EXIT-signalen
- D) Skapar filen

**4. Hur startar du en process i bakgrunden?**
- A) bg kommando
- B) kommando &bg
- C) kommando & ✅
- D) background kommando

**5. Vad gör Ctrl+Z?**
- A) Avslutar processen
- B) Pausar processen ✅
- C) Kör processen i bakgrunden
- D) Skickar SIGKILL

**6. Hur får du PID för senast startade bakgrundsprocess?**
- A) $PID
- B) $!  ✅
- C) $$
- D) $?

**7. Vad är skillnaden mellan SIGTERM och SIGKILL?**
- A) Ingen skillnad
- B) SIGTERM kan fångas, SIGKILL kan inte ✅
- C) SIGKILL är snällare
- D) SIGTERM fungerar bara på root

**8. Hur väntar du på en bakgrundsprocess?**
- A) sleep PID
- B) wait PID ✅
- C) pause PID
- D) hold PID

**9. Vad gör kommandot `fg %2`?**
- A) Startar jobb 2
- B) Pausar jobb 2
- C) Tar jobb 2 till förgrunden ✅
- D) Avslutar jobb 2

**10. Hur skickar du SIGTERM till process 1234?**
- A) signal 1234
- B) kill 1234 ✅
- C) term 1234
- D) stop 1234

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Testa trap
```bash
#!/usr/bin/env bash
trap 'echo "Ctrl+C fångad!"' SIGINT
echo "Tryck Ctrl+C (eller vänta 10 sek)..."
sleep 10
echo "Klar!"
```

### Övning 2: Cleanup med trap
Skriv ett skript som:
1. Skapar en tempfil med `mktemp`
2. Använder `trap ... EXIT` för att ta bort filen
3. Testa att filen försvinner även vid Ctrl+C

### Övning 3: Bakgrundsjobb
```bash
# 1. Starta sleep 100 i bakgrunden
sleep 100 &

# 2. Lista jobb
jobs

# 3. Ta processen till förgrunden
fg %1

# 4. Pausa med Ctrl+Z

# 5. Skicka tillbaka till bakgrunden
bg

# 6. Avsluta
kill %1
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| Glömma trap EXIT | Resurser läcker | Alltid trap cleanup EXIT |
| kill -9 som första val | Ingen graceful shutdown | Prova SIGTERM först |
| Glömma & | Processen blockerar | kommando & för bakgrund |
| Trap i subshell | Fungerar inte utanför | Definiera trap i main shell |
| Använda SIGKILL på zombie | Funkar inte | Zombies är redan döda |

---

## 📝 SAMMANFATTNING

```bash
# SIGNALER
SIGINT (2)    # Ctrl+C - avbryt
SIGTERM (15)  # Snäll shutdown
SIGKILL (9)   # Tvångsavslut (kan ej fångas!)
SIGHUP (1)    # Terminal stängs

# SKICKA SIGNAL
kill PID           # SIGTERM
kill -9 PID        # SIGKILL
kill -HUP PID      # SIGHUP
pkill namn         # Kill by name

# TRAP
trap 'cleanup' EXIT           # Vid avslut
trap 'handler' SIGINT SIGTERM # Vid signal
trap - SIGINT                 # Ta bort trap

# JOB CONTROL
kommando &     # Bakgrund
$!             # Senaste bakgrunds-PID
jobs           # Lista jobb
Ctrl+Z         # Pausa
bg             # Till bakgrund
fg             # Till förgrund
wait           # Vänta på bakgrundsjobb

# CLEANUP-MÖNSTER
#!/usr/bin/env bash
set -euo pipefail
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
```

"""
}

