#!/usr/bin/env python3
import os
import glob
import hashlib


# /home/coder/Workspace/aktueller-kurs/Materialien/

#E
                
pfad1='/home/coder/Workspace/aktueller-kurs/Materialien/'
pfad2='/home/coder/Workspace/aktueller-kurs/Materialien/'

filenames1=[x for x in glob.glob(os.path.join(pfad1, "*"), recursive=False) if os.path.isfile(x)]
filenames2=[x for x in glob.glob(os.path.join(pfad1, "*"), recursive=False) if os.path.isfile(x)]

#V
hash_vals={}
for file in filenames1+filenames2:
    with open(file, 'rb') as f:
        data = f.read()
        try:
            hash_vals[hashlib.md5(data).hexdigest()]
            hash_vals[hashlib.md5(data).hexdigest()].append(file)
        except:
            hash_vals[hashlib.md5(data).hexdigest()]=file


#A
print('1>',hash_vals)

