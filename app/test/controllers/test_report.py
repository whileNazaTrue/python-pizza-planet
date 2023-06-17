import pytest
from app.controllers import (IngredientController, OrderController, SizeController,
                             BeverageController, CustomerController)
from app.controllers.base import BaseController

def __report_extra_data(ingredients: list, customers: list, 
                        beverages: list,ingredients_for_order: list, beverages_for_order: list,
                        size_for_order: dict, sizes: list, orders: list,
                        ):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    customers = [customer.get('_id') for customer in customers]
    beverages = [beverage.get('_id') for beverage in beverages]
    orders = [order.get('_id') for order in orders]
    ingredients_for_order = [ingredient.get( '_id') for ingredient in ingredients_for_order]
    beverages_for_order = [beverage.get('_id') for beverage in beverages_for_order]
    size_for_order_id = size_for_order.get('_id') if size_for_order else 1
    
    return {
        'ingredients': ingredients,
        'customers': customers,
        'beverages': beverages,
        'ingredients_for_order': ingredients_for_order,
        'beverages_for_order': beverages_for_order,
        'size_for_order_id': size_for_order_id,
        'sizes': sizes,
        'orders': orders,
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for item in items:
        created_item, error = controller.create(item)
        pytest.assume(error is None)
        created_items.append(created_item)
    return created_items


def __create_data_for_report(ingredients: list, customers: list, 
                        beverages: list,ingredients_for_order: list, beverages_for_order: list,
                        size_for_order: dict, sizes: list, orders: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_customers = __create_items(customers, CustomerController)
    created_beverages = __create_items(beverages, BeverageController)
    created_sizes = __create_items(sizes, SizeController)
    created_ingredients_for_order = __create_items(ingredients_for_order, IngredientController)
    created_beverages_for_order = __create_items(beverages_for_order, BeverageController)
    created_size_for_order = __create_items(size_for_order, SizeController)
    created_orders = __create_items(orders, OrderController)
    return (
        created_ingredients,
        created_customers,
        created_beverages,
        created_sizes[0] if len(created_sizes) > 0 else None,
        created_ingredients_for_order,
        created_beverages_for_order,
        created_size_for_order[0] if len(created_size_for_order) > 0 else None,
        created_orders
    )

