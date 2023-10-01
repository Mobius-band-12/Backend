from rest_framework import mixins
from stores.models import Store


class StoreViewSet(mixins.ListModelMixin):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer
