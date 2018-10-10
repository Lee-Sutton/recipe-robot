import os
import pytest

from recipe_robot.application import create_app
from recipe_robot.models import db


@pytest.fixture
def client():
    os.environ['APP_SETTINGS'] = 'recipe_robot.config.TestingConfig'
    app = create_app()

    with app.app_context():
        db.create_all()
        db.session.commit()

        yield app.test_client()

        db.session.remove()
        db.drop_all()
