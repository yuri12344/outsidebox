
from flask import Blueprint, request, current_app, jsonify
from app.views.login_view import token_required
from http import HTTPStatus
from app.models.feedback_model import FeedbackModel
from app.models.signup_client_model import ClientModel
from app.models.service_specific_model import ServiceSpecificModel
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app import user_logged

bp_feedback = Blueprint('bp_feedback', __name__)


@bp_feedback.route('/feedback/<int:id_company>/<int:id_service>/<int:id_user>', methods=['POST'])
@token_required
def service(id_company=0, id_service=0, id_user=0):
    session = current_app.db.session
    user = user_logged[2]['user']
    client_check = ClientModel.query.filter_by(id=id_user).first()
    if client_check.email != user['email']:
        return jsonify({"message": "Wrong user loged"})

    service_specifc_check = ServiceSpecificModel.query.filter_by(
        id=id_service).first()
    service_catalog_check = ServiceRequestCatalogModel.query.filter_by(
        id=id_service).first()

    if not service_specifc_check and not service_catalog_check:
        return jsonify({'message': 'this service id not exists'})

    data = request.get_json()
    if id_company == 0 or id_service == 0 or id_user == 0:
        return {"message": "dados passados por parametro invalidos"}

    if user['id'] != id_user:
        return {"message": "voce não fez este serviço"}

    try:
        if len(data['feedback']) == 0:
            return {"message": "feedback não pode estar vazio"}
        if len(data['feedback']) > 244:
            return {"message": "feedback não pode ter mais que 244 caracteres"}
        data.get(data['feedback'])
        feedback = FeedbackModel(
            feedback=data["feedback"], company_id=id_company)
        session.add(feedback)
        session.commit()

        return {"status": "feedback criado com sucesso", "feedback": feedback.feedback, "id_company": id_company, "id_service": id_service, "id_user": id_user}, HTTPStatus.CREATED

    except KeyError:
        return {"message": "json do  feedback escrito errado"}


@bp_feedback.route("/feedback/", methods=["GET", "POST"])
def only_slash():
    return {"menssage": '/feedback/<int:id_company>/<int:id_service>/<int:id_user>'}
