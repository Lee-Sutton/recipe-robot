import json
from flask_testing import TestCase

from recipe_robot.application import create_app
from recipe_robot.models import db, Recipe


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


class TestPing(BaseTestCase):
    def test_ping(self):
        response = self.client.get('/api/ping/')
        assert response.status_code == 200
        assert response.json == {'msg': 'pong'}


class TestRecipeApi(BaseTestCase):
    """Recipe rest routes"""

    def test_get_recipes(self):
        response = self.client.get('/api/recipes/')
        assert response.status_code == 200

    def test_post_recipes(self):
        data = {'name': 'Testing',
                'ingredients': [{'name': 'Dummy Ingredient'}]}
        response = self.client.post('/api/recipes/',
                                    data=json.dumps(data),
                                    content_type='application/json')
        assert response.status_code == 201
