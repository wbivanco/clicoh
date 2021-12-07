import pytest

from .utils import get,post


@pytest.mark.django_db
def test_order_list_ok():
    endpoint = "/api/order/"
    response = get(endpoint)
    assert response.status_code == 200



@pytest.mark.django_db
def test_order_create():
    endpoint = "/api/order/"

    data = {
        "data": {
            "type": "Order",
            "attributes": {
                "datetime": "2021-12-06 12:00:00"
            }
        }
    }

    response = post(endpoint, data=data)
    assert response.status_code == 201