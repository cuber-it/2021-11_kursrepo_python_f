import re

regex = r"\s([A-Z]*)\s*\:"

test_str = ("03/22 08:51:06 TRACE  :...read_physical_netif: Home list entries returned = 7\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #1, interface TR1 has address 9.37.65.139, ifidx 1\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #2, interface LINK11 has address 9.67.100.1, ifidx 2\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #3, interface LINK12 has address 9.67.101.1, ifidx 3\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #4, interface CTCD0 has address 9.67.116.98, ifidx 4\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #5, interface CTCD2 has address 9.67.117.98, ifidx 5\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #6, interface LOOPBACK has address 127.0.0.1, ifidx 0\n"
	"03/22 08:51:06 INFO   :....mailslot_create: creating mailslot for timer\n"
	"03/22 08:51:06 INFO   :...mailbox_register: mailbox allocated for timer\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 129.1.1.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP")

matches = re.finditer(regex, test_str, re.MULTILINE)
events = {}
for matchNum, match in enumerate(matches, start=1):
    event = match.group(1)
    if event in events:
        current = events.get(event)
        new = current + 1
        events[event] = new
    else: events[event] = 1
print(events)