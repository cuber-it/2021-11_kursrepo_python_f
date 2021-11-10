#!/usr/bin/env python3
import random

class Eingabe:
    """
    Dummyklasse zum Testen
    Liefert in den Testfällen vordefinierte Werte
    """
    def get_values(self):
        return "6,2,3,4,5,1"

class Ausgabe:
    values = {}
    def set_values(self, **kwargs):
        #print('K',kwargs)
        self.values['Tipp']=kwargs['Tipp']
        self.values['Ziehung']=kwargs['Ziehung']
        self.values['Ergebnis']=kwargs['Ergebnis']

    def print_result(self):
        print("Tipp:     ",self.values["Tipp"])
        print("Ziehung:  ",self.values["Ziehung"])
        print("Ergebnis: ",self.values["Ergebnis"])


class Ziehung:
    def shuffle(self):
        return random.sample(range(1,50), 6).sort()
        

class Lottobude:
    ergebnis = None
    def __init__(self, eingabe, ausgabe):
        self.eingabe = eingabe
        self.ausgabe = ausgabe
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    def _prepare_tipp(self, raw_data):
        raw_data = raw_data.replace(" ", "").split(",")
        self.tipp = self._check_tipp_values(raw_data) 

    def _check_tipp_values(self, raw_data):
        tipp_zahlen=raw_data.copy()
        if len(tipp_zahlen) != 6:
            raise RuntimeError("Kein gültiger Tipp, 6 Zahlen bitte")
        while len(tipp_zahlen) > 0:
            x=tipp_zahlen.pop()
            try:
                i=int(x)
            except TypeError:
                raise RuntimeError("Kein gültiger Tipp, nur Ganzzahlen bitte")
            if x in tipp_zahlen:
                raise RuntimeError("Kein gültiger Tipp, Zahlen sind doppelt")
            if (i < 1) or (i > 49):
                raise RuntimeError("Kein gültiger Tipp, nur Zahlen zw 1 und 49 erlaubt")
        return raw_data
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        treffer=0
        for x in self.tipp:
            if x in self.tipp:
                treffer += 1
        self.ergebnis=treffer            

    def spiele(self):
        self._prepare_tipp(self.eingabe.get_values())
        #print('T',self.tipp)
        #self._check_tipp_values()
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
    
