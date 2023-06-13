import pytest
from app.controllers import CustomerController

def test_create(app, customer: dict):
    created_customer, error = CustomerController.create(customer)
    pytest.assume(error is None)
    for param, value in customer.items():
        pytest.assume(param in created_customer)
        pytest.assume(value == created_customer[param])
        

        

def test_update(app, customer: dict):
    created_customer, _ = CustomerController.create(customer)
    updated_fields = {
        'client_name': 'updated',
        'client_address': 'test',
    }
    updated_customer, error = CustomerController.update({
        '_id': created_customer['_id'],
        **updated_fields
    })

    pytest.assume(error is None)
    customer_from_database, error = CustomerController.get_by_id(created_customer['_id'])
    pytest.assume(error is None)
    for param, value in updated_fields.items():
        pytest.assume(updated_customer[param] == value)
        pytest.assume(customer_from_database[param] == value)


def test_get_by_id(app, customer: dict):
    created_customer, _ = CustomerController.create(customer)
    customer_from_db, error = CustomerController.get_by_id(created_customer['_id'])
    pytest.assume(error is None)
    for param, value in created_customer.items():
        pytest.assume(customer_from_db[param] == value)


def test_get_all(app, customers: list):
    created_customers = []
    for customer in customers:
        created_customer, _ = CustomerController.create(customer)
        created_customers.append(created_customer)

    customers_from_db, error = CustomerController.get_all()
    searchable_customers = {db_customer['_id']: db_customer for db_customer in customers_from_db}
    pytest.assume(error is None)
    for created_customer in created_customers:
        current_id = created_customer['_id']
        assert current_id in searchable_customers
        for param, value in created_customer.items():
            pytest.assume(searchable_customers[current_id][param] == value)