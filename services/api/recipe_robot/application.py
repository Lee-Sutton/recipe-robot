import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()


def create_app(app_name='RECIPE_ROBOT'):
    app = Flask(app_name)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    from recipe_robot.api import api
    app.register_blueprint(api, url_prefix='/api')

    from recipe_robot.models import db
    db.init_app(app)

    toolbar.init_app(app)

    return app
