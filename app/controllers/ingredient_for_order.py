from ..repositories.managers import IngredientForOrderManager
from .base import BaseController



class IngredientForOrderController(BaseController):
    manager = IngredientForOrderManager
    __required_info = ('name', 'price')
