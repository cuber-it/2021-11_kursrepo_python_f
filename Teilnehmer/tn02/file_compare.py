# Aufgabe 1 File_Compare
import os
from os.path import isfile, join
import glob
import sys
import hashlib
from pprint import pprint as pprint

def get_hashes(path):
    """Find all files in a folder and calculate their hash value."""
    """input: path"""
    """output: tuple of path and hash """
    files = [fname for fname in glob.glob(path+"/*")]
    hashes = []
    #print(files)
    for fname in files:
        with open(fname, "rb") as f:
            hashes.append(hashlib.md5(f.read()).hexdigest())
    hash_pairs = tuple(zip(hashes, files))
    return hash_pairs

def file_compare(hashes1, hashes2):
    """input: hashes1, hashes2"""
    """output: dublets"""

    hash_pairs1 = get_hashes(path1)
    hash_pairs2 = get_hashes(path2)

    #print(hash_pairs1)
    d = dict()
    for t1 in hash_pairs1:
        if t1[0] in hash_pairs2.keys():
            d[t1[0]] = [t1[1], hash_pairs2[1]]

    pprint(d)

path1 = sys.argv[1]
path2 = sys.argv[2]

file_compare(path1, path2)

# Ziel: dict gefunden, key: md5hash, value=[path1, path2*]   *wenn vorhanden


