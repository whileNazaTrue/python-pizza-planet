import pytest

from ..utils.functions import get_random_price, get_random_string


def ingredient_for_order_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def ingredient_for_order_uri():
    return '/ingredientfororder/'


@pytest.fixture
def ingredient_for_order():
    return ingredient_for_order_mock()


@pytest.fixture
def ingredients_for_order():
    return [ingredient_for_order_mock() for _ in range(5)]


@pytest.fixture
def create_ingredient_for_order(client, ingredient_for_order_uri) -> dict:
    response = client.post(ingredient_for_order_uri,
                           json=ingredient_for_order_mock())
    return response


@pytest.fixture
def create_ingredients_for_order(client, ingredient_for_order_uri) -> list:
    ingredients_for_order = []
    for _ in range(10):
        new_ingredient_for_order = client.post(
            ingredient_for_order_uri, json=ingredient_for_order_mock())
        ingredients_for_order.append(new_ingredient_for_order.json)
    return ingredients_for_order
