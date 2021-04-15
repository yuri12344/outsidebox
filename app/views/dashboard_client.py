
from flask import Blueprint, request,  current_app
from http import HTTPStatus
from app.models.user_client_model import UserClient
from ..services.dashboard_client_services import validate_data,validate_email,validate_password

bp_client= Blueprint('client_route', __name__)

@bp_client.route('/client',methods=["POST"])
def client():
    session = current_app.db.session
    data = request.get_json()

    if validate_data(data) == False:
        return "Obrigatório preencher todos os campos", 400
    if validate_email(data['email']) == False:
        return "email invalido", 400
    if validate_password(data['password_hash']) == False:
        return "Senha invalida", 400

    client = UserClient(  #criação da model
        name=data["name"],
        email=data["email"],
        password_hash=data["password_hash"],
        phone=data["phone"],
        adress=data["adress"],
        city= data["city"],
        state= data["state"]
    )
    try:
        session.add(client)  # Adicionando essa model a o nossa tabela 'bands'
        session.commit()  # Dando commit nas inserções feita na nossa tabela
    except:
        return {"status":"Email já cadastrado"}, HTTPStatus.UNPROCESSABLE_ENTITY

    return {"id": client.id,
            "name": client.name,
            "email": client.email,
            "password": client.password_hash,
            "phone" : client.phone,
            "adress": client.adress,
            "city": client.city,
            "state": client.state
            }
