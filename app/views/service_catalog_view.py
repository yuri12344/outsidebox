from app.views.login_view import token_required
from flask import Blueprint, request, current_app
from app.services.validated_service_catalog import ValidatedServiceCatalog
from http import HTTPStatus
from app.models.service_catalog_model import ServiceCatalogModel

bp_service_catalog = Blueprint(
    'bp_service_catalog', __name__, url_prefix='/service_catalog')


@bp_service_catalog.route('/create/<int:id_company>', methods=['POST'])
@token_required
def service_catalog(id_company):
    session = current_app.db.session
    data = request.get_json()

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
            id_company=id_company
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
