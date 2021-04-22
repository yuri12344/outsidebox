
from flask import Blueprint, request, current_app
from app.views.login_view import token_required
from http import HTTPStatus
from app.models.feedback_model import FeedbackModel

bp_feedback = Blueprint('bp_feedback', __name__)


@bp_feedback.route('/feedback/<int:id_company>/<int:id_service>/<int:id_user>', methods=['POST'])
@token_required
def service(id_company=0, id_service=0, id_user=0):
    session = current_app.db.session
    data = request.get_json()
    user = current_app.secret_key[2]
    user = user['user']
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
        feedback = FeedbackModel(feedback=data["feedback"], company_id=id_company)
        session.add(feedback)
        session.commit()

        return {"status": "feedback criado com sucesso", "feedback": feedback.feedback, "id_company": id_company, "id_service": id_service, "id_user": id_user}, HTTPStatus.CREATED

    except KeyError:
        return {"message": "json do  feedback escrito errado"}


@bp_feedback.route("/feedback/", methods=["GET", "POST"])
def only_slash():
    return {"menssage": '/feedback/<int:id_company>/<int:id_service>/<int:id_user>'}
