<<<<<<< HEAD
from flask import Blueprint, current_app, request

from app.models.service_specific_model import ServiceSpecificModel

bp_service_specific = Blueprint('bp_service_specific', __name__, url_prefix='/service_specific')


@bp_service_specific.route('/create/<int:id_company>', methods=['POST'])
def service_catalog(id_company):
    session = current_app.db.session
    data = request.get_json()

    def str_to_bool(data):
        return data.lower() in ("False", "True")

    aproved_boolean = Boolean()
    service_specific = ServiceSpecificModel(
        name_of_service=data["name_of_service"],
        price=data["price"],
        service_description=data["service_description"],
        client_name=data["client_name"],
        id_client=data["id_client"],
        date_time=data["date_time"],
        informations=data["informations"],
        feedback_url=data["feedback_url"],
        aproved=str_to_bool(data),
        responsible=data["responsible"],
        id_company=id_company
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
=======
from flask import Blueprint, request, jsonify

bp_services_specific = Blueprint(
    'bp_services_specific', __name__, url_prefix='/services_specific/create')


@bp_services_specific.route('/<id_company>', methods=['POST'])
def specific_service(id_company=0):

    return {"message": "Rota services specific"}


@bp_services_specific.route('/', methods=['POST'])
def only_slash():
    return jsonify({'message': 'you need use url => services_specific/create/<id_company> '})
>>>>>>> 522b99973e70db515a38d64fd1998e67a4666097
