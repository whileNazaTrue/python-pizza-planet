import pytest
from app.controllers import (IngredientController, OrderController, SizeController,
                             BeverageController, CustomerController, ReportController)
from app.controllers.base import BaseController
import datetime

def __report_extra_data(ingredients: list, customers: list, 
                        beverages: list, orders: list, sizes: list):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    customers = [customer.get('_id') for customer in customers]
    beverages = [beverage.get('_id') for beverage in beverages]
    sizes = [size.get('_id') for size in sizes]
    orders = [order.get('_id') for order in orders]
    return {
        'ingredients': ingredients,
        'customers': customers,
        'beverages': beverages,
        'sizes': sizes,
        'orders': orders
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for item in items:
        created_item, error = controller.create(item)
        pytest.assume(error is None)
        created_items.append(created_item)
    return created_items


def __create_data_for_report(ingredients: list, customers: list, 
                             beverages: list, sizes: list, orders: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_customers = __create_items(customers, CustomerController)
    created_beverages = __create_items(beverages, BeverageController)
    created_sizes = __create_items(sizes, SizeController)
    created_orders = __create_items(orders, OrderController)
    return (
        created_ingredients,
        created_customers,
        created_beverages,
        created_sizes,
        created_orders
    )


def __create_many_attributes(ingredients: list, customers: list,
                              beverages: list, sizes: list, orders: list):
    (created_ingredients, created_customers, 
     created_beverages, created_sizes, created_orders) = __create_data_for_report(
        ingredients, customers, beverages, sizes, orders)
    return (
        created_ingredients,
        created_customers,
        created_beverages,
        created_sizes,
        created_orders


    )


def test_report(app, ingredients, customers, beverages, sizes, orders):
    with app.app_context():
        (created_ingredients,created_customers , 
         created_beverages, created_sizes, created_orders) = __create_many_attributes(
            ingredients, customers, beverages, sizes, orders)
        __report_extra_data(created_ingredients, created_customers,
                          created_beverages, created_sizes, created_orders)
        report = {
            'year': datetime.date.today().year,
        }
        created_report, error = ReportController.create(report)

        pytest.assume(error is None)
        pytest.assume(created_report["most_requested_ingredient"] in created_ingredients)
<<<<<<< HEAD
=======
        pytest.assume(created_report["top_one_customer"] is not None)
        pytest.assume(created_report["top_two_customer"] is not None)
        pytest.assume(created_report["top_three_customer"] is not None)
>>>>>>> d849ca8c4c20e72941ffca6543f8e3d545cb3193
        pytest.assume(created_report["year"] == report["year"])
        
        


