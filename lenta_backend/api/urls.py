from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


API_V1 = 'v1/'

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', views.UserViewSet, basename='users')  # если будет ЛК, иначе убрать
router_v1.register('categories', views.ProductViewSet, basename='categories')
router_v1.register('shops', views.StoreViewSet, basename='shops')
router_v1.register('sales', views.SaleViewSet, basename='sales')
router_v1.register('forecast', views.ForecastViewSet, basename='forecast')


urlpatterns = [
    path(API_V1, include(router_v1.urls)),
]
