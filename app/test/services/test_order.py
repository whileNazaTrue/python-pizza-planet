import pytest
from pytest_mock import mocker
from app.test.utils.functions import get_random_string, get_random_price
import json


def test_create_order_service(create_beverages, create_sizes,create_ingredients, create_order):
    beverages = create_beverages
    sizes = create_sizes
    ingredients = create_ingredients

    order = create_order.json
    pytest.assume(order['_id'])
    pytest.assume(order['beverages'])
    pytest.assume(order['customer'])
    pytest.assume(order['ingredients'])
    pytest.assume(order['size'])
    pytest.assume(order['total_price'])
    pytest.assume(order['date'])
    pytest.assume(order['customer']['_id'])
    pytest.assume(order['customer']['client_name'])
    pytest.assume(order['customer']['client_dni'])
    pytest.assume(order['customer']['client_address'])
    pytest.assume(order['customer']['client_phone'])
    


def test_get_by_id_service(client,order_uri, create_beverages, create_sizes,create_ingredients, create_order):
    beverages = create_beverages
    sizes = create_sizes
    ingredients = create_ingredients
    

    orders = []
    for _ in range(10):
        order = create_order.json
        orders.append(order)


    for order in orders:
        response = client.get(f'{order_uri}id/{order["_id"]}')
        pytest.assume(response.status.startswith('200'))
        returned_order = response.json
        for param, value in order.items():
            pytest.assume(returned_order[param] == value)


def test_get_orders(client,order_uri, create_beverages, create_sizes,create_ingredients, create_order):
    beverages = create_beverages
    sizes = create_sizes
    ingredients = create_ingredients
    
    array = []
    for _ in range(10):
        order = create_order.json
        array.append(order)

    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in array:
        pytest.assume(order['_id'] in returned_orders)



