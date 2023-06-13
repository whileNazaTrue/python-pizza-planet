from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager, SizeManager, BeverageManager, CustomerManager)
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    customer_manager = CustomerManager
    __required_info = ('client_dni', 'client_name', 'client_address', 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        price = size_price + sum(ingredient.price for ingredient in ingredients) + sum(beverage.price for beverage in beverages)
        print(str(price) + "precio")
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        client_dni = current_order.get('client_dni')
        customer = cls.customer_manager.get_by_dni(client_dni)

        if not customer:
            # Create a new customer if it doesn't exist
            customer_data = {
                'client_dni': client_dni,
                'client_name': current_order.get('client_name'),
                'client_address': current_order.get('client_address'),
                'client_phone': current_order.get('client_phone')
            }
            customer = cls.customer_manager.create(customer_data)

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)

        if not size:
            return 'Invalid size for Order', None

        ingredient_ids = current_order.pop('ingredients', [])
        beverage_ids = current_order.pop('beverages', [])

        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            beverages = BeverageManager.get_by_id_list(beverage_ids)
            price = cls.calculate_order_price(size.get('price'), ingredients, beverages)
            order_with_price = {**current_order, 'total_price': price, 'customer_id': customer['_id']}

            return cls.manager.create(order_with_price, ingredients, beverages, customer), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
