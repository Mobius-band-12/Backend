from django.db import models


class Store(models.Model):
    store_id = models.CharField(
        'id магазина',
        max_length=32,
        blank=True,
    )
    city_id = models.CharField(
        'id города',
        max_length=32,
        blank=True,
    )
    dividion_id = models.CharField(
        'id подразделения',
        max_length=32,
        blank=True,
    )
    format_id = models.CharField(
        'id типа формата магазина',
        max_length=1,
        blank=True,
    )
    location_id = models.CharField(
        'id типа локации магазина',
        max_length=1,
        blank=True,
    )
    size_id = models.CharField(
        'id типа размера магазина',
        max_length=2,
        blank=True,
    )
    is_active = models.BooleanField(
        'Флаг активного магазина',
    )
