from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Employee, Attendance
from .models import Payroll


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Employee._meta.fields]


class AttendanceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Attendance._meta.fields]


class PayrollAdmin(admin.ModelAdmin):
    list_display = ('updated_on', 'name', 'payment')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Payroll, PayrollAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
