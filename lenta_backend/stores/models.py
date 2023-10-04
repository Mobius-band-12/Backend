# from django.contrib.gis.db import models as geo_models
from django.db import models


# 'max_length' is ignored when used with PositiveSmallIntegerField
class Store(models.Model):
    store = models.CharField(
        'Магазин',
        max_length=32,
        unique=True,
    )
    city = models.CharField(
        'Город',
        max_length=32,
    )
    division = models.CharField(
        'Подразделение',
        max_length=32,
    )
    type_format = models.PositiveSmallIntegerField(
        'Формат магазина',
        # max_length=1,
    )
    location = models.PositiveSmallIntegerField(
        'Локация магазина',
        # max_length=1,
    )
    size = models.PositiveSmallIntegerField(
        'Размер магазина',
        # max_length=2,
    )
    is_active = models.BooleanField(
        'Флаг активного магазина',
    )
    # loc_point = geo_models.PointField(
    #     'Географические координаты',
    #     geography=True,
    #     null=True,
    # )
    address = models.CharField(
        'Адрес магазина',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'
        ordering = ('pk',)

    def __str__(self):
        return f'Магазин {self.store}'
