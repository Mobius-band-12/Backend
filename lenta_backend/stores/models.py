from django.db import models


class Store(models.Model):
    hashed_store_id = models.CharField(
        'Хешированный id магазина',
        max_length=32,
    )
    store_id = models.CharField(
        'id магазина',
        max_length=32,
        blank=True,
    )
    hashed_city_id = models.CharField(
        'Хешированный id города',
        max_length=32,
    )
    city_id = models.CharField(
        'id города',
        max_length=32,
        blank=True,
    )
    hashed_dividion_id = models.CharField(
        'Хешированный id подразделения',
        max_length=32,
    )
    dividion_id = models.CharField(
        'id подразделения',
        max_length=32,
        blank=True,
    )
    hashed_format_id = models.CharField(
        'Хешированный id типа формата магазина',
        max_length=1,
    )

    format_id = models.CharField(
        'id типа формата магазина',
        max_length=1,
        blank=True,
    )
    hashed_location_id = models.CharField(
        'Хешированный id типа локации магазина',
        max_length=1,
    )
    location_id = models.CharField(
        'id типа локации магазина',
        max_length=1,
        blank=True,
    )
    hashed_size_id = models.CharField(
        'Хешированный id типа размера магазина',
        max_length=2,
    )
    size_id = models.CharField(
        'id типа размера магазина',
        max_length=2,
        blank=True,
    )
    is_active = models.BooleanField(
        'Флаг активного магазина',
    )
