import re

# Variante mit voriger Kompilierung spart Zeit bei der Verarbeitung
# Regulaerer Ausruck: Leerzeichen zu Beginn, Grossbuchstaben (einer oder mehrere), beliebig viele Leerzeichen, Doppelpunkt als Abschluss
rex = re.compile(r" ([A-Z]+) *?:")

events = {}
with open("/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt") as fd:
    for line in fd.read().splitlines():
        match = rex.search(line)
        if match:
            event_name = match.group(1)
            
            if not event_name in events:
                events[event_name] = 0
                
            events[event_name] += 1

for k, v in events.items():
    print(f"Ereignis: {k}, Häufigkeit: {v}")
