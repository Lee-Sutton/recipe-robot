from flask_testing import TestCase

from recipe_robot.application import create_app
from recipe_robot.models import db


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app(config='recipe_robot.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
