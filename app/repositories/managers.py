from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column, func, extract, label

from .models import Ingredient, Order, Size, db, Beverage, Customer, Report
from .serializers import (IngredientSerializer, OrderSerializer,SizeSerializer,
                           BeverageSerializer, CustomerSerializer, ReportSerializer,ma)
from ..common.builders.order_builder import OrderBuilder
from ..common.builders.report_builder import ReportBuilder

class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
    

class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []

class CustomerManager(BaseManager):
    model = Customer
    serializer = CustomerSerializer


    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []

    @classmethod
    def get_by_dni(cls, dni: str):
        return cls.session.query(cls.model).filter(cls.model.client_dni == dni).first()
    
    @classmethod
    def only_get_customer_info(cls, dni: str):
        return cls.session.query(cls.model.client_name, 
                                 cls.model.client_dni, 
                                 cls.model.client_address,
                                 cls.model.client_phone 
                                 ).filter(cls.model.client_dni == dni).first()
    

    

    @classmethod
    def get_order_count(cls, dni: str, year: int):
        return (
            cls.session.query(func.count(Order._id))
            .join(Order.customer)
            .filter(Customer.client_dni == dni, extract('year', Order.date) == year)
            .scalar()
        )
    



class ReportManager(BaseManager):
    model = Report
    serializer = ReportSerializer

    @classmethod
    def get_by_year(cls, year: int):
        return cls.session.query(cls.model).filter(cls.model.date.like(f'{year}%')).all()
    
    @classmethod
    def create(cls, report_data: dict):
        report_builder = ReportBuilder()
        report_builder.with_most_requested_ingredient_id(report_data['most_requested_ingredient_id'])
        report_builder.with_month_with_most_revenue(report_data['month_with_most_revenue'])
        report_builder.with_sales_in_month_with_most_revenue(report_data['sales_in_month_with_most_revenue'])
        report_builder.with_year(report_data['year'])
        report_builder.with_top_one_customer_id(report_data['top_one_customer_id'])
        report_builder.with_top_two_customer_id(report_data['top_two_customer_id'])
        report_builder.with_top_three_customer_id(report_data['top_three_customer_id'])
        new_report = report_builder.build()
        cls.session.add(new_report)
        cls.session.commit()
        return cls.serializer().dump(new_report)
    
    
    


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer
    

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        order_builder = OrderBuilder()
        order_builder.with_customer_id(order_data['customer_id'])
        order_builder.with_size(order_data['size_id'])
        order_builder.with_total_price(order_data['total_price'])
        order_builder.with_ingredients(ingredients)
        order_builder.with_beverages(beverages)
        new_order = order_builder.build()
        cls.session.add(new_order)
        cls.session.commit()
        return cls.serializer().dump(new_order)


    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')
    
    @classmethod
    def get_month_with_most_revenue(cls, year: int):
        return (
            cls.session.query(func.extract('month', Order.date), func.sum(Order.total_price))
            .filter(extract('year', Order.date) == year)
            .group_by(func.extract('month', Order.date))
            .order_by(func.sum(Order.total_price).desc())
            .first()
        )
    
    @classmethod
    def get_most_requested_ingredient(cls, year: int):
        return (
            cls.session.query(
                Ingredient._id,
                label('count', func.count(Order.ingredients))
            )
            .join(Order.ingredients)
            .join(Order.order_x_ingredient)
            .filter(extract('year', Order.date) == year)
            .group_by(Ingredient._id)
            .order_by(func.count(Order.ingredients).desc())
            .first()
        )
    
    @classmethod
    def get_years_with_orders(cls):
        years = cls.session.query(
            func.extract('year', Order.date)
            ).group_by(func.extract('year', Order.date)).all()

        return [year[0] for year in years]

    

class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
