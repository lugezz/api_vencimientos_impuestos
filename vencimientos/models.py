from tabnanny import verbose
from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Tax(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('agency', 'name')
        verbose_name_plural = 'taxes'

    def __str__(self) -> str:
        return self.name


class Criteria(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class DueDateRule(models.Model):
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    value = models.SmallIntegerField()
    day = models.SmallIntegerField()
    next_month = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.tax} - {self.criteria} - {self.value} - {self.day}'


class DueDate(models.Model):
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    period = models.DateField()
    value = models.SmallIntegerField()
    due_date = models.DateField()

    def __str__(self) -> str:
        this_due_date = self.due_date.strftime('%d/%m/%Y')
        this_period = self.period.strftime('%m/%Y')

        return f'{self.tax} - {self.criteria} - {self.value} - {this_period} - {this_due_date}'
