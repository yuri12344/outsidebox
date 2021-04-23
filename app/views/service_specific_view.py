from app.views.login_view import token_required
from flask import Blueprint, request, jsonify, current_app
from app.models.service_specific_model import ServiceSpecificModel
from app.services.validate_service_specific import ValidateServiceSpecific
from app.models.services_created import ServicesCreated
import os

bp_services_specific = Blueprint(
    'bp_services_specific', __name__, url_prefix='/services_specific/create')


@bp_services_specific.route('/', methods=['POST'])
@token_required
def specific_service():
    base_url = os.getenv('BASE_URL')
    session = current_app.db.session
    company_logged = current_app.secret_key[2]['user']
    try:
        company_logged.get(company_logged['description'])
    except KeyError:
        return {"msg": "Você precisa logar como empresa para acessar esta rota"}

    data = request.json
    data = ValidateServiceSpecific(data)
    data = data.__dict__
    if data['can_register'] == False:
        return jsonify({'status': data['specific_error']})
    try:
        service_specifc_request = ServiceSpecificModel(
            name_of_service=data['name_of_service'],
            price=data['price'],
            service_description=data['service_description'],
            client_name=data['client_name'],
            id_client=data['id_client'],
            date_time=data['date_time'],
            informations=data['informations'],
            feedback_url=data['feedback'],
            aproved=data['aproved'],
            responsible=data['responsible'],
            id_company=company_logged['id'],
        )
        session.add(service_specifc_request)
        session.commit()

        service_create = ServicesCreated(
            id_service_create_specific=service_specifc_request.id,
            id_company=company_logged['id'],
            from_="specific"
        )
        try:
            session.add(service_create)
            session.commit()
        except:
            return jsonify({'message': 'Just try again'})

        company_loged_id = company_logged['id']
        url = base_url + "/feedback/" + \
            str(company_loged_id) + "/" + str(service_create.id) + \
            "/" + str(data['id_client'])

        url_to_get_service = base_url + "/get_services/" + \
            str(company_loged_id) + "/" + str(service_create.id)
        if data["feedback"] == "True":
            service_create.feedback_url = url
            session.commit()
            return jsonify({'status': 'Criado com sucesso', 'Link': url_to_get_service, 'Link p/ feedback': url})

        return jsonify({'status': 'Criado com sucesso', 'Link': url_to_get_service})

    except KeyError:
        return jsonify({'message': 'Apenas usuário do tipo empresa pode acessar essa rota'})
