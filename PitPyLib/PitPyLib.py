#
#   My Python Lib
#   version:    0.01
#
import datetime


class PitRootClass:
    @staticmethod
    def PitOutfMess(mess):
        import datetime
        return f'{datetime.datetime.now().strftime("%d-%m-%y %X")}:\t{mess}'

    @staticmethod
    def PitOutMess(mess):
        print(PitRootClass.PitOutfMess(mess))