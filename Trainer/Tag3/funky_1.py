def uc_print(*args, **optionen):
    ausgabe = ""
    trenner = optionen["trenner"] if "trenner" in optionen else " "
        
    for a in args:
        ausgabe += str(a) + trenner
    print(ausgabe[:-1])

uc_print()
uc_print("A", 1, 2, 4711)
uc_print("A", 3, 4, 1234, trenner="-")


def finde_doppelte(werte1, werte2):
    erg_anzahl = 0
    erg_elemente = []
    for w in werte1:
        if w in werte2:
            erg_anzahl += 1
            erg_elemente.append(w)
    return { "Anzahl": erg_anzahl, "Elemente": erg_elemente }

l1 = [1,2,3,4,5,6]
l2 = [4,5,6,7,8,9]

e = finde_doppelte(l1, l2)
print(e)
#--------------------------------------------------
def suche_datei(dateiname, start="/"):
    uc_print("Suche beginnt für ", dateiname, start)

suche_datei("test.py")
suche_datei("test.py", "/home/coder")
#---------------------------------------------------
def finde_datei(dateiname, *startpunkte):
    if len(startpunkte) == 0: #es kann sein, dass eine leere Liste kommt, dieser Test ist optional, weil leere Liste aus sinnvoll sein kann
        startpunkte = ["/"]
    for startpunkt in startpunkte:
        uc_print("Suche beginnt für ", dateiname, startpunkt)

finde_datei("test.py")
finde_datei("test.py", "/bin", "/usr/bin", "/home/coder")


