from flask import Blueprint

from ..controllers import CustomerController
from .generic_routes import create_generic_routes


customer = Blueprint('customer', __name__)

create_generic_routes(customer, CustomerController, can_update=True)
