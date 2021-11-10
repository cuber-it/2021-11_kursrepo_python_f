#!/usr/bin/env python3
import sys
import os

x = 1
x += 1
#print ("x = ", x)

squares = []
for x in range(1,11):
    square = x**2
    squares.append(square)

#print(squares[0:])

#d = {}
#for k in Werte_k:
#    for v in Werte_v:
#        d[n] = v
a ={table:table for table in range(32,128)}
#print(a)

#ASCII TABELLE MIT DICTIONARY
a ={table:chr(table) for table in range(32,128)}
#print(a)

# MAP BEISPIEL
l = [1,2,3,4,5]
quadrat = map(lambda x: x**2, l)
#print(list(quadrat))
#print(list(quadrat))

def machwas(x):
    return x ** 2

quadrat = map(machwas, l)
#print(list(quadrat))
#print(list(quadrat))

#LAMBDA funtioniert nicht bei Filter
quadrat = filter(lambda x: x**2, l)
#print(list(quadrat))
#print(list(quadrat))


# YIELD BEISPIEL = YIELD GENERATOR
def werte_tabelle(start, ende, schritt):
    while start < ende:
        start += schritt
        yield start

for x in werte_tabelle(1,10,2):
#    print(x)
    var = 0

# ZIP BEISPIEL
lw = ["a", "b", "c", "d", "e"]
lz=[1,2,3,4]
a = list(zip(lw,lz))
#print(a)
b = dict(list(zip(lw,lz)))
#print(b)
# AUSGABE IN LISTE (ZIP ALS COMPREHENTION)
l = [list(n) for n in zip(lw, lz) ]
#print(l)

# IMPORT OS BeiSPIEL

import glob
for name in glob.glob("'"):
    if os.path.isfile(name):
        print("Ist Datei: ", name)