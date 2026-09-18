import sys

sys.path.append("PitPyLib")
from PitPyLib import PitRootClass

class PitAppClass(PitRootClass):
    @staticmethod
    def PitLogWrite(fLog, mess):
        with open(fLog, "a") as f:
            f.write(f"{PitAppClass.PitOutfMess(mess)}\n")
        f.close()

    @staticmethod
    def PitLogClear(fLog):
        import os
        os.remove(fLog)
        PitAppClass.PitOutMess(f'Log file {fLog} clear..')


if __name__ == '__main__':
    import sys
    print(f"Test my Py Lib (c) Pit Smelyansky 2026\n")

    myClass = PitAppClass
    myClass.PitOutMess("Hello, Pit!..")

    #print(len(sys.argv))
    if len(sys.argv) > 1 and sys.argv[1] == 'clr':
        myClass.PitLogClear('Logs/log.txt')
    else:
        myClass.PitLogWrite('Logs/log.txt', 'Start work..')
        myClass.PitLogWrite('Logs/log.txt', 'End work..')