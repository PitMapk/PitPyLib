import datetime
import sys

sys.path.append("PitPyLib")
from PitPyLib import PitRootClass

if __name__ == '__main__':
    MyClass = PitRootClass()
    MyClass.PitOut('Hello Pit from class!..')
    MyClass.PitOut(sys.version)
