# Linux Mastery — 20 Individuella Prompts för Opus

Detta dokument innehåller 20 färdiga prompts som kan skickas direkt till Opus för att generera komplett innehåll för varje nod i Linux Mastery-modulen.

**Användning:**
1. Kopiera en prompt
2. Skicka till Opus
3. Verifiera output mot kvalitetschecklistan
4. Spara som `NOD_XX_titel.md`

---

## Prompt 1: Filesystem Hierarchy Standard (FHS)

**[REDAN GENERERAD - SE NOD_01_filesystem_hierarchy_standard.md]**

---

## Prompt 2: Mount Points och Device Files

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 2 av 20
- **Titel:** Mount Points och Device Files
- **Slug:** mount-points-device-files
- **Difficulty:** Lätt
- **Tid:** 40 minuter
- **XP:** 65
- **Föregående:** Filesystem Hierarchy Standard
- **Nästa:** File Permissions

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Vad mount points är och hur de fungerar
2. Device files i /dev (block vs character devices)
3. Kommandon: lsblk, mount, umount, findmnt
4. /etc/fstab - struktur och syntax
5. UUID vs device names - varför UUID är säkrare
6. Mounting USB-enheter och nätverksshares
7. Bind mounts och deras användning
8. Tmpfs och rambaserade filsystem

## Övningar
1. **Grundläggande:** Utforska mount points med lsblk, mount och findmnt
2. **Tillämpad:** Skapa en tmpfs och montera en ISO-fil
3. **Utmanande:** Konfigurera persistent mount i fstab med UUID och verifiera

## DevOps-kontext
- Docker volume mounts och bind mounts
- Kubernetes PersistentVolumes
- NFS-mounts för delad lagring i kluster
- Disk management i CI/CD runners

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard (mount, device, UUID)
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 3: File Permissions

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 3 av 20
- **Titel:** File Permissions
- **Slug:** file-permissions
- **Difficulty:** Lätt
- **Tid:** 50 minuter
- **XP:** 75
- **Föregående:** Mount Points och Device Files
- **Nästa:** Inodes, Hard Links och Symbolic Links

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Grundläggande permissions: read, write, execute
2. User, Group, Others - tredelningen
3. chmod - numerisk (755) och symbolisk (u+x) notation
4. chown och chgrp - ägarskap
5. Specialbitar: setuid, setgid, sticky bit
6. Default permissions med umask
7. Hur permissions påverkar kataloger vs filer
8. stat-kommandot för detaljerad information

## Övningar
1. **Grundläggande:** Skapa filer och kataloger, experimentera med chmod
2. **Tillämpad:** Skapa ett delat team-directory med korrekta permissions
3. **Utmanande:** Sätt upp en deploy-katalog med sticky bit och gruppskrivning

## DevOps-kontext
- Dockerfile och permission-problem (USER-direktiv)
- SSH-nycklar och deras kritiska permissions (600/700)
- Secrets management och file permissions
- CI/CD artifact permissions

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 4: Inodes, Hard Links och Symbolic Links

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 4 av 20
- **Titel:** Inodes, Hard Links och Symbolic Links
- **Slug:** inodes-links
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 80
- **Föregående:** File Permissions
- **Nästa:** Disk Management

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Vad inodes är och varför de finns
2. Inode-struktur: metadata vs data
3. Hard links - samma inode, olika namn
4. Symbolic links - pekare till sökväg
5. Skillnader: hard vs soft links
6. ln-kommandot för båda typer
7. stat och ls -i för inode-information
8. Inode exhaustion - när inodes tar slut

## Övningar
1. **Grundläggande:** Skapa hard och soft links, inspektera med ls -li
2. **Tillämpad:** Skapa en versionshantering med symlinks (current → v1, v2, v3)
3. **Utmanande:** Diagnostisera och lös ett "disk full" problem orsakat av inode exhaustion

## DevOps-kontext
- Symlinks i deployments (current → release-xxx)
- Docker layers och copy-on-write
- Configuration management med symlinks
- Atomic deployments med symlink-swap

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept (t.ex. bibliotekskortsanalogi för inodes)
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 5: Disk Management

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 5 av 20
- **Titel:** Disk Management
- **Slug:** disk-management
- **Difficulty:** Medium
- **Tid:** 55 minuter
- **XP:** 85
- **Föregående:** Inodes, Hard Links och Symbolic Links
- **Nästa:** Process Lifecycle and States

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Disk-terminologi: partitioner, volymer, filsystem
2. Partitioneringsverktyg: fdisk, parted, gdisk
3. Filsystem: ext4, xfs, btrfs - för/nackdelar
4. mkfs för att skapa filsystem
5. LVM basics: PV, VG, LV
6. df och du för diskutrymmesanalys
7. ncdu för interaktiv analys
8. Disk health med smartctl

