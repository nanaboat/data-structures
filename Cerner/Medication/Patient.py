class Patient:
    def __init__(self, name, diagnoses):
        self._name = name
        self._diagnoses = diagnoses
        self._prescription_list = []
    
    def set_prescription(self, prescription_list):
        self._prescription_list + prescription_list
    
    def add_prescription(self, medicine):
        self._prescription_list.append(medicine)
    
    def __repr__(self):
        return 'Patient: ' + self._name + ' diagnosed with: ' + self._diagnoses
    
    def patient_profile(self):
        print(self)
        for med in self._prescription_list:
            print(med)
