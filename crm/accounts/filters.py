import django_filters

#to create date filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    #gte greater than or equal to #lte less than or equal to
    start_date = DateFilter(field_name="date_created",lookup_expr="gte")
    end_date = DateFilter(field_name="date_created",lookup_expr="lte")
    #search my note, CharFilter #icontains means ignore case sensetivity
    note = CharFilter(field_name="note",lookup_expr="icontains")

    class Meta:
        model = Order
        fields = '__all__'
        # excludes some fields from what __all__ renders
        exclude = ['customer','date_created']