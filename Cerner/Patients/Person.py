import Address

class Person:
    def __init__(self, fname, lname, age, address, race=None, ethnicity=None):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.address = address
        self. race = race
        self.ethnicity = ethnicity
    
    @property
    def fullname(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def profile(self):
        return 'Name: ' + self.fullname + '\n' + 'Address: ' + self.address.get_address + '\n' + self.address.Contact


if __name__ == "__main__":
    addy = Address.Address('8150 SW Barnes Rd', 'OR', 'Portland', 'USA', '609-491-6566', '95566')
    p1 = Person('Nana', 'Sim', 45, addy)
    #print(p1.profile)