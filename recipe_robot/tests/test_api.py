import json
from recipe_robot.tests.client import BaseTestCase


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
