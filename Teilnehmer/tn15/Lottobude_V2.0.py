#!/usr/bin/env python3
"""
Bibliothek for eine einfache Lotterie 6 aus 49
"""
import random

# Erzeugt die Eingabe
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

# Eingabe per Abfrage, MEthode get_values notwendig durch aufbau von spiel
class UserEingabe:
    def get_values(self):
        return input("Ihre Tippeingabe (6 Zahlen, Kommagetrennt): ")

class DateiEingabe:
    def __init__(self, fname):
        self.fname = fname

class Ausgabe:
    # Damit es nicht zu Aufruffehlern vor Wertebelegung kommt
    values = {}
    def set_values(self, **kwargs):
        self._values = kwargs

    def print_result(self):
        for k, v in self._values.items():
            print(f"{k:<15}: {sorted(v)}")

class Ziehung:
    def shuffle(self):
        return random.sample(range(1,50), 6)

class Lottobude:
    # Initialisierung
    def __init__(self, eingabe, ausgabe):
        self.eingabe = eingabe
        self.ausgabe = ausgabe
        self.lostrommel = Ziehung()
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []

    # Erste Methode, privat, verarbeitet die Lottoeingabe für die ausgabe
    def _prepare_tipp(self, raw_data):
        raw_data = raw_data.replace(" ", "").split(",") # lösche alle leerzeichen
        self._check_len(raw_data) # prüfe ob 6 zahlen
        result = [] # Initialisierung des ergebnisses
        for n in raw_data: # überprüfe jede zahl einzeln
            value = self._convert_to_int(n) # mache zu integer
            self._check_is_in_range(value) # überprüfe ob zwischen 1 und 49
            self._check_is_no_dup(value, result) # überprüfe ob doppelte vorliegen
            result.append(value) # hänge des ergebnis an result an
        self.tipp = result # warum wird result nicht direkt referenziert?
    
    # zweite Methode, privat, erhält eine zahl aus den resultaten und schaut ob das in der liste aller eingaben liegt? warum ist das nicht immer true?
    # values is die liste der bereits überprüften eingabewerte - d.h. es startet mit einer leeren liste
    def _check_is_no_dup(self, value, values):
        if value in values:
            raise RuntimeError("Duplicate Value: ", value)
    
    # Dritte Methode, privat, erhält die gesamte eingabe und überprüft, ob diese 6 zahlen lang ist
    def _check_len(self, values):
        if not len(values) == 6:
            raise RuntimeError("Invalid length: ", values)

    # Vierte Methode, privat, erhält einen Wert und versucht diesen in einen integer umzuwandeln
    def _convert_to_int(self, value):
        try:
            return int(value)
        except TypeError:
            raise RuntimeError("Invalid value: ", value)
    
    # Fünfte Methode, bekommt einen wert und prüft, ob dieser zwischen 1 und 49 liegt
    # Anmerkung: da wert in int umgewandelt wurde, ist die abfrage 1 <= überflüssig? wahrscheinlich besser lesbar hier
    def _check_is_in_range(self, value):
        if not (1 <= value <= 49):
            raise RuntimeError("Invalid value: ", value)

    # def _check_tipp_values(self):
    #     pass
    #     # Bei Fehler raise RuntimeError!

    # Sechste Methode, privat, erstellt eine Liste der Lottotreffer
    # warum sind tipp und ziehung sichtbar von hier? - weil innerhalb der klasse global initiiert
    def _compare(self):
        self.ergebnis = list(set(self.tipp).intersection(set(self.ziehung)))

    # Siebte Methode, öffentlich, führt das Lottospiel durch
    # Welche Methoden sind von wo nochmal sichtbar?...
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
    Lottobude(Eingabe(), Ausgabe()).spiele().print()
    
