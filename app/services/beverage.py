from flask import Blueprint

from ..controllers import BeverageController
from .generic_routes import create_generic_routes


beverage = Blueprint('beverage', __name__)

create_generic_routes(beverage, BeverageController, can_update=True)

