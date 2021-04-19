from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.feedback_model import FeedbackModel

bp_feedback = Blueprint('bp_feedback', __name__, url_prefix='/feedback')


@bp_feedback.route('/', methods=['POST'])
def service():
    session = current_app.db.session
    data = request.get_json()
    feedback = FeedbackModel(feedback=data["feedback"])
    session.add(feedback)
    session.commit()

    return {"id": service.id, "feedback": feedback.feedback}, HTTPStatus.CREATED
