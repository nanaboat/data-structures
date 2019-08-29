import Dosage


class Medicine:
    def __init__(self, name: str, qty: int, frequency: Dosage, start, end=None):
        self._name = name
        self._prescription = Dosage.Dosage(qty)
        self._prescription.set_frequency(frequency)
    
    def __repr__(self):
        return 'Take ' + str(self._prescription._quantity) + ' ' + self._name \
            + ' every ' + ''.join([(freq.name + ', ')  for freq in self._prescription._frequency])