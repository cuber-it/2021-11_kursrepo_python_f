import re
rex = re.compile(r"([a-Z]+) *?:")

events = {}
with open("/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn04/sample.log.txt") as fd:
    for line in fd.read().splitlines():
        match = rex.search(line)
        if match:
            event_name = match.group(1)
            if not event_name in events:
                events[event_name] +=1

for k, v in events.items():
    print(f"Ereignis: {k} Häufigkeit: {v}")