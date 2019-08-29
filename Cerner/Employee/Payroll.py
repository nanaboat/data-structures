class Payroll:
    emp_list = set()
    manager_list = set()
    def add_managers(self, manager):
        self.manager_list = set(manager)
    
    def calculate_payroll(self):
        payroll = []
        for manager in self.manager_list:
            payroll.append(sum(manager.calculate_employee_wages()))
        return payroll
    
    def payroll(self):
        import pdb; pdb.set_trace()
        total = self.calculate_payroll()
        print("---------Payroll -----------")
        for m, i in enumerate(self.manager_list):
            print("Manager: {0} has a wage bill of: {1}".format(i.name, total[m]))
        print("Total payroll is: {0}".format(sum(total)))
