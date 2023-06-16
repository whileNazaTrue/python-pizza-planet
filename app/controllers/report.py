
from ..common.utils import check_required_keys, number_to_month
from ..repositories.managers import (ReportManager, IngredientManager,
                                      CustomerManager, OrderManager)
from .base import BaseController
from sqlalchemy.exc import SQLAlchemyError


class ReportController(BaseController):
    manager = ReportManager
    customer_manager = CustomerManager
    ingredient_manager = IngredientManager
    order_manager = OrderManager

    __required_info = ('year', 'top_customers')

    @classmethod
    def create(cls, report_data: dict):
        current_report = report_data.copy()
        check_required_keys(cls.__required_info, report_data)
        year = report_data['year']

        most_requested_ingredient_id = cls.find_most_requested_ingredient(year)

        month_most_sales, month_most_revenue = cls.find_month_with_most_revenue(year)

        customers_with_most_orders = cls.find_customers_with_most_orders(year, limit=3)
        customers_ids = current_report.pop('top_customers', [])
        for customer in customers_with_most_orders:
            customers_ids.append(customer[0])
        print(customers_ids)


            
        report = {
            'most_requested_ingredient_id': most_requested_ingredient_id,
            'month_with_most_revenue': number_to_month(month_most_sales),
            'sales_in_month_with_most_revenue': month_most_revenue,
            'year': year,
        }
        
        try:
            top_customers = cls.customer_manager.get_by_id_list(customers_ids)
            new_report = cls.manager.create(report, top_customers)
            return new_report, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def find_most_requested_ingredient(cls, year: int):
        data = cls.order_manager.get_most_requested_ingredient(year)
        return data[0]

    
    @classmethod
    def find_month_with_most_revenue(cls, year: int):
        data = cls.order_manager.get_month_with_most_revenue(year)
        month = data[0]
        revenue = data[1]
        return month, revenue

    
    @classmethod
    def find_customers_with_most_orders(cls, year: int, limit: int):
        data = cls.customer_manager.get_customers_with_most_orders(year, limit)
        return data


    
    @staticmethod
    def row_to_dict(row):
        return {col: getattr(row, col) for col in row.__table__.columns.keys()}
    
    
    @classmethod
    def get_years_with_reports(cls):
        years = cls.order_manager.get_years_with_orders()
        years_dict_list = [{'year': year} for year in years]
        return years_dict_list, None
        