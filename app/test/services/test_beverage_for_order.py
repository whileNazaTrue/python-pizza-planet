import pytest


def test_create_beverage_for_order_service(create_beverage_for_order):
    beverage = create_beverage_for_order.json
    pytest.assume(create_beverage_for_order.status.startswith('200'))
    pytest.assume(beverage['_id'])
    pytest.assume(beverage['name'])
    pytest.assume(beverage['price'])


def test_get_beverages_beverages_for_order_service(client, create_beverages_for_order,
                                                   beverage_for_order_uri):
    response = client.get(beverage_for_order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_beverages_beverages_for_order = {
        beverage_for_order['_id']: beverage_for_order for beverage_for_order in response.json}
    for beverage in create_beverages_for_order:
        pytest.assume(beverage['_id']
                      in returned_beverages_beverages_for_order)
