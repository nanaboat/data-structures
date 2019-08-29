import abc

class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_wages(self):
        pass


class RegularEmployee(Employee):
    def __init__(self, name, wages=6000):
        self.name = name
        self.hours = 40
        self.wages = wages
    
    def calculate_wages(self):
        return self.wages


class ContractEmployee(Employee):
    def __init__(self, name, rate=30.5):
        self.name = name
        self.hours = 0.0
        self.rate = rate
    
    def calculate_wages(self):
        return (self.hours * self.rate)


class Manager:
    def __init__(self, name):
        self.name = name
        self.employeelist = set()
    
    def set_employees(self, emplist):
        self.employeelist += emplist
    
    def add_employee(self, emp):
        self.employeelist.add(emp)
    
    def calculate_employee_wages(self):
        wage_bill = []
        for emp in self.employeelist:
            wage_bill.append(emp.calculate_wages())
        return wage_bill
    
    def set_employee_time(self, emp, hrs):
        if emp in self.employeelist:
            emp.hours = hrs
        else:
            print("{0} doesn't manage {1}".format(self.name, emp.name))
    
    def assign_employee(self, emp):
        self.add_employee(emp)