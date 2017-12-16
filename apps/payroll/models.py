from django.db import models
from django.utils import timezone

martial_status = [('Married', 'Married'), ('Unmarried', 'Unmarried')]


class EmployeeStatus(models.Model):
    suspended = models.BooleanField(default=False)
    married = models.CharField(max_length=10, choices=martial_status, default='Unmarried')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.married

    class Meta:
        verbose_name_plural = "0. Employee Statuses"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)
    status = models.ForeignKey(EmployeeStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1. Employees"


class Attendance(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_present_days = models.IntegerField(default=0)
    total_days = models.IntegerField(default=30)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "2. Attendance"


# Sum is added to the payment
class Incentive(models.Model):
    """
    Extra money provided to encourage the Employee's work.
    """
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255, default='Not mentioned.')
    amount = models.IntegerField(default=0)
    sum_total = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.sum_total += self.amount
        super(Incentive, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "3. Incentive"


class Compensation(models.Model):
    """
    Compensation is the money provided to the employee if he/she resign/suspend
    from his/her job and company will pay the sum of money he/she work till
    the suspension day.
    """
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_entry = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    # def save(self, *args, **kwargs):
    #     import pdb
    #     pdb.set_trace()
    #     if self.name.suspended == True:
    #         total_days = self.attendance_entry.total_days
    #         present_days = self.attendance_entry.total_present_days
    #         self.amount = self.name.salary / total_days * present_days
    #
    #     super(Compensation, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "4. Compensation"


class Addition(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    incentive_entry = models.ForeignKey(Incentive, on_delete=models.CASCADE)
    compenstation_entry = models.ForeignKey(Compensation, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "5. Addition"

    def save(self, *args, **kwargs):
        self.amount = self.incentive_entry.amount + self.compenstation_entry.amount

        super(Addition, self).save(*args, **kwargs)


# Sum is deducted from the payment.
class Tax(models.Model):
    """
    Deduce tax and keep track of the total amont deduced in employee working years.
    """
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    percent = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        emp_salary = self.name.salary
        self.amount = self.percent / 100 * emp_salary
        super(Tax, self).save(*args, **kwargs)

        # samples = Sample.objects.filter(sampledate__gt=datetime.date(2011, 1, 1), sampledate__lt=datetime.date(2011, 1, 31))

    class Meta:
        verbose_name_plural = "6. Tax"


class ProvidentFund(models.Model):
    """"
    Deduct the amount monthly basis but sum up monthly deducted amount.
    """
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    sum_total = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.sum_total += self.amount
        super(ProvidentFund, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "7. ProvidentFund"


class Deduction(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    provident_entry = models.ForeignKey(ProvidentFund, on_delete=models.CASCADE)
    tax_entry = models.ForeignKey(Tax, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    # updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.amount = self.tax_entry.amount + self.provident_entry.amount
        super(Deduction, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "8. Deduction"


class MonthlySheet(models.Model):
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.end)

    class Meta:
        verbose_name_plural = "9. Monthly Sheets"


class PayRoll(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    monthly_sheet = models.ForeignKey(MonthlySheet, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255, default='Not mentioned.')
    payment = models.PositiveIntegerField(default=0)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        attendee_name = Attendance.objects.get(name=self.name)
        employee = Employee.objects.get(name=self.name)
        taxee = employee.tax_set.get(name=self.name)
        emp_provident_fund = employee.providentfund_set.get(name=self.name)

        present_days = attendee_name.total_present_days
        total_days = attendee_name.total_days
        salary = employee.salary
        self.payment = salary / total_days * present_days

        # # # deduction part
        tax_amount = taxee.percent / 100 * self.payment
        self.payment = self.payment - tax_amount - emp_provident_fund.amount
        super(PayRoll, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = " PayRoll"
