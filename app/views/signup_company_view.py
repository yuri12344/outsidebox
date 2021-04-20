from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.signup_company_model import CompanyModel
from app.services.signup import SignUp

bp_signup_comapany = Blueprint(
    'bp_signup_comapany', __name__, url_prefix='/signup_company')


@bp_signup_comapany.route('/', methods=['POST', 'GET'])
def signup_comp():
    data = request.get_json()
    checked_data = SignUp(data)
    print(checked_data.__dict__)

    session = current_app.db.session
    #data_to_write_in_database = CompanyModel(feedback=data["feedback"])
    # session.add(data_to_write_in_database)
    # session.commit()

    return checked_data.__dict__, HTTPStatus.CREATED
