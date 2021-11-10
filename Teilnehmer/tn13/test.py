# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

class B:
    def __init__(self):
        pass
    def mach_was(self):
        pass
    def __geheim(self):
        pass
    def macht_nix(self):
        pass

class K(B):
    def __init__(self):
        pass



test = B()
test2 = K()
print(dir(test))
print(dir(test2))
test._B__geheim
test2._B__geheim