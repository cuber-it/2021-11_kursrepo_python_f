class X:
    def __init__(self, v):
        self._v = v

    def get(self):
        return self._v

    def set(self, v):
        self._v = v


def obj_erzeuger(wert):
    return X(wert)

anzahl = int(input("Wieviele Objekte: "))

objekte = []
for n in range(0, anzahl):
    objekte.append(obj_erzeuger(n))

print("Anzahl: ", len(objekte))

for n in objekte:
    print(n.get())