#
#   My Python Lib
#   version:    0.01
#
import datetime


class PitRootClass:
    @staticmethod
    def PitGetfMess(mess):
        return f'{datetime.datetime.now().strftime("%X %d-%m-%y")}\t{mess}'

    def PitOut(self, mess):
        print(self.PitGetfMess(mess))
