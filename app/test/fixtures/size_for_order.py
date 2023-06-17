import pytest

from ..utils.functions import get_random_price, get_random_string


def size_for_order_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }

@pytest.fixture
def size_for_order_uri():
    return '/sizefororder/'


@pytest.fixture
def size_for_order():
    return size_for_order_mock()


@pytest.fixture
def sizes_for_order():
    return [size_for_order_mock() for _ in range(5)]


@pytest.fixture
def create_size_for_order(client, size_for_order_uri) -> dict:
    response = client.post(size_for_order_uri, json=size_for_order_mock())
    return response

@pytest.fixture
def create_sizes_for_orders(client, size_for_order_uri) -> list:
    sizes_for_order = []
    for _ in range(10):
        new_size_for_order = client.post(size_for_order_uri, json=size_for_order_mock())
        sizes_for_order.append(new_size_for_order.json)
    return sizes_for_order
