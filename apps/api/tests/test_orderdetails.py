import pytest

from .utils import get,post
from .fixtures import order_create, product_create


@pytest.mark.django_db
def test_orderdeteil_list_ok():
    endpoint = "/api/orderdetail/"
    response = get(endpoint)
    assert response.status_code == 200


@pytest.mark.django_db
def test_orderdetail_create():
    endpoint = "/api/orderdetail/"

    # Creo ordenes de prueba.
    order1 = order_create(datetime='2021-12-05 17:30:00')

    # Creo productos de prueba.
    product1 = product_create(
        name='Zapatillas Adidas adulto',
        price=15600.00,
        stock=10
    )

    data = {
        "data": {
            "type": "OrderDetail",
            "attributes": {
                "quantity": 2,
                "product": product1,
                "order": order1,
            }
        }
    }

    response = post(endpoint, data=data)
    assert response.status_code == 201