from rest_framework import viewsets

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

    # def create(self, validated_data):
    #     product = validated_data.pop('product')
    #
    #     order = validated_data.
    #
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album