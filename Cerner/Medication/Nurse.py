import Frequency
import time


class Nurse:
    def __init__(self, name:str):
        self._name = name
        self._times = set()
    
    def add_time(self, times: Frequency):
        ''' Create schedule times for nurse.'''
        self._times.add(times)
    
    def notify(self, period: Frequency):
        '''Notify nurse if period is part of her schedule.'''
        if period in self._times:
            print("Nurse {0}, you are being notified of event: {1} ; {2}".format(self._name, period.name, time.time()))