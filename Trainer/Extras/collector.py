#!/usr/bin/env python3
import os
import sys
import glob


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {os.path.basename(sys.argv[0])} folder_to_scan", file=sys.stderr)
        sys.exit(1)

    files = {}

    for lfdnr, fname in enumerate(glob.glob(os.path.join(sys.argv[1], "*"))):
        if os.path.isfile(fname):
            fname = os.path.basename(fname)
            if not fname[:10] in files:
                files[fname[:10]] = []
            files[fname[:10]].append({
                "name": fname,
                "size": 0,
                "created": 0})

    import pprint
    pprint.pprint(files)
