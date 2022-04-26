from .models import Car
from django_filter import CharFilter


class CarFilter(django_filter.FilterSet):
    make = CharFilter(field_name="make", lookup_expr='icontains')
    year = CharFilter(field_name="year", lookup_expr='icontains')
    class Meta:
        model = Car
        fields = ['make','year']