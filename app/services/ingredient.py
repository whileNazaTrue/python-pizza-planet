from flask import Blueprint

from ..controllers import IngredientController
from .generic_routes import create_generic_routes


ingredient = Blueprint('ingredient', __name__)
create_generic_routes(ingredient, IngredientController, can_update=True)

