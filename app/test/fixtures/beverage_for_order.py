import pytest

from ..utils.functions import get_random_price, get_random_string


def beverage_for_order_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }

@pytest.fixture
def beverage_for_order_uri():
    return '/beveragefororder/'


@pytest.fixture
def beverage_for_order():
    return beverage_for_order_mock()


@pytest.fixture
def beverages_for_order():
    return [beverage_for_order_mock() for _ in range(5)]


@pytest.fixture
def create_beverage_for_order(client, beverage_for_order_uri) -> dict:
    response = client.post(beverage_for_order_uri, json=beverage_for_order_mock())
    return response

@pytest.fixture
def create_beverages_for_order(client, beverage_for_order_uri) -> list:
    beverages_for_order = []
    for _ in range(10):
        new_beverage_for_order = client.post(beverage_for_order_uri, json=beverage_for_order_mock())
        beverages_for_order.append(new_beverage_for_order.json)
    return beverages_for_order
