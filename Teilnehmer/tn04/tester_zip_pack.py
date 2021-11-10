
#zippen zweier listen zu einer Tupelliste oder zu einem Dictionary oder zu List in List
l1 = [1, 2, 3, 4, 5]
l2 = ["weiss", "gelb", "rot", "gruen", "blau"]

d=zip(l1, l2)
print(d) #whatever

f=list(zip(l1, l2))
print(f) #zipped tuples

g= dict(zip(l1,l2))
print(g) #zipped dict
#cool. funktioniert.

e = [list(n) for n in zip(l1, l2)]  
print(e) #zipped lists in list, praktisch durch umwandeln von tupeln in list
# yeah, funktioniert auch :)

#--------------------------------------------------------

# pack...  another strange thing. ignorieren.

