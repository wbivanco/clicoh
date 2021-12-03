from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Sum

from .models import Product, Order, OrderDetail

from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    @action(detail=True, methods=['get'])
    def get_total(self, requets, pk=None):
        queryset = OrderDetail.objects.get(id=self.id).aggregate(Sum('quantity'))
        serializer = OrderDetailSerializer(queryset, many=True)
        return Response(serializer.data)
        # sum(Decimal(product['price']) * od['quantity'] for product in self.product.values)