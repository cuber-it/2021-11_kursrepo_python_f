#!/usr/bin/env python3
class Adder:
    def __init__(self): # wird immer bei Objektanlage aufgerufen, bereitet das Objekt vor
        self._werte = [] # self bedeutet, dass das Elemnt zu dieser Klasse und zu dem speziellen Objekt gehört

    def __str__(self): # wird immer aufgerufen, wenn das Objekt in einen String-Kontext kommt
        return str(self._werte)

    # die Objektschnittstelle, das Objekt-API
    def push(self, value): # Eingabe
        self._werte.append(value)

    def add(self): # Verarbeitung
        if len(self._werte) >= 2:
            erg = self._werte[-1] + self._werte[-2]
            self._werte[-2] = erg
            del self._werte[-1]
        else:
            raise Exception("No valid number of values")

    def pop(self): # Ausgabe
        erg = None
        if len(self._werte) >= 1:
            erg = self._werte[-1]
            del self._werte[-1]
        else:
            raise Exception("No valid number of values")
        return erg

# fürs testen:
if __name__ == "__main__": # wird nicht ausgeführt wenn mit import geladen
    a = Adder() # Objektanlage, absieren auf Klasse und dort __init__-Methode

    a.push(5)
    print(a) # print ist ein String-Kontext, für a wird dann implizit a.__str__() aufgerufen
    a.push(10)
    print(a) # print(str(a)) -> print(a.__str__())
    a.add()
    print(a)
    e = a.pop()
    print(a)
    print(e, e == (10+5))
    a.push(7)
    a.add()
