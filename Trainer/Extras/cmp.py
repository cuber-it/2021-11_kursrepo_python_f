import os
import sys
import glob

def prep_file_data(files, file_list):
    for fname in file_list:
        key = os.path.basename(fname)
        if not key in files:
            files[key] = []
        files[key].append(fname)
    return files

def get_dups(files):
    return [k for k, v in files.items() if len(v) > 1]

def get_files(path):
    return glob.glob(os.path.join(path, "*.mp4"))

def remove_files(target, files, verbose=True):
    for fname in files:
        file = os.path.join(target, fname)
        if verbose:
            print("removing: ", file)
        os.remove(file)

if __name__ == "__main__":
    files = prep_file_data({}, get_files(sys.argv[1]))
    files = prep_file_data(files, get_files(sys.argv[2]))

    dups = get_dups(files)

    if "--clean" in sys.argv:
        index = sys.argv.index("--clean")
        target = sys.argv[index + 1]
        remove_files(target, dups)
