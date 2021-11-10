class Basis:
    def __init__(self):
        self._daten = "Basiswert"

    def aktion(self):
        print(self._daten)

class Kind1(Basis):
    def set_daten(self, wert):
        self._daten = wert

class Kind2(Basis):
    pass

class Enkel1(Kind1):
    def count_letters(self):
        print(len(self._daten))

class Enkel2(Kind1, Kind2): # Mehrfachvererbung, möglich, manchmal ok, oft aber Quelle grösserer Probleme
    pass


if __name__ == "__main__":
    o = Basis()
    o.aktion()

    k = Kind1()
    k.set_daten("Kindwert")
    k.aktion()

    e = Enkel1()
    e.set_daten("Enkelwert")
    e.aktion()
    e.count_letters()

