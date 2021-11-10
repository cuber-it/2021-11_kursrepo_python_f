class X:
  def __init__(self, v):
    self._v = v # per Konvention gilt _v als hidden/private

  def calc(self, exp):
    return self._v ** exp


class Y:
  def __init__(self, v):
    self.__v = v

  def calc(self, exp):
    return self.__v ** exp



x = X(5)
e = x.calc(3)
print(e)

x._v = 500 # Böse! Böse! Böse! - _v gilt als private/hidden und sollte nie direkt genutzt werden!
e = x.calc(3)
print(e)

y = Y(5)
y.__v = 4711 # Auch wieder böse! Weil sinnlos, da der Wert verlorengeht. __v ist nicht erreichbar von aussen
e = y.calc(3) # Gerechnet wird mit dem initalen Wert
print(e) # 125 als Ergebnis und nicht 4711 ** 3
