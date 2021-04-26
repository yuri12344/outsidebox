from flask import Blueprint
from flask.globals import current_app
from flask.json import jsonify

bp_home = Blueprint('/home', __name__, url_prefix='/')

string = "postgres://ng"


@bp_home.route('/', methods=['GET'])
def home():
    return jsonify({'message': new_string})
