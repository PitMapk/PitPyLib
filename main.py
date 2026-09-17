import sys

sys.path.append("PitPyLib")
from PitPyLib import PitRootClass

class PitAppClass(PitRootClass):
    pass

if __name__ == '__main__':
    MyClass = PitAppClass
    MyClass.PitOut('Hello Pit from class!..')
    MyClass.PitOut(sys.version)
