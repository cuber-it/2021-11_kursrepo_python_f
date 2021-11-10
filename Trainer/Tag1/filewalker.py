import os

def recursive_walk(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        if subfolders:
            for subfolder in subfolders:
                recursive_walk(subfolder)
        print('\nFolder: ' + folderName + '\n')
        for filename in filenames:
            print(filename + '\n')

recursive_walk('test.tmp')