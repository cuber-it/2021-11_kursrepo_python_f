#! /usr/bin/env python3

import os
import sys

import messgeraete as mg
import messung
import auswertung

# Vorbereitung der Geräte
g = [ mg.MG_R("R_01"), mg.MG_R("R_02")]

# Vorbereitung der Auswertungsinfrastruktur
daten = {}
for m in g:
    a = messung.Messung(m)
    a.run(3)
    daten[m.id] = a.result

# import pprint
# pprint.pprint(daten)

auswertung.Roentgen(daten).analyze().report()