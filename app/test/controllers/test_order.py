import pytest
from app.controllers import (IngredientController, OrderController, SizeController, 
                             BeverageController, CustomerController)
from app.controllers.base import BaseController


def __order(ingredients: list, size: dict, beverages: list, customer: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    
    size_id = size.get('_id')
    

    return {
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverages,
        'customer': {
            'client_dni': customer['client_dni'],
            'client_name': customer['client_name'],
            'client_address': customer['client_address'],
            'client_phone': customer['client_phone']
        }
    }

def __create_items(items: list, controller: BaseController):
    created_items = []
    for ingredient in items:
        created_item, error = controller.create(ingredient)
        pytest.assume(error is None)
        created_items.append(created_item)
    return created_items

def __create_many_attributes(ingredients: list, sizes: list, beverages: list, customers: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_sizes = __create_items(sizes, SizeController)
    created_beverages = __create_items(beverages, BeverageController)
    created_customers = __create_items(customers, CustomerController)
    return (
        created_sizes[0] if len(created_sizes) > 0 else None,
        created_ingredients,
        created_beverages,
        created_customers[0] if len(created_customers) > 0 else None,
    )


def test_create(app, ingredients, size, beverages, customer):
    with app.app_context():
        (created_sizes, created_ingredients, 
         created_beverages, created_customers) = __create_many_attributes(
            [size], ingredients, beverages, [customer]
        )
        order = __order(created_ingredients, created_sizes, created_beverages, created_customers)
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)
        size_id = created_sizes["_id"]
        ingredient_ids = order.pop('ingredients', [])
        beverage_ids = order.pop('beverages', [])
        customer_id = created_order['customer']['_id']
        ingredients_in_order = created_order.get('ingredients', [])
        beverages_in_order = created_order.get('beverages', [])
        ingredient_set = set(ingredient_ids)
        beverage_set = set(beverage_ids)

        ingredient_present = ingredient_set.intersection(
            item["_id"] 
                for item in ingredients_in_order
                )
        beverage_present = beverage_set.intersection(
            item["_id"] 
                for item in beverages_in_order
                )

        pytest.assume(ingredient_present)
        pytest.assume(beverage_present)
        pytest.assume(customer_id == created_order['customer']['_id'])
        pytest.assume(created_order is not None)
        pytest.assume(created_order['_id'] is not None)
        pytest.assume(size_id == created_order['size']['_id'])

def test_calculate_order_price(app, ingredients, size, beverages, customer):
    with app.app_context():
        (created_sizes, created_ingredients, 
         created_beverages, created_customers) = __create_many_attributes(
            [size], ingredients, beverages, [customer]
        )
        order = __order(created_ingredients, created_sizes, created_beverages, created_customers)
        created_order = OrderController.create(order)
        expected_total_price = round(
            created_sizes['price'] + 
            sum(item['price'] for item in created_ingredients) + 
            sum(item['price'] for item in created_beverages), 2
            )
        pytest.assume(created_order[0]['total_price'] == expected_total_price)

def test_get_by_id(app, ingredients, size, beverages, customer):
    with app.app_context():
        (created_size, created_ingredients, 
         created_beverages, created_customer) = __create_many_attributes(
            ingredients, [size], beverages, [customer]
        )
        order = __order(created_ingredients, created_size, created_beverages, created_customer)
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)

        order_id = created_order['_id']

        order_by_id, error = OrderController.get_by_id(order_id)
        pytest.assume( order_by_id['_id'] == order_id)


def test_get_all(app, ingredients, size, beverages, customer):
    with app.app_context():
        (created_size, created_ingredients,
          created_beverages, created_customer) = __create_many_attributes(
            ingredients, [size], beverages, [customer]
        )
        create_orders = []
        for _ in range(5):
            order = __order(created_ingredients, created_size, created_beverages, created_customer)
            created_order, error = OrderController.create(order)
            create_orders.append(created_order)
            pytest.assume(error is None)

        for order in create_orders:
            order_id = order['_id']
            order_by_id, error = OrderController.get_by_id(order_id)
            pytest.assume(error is None)

            pytest.assume( order_by_id['_id'] == order_id)




