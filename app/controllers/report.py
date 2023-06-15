
from ..common.utils import check_required_keys, number_to_month
from ..repositories.managers import (ReportManager, IngredientManager,
                                      CustomerManager, OrderManager)
from .base import BaseController


class ReportController(BaseController):
    manager = ReportManager
    customer_manager = CustomerManager
    ingredient_manager = IngredientManager
    order_manager = OrderManager

    __required_info = ('year')

    @classmethod
    def create(cls, report_data: dict):
        check_required_keys(cls.__required_info, report_data)
        year = report_data['year']

        most_requested_ingredient_id = cls.find_most_requested_ingredient(year)

        month_most_sales, month_most_revenue = cls.find_month_with_most_revenue(year)

        customers_with_most_orders = cls.find_customers_with_most_orders(year, limit=3)


        report = {
            'most_requested_ingredient_id': most_requested_ingredient_id,
            'month_with_most_revenue': number_to_month(month_most_sales),
            'sales_in_month_with_most_revenue': month_most_revenue,
            'year': year,
            'top_one_customer_id': customers_with_most_orders[0],
            'top_two_customer_id': customers_with_most_orders[1],
            'top_three_customer_id': customers_with_most_orders[2]
        }
        
        new_report = cls.manager.create(report)

        return new_report, None

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
    def find_customers_with_most_orders(cls, year: int, limit: int = 3):
        customers = cls.customer_manager.get_all()
        sorted_customers = sorted(
            customers,
            key=lambda customer: cls.customer_manager.get_order_count(customer['client_dni'], year),
            reverse=True
        )
        top_customers = [customer['_id'] for customer in sorted_customers[:limit]]
        return top_customers



    
    @staticmethod
    def row_to_dict(row):
        return {col: getattr(row, col) for col in row.__table__.columns.keys()}
    
    
    @classmethod
    def get_years_with_reports(cls):
        years = cls.order_manager.get_years_with_orders()
        years_dict_list = [{'year': year} for year in years]
        return years_dict_list, None
        