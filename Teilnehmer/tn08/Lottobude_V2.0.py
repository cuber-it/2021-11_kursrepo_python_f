#! /usr/bin/eny python3

import random

class Eingabe:
    pass

class Ausgabe:
    def set_values(self, **kwargs)
        pass

class Ziehung:
    def shuffle(self)
        pass

class Lottobude:
    def __init__(self):
        self.eingabe = Eingabe()
        self.ausgabe = Ausgabe()
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    def _prepare_tipp(self, raw_data):
        pass

    def _check_tipp_values(self):
        pass

    def _compare(self):
        pass

    def spiel(self):
        self._prepare_tipp(self.eingabe.get_values())
        self.ziehung = self.lostrommel.shuffle()
        self._compare()
        return self

    def print(self):
        self.ausgabe.set_values(self.tipp,)

if __name__ == "__main__":
    lb = Lottobude(Eingabe(), Ausgabe())
    lb.spiele().print_results()