## Övningar
1. **Grundläggande:** Analysera diskutrymme med df, du och ncdu
2. **Tillämpad:** Skapa en loopback-device, partitionera och montera
3. **Utmanande:** Sätt upp LVM med två virtuella diskar och utöka en logical volume

## DevOps-kontext
- EBS volumes i AWS - resize och snapshot
- Kubernetes storage classes och provisioners
- Monitoring diskutrymme med Prometheus node_exporter
- Automatisk disk cleanup i CI/CD

## Struktur att följa
1. Hook (relaterbar scenario - disk full i produktion)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 6: Process Lifecycle and States

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 6 av 20
- **Titel:** Process Lifecycle and States
- **Slug:** process-lifecycle-states
- **Difficulty:** Medium
- **Tid:** 50 minuter
- **XP:** 80
- **Föregående:** Disk Management
- **Nästa:** Foreground vs Background Processes

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Vad är en process? PID, PPID, hierarki
2. Process states: Running (R), Sleeping (S/D), Stopped (T), Zombie (Z)
3. fork() och exec() - hur processer skapas
4. init/systemd som process 1 och förälder till allt
5. /proc-filsystemet för processinformation
6. Process priority och nice values
7. Orphan processes och zombie processes
8. Process groups och sessions

## Övningar
1. **Grundläggande:** Utforska /proc för en körande process
2. **Tillämpad:** Skapa ett skript som spawnar child processes och observera hierarkin
3. **Utmanande:** Identifiera och eliminera zombie processes i ett testsystem

## DevOps-kontext
- Container PID 1 problem (tini, dumb-init)
- Kubernetes pod lifecycle och restart policies
- Process monitoring med systemd
- Graceful shutdown i microservices

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - familjeträd för processhierarki)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 7: Foreground vs Background Processes

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 7 av 20
- **Titel:** Foreground vs Background Processes
- **Slug:** foreground-background-processes
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 80
- **Föregående:** Process Lifecycle and States
- **Nästa:** Job Control

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Foreground vs background - konceptuell skillnad
2. Starta processer i bakgrunden med &
3. Ctrl+Z för att stoppa (suspend) en process
4. stdin, stdout, stderr i förhållande till terminal
5. Vad händer vid terminal-disconnect?
6. Process groups och controlling terminal
7. Session leaders och deras roll

## Övningar
1. **Grundläggande:** Starta processer i förgrund och bakgrund, observera beteende
2. **Tillämpad:** Kör ett långvarigt jobb i bakgrunden med output redirect
3. **Utmanande:** Simulera terminal-disconnect och se vad som överlever

## DevOps-kontext
- SSH-sessioner och bakgrundsprocesser
- CI/CD job runners och process management
- Daemon-processer vs interaktiva processer
- Container foreground requirement

## Struktur att följa
1. Hook (relaterbar scenario - SSH-sessionen dog mitt i deployment)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 8: Job Control (jobs, fg, bg, nohup)

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 8 av 20
- **Titel:** Job Control (jobs, fg, bg, nohup)
- **Slug:** job-control
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 75
- **Föregående:** Foreground vs Background Processes
- **Nästa:** Signals

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Shell job control - jobs-kommandot
2. Job ID vs PID
3. fg och bg för att flytta jobb
4. %1, %2 notation för jobb
5. nohup - överlevnad efter logout
6. disown - koppla loss från shell
7. tmux/screen intro för session persistence
8. Skillnaden mellan nohup, disown och screen/tmux

## Övningar
1. **Grundläggande:** Hantera flera jobb med jobs, fg, bg
2. **Tillämpad:** Kör ett långvarigt skript med nohup och verifiera output
3. **Utmanande:** Sätt upp tmux med named sessions och window management

