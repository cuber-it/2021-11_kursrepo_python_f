daten = [1, 2, 3, 4, 5, 6]

dummy = lambda x: "Hello"

x5 = lambda x: x * 5 # "anonyme/wegwerf-Funktion", weil kein def genommen wurde, mit x5 als Variable verbunden

def mal_10(wert): # reguläre Funktion
    return wert * 10

for e in map(dummy, daten): #
    print(e)

print("-"*80)

for e in map(x5, daten):
    print(e)

print("-" * 80)

for e in map(mal_10, daten):
    print(e)

print("-" * 80)

for e in map(lambda x: x ** x, daten): # lambda ist sofort danach vergessen!!!
    print(e)



d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
print(d.items())
s1 = sorted(d.items()) # Standardmässig sortiert er nach dem 1. Element der Tupel
print(s1)
s2 = sorted(d.items(), key=lambda x: x[1])
print(s2)

d = {
     "Pierre": { "Alter":42, "Einkommen": 40000 }, 
     "Anne": {"Alter": 33, "Einkommen": 300000}, 
     "Zoe": {"Alter":24, "Einkommen": 15000}
    }
print(d.items())
s3 = sorted(d.items())
print(s3)
s4 = sorted(d.items(), key=lambda x: x[1]["Einkommen"])
print(s4)