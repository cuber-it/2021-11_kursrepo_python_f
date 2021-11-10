#!/usr/bin/env python3
"""
Bibliothek für eine einfache Lotterie 6 aus 49
"""
import random
import pdb
import numpy

class Eingabe:
    def __init__(self):
        self.tipp = None
    
    def get_values(self):
        self.tipp = "1,2,3,4,5,6"
        #self.data = input('6 Zahlen eingeben, komma-separiert bitte: ')
        return self

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    values = {}

    def set_values(self, Tipp, Ziehung, Ergebnis):
        self.tipp = Tipp
        self.ziehung = Ziehung
        self.ergebnis = Ergebnis

    def print_result(self):
        # self.richtige = sum(self.ergebnis)
        if self.ergebnis == 0: print('leider nichts gewonnen, die Bank gewinnt!')
        if self.ergebnis != 0: print('%d richtige Zahlen, Glückwunsch!'%self.ergebnis)
        return self
    
class Ziehung:
    def shuffle(self):
        return random.sample(range(1,50), 6)


class Lottobude:
    def __init__(self):
        self.eingabe = Eingabe()
        self.ausgabe = Ausgabe()
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    def _prepare_tipp(self):
        self.tipp = self.eingabe.tipp.replace(" ", "").split(",")
        self.tipp = [int(number) for number in self.tipp]
        

    def _check_tipp_values(self):
        pass
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        ziehung_sorted = numpy.sort(self.ziehung)
        data_sorted = numpy.sort(self.tipp)
        for i in range(len(ziehung_sorted)):
            self.ergebnis.append(ziehung_sorted[i] == data_sorted[i])
        self.ergebnis = sum(self.ergebnis)
        return(self)


    def spiele(self):
        self.eingabe.get_values()
        self._prepare_tipp()
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
        return self


if __name__ == "__main__":
    Lottobude().spiele().print()

