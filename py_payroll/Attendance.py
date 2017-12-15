# from __builtin__ import raw_input
from .Input import total_days, present_days


class Attendance:
    """
       Keep track of attendance of employee.
    """

    def __init__(self, total_days, present_days):
        self.total_days = total_days
        self.present_days = present_days

    def get_total_days(self):
        return "Total days: " + str(self.total_days) + " days"

    def employee_present_days(self):
        return "Present days: " + str(self.present_days) + " days"


        # @classmethod
        # def from_input(cls):
        #     return cls(raw_input('Name: '),
        #         int(raw_input('User ID: ')),
        #         int(raw_input('Reputation: ')),
        #     )


# if __name__ == "__main__":
#     a = Attendance(total_days, present_days)
#     print(a.get_total_days())
