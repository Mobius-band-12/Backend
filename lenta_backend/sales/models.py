from django.db import models
from products.models import Product
from stores.models import Store


class Sale(models.Model):
    '''Модель для хранения данных о фактических продажах.'''

    store = models.ForeignKey(
        Store,
        to_field='store',
        on_delete=models.CASCADE,
        verbose_name='Магазин',
        max_length=32,
    )
    sku = models.ForeignKey(
        Product,
        to_field='sku',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        max_length=32,
    )
    date = models.DateField(
        'Дата продажи',
    )
    is_promo = models.BooleanField(
        'Флаг промо',
    )
    sales_units = models.PositiveSmallIntegerField(
        'Число продаж без признака промо',
        default=0,
    )
    sales_units_promo = models.PositiveSmallIntegerField(
        'Число продаж с признаком промо',
        default=0,
    )
    sales_rub = models.PositiveIntegerField(
        'Продажи без признака промо в руб.',
        default=0,
    )
    sales_rub_promo = models.PositiveIntegerField(
        'Продажи с признаком промо в руб.',
        default=0,
    )

    class Meta:
        verbose_name = 'продажи'
        verbose_name_plural = 'продажи'
        ordering = ('pk',)

    def __str__(self):
        return f'Продажи товара {self.product_id} за {self.date}'


class Forecast(models.Model):
    '''Модель для хранения данных о прогнозных продажах.'''

    store = models.ForeignKey(
        Store,
        to_field='store',
        on_delete=models.CASCADE,
        verbose_name='Магазин',
        max_length=32,
    )
    forecast_date = models.DateField(
        'Дата прогнозной продажи',
    )
    sku = models.ForeignKey(
        Product,
        to_field='sku',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        max_length=32,
        null=True
    )
    forecast = models.JSONField(
        'Прогнозные продажи',
    )

    class Meta:
        verbose_name = 'прогнозные продажи'
        verbose_name_plural = 'прогнозные продажи'
        ordering = ('pk',)

    def __str__(self):
        return f'''Прогнозные продажи товара {self.sku}
                за {self.forecast_date}'''
