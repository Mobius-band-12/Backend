from django.db import models
from stores.models import Store
from products.models import Product


class Sale(models.Model):
    store_id = models.ForeignKey(
        Store,
        to_field='store_id',
        on_delete=models.CASCADE,
        verbose_name='id магазина',
        max_length=32,
    )
    product_id = models.ForeignKey(
        Product,
        to_field='product_id',
        on_delete=models.CASCADE,
        verbose_name='id товара',
        max_length=32,
    )
    date = models.DateField(
        'Дата продажи',
    )
    is_promo = models.BooleanField(
        'Флаг промо',
    )
    sales_in_units = models.PositiveSmallIntegerField(
        'Число проданных товаров без признака промо',
    )
    promo_sales_in_units = models.PositiveSmallIntegerField(
        'Число проданных товаров с признаком промо',
    )
    sales_in_rub = models.PositiveIntegerField(
        'Продажи без признака промо в руб.',
    )
    promo_sales_in_rub = models.PositiveIntegerField(
        'Продажи с признаком промо в руб.',
    )

    class Meta:
        verbose_name = 'продажи'
        verbose_name_plural = 'продажи'
        ordering = ('pk',)

    def __str__(self):
        return f'Продажи товара {self.product_id} за {self.date}'


class Forecast(models.Model):
    store_id = models.ForeignKey(
        Store,
        to_field='store_id',
        on_delete=models.CASCADE,
        verbose_name='id магазина',
        max_length=32,
    )
    product_id = models.ForeignKey(
        Product,
        to_field='product_id',
        on_delete=models.CASCADE,
        verbose_name='id товара',
        max_length=32,
    )
    forecast_date = models.DateField(
        'Дата прогнозной продажи',
    )
    forecast = models.PositiveIntegerField(
        'Прогнозные продажи',
    )

    class Meta:
        verbose_name = 'прогнозные продажи'
        verbose_name_plural = 'прогноные продажи'
        ordering = ('pk',)

    def __str__(self):
        return f'Прогнозные продажи товара {self.product_id} за {self.forecast_date}'
