import re

# Reg Ex: IPv4 Adresse als eigenständiges Wort
regex = r"\b(\d{1,3}\.){3}\d{1,3}\b"

fname = "/home/coder/Workspace/kurse_python_f/Materialien/SampleLog.log"
test_str = open(fname).read()
matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

print("-" * 80)

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print (f"Match {matchNum:<5} : {match.group():>20}")    # linksbündig und rechtsbündig
     