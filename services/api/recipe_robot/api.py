from flask import Blueprint, jsonify, request

from recipe_robot.models import Recipe, Ingredient, db

api = Blueprint('api', __name__)


@api.route('/ping/', methods=['GET'])
def ping():
    response = {'msg': 'pong'}
    return jsonify(response)


@api.route('/recipes/', methods=('GET', 'POST'))
def recipes():
    if request.method == 'GET':
        recipes = Recipe.query.all()
        return jsonify({'recipes': [r.to_dict() for r in recipes]})

    elif request.method == 'POST':
        try:
            data = request.get_json()
            recipe = Recipe(name=data['name'])
            ingredients = [Ingredient(name=i['name']) for i in
                           data['ingredients']]
            recipe.ingredients = ingredients
            db.session.add(recipe)
            db.session.commit()
            return jsonify(recipe.to_dict()), 201
        except KeyError:
            return 'invalid request', 400


@api.route('/recipes/<int:recipe_id>/')
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return jsonify(recipe.to_dict()), 200