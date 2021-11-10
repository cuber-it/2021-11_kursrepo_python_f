class B:
    def __init__(self):
        pass
    
    def __geheim(self):
        pass
    
    def _helfer(self):
        pass
    
    def mach_was(self):
        self._helfer()
        self.__geheim()
    
    
class K(B):
    def __init__(self, value=None):
        super().__init__()
        
    
    def tu_was(self):
        self._helfer()
        #self.__geheim() - funktioniert nicht
        
    def mach_was(self):
        super().mach_was()

#bo = B()
#bo.mach_was()

ko = K()
ko.mach_was()
ko.tu_was()