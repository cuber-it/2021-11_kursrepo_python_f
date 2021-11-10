class Eingabe:
    def __init__(self):
        self.daten = None

    def _aufbereitung(self):
        self.daten =self.daten.split(",")

    def einlesen(self):
        self.daten = input("Tippdaten eingeben:")
        self._aufbereitung()
        return self
    
class DateiEingabe(Eingabe):
    pass

if __name__ = "__main__":
    eingabe = DateiEingabe().einlesen("Dateiname.txt")
    print(eingabe.daten)