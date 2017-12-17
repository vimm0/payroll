from django.views.generic import ListView

from .models import PayRoll, Employee, Attendance, Addition, Deduction, MonthlySheet


class EmployeeListView(ListView):
    queryset = Employee.objects.all()


class PayRollListView(ListView):
    queryset = PayRoll.objects.all().select_related('name', 'monthly_sheet')

    # def get_context_data(self, **kwargs):
    #     context = super(PayRollListView, self).get_context_data(**kwargs)  # get the default context data
    #     context['monthly_sheet'] = MonthlySheet.objects.all()  # add extra field to the context
    #     return context


class AttendanceListView(ListView):
    queryset = Attendance.objects.all().select_related('name')


class AdditionListView(ListView):
    queryset = Addition.objects.all().select_related('incentive_entry', 'compenstation_entry')


class DeductionListView(ListView):
    queryset = Deduction.objects.all().select_related('tax_entry', 'provident_entry')
