# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r" ([A-Z]+) *?:"

test_str = ("03/22 08:51:01 INFO   :.main: *************** RSVP Agent started ***************\n"
	"03/22 08:51:01 INFO   :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf\n"
	"03/22 08:51:01 INFO   :.main: Using log level 511\n"
	"03/22 08:51:01 INFO   :..settcpimage: Get TCP images rc - EDC8112I Operation not supported on socket.\n"
	"03/22 08:51:01 INFO   :..settcpimage: Associate with TCP/IP image name = TCPCS\n"
	"03/22 08:51:02 INFO   :..reg_process: registering process with the system\n"
	"03/22 08:51:02 INFO   :..reg_process: attempt OS/390 registration\n"
	"03/22 08:51:02 INFO   :..reg_process: return from registration rc=0\n"
	"03/22 08:51:06 TRACE  :...read_physical_netif: Home list entries returned = 7\n"
	"03/22 08:51:06 INFO   :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.