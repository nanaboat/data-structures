from Dosage import Dosage
from Frequency import Frequency
from Medicine import Medicine
from Nurse import Nurse
from Patient import Patient
from Scheduler import Scheduler
from sched import scheduler as event_scheduler
import time

class Run:
    def main(self):
        patient1 = Patient('Mark', 'Light Fever')
        #print(patient1)
        freq1 = [Frequency.Morning, Frequency.Afternoon, Frequency.Evening]
        freq2 = [Frequency.Morning, Frequency.Evening]
        #print(''.join([freq.name for freq in freq1]))
        med1 = Medicine('Ibuprofen', 2, freq1)
        med2 = Medicine('Theraflu', 1, freq2)
        #import pdb; pdb.set_trace()
        patient1.add_prescription(med1)
        patient1.add_prescription(med2)
        #patient1.patient_profile()
        alice = Nurse('Alice')
        bob = Nurse('Bob')
        alice.add_time(Frequency.Morning)
        alice.add_time(Frequency.Afternoon)
        bob.add_time(Frequency.Afternoon)
        bob.add_time(Frequency.Evening)
        schedule = Scheduler()
        schedule.update_schedule(alice)
        schedule.update_schedule(bob)
        schedule1 = Scheduler()
        schedule1.update_schedule(alice)
        schedule1.update_schedule(bob)
        event = event_scheduler(time.time, time.sleep)
        print('START:', time.time())
        event.enter(5, 1, schedule1.notify_nurse, (Frequency.Morning,))
        event.enter(25, 1, schedule1.notify_nurse, (Frequency.Afternoon,))
        event.run()
        #schedule1.notify_nurse(Frequency.Evening)


if __name__ == "__main__":
    Run().main()
