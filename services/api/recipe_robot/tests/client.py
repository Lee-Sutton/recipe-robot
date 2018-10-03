import os
from flask_testing import TestCase

from recipe_robot.application import create_app
from recipe_robot.models import db


class BaseTestCase(TestCase):
    def create_app(self):
        os.environ['APP_SETTINGS'] = 'recipe_robot.config.TestingConfig'
        app = create_app()
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
