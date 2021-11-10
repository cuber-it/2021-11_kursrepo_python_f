import os
import re

class FileWalker:
    def __init__(self, start, pattern):
        self.start = start
        self.pattern = re.compile(pattern)
        self.results = []

    def walk(self, pattern=None):
        if pattern:
            self.pattern = re.compile(pattern)
        for cwd, _, files in os.walk(self.start):
            for fname in files:
                if self.pattern.search(fname):
                    self.results.append(os.path.join(cwd,fname))
        return self
    
if __name__ == "__main__":
    fw = FileWalker("/home/coder/Workspace", r"\.py$")
    print(fw.walk().results)
    