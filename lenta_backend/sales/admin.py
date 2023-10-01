from django.contrib import admin
from .models import Sale, Forecast


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    pass
