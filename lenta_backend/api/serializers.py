from djoser import serializers as djoser_serializers
from rest_framework import serializers
from products.models import Product
from stores.models import Store
from sales.models import Sale, Forecast
from users.models import User


class UserSerializer(djoser_serializers.UserSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'position')


class GetTokenSerializer(djoser_serializers.TokenCreateSerializer):

    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('password', 'email')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('store', 'city', 'division', 'type_format', 'location',
                  'size', 'is_active', 'loc_point', 'address')
        model = Store


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('store', 'sku', 'date', 'is_promo', 'sales_units',
                  'sales_units_promo', 'sales_rub', 'sales_rub_promo')
        model = Sale


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('sku', 'group', 'category', 'subcategory', 'uom')


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'forecast_date', 'forecast')


class PostForecastSerializer(serializers.ModelSerializer):
    forecast = serializers.JSONField()

    class Meta:
        model = Forecast
        fields = ('store', 'forecast_date', 'forecast')
