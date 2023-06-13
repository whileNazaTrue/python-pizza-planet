from datetime import datetime
from random import randint, sample
from faker import Faker
from app.plugins import db
from ..repositories.models import Ingredient, Beverage, Size
from .factories import OrderGenerator, OrderFactory

fake = Faker()

def seed_data():
    # Seed Ingredients
    ingredients = []
    for i in range(1, 11):
        ingredient = Ingredient(name=fake.word(), price=randint(1, 10))
        ingredients.append(ingredient)
        db.session.add(ingredient)

    # Seed Beverages
    beverages = []
    for i in range(1, 11):
        beverage = Beverage(name=fake.word(), price=randint(5, 15))
        beverages.append(beverage)
        db.session.add(beverage)

    # Seed Sizes
    sizes = []
    for i in range(1, 6):
        size = Size(name=fake.word(), price=randint(5, 15))
        sizes.append(size)
        db.session.add(size)

    regular_order_generator = OrderGenerator(sizes, ingredients, beverages)
    specific_order_generator = OrderGenerator(sizes, ingredients, beverages)

    regular_order_factory = OrderFactory(regular_order_generator)
    specific_order_factory = OrderFactory(specific_order_generator)

    regular_order_factory.generate_orders(60)

    specific_order_factory.create_orders('40123456', 25, randint(1, 5), randint(1, 3))
    specific_order_factory.create_orders('20987654', 20, randint(1, 5), randint(1, 3))
    specific_order_factory.create_orders('10555555', 15, randint(1, 5), randint(1, 3))

    regular_order_generator.commit_orders()
    specific_order_generator.commit_orders()
    db.session.commit()
    print('Seeding completed!')
