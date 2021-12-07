import pytest

from .utils import get, post


@pytest.mark.django_db
def test_product_list_fail_user_no_authenticated():
    endpoint = "/api/product/"
    response = get(endpoint)
    assert response.status_code == 401


@pytest.mark.django_db
def test_product_list_fail_user_no_authenticated():
    endpoint = "/api/product/"

    data = {
        "data": {
            "type": "Product",
            "attributes": {
                "name": "Artículo de deporte",
                "price": 267.00,
                "stock": 15,
            }
        }
    }

    response = post(endpoint, data=data)
    assert response.status_code == 201