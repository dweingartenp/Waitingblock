#models
import uuid
import django_tables2 as tables
import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
#from django.utils.timesince import timesince
from django.utils.timezone import utc
from phonenumber_field.modelfields import PhoneNumberField
#from django_tables2 import MultiTableMixin
#from django.forms import ModelForm


class Restaurant(models.Model):
    restaurant_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contact = PhoneNumberField(blank=True)

BOOL_CHOICES = ((True, 'Waiting'), (False,'Seated'))

class Customer(models.Model):
#    name = models.CharField(max_length=30)
    name = models.CharField(primary_key=True, max_length=30)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    partysize = models.IntegerField()
    arrival_time = models.DateTimeField(auto_now_add=True, blank=True)
    contact = PhoneNumberField(blank=True)
    status = models.BooleanField(choices=BOOL_CHOICES)

    def get_time_diff(self):
        if self.arrival_time:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.arrival_time
            return timediff.total_seconds()

    wait = get_time_diff

    def __str__(self):
        return self.name

        class Meta:
            verbose_name = 'Customer'
            verbose_name_plural = 'Customers'
            ordering = ['-arrival_time']
