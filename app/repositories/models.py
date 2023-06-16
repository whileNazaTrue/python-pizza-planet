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

class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', secondary=order_x_ingredient, back_populates='ingredients')

class Beverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', secondary=order_x_beverage, back_populates='beverages')

class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', back_populates='size')

class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))
    size = db.relationship('Size', back_populates='orders')
    ingredients = db.relationship('Ingredient', secondary=order_x_ingredient, back_populates='orders')
    beverages = db.relationship('Beverage', secondary=order_x_beverage, back_populates='orders')
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
