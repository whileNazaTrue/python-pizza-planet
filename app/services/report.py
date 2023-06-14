from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=POST)
def create_report():
    report, error = ReportController.create(request.json)
    response = report if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@report.route('/', methods=GET)
def get_report():
    report, error = ReportController.get_all()
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/id/<_id>', methods=GET)
def get_report_by_id(_id: int):
    report, error = ReportController.get_report_by_id(_id)
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/date/<date>', methods=GET)
def get_report_by_date(date: str):
    report, error = ReportController.get_report_by_date(date)
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code
