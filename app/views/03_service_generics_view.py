from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.service_model import ServiceModel

bp_service = Blueprint('bp_service', __name__, url_prefix='/service')


@bp_service.route('/', methods=['POST'])
def service():
    session = current_app.db.session
    data = request.get_json()
    service = ServiceModel(service_price=data["service_price"], service_description=data["service_description"])
    session.add(service)
    session.commit()

    return {"id": service.id, "service_price": service.service_price}, HTTPStatus.CREATED
