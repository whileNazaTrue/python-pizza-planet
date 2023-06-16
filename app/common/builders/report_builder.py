from ...repositories.models import Report, Customer
from typing import List
from datetime import datetime

class ReportBuilder:
    def __init__(self):
        self.report_data = {}
        self.top_customers = []

    def with_most_requested_ingredient_id(self, most_requested_ingredient_id: int) -> 'ReportBuilder':
        self.report_data['most_requested_ingredient_id'] = most_requested_ingredient_id
        return self

    def with_year(self, year: int) -> 'ReportBuilder':
        self.report_data['year'] = year
        return self

    def with_month_with_most_revenue(self, month_with_most_revenue: str) -> 'ReportBuilder':
        self.report_data['month_with_most_revenue'] = month_with_most_revenue
        return self

    def with_sales_in_month_with_most_revenue(self, sales_most_revenue: int) -> 'ReportBuilder':
        self.report_data['sales_in_month_with_most_revenue'] = sales_most_revenue
        return self

    def with_top_customers(self, top_customers: List[Customer]) -> 'ReportBuilder':
        self.report_data['top_customers'] = top_customers
        return self

    def with_created_at(self, created_at: datetime) -> 'ReportBuilder':
        self.report_data['created_at'] = created_at
        return self

    def build(self) -> Report:
        print("loading")
        new_report = Report(**self.report_data)
        for customer in self.top_customers:
            print("customer",customer)
            new_report.customers.append(customer)
        return new_report
