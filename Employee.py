class Employee:
    """
       Keep information of employee and their information.
    """

    def __init__(self):
        self.name = 'Santosh Chaudhary'
        self.position = 'Manager'
        self.salary = 45000

    def get_employee_name(self):
        return "Employee Name: " + str(self.name)

    def get_position(self):
        return "Position: " + str(self.position)

    def get_salary(self):
        return "Salary: " + str(self.salary)
