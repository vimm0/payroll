from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Employee, Attendance, Tax, ProvidentFund, Addition, EmployeeStatus
from .models import PayRoll, MonthlySheet, Deduction, Incentive, Compensation

class EmployeeStatusAdmin(admin.ModelAdmin):
    list_display = [f.name for f in EmployeeStatus._meta.fields]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Employee._meta.fields]


class AttendanceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Attendance._meta.fields]


class IncentiveAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Incentive._meta.fields]


class CompensationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Compensation._meta.fields]

class AdditionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Addition._meta.fields]

class TaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tax._meta.fields]

class ProvidentFundAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProvidentFund._meta.fields]

class DeductionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Deduction._meta.fields]

class PayRollInlineAdmin (admin.TabularInline):
    model = PayRoll

class PayRollAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PayRoll._meta.fields]

class MonthlySheetAdmin(admin.ModelAdmin):
    inlines = [ PayRollInlineAdmin ]

admin.site.register(EmployeeStatus, EmployeeStatusAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)

admin.site.register(Incentive, IncentiveAdmin)
admin.site.register(Compensation, CompensationAdmin)
admin.site.register(Addition, AdditionAdmin)

admin.site.register(Tax, TaxAdmin)
admin.site.register(ProvidentFund, ProvidentFundAdmin)
admin.site.register(Deduction, DeductionAdmin)

admin.site.register(MonthlySheet, MonthlySheetAdmin)
admin.site.register(PayRoll, PayRollAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
