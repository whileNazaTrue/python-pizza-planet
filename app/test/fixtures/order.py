
import pytest

from ..utils.functions import get_random_price, get_random_string
import datetime



def order_mock() -> dict:
    return{
        "beverages": ['1'],
        "customer": {
            "client_name": 'te',
            "client_dni": '1',
            "client_address": '2',
            "client_phone": '5'
        },
        "ingredients": ['1'],
        "size_id": '1'
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def order():
    return order_mock()

@pytest.fixture
def orders():
    return [order_mock() for _ in range(5)]


@pytest.fixture
def create_order(client, order_uri) -> dict:
    response = client.post(order_uri, json=order_mock())
    return response

@pytest.fixture
def create_orders(client, order_uri) -> list:
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json=order_mock())
        orders.append(new_order.json)
    return orders


@pytest.fixture
def create_order(client, order_uri) -> dict:
    response = client.post(order_uri, json=order_mock())
    return response


@pytest.fixture
def create_orders(client, order_uri) -> list:
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json=order_mock())
        orders.append(new_order.json)
    return orders