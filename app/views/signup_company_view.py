from flask import Blueprint, request, current_app
import hashlib
import binascii
import os

from http import HTTPStatus
from app.models.signup_company_model import CompanyModel
from app.services.signup_client_services import SignUp

bp_signup_company = Blueprint(
    'bp_signup_company', __name__, url_prefix='/signup_company')


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


@bp_signup_company.route('/', methods=['POST', 'GET'])
def signup_comp():
    data = request.get_json()
    session = current_app.db.session
    check_json_data = SignUp(data)
    check_json_data = check_json_data.__dict__

    if check_json_data['can_register'] == False:
        return check_json_data

    if check_json_data['can_register'] == True:
        user_data = check_json_data['try_register']

        hashed_password = hash_password(user_data['password'])

        company = CompanyModel(
            nome=user_data["name"],
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
        except:
            return {"status": "ERROR: Usuário com este e-mail já existe"}, HTTPStatus.UNPROCESSABLE_ENTITY
