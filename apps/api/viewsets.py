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
        """ Sobreescribo el método para verificar que el producto no esté repetido en la orden."""

        import json
        data = request.data
        serializer = OrderDetailSerializer(data=data)

        if serializer.is_valid():
            order = json.loads(data['order'])
            product = json.loads(data['product'])

            # Valido que haya existencia suficiente para cubrir la cantidad pedida.
            if product['stock'] < data['quantity']:
                raise serializers.ValidationError(
                    {"detail": "La cantidad solicitada es mayor que la existente({}).".format(product['stock'])})

            # Verifico si hay orden(ya hubo alta) sino no verifico(primer registro en el detalle de la orden).
            if order:
                order_id = order['id']
                product_id = product['id']

                # Verifico si el producto esta en la orden.
                count_order_detail = OrderDetail.objects.filter(product__id=product_id).filter(order__id=order_id).count()

                if count_order_detail > 0:
                    raise serializers.ValidationError({"detail": "Ya existe ese producto en la orden."})
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)