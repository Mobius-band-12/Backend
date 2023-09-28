from django.contrib.gis.db import models as geo_models
from django.db import models


class Store(models.Model):
    store_id = models.CharField(
        'ID магазина',
        max_length=32,
    )
    city_id = models.CharField(
        'ID города',
        max_length=32,
    )
    city_name = models.CharField(
        'Город',
        max_length=32,
        blank=True,
    )
    dividion_id = models.CharField(
        'ID подразделения',
        max_length=32,
    )
    dividion_name = models.CharField(
        'Название подразделения',
        max_length=32,
        blank=True,
    )
    format_id = models.PositiveSmallIntegerField(
        'id типа формата магазина',
        max_length=1,
    )
    format_name = models.CharField(
        'Тип формата магазина',
        max_length=32,
        blank=True,
    )
    location_type_id = models.PositiveSmallIntegerField(
        'id типа локации магазина',
        max_length=1,
    )
    location_type_name = models.CharField(
        'Тип локации магазина',
        max_length=32,
        blank=True,
    )
    size_type_id = models.PositiveSmallIntegerField(
        'id типа размера магазина',
        max_length=2,
    )
    size_type_name = models.CharField(
        'тип размера магазина',
        max_length=32,
        blank=True,
    )
    is_active = models.BooleanField(
        'Флаг активного магазина',
    )
    location = geo_models.PointField(
        'Географические координаты',
        geography=True,
        null=True,
    )
    address = models.CharField(
        'Адрес магазина',
        max_length=2,
        blank=True,
    )

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'
        ordering = ('pk',)

    def __str__(self):
        return self.name
