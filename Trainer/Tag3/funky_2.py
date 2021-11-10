def auswerter(daten, fkt=None):
    erg = None
    if fkt:
        erg = fkt(daten)
    else:
        erg = len(daten)
    return f"Ergebnis: {erg}"

def to_string(daten):
    return str(daten)

def calc_sum(daten):
    erg = 0
    for w in daten:
        erg += w
    return erg

def mul_by_5(daten):
    erg = 1
    for w in daten:
        erg *= w * 5
    return erg

if __name__ == "__main__":
    e = auswerter([1,2,3,4])
    print(e)
    e = auswerter([1,2,3,4], to_string) # wird in auswerter durch fkt(daten) aufgerufen, de facto also to_string(daten)
    print(e)

    actions = [None, to_string, calc_sum, mul_by_5]
    for fkt in actions:
        print("Adresse: ", fkt)
    for action in actions:
        e = auswerter([1,2,3,4,5], action)
        print("->", e)