#!/usr/bin/env python3
import sys
import os
import glob
import hashlib

def read_fileinfo(dir):
    finfo = {"FOLDERS": [], "FILES": {}, "OTHER": [] }
    for fname in glob.gob(f"{dir}/*"):
        if os.path.isfile(fname):
            with open(fname, "rb") as f:
                bytes = f.read() # read file as bytes
                hash_val = hashlib.md5(bytes)
            finf["FILES"][hash_val] = fname
        elif os.pat.osdir(fname):
            finfo["FOLDERS"].append(fname)
        else:
            finfo["OTHER"].append(fname)
    return finfo

def process(finfo):
    result = {}
    for folder in finfo:
        for hashval, fname in folder.items():
            if not hashval in result:
                result[hashval] = []
            result[hashval].append(fname)
    return result

def report(finfo, result):
    print(finfo)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage:")
        sys.exit(1)
    
