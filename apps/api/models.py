from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Productos"


class Order(models.Model):
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = "Ordenes"


class OrderDetail(models.Model):
    cuantity = models.IntegerField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.order, self.product)

    class Meta:
        verbose_name = "Detalle Ordenes"
