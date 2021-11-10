import copy
import pprint

l1 = [4177, ["a", "b", "c"], { "Name": "Willi", "Ort": "Hamburg "}]
pprint.pprint(l1)

l2 = l1 # garkeine Kopie
l3 = l1.copy() # flache Kopie
l4 = copy.copy(l1) # flache Kopie
l5 = copy.deepcopy(l1) # tiefe Kopie

pprint.pprint(l2)
pprint.pprint(l3)
pprint.pprint(l4)
pprint.pprint(l5)
print("-" * 80)
l2[0] = 1234

pprint.pprint(l1)
pprint.pprint(l2)
pprint.pprint(l3)
pprint.pprint(l4)
pprint.pprint(l5)
print("-" * 80)
l3[1][0] = "Hallo"
l4[1][1] = "Welt"

pprint.pprint(l1)
pprint.pprint(l2)
pprint.pprint(l3)
pprint.pprint(l4)
pprint.pprint(l5)
print("-" * 80)
l5[2]["PLZ"]="12345"

pprint.pprint(l1)
pprint.pprint(l2)
pprint.pprint(l3)
pprint.pprint(l4)
pprint.pprint(l5)
print("-" * 80)
