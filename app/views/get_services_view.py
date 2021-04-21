from flask import Blueprint, request, jsonify

bp_get_services = Blueprint(
    'bp_get_services', __name__, url_prefix='/get_services/')


@bp_get_services.route('/<id_company>/<id_service>', methods=['GET'])
def service_catalog(id_company=0, id_service=0):
    data = request.get_json()
    if id_company == 0 or id_service == 0:
        return jsonify({'message': 'id_company cannot be blank, id_service cannot be blank, you need to pass a valid value'})

    return {"ROTA": "ROTA GET SERVICES"}


@bp_get_services.route('/', methods=['GET'])
def only_slash():
    return jsonify({'message': 'you need use url => get_services/<id_company>/<id_service> '})
