from django.contrib import admin

from .models import Forecast, Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    pass
