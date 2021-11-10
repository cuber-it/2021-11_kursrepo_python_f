#! /usr/bin/env python3

import sys
import os
import hashlib

def eingabe(pfade):
    # print(pfade)
    if not len(pfade) == 3:
        print("Zwei Pfade angeben.")
        quit()
    pfad1, pfad2 = pfade[1:3]
    # print("Pfad 1:", pfad1)
    # print("Pfad 2:", pfad2)
    return [pfad1, pfad2]

def get_files(pfad):
    print("pfad: ", pfad)
    print("files: ", os.listdir(pfad))
    print(os.path.join(pfad, os.listdir(pfad)[1]))
    files_pfad = [os.path.join(pfad, f) for f in os.listdir(pfad) if os.path.isfile(os.path.join(pfad, f))]
    return files_pfad

def get_md5hash(file):
    with open(file, "r") as fd:
        inhalt = fd.read()
    return hashlib.md5(inhalt).hexdigest()


def verarbeitung(pfad1, pfad2):
    files1 = get_files(pfad1)
    files2 = get_files(pfad2)
    return [files1,files2]



pfad1, pfad2 = eingabe(sys.argv)
files1, files2 = verarbeitung(pfad1, pfad2)

print("files1: ", files1)

# print("Files 1:", files1)
# print("Files 2:", files2)

get_md5hash(files1[1])


