from flask import Blueprint

from ..controllers import IngredientForOrderController
from .generic_routes import create_generic_routes


ingredientfororder = Blueprint('ingredientfororder', __name__)


create_generic_routes(ingredientfororder, IngredientForOrderController, can_update=False)

