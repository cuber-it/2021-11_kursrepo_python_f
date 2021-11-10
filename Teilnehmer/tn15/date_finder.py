#! /usr/bin/env python3
import re
import datetime

regex = r"^(\d{2})\/(\d{2})\/(\d{4})"

test_str = ("06/02/2020, $323.34, 21910700, $320.745, $323.44, $318.93\n"
	"06/01/2020, $321.85, 20254650, $317.75, $322.35, $317.21\n"
	"05/29/2020, $317.94, 38399530, $319.25, $321.15, $316.47\n"
	"05/28/2020, $318.25, 33449100, $316.77, $323.44, $315.63\n"
	"05/27/2020, $318.11, 28236270, $316.14, $318.71, $313.09")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    if len(match.groups()) == 3:
        mon = int(match.group(1))
        day = int(match.group(2))
        year = int(match.group(3))
        date = datetime.datetime(year, mon, day)
        print(f"{day} {mon} {year}")
        print(f"{date}")

        print(f"{day} {mon} {year}")

    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("\tGroup {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))