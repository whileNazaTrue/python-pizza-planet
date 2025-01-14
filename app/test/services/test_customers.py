import pytest



def test_create_customer_service(create_customer):
    customer = create_customer.json
    pytest.assume(create_customer.status.startswith('200'))
    pytest.assume(customer['_id'])
    pytest.assume(customer['client_name'])
    pytest.assume(customer['client_address'])
    pytest.assume(customer['client_phone'])
    pytest.assume(customer['client_dni'])



def test_get_customer_by_id_service(client, create_customer, customer_uri):
    current_customer = create_customer.json
    response = client.get(f'{customer_uri}id/{current_customer["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_customer = response.json
    for param, value in current_customer.items():
        pytest.assume(returned_customer[param] == value)


def test_get_customers_service(client, create_customers, customer_uri):
    response = client.get(customer_uri)
    pytest.assume(response.status.startswith('200'))
    returned_customers = {customer['_id']: customer for customer in response.json}
    for customer in create_customers:
        pytest.assume(customer['_id'] in returned_customers)
