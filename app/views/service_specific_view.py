from app.views.login_view import token_required
from flask import Blueprint, request, jsonify, current_app
from app.models.service_specific_model import ServiceSpecificModel

bp_services_specific = Blueprint(
    'bp_services_specific', __name__, url_prefix='/services_specific/create')


@bp_services_specific.route('/', methods=['POST'])
@token_required
def specific_service(id_company=1):
    company_logged = current_app.secret_key[2]['user']
    print(company_logged)

    try:
        company_logged.get(company_logged['description'])

        session = current_app.db.session
        data = request.get_json()

        def str_to_bool(data):
            data = data.lower()
            if data == "false":
                return "False"
            if data == "true":
                return "True"
            else:
                return "invalid"

        service_specific = ServiceSpecificModel(
            name_of_service=data["name_of_service"],
            price=data["price"],
            service_description=data["service_description"],
            client_name=data["client_name"],
            id_client=data["id_client"],
            date_time=data["date_time"],
            informations=data["informations"],
            feedback_url=data["feedback_url"],
            aproved=str_to_bool(data['aproved']),
            responsible=data["responsible"],
            id_company=company_logged['id']
        )

        session.add(service_specific)
        session.commit()
        return {
            "status": "created sucess",
            "id": service_specific.id,
            "name_of_service": service_specific.name_of_service,
            "price": service_specific.price,
            "service_description": service_specific.service_description,
            "client_name": service_specific.client_name,
            "id_client": service_specific.id_client,
            "date_time": service_specific.date_time,
            "informations": service_specific.informations,
            "feedback_url": service_specific.feedback_url,
            "aproved": service_specific.aproved,
            "responsible": service_specific.responsible,
            "id_company": service_specific.id_company
        }
    except KeyError:
        return {"msg": "Só pode ser executado por uma empresa"}


@bp_services_specific.route('/', methods=['POST'])
def only_slash():
    return jsonify({'message': 'you need use url => services_specific/create/<id_company> '})
