from Frequency import Frequency
from Nurse import Nurse


class Scheduler:
    schedule = []

    def update_schedule(self, nurse: Nurse):
        '''Update the main schedule for all nurses.'''
        self.schedule.append(nurse)
    
    def notify_nurse(self, times: Frequency):
        for nurse in self.schedule:
            nurse.notify(times)
    
    