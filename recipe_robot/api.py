from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>')
def say_hello(name):
    response = {'msg': f'Hello {name}'}
    return jsonify(response)
