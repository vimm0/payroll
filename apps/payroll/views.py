from django.shortcuts import render
from django.views.generic import ListView

from .models import Payroll, Employee, Attendance


class EmployeeListView(ListView):
    queryset = Employee.objects.all()


class PayRollListView(ListView):
    queryset = Payroll.objects.all().select_related('name')

    # def get_context_data(self, **kwargs):
    #     context = super(PayRollListView, self).get_context_data(**kwargs)  # get the default context data
    #     context['employee'] = Employee.objects.all()
    #     context['attendance'] = Attendance.objects.all()
    #     return context


class AttendanceListView(ListView):
    queryset = Attendance.objects.all().select_related('name')
