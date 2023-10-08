from django.db import models


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
    )
    location = models.PositiveSmallIntegerField(
        'Локация магазина',
    )
    size = models.PositiveSmallIntegerField(
        'Размер магазина',
    )
    is_active = models.BooleanField(
        'Флаг активного магазина',
    )
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
