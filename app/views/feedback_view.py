from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.feedback_model import FeedbackModel

bp_feedback = Blueprint('bp_feedback', __name__, url_prefix='/feedback')


@bp_feedback.route('/', methods=['POST'])
def service():

    return {'message': 'feedback route'}
