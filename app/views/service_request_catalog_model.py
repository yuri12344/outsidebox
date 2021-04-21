from flask import Blueprint, request, jsonify

bp_catalog_service_request = Blueprint(
    'bp_catalog_service_request', __name__, url_prefix='/catalog_service_request')


@bp_catalog_service_request.route('/<id_company>', methods=['POST'])
def service_catalog(id_company=0):

    return {"message": "Rota catalog service request"}


@bp_catalog_service_request.route('/', methods=['POST'])
def only_slash():
    return jsonify({'message': 'you need use url => catalog_service_request/<id_company>/ '})
