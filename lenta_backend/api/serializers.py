from djoser import serializers as djoser_serializers
from products.models import Product
from rest_framework import serializers
from sales.models import Forecast, Sale
from stores.models import Store
from users.models import User


class UserSerializer(djoser_serializers.UserSerializer):
    '''Сериализатор для модели User.'''

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'position')


class GetTokenSerializer(djoser_serializers.TokenCreateSerializer):
    '''Сериализатор для получения токена авторизации.'''

    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('password', 'email')


class StoreSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Store.'''

    class Meta:
        fields = ('store', 'city', 'division', 'type_format', 'location',
                  'size', 'is_active', 'loc_point', 'address')
        model = Store


class SaleSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Sale.'''

    class Meta:
        fields = ('store', 'sku', 'date', 'is_promo', 'sales_units',
                  'sales_units_promo', 'sales_rub', 'sales_rub_promo')
        model = Sale


class FactSerializer(serializers.ModelSerializer):
    '''Вложенные сериализатор для модели Sale.'''

    total_sales_units = serializers.IntegerField()
    total_sales_rub = serializers.IntegerField(required=False)

    class Meta:
        fields = ('date', 'total_sales_units', 'total_sales_rub')
        model = Sale


class ProductSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Product.'''

    class Meta:
        model = Product
        fields = ('sku', 'group', 'category', 'subcategory', 'uom')


class ForecastSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Forecast.'''

    forecast = serializers.JSONField()

    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'forecast_date', 'forecast')


class DownloadForecastSerializer(serializers.ModelSerializer):
    '''Сериализатор для скачивания прогноза.'''

    class Meta:
        model = Forecast
        fields = ('forecast',)
