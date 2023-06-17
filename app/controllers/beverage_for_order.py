from ..repositories.managers import BeverageForOrderManager
from .base import BaseController



class BeverageForOrderController(BaseController):
    manager = BeverageForOrderManager
    __required_info = ('name', 'price')
