from . import Attendance
from . import Employee


class PayRoll:
    """
    Calculate the total payment company pay to their employee.
    """

    def __init__(self, attendance, employee):
        self.attendance = attendance
        self.employee = employee

    def each_day_payroll(self):
        total_days = self.attendance.total_days
        salary = self.employee.salary
        each_day_payment = salary / total_days
        return each_day_payment

    def get_payroll(self):
        present_days = self.attendance.present_days
        payment = self.each_day_payroll() * present_days
        return 'Total Payment: ' + str(payment)


if __name__ == "__main__":
    attendance = Attendance()
    employee = Employee()

    p = PayRoll(attendance, employee)
    print(p.get_payroll())
