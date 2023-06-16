from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import BaseManager


class BaseController:
    manager: Optional[BaseManager] = None

    @classmethod
    def get_by_id(cls, _id: Any) -> Tuple[Any, Optional[str]]:
        try:
            item = cls.manager.get_by_id(_id)
            return item, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_all(cls) -> Tuple[Any, Optional[str]]:
        try:
            items = cls.manager.get_all()
            return items, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def create(cls, entry: dict) -> Tuple[Any, Optional[str]]:
        try:
            created_item = cls.manager.create(entry)
            return created_item, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def update(cls, new_values: dict) -> Tuple[Any, Optional[str]]:
        try:
            _id = new_values.pop('_id', None)
            if not _id:
                return None, 'Error: No id was provided for update'
            updated_item = cls.manager.update(_id, new_values)
            return updated_item, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