## DevOps-kontext
- Long-running deployments över SSH
- Tmux i jump hosts och bastion servers
- CI/CD timeout management
- Background jobs i provisioning scripts

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 9: Signals (SIGTERM, SIGKILL, SIGHUP)

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 9 av 20
- **Titel:** Signals (SIGTERM, SIGKILL, SIGHUP)
- **Slug:** signals
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 80
- **Föregående:** Job Control
- **Nästa:** Process Monitoring

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Vad är signals? Inter-process communication
2. Vanliga signals: SIGTERM (15), SIGKILL (9), SIGHUP (1), SIGINT (2)
3. kill-kommandot och killall
4. Varför SIGTERM före SIGKILL
5. Signal handlers i scripts (trap)
6. pkill för pattern-baserad killing
7. Signals som inte kan fångas (SIGKILL, SIGSTOP)
8. Signal forwarding i containers

## Övningar
1. **Grundläggande:** Skicka olika signals och observera processbeteende
2. **Tillämpad:** Skapa ett skript med trap för graceful shutdown
3. **Utmanande:** Implementera en signal handler som sparar state före termination

## DevOps-kontext
- Kubernetes pod termination och preStop hooks
- Docker stop vs kill (SIGTERM grace period)
- Systemd KillMode och TimeoutStopSec
- Application graceful shutdown patterns

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - signaler som telefonsamtal)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 10: Process Monitoring (ps, top, htop)

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 10 av 20
- **Titel:** Process Monitoring (ps, top, htop)
- **Slug:** process-monitoring
- **Difficulty:** Medium
- **Tid:** 50 minuter
- **XP:** 80
- **Föregående:** Signals
- **Nästa:** Systemd Architecture

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. ps - snapshot av processer (aux, -ef, custom output)
2. top - realtidsövervakning
3. htop - interaktiv processhantering
4. Load average - vad det betyder
5. CPU%, MEM%, VSZ, RSS - förstå kolumnerna
6. Sortering och filtrering i top/htop
7. pgrep för att hitta processer
8. /proc/[pid]/status för detaljerad info

## Övningar
1. **Grundläggande:** Utforska ps aux och lär dig tolka output
2. **Tillämpad:** Använd htop för att identifiera resurskrävande processer
3. **Utmanande:** Skapa ett monitoring-script som alertar vid hög CPU/minne

## DevOps-kontext
- Container resource monitoring med cgroups
- Kubernetes pod metrics och resource requests/limits
- Prometheus process exporter
- Alerting on runaway processes

## Struktur att följa
1. Hook (relaterbar scenario - servern är seg, vad gör du?)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 11: Systemd Architecture

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 11 av 20
- **Titel:** Systemd Architecture
- **Slug:** systemd-architecture
- **Difficulty:** Medium
- **Tid:** 55 minuter
- **XP:** 85
- **Föregående:** Process Monitoring
- **Nästa:** Unit Files

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Vad är systemd och varför ersatte det init/SysV
2. Systemd som PID 1 och init system
3. Unit types: service, socket, timer, mount, target
4. Dependencies och ordering (After, Requires, Wants)
5. Targets vs runlevels
6. Systemd directories: /lib/systemd/system, /etc/systemd/system
7. systemctl basics: status, list-units, list-unit-files
8. Systemd logging integration med journald

## Övningar
1. **Grundläggande:** Utforska systemd units med systemctl
2. **Tillämpad:** Analysera dependencies för en service med systemctl show
3. **Utmanande:** Rita ut boot-dependency chain med systemd-analyze

## DevOps-kontext
- Containerized systemd (begränsningar)
- Infrastructure as Code för services
- Consistency across server fleet
- Service recovery och restart policies

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - systemd som orkesterledare)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 12: Unit Files (service, timer, socket)

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 12 av 20
- **Titel:** Unit Files (service, timer, socket)
- **Slug:** unit-files
- **Difficulty:** Medium
- **Tid:** 55 minuter
- **XP:** 85
- **Föregående:** Systemd Architecture
- **Nästa:** Service Management

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Unit file anatomy: [Unit], [Service], [Install] sektioner
2. Service types: simple, forking, oneshot, notify
3. ExecStart, ExecStop, ExecReload
4. Restart policies och RestartSec
5. Timer units som cron-ersättning (OnCalendar, OnBootSec)
6. Socket activation basics
7. Environment och EnvironmentFile
8. User, Group, WorkingDirectory

## Övningar
1. **Grundläggande:** Analysera en befintlig service unit file
2. **Tillämpad:** Skapa en egen service för ett shell-script
3. **Utmanande:** Sätt upp en timer unit som kör backup-script dagligen

