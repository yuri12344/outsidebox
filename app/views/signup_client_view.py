from flask import Blueprint, request,  current_app

from flask.json import jsonify
from app.models.signup_client_model import ClientModel
from app.services.signup_client_services import SignupClient
from app.models.signup_company_model import CompanyModel

bp_client = Blueprint("client_route", __name__)


@bp_client.route('/signup_client', methods=["POST"])
def client():

    session = current_app.db.session
    data = request.get_json()

    validate_user = SignupClient(data)
    validate_user = validate_user.__dict__
    check_email = CompanyModel.query.filter_by(
        email=validate_user['try_register']['email']).first()
    if check_email:
        return jsonify({'message': 'you cant create account with this email, because a company a ready taken'})

    if validate_user['can_register'] == False:
        return validate_user

    if validate_user['can_register'] == True:
        user_data = validate_user['try_register']

        client = ClientModel(  # criação da modelflask
            name=user_data["name"],
            email=user_data["email"],
            password=user_data['password'],
            phone=user_data["phone"],
            address=user_data["address"],
            city=user_data["city"],
            state=user_data["state"]
        )

        try:
            # Adicionando essa model a o nossa tabela 'bands'
            session.add(client)
            session.commit()  # Dando commit nas inserções feita na nossa tabela
            return {"sucess": "User created with sucess"}
        except Exception as e:
            return {"status": str(e.__dict__["orig"])}
