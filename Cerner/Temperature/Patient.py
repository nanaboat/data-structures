from collections import deque
from Temperature import Temperature


class Patient:
    def __init__(self, name):
        self._name = name
        self._temp_vals = deque()
    
    @property
    def avg_temp(self):
        return sum(self._temp_vals) / len(self._temp_vals)
    
    def add_temperature(self, temp):
        self._temp_vals.append(temp)
    


class Nurse:
    def __init__(self, name):
        self._name = name
        self._patients = []
    
    def record_temperature(self, patient, temp_val, method):
        temp = Temperature(temp_val, method)
        temp.rate_temperature()
        for p in self._patients:
            if p._name == patient:
                p.add_temperature(temp)
                return
        self.add_patient(Patient(patient))
    
    def add_patient(self, new_patient):
        self._patients.append(new_patient)