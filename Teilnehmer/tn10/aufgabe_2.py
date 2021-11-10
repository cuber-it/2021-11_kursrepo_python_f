#!/usr/bin/env python3
import sys
import os
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r".([A-Z]+).*?:"

test_str = ("03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp\n"
	"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.67.101.1, entity for rsvp allocated and initialized\n"
	"03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot for RSVP\n"
	"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.