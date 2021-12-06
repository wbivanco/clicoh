from django.urls import path
from rest_framework import routers

from .viewsets import ProductViewSet, OrderViewSet, OrderDetailViewSet
from .views import login

route = routers.SimpleRouter()
route.register('product', ProductViewSet)
route.register('order', OrderViewSet)
route.register('orderdetail', OrderDetailViewSet)

urlpatterns = route.urls

urlpatterns += path('login', login),
