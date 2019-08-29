class Address:
    def __init__(self, address, state, city, country, number, zipcode=None,):
        self.address = address
        self.city = city
        self.state = state
        self._zip = zipcode
        self.country = country
        self.number = number
    
    @property
    def get_address(self):
        return self.address + ',\n' + self.city + ', ' + self.state + '\n' + self._zip + ', ' + self.country
    
    @property
    def Contact(self):
        return 'Contact: ' + str(self.number)