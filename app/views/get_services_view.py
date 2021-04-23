from flask import Blueprint, jsonify
from app.models.services_created import ServicesCreated
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app.models.service_specific_model import ServiceSpecificModel
from app.models.signup_client_model import ClientModel

bp_get_services = Blueprint(
    'bp_get_services', __name__, url_prefix='/get_services/')


@bp_get_services.route('/<id_company>/<id_service>', methods=['GET'])
def service_catalog(id_company=0, id_service=0):
    if id_company == 0 or id_service == 0:
        return jsonify({'message': 'id_company cannot be blank, id_service cannot be blank, you need to pass a valid value'})
    service_created = ServicesCreated.query.get(id_service)

    if not service_created:
        return jsonify({'message': 'This service id doenst exists in our database'})

    if service_created.from_ == 'catalog':
        data_service = ServiceRequestCatalogModel.query.get(
            service_created.id_service_create_catalog)
        try:
            data_client = ClientModel.query.get(data_service.id_client)
            if data_client:
                return jsonify({
                    "service_from": "catalog",
                    "cliente_e_cadastrado": "Yes",
                    "client_name": data_client.name,
                    "client_phone": data_client.phone,
                    "date/time": data_service.date_time,
                    "informations": data_service.informations,
                    "aproved": data_service.aproved,
                    "responsible": data_service.responsible
                })
        except:
            return jsonify({
                "service_from": "catalog",
                "cliente_e_cadastrado": "Não",
                "client_name": data_service.client_name,
                "date/time": data_service.date_time,
                "informations": data_service.informations,
                "aproved": data_service.aproved,
                "responsible": data_service.responsible
            })

    if service_created.from_ == "specific":
        data_service = ServiceSpecificModel.query.get(
            service_created.id_service_create_catalog)
        try:
            data_client = ClientModel.query.get(data_service.id_client)
            if data_client:
                return jsonify({
                    "cliente_e_cadastrado": "Sim",
                    "name_of_service": data_service.name_of_service,
                    "client_name": data_client.name,
                    "date_time": data_service.date_time,
                    "informations": data_service.informations,
                    "aproved": data_service.aproved,
                    "responsible": data_service.responsible
                })
        except:
            return jsonify({
                "cliente_e_cadastrado": "Nao",
                "name_of_service": data_service.name_of_service,
                "client_name": data_service.client_name,
                "date_time": data_service.date_time,
                "informations": data_service.informations,
                "aproved": data_service.aproved,
                "responsible": data_service.responsible
            })

    return {"ROTA": "ROTA GET SERVICES"}


@bp_get_services.route('/', methods=['GET', 'POST'])
def only_slash():
    return jsonify({'message': 'Use this url: /get_services/<id_company>/<id_service> '})


@bp_get_services.route('/<id_company>', methods=['GET', 'POST'])
def only_slash_and_one_number(id_company=0):
    return jsonify({'message': 'Use this url: /get_services/<id_company>/<id_service> '})
