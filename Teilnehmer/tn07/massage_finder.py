#!/usr/bin/env python3
import re

regex = re.compile(r"([A-Z]+).*?:")

test_str = ("03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 129.1.1.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.")


result = {}
with open('/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt') as f:
    for line in f.read().splitlines():
        match = regex.search(line)
        if match:
            word = match.group(1)      # or use: this is faster
            if not word in result:     # try:
                result[word] = 0       #    result[word] += 1 
            result[word] += 1          # except KeyError:
                                       #    events[event_name] = 1

for key, value in result.items():
    print(f"The massage {key} was thrown {value} times.")
   