from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)
    suspend_status = models.BooleanField()
    martial_status = models.BooleanField()

    def __str__(self):
        return self.name


class Attendance(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_present_days = models.IntegerField(default=0)
    total_days = models.IntegerField(default=30)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


# Sum is deducted from the payment.
class Tax(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        payment = Payroll.objects.get(name=self.name)
        # Married
        if Employee.objects.get(name=self.name, martial_status=True):
            tax_percent = 1
            self.amount = tax_percent / 100 * payment
        # Unmarried
        elif Employee.objects.get(name=self.name, martial_status=False):
            tax_percent = 1.5
            self.amount = tax_percent / 100 * payment
        super(Tax, self).save(*args, **kwargs)


class ProvidentFund(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    sum_total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.sum_total += self.amount
        super(ProvidentFund, self).save(*args, **kwargs)


# Sum is added to the payment
class Incentive(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Compensation(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Each day payment
        attendee_name = Attendance.objects.get(name=self.name)
        emp_incentive = Incentive.objects.get(name=self.name)
        # if emp_incentive.created_on > timezone.now:
        #     self.amount = 0 (warning: Future incentive is not possible.)
        # elif emp_incentive.created_on <= timezone.now and only for present month:
        #     emp_incentive_amount
        employee = Employee.objects.get(name=self.name)

        # if Employee.objects.get(name=self.name, suspension_status=True):
        #     self.amount = 0
        # elif Employee.objects.get(name=self.name, suspension_status=False):
        #     add amount of every day sum of personal with his own rate <--- create variable and add below

        total_days = attendee_name.total_days
        salary = employee.salary
        self.amount = salary / total_days + emp_incentive
        # count_suspension_status for counting active days
        # then multiply active days with the above amount for each day
        pass


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
        present_days = attendee_name.total_present_days
        total_days = attendee_name.total_days
        salary = employee.salary
        self.payment = salary / total_days * present_days
        super(Payroll, self).save(*args, **kwargs)
