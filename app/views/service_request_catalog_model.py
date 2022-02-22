from app.views.login_view import token_required
from flask import Blueprint, request, jsonify, current_app
from app.services.validate_service_request_catalog import ValidateServiceRequestFromCatalog
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app.models.services_created import ServicesCreated
import os
from app import user_logged


bp_catalog_service_request = Blueprint(
    'bp_catalog_service_request', __name__, url_prefix='/catalog_service_request/')


@bp_catalog_service_request.route('/', methods=['POST'])
@token_required
def service_request_catalog():
    base_url = os.getenv('BASE_URL')
    session = current_app.db.session

    company_logged = user_logged[2]['user']
    data = request.json
    validate_data = ValidateServiceRequestFromCatalog(data)
    validate_data = validate_data.__dict__
    try:
        company_logged.get(company_logged['description'])

        if validate_data['can_register'] == True:
            service = ServiceRequestCatalogModel(
                client_name=validate_data['client_name'],
                date_time=validate_data['date_time'],
                informations=validate_data['informations'],
                feedback_url=validate_data['feedback'],
                aproved=validate_data['aproved'],
                responsible=validate_data['responsible'],
                id_company=int(company_logged['id']),
                id_client=validate_data['id_client'],
                id_service_catalog=int(validate_data['id_service'])
            )
            session.add(service)
            session.commit()

            services_created = ServicesCreated(
                id_service_create_catalog=service.id,
                id_company=company_logged['id'],
                from_='catalog'
            )
            try:
                session.add(services_created)
                session.commit()
            except:
                return jsonify({'message': 'just try again'})

            company_loged_id = company_logged['id']
            url = base_url + "/feedback/" + \
                str(company_loged_id) + "/" + str(services_created.id) + \
                "/" + str(validate_data['id_client'])

            url_to_get_service = base_url + "/get_services/" + \
                str(company_loged_id) + "/" + str(services_created.id)
            if validate_data["feedback"] == "True":
                service.feedback_url = url
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
        return jsonify({'message': validate_data['specific_error']})
