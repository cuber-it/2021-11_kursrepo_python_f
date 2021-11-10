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

class UserEingabe:
    def get_values(self):
        return input("Ihre Tippeingabe (6 Zahln, Kommagetrennt): ")

class DateiEingabe:
    def __init__(self, fname):
        self.fname = fname

    def get_values(self):
        with open(self.fname) as fd:
            return fd.readline()

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    _values = {}
    def set_values(self, **kwargs):
        self._values = kwargs

    def print_result(self):
        for k, v in self._values.items():
            print(f"{k:<15}: {sorted(v)}")


class Ziehung:
    def shuffle(self):
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
        raw_data = raw_data.replace(" ", "").split(",")
        self._check_len(raw_data)
        result = []
        for n in raw_data:
            value = self._convert_to_int(n)
            self._check_is_in_range(value)
            self._check_is_no_dup(value, result)
            result.append(value)
        self.tipp = result

    def _check_is_no_dup(self, value, values):
        if value in values:
            raise RuntimeError("Duplicate Value: ", value)

    def _check_len(self, values):
        if not len(values) == 6:
            raise RuntimeError("Invalid length: ", values)

    def _convert_to_int(self, value):
        try:
            return int(value)
        except TypeError:
            raise RuntimeError("Invalid type: ", value)

    def _check_is_in_range(self, value):
        if not (1 <= value <= 49):
            raise RuntimeError("Invalid value: ", value)
    
    def _compare(self):
        self.ergebnis = list(set(self.tipp).intersection(set(self.ziehung)))

    def spiele(self):
        self._prepare_tipp(self.eingabe.get_values())
        self.ziehung = self.lostrommel.shuffle()
        self._compare()
        
    def print(self):
        self.ausgabe.set_values(
            Tipp=self.tipp, 
            Ziehung=self.ziehung, 
            Ergebnis=self.ergebnis)
        self.ausgabe.print_result()


if __name__ == "__main__":
    lb = Lottobude(DateiEingabe("tipp.txt"), Ausgabe())
    lb.spiele()
    lb.print()
    
