from rest_framework import mixins
from users.models import User
from stores.models import Store
from sales.models import Sale
import serializers


class UserViewSet(mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class StoreViewSet(mixins.ListModelMixin):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer


class SaleViewSet(mixins.ListModelMixin):
    queryset = Sale.objects.all()
    serializer_class = serializers.SaleSerializer
