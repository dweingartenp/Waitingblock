#filters

import django_filters
from .models import Customer


class CustomerListFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['name', 'partysize', 'arrival_time', 'status']
        order_by = ['pk']
