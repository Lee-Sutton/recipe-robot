from flask import Flask


def create_app(app_name='RECIPE_ROBOT'):
    app = Flask(app_name)
    app.config.from_object('recipe_robot.config.BaseConfig')

    from recipe_robot.api import api
    app.register_blueprint(api, url_prefix='/api')

    from recipe_robot.models import db
    db.init_app(app)

    return app
