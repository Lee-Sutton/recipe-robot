from flask_testing import TestCase
from recipe_robot.application import create_app
from flask import current_app
import os


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        self.app = create_app(config='recipe_robot.config.DevelopmentConfig')
        return self.app

    def test_app_is_development(self):
        assert self.app.config['SECRET_KEY'] == 'secretkey'
        assert current_app is not None
        assert (self.app.config['SQLALCHEMY_DATABASE_URI'] ==
                os.environ.get('DATABASE_URL'))


# class TestTestingConfig(TestCase):
#     def create_app(self):
#         app.config.from_object('project.config.TestingConfig')
#         return app
#
#     def test_app_is_testing(self):
#         self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
#         self.assertTrue(app.config['TESTING'])
#         self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
#         self.assertTrue(
#             app.config['SQLALCHEMY_DATABASE_URI'] ==
#             os.environ.get('DATABASE_TEST_URL')
#         )
#
#
# class TestProductionConfig(TestCase):
#     def create_app(self):
#         app.config.from_object('project.config.ProductionConfig')
#         return app
#
#     def test_app_is_production(self):
#         self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
#         self.assertFalse(app.config['TESTING'])
