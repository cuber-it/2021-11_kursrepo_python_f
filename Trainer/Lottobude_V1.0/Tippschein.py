""" Tippschein

Modul für die Lottobude

Version 0.1 - 2021-10-29

Historie:

2021-10-26 - Erstanlage  Ulrich Cuber (kontakt@uc-it.de) - Jira-Ticket: VODA-001

...
"""
class Tippschein:
<<<<<<< HEAD
    """ Class Tippschein
=======
    def __init__(self, eingabe):
        # Zerlegen
        # Umwandeln
        # check 1: 6 Zahlen
        # check 2: 1-49
        # check 3: keine Doppelten
        # speichern in: self.tipp - vom Typ Liste
        if isinstance(eingabe, str):
            eingabe = eingabe.split(",")
        if len(eingabe) == 6:
            for i, n in enumerate(eingabe):

    #def _convert_int(self, val):
        #    result = []
        #    for i in val:
        #        result.append(int(i))
        #    return result

        #def _check_len(self, val, len=6):
        #    if len(val) != len:
        #        raise RuntimeError(f"Länge: {len(val)}")

        #def _check_dups(self, val):
        #    if len(val)!=len(set(val)):
        #        raise RuntimeError(f"Duplicate: {val}")
        #pass
>>>>>>> Beispiele

    Init - Eingabe eines Strings/Liste mit 6 Zahlen 1-49

    ...
    """

    
    def __init__(self, eingabe):    
        self.eingabe = eingabe

    def prepare(self):    
        """ __init__:

        Vorgehen:
        - Zerlegen
        - Umwandeln
        - check 1: 6 Zahlen
        - check 2: 1-49
        - check 3: keine Doppelten
        - speichern in: self.tipp - vom Typ Liste
        """
        self.tipp = None
        if isinstance(self.eingabe, str):
            self.tipp = self.eingabe.split(",")
        self._convert_int()
        self._check_len()
        self._check_dups()
        self._check_range()
        
        
    def _convert_int(self):
        # Funktion:
        result = []
        for i in self.tipp:
            result.append(int(i))
        self.tipp = result

    def _check_len(self):
        if len(self.tipp) != 6:
            raise RuntimeError(f"Länge: {len(self.tipp)}")

    def _check_dups(self):
        if len(self.tipp) != len(set(self.tipp)):
            raise RuntimeError(f"Duplicate: {self.tipp}")

    def _check_range(self):
        valid = range(1,50)
        for n in self.tipp:
            if n not in valid:
                raise RuntimeError(f"Range: {n} in {self.tipp}")

# - das wäre in einer eigenen Datei
import unittest

class TippscheinTests(unittest.TestCase):
    def test_alles_richtig(self):
        tippschein = Tippschein("1,2,3,4,5,6")
        tippschein.prepare()
        self.assertEqual(tippschein.tipp, [1,2,3,4,5,6])

    def test_doppelte_exception(self):
        tippschein = Tippschein("1,2,3,3,5,6")
        self.assertRaises(RuntimeError, tippschein.prepare)

    def test_bereich_exception(self):
        tippschein = Tippschein("1,2,3,4,5,99")
        self.assertRaises(RuntimeError, tippschein.prepare)


if __name__ == "__main__":
    unittest.main()