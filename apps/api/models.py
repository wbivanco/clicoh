from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

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

    def __str__(self):
        return '{}'.format(self.id)

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

    order = models.ForeignKey(Order, related_name='detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.order, self.product)

    class Meta:
        verbose_name_plural = "Detalle Ordenes"
        verbose_name = "Detalle Orden"


@receiver(post_save, sender=OrderDetail)
def orderdetail_save(sender, instance, **kwargs):
    """ Resto la cantidad pedida del stock del producto."""
    product_id = instance.product.id

    prod = Product.objects.get(pk=product_id)
    if prod:
        prod.stock = int(prod.stock) - int(instance.quantity)
        prod.save()


@receiver(post_delete, sender=OrderDetail)
def orderdetail_delete(sender, instance, **kwargs):
    """ Sumo la cantidad pedida al stock del producto."""
    product_id = instance.product.id

    prod = Product.objects.get(pk=product_id)
    if prod:
        prod.stock = int(prod.stock) + int(instance.quantity)
        prod.save()
