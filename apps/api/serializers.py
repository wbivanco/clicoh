from rest_framework_json_api import serializers

from .models import Product, Order, OrderDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, name):
        name = name.lower()

        if Product.objects.filter(name=name).exist():
            raise serializers.ValidationError('El producto {} ya esxiste'.format(name))
        return name


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('datetime',)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    included_serializers = {
        'product': ProductSerializer,
        'order': OrderSerializer,
    }