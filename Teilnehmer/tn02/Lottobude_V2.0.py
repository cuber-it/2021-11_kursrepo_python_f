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
        input_string = input("Bitte Lottozahlen eingeben: ")
        return input_string

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    values = {}
    def set_values(self, **kwargs):
        self.values = kwargs

    def print_result(self):
        print("--------------------")
        print("Tipp:")
        print(*self.values["Tipp"], sep=", ")
        print("Ziehung:")
        print(*self.values["Ziehung"], sep=", ")
        print("Ergebnis: %s" % self.values["Ergebnis"])

class Ziehung:
    def shuffle(self):
        numbers = set()
        while len(numbers)<=6:
            numbers.add(random.randint(1,49))
        return [str(n) for n in sorted(numbers)]

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
        

    def _check_tipp_values(self):
        try:
            if len(self.tipp)!=6:
                raise RuntimeError("Falsche Anzahl von abgegebenen Zahlen!")
            for n in self.tipp:
                if int(n)<0 or int(n)>49:
                    raise RuntimeError("Zahl außerhalb des gültigen Bereichs!")        
        except TypeError:
            raise RuntimeError("Nur Integer-Zahlen eingeben!")
        # Bei Fehler raise RuntimeError!

    def _compare(self):
        if self.tipp == self.ziehung:
            self.ergebnis = "Gewonnen!!! :-)"
        else:
            self.ergebnis = "Verloren... :-("

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
    
