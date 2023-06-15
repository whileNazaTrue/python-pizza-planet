

import pytest

from ..utils.functions import get_random_price, get_random_string
import datetime


def report_mock() -> dict:
    return{
        'year': datetime.date.today().year,
    }


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def report():
    return report_mock()


@pytest.fixture
def reports():
    return [report_mock() for _ in range(5)]


@pytest.fixture
def create_report(client, report_uri) -> dict:
    response = client.post(report_uri, json=report_mock())
    return response


@pytest.fixture
def create_reports(client, report_uri) -> list:
    reports = []
    for _ in range(10):
        new_report = client.post(report_uri, json=report_mock())
        reports.append(new_report.json)
    return reports
