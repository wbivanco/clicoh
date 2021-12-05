from rest_framework import viewsets
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.response import Response

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

    def create(self, request):
        import json
        data = request.data
        serializer = OrderDetailSerializer(data=data)

        if serializer.is_valid():
            order = json.loads(data['order'])

            if order:
                order_id = order['id']
                product = json.loads(data['product'])
                product_id = product['id']

                count_order_detail = OrderDetail.objects.filter(product__id=product_id).filter(order__id=order_id).count()

                if count_order_detail > 0:
                    raise serializers.ValidationError({"detail": "Ya existe ese producto en la orden."})
                else:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)