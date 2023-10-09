# Generated by Django 4.2.5 on 2023-10-04 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата продажи')),
                ('is_promo', models.BooleanField(verbose_name='Флаг промо')),
                ('sales_units', models.PositiveSmallIntegerField(verbose_name='Число продаж без признака промо')),
                ('sales_units_promo', models.PositiveSmallIntegerField(verbose_name='Число продаж с признаком промо')),
                ('sales_rub', models.PositiveIntegerField(verbose_name='Продажи без признака промо в руб.')),
                ('sales_rub_promo', models.PositiveIntegerField(verbose_name='Продажи с признаком промо в руб.')),
                ('sku', models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, to='products.product', to_field='sku', verbose_name='Товар')),
                ('store', models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, to='stores.store', to_field='store', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'продажи',
                'verbose_name_plural': 'продажи',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecast_date', models.DateField(verbose_name='Дата прогнозной продажи')),
                ('forecast', models.JSONField(verbose_name='Прогнозные продажи')),
                ('sku', models.ForeignKey(max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', to_field='sku', verbose_name='Товар')),
                ('store', models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, to='stores.store', to_field='store', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'прогнозные продажи',
                'verbose_name_plural': 'прогнозные продажи',
                'ordering': ('pk',),
            },
        ),
    ]
