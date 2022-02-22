from flask import Blueprint, request, current_app
import hashlib
import binascii
import psycopg2
import os
import ipdb
from flask.json import jsonify
from app.models.signup_client_model import ClientModel

from http import HTTPStatus
from app.models.signup_company_model import CompanyModel
from app.services.signup_client_services import SignUp

bp_signup_company = Blueprint(
    'bp_signup_company', __name__, url_prefix='/signup_company')


@bp_signup_company.route('/', methods=['POST', 'GET'])
def signup_comp():
    data = request.get_json()
    session = current_app.db.session
    check_json_data = SignUp(data)
    check_json_data = check_json_data.__dict__
    check_email_client = ClientModel.query.filter_by(
        email=check_json_data['try_register']['email']).first()

    if check_email_client:
        return jsonify({"message": "You cant create account with this email, a ready have a client with this email"})

    if check_json_data['can_register'] == False:
        return check_json_data

    if check_json_data['can_register'] == True:
        user_data = check_json_data['try_register']

        company = CompanyModel(
            name=user_data["name"],
            email=user_data["email"],
            password=user_data['password'],
            phone=user_data["phone"],
            address=user_data["address"],
            city=user_data["city"],
            state=user_data["state"],
            cpf_cnpj=user_data["cpf/cnpj"],
            schedule=user_data["schedule"],
            description=user_data["description"],
        )

        try:
            session.add(company)
            session.commit()
            return {"status": "User created"}
        except Exception as e:
            return {"status": str(e.__dict__["orig"])}
