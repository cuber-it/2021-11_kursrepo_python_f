
txt = """Strasse,    Hausnummer,    PLZ,    Ort
Aachener Straße,    131,    40223,    Düsseldorf
ABC-Straße,    21,    20354,    Hamburg
Abteistr.,    17-19,    45239,    Essen
Abteistr.,    20,    45239,    Essen
Adalbert-Eisenhuth-Straße,    17,    63457,    Hanau
Adalbertstr. ,   023B,    10997,    Berlin
Achtern Höben,    3,    21465,    Wentorf bei Hamburg
Ackerstraße,    14-15,    10115,    Berlin"""

result = []
lines = txt.splitlines()
header = lines[0].replace(" ", "").split(",")
result.append(header)
for line in lines[1:]:
    line = [v.strip() for v in line.split(",")]
    if "-" in line[1]:
        von, bis = line[1].split("-")
        for hnr in range(int(von), int(bis)+1):
            newline = line.copy()
            newline[1] = hnr
            result.append(newline)
    else:
        result.append(line)

import pprint
pprint.pprint(result)
    
