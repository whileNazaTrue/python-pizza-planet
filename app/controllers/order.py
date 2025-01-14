from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (IngredientManager, OrderManager, SizeManager,
                                     BeverageManager, CustomerManager, IngredientForOrderManager,
                                     BeverageForOrderManager, SizeForOrderManager)
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    customer_manager = CustomerManager
    ingredient_for_order_manager = IngredientForOrderManager
    beverage_for_order_manager = BeverageForOrderManager
    size_for_order_manager = SizeForOrderManager
    __required_info = ('ingredients', 'size_id', 'beverages',
                       'customer', 'size_for_order_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        price = (size_price
                 + sum(ingredient.price for ingredient in ingredients)
                 + sum(beverage.price for beverage in beverages)
                 )
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        customer = current_order.get('customer')
        client_dni = customer["client_dni"]
        exists = cls.customer_manager.get_by_dni(client_dni)

        if not exists:
            customer_data = {
                'client_dni': customer["client_dni"],
                'client_name': customer["client_name"],
                'client_address': customer["client_address"],
                'client_phone': customer["client_phone"],
            }
            customer = cls.customer_manager.create(customer_data)
            customer_id = customer.get('_id')
        else:
            customer_id = exists._id

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)
        if not size:
            return 'Invalid size for Order', None

        size_for_order_id = SizeForOrderManager.exists_size_for_order(
            size["name"], size["price"])
        final_size = None
        if not size_for_order_id:
            mapped_size = {"name": size["name"], "price": size["price"]}
            final_size = cls.size_for_order_manager.create(mapped_size)
        else:
            final_size = cls.size_for_order_manager.get_by_id(
                size_for_order_id)

        ingredient_ids = current_order.pop('ingredients', [])
        ingredient_for_order_ids = cls.create_entities_for_order(
            ingredient_ids, IngredientManager, IngredientForOrderManager
        )

        beverage_ids = current_order.pop('beverages', [])
        beverage_for_order_ids = cls.create_entities_for_order(
            beverage_ids, BeverageManager, BeverageForOrderManager
        )

        final_size_price = final_size["price"]

        try:
            current_order["size_for_order_id"] = final_size["_id"]
            ingredient_for_orders = IngredientForOrderManager.get_by_id_list(
                ingredient_for_order_ids)
            beverage_for_orders = BeverageForOrderManager.get_by_id_list(
                beverage_for_order_ids)
            price = cls.calculate_order_price(
                final_size_price, ingredient_for_orders, beverage_for_orders)
            order_with_price = {**current_order,
                                'total_price': price, 'customer_id': customer_id}
            return cls.manager.create(order_with_price, ingredient_for_orders, 
                                      beverage_for_orders), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def create_entities_for_order(cls, entity_ids, entity_manager, for_order_manager):
        entity_for_order_ids = []
        for entity_id in entity_ids:
            entity = entity_manager.get_by_id(entity_id)
            entity_for_order_id = for_order_manager.exists_entity_for_order(
                entity["name"], entity["price"]
            )
            final_entity = None
            if not entity_for_order_id:
                mapped_entity = {
                    "name": entity["name"], "price": entity["price"]}
                final_entity = for_order_manager.create(mapped_entity)
            else:
                final_entity = for_order_manager.get_by_id(entity_for_order_id)
            entity_for_order_ids.append(final_entity["_id"])
        return entity_for_order_ids
