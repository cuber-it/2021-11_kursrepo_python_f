#!/usr/bin/env python3
import os
import sys
import glob

# E_ingabe
def read_from_path(dateipfad):
    unterordner = []
    dateien = []
    
    for akt_element in glob.glob(f"{dateipfad}/*"):
        if os.path.isdir(akt_element):
            unterordner.append(akt_element)
        elif os.path.isfile(akt_element):
            dateien.append(akt_element)
    print(unterordner, dateien)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Erforderliche Parameter: {sys.argv[0]}, Dateipfad 1, Dateipfad 2.", file=sys.stderr)
        sys.exit(1)
    
    try:
        read_from_path(sys.argv[1:])
    except Exception as e:
        print("Fehler: ", e)
        sys.exit(2)