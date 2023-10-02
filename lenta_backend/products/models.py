from django.db import models


class Product(models.Model):
    sku = models.CharField(
        'SKU товара',
        max_length=32,
        unique=True,
    )
    group = models.CharField(
        'Группа товара',
        max_length=32,
    )
    category = models.CharField(
        'Категория товара',
        max_length=32,
    )
    subcategory = models.CharField(
        'Подкатегория товара',
        max_length=32,
    )
    uom = models.CharField(
        'Маркер единицы измерения товара',
        max_length=1,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('pk',)

    def __str__(self):
        return self.sku