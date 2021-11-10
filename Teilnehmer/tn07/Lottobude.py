#!/usr/bin/env python3
import random

class Eingabe:
    """ 
    Dummyklasse zum Testen
    Liefert in den Testfällen vordefinierte Werte
    """
    def get_values(self):
        #input_string = input("Gib einen Tipp ab: ")
        input_string = "1,2,3,4,5,6"
        return input_string

class UserEingabe:

    def get_values(self):
        input_string = input("Gib einen Tipp ab (6 Zahlen mit Komma getrennt): ")
        return input_string     

class DateiEingabe:
    def __init__(self, fname):
        self.fname = fname

    def get_values(self):
        with open(self.fname) as fd:
            input_string = fd.readline()
            return input_string

class Ausgabe:
    _values = {}
    def set_values(self, **kwargs):
        self._values = kwargs

    def print_result(self):
        for value in self._values:
            print(f"{value:10} \t\t{self._values[value]}")


class Ziehung:
    def shuffle(self):
        return random.sample(range(1, 50), 6)

class Lottobude:
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
        result = [] # Copy-Problem
        if not len(raw_data) == 6:
            raise RuntimeError("Invalid length: ", raw_data) 
        for n in raw_data:
            try:
                n = int(n)
            except TypeError:
                raise RuntimeError("Invalid type: ", n)
            if not (n > 0 and n < 50):
                raise RuntimeError("Invalid value: ", n)
            elif n in result:
                raise RuntimeError("Double value: ", n)
            else:
                result.append(n)
        return result

    def _compare(self):
        self.ergebnis = list((set(self.tipp)).intersection(set(self.ziehung)))

    def spiele(self):
        self._prepare_tipp(self.eingabe.get_values())
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
    Lottobude(DateiEingabe('Tipp.txt'), Ausgabe()).spiele().print()