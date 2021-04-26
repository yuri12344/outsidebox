from flask import Blueprint
from flask.globals import current_app
from flask.json import jsonify
from os import getenv

bp_home = Blueprint('/home', __name__, url_prefix='/')


old_string = getenv('DATABASE_URL')

new_string = old_string[:8] + "ql" + old_string[8:]


@bp_home.route('/', methods=['GET'])
def home():
    return jsonify({'message': new_string})
