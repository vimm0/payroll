from django.shortcuts import render
from django.views.generic import ListView

from .models import PayRoll, Employee, Attendance


class EmployeeListView(ListView):
    queryset = Employee.objects.all()


class PayRollListView(ListView):
    queryset = PayRoll.objects.all().select_related('name')


class AttendanceListView(ListView):
    queryset = Attendance.objects.all().select_related('name')
