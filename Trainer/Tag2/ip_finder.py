import re

fname = "/home/coder/Workspace/kurse_python_f/Materialien/SampleLog.log"
test_str = open(fname).read()

# Reg Ex: ip4-Adresse als eigenständiges Wort
regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print(f"Match {matchNum:<5}:  {match.group():>20}") # seit 3.6, eleganteste Methode mit f-Stringmodifier
    #print("Match ", matchNum, ": ", match.group())  # für simpelste Ausgaben
    #print("Match %s: %s" % matchNum, match.group()) # ganz alter 2.7 Stil, wird nicht mehr benutzt
    #print("Match {}: {}".format(matchNum, match.group())) # neuert 3.x Stil mit format-Methode
    
