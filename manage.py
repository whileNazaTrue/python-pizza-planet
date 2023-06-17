

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, Size, Beverage, Customer, IngredientForOrder
from app.common.seeder import seed_data
import sys

manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])

@manager.command('dbdrop', with_appcontext=True)
def dbdrop():
    db.drop_all()

@manager.command('seed', with_appcontext=True)
def seed():
    sys.path.insert(0, '.') 
    seed_data()


if __name__ == '__main__':
    manager()
