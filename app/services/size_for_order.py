from flask import Blueprint

from ..controllers import SizeForOrderController
from .generic_routes import create_generic_routes


sizefororder = Blueprint('sizefororder', __name__)


create_generic_routes(sizefororder, SizeForOrderController, can_update=False)

