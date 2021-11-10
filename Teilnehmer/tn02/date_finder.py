# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^(\d{2})\/(\d{2})\/(\d{4})"

test_str = ("06/02/2020, $323.34, 21910700, $320.745, $323.44, $318.93\n"
	"06/01/2020, $321.85, 20254650, $317.75, $322.35, $317.21\n"
	"05/29/2020, $317.94, 38399530, $319.25, $321.15, $316.47")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    if len
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


