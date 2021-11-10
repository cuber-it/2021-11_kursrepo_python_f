#!/usr/bin/env python3
import glob
import os
import hashlib

IN_PATH_1="/home/coder/Workspace/aktueller-kurs/Materialien"
IN_PATH_2="/home/coder/Workspace/aktueller-kurs/Materialien"

def get_file_names(path):
    return [names for names in glob.glob("*")]

def find_identical(list_names_1,list_names_2):
    nameslist={hashlib.md5((IN_PATH_1+filename).encode("utf-8")).hexdigest():name for filename in list_names_1 for name in list_names_1}
    identical_files=[]
    for name2 in list_names_2:
        if nameslist[hashlib.md5((IN_PATH_2+name2).encode("utf-8")).hexdigest()]:
            identical_files.append(nameslist[hashlib.md5((IN_PATH_2+name2).encode("utf-8")).hexdigest()])
    return identical_files

def print_doubles(identical_files):
    for i in range(0,len(identical_files)):
        print(identical_files[i])

files_1 = get_file_names(IN_PATH_1)
files_2 = get_file_names(IN_PATH_2)
identical_files = find_identical(files_1,files_2)
print_doubles(identical_files)


