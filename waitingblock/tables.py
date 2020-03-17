#tables

import django_tables2 as tables
from django_tables2.utils import A
from .models import Customer


class CustomerTable(tables.Table):
    name = tables.Column()
    wait = tables.Column(order_by=('arrival_time'))
    partysize = tables.Column()
    arrival_time = tables.Column()
    status = tables.Column()
    contact = tables.Column()
    seat = tables.LinkColumn('status_update', accessor='pk', text='✔️')

    class Meta:
        data = Customer.objects.all()


class CustomerUpdateTable(tables.Table):
    name = tables.Column()
    wait = tables.Column(order_by=('arrival_time'))
    partysize = tables.Column()
    arrival_time = tables.Column()
    status = tables.Column()
    contact = tables.Column()

    class Meta:
        data = Customer.objects.all()
