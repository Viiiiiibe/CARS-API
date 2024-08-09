from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price')
    search_fields = ('pk', 'brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price')
    list_filter = ('brand', 'fuel_type', 'transmission')


admin.site.register(Car, CarAdmin)
