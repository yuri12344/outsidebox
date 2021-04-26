from flask.json import jsonify
from app.views.login_view import token_required
from flask import Blueprint, request, current_app
from app.services.validated_service_catalog import ValidatedServiceCatalog
from app.models.signup_company_model import CompanyModel
from app.models.service_catalog_model import ServiceCatalogModel
from app import user_logged

bp_service_catalog = Blueprint(
    'bp_service_catalog', __name__, url_prefix='/service_catalog')


@bp_service_catalog.route('/create/', methods=['POST'])
@token_required
def service_catalog():
    user_loged = user_logged[2]['user']
    session = current_app.db.session
    data = request.get_json()

    company_to_create_service = CompanyModel.query.filter_by(
        id=user_loged['id']).first()

    if not company_to_create_service:
        return jsonify({'message': "Voce precisa ser uma empresa para crar um serviço no catalogo"})

    if company_to_create_service.email != user_loged['email']:
        return jsonify({'message': 'Só pode ser feito por uma company'})

    validated_service_catalog = ValidatedServiceCatalog(data)
    validated_service_catalog = validated_service_catalog.__dict__

    if validated_service_catalog['can_register'] == False:
        return validated_service_catalog

    if validated_service_catalog['can_register'] == True:
        user_data = validated_service_catalog['try_register']

        service = ServiceCatalogModel(
            name_of_service=user_data["name_of_service"],
            price=user_data["price"],
            service_description=user_data["service_description"],
            id_company=user_loged['id']
        )

        try:
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
        except:
            return {"status": "service not created, check company id"}
