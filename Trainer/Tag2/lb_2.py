# Infos:
# self.variable = Objektvariable, kann von jeder Methode Ort im Objekt zugegriffen werden
# variable in der Methode = lokale Variable, damit nur innerhalb der Methode sichtbar "Arbeitsvariablen"
#
# self._name = "private" Methode/Variable, soll nicht von ausserhalb des Objektes zugegriffen werden
# self.name = "public" Methode/Variable, darf von aussen zugegriffen werden
#
# __dingens__ "dingens" ist etwas was von python ausgewertet wird. Oft mit Defaultfunktionen belegt, kann von uns angepasst werden
import random

class Lottobude:
    def __init__(self, lostrommel=[]): # der Name self ist Konvention, self repräsentiert das aktive Objekt der Klasse, lostrommel ist optional
        # Defaultverhalten: wenn keine lostrommel angegeben wurde, dann nimm Standard-Lotto
        if lostrommel:
            self._numbers = lostrommel.copy() # Kopie, damit nicht versehentlich "von aussen" was geändert werden kann, Stichwort Referenz!
        else:
            self._numbers = list(range(1,50)) # [1,2,3...49]
        self._stats = [0] * 7 # [0,0,0,0,0,0,0]
        self._ziehung = [] # nix

    def __str__(self):
        return f"Lottobude:\n\t{str(self._ziehung)}\n\t{self._stats}"

    def ziehung(self):
        self._ziehung = random.sample(self._numbers, 6)
        return self._ziehung

    def auswerten(self, tipp):
        treffer = set(self._ziehung).intersection(set(tipp))
        self._stats[len(treffer)] += 1
        return list(treffer)

    def get_stats(self):
        return self._stats

if __name__ == "__main__":
    lb = Lottobude(list(range(7, 105))) # Spezielle Variante
    for n in range(0,10000):
        print("Ziehung:", lb.ziehung()) # <- Methode Ziehung
        print("Treffer:", lb.auswerten([11,12,13,14,15,16])) 
        print(lb)
        # print(lb._ziehung) <- private Variable de sObjekte, soll nicht so zugegriffen werden. Konvention!
    print(lb.get_stats())