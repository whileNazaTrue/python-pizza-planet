import pytest
from app.controllers import BeverageForOrderController


def test_create(app, beverage_for_order: dict):
    created_beverage_for_order, error = BeverageForOrderController.create(
        beverage_for_order)
    pytest.assume(error is None)
    for param, value in beverage_for_order.items():
        pytest.assume(param in created_beverage_for_order)
        pytest.assume(value == created_beverage_for_order[param])
        pytest.assume(created_beverage_for_order['_id'])


def test_get_all(app, beverages_for_order: list):
    created_beverage_for_orders = []
    for beverage_for_order in beverages_for_order:
        created_beverage_for_order, _ = BeverageForOrderController.create(
            beverage_for_order)
        created_beverage_for_orders.append(created_beverage_for_order)

    beverages_for_order_from_db, error = BeverageForOrderController.get_all()
    searchable_beverages_for_order = {
        db_beverage_for_order['_id']: 
        db_beverage_for_order for db_beverage_for_order in beverages_for_order_from_db}
    pytest.assume(error is None)
    for created_beverage_for_order in created_beverage_for_orders:
        current_id = created_beverage_for_order['_id']
        assert current_id in searchable_beverages_for_order
        for param, value in created_beverage_for_order.items():
            pytest.assume(
                searchable_beverages_for_order[current_id][param] == value)
