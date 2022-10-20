class Employee:

    def __init__(self,employee_name,employee_salary,employee_email):
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.employee_email = employee_email




    def __dict__(self):
        pass

    def __module__(self):
        pass


print(type(Employee))