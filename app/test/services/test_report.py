import pytest


def test_create_report_service(create_beverages, create_customers, create_sizes,
                                create_ingredients, create_orders, create_report):

    report = create_report.json
    pytest.assume(report['_id'])
    pytest.assume(report['month_with_most_revenue'])
    pytest.assume(report['sales_in_month_with_most_revenue'])
    pytest.assume(report['top_customers'])
 


def test_get_by_id_report_service(client, report_uri, create_beverages, create_customers,
                                   create_sizes, create_ingredients, create_orders, create_report):

    reports = []
    for _ in range(3):
        report = create_report.json
        reports.append(report)

    for report in reports:
        response = client.get(f'{report_uri}id/{report["_id"]}')
        pytest.assume(response.status.startswith('200'))
        returned_report = response.json
        for param, value in report.items():
            pytest.assume(returned_report[param] == value)


def test_get_reports(client, report_uri, create_beverages, create_customers, 
                     create_sizes, create_ingredients, create_orders, create_report):

    reports = []
    for _ in range(10):
        report = create_report.json
        reports.append(report)

    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    returned_reports = {report['_id']: report for report in response.json}
    for report in reports:
        for param, value in report.items():
            pytest.assume(returned_reports[report['_id']][param] == value)
