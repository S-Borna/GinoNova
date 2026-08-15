#!/usr/bin/env python3
"""
Konverterar ManpageTentan.md till TypeScript quiz format
- Extraherar alla frågor (210 G + 55 VG)
- Randomiserar rätt svarsalternativ för att undvika mönster
- Bevarar allt innehåll
"""

import re
import random
from typing import List, Dict, Tuple

def parse_questions(filepath: str) -> Tuple[List[Dict], List[Dict]]:
    """Läser och parsar alla frågor från markdown-filen"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split på VG-markering
    parts = content.split('### VG FRÅGOR FÖLJER NEDAN')
    g_section = parts[0]
    vg_section = parts[1] if len(parts) > 1 else ""

    def extract_questions(text: str) -> List[Dict]:
        questions = []
        # Split text into lines for manual parsing
        lines = text.split('\n')

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Hitta fråga (slutar med ? ELLER slutar med :)
            # Men måste vara rimlig längd och inte börja med A/B/C/D
            is_question = False
            if line and not line.startswith(('A.', 'B.', 'C.', 'D.', 'Rätt', '#')):
                if line.endswith('?') or line.endswith(':'):
                    is_question = True
                # Kan också vara ett statement som "Exit code 0 means"
                elif len(line) > 10 and not line.startswith('1.'):
                    # Kolla om nästa icke-tomma rad är "A."
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip().startswith('A.'):
                        is_question = True

            if is_question:
                question_text = line

                # Försök läsa de 4 alternativen
                options = []
                j = i + 1

                # Hoppa över tomma rader
                while j < len(lines) and not lines[j].strip():
                    j += 1

                # Läs A, B, C, D
                for expected_prefix in ['A.', 'B.', 'C.', 'D.']:
                    if j >= len(lines):
                        break
                    opt_line = lines[j].strip()
                    if opt_line.startswith(expected_prefix):
                        options.append(opt_line[2:].strip())
                        j += 1
                    else:
                        break

                # Om vi har alla 4 alternativ, leta efter rätt svar
                if len(options) == 4:
                    # Hoppa över tomma rader
                    while j < len(lines) and not lines[j].strip():
                        j += 1

                    if j < len(lines):
                        answer_line = lines[j].strip()
                        # Matcha "Rätt:" eller "Rätt svar:"
                        match = re.match(r'Rätt(?:\s+svar)?:\s*([A-D])', answer_line)
                        if match:
                            correct_letter = match.group(1)
                            correct_idx = ord(correct_letter) - ord('A')

                            # Översätt fråga och alternativ till engelska
                            translated_question = translate_to_english(question_text)
                            translated_options = [translate_to_english(opt) for opt in options]

                            questions.append({
                                'question': translated_question,
                                'options': translated_options,
                                'correct_index': correct_idx
                            })

                            i = j

            i += 1

        return questions

    g_questions = extract_questions(g_section)
    vg_questions = extract_questions(vg_section)

    return g_questions, vg_questions

def is_swedish(text: str) -> bool:
    """Detekterar om texten är på svenska"""
    swedish_words = ['Vad', 'Vilket', 'Varför', 'Hur', 'När', 'Var', 'Vilken',
                     'används', 'innebär', 'gör', 'visar', 'betyder', 'är',
                     'kommando', 'frågor', 'svar', 'till', 'på', 'för']
    return any(word in text for word in swedish_words)

def translate_to_english(text: str) -> str:
    """Översätter svenska text till engelska, bevarar tekniska termer exakt"""
    if not is_swedish(text):
        return text

    # Dictionary för översättningar - bevarar kommandoord och tekniska termer
    translations = {
        # Frågeord
        'Vad är ': 'What is ',
        'Vad gör ': 'What does ',
        'Vad används ': 'What is ',
        'Vad innebär ': 'What does ',
        'Vad betyder ': 'What means ',
        'Vad visar ': 'What shows ',
        'Vad händer ': 'What happens ',
        'Vilket kommando ': 'Which command ',
        'Vilket Docker-kommando ': 'Which Docker command ',
        'Vilket Docker-objekt ': 'Which Docker object ',
        'Vilken ': 'Which ',
        'Vilket ': 'Which ',
        'Varför ': 'Why ',
        'Hur ': 'How ',
        'Var körs ': 'Where do ',
        'Var ': 'Where ',

        # Verb och fraser
        ' för nya filer': ' mean for new files',
        ' på en fil': ' on a file',
        ' på en katalog': ' on a directory',
        ' i Docker': ' in Docker',
        ' i en katalog': ' in a directory',
        ' från hosten': ' from host',
        ' via localhost': ' via localhost',
        ' från registry': ' from registry',
        ' i en redan körande container': ' in an already running container',
        ' och dess hemkatalog': ' and their home directory',
        ' till?': ' used for?',
        ' en bind mount': ' a bind mount',

        # Specifika fraser
        'främst?': 'primarily?',
        'bäst beskriven som:': 'best described as:',
        'listar körande containrar?': 'lists running containers?',
        'listar alla körande processer för alla användare?': 'lists all running processes for all users?',
        'ändrar ägare': 'changes owner',
        'startar en container?': 'starts a container?',
        'startar en container i bakgrunden?': 'starts a container in background?',
        'extraherar ett tar-arkiv?': 'extracts a tar archive?',
        'hämtar en Docker image': 'pulls a Docker image',
        'kör ett kommando': 'runs a command',
        'stoppar en systemd-tjänst?': 'stops a systemd service?',
        'tar bort en användare': 'removes a user',
        'skickar SIGTERM som standard?': 'sends SIGTERM by default?',
        'visar systemets load average?': 'shows system load average?',
        'visar binärens sökväg för': 'shows binary path for',
        'visar vilka portar som lyssnar på systemet?': 'shows which ports are listening on the system?',
        'visar minnesanvändning?': 'shows memory usage?',
        'visar aktuell katalog?': 'shows current directory?',
        'visar hur mycket diskutrymme som används per katalog?': 'shows how much disk space is used per directory?',
        ' skiljer en bind mount från en named volume?': ' distinguishes a bind mount from a named volume?',
        ' används för nätverksisolering?': ' is used for network isolation?',

        # Svar alternativen
        'Virtuell maskin': 'Virtual machine',
        'Containerplattform': 'Container platform',
        'Pakethanterare': 'Package manager',
        'Init-system': 'Init system',
        'En komplett OS-instans': 'A complete OS instance',
        'En isolerad process': 'An isolated process',
        'En virtuell disk': 'A virtual disk',
        'En kernelmodul': 'A kernel module',
        'Körande containrar': 'Running containers',
        'Nedladdade images': 'Downloaded images',
        'Volymer': 'Volumes',
        'Nätverk': 'Network',
        'En körande container': 'A running container',
        'En mall för containrar': 'A template for containers',
        'Ett nätverk': 'A network',
        'En volym': 'A volume',
        'Containern fortsätter': 'Container continues',
        'Containern pausar': 'Container pauses',
        'Containern stoppas': 'Container stops',
        'Containern startas om automatiskt': 'Container restarts automatically',
        'Debug': 'Debug',
        'Delete on exit': 'Delete on exit',
        'Detached mode': 'Detached mode',
        'Download image': 'Download image',
        'Startar container': 'Starts container',
        'Bygger image': 'Builds image',
        'Hämtar image': 'Pulls image',
        'Tar bort image': 'Removes image',
        'I egen kernel': 'In own kernel',
        'På hypervisor': 'On hypervisor',
        'På hostens kernel': 'On host kernel',
        'I BIOS': 'In BIOS',
        'Egen kernel': 'Own kernel',
        'Hypervisor': 'Hypervisor',
        'Hostens kernel': "Host's kernel",
        'Redirecten är felaktig': 'Redirect is incorrect',
        'Output går till stderr': 'Output goes to stderr',
        'Filen är tom': 'File is empty',
        'kräver sudo': 'requires sudo',
        'Filen är för stor': 'File is too large',
        'Filen är osorterad': 'File is not sorted',
        'kräver flaggor': 'requires flags',
        'ignorerar whitespace': 'ignores whitespace',
        'Endast kataloger': 'Only directories',
        'Dolda filer': 'Hidden files',
        'Filstorlek': 'File size',
        'Filtyp': 'File type',
        'Ange hemkatalog': 'Set home directory',
        'Ange sökvägar för kommandon': 'Set command paths',
        'Lagra miljövariabler': 'Store environment variables',
        'Styra rättigheter': 'Control permissions',
        'Visa innehåll': 'Show contents',
        'Skapa filer': 'Create files',
        'Gå in i katalogen': 'Enter directory',
        'Ta bort katalogen': 'Remove directory',
        'Containern körs som root': 'Container runs as root',
        'Docker daemon är stoppad': 'Docker daemon is stopped',
        'Image saknar CMD': 'Image lacks CMD',
        'Port är inte publicerad': 'Port is not published',
        'Ingen CMD körs': 'No CMD runs',
        'Huvudprocessen avslutas': 'Main process exits',
        'Image är korrupt': 'Image is corrupt',
        'Snabbare nätverk': 'Faster network',
        'Persistens utanför container-livscykeln': 'Persistence outside container lifecycle',
        'Persistens': 'Persistence',
        'Säker inloggning': 'Secure login',
        'Säkerhet': 'Security',
        'Isolering av CPU': 'CPU isolation',
        'CPU-begränsning': 'CPU limitation',
        'alltid read-only': 'always read-only',
        'ligger i image': 'stored in image',
        'Pekar på host-sökväg': 'Points to host path',
        'pekar direkt på host-path': 'points directly to host path',
        'delas inte': 'not shared',
        'Docker-intern lagring': 'Docker internal storage',
        'Krypterad volym': 'Encrypted volume',
        'Tillfällig cache': 'Temporary cache',
        'Skriva endast till fil': 'Write only to file',
        'Visa och spara output samtidigt': 'Show and save output simultaneously',
        'Redirect stderr': 'Redirect stderr',
        'Sortera output': 'Sort output',
        'Ingen': 'None',
        'Samla filer vs minska storlek': 'Collect files vs reduce size',
        'Kryptera vs signera': 'Encrypt vs sign',
        'Sortera vs filtrera': 'Sort vs filter',
        'CPU-temperatur': 'CPU temperature',
        'Genomsnitt av körbara/väntande processer': 'Average of runnable/waiting processes',
        'RAM-förbrukning': 'RAM consumption',
        'Disk-IO': 'Disk IO',
        'Brandvägg': 'Firewall',
        'Separata nätverks-namespaces': 'Separate network namespaces',
        'Fel DNS': 'Wrong DNS',
        'Ingen routing': 'No routing',
        'hämtar paketlistor': 'fetches package lists',
        'tar bort paket': 'removes packages',
        'kräver reboot': 'requires reboot',
        'Visar images': 'Shows images',
        'Visar volymer': 'Shows volumes',
        'Visar körande containrar': 'Shows running containers',
        'Visar nätverk': 'Shows networks',
        'Tar bort kolumn 1': 'Removes column 1',
        'Visar första fältet': 'Shows first field',
        'Sorterar filen': 'Sorts file',
        'Räknar rader': 'Counts lines',
        'Startar tjänster': 'Starts services',
        'Visar loggar': 'Shows logs',
        'Skapar användare': 'Creates users',
        'Hanterar nätverk': 'Manages network',
        'kan inte köra kommandon': 'cannot run commands',
        'Svårare spårbarhet och högre risk': 'Harder traceability and higher risk',
        'saknar lösenord': 'lacks password',
        'kan inte använda sudo': 'cannot use sudo',

        # Långa meningar
        'Du kör cmd > out.txt men ser fortfarande text i terminalen. Varför?':
            'You run cmd > out.txt but still see text in terminal. Why?',
        'En container fungerar lokalt men kan inte nås från hosten.\\nVilken är den troligaste orsaken?':
            'A container works locally but cannot be reached from host.\\nWhat is the most likely cause?',
        'En container fungerar lokalt men kan inte nås från hosten.':
            'A container works locally but cannot be reached from host.',
        'Vilken är den troligaste orsaken?': 'What is the most likely cause?',
        'Två containrar försöker kommunicera via localhost men misslyckas. Varför?':
            'Two containers try to communicate via localhost but fail. Why?',
        'Du kör docker run nginx varpå containern startar och stannar direkt. Varför?':
            'You run docker run nginx and the container starts then stops immediately. Why?',
        'Vad skiljer en bind mount från en named volume?':
            'What distinguishes a bind mount from a named volume?',
        'Vad är skillnaden mellan apt update och apt upgrade?':
            'What is the difference between apt update and apt upgrade?',
        'Vad är skillnaden mellan arkivering och komprimering?':
            'What is the difference between archiving and compression?',
        'Varför kan två containrar inte nå varandra via localhost?':
            'Why can two containers not reach each other via localhost?',
        'Varför bör man undvika direkt root-login?':
            'Why should direct root login be avoided?',
        'Vad händer med data när container tas bort?':
            'What happens to data when container is removed?',
        'Vad händer när huvudprocessen i en container avslutas?':
            'What happens when main process in container exits?',
        'Du kan lista en katalog men inte gå in i den. Vad saknas?':
            'You can list a directory but not enter it. What is missing?',

        # Tekniska termer
        'rättighet': 'permission',
        'rättigheter': 'permissions',
        'rättigheten': 'permission',
        'användare': 'user',
        'katalog': 'directory',
        'miljövariabeln': 'environment variable',

        # Container-relaterade
        'Allt sparas': 'Everything is saved',
        'Writable layer försvinner': 'Writable layer disappears',
        'Flyttas till host': 'Moved to host',
        'Krypteras': 'Encrypted',
        'localhost är reserverad': 'localhost is reserved',
        'Varje container har eget nätverksnamespace': 'Each container has own network namespace',
        'Docker blockerar TCP': 'Docker blocks TCP',
        'DNS saknas': 'DNS missing',
        'nginx kräver port mapping': 'nginx requires port mapping',

        # Permissions
        'Vad innebär rättigheten chmod 640 file?': 'What does permission chmod 640 file mean?',
        'Vad innebär execute-rättighet på en katalog?': 'What does execute permission on directory mean?',
        'Vilken rättighet styr skapande och borttagning av filer i en katalog?':
            'Which permission controls creation and deletion of files in directory?',
        'Vad innebär umask 022 för nya filer?': 'What does umask 022 mean for new files?',
        'Vad innebär load average?': 'What does load average mean?',

        # Misc
        'Vad är syftet med miljövariabeln $PATH?': 'What is the purpose of environment variable $PATH?',
        'Vilket Docker-objekt används för nätverksisolering?': 'Which Docker object is used for network isolation?',
        'Container layer': 'Container layer',
        'Var körs Docker-containrar?': 'Where do Docker containers run?',
        'Docker-containrar?': 'Docker containers?',
    }

    result = text
    # Sort by length (longest first) to avoid partial replacements
    for sv, en in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(sv, en)

    return result

def randomize_options(question: Dict, target_idx: int = None) -> Dict:
    """Randomiserar ordningen på svarsalternativen
    Om target_idx ges, placera rätt svar där, annars randomisera"""
    options = question['options'].copy()
    correct_idx = question['correct_index']

    if target_idx is not None:
        # Flytta rätt svar till target position
        indices = [0, 1, 2, 3]
        indices.remove(correct_idx)
        random.shuffle(indices)

        # Skapa ny ordning där rätt svar är på target_idx
        new_indices = []
        idx_counter = 0
        for i in range(4):
            if i == target_idx:
                new_indices.append(correct_idx)
            else:
                new_indices.append(indices[idx_counter])
                idx_counter += 1

        new_options = [options[i] for i in new_indices]
        new_correct_idx = target_idx
    else:
        # Slumpa helt
        indices = [0, 1, 2, 3]
        random.shuffle(indices)
        new_options = [options[i] for i in indices]
        new_correct_idx = indices.index(correct_idx)

    return {
        'question': question['question'],
        'options': new_options,
        'correct_index': new_correct_idx
    }

def categorize_question(question_text: str) -> str:
    """Försöker kategorisera frågan baserat på innehåll"""
    text_lower = question_text.lower()

    if 'docker' in text_lower or 'container' in text_lower or 'image' in text_lower:
        return 'Docker & Containers'
    elif 'chmod' in text_lower or 'permission' in text_lower or 'chown' in text_lower:
        return 'Permissions & Rättigheter'
    elif 'systemctl' in text_lower or 'systemd' in text_lower or 'service' in text_lower:
        return 'Systemd & Services'
    elif 'network' in text_lower or 'ip' in text_lower or 'ping' in text_lower or 'dns' in text_lower:
        return 'Nätverk'
    elif 'user' in text_lower or 'sudo' in text_lower or 'passwd' in text_lower:
        return 'Användarhantering'
    elif 'process' in text_lower or 'kill' in text_lower or 'signal' in text_lower or 'pid' in text_lower:
        return 'Processer & Signaler'
    elif 'pipe' in text_lower or 'redirect' in text_lower or '|' in question_text or '>' in question_text:
        return 'Pipes & Redirection'
    elif 'disk' in text_lower or 'df' in text_lower or 'du' in text_lower or 'mount' in text_lower:
        return 'Disk & Storage'
    elif 'tar' in text_lower or 'gzip' in text_lower or 'zip' in text_lower or 'compress' in text_lower:
        return 'Arkiv & Komprimering'
    elif 'file' in text_lower or 'directory' in text_lower or 'ls' in text_lower or 'find' in text_lower:
        return 'Filer & Kataloger'
    elif 'bash' in text_lower or 'script' in text_lower or 'variable' in text_lower or '$' in question_text:
        return 'Bash Scripting'
    else:
        return 'Linux Grundläggande'

def escape_typescript_string(s: str) -> str:
    """Escape special characters för TypeScript strings"""
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('\n', '\\n')
    return s

def generate_typescript(g_questions: List[Dict], vg_questions: List[Dict], output_file: str):
    """Genererar TypeScript-fil"""

    lines = [
        '/**',
        ' * MANPAGE TENTAN - Omfattande Linux/Unix kommandoreferens quiz',
        ' * 265 frågor om bash, pipes, filer, permissions, processer, nätverk, containers m.m.',
        ' *',
        ' * Skapad: 2026-01-17',
        ' * Källa: ManpageTentan.md - Komplett tentamaterial',
        ' * Innehåll: 210 G-frågor + 55 VG-frågor',
        ' */',
        '',
        'export interface ManpageTentaQuestion {',
        '    id: string',
        '    question: string',
        '    options: [string, string, string, string]',
        '    correctIndex: 0 | 1 | 2 | 3',
        '    explanation: string',
        '    difficulty: \'G\' | \'VG\'',
        '    category: string',
        '}',
        '',
        'export const MANPAGE_TENTA_QUESTIONS: ManpageTentaQuestion[] = ['
    ]

    # Skapa perfekt jämn fördelning av correctIndex
    # 298 frågor: 298 % 4 = 2, så två får 75 och två får 74
    all_questions = g_questions + vg_questions
    total = len(all_questions)

    # Skapa exakt fördelning: varje index får floor(total/4) eller ceil(total/4)
    base_count = total // 4  # 74
    extra = total % 4  # 2

    target_distribution = []
    for i in range(4):
        count = base_count + (1 if i < extra else 0)
        target_distribution.extend([i] * count)

    # Verifiera att vi har rätt antal
    assert len(target_distribution) == total, f"Distribution length mismatch: {len(target_distribution)} != {total}"

    # Shuffla för att undvika sekventiellt mönster
    random.shuffle(target_distribution)

    # G-frågor
    for idx, q in enumerate(g_questions, 1):
        target_idx = target_distribution[idx - 1]
        randomized = randomize_options(q, target_idx)
        category = categorize_question(randomized['question'])

        lines.append('    {')
        lines.append(f"        id: 'manpage-g{idx}',")
        lines.append(f"        question: '{escape_typescript_string(randomized['question'])}',")
        lines.append(f"        options: [")
        for opt in randomized['options']:
            lines.append(f"            '{escape_typescript_string(opt)}',")
        lines.append(f"        ],")
        lines.append(f"        correctIndex: {randomized['correct_index']},")
        lines.append(f"        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',")
        lines.append(f"        difficulty: 'G',")
        lines.append(f"        category: '{category}'")
        lines.append('    },')

    # VG-frågor
    for idx, q in enumerate(vg_questions, 1):
        target_idx = target_distribution[len(g_questions) + idx - 1]
        randomized = randomize_options(q, target_idx)
        category = categorize_question(randomized['question'])

        lines.append('    {')
        lines.append(f"        id: 'manpage-vg{idx}',")
        lines.append(f"        question: '{escape_typescript_string(randomized['question'])}',")
        lines.append(f"        options: [")
        for opt in randomized['options']:
            lines.append(f"            '{escape_typescript_string(opt)}',")
        lines.append(f"        ],")
        lines.append(f"        correctIndex: {randomized['correct_index']},")
        lines.append(f"        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',")
        lines.append(f"        difficulty: 'VG',")
        lines.append(f"        category: '{category}'")
        lines.append('    }' if idx == len(vg_questions) else '    },')

    lines.append(']')
    lines.append('')
    lines.append('// Export för enkel import i tentasimulator')
    lines.append('export const ALL_MANPAGE_TENTA_QUESTIONS = MANPAGE_TENTA_QUESTIONS')
    lines.append('')

    # Skriv till fil
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    print("🔄 Läser ManpageTentan.md...")
    g_questions, vg_questions = parse_questions('ManpageTentan.md')

    print(f"✅ Extraherade {len(g_questions)} G-frågor")
    print(f"✅ Extraherade {len(vg_questions)} VG-frågor")
    print(f"📊 Totalt: {len(g_questions) + len(vg_questions)} frågor")

    if len(g_questions) != 210:
        print(f"⚠️  VARNING: Förväntat 210 G-frågor, hittade {len(g_questions)}")
    if len(vg_questions) != 55:
        print(f"⚠️  VARNING: Förväntat 55 VG-frågor, hittade {len(vg_questions)}")

    print("\n🎲 Randomiserar svarsalternativ...")
    output_file = 'apps/frontend/src/data/manpage-tenta-quiz.ts'
    generate_typescript(g_questions, vg_questions, output_file)

    print(f"✅ Skapade {output_file}")
    print("🎉 Klart!")

    # Statistik på rätta svar efter randomisering
    print("\n📊 Fördelning av korrekta svar (efter randomisering):")

    # Läs faktisk fördelning från genererad fil
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    import re
    indices = re.findall(r'correctIndex:\s*(\d+)', content)
    dist = [indices.count(str(i)) for i in range(4)]

    print(f"   A: {dist[0]} ({dist[0]/len(indices)*100:.1f}%)")
    print(f"   B: {dist[1]} ({dist[1]/len(indices)*100:.1f}%)")
    print(f"   C: {dist[2]} ({dist[2]/len(indices)*100:.1f}%)")
    print(f"   D: {dist[3]} ({dist[3]/len(indices)*100:.1f}%)")

if __name__ == '__main__':
    main()
