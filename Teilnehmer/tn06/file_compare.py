import os
import glob
import sys

def analyseFolder(filepath):
    #print(filepath)
    folderlist = glob.glob(f"{filepath}/*")
    #folderlist = os.listdir(filepath)
    #for name in glob.glob('/home/coder/Workspace/aktueller-kurs/Materialien/'):
    #    print(name)
    finfo = {"FOLDERS": [], "FILES":[]}
    for fname in folderlist:
        if os.path.isfile(filepath+"/"+fname):
            finfo['FILES'].append(fname)
        elif finfo['FOLDERS'].append(fname):
            print("Folder")
    num_files = 0
    for i in folderlist:
        os.path.isfile(filepath+i)
        num_files = num_files + 1
    print(folderlist)

    return finfo

def main():
    print("file_compare")
    filepath1 = ""
    filepath2 = ""
    if len(sys.argv) == 2:
        filepath1 = sys.argv[1]
        filepath2 = sys.argv[1]
    elif len(sys.argv) == 3:
        filepath1 = sys.argv[2]
        filepath2 = sys.argv[3]
    else:
        print("Error Filepath needed")
        sys.exit(1)

    f.append(analyseFolder(filepath1))
    f = analyseFolder(filepath2)

if __name__ == "__main__":
    main()