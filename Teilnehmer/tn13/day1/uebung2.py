# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import pprint as pp

regex = r"([A-Z]+) *?:"

test_str = ("03/22 08:51:06 INFO   :...read_physical_netif: index #6, interface LOOPBACK has address 127.0.0.1, ifidx 0\n"
	"03/22 08:51:06 INFO   :....mailslot_create: creating mailslot for timer\n"
	"03/22 08:51:06 INFO   :...mailbox_register: mailbox allocated for timer\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 129.1.1.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP via UDP\n"
	"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.37.65.139, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp")

matches = re.finditer(regex, test_str, re.MULTILINE)

matchlist = []
for matchNum, match in enumerate(matches):
    matchlist += [match.group(1)]

matchdict = {}

for i in range(len(matchlist)):
    try: 
        matchdict[matchlist[i]]
        matchdict[matchlist[i]] += 1
    except KeyError: 
        matchdict[matchlist[i]] = 1

pp.pprint(matchdict)