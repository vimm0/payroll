from django.urls import path
from .views import PayRollListView, AttendanceListView, EmployeeListView

urlpatterns = [
    path('', PayRollListView.as_view()),
    path('attendance/', AttendanceListView.as_view()),
    path('employee/', EmployeeListView.as_view()),

]
