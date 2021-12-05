from rest_framework_json_api import serializers

from .models import Product, Order, OrderDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, name):
        name = name.lower()

        if Product.objects.filter(name=name).exists():
            raise serializers.ValidationError('El producto {} ya esxiste.'.format(name))
        return name

    def validate_stock(self, stock):
        if stock < 0:
            raise serializers.ValidationError('El stock no puede ser negativo.')
        return stock

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('El precio no puede ser nagativo.')
        return price


class OrderSerializer(serializers.ModelSerializer):
    detail = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ('datetime', 'get_total', 'get_total_usd', 'detail')


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

    included_serializers = {
        'product': ProductSerializer,
        'order': OrderSerializer,
    }

    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor que 0.')
        return quantity

    def validate_product(self, product):
        product = Product.objects.get(pk=product.id)

        if product.stock <= 0:
            raise serializers.ValidationError('No hay stock del producto {}.'.format(product.name))
        # if OrderDetail.objects.filter(product__id = product.id).filter(id = obj.id).exists:
        #     raise serializers.ValidationError('El producto {} ya esta cargada en la orden.'.format(product))
        return product