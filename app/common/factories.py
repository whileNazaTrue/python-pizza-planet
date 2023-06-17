from datetime import datetime
from random import randint, sample
from faker import Faker
from app.plugins import db
from ..repositories.models import Order, Customer

fake = Faker()

class OrderGenerator:
    def __init__(self, sizes, ingredients, beverages, 
                 sizes_for_order, ingredients_for_order, beverages_for_order):
        self.orders = []
        self.sizes = sizes
        self.ingredients = ingredients
        self.beverages = beverages
        self.sizes_for_order = sizes_for_order
        self.ingredients_for_order = ingredients_for_order
        self.beverages_for_order = beverages_for_order

    def generate_order(self, client_dni=None):
        if client_dni is None:
            client_dni = str(fake.random_int(min=10000000, max=99999999))

        order = Order(
            size_for_order=sample(self.sizes_for_order, 1)[0],
            customer=Customer(
                client_name=fake.name(),
                client_dni=str(client_dni),
                client_address=fake.address(),
                client_phone=fake.phone_number()
            )
        )

        order.date = fake.date_time_between(
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31)
        )

        order.ingredients_for_order = sample(self.ingredients_for_order, randint(1, 5))
        order.beverages_for_order = sample(self.beverages_for_order, randint(1, 3))
        order.total_price = self.calculate_total_price(
            order.size_for_order,
            order.ingredients_for_order,
            order.beverages_for_order
        )
        return order

    def calculate_total_price(self, size_for_order, ingredients_for_order, beverages_for_order):
        size_price = size_for_order.price if size_for_order else 0
        ingredients_price = sum(ingredient.price for ingredient in ingredients_for_order)
        beverages_price = sum(beverage.price for beverage in beverages_for_order)
        total_price = size_price + ingredients_price + beverages_price
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

    def create_orders(self, client_dni=None, num_orders=None, 
                      num_ingredients=None, num_beverages=None):
        for _ in range(num_orders):
            order = self.order_generator.generate_order(client_dni, num_ingredients, num_beverages)
            self.order_generator.orders.append(order)