## DevOps-kontext
- Configuration management av systemd units (Ansible)
- Service discovery med socket activation
- Scheduled jobs utan cron
- Application deployment patterns

## Struktur att följa
1. Hook (relaterbar scenario)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 13: Service Management (systemctl)

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 13 av 20
- **Titel:** Service Management (systemctl)
- **Slug:** service-management
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 80
- **Föregående:** Unit Files
- **Nästa:** Boot Process and Targets

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. systemctl start, stop, restart, reload
2. enable vs disable (boot persistence)
3. mask vs disable - permanent blockering
4. status - tolka output och exit codes
5. daemon-reload efter unit file changes
6. show för alla properties
7. edit för drop-in overrides
8. is-active, is-enabled, is-failed checks

## Övningar
1. **Grundläggande:** Hantera nginx/apache med systemctl
2. **Tillämpad:** Skapa drop-in override för att ändra timeouts
3. **Utmanande:** Skriv ett healthcheck-script som verifierar service status

## DevOps-kontext
- Service management i deployment pipelines
- Ansible service module
- Health checks och readiness probes
- Zero-downtime restarts

## Struktur att följa
1. Hook (relaterbar scenario - "varför startar inte servicen vid boot?")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 14: Boot Process and Targets

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 14 av 20
- **Titel:** Boot Process and Targets
- **Slug:** boot-process-targets
- **Difficulty:** Medium
- **Tid:** 50 minuter
- **XP:** 80
- **Föregående:** Service Management
- **Nästa:** Journald and Logging

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Boot sequence: BIOS/UEFI → bootloader → kernel → systemd
2. GRUB2 basics och kernel parameters
3. Systemd targets: graphical, multi-user, rescue, emergency
4. Default target och hur man ändrar
5. Boot into rescue/emergency mode
6. systemd-analyze för boot time analysis
7. Debugging boot problems
8. Target dependencies och isolate

## Övningar
1. **Grundläggande:** Analysera boot time med systemd-analyze
2. **Tillämpad:** Ändra default target och testa boot utan GUI
3. **Utmanande:** Felsök ett system som inte bootar - rescue mode recovery

## DevOps-kontext
- Server boot optimization
- Headless server configuration
- Recovery scenarios i cloud environments
- AMI/image boot customization

## Struktur att följa
1. Hook (relaterbar scenario - servern bootar inte efter kernel upgrade)
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - boot som raketuppskjutning)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 15: Journald and Logging

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 15 av 20
- **Titel:** Journald and Logging
- **Slug:** journald-logging
- **Difficulty:** Medium
- **Tid:** 50 minuter
- **XP:** 80
- **Föregående:** Boot Process and Targets
- **Nästa:** User and Group Management

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. journalctl - systemd journal interface
2. Filtrering: -u (unit), -p (priority), --since/--until
3. Following logs: -f (follow)
4. Journal storage och persistens (/var/log/journal)
5. Rotation och storage limits (journald.conf)
6. Integration med syslog och rsyslog
7. Strukturerad loggning och fields
8. Log levels och facilities

## Övningar
1. **Grundläggande:** Utforska journalctl med olika filter
2. **Tillämpad:** Konfigurera persistent journal storage och sätt storage limits
3. **Utmanande:** Skapa ett log analysis script som hittar error patterns

## DevOps-kontext
- Centraliserad loggning (ELK, Loki)
- Log shipping och aggregation
- Container logging drivers
- Compliance och log retention policies

## Struktur att följa
1. Hook (relaterbar scenario - "när kraschade servicen egentligen?")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - journal som svart låda)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 16: User and Group Management

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 16 av 20
- **Titel:** User and Group Management
- **Slug:** user-group-management
- **Difficulty:** Medium
- **Tid:** 50 minuter
- **XP:** 80
- **Föregående:** Journald and Logging
- **Nästa:** Sudo Configuration

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. /etc/passwd och /etc/shadow - struktur och fält
2. /etc/group - grupphantering
3. useradd, usermod, userdel
4. groupadd, groupmod, groupdel
5. Primär vs sekundär grupp
6. passwd för lösenordshantering
7. System accounts vs regular accounts
8. Home directory skeleton (/etc/skel)

