import datetime
import sys

sys.path.append("PitPyLib")
from PitPyLib import PitRootClass


def print_hi(name):
    #    print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\t{name}')
    print(f'{datetime.datetime.now().strftime("%X %d-%m-%y")}\t{name}')


if __name__ == '__main__':
    MyClass = PitRootClass()
    MyClass.PitOut('Hello Pit from class!..')
    MyClass.PitOut(sys.version)

