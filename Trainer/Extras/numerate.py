#!/usr/bin/env python3
import glob
import argparse
import os
import re
import sys
import traceback

def get_args():
    parser = argparse.ArgumentParser(description='numerate: Numeriert nach Namen sortierte Dateien und bearbeitet ggf. den Dateinamen')
    # Pflichtparameter
    parser.add_argument("path", help="Dateiordner mit den zu bearbeitenden Dateien")
    parser.add_argument("pattern", help="Dateinamenmuster")
    # Optionale Parameter
    parser.add_argument("-r", "--replace", help="Muster für Dateinamenbearbeitung - Schema: Suchmuster==Ersetzung - default: None")
    parser.add_argument("-s", "--start", type=int, default=1, help="Startwert der Numerierung - default: 1")
    parser.add_argument("-n", "--number", default="03d", help="Muster der Zahlenausgabe - default: 03d = 000")
    parser.add_argument("-d", "--dry", action='store_true', default=False, help="Trockenlauf")
    parser.add_argument("-v", "--verbose", action='store_true', default=False, help="Ausführlichere Ausgaben")
    return parser.parse_args()

def process_files(args):
    rex = None
    old_dir = os.getcwd()
    if args.replace:
        pattern, replacement = args.replace.split("==")
        rex = re.compile(pattern)
    os.chdir(args.path)
    try:
        for i, old_name in enumerate(sorted(glob.glob(args.pattern)), start=args.start):
            new_name = f"{i:{args.number}}_{old_name}"
            if rex:
                new_name = rex.sub(replacement, new_name)
            if args.dry:
                print(f"{old_name} -> {new_name}")
            else:
                os.rename(old_name, new_name)
    finally:
        os.chdir(old_dir)
    return i - args.start


if __name__ == "__main__":
    args = get_args()
    try:
        process_files(args)
        sys.exit(0)
    except Exception as e:
        print(f"FAIL: {os.path.basename(sys.argv[0])} {sys.argv[1:]} mit Fehler abgebrochen", file=sys.stderr)
        print(e, file=sys.stderr)
        if args.verbose:
            print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)
