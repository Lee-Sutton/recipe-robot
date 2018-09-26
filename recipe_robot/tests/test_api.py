import json

from recipe_robot.models import Recipe, db
from recipe_robot.tests.client import BaseTestCase


class TestPing(BaseTestCase):
    def test_ping(self):
        response = self.client.get('/api/ping/')
        assert response.status_code == 200
        assert response.json == {'msg': 'pong'}


class TestRecipeApi(BaseTestCase):
    """Recipe rest routes"""

    def test_get_recipes(self):
        with self.client:
            response = self.client.get('/api/recipes/')
            assert response.status_code == 200

    def test_post_recipes(self):
        with self.client:
            data = {'name': 'Testing',
                    'ingredients': [{'name': 'Dummy Ingredient'}]}
            response = self.client.post('/api/recipes/',
                                        data=json.dumps(data),
                                        content_type='application/json')
            assert response.status_code == 201

    def test_add_invalid_recipe(self):
        """Ensure error is thrown if JSON object is empty"""
        with self.client:
            response = self.client.post('/api/recipes/',
                                        data=json.dumps({}),
                                        content_type='application/json')
            assert response.status_code == 400
            assert 'invalid request' in response.data.decode()

    def test_get_recipe(self):
        recipe = Recipe(id=1, name='test')
        db.session.add(recipe)
        db.session.commit()
        with self.client:
            response = self.client.get('/api/recipes/1')
            assert response.status_code == 200
            data = json.loads(response.data.decode())
            assert data['name'] == 'test'
