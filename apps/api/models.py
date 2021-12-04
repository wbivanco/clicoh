from django.db import models

from .services import get_dollar_blue_value


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"


class Order(models.Model):
    datetime = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Ordenes"
        verbose_name = "Orden"

    def get_total(self):
        ods = OrderDetail.objects.filter(order_id=self.id)

        return sum(float(od.product.price) * od.quantity for od in ods)

    def get_total_usd(self):
        pesos_value = self.get_total()

        dolar_value = get_dollar_blue_value().replace(',','.')

        dolar_price= pesos_value * float(dolar_value)
        return dolar_price


class OrderDetail(models.Model):
    quantity = models.IntegerField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.order, self.product)

    class Meta:
        verbose_name_plural = "Detalle Ordenes"
        verbose_name = "Detalle Orden"
