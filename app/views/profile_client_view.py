from flask import Blueprint, request, current_app

from flask.json import jsonify

bp_client_profile = Blueprint(
    'bp_client_profile', __name__, url_prefix='/client_profile/')


@bp_client_profile.route('/<id_client>', methods=['POST', 'GET'])
def service(id_client=0):

    return jsonify({'message': 'CLIENT PROFILE'})


@bp_client_profile.route('/', methods=['POST', 'GET'])
def route_slash():

    return jsonify({'message': 'use url: client_profile/<id_client>'})
