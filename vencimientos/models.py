from django.db import models

PERIODICIDAD = [
    ('A', 'Anual'),
    ('M', 'Mensual'),
    ('B', 'Bimestral'),
    ('T', 'Trimestral'),
    ('C', 'Cuatrimestral'),
]


class Agency(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'agencies'


class Tax(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True, null=True)
    periodicidad = models.CharField(max_length=1, choices=PERIODICIDAD, default='M')

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.tax} - {self.criteria} - {self.value} - {self.day}'


class DueDate(models.Model):
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    period = models.DateField()
    value = models.SmallIntegerField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        this_due_date = self.due_date.strftime('%d/%m/%Y')
        this_period = self.period.strftime('%m/%Y')

        return f'{self.tax} - {self.criteria} - {self.value} - {this_period} - {this_due_date}'


class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True, null=True)
    cuit = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'companies'


class CompaniesDueDate(models.Model):
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    period = models.DateField()
    due_date = models.DateField()

    def __str__(self) -> str:
        this_due_date = self.due_date.strftime('%d/%m/%Y')
        this_period = self.period.strftime('%m/%Y')

        return f'{self.tax} - {self.company} - {this_period} - {this_due_date}'


class Holiday(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.date} - {self.description}'