## Övningar
1. **Grundläggande:** Skapa användare och grupper, utforska /etc/passwd
2. **Tillämpad:** Konfigurera en deploy-användare med specifika gruppmedlemskap
3. **Utmanande:** Skapa ett onboarding-script för nya utvecklare

## DevOps-kontext
- Service accounts för applikationer
- User namespaces i containers
- Ansible user module
- LDAP/AD integration (intro)

## Struktur att följa
1. Hook (relaterbar scenario - "ny utvecklare ska ha access")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 17: Sudo Configuration

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 17 av 20
- **Titel:** Sudo Configuration
- **Slug:** sudo-configuration
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 80
- **Föregående:** User and Group Management
- **Nästa:** PAM Modules

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. sudo vs su - skillnader och best practices
2. /etc/sudoers - syntax och struktur
3. visudo för säker editering
4. User och group specifications
5. Command aliases och User aliases
6. NOPASSWD och säkerhetsrisker
7. /etc/sudoers.d/ för modular konfiguration
8. Logging och auditing av sudo

## Övningar
1. **Grundläggande:** Ge en användare begränsad sudo access
2. **Tillämpad:** Skapa en deploy-roll med specifika kommandon utan lösenord
3. **Utmanande:** Konfigurera sudo med loggning till separat fil

## DevOps-kontext
- Least privilege i automation
- Ansible become directives
- CI/CD pipeline permissions
- Audit trails för compliance

## Struktur att följa
1. Hook (relaterbar scenario - "hur ger jag deploy-scriptet root-access säkert?")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - sudo som nyckelskåp)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 18: PAM Modules

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 18 av 20
- **Titel:** PAM Modules
- **Slug:** pam-modules
- **Difficulty:** Medium
- **Tid:** 45 minuter
- **XP:** 85
- **Föregående:** Sudo Configuration
- **Nästa:** SSH Hardening

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Vad är PAM (Pluggable Authentication Modules)?
2. PAM stack: auth, account, password, session
3. Control flags: required, requisite, sufficient, optional
4. /etc/pam.d/ - service-specifik konfiguration
5. pam_unix, pam_permit, pam_deny - vanliga moduler
6. pam_limits för resource limits
7. pam_faillock för login försök
8. Debugging PAM (auth.log)

## Övningar
1. **Grundläggande:** Utforska PAM-konfiguration för sudo och sshd
2. **Tillämpad:** Konfigurera pam_limits för en applikationsanvändare
3. **Utmanande:** Sätt upp pam_faillock för att blockera brute force

## DevOps-kontext
- SSH hardening med PAM
- Resource limits för containers/services
- MFA integration (Google Authenticator PAM)
- Centralized auth (SSSD/FreeIPA)

## Struktur att följa
1. Hook (relaterbar scenario - "varför kan användaren inte logga in?")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - PAM som säkerhetsvakter)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 19: SSH Hardening

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 19 av 20
- **Titel:** SSH Hardening
- **Slug:** ssh-hardening
- **Difficulty:** Medium
- **Tid:** 50 minuter
- **XP:** 85
- **Föregående:** PAM Modules
- **Nästa:** Firewall Basics

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. SSH key-baserad autentisering (ed25519 vs RSA)
2. ssh-keygen och key management
3. /etc/ssh/sshd_config - viktiga direktiv
4. Disable root login och password auth
5. Port change och security through obscurity
6. AllowUsers/AllowGroups restrictions
7. Fail2ban för brute force protection
8. SSH jump hosts och ProxyJump

## Övningar
1. **Grundläggande:** Sätt upp SSH key-based auth och testa
2. **Tillämpad:** Härda sshd_config enligt best practices
3. **Utmanande:** Konfigurera fail2ban och SSH jump host

## DevOps-kontext
- Bastion hosts och jump servers
- Ansible SSH connection settings
- GitHub deploy keys
- SSH certificates (intro)

## Struktur att följa
1. Hook (relaterbar scenario - "servern attackeras med brute force")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

## Prompt 20: Firewall Basics (ufw, iptables)

