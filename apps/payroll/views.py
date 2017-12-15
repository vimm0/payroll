from django.shortcuts import render
from django.views.generic import ListView

from .models import Payroll, Employee, Attendance


class EmployeeListView(ListView):
    queryset = Employee.objects.all()


class PayRollListView(ListView):
    queryset = Payroll.objects.all().select_related('name')


class AttendanceListView(ListView):
    queryset = Attendance.objects.all().select_related('name')
