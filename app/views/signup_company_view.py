from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.signup_company_model import CompanyModel
from app.services.signup_client_services import SignUp

bp_signup_comapany = Blueprint(
    'bp_signup_comapany', __name__, url_prefix='/signup_company')


@bp_signup_comapany.route('/', methods=['POST', 'GET'])
def signup_comp():
    data = request.get_json()
    session = current_app.db.session
    check_json_data = SignUp(data)
    check_json_data = check_json_data.__dict__

    if check_json_data['can_register'] == False:
        return check_json_data

    if check_json_data['can_register'] == True:
        user_data = check_json_data['try_register']

        company = CompanyModel(
            nome=user_data["name"],
            email=user_data["email"],
            password_hash=user_data["password"],
            phone=user_data["phone"],
            adress=user_data["address"],
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
            return {"status": "Usuário com este e-mail já existe"}, HTTPStatus.UNPROCESSABLE_ENTITY
