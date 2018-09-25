import pytest
import json

from recipe_robot.application import create_app
from recipe_robot.models import db, Recipe


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    recipe1 = Recipe(name='Dummy Recipe')
    db.session.add(recipe1)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


def test_ping(test_client):
    response = test_client.get('/api/ping/')
    assert response.status_code == 200
    assert response.json == {'msg': 'pong'}


def test_get_recipes(test_client, init_database):
    response = test_client.get('/api/recipes/')
    assert response.status_code == 200


def test_post_recipes(test_client, init_database):
    data = {'name': 'Testing', 'ingredients': [{'name': 'Dummy Ingredient'}]}
    response = test_client.post('/api/recipes/',
                                data=json.dumps(data),
                                content_type='application/json')
    assert response.status_code == 201
    assert False, 'Check Recipe saved in database'
