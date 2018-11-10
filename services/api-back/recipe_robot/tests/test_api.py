import json

from recipe_robot.models import Recipe, db


def test_ping(client):
    response = client.get('/api/ping/')
    assert response.status_code == 200
    assert response.json == {'msg': 'pong'}


def test_get_recipes(client):
    with client:
        response = client.get('/api/recipes/')
        assert response.status_code == 200


def test_post_recipes(client):
    with client:
        data = {'name': 'Testing',
                'ingredients': [{'name': 'Dummy Ingredient'}]}
        response = client.post('/api/recipes/',
                               data=json.dumps(data),
                               content_type='application/json')
        assert response.status_code == 201


def test_add_invalid_recipe(client):
    """Ensure error is thrown if JSON object is empty"""
    with client:
        response = client.post('/api/recipes/',
                               data=json.dumps({}),
                               content_type='application/json')
        assert response.status_code == 400
        assert 'invalid request' in response.data.decode()


def test_get_recipe(client):
    recipe = Recipe(name='test')
    db.session.add(recipe)
    db.session.commit()
    with client:
        response = client.get(f'/api/recipes/{recipe.id}/')
        assert response.status_code == 200
        data = response.json
        assert data['name'] == 'test'
        assert type(data['created_at']) is str
