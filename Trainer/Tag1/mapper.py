def machwas(fp, daten):
    result = []
    for v in daten:
        result.append(fp(v))
    return result



l = [ 1,2,3,4]
print(machwas(lambda x: x * x, l))
print(machwas(lambda x: str(x), l))
print(machwas(lambda x: x - 10, l))

x_werte = [ {"NAME": "Willi"}, {"NAME": "Heinz"}, {"NAME": "Klaus"}]
print(machwas(lambda x: x["NAME"] if "i" in x["NAME"] else None, x_werte))


wert = 42
frage = "Alles" if wert == 42 else "Weiss nicht"
print(frage)

if wert == 42:
    frage = "Alles"
else:
    frage = "Weiss nicht"