from django_filters import rest_framework as filters
from .models import Car


class CarFilter(filters.FilterSet):
    brand = filters.CharFilter()
    model = filters.CharFilter()
    year = filters.CharFilter()
    fuel_type = filters.CharFilter()
    transmission = filters.CharFilter()
    mileage = filters.RangeFilter()
    price = filters.RangeFilter()

    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price']
