from app.views.login_view import token_required
from flask import Blueprint, request, jsonify
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app.models.service_catalog_model import ServiceCatalogModel
from app.models.signup_client_model import ClientModel
bp_catalog_service_request = Blueprint(
    'bp_catalog_service_request', __name__, url_prefix='/catalog_service_request/')


@token_required
@bp_catalog_service_request.route('/<id_company>', methods=['POST'])
def service_request_catalog(id_company=0):
    session = current_app.db.session

    catalog_service_request = ServiceRequestCatalogModel(
        client=data["name_of_service"],
        data_time=data["data_time"],
        informations=data["informations"],
        feedback_url=data["feedback_url"],
        aproved=data["aproved"],
        responsible=data["responsible"],
        id_company=id_company,
        id_client=id_client,
        id_service_catalog=id_service_catalog

    )

    session.add(catalog_service_request)
    session.commit()

    return {
        "id_service": "ID from  service in catalog ex: 1",
        "client_name": "Optional",
        "id_client": "Optional, if client have account put id_client here",
        "date/time": "2020-20-05",
        "informations": "links or extra informations",
        "feedback_url": "",
        "aproved": "Bool, True or False, if client aproved the service, put True, if is a budget, put False",
        "responsible": "Felipe"
    }


@bp_catalog_service_request.route('/', methods=['POST'])
def only_slash():
    return jsonify({'message': 'you need use url => catalog_service_request/<id_company>/ '})
