from flask import Blueprint

from ..controllers import OrderController
from .generic_routes import create_generic_routes

order = Blueprint('order', __name__)
create_generic_routes(order, OrderController, can_update=False)



