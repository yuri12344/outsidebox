from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.service_catalog_model import ServiceCatalogModel

bp_service_catalog = Blueprint('bp_service_catalog', __name__, url_prefix='/service_catalog')


@bp_service_catalog.route('/create/<int:id_company>', methods=['POST'])
def service_catalog(id_company):
    session = current_app.db.session
    data = request.get_json()
    service = ServiceCatalogModel(
        name_of_service=data["name_of_service"],
        price=data["price"],
        service_description=data["service_description"],
        id_company=id_company
    )
    session.add(service)
    session.commit()

    return {
            "id": service.id,
            "name_of_service": service.name_of_service,
            "price": service.price,
            "service_description": service.description,
            "id_company": service.id_company
            }, HTTPStatus.CREATED
