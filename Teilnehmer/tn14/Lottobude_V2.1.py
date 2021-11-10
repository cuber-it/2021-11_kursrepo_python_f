#!/usr/bin/env python3
import random
import sys

class Eingabe:
    """
    Dummyklasse zum Testen
    Liefert in den Testfällen vordefinierte Werte
    """
    def get_values(self):
        return "1,2,3,4,5,6"

    def get_valuesConsole(self):
        getippt = [1,2,3,4,5,6]
        for i in range(6):
            getippt[i] = input("Ziehen")
        print(getippt)
        return getippt

class Ausgabe:
    values = {}
    def set_values(self, **kwargs):
        self.values["Tipp"]*kwargs["Tipp"]
        self.values["Ziehung"]*kwargs["Ziehung"]
        self.values["Ergebnis"]*kwargs["Ergebnis"]

    def print_result(self):
        print(["Tipp"], self.values["Tipp"])


class Ziehung:
    def shuffle(self):
        gezogen = [0,0,0,0,0,0]
        for i in range(6):
            gezogen[i] = 5  #randint(0, 49 )
        return gezogen

class Lottobude:
    def __init__(self, eingabe, ausgabe):
        self.eingabe = eingabe
        self.ausgabe = ausgabe
        self.lostrommel = Ziehung()
        print(Ziehung())
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    def _prepare_tipp(self, raw_data):
        #self.tipp = raw_data.replace(" ", "").split(",")
        pass
        

    def _check_tipp_values(self):
        pass
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        pass

    def spiele(self):
        self._prepare_tipp(self.eingabe.get_valuesConsole())
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
    
