#!/usr/bin/env python3
from PIL import Image
import argparse
import traceback
import glob
import os
import sys
import re

def get_args():
    parser = argparse.ArgumentParser(description='numerate: Numeriert nach Namen sortierte Dateien und bearbeitet ggf. den Dateinamen')
    # Pflichtparameter
    parser.add_argument("path", help="Dateiordner mit den zu bearbeitenden Dateien")
    parser.add_argument("pattern", help="Dateinamenmuster")
    # Optionale Parameter
    parser.add_argument("-o", "--outfile", help="Name für eine Gesamtdatei, wenn nicht angegeben Einzeldateien")
    parser.add_argument("-r", "--replace", help="Muster für Dateinamenbearbeitung bei Einzeldateien - Schema: Suchmuster==Ersetzung - default: None")
    parser.add_argument("-d", "--dry", action='store_true', default=False, help="Trockenlauf")
    parser.add_argument("-v", "--verbose", action='store_true', default=False, help="Ausführlichere Ausgaben")
    return parser.parse_args()

def process_files(args):
    rex = None
    old_dir = os.getcwd()2pdf
    if args.replace:
        pattern, replacement = args.replace.split("==")
        rex = re.compile(pattern)
    os.chdir(args.path)
    try:
        file_list = sorted(glob.glob(os.path.join(args.pattern)))
        converted = {file: Image.open(file).convert('RGB') for file in file_list}
        if args.outfile:
            if args.dry:
                print(f"{file_list} -> {args.outfile}")
            else:
                converted = list(converted.values())
                converted[0].save(args.outfile, save_all=True, append_images=converted[1:])
        else:
            for old_name, content in converted.items():
                new_name = f"{old_name[:-4]}.pdf"
                if rex:
                    new_name = rex.sub(replacement, new_name)
                if args.dry:
                    print(f"{old_name} -> {new_name}")
                else:
                    content.save(new_name)
    finally:
        os.chdir(old_dir)
    return len(converted)

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
