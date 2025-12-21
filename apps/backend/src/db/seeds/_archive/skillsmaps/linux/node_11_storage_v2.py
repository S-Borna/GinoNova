"""
Linux Mastery Node 11: Disk & Storage Management - V2 Interactive Format
"""

LINUX_NODE_11_STORAGE_V2 = {
    "node_id": 11,
    "title": "Disk & Storage Management",
    "slug": "disk-storage",
    "description": "Partitioner, mount, filsystem och LVM",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Disk & Storage",
            "content": {
                "headline": "Disk full = system down",
                "hook": "En full /var/log kan krascha din databas. En full root-partition stoppar allt. Du MÅSTE veta hur du kollar, hanterar och utökar lagring.",
                "learning_objectives": [
                    "Analysera diskutrymme med df och du",
                    "Förstå partitioner och filsystem",
                    "Montera och avmontera filsystem",
                    "Konfigurera /etc/fstab för permanenta mounts"
                ],
                "prerequisites": ["Basic terminal", "File system navigation"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Storage Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "df - Disk Free",
                        "explanation": "df visar tillgängligt utrymme per filsystem. -h för human-readable. Varning vid 80%+, kritiskt vid 90%+.",
                        "diagram": """
+-----------------------------------------------------+
| DF OUTPUT EXEMPEL                                   |
+-----------------------------------------------------+
| $ df -h                                             |
| Filesystem      Size  Used Avail Use% Mounted on   |
| /dev/sda1        50G   15G   32G  32% /            |
| /dev/sda2       200G  150G   40G  79% /home   ⚠️   |
| /dev/sdb1       500G  480G   10G  96% /data   🚨   |
+-----------------------------------------------------+
| VARNINGSNIVÅER:                                     |
| 80%+ -> Planera expansion                           |
| 90%+ -> Kritiskt, åtgärda nu                        |
| 95%+ -> AKUT, system kan sluta fungera              |
+-----------------------------------------------------+""",
                        "pro_tip": "df -i visar inodes - kan vara slut även med ledigt utrymme!",
                        "common_mistake": "Att bara kolla root (/) när /var eller /home kan vara fulla."
                    },
                    {
                        "title": "du - Disk Usage",
                        "explanation": "du visar storlek på filer/kataloger. Perfekt för att hitta vad som äter diskutrymme.",
                        "diagram": """
+-----------------------------------------------------+
| DU KOMMANDON                                        |
+-----------------------------------------------------+
| du -sh /var/log     | Total storlek på katalog     |
| du -h --max-depth=1 | En nivå i taget              |
| du -h /var | sort -rh | head -20                   |
|                     | Hitta de största tjuvarna     |
+-----------------------------------------------------+
| HITTA STORA FILER:                                  |
| find / -type f -size +100M 2>/dev/null             |
| ncdu /   <- interaktiv disk usage                   |
+-----------------------------------------------------+""",
                        "pro_tip": "Installera ncdu för interaktiv diskanalys - mycket snabbare!",
                        "common_mistake": "Att glömma 2>/dev/null på find - du drunknar i permission errors."
                    },
                    {
                        "title": "Mount & fstab",
                        "explanation": "mount kopplar filsystem till kataloger. /etc/fstab gör mounts permanenta över omstarter.",
                        "diagram": """
+-----------------------------------------------------+
| MOUNT WORKFLOW                                      |
+-----------------------------------------------------+
| lsblk              | Lista blockenheter            |
| sudo mount /dev/sdb1 /mnt/data                     |
|                    | Temporär mount                |
| sudo umount /mnt/data                              |
|                    | Avmontera                      |
+-----------------------------------------------------+
| /etc/fstab SYNTAX:                                  |
| /dev/sdb1  /mnt/data  ext4  defaults  0  2        |
| |          |         |     |         |  |         |
| device     mountpoint fs    options  dump fsck    |
+-----------------------------------------------------+""",
                        "pro_tip": "Använd UUID istället för /dev/sdX - det ändras inte!",
                        "common_mistake": "Fel i fstab kan göra systemet obootbart. Alltid test med 'mount -a' först!"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Storage",
            "content": {
                "exercises": [
                    {
                        "task": "Visa diskutrymme",
                        "instruction": "Visa tillgängligt utrymme på alla filsystem i human-readable format",
                        "expected_command": "df -h",
                        "hint": "-h gör GB/MB istället för bytes"
                    },
                    {
                        "task": "Hitta stora kataloger",
                        "instruction": "Visa de 10 största katalogerna under /var",
                        "expected_command": "du -h /var --max-depth=1 | sort -rh | head -10",
                        "hint": "sort -rh sorterar human-readable storlekar omvänt"
                    },
                    {
                        "task": "Lista blockenheter",
                        "instruction": "Visa alla diskar och partitioner",
                        "expected_command": "lsblk",
                        "hint": "lsblk visar också mountpoints"
                    },
                    {
                        "task": "Hitta stora filer",
                        "instruction": "Hitta alla filer större än 100MB",
                        "expected_command": "find / -type f -size +100M 2>/dev/null",
                        "hint": "+100M = större än 100 megabyte"
                    }
                ],
                "estimated_time": "10 min",
                "xp_reward": 30
            }
        },
        {
            "section_id": "quiz",
            "type": "quiz",
            "title": "Testa dina kunskaper",
            "content": {
                "questions": {
                    "flashcards": [
                        {"front": "Skillnad mellan df och du?", "back": "df visar tillgängligt per filsystem, du visar storlek per katalog/fil"},
                        {"front": "Vad gör /etc/fstab?", "back": "Definierar vilka filsystem som monteras automatiskt vid boot"},
                        {"front": "Varför använda UUID i fstab?", "back": "UUID ändras inte om diskordning ändras, /dev/sdX kan byta plats"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vad betyder 'Avail' i df output?",
                            "options": ["Totalt utrymme", "Använt utrymme", "Ledigt utrymme", "Reserverat utrymme"],
                            "correct": 2,
                            "explanation": "Avail = Available = ledigt utrymme på filsystemet"
                        },
                        {
                            "question": "Hur verifierar du fstab-ändringar utan reboot?",
                            "options": ["systemctl reload", "mount -a", "fstab --check", "mount --verify"],
                            "correct": 1,
                            "explanation": "mount -a försöker montera allt i fstab, visar fel om något är fel"
                        }
                    ]
                },
                "passing_score": 0.8,
                "estimated_time": "5 min",
                "xp_reward": 25
            }
        },
        {
            "section_id": "challenge",
            "type": "challenge",
            "title": "Storage Challenge",
            "content": {
                "scenario": "Servern varnar för lågt diskutrymme. Analysera och åtgärda.",
                "requirements": [
                    "Identifiera vilket filsystem som är fullt",
                    "Hitta de 5 största katalogerna",
                    "Hitta och lista filer större än 50MB",
                    "Identifiera vad som kan tas bort säkert"
                ],
                "hints": [
                    "df -h för översikt",
                    "du + sort + head för att hitta tjuvar",
                    "Kolla /var/log/ och /tmp/"
                ],
                "solution": """# 1. Översikt - vilket filsystem är fullt?
df -h

# 2. Analysera /var (ofta problemet)
du -h /var --max-depth=1 | sort -rh | head -10

# 3. Gå djupare på /var/log
du -h /var/log --max-depth=1 | sort -rh | head -10

# 4. Hitta stora filer
find /var -type f -size +50M 2>/dev/null | xargs ls -lh

# 5. Säker cleanup
# Ta bort gamla loggar
sudo find /var/log -name "*.gz" -mtime +30 -delete
sudo find /var/log -name "*.old" -delete

# Rensa journal
sudo journalctl --vacuum-time=7d

# Rensa apt cache
sudo apt clean

# 6. Verifiera
df -h""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
