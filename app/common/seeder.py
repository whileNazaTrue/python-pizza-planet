from random import randint
from faker import Faker
from app.plugins import db
from ..repositories.models import (Ingredient, Beverage, Size, 
SizeForOrder, IngredientForOrder, BeverageForOrder)
from .factories import OrderGenerator, OrderFactory

fake = Faker()

def seed_data():
    # Seed Ingredients and Ingredients for Order
    ingredients = []
    ingredients_for_order = []
    for i in range(1, 11):
        ingredient_name = fake.word()
        ingredient_price = randint(1, 10)
        ingredient = Ingredient(name=ingredient_name, price=ingredient_price)
        ingredient_for_order = IngredientForOrder(name=ingredient_name, price=ingredient_price)
        ingredients.append(ingredient)
        ingredients_for_order.append(ingredient_for_order)
        db.session.add(ingredient)
        db.session.add(ingredient_for_order)

    # Seed Beverages and Beverages for Order
    beverages = []
    beverages_for_order = []
    for i in range(1, 11):
        beverage_name = fake.word()
        beverage_price = randint(5, 15)
        beverage = Beverage(name=beverage_name, price=beverage_price)
        beverage_for_order = BeverageForOrder(name=beverage_name, price=beverage_price)
        beverages.append(beverage)
        beverages_for_order.append(beverage_for_order)
        db.session.add(beverage)
        db.session.add(beverage_for_order)

    # Seed Sizes and Sizes for Order
    sizes = []
    sizes_for_order = []
    for i in range(1, 6):
        size_name = fake.word()
        size_price = randint(5, 15)
        size = Size(name=size_name, price=size_price)
        size_for_order = SizeForOrder(name=size_name, price=size_price)
        sizes.append(size)
        sizes_for_order.append(size_for_order)
        db.session.add(size)
        db.session.add(size_for_order)

    order_generator = OrderGenerator(sizes, ingredients, beverages, 
                                     sizes_for_order, ingredients_for_order, beverages_for_order)

    order_factory = OrderFactory(order_generator)

    order_factory.generate_orders(60)

    order_generator.commit_orders()
    db.session.commit()
    print('Seeding completed!')
