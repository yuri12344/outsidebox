from flask import Blueprint, request, jsonify

bp_update_service = Blueprint(
    'bp_update_service', __name__, url_prefix='/update_service/')


@bp_update_service.route('/<id_company>/<id_service>', methods=['PATCH', 'GET'])
def service_catalog(id_company=0, id_service=0):

    return {"message": "Route Update Service"}


@bp_update_service.route('/', methods=['PATCH', 'GET'])
def only_slash():
    return jsonify({'message': 'you need use url => update_service/<id_company>/<id_service> '})
