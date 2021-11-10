import random

class Lottobude:
    _stats = [0,0,0,0,0,0,0]
    _ziehung = None

    def ziehung_durchfuehren(self):
        """

        """
        self._ziehung = random.sample(range(1,50), 6)

    def tipp_auswerten(self, tipp):
        x = set(tipp).intersection(set(self._ziehung))
        self._stats[len(x)] += 1
        return x

    def statistik_lesen(self):
        return self._stats

if __name__ == "__main__":
    lb = Lottobude()
    tipp = [1,2,3,4,5,6]
    for n in range(1, 10000000):
        lb.ziehung_durchfuehren()
        erg = lb.tipp_auswerten(tipp)
        if len(erg) >= 5:
            print("Ein fetter Gewinn!!! für ", erg, "in Lauf ", n)
    stats = lb.statistik_lesen()
    for i, n in enumerate(stats):
        print(f"Treffer: {i} - {n}")
        

        sorted