from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import CustomerController

customer = Blueprint('customer', __name__)


@customer.route('/', methods=POST)
def create_customer():
    customer, error = CustomerController.create(request.json)
    response = customer if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code

@customer.route('/id/<_id>', methods=GET)
def get_customer_by_id(_id: int):
    customer, error = CustomerController.get_by_id(_id)
    response = customer if not error else {'error': error}
    status_code = 200 if customer else 404 if not error else 400
    return jsonify(response), status_code

@customer.route('/', methods=GET)
def get_customers():
    customers, error = CustomerController.get_all()
    response = customers if not error else {'error': error}
    status_code = 200 if customers else 404 if not error else 400
    return jsonify(response), status_code


