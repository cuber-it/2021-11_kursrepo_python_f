import os
import re

class Filefinder:
    def __init__(self, start_folder, pattern=None):
        self.start_folder = start_folder
        self.pattern = pattern
        self.results = []

    def __str__(self):
        text = "Filefinder-Objekt:\n"
        text += f"\tStart: {self.start_folder}\n"
        text += f"\tMuster: {self.pattern}\n"
        text += f"\tAnzahl: {len(self.results)}\n"
        text += f"\tFiles: {self.results}\n"
        return text

    def __repr__(self):
        return [
            type(self).__name__,
            self.start_folder,
            self.pattern,
            self.results
        ]

    def find(self, pattern=None):
        self.results = []
        if pattern:
            self.pattern = pattern
        rex = re.compile(self.pattern) # Vorbereitung, dadurch wird das Gesamtkonstrukt schneller

        for root, _, files in os.walk(self.start_folder):
            for basename in files:
                if rex.findall(basename):
                    self.results.append(os.path.join(root, basename))  
        return self # damit Kettenaufrufe möglich sind

    def result_list(self):
        return self.results

    def files_found(self):
        return len(self.results)

# Usage
#ff = Filefinder(start_ordner)
#ff.find(regular_pattern_for_filename)
#ff.result_list()
#ff.files_found()

if __name__ == "__main__":
    ff = Filefinder("/home/coder/Workspace/kurse_python_f") # __init__
    print(ff.__repr__())

    ff.find(r".*\.py$") # suche alle die mit py enden
    print(ff.__repr__())
    #print(ff.result_list())
    #print(ff.files_found())
    #print(ff.find(r".*\.md$").result_list())
    #print(80*"*")
    #print(ff)
    