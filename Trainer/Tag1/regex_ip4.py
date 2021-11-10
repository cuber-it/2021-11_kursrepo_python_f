import re

def matcher(text, to_str=False):
    regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    matches = re.finditer(regex, text, re.MULTILINE)
    result = matches
    if to_str:
        result = []
        for matchNum, match in enumerate(matches, start=1):
            result.append("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                result.append("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
        result = "\n".join(result)
    return result     
    

if __name__ == "__main__":
    t = "BlaBla 127.0.0.1 Bla Bla"

    m = matcher(t)
    print(type(m))

    s = matcher(t, to_str=True)
    print(type(s))