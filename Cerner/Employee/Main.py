import Employee
from Payroll import Payroll

def create_regular_employee(name, wage=None):
    return Employee.RegularEmployee(name, wage)

def create_contract_employee(name, rate=46):
    return Employee.ContractEmployee(name, rate)

def create_manager(name):
    return Employee.Manager(name)

def main():
    adam = create_contract_employee('Adam')
    dan = create_regular_employee('Dan', 7500)
    fran = create_contract_employee('Fran', 44.6)
    jay = create_contract_employee('Jay', 65)
    dan1 = create_manager('Dan')
    frank = create_manager('Frank')
    dan1.assign_employee(adam)
    dan1.assign_employee(dan)
    frank.assign_employee(fran)
    frank.assign_employee(jay)
    managers = [dan1, frank]
    frank.set_employee_time(fran, 65)
    frank.set_employee_time(jay, 35)
    dan1.set_employee_time(adam, 45)

    p = Payroll()
    p.add_managers(managers)
    p.payroll()

if __name__ == "__main__":
    main()