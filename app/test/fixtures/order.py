
import pytest

from ..utils.functions import get_random_price, get_random_string
import datetime



def order_mock() -> dict:
    return{
        "beverages": [
            {
                "name": get_random_string(),
                "price": get_random_price(10, 20)
            }
        ],
        "customer": {
            "client_address": get_random_string(),
            "client_dni": get_random_string(),
            "client_name": get_random_string(),
            "client_phone": get_random_string(),
        },
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ingredients": [
            {
                "name": get_random_string(),
                "price": get_random_price(10, 20)
            },
            {
                "name": get_random_string(),
                "price": get_random_price(10, 20)
            }
        ],
        "size": {
            "name": get_random_string(),
            "price": get_random_price(10,20)
        },
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
def create_order(client, order_uri, order_data) -> dict:
    response = client.post(order_uri, json=order_data)
    return response.json()


@pytest.fixture
def create_orders(client, order_uri, order_data) -> list:
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json=order_data)
        orders.append(new_order.json)
    return orders