from flask import Blueprint

from ..controllers import BeverageForOrderController
from .generic_routes import create_generic_routes


beveragefororder = Blueprint('beveragefororder', __name__)


create_generic_routes(beveragefororder, BeverageForOrderController, can_update=False)

