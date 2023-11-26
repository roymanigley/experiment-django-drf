from django.db import models
from django.utils.timezone import now


class Account(models.Model):
    class Type(models.Choices):
        ACTIVE = 'ACTIVE'
        PASSIVE = 'PASSIVE'
        EXPENSE = 'EXPENSE'
        REVENUE = 'REVENUE'

    number = models.IntegerField(null=False, unique=True)
    name = models.CharField(null=False, blank=False, max_length=100)
    type = models.CharField(null=False, blank=False, max_length=100, choices=Type.choices)


class Booking(models.Model):
    date = models.DateField(null=False)
    debit_account = models.ForeignKey(Account, related_name='debit_booking', null=False, on_delete=models.DO_NOTHING)
    credit_account = models.ForeignKey(Account, related_name='credit_booking', null=False, on_delete=models.DO_NOTHING)
    amount = models.FloatField(null=False)
    remark = models.TextField(null=True)
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(default=now)
