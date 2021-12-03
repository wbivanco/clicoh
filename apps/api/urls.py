from django.urls import path
from rest_framework import routers

from .viewsets import ProductViewSet, OrderViewSet, OrderDetailViewSet

route = routers.SimpleRouter()
route.register('product', ProductViewSet)
route.register('order', OrderViewSet)
route.register('order_detail', OrderDetailViewSet)

urlpatterns = route.urls

