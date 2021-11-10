#!/usr/bin/env python3
import random

class Eingabe:
    """
    Dummyklasse zum Testen
    Liefert in den Testfällen vordefinierte Werte
    """
    def get_values(self):
        return "1,2,3,4,5,6"

class Ausgabe:
    _values = {}
    def set_values(self, **kwargs):
        _values = kwargs
        return self

    def print_result(self):
        for k, v in self._values.items():
            print( k, v)
        return self


class Ziehung:
    def shuffle(self):
        lottozahlen = random.sample(range(1,50), 6)
        return lottozahlen

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
        try:
            tipps = []
            for i in self.tipp:
                tipps.append(int(i))
            self.tipp = tipps
            return self
        except ValueError:
            print("Could not convert data to an integer.")
        

    def _check_tipp_values(self):
        if(len(self.tipp) != 6):
            raise RuntimeError
        if(len(set(self.tipp)) != 6):
            raise RuntimeError
        for i in self.tipp:
            if(type(i) != int):
                raise RuntimeError
        return self
        
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        erg = []
        for i in self.tipp:
            erg.append(i)
        for i in self.eingabe:
            erg.append(i)
        self.ergebnis = list(set(erg))
        return self

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
        return self



if __name__ == "__main__":
    Lottobude(Eingabe(), Ausgabe()).spiele().print()
    
