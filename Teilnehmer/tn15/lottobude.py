#! /usr/bin/env python3
import random

class Eingabe:
    """
    Dummyklasse zum Testen
    Liefert in den Testfällen vordefinierte Werte
    """
    def get _values(self):
        return "1,2,3,4,5,6"

class Ausgabe:
    values = {}
    def set_values(self, **kwargs)
        pass

    def print_result(self)
        pass

class Ziehung:
    def shuffle(self):
        return 0

class Lottobude:
    def __init__(self, eingabe, ausgabe):
        self.eingabe = eingabe
        self.ausgabe = ausgabe
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []

    def _prepare_tipp(self, raw_data):
        self.tipp = raw_data.replace("", "").split(",")
        self._check_tipp_values()

    def _check_tipp_values(self):
        pass
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        pass

    def spiele(self):
        eingabe = self.eingabe.get_values()
        self._prepare_tipp(eingabe)
        self._check_tipp_values()
        self.ziehung= self.lostrommel.shuffle()
        self._compare()
        return self
    
    def print(self):
        self.ausgabe.set_values(
            tipp = self.tipp,
            ziehung = self.ziehung,
            ergebnis = self.ergebnis
            ).print_result()
        print("Tipp:     ", self.tipp)
        print("Ziehung:  ", self.ziehung)
        # print("Treffer:  ")


if __name__ == "__main__":
    Lottobude().spiele().print()