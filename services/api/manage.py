"""CLI for interacting with and setting up the server"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from recipe_robot.application import create_app
from recipe_robot.models import db, Recipe, Ingredient

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# Migration utility command
manager.add_command('db', MigrateCommand)


@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Recipe=Recipe,
                Ingredient=Ingredient)


if __name__ == '__main__':
    manager.run()
