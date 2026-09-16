#
#   My Python Lib
#   version:    0.01
#
import datetime


class PitRootClass:

    @staticmethod
    def PitOut(mess):
        print(f'{datetime.datetime.now().strftime("%X %d-%m-%y")}\t{mess}')
