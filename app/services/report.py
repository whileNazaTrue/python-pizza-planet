from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers import ReportController
from .generic_routes import create_generic_routes


report = Blueprint('report', __name__)
create_generic_routes(report, ReportController, can_update=False)

@report.route('/years', methods=GET)
def get_years_with_reports():
    report, error = ReportController.get_years_with_reports()
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code