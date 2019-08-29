from time import time
from datetime import datetime

class Temperature:
    def __init__(self, temp_val=32.0, method=None, default='F'):
        ''' Temperature is in Farenheit.'''
        self._temperature = temp_val
        self._time_taken = time()
        self._method = method
        self._metric = default
    
    def rate_temperature(self):
        if self._temperature <= 99.5 and self._temperature >= 97.7:
            print("Temperature is good")
        elif self._temperature < 97.7:
            print("Low temperature")
        else:
            print("High temperature. You have a fever")
    
    def __repr__(self):
        t = datetime.fromtimestamp(self._time_taken).strftime("%m/%d/%Y  %H:%M:%S")
        return "Temperature {0}{3} at {1} taken by {2}".format(self._temperature, t, self._method, self._metric)
    
    def update_temperature(self, new_temp):
        self._temperature = new_temp
    
    def get_temperature_celsius(self):
        if self._metric == 'F':
            return Temperature.convert_to_celsius(self._temperature)
        return self._temperature
    
    def get_temperature_farenheit(self):
        if self._metric == 'C':
            return Temperature.convert_to_farenheit(self._temperature)
        return self._temperature
    
    @staticmethod
    def convert_to_celsius(f_val):
        return (5/9) * (f_val - 32)
    
    @staticmethod
    def convert_to_farenheit(c_val):
        return (9/5 * c_val) + 32
    

