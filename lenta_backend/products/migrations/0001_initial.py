# Generated by Django 4.2.5 on 2023-10-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=32, unique=True, verbose_name='SKU товара')),
                ('group', models.CharField(max_length=32, verbose_name='Группа товара')),
                ('category', models.CharField(max_length=32, verbose_name='Категория товара')),
                ('subcategory', models.CharField(max_length=32, verbose_name='Подкатегория товара')),
                ('uom', models.CharField(max_length=1, verbose_name='Маркер единицы измерения товара')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('pk',),
            },
        ),
    ]
