from app.models import service_request_catalog_model
from app.views.login_view import token_required, current_app
from flask import Blueprint, request, jsonify
from app.services.validate_service_request_catalog import ValidateServiceRequestFromCatalog
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app.services.random_id import id_generator
import os
import binascii
bp_catalog_service_request = Blueprint(
    'bp_catalog_service_request', __name__, url_prefix='/catalog_service_request/')


@bp_catalog_service_request.route('/', methods=['POST'])
@token_required
def service_request_catalog():
    session = current_app.db.session
    randhash = id_generator()

    company_logged = current_app.secret_key[2]['user']
    data = request.json

    try:
        company_logged.get(company_logged['description'])

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
                id_company=company_logged['id'],
                id_client=validate_data['id_client'],
                id_service_catalog=validate_data['id_service'],
                hash_to_feedback=randhash
            )
            session.add(service)
            session.commit()

            update_service = ServiceRequestCatalogModel.query.filter_by(
                hash_to_feedback=randhash).first()

            company_loged_id = company_logged['id']
            base_url = os.getenv('BASE_URL')
            url = base_url + "/feedback/" + \
                str(company_loged_id) + "/" + str(update_service.id) + \
                "/" + str(validate_data['id_client'])

            url_to_get_service = base_url + "/" + \
                str(company_loged_id) + "/" + str(update_service.id)
            if validate_data["feedback"] == "True":
                update_service.feedback_url = url
                session.commit()
                return jsonify({
                    'status': 'sucess',
                    'Link service': url_to_get_service,
                    'Link to your client give feedback': url}
                )
            return jsonify({'message': 'Sucess', 'Link': url_to_get_service})

        if validate_data['can_register'] == False:
            return jsonify({'message': validate_data['specific_error']})

    except KeyError:
        return jsonify({'message': 'Apenas usuário do tipo empresa pode acessar essa rota'})
