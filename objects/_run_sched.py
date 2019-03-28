import datetime

class Sched(object):

    def __init__(self, time):
        dateSTR = datetime.datetime.now().strftime("%H:%M:%S")
        while dateSTR != (time):
            # print(dateSTR)
            time.sleep(1)
            dateSTR = datetime.datetime.now().strftime("%H:%M:%S")