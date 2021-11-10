#!/usr/bin/env python3
import os
import glob
import sys
import hashlib
import pprint


def _to_md5hash(fname):
    with open(fname,"rb") as f:
        bytes = f.read() # read file as bytes
        return hashlib.md5(bytes).hexdigest()
          

def read_fileinfo(dir):
    finfo = { "FOLDERS": [], "FILES": {}, "OTHER": [] }
    for fname in glob.glob(f"{dir}/*"):
        if os.path.isfile(fname):
            finfo["FILES"][_to_md5hash(fname)] = fname
        elif os.path.isdir(fname):
            finfo["FOLDERS"].append(fname)
        else:
            finfo["OTHER"].append(fname)
    return finfo

def process(finfo):
    result = { }
    for folder in finfo:
        for hashval, fname in folder["FILES"].items():
            if not hashval in result:
                result[hashval] = []
            result[hashval].append(fname)
    return result

def report(finfo, result):
    pprint.pprint(finfo)
    print("="*120)
    pprint.pprint(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {os.path.basename(sys.argv[0])} dir_A dir_B", file=sys.stderr)
        sys.exit(1)

    try:
        finfo = []
        for dirname in sys.argv[1:]:
            finfo.append(read_fileinfo(dirname))
        result = process(finfo)
        report(finfo, result)
        sys.exit(0)
    except Exception as e:
        print(f"FAILURE: {e}")
        sys.exit(2)
