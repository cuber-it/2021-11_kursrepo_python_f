#!/usr/bin/env python3
class Eingabe:
    def __init__(filename):
#        try:
#            with open(file, 'rb') as f:
#            data = f.read()
#            readline().strip()
#
#        except:
    return "1, 2, 3, 4, 5, 6"

    def get_input(self):
        return str

class Ausgabe:
    values = {}
    def set_values(self,tipp,ziehung,ergebnis):
        values["Tipp"]=tipp
        values["Ziehung"]=ziehung
        values["Ergebnis"]=ergebnis

    def print_results(self,tipp,ziehung,ergebnis)
        print("Tipp:     ",self.values["Tipp"])
        print("Ziehung:  ",self.values["Ziehung"])
        print("Ergebnis: ",self.values["Ergebnis"])

class Ziehung:
    def shuffle
        return None

    def get_values
        return (6)

class Lottobude:
    def __init__(self,eingab,ausgabe,ziehung):
        self.eingabe=self.eingabe
        self.ausgabe=self.ausgabe
        self.lostrommel=self.ziehung
        self.tipp = []
        self.ziehung = []
        self.ergebnis = []
        return self

    def _check_tipp_values(self)
        pass
        # Bei Fehler raise RuntimeError

    def _prepare_tipp(self, raw_data)
        self._check_tipp_values()

        def _compare(sefl)
        pass

    def spiele(self):
        eingabe = self.eingabe.get_values()
        self._prepare_tipp(eingabe)
        self.ziehung = self.lostrommel.shuffle()
        self._compare()
        return self

    def print(self):
        self.ausgabe.set_values(self.tipp,self.ziehung,self.ergebnis)
        self.ausgabe.print_result()
        return self

if __name__ == "__main__":
    e = Eingabe ()
    a = Ausgabe ()
    lb = Lottobude(e, a)
    lb.spiele().print_reuslts()

