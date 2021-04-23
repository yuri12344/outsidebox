import re
from app.views.login_view import token_required, current_app
from flask import Blueprint, request, jsonify
from app.services.validate_service_request_catalog import ValidateServiceRequestFromCatalog
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
bp_catalog_service_request = Blueprint(
    'bp_catalog_service_request', __name__, url_prefix='/catalog_service_request/')


@bp_catalog_service_request.route('/', methods=['POST'])
@token_required
def service_request_catalog():
    session = current_app.db.session

    user_logged = current_app.secret_key[2]['user']
    data = request.json

    try:
        user_logged.get(user_logged['description'])

        validate_data = ValidateServiceRequestFromCatalog(data)
        validate_data = validate_data.__dict__

        if validate_data['can_register'] == True:
            service = ServiceRequestCatalogModel(
                client_name=validate_data['client_name'],
                date_time=validate_data['date_time'],
                informations=validate_data['informations'],
                feedback_url=validate_data['feedback'],
                aproved=validate_data['aproved'],
                responsible=validate_data['responsible'],
                id_company=user_logged['id'],
                id_client=validate_data['id_client'],
                id_service_catalog=validate_data['id_service'],
            )
            session.add(service)
            session.commit()

        if validate_data['can_register'] == False:
            return jsonify({'message': validate_data['specific_error']})

        return jsonify({"sucess": f"Sucess, you can check service here"})
    except KeyError:
        return jsonify({'message': 'Apenas usuário do tipo empresa pode acessar essa rota'})
