#tables

import django_tables2 as tables
#import datetime
#from django.utils import timezone
#from django.utils.timezone import utc
from django_tables2.utils import A
from .models import Customer

class CustomerTable(tables.Table):
    name = tables.Column()
    wait = tables.Column()
    partysize = tables.Column()
    arrival_time = tables.Column()
    status = tables.Column()
    contact = tables.Column()
    seat = tables.LinkColumn('status_update', accessor='pk', text='✔️')

    class Meta:
        data = Customer.objects.all()


class CustomerUpdateTable(tables.Table):
    name = tables.Column()
    wait = tables.Column()
    partysize = tables.Column()
    arrival_time = tables.Column()
    status = tables.Column()
    contact = tables.Column()

    class Meta:
#        data = Customer.objects.get(pk=self.kwargs.get('pk'))
        data = Customer.objects.all()

#class CustomerTable(tables.Table):
#    name = tables.LinkColumn('customer-detail', args=[A,('pk')])
#    wait = tables.LinkColumn('customer-detail', args=[A,('pk')])
#    partysize = tables.LinkColumn('customer-detail', args=[A,('pk')])
#    status = tables.LinkColumn('customer-detail', args=[A,('pk')])
#
#    class Meta:
#        model = Customer
#        fields = ('name', 'partysize', 'contact', 'arrival_time')
#        attrs = {"class": "table-striped table-bordered"}
#        empty_text = "No matching customers"
