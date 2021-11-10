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
        for key, value in kwargs.items():
            self.values[key]=value

    def print_result(self):
        for entry in self.values:
            print(self.values[entry])

class Ziehung:
    def ziehung(self):
        return random.sample(range(1,50), 6)

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
        if len(self.tipp)==6:
            self.tipp=[int(x) for x in self.tipp]

    def _compare(self):
        """
        Vergleich von ziehung und eingabe
        """
        self.ergebnis=list(set(self.tipp).intersection(self.ziehung))

    def spiele(self):
        self._prepare_tipp(self.eingabe.get_values())
        self.ziehung = self.lostrommel.ziehung()
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
    #Lottobude(Eingabe(), Ausgabe()).print()
    
