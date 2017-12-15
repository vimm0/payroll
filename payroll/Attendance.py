class Attendance:
    """
       Keep track of attendance of employee.
    """
    def __init__(self):
        self.total_days = 30
        self.present_days = 20

    def get_total_days(self):
        return "Total days: " + str(self.total_days) + " days"

    def employee_present_days(self):
        return "Present days: " + str(self.present_days) + " days"