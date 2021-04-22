from app.views.login_view import token_required
from flask import Blueprint, request, jsonify

bp_catalog_service_request = Blueprint(
    'bp_catalog_service_request', __name__, url_prefix='/catalog_service_request')


@bp_catalog_service_request.route('/<id_company>', methods=['POST'])
def service_catalog(id_company=0):
    session = current_app.db.session
    data = request.get_json()

    session.add(service)
    session.commit()
    return {
        "status": "created sucess",
        "id": service.id,
        "name_of_service": service.name_of_service,
        "price": service.price,
        "service_description": service.service_description,
        "id_company": service.id_company
    }


@bp_catalog_service_request.route('/', methods=['POST'])
def only_slash():
    return jsonify({'message': 'you need use url => catalog_service_request/<id_company>/ '})
