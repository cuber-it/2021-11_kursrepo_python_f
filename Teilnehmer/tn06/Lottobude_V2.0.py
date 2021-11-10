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
        return "1,1,3,4,5,6"

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    values = {}
    def set_values(self, **kwargs):
        self.values = kwargs
        pass

    def print_result(self):
        print(f"Tipp: {self.values['Tipp']}")
        print(f"Ziehung: {self.values['Ziehung']}")
        print(f"Ergebnis: {self.values['Ergebnis']}")
        pass


class Ziehung:
    def shuffle(self):
        return random.sample(range(1,50),6)

class Lottobude:
    def __init__(self, eingabe, ausgabe):
        self.eingabe = eingabe
        self.ausgabe = ausgabe
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    def _prepare_tipp(self, raw_data):
        self.tipp = raw_data.replace(" ", "").split(",")
        self.tipp = [int(tipp) for tipp in self.tipp]


    def _check_tipp_values(self):
        doppelte = list(set(self.tipp) & set(self.tipp))
        print(doppelte)
        try:
            if not len(doppelte) == 0:
                raise RuntimeError ("Doppelte")
        except RuntimeError as err:
            print("RuntimeError", err)
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        sorted_tipp = self.tipp.copy()
        sorted_tipp.sort()
        sorted_ziehung = self.ziehung.copy()
        sorted_ziehung.sort()
        #print(set(sorted_tipp) & set(sorted_ziehung))
        #print(sorted_tipp[0])
        for i in range(6):
            if sorted_tipp[i] == sorted_ziehung[i]:
                self.ergebnis.append(sorted_ziehung[i])
        pass

    def spiele(self):
        self._prepare_tipp(self.eingabe.get_values())
        self._check_tipp_values()
        self.ziehung = self.lostrommel.shuffle()
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
    
