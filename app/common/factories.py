from datetime import datetime
from random import randint, sample
from faker import Faker
from app.plugins import db
from ..repositories.models import Order

fake = Faker()

from datetime import datetime
from random import randint, sample
from faker import Faker
from app.plugins import db
from ..repositories.models import Order

fake = Faker()

class OrderGenerator:
    def __init__(self, sizes, ingredients, beverages):
        self.orders = []
        self.sizes = sizes
        self.ingredients = ingredients
        self.beverages = beverages

    def generate_order(self, client_dni=None, num_ingredients=None, num_beverages=None):
        if client_dni is None:
            client_dni = str(fake.random_int(min=10000000, max=99999999))

        if num_ingredients is None:
            num_ingredients = randint(1, 5)

        if num_beverages is None:
            num_beverages = randint(1, 3)

        
        order = Order(
            client_name=fake.name(),
            client_dni=str(client_dni),
            client_address=fake.address(),
            client_phone=fake.phone_number(),
            date=fake.date_time_between(start_date='-1y', end_date='now'),
            size=sample(self.sizes, 1)[0],
            
        )
        order.ingredients = sample(self.ingredients, num_ingredients)
        order.beverages = sample(self.beverages, num_beverages)
        order.total_price = self.calculate_total_price(order.size, order.ingredients, order.beverages)
        return order


    def calculate_total_price(self, size, ingredients, beverages):
        ingredients_price = sum(ingredient.price for ingredient in ingredients)
        beverages_price = sum(beverage.price for beverage in beverages)
        total_price = size.price + ingredients_price + beverages_price
        return total_price
    

    def commit_orders(self):
        for order in self.orders:
            db.session.add(order)
        db.session.commit()



class OrderFactory:
    def __init__(self, order_generator):
        self.order_generator = order_generator

    def generate_orders(self, num_orders):
        for _ in range(num_orders):
            order = self.order_generator.generate_order()
            self.order_generator.orders.append(order)

    def create_orders(self, client_dni=None, num_orders=None, num_ingredients=None, num_beverages=None):
        for _ in range(num_orders):
            order = self.order_generator.generate_order(client_dni, num_ingredients, num_beverages)
            self.order_generator.orders.append(order)

