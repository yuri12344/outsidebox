from flask import Blueprint
from flask.globals import current_app
from flask.json import jsonify
from os import getenv

bp_home = Blueprint('/home', __name__, url_prefix='/')


@bp_home.route('/', methods=['GET'])
def home():
    return jsonify({'message': "Seja bem vindo ao projeto OUTSIDE THE BOX!!!"})
