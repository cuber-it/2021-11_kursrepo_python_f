#!/usr/bin/env python3
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
    values = {}
    def set_values(self, **kwargs):
        pass

    def print_result(self):
        pass


class Ziehung:
    def shuffle(self):
        draw = random.sample(range(1,50), 6)
        return draw

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
        # Inhalte von Liste "tipp" in int konvertieren
        for number in range(0, len(self.tipp)):
            self.tipp[number] = int(self.tipp[number])
        
    def _check_tipp_values(self):
        for number in self.tipp:
            if not 1 <= number <= 49:
                raise RuntimeError("Fehler! Es sind nur Zahlen von 1 bis 49 erlaubt.", number)

    def _compare(self):
        self.ergebnis = list(set(self.tipp).intersection(set(self.ziehung)))

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
    
