from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.feedback_model import FeedbackModel

bp_feedback = Blueprint('bp_feedback', __name__)


@bp_feedback.route('/feedback/<int:id_company>/<int:id_service>/<int:id_user>', methods=['POST'])
def service(id_company, id_service, id_user):
    session = current_app.db.session
    data = request.get_json()

    feedback = FeedbackModel(feedback=data["feedback"])
    # feedback = FeedbackModel(feedback=data["feedback"], id_company=id_company)

    session.add(feedback)
    session.commit()

    return {"feedback": feedback.feedback, "id_company": id_company, "id_service": id_service, "id_user": id_user}, HTTPStatus.CREATED


g
