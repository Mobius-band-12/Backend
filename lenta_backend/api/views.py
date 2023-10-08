from datetime import datetime, timedelta
from django.db.models import Min, Sum
from django.shortcuts import get_object_or_404
from rest_framework import decorators, mixins, viewsets, response, status

from products.models import Product
from sales.models import Forecast, Sale
from stores.models import Store
from users.models import User
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

    def get_sale_data(self, sku, start_date, end_date, is_rub_included=False):
        if start_date:
            query = Sale.objects.filter(
                sku=sku,
                date__range=(start_date, end_date)
                ).values('date').annotate(
                    total_sales_units=Sum('sales_units')
                )
            if is_rub_included:
                query = query.annotate(total_sales_rub=Sum('sales_rub'))

            return serializers.FactSerializer(query, many=True)

        return []

    @decorators.action(methods=['GET'], detail=False, url_path='21-days')
    def sales_21_days(self, request):
        store = get_object_or_404(
            Store, store=request.query_params.get('store')
        ).store
        sku = get_object_or_404(
            Product, sku=request.query_params.get('sku')
        ).sku

        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=21)

        serialized_data = self.get_sale_data(sku, start_date, end_date, False)

        response_data = {
            "store": store,
            "sku": sku,
            "fact": serialized_data.data
        }

        return response.Response({"data": response_data},
                                 status=status.HTTP_200_OK)

    @decorators.action(methods=['GET'], detail=False, url_path='total')
    def sales_total(self, request):
        sku = get_object_or_404(
            Product, sku=request.query_params.get('sku')
            ).sku
        start_date = Sale.objects.aggregate(min_date=Min('date'))['min_date']
        end_date = request.query_params.get('end_date')

        end_date = (datetime.strptime(end_date, '%Y-%m-%d').date() if end_date
                    else datetime.now().date())

        serialized_data = self.get_sale_data(sku, start_date, end_date, True)

        response_data = {
            "sku": sku,
            "fact": serialized_data.data
        }

        return response.Response({"data": response_data},
                                 status=status.HTTP_200_OK)


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
