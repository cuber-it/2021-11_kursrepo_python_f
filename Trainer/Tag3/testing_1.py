class C:
    def __init__(self, v):
        self._v = v

    def get(self):
        return self._v

    def set(self, v):
        self._v = v

    def add(self, w):
        self._v += w

    def sub(self, w):
        self._v -= w

    def mul(self, w):
        self._v *= w

    def div(self, w):
        self._v /= w

if __name__ == "__main__":
    o = C(1)
    assert o.get() == 1

    o = C(1)
    o.set(5)
    assert o.get() == 5

    o = C(1)
    o.add(5)
    assert o.get() == 6, "result should have been 6"

    o = C(5)
    o.mul(5)
    assert o.get() == 25, "result should have been 25"

    o = C(1)
    o.sub(1)
    assert o.get() == 0, "result should have been 0"

    o = C(1)
    o.div(4)
    assert o.get() == 0.25, "result should have been 0.25"
