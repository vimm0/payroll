from django.urls import path
from .views import PayRollListView, AttendanceListView, EmployeeListView

urlpatterns = [
    path('', PayRollListView.as_view(), name='payroll'),
    path('attendance/', AttendanceListView.as_view(), name='attendance'),
    path('employee/', EmployeeListView.as_view(), name='employee'),

]
