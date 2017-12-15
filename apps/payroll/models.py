from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    present_days = models.IntegerField(default=0)
    total_days = models.IntegerField(default=30)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Payroll(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    payment = models.PositiveIntegerField(default=0, editable=False)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        attendee_name = Attendance.objects.get(name=self.name)
        employee = Employee.objects.get(name=self.name)
        present_days = attendee_name.present_days
        total_days = attendee_name.total_days
        salary = employee.salary
        self.payment = salary / total_days * present_days
        super(Payroll, self).save(*args, **kwargs)
