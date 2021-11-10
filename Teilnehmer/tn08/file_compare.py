#! /usr/bin/env python3
import os
import glob
import hashlib

ersterpfad = input("Bitte ersten Pfad eingeben:")
zweiterpfad = input("Bitte zweiten Pfad eingeben:")




erstepfadlist = glob.glob(ersterpfad)
zweitepfadlist = glob.glob(zweiterpfad)
unterverzeichnisanzahlserte = 0
unterverzeichnisanzahlszweite = 0
for moeglichedatei in ersterpfad:
    if os.path.isfile(moeglichedatei):
        