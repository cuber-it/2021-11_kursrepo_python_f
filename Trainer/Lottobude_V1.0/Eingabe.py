class Eingabe:
    def __init__(self):
        self.daten = None

    def __zerlege(self):
        return self.daten.split(",") # wird nicht vererbt, echt privat

    def _aufbereitung(self): # Vererbbar! Wenn __aufbereitung -> das wäre nicht vererbt worden!
        self.daten = self.__zerlege()

    def einlesen(self):
        self.daten = input("Tippdaten eingeben:" )
        self._aufbereitung()
        return self

class DateiEingabe(Eingabe): # Erbt von Eingabe
    def einlesen(self, fname):
        with open(fname) as fd:
            self.daten = fd.readline()
        self._aufbereitung() # nutzung der geerbten Funktionalität
        return self


if __name__ == "__main__":
    print(Eingabe().einlesen().daten)
    print(DateiEingabe().einlesen("/home/coder/Workspace/aktueller-kurs/Trainer/Lottobude/testdaten.txt").daten)

