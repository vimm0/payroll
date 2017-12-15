from .Input import name, position, salary


class Employee:
    """
       Keep information of employee and their information.
    """

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_employee_name(self):
        return "Employee Name: " + str(self.name)

    def get_position(self):
        return "Position: " + str(self.position)

    def get_salary(self):
        return "Salary: " + str(self.salary)


# if __name__ == "__main__":
#     p = Employee(name, position, salary)
#     print(p.get_position())
