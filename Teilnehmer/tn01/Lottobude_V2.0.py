#!/usr/bin/env python3
"""
Bibliothek für eine einfache Lotterie 6 aus 49
"""
import random

class Eingabe:
    """
    Dummyklasse zum Testen
    Liefert in den Testfällen vordefinierte Werte
    """
    def get_values(self):
        """
        get_values: Liefert Benutzereingabe zurück

        Hier nur simuliert mit feststehendem Wert

        @parameters: Keine
        @returns: string
        """
        tipp = random.sample(range(1, 47), 6)
        tipp_string = f"{tipp[0]},{tipp[1]},{tipp[2]},{tipp[3]},{tipp[4]},{tipp[5]}"
        return tipp_string

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    def __init__(self):
        self.values = {}
    def set_values(self, Tipp, Ziehung, Ergebnis):
        self.values  = {"Tipp": Tipp,
                   "Ziehung": Ziehung,
                   "Ergebnis": Ergebnis}

    def print_result(self):
        print(self.values)


class Ziehung:
    def shuffle(self):
        return random.sample(range(1, 47), 6)

class Lottobude:
    def __init__(self, eingabe, ausgabe):
        self.eingabe = eingabe
        self.ausgabe = ausgabe
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    def _prepare_tipp(self, raw_data):
        str_list = raw_data.replace(" ", "").split(",")
        self.tipp = [int(i) for i in str_list]
        

    def _check_tipp_values(self):
        # Bei Fehler raise RuntimeError!
        assert isinstance(self.tipp, list)
        assert len(self.tipp) == 6
        assert all(isinstance(x, int) for x in self.tipp)
        assert len(set(self.tipp)) == 6
        # @todo: correct range

    def _make_tipp_values_set(self):
        self.tipp = set(self.tipp)

    def _compare(self): 
        self.ergebnis = self.tipp.intersection(self.ziehung)


    def spiele(self):
        self._prepare_tipp(self.eingabe.get_values())
        self._check_tipp_values()
        self._make_tipp_values_set()
        self.ziehung = set(self.lostrommel.shuffle())
        self._compare()
        return self

    def print(self):
        self.ausgabe.set_values(
            Tipp=self.tipp, 
            Ziehung=self.ziehung, 
            Ergebnis=self.ergebnis)
        self.ausgabe.print_result()


if __name__ == "__main__":
    Lottobude(Eingabe(), Ausgabe()).spiele().print()



