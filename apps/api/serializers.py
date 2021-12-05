from rest_framework_json_api import serializers

from .models import Product, Order, OrderDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, name):
        """ Valido que el nombre del producto no esté repetido."""

        name = name.lower()

        if Product.objects.filter(name=name).exists():
            raise serializers.ValidationError('El producto {} ya esxiste.'.format(name))
        return name

    def validate_stock(self, stock):
        """ Valido que el stock del producto no sea negativo. """

        if stock < 0:
            raise serializers.ValidationError('El stock no puede ser negativo.')
        return stock

    def validate_price(self, price):
        """ Valido que el precio del producto no sea genativo. """

        if price < 0:
            raise serializers.ValidationError('El precio no puede ser nagativo.')
        return price


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


    def validate_quantity(self, quantity):
        """ Valido que la cantidad a comprar sea mayor que cero."""

        if quantity <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor que 0.')
        return quantity

    def validate_product(self, product):
        """ Valido que el producto tenga estock para la venta."""

        product = Product.objects.get(pk=product.id)

        if product.stock <= 0:
            raise serializers.ValidationError('No hay stock del producto {}.'.format(product.name))
        return product


class OrderSerializer(serializers.ModelSerializer):
    detail = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('datetime', 'get_total', 'get_total_usd', 'detail')
