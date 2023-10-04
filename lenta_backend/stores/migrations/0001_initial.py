# Generated by Django 4.2.5 on 2023-10-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=32, unique=True, verbose_name='Магазин')),
                ('city', models.CharField(max_length=32, verbose_name='Город')),
                ('division', models.CharField(max_length=32, verbose_name='Подразделение')),
                ('type_format', models.PositiveSmallIntegerField(verbose_name='Формат магазина')),
                ('location', models.PositiveSmallIntegerField(verbose_name='Локация магазина')),
                ('size', models.PositiveSmallIntegerField(verbose_name='Размер магазина')),
                ('is_active', models.BooleanField(verbose_name='Флаг активного магазина')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Адрес магазина')),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'магазины',
                'ordering': ('pk',),
            },
        ),
    ]
