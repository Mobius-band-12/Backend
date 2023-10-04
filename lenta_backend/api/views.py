from rest_framework import mixins, viewsets
from users.models import User
from products.models import Product
from stores.models import Store
from sales.models import Forecast, Sale
from . import serializers


class UserViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class StoreViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer


class SaleViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class ForecastViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Forecast.objects.all()
        
    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.PostForecastSerializer
        return serializers.GetForecastSerializer


class ProductViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer