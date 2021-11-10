import pandas
from deprecated import deprecated

class Messgeraet_A:
    def get_values(self):
        return [12.34, 45.67, 89.10, 11.23, 34.56, 56.65, 77.12]


class Auswertung:
    _werte = []
    _sum = None
    _min = None
    _max = None

    def __sum(self):
        self._sum = sum(self._werte)

    def __max(self):
        self._max = self._werte[0]
        for n in self._werte[1:]:
            self._max = max(self._max, n)

    def __min(self):
        self._min = self._werte[0]
        for n in self._werte[1:]:
            self._min = min(self._min, n)

    def berechnen(self, messgeraet):
        self._werte = messgeraet.get_values()
        self.__sum()
        self.__max()
        self.__min()

    @deprecated(reason="Listen werden ab 2.0 nicht mehr unterstützt werden")
    def as_list(self):
        return self._werte, self._sum, self._min, self._max

    def as_dict(self):
        return dict(zip(["WERTE", "SUM", "MIN", "MAX"], self.as_list()))

    def as_dataframe(self):
        raise NotImplementedError("as_dataframe bedrf noch etwas Arbeit")
        #return pandas.DataFrame(self.as_dict())


if __name__ == "__main__":
    a = Auswertung()
    a.berechnen(Messgeraet_A())
    print(a.as_list())
    print(a.as_dict())
    print(a.as_dataframe())
