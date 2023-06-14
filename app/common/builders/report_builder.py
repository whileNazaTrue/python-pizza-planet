from ...repositories.models import Customer, Order, Report
from typing import List
from datetime import datetime

class ReportBuilder:
    def __init__(self):
        self.report_data = {}
        self.customers = []

    def with_most_requested_ingredient_id(self, most_requested_ingredient_id: int) -> 'ReportBuilder':
        self.report_data['most_requested_ingredient_id'] = most_requested_ingredient_id
        return self
    

    def with_year(self, year: int) -> 'ReportBuilder':
        self.report_data['year'] = year
        return self
    
    def with_month_with_most_revenue(self, month_with_most_revenue: str) -> 'ReportBuilder':
        self.report_data['month_with_most_revenue'] = month_with_most_revenue
        return self
    
    def with_sales_in_month_with_most_revenue(self, sales_in_month_with_most_revenue: int) -> 'ReportBuilder':
        self.report_data['sales_in_month_with_most_revenue'] = sales_in_month_with_most_revenue
        return self


    def with_customers(self, customers: List[Customer]) -> 'ReportBuilder':
        self.customers = customers
        return self
        

    def with_created_at(self, created_at: datetime) -> 'ReportBuilder':
        self.report_data['created_at'] = created_at
        return self
    
    
    def build(self) -> Report:
        new_report = Report(**self.report_data)
    
        for customer_data in self.customers:
            customer_info = {
                'client_name': customer_data['client_name'],
                'client_dni': customer_data['client_dni'],
                'client_address': customer_data['client_address'],
                'client_phone': customer_data['client_phone'],
            }
            customer = Customer(**customer_info)
            new_report.customers.append(customer)
    
        return new_report
    