from flask import Blueprint

from ..controllers import SizeController
from .generic_routes import create_generic_routes

size = Blueprint('size', __name__)


create_generic_routes(size, SizeController, can_update=True)

