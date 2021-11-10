#!/usr/bin/env python3
import glob
import os
import hashlib
import pprint


def get_data():
    path1 = input("Enter path 1: ")
    path2 = input("Enter path 2: ")
    dirlist_1 = [filename for filename in os.listdir(path1) if os.path.isdir(os.path.join(path1,filename))]
    dirlist_2 = [filename for filename in os.listdir(path2) if os.path.isdir(os.path.join(path2,filename))]
    filelist_1 = [os.path.join(path1,filename) for filename in os.listdir(path1) if os.path.isfile(os.path.join(path1,filename))]
    filelist_2 = [os.path.join(path2,filename) for filename in os.listdir(path2) if os.path.isfile(os.path.join(path2,filename))]
    num_subdir_path1 = len(dirlist_1)
    num_subdir_path2 = len(dirlist_2)
    num_files_path1 = len(filelist_1)
    num_files_path2 = len(filelist_2)
    print()
    print("Result:")
    print("Under Path " + path1 + " there are " +str(num_subdir_path1) + " subdirectories and " + str(num_files_path1) + " files.")
    print("Under Path " + path2 + " there are " +str(num_subdir_path2) + " subdirectories and " + str(num_files_path2) + " files.")
    #print(filelist_1)
    filelist = filelist_1 + filelist_2
    #print(filelist)
    return filelist


def get_hash_list(filelist):
    hashvalues = []
    for files in filelist:
        with open(files, "rb") as f:
            bytes = f.read()
            hashvalues.append(hashlib.md5(bytes).hexdigest())
    return hashvalues


#print(len(get_hash_list(filelist)))

def process(file_list, hash_list):
    result = {}
    for i, hashvalue in enumerate(hash_list):
        filename = file_list[i]
        if not hashvalue in result:
            result[hashvalue] = []
        result[hashvalue].append(filename)
    return result

def main():
    file_list = get_data()
    hash_list = get_hash_list(file_list)
    result = process(file_list, hash_list)
    pprint.pprint(result)


if __name__ == "__main__":
   main()