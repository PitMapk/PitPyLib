import sys

sys.path.append("PitPyLib")
from PitPyLib import PitRootClass

class PitAppClass(PitRootClass):

    def PitLogWrite(self, fLog, mess):
        with open(fLog, "w") as f:
            f.writelines(super.PitGetfMess(mess))
        f.close()


if __name__ == '__main__':
    MyClass = PitAppClass

    MyClass.PitLogWrite(PitAppClass,'log.txt', 'Запись в лог..')

    #MyClass.PitOut('Hello Pit from class!..')
    #MyClass.PitOut(sys.version)

