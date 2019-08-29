import Person

class Patient(Person.Person):
    def __init__(self, name, age, address, temp, allergies=None, diseases=None, last_seen=None):
        self.name = name
        self.age = age
        self.address = address
        self.temperature = temp
        self.allergies = [allergies]
        self.diseases = [diseases]
        self.last_seen = [last_seen]
    
    def set_allergies(self, allergy_list):
        if self.allergies[0] is None:
            self.allergies.pop()
        self.allergies += allergy_list
    
    def add_allergies(self, allergy):
        if self.allergies[0] is None:
            self.allergies.pop()
        self.allergies.append(allergy)
    
    def set_diseases(self, disease_list):
        if self.diseases[0] is None:
            self.diseases.pop()
        self.diseases += disease_list
    
    def add_diseases(self, disease):
        if self.diseases[0] is None:
            self.diseases.pop()
        self.diseases.append(disease)
    
    def add_last_seen(self, last):
        if self.last_seen[0] is None:
            self.last_seen.pop()
        self.last_seen.append(last)
    
    @property
    def allergy_profile(self):
        name = 'Patient Name: ' + self.name + 'has the following allergies:  \n'
        line = [name]
        for a in self.allergies:
            line.append('- {0} with severity of {1}'.format(a.name, a.severity))
        return ''.join(line)
    
    @property
    def disease_profile(self):
        name = 'Patient Name: ' + self.name + 'has the following diseases:  \n'
        line = [name]
        for a in self.diseases:
            line.append('- {0} '.format(a.name))
        return ''.join(line)


if __name__ == "__main__":
    pass