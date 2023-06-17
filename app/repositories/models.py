from datetime import datetime
from app.plugins import db

order_x_ingredient = db.Table(
    'order_x_ingredient',
    db.Column('order_id', db.Integer, db.ForeignKey('order._id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient._id'), primary_key=True)
)

order_x_beverage = db.Table(
    'order_x_beverage',
    db.Column('order_id', db.Integer, db.ForeignKey('order._id'), primary_key=True),
    db.Column('beverage_id', db.Integer, db.ForeignKey('beverage._id'), primary_key=True)
)

report_x_customer = db.Table(
    'report_x_customer',
    db.Column('report_id', db.Integer, db.ForeignKey('report._id'), primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customer._id'), primary_key=True)
)

order_x_ingredients_for_order = db.Table(
    'order_x_ingredients_for_order',
    db.Column('order_id', db.Integer, db.ForeignKey('order._id'), primary_key=True),
    db.Column('ingredient_for_order_id', db.Integer, db.ForeignKey('ingredient_for_order._id'), primary_key=True)
)

order_x_beverages_for_order = db.Table(
    'order_x_beverages_for_order',
    db.Column('order_id', db.Integer, db.ForeignKey('order._id'), primary_key=True),
    db.Column('beverage_for_order_id', db.Integer, db.ForeignKey('beverage_for_order._id'), primary_key=True)
)


class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', secondary=order_x_ingredient, back_populates='ingredients')

class IngredientForOrder(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders_for_order = db.relationship('Order', secondary=order_x_ingredients_for_order, back_populates='ingredients_for_order')

class Beverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', secondary=order_x_beverage, back_populates='beverages')

class BeverageForOrder(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders_for_order = db.relationship('Order', secondary=order_x_beverages_for_order, back_populates='beverages_for_order')



class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', back_populates='size')

class SizeForOrder(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders_for_order = db.relationship('Order', back_populates='size_for_order')


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))
    size = db.relationship('Size', back_populates='orders')
    ingredients = db.relationship('Ingredient', secondary=order_x_ingredient, back_populates='orders')
    ingredients_for_order = db.relationship('IngredientForOrder', secondary=order_x_ingredients_for_order, back_populates='orders_for_order')
    beverages = db.relationship('Beverage', secondary=order_x_beverage, back_populates='orders')
    beverages_for_order = db.relationship('BeverageForOrder', secondary=order_x_beverages_for_order, back_populates='orders_for_order')
    size_for_order_id = db.Column(db.Integer, db.ForeignKey('size_for_order._id'))
    size_for_order = db.relationship('SizeForOrder', back_populates='orders_for_order')
    total_price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer._id'))
    customer = db.relationship('Customer', back_populates='orders')

class Customer(db.Model):
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    orders = db.relationship('Order', back_populates='customer')
    reports = db.relationship('Report', secondary=report_x_customer, back_populates='top_customers')


class Report(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    most_requested_ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'))
    most_requested_ingredient = db.relationship('Ingredient', backref=db.backref('report'))
    year = db.Column(db.Integer, default=datetime.now().year)
    month_with_most_revenue = db.Column(db.String(15))
    sales_in_month_with_most_revenue = db.Column(db.Float)
    top_customers = db.relationship('Customer', secondary=report_x_customer, back_populates='reports')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
