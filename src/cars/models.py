from django.db import models


class Car(models.Model):
    FUEL_OPTIONS = (
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
        ('электричество', 'электричество'),
        ('гибрид', 'гибрид')
    )
    TRANSMISSION_OPTIONS = (
        ('механическая', 'механическая'),
        ('автоматическая', 'автоматическая'),
        ('вариатор', 'вариатор'),
        ('робот', 'робот')
    )
    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    fuel_type = models.CharField(choices=FUEL_OPTIONS, verbose_name='Тип топлива', max_length=40)
    transmission = models.CharField(choices=TRANSMISSION_OPTIONS, verbose_name='Тип КПП', max_length=40)
    mileage = models.IntegerField(verbose_name='Пробег')
    price = models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Автомоболь'
        verbose_name_plural = 'Автомоболи'