```markdown
# DevOpsHub Content Generation Request

## Metadata
- **Modul:** Linux Mastery
- **Nod:** 20 av 20
- **Titel:** Firewall Basics (ufw, iptables)
- **Slug:** firewall-basics
- **Difficulty:** Medium
- **Tid:** 55 minuter
- **XP:** 85
- **Föregående:** SSH Hardening
- **Nästa:** [Nästa modul: Shell Scripting Foundations]

## Uppgift
Skapa komplett pedagogiskt innehåll för denna nod enligt DevOpsHub:s standardstruktur.

## Innehåll att täcka
1. Firewall koncept: ingress, egress, chains
2. ufw - user-friendly frontend
3. ufw enable, allow, deny, reject
4. ufw app profiles
5. iptables basics: INPUT, OUTPUT, FORWARD
6. iptables -L för att visa regler
7. nftables som iptables-ersättare (intro)
8. Persistent firewall rules

## Övningar
1. **Grundläggande:** Konfigurera ufw för en webserver (22, 80, 443)
2. **Tillämpad:** Skapa rate limiting för SSH med ufw
3. **Utmanande:** Implementera samma regler med iptables och jämför

## DevOps-kontext
- Security groups i cloud environments
- Kubernetes network policies
- Container networking och iptables
- Infrastructure as Code för firewall rules

## Struktur att följa
1. Hook (relaterbar scenario - "servern är exponerad mot internet")
2. Lärandemål (4-5 mätbara mål med checkboxar)
3. Förkunskaper
4. Koncept & Teori (narrativ stil, analogier - firewall som grindar)
5. Praktiska exempel (5-8 st, ALLA med kommentarer)
6. Övningar (exakt 3 st med dolda lösningar i <details>)
7. Vanliga misstag (3-4 st med Symptom → Orsak → Lösning)
8. Best Practices & Tips
9. DevOps i praktiken (2+ scenarier)
10. Sammanfattning (5-7 punkter)
11. Nästa steg (avsluta modulen, peka mot nästa)

## Stilkrav
- Svenska språket genomgående
- "Du"-form, inte "man" eller "vi"
- Tekniska termer på engelska där det är standard
- Narrativ, pedagogisk ton - inte akademisk
- Analogier för abstrakta koncept
- ALLA kodblock MÅSTE ha förklarande kommentarer på svenska
- Lösningar i <details><summary>🔍 Visa lösning</summary>...</details>
- Ubuntu/Debian-fokus för kommandon
```

---

# Modul-sammanfattning

## Linux Mastery - 20 Noder

| # | Titel | Tid | XP | Difficulty |
|---|-------|-----|-----|-----------|
| 1 | Filesystem Hierarchy Standard | 45 min | 75 | Lätt |
| 2 | Mount Points och Device Files | 40 min | 65 | Lätt |
| 3 | File Permissions | 50 min | 75 | Lätt |
| 4 | Inodes, Hard Links och Symbolic Links | 45 min | 80 | Medium |
| 5 | Disk Management | 55 min | 85 | Medium |
| 6 | Process Lifecycle and States | 50 min | 80 | Medium |
| 7 | Foreground vs Background Processes | 45 min | 80 | Medium |
| 8 | Job Control (jobs, fg, bg, nohup) | 45 min | 75 | Medium |
| 9 | Signals (SIGTERM, SIGKILL, SIGHUP) | 45 min | 80 | Medium |
| 10 | Process Monitoring (ps, top, htop) | 50 min | 80 | Medium |
| 11 | Systemd Architecture | 55 min | 85 | Medium |
| 12 | Unit Files (service, timer, socket) | 55 min | 85 | Medium |
| 13 | Service Management (systemctl) | 45 min | 80 | Medium |
| 14 | Boot Process and Targets | 50 min | 80 | Medium |
| 15 | Journald and Logging | 50 min | 80 | Medium |
| 16 | User and Group Management | 50 min | 80 | Medium |
| 17 | Sudo Configuration | 45 min | 80 | Medium |
| 18 | PAM Modules | 45 min | 85 | Medium |
| 19 | SSH Hardening | 50 min | 85 | Medium |
| 20 | Firewall Basics (ufw, iptables) | 55 min | 85 | Medium |

**Totalt:** ~16 timmar, 1605 XP

---

# Batch Processing Workflow

1. **Skicka prompt till Opus** (en i taget)
2. **Verifiera output:**
   - [ ] Alla 11 sektioner finns
   - [ ] Svenska genomgående
   - [ ] Alla kodblock har kommentarer
   - [ ] 3 övningar med dolda lösningar
   - [ ] DevOps-kontext inkluderad
3. **Spara som:** `NOD_XX_slug.md`
4. **Upprepa för nästa nod**

**Uppskattat total tid:** 20 noder × 15 min = ~5 timmar
