import pytest

from ..utils.functions import get_random_string


def customer_mock() -> dict:
    return {
        'client_name': get_random_string(),
        'client_address':  get_random_string(),
        'client_phone':  get_random_string(),
        'client_dni':  get_random_string(),
    }

@pytest.fixture
def customer_uri():
    return '/customer/'


@pytest.fixture
def customer():
    return customer_mock()


@pytest.fixture
def customers():
    return [customer_mock() for _ in range(5)]

@pytest.fixture
def create_customer(client, customer_uri) -> dict:
    response = client.post(customer_uri, json=customer_mock())
    return response


@pytest.fixture
def create_customers(client, customer_uri) -> list:
    customers = []
    for _ in range(10):
        new_customer = client.post(customer_uri, json=customer_mock())
        customers.append(new_customer.json)
    return customers
