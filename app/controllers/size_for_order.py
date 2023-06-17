from ..repositories.managers import SizeForOrderManager
from .base import BaseController



class SizeForOrderController(BaseController):
    manager = SizeForOrderManager
    __required_info = ('name', 'price')
