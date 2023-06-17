import pytest
from app.controllers import SizeForOrderController


def test_create(app, size_for_order: dict):
    created_size_for_order, error = SizeForOrderController.create(
        size_for_order)
    pytest.assume(error is None)
    for param, value in size_for_order.items():
        pytest.assume(param in created_size_for_order)
        pytest.assume(value == created_size_for_order[param])
        pytest.assume(created_size_for_order['_id'])


def test_get_all(app, beverages_for_order: list):
    created_size_for_orders = []
    for size_for_order in beverages_for_order:
        created_size_for_order, _ = SizeForOrderController.create(
            size_for_order)
        created_size_for_orders.append(created_size_for_order)

    beverages_for_order_from_db, error = SizeForOrderController.get_all()
    searchable_beverages_for_order = {
        db_size_for_order['_id']: db_size_for_order 
        for db_size_for_order in beverages_for_order_from_db}
    pytest.assume(error is None)
    for created_size_for_order in created_size_for_orders:
        current_id = created_size_for_order['_id']
        assert current_id in searchable_beverages_for_order
        for param, value in created_size_for_order.items():
            pytest.assume(
                searchable_beverages_for_order[current_id][param] == value)
