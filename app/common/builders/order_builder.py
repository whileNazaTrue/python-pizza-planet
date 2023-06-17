from ...repositories.models import (Ingredient, Order, Beverage,
                                    IngredientForOrder, BeverageForOrder)
from typing import List


class OrderBuilder:
    def __init__(self):
        self.order_data = {}
        self.ingredients = []
        self.ingredients_for_order = []
        self.beverages = []
        self.beverages_for_order = []

    def with_customer_id(self, customer_id: int) -> 'OrderBuilder':
        self.order_data['customer_id'] = customer_id
        return self

    def with_size(self, size_id: int) -> 'OrderBuilder':
        self.order_data['size_id'] = size_id
        return self

    def with_size_for_order(self, size_for_order_id: int) -> 'OrderBuilder':
        self.order_data['size_for_order_id'] = size_for_order_id
        return self

    def with_total_price(self, total_price: float) -> 'OrderBuilder':
        self.order_data['total_price'] = total_price
        return self

    def with_ingredients(self, ingredients: List[Ingredient]) -> 'OrderBuilder':
        self.ingredients = ingredients
        return self

    def with_ingredients_for_order(self,
                                ingredients_for_order: List[IngredientForOrder]) -> 'OrderBuilder':
        self.ingredients_for_order = ingredients_for_order
        return self

    def with_beverages(self, beverages: List[Beverage]) -> 'OrderBuilder':
        self.beverages = beverages
        return self

    def with_beverages_for_order(self,
                                beverages_for_order: List[BeverageForOrder]) -> 'OrderBuilder':
        self.beverages_for_order = beverages_for_order
        return self

    def build(self) -> Order:
        new_order = Order(**self.order_data)
        for ingredient in self.ingredients:
            new_order.ingredients.append(ingredient)
        for beverage in self.beverages:
            new_order.beverages.append(beverage)
        for ingredient_for_order in self.ingredients_for_order:
            new_order.ingredients_for_order.append(ingredient_for_order)
        for beverage_for_order in self.beverages_for_order:
            new_order.beverages_for_order.append(beverage_for_order)
        return new_order
