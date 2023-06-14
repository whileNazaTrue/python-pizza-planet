from ...repositories.models import Customer, Order, Report
from typing import List

class ReportBuilder:
    def __init__(self):
        self.report_data = {}
        self.customer = []

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


    def with_customer(self, customer: List[Customer]) -> 'ReportBuilder':
        self.customer = customer
        return self
    
    
    def build(self) -> Report:
        new_report = Report(**self.report_data)
        for customer in self.customer:
            new_report.customer.append(customer)
        for order in self.orders:
            new_report.orders.append(order)
        return new_report