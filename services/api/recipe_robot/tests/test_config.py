from flask_testing import TestCase
from recipe_robot.application import create_app
from flask import current_app
import os


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        os.environ['APP_SETTINGS'] = 'recipe_robot.config.DevelopmentConfig'
        self.app = create_app()
        return self.app

    def test_app_in_development_mode(self):
        assert self.app.config['SECRET_KEY'] == 'secretkey'
        assert current_app is not None
        assert (self.app.config['SQLALCHEMY_DATABASE_URI'] ==
                os.environ.get('DATABASE_URL'))


class TestTestingConfig(TestCase):
    def create_app(self):
        os.environ['APP_SETTINGS'] = 'recipe_robot.config.TestingConfig'
        self.app = create_app()
        return self.app

    def test_app_in_test_mode(self):
        assert self.app.config['SECRET_KEY'] == 'secretkey'
        assert current_app is not None
        assert (self.app.config['SQLALCHEMY_DATABASE_URI'] ==
                'sqlite:///test.db')


class TestProductionConfig(TestCase):
    def create_app(self):
        os.environ['APP_SETTINGS'] = 'recipe_robot.config.ProductionConfig'
        self.app = create_app()
        return self.app

    def test_app_in_production_mode(self):
        assert self.app.config['SECRET_KEY'] == 'secretkey'
        assert current_app is not None
        assert (self.app.config['SQLALCHEMY_DATABASE_URI'] ==
                os.environ.get('DATABASE_URL'))