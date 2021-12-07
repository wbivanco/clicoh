import pytest

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.api.models import Product, Order, OrderDetail


# def create_token(username, password):
#     """ Genero el token y devuelvo si está ok. """
#
#     try:
#         user = User.objects.filter(username=username).first()
#     except User.DoesNotExist:
#         return Response('Usuario no existe.')
#
#     password_valid = check_password(password, user.password)
#
#     if not password_valid:
#         return Response('contraseña erronea.')
#
#     token, _ = Token.objects.get_or_create(user=user)
#
#     return Response('Token creado.')


def product_create(name, price, stock):
    """ Método que pasa los datos de un producto para crear en la BD y luego los obtiene para ser usado en los test. """

    product, _ = Product.objects.get_or_create(
        name=name,
        price=price,
        stock=stock,
    )

    return product


def order_create(datetime):
    """ Método que pasa los datos de una orden para crear en la BD y luego los obtiene para ser usado en los test. """
    order, _ = Order.objects.get_or_create(
        datetime=datetime
    )

    return order


# @pytest.fixture
# def orderdetail_create():
#     """ Método que pasa los datos de un detalle de orden para crear en la BD y luego los obtiene para ser usado en
#     los test. """
#
#     # Creo ordenes de prueba.
#     order_1 = order_create(datetime='2021-12-03 12:00:00')
#
#     order_2 = order_create(datetime='2021-12-05 17:30:00')
#
#     # Creo productos de prueba.
#     product_1 = product_create(
#         name='Zapatillas Adidas adulto',
#         price=15600.00,
#         stock=10
#     )
#
#     product_2 = product_create(
#         name='Guantes de arquero Reusch niño',
#         price=3200.00,
#         stock=22
#     )
#
#     product_3 = product_create(
#         name='Zpatillas Adidas adulto',
#         price=15600.00,
#         stock=10
#     )
#
#     # Creo el detalle de la orden a partir de los datos creados.
#     orderdetail_1, _ = OrderDetail.objects.get_or_create(
#         quantity=10,
#         order=order_1,
#         product=product_1,
#     )
#
#     orderdetail_2, _ = OrderDetail.objects.get_or_create(
#         quantity=10,
#         order=order_1,
#         product=product_2,
#     )
#
#     orderdetail_3, _ = OrderDetail.objects.get_or_create(
#         quantity=10,
#         order=order_2,
#         product=product_3,
#     )
