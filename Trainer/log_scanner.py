#!/usr/bin/env python3
import re

rex = re.compile(r"([A-Z]+) *?:")

events = {}
with open("/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt") as fd:
    for line in fd.read().splitlines():
        match = rex.search(line)
        if match:
            event_name = match.group(1)
            try:
                events[event_name] += 1
            except KeyError:
                events[event_name] = 1

for k, v in events.items():
    print(f"Ereignis: {k} Häufigkeit: {v}")
    