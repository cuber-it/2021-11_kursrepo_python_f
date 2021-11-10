import os
import glob
import hashlib
import pprint


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


path1 = r"/home/coder/Workspace/aktueller-kurs/Materialien/"
path2 = r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/"


files_1 = [os.path.join(path1, f) for f in os.listdir(path1) if os.path.isfile(os.path.join(path1, f))]
files_2 = [os.path.join(path2, f) for f in os.listdir(path2) if os.path.isfile(os.path.join(path2, f))]

files = files_1 + files_2

hashes = [md5(file) for file in files]

#hash_dict = {1: "asd", 2: "asddd"}

hash_dict = {}

for hash, file in zip(hashes, files):
    if hash in hash_dict:
        current = hash_dict.get(hash)
        new = current.append(file)
    else: hash_dict[hash] = [file]

pprint.pprint(hash_dict)