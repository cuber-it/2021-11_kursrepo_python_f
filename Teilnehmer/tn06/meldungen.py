import re
import sys
import pprint

def parseFile(file):
    #print(file)
    f = open(file, "r")
    events = {}
    regex = r" ([A-Z]+) *:"
    matches = re.finditer(regex, f.read(), re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if match.group(1) in events:
                events[match.group(1)] = events[match.group(1)]+1
            else:
                events[match.group(1)] = 1
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    return events

def main():
    print("meldungen")
    f = ""
    if len(sys.argv) == 2:
        f = sys.argv[1]  
    else:
        print("Error File needed")
        sys.exit(1)

    file_events = parseFile(f)
    pprint.pprint(file_events)

if __name__ == "__main__":
    main()