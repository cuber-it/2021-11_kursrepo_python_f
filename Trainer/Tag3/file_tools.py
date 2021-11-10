"""Ein Doc-String
"""
import os
import fnmatch

def file_search(pattern, *folders, **kwargs):
    '''
    Durchsucht das Dateisystem nach Dateien und wendet optionalen Filter an

    Parameters:
    - :param pattern: String with filename pattern
    - :param *folders: list of folders to start search at
    - :param **kwargs: different options 
        - filter: reference to filter function

    :returns:
    - Dictionary: contains Pattern, Reference to filter, for every visited folder the foldername and findings
    '''
    filter = kwargs["filter"] if "filter" in kwargs else None
    result = {
        "pattern": pattern,
        "filter": filter
    }

    for start_folder in folders:
        file_list = []
        for root, _, files in os.walk(start_folder):
            for basename in files:
                if fnmatch.fnmatch(basename, pattern):
                    fullname = os.path.join(root, basename)
                    # Wenn filterfunktion übergeben wure, wird deren Ergebnis eingehängt
                    if filter:
                       ergebnis = filter(fullname)
                       file_list.append(ergebnis)
                    else: 
                       # ... ansonten einfach den fullname merken 
                       file_list.append(fullname)  
        result[start_folder] = file_list
    return result

if __name__ == "__main__":
    print(file_search.__doc__)
    
    workspace = "/home/coder/Workspace/kurse_python_f/"
    e = file_search("*py", 
                    workspace + "Trainer/Tag1", workspace + "Trainer/Tag2",
                    filter = lambda x: (x, open(x).read()))
    for k, v in e.items():
        print(k, " ==> ", v)
    