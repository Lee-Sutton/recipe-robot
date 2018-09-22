from flask import Flask
from recipe_robot.api import api


def create_app(app_name='RECIPE_ROBOT'):
    app = Flask(app_name)
    app.config.from_object('recipe_robot.config.BaseConfig')
    app.register_blueprint(api, url_prefix='/api')
    return app
