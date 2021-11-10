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
        return "1,2,3,4,5,6"

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    values = {}
    def set_values(self, **kwargs):
        pass

    def print_result(self):
        pass


class Ziehung:
    def shuffle(self):
        return []

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
        if len(self.tipp)!=6:
            return self.tipp
        
    def _check_tipp_values(self):
        pass
        # Bei Fehler raise RuntimeError!

    def _compare(self):
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
    
