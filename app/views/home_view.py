from flask import Blueprint
from flask.globals import current_app
from flask.json import jsonify
from app import user_logged

bp_home = Blueprint('/home', __name__, url_prefix='/')


@bp_home.route('/', methods=['GET'])
def home():
    return jsonify({'message': "home"})
