from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.user_company_model import UserCompany

bp_signup_comapany = Blueprint('bp_signup_comapany', __name__, url_prefix='/signup_company')


@bp_signup_comapany.route('/', methods=['POST', 'GET'])
def signup_comp():
    session = current_app.db.session
    data = request.get_json()
    data_to_write_in_database = UserCompany(feedback=data["feedback"])
    session.add(data_to_write_in_database)
    session.commit()

    return {"retorno": "criado"}, HTTPStatus.CREATED
