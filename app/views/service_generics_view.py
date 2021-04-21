from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.service_generic_model import ServiceGenericModel

bp_service = Blueprint('bp_service', __name__, url_prefix='/service')


@bp_service.route('/', methods=['POST'])
def service():
    session = current_app.db.session
    data = request.get_json()
    service = ServiceGenericModel(
    service_price=data["service_price"], service_description=data["service_description"])
    session.add(service)
    session.commit()

    return {"id": service.id, "service_price": service.service_price}, HTTPStatus.CREATED
