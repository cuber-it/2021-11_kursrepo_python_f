def machwas(daten, start=0):
    for n in daten[start:]:
        print(n)


l = [ 1,2,3,4,5,6,7]

#machwas(l)
#print("-"*80)
#machwas(l, 5)

def tuwas(*args):
    for n in args:
        print(n)

#tuwas()
#print("-"*80)

#tuwas(1, 2, 3)
#print("-"*80)

#tuwas(*list(range(1, 10)))
#print("-"*80)

def aktion(a, b=0, c="HUHU", d=None):
    print(a)
    print(b)
    print(c)
    print(d)

aktion("P")
aktion("P", d=4711)
aktion(d="1234", a="X")
