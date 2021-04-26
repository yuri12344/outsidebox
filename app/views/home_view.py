from flask import Blueprint
from flask.json import jsonify

bp_home = Blueprint('/home', __name__, url_prefix='/')


@bp_home.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'home'})
