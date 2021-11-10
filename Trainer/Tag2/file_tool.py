#!/usr/bin/env python3
import file_finder
import sys
import os

if len(sys.argv) < 3:
    print("usage: ", os.path.basename(sys.argv[0]), "root pattern")
    sys.exit(1)

root = sys.argv[1]
muster = sys.argv[2]
daten = file_finder.Filefinder(root).find(muster).result_list()

for fname in daten:
    print(fname)


