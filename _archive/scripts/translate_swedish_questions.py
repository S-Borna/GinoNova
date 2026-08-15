#!/usr/bin/env python3
"""
Översätter alla svenska VG-frågor till engelska
"""

import re

# Översättningstabell för svenska frågor
translations = {
    # VG frågor
    'Ett kommando skriver både normal output och felmeddelanden. Du vill att inget visas i terminalen men att endast felen sparas i fil.':
        'A command writes both normal output and error messages. You want nothing displayed in terminal but only errors saved to file.',

    'Du vill visa unika rader och hur många gånger varje förekommer.':
        'You want to display unique lines and how many times each occurs.',

    'Vad blir effekten av att köra uniq före sort?':
        'What is the effect of running uniq before sort?',

    'Du kan lista en katalog men inte gå in i den.':
        'You can list a directory but not enter it.',

    'Vad krävs för att ta bort en directory med innehåll?':
        'What is required to remove a directory with contents?',

    'Ett script är exekverbart men kan inte köras.':
        'A script is executable but cannot be run.',

    'Vilka permissions gäller om usern tillhör gruppen men inte är owner?':
        'Which permissions apply if user belongs to group but is not owner?',

    'Syftet med umask är att:':
        'The purpose of umask is to:',

    'Which directorypermission innebär störst risk?':
        'Which directory permission poses the greatest risk?',

    'Vad skiljer SIGTERM från SIGKILL?':
        'What distinguishes SIGTERM from SIGKILL?',

    'Bakgrundsprocess dör när terminalen stängs.':
        'Background process dies when terminal closes.',

    'När är zip mest lämpligt?':
        'When is zip most appropriate?',

    'Why är PID 1 kritisk?':
        'Why is PID 1 critical?',

    'Why är bind mounts känsligare?':
        'Why are bind mounts more sensitive?',

    '1. Why är containrar lättare än VM?':
        'Why are containers lighter than VMs?',

    'En container är best described as:':
        'A container is best described as:',

    'Why fungerar inte uniq file.txt alltid som förväntat?':
        'Why does uniq file.txt not always work as expected?',

    'Which signal kan inte fångas av ett program?':
        'Which signal cannot be caught by a program?',

    'What is Docker volumes främst used for?':
        'What are Docker volumes primarily used for?',

    'Which command visar output på skärmen och skriver samma output till fil?':
        'Which command displays output on screen and writes same output to file?',

    'Which command visar status från senast körda kommando?':
        'Which command shows status from last executed command?',

    'Why ger uniq file.txt inte alltid förväntat resultat?':
        'Why does uniq file.txt not always give expected result?',

    'Extrahera kolumn 1 från CSV, sortera numeriskt fallande och visa tre greatesta värdena.':
        'Extract column 1 from CSV, sort numerically descending and show three greatest values.',

    'Why används less för stora filer?':
        'Why is less used for large files?',

    'Innehållet följer inte med vid kopiering av katalog.':
        'Contents not included when copying directory.',

    'How avgör kommandot file filtyp?':
        'How does the file command determine file type?',

    'What does x på directory?':
        'What does x on directory do?',

    'Sudo echo test > file ger permission denied. Varför?':
        'Sudo echo test > file gives permission denied. Why?',

    'Why bör SIGKILL undvikas?':
        'Why should SIGKILL be avoided?',

    'Why körs apt update separat från apt upgrade?':
        'Why is apt update run separately from apt upgrade?',

    'How hittas ls vid körning?':
        'How is ls found when executed?',

    'Tillgängligt diskutrymme skiljer sig p.g.a.:':
        'Available disk space differs due to:',

    'Why används swap trots ledigt RAM?':
        'Why is swap used despite available RAM?',

    'Why används tar tillsammans med gzip?':
        'Why is tar used together with gzip?',

    'Arkivering jämfört med komprimering:':
        'Archiving compared to compression:',

    'Första felsökningssteg vid krasch:':
        'First troubleshooting step on crash:',

    'Journalctl fördel:':
        'Journalctl advantage:',

    # Options översättningar
    'Saknar read': 'Missing read permission',
    'Scriptet är tomt': 'Script is empty',
    'Katalog saknar execute': 'Directory missing execute',
    'Fel ägare': 'Wrong owner',
    'Group permissions': 'Group permissions',
    'Owner permissions': 'Owner permissions',
    'Other permissions': 'Other permissions',
    'Ingen skillnad': 'No difference',
    'Endast unika rader visas': 'Only unique lines displayed',
    'Alla rader visas': 'All lines displayed',
    'Endast dubletter försvinner': 'Only duplicates removed',
    'Standard defaultpermissions': 'Default standard permissions',
    'Begränsa defaultpermissions': 'Limit default permissions',
    'Ändra permissions': 'Change permissions',
    'Ta bort permissions': 'Remove permissions',
    'Startar all andra processer': 'Starts all other processes',
    'Första process': 'First process',
    'Systemprocess': 'System process',
    'Kan terminera system': 'Can terminate system',
    'Säkerhet': 'Security',
    'Kompatibilitet': 'Compatibility',
    'Prestanda': 'Performance',
    'Portabilitet': 'Portability',
    'Kan starta om system': 'Can restart system',
    'Delar host kernel': 'Shares host kernel',
    'Mindre resurser': 'Fewer resources',
    'Snabbare start': 'Faster startup',
    'Mappar host filesystem direkt': 'Maps host filesystem directly',
    'Högriskområden exponerade': 'High-risk areas exposed',
    'Lättare att ta bort': 'Easier to remove',
    'Ingen isolering': 'No isolation',
    'SIGTERM kan fångas': 'SIGTERM can be caught',
    'SIGKILL kan inte fångas': 'SIGKILL cannot be caught',
    'SIGTERM är snabbare': 'SIGTERM is faster',
    'Båda är lika': 'Both are equal',
    'Använd nohup': 'Use nohup',
    'Använd &': 'Use &',
    'Använd disown': 'Use disown',
    'Starta ny terminal': 'Start new terminal',
}

def translate_file():
    with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    count = 0

    # Översätt varje fråga och option
    for swedish, english in translations.items():
        if swedish in content:
            content = content.replace(swedish, english)
            count += 1

    # Fixa några återstående patterns
    content = re.sub(r'Why är', 'Why is', content)
    content = re.sub(r'innebär', 'means', content)
    content = re.sub(r'störst', 'greatest', content)

    with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Översatte {count} texter från svenska till engelska")

    # Verifiera
    with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'r') as f:
        new_content = f.read()

    swedish_chars = sum(1 for line in new_content.split('\n') if 'question:' in line and any(c in line for c in 'åäöÅÄÖ'))
    print(f"✓ Återstående frågor med svenska tecken: {swedish_chars}")

if __name__ == '__main__':
    translate_file()
