import os
from flask import current_app
from recipe_robot.application import create_app


def test_development_config():
    os.environ['APP_SETTINGS'] = 'recipe_robot.config.DevelopmentConfig'
    app = create_app()
    assert app.config['SECRET_KEY'] == 'secretkey'
    assert current_app is not None
    assert (app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL'))


def test_testing_config():
    os.environ['APP_SETTINGS'] = 'recipe_robot.config.TestingConfig'
    app = create_app()
    assert app.config['SECRET_KEY'] == 'secretkey'
    assert current_app is not None
    assert (app.config['SQLALCHEMY_DATABASE_URI'] ==
            'sqlite:///test.db')


def test_production_config():
    os.environ['APP_SETTINGS'] = 'recipe_robot.config.ProductionConfig'
    app = create_app()
    assert app.config['SECRET_KEY'] == 'secretkey'
    assert current_app is not None
    assert (app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL'))
