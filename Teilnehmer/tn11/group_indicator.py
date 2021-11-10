import re
import os
import glob

regex = r" ([A-Z]+)( +):"

IN_PATH="/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt"

#test_str = ("03/22 08:54:22 TRACE  :........flow_timer_start: Start T4\n"
#	"03/22 08:54:22 TRACE  :.......rsvp_flow_stateMachine: reentering state RESVED\n"
#	"03/22 08:54:24 EVENT  :..mailslot_sitter: process received signal SIGALRM\n"
#	"03/22 08:54:24 TRACE  :.....event_timerT1_expire: T1 expired\n"
#	"03/22 08:54:24 INFO   :......router_forward_getOI: Ioctl to query route entry successful\n"
#	"03/22 08:54:24 TRACE  :......router_forward_getOI:         source address:   9.67.116.98\n"
#	"03/22 08:54:24 TRACE  :......router_forward_getOI:         out inf:   9.67.116.98\n"
#	"03/22 08:54:24 TRACE  :......router_forward_getOI:         gateway:   0.0.0.0\n"
#	"03/22 08:54:24 TRACE  :......router_forward_getOI:         route handle:   7f5251c8")

#matches = re.finditer(regex, test_str, re.MULTILINE)

#file = open(IN_PATH)
#line = file.read().replace("\n", " ")
#file.close()

with open(IN_PATH) as input_file:
    text=input_file.read().replace("\n"," ")

matches = re.finditer(regex, text, re.MULTILINE)

exact_matches={}
for matchNum, match in enumerate(matches, start=1):
    if match.group(1) in exact_matches.keys():
        exact_matches[match.group(1)]+=1
    else:
        exact_matches[match.group(1)]=1

for key, value in exact_matches.items():
    print(key,value)

    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #print(match.group(1))
    #for groupNum in range(0, len(match.groups())):
        #print(match.group(groupNum))

        #groupNum = groupNum + 1
        
        #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
