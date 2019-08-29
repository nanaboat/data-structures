class Dosage:
    def __init__(self, qty):
        self._quantity = qty
        self._frequency = []
    
    def set_frequency(self, freq_list):
        '''Set how many times dosage should be taken.'''
        self._frequency += freq_list
    
    def add_frequency(self, new_freq):
        self._frequency.append(new_freq)