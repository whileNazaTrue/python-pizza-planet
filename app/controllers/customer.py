from ..repositories.managers import CustomerManager
from .base import BaseController
from ..common.utils import check_required_keys


class CustomerController(BaseController):
    manager = CustomerManager
    __required_info = ('client_name', 'client_dni','client_address', 'client_phone')

    @classmethod
    def create(cls, customer: dict):
        current_customer = customer.copy()
        if not check_required_keys(cls.__required_info, current_customer):
            return 'Invalid customer payload', None
        return cls.manager.create(current_customer), None
