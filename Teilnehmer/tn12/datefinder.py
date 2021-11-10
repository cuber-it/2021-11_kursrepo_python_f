# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import datetime

regex = r"^(\d{2})\/(\d{2})\/(\d{4})"

test_str = ("Date, Close/Last, Volume, Open, High, Low\n"
	"06/02/2020, $323.34, 21910700, $320.745, $323.44, $318.93\n"
	"06/01/2020, $321.85, 20254650, $317.75, $322.35, $317.21\n"
	"05/29/2020, $317.94, 38399530, $319.25, $321.15, $316.47\n"
	"05/28/2020, $318.25, 33449100, $316.77, $323.44, $315.63\n"
	"05/27/2020, $318.11, 28236270, $316.14, $318.71, $313.09\n"
	"05/26/2020, $316.73, 31380450, $323.5, $324.24, $316.5\n"
	"05/22/2020, $318.89, 20450750, $315.77, $319.23, $315.35\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

    if len(match.groups()) == 3:
        mon = int(match.group(1))
        day = int(match.group(2))
        year = int(match.group(3))
        date = datetime.datetime(year, mon, day)
        print(f"{day} {mon} {year}")
        print(f"{date}")

 