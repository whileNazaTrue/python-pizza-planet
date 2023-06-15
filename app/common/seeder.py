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

    order_generator = OrderGenerator(sizes, ingredients, beverages)

    order_factory = OrderFactory(order_generator)

    order_factory.generate_orders(60)

    order_generator.commit_orders()
    db.session.commit()
    print('Seeding completed!')
