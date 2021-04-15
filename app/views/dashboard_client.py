import re
from flask import Blueprint, request,  current_app
from http import HTTPStatus
from app.models.user_client_model import UserClient

def validate_data(client):
    if client["name"] == None or client["name"] == "":
        return False
    if client["phone"] == None or client["phone"] == "":
        return False
    if client["adress"] == None or client["adress"] == "":
        return False
    if client["city"] == None or client["city"] == "":
        return False
    if client["state"] == None or client["state"] == "":
        return False

    return True

def validate_email(email):
     # regex = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
     regex = r"^([\w\.\-]+)@([\w\-]+)((\.(\w){2,})+)$"
     return bool(re.match(regex, email))

def validate_password(password):
    # Minimo 6 digitos, 1 letra minuscula, 1 letra maiuscula, 1 numero, 1 caracter especial
    regex = r"(?=.*[a-z]){1,}(?=.*[A-Z]){1,}(?=.*[0-9]){1,}(?=.*[!@#$%^&*()--__+.]){1,}.{6,}$"

    return bool(re.match(regex, password))

bp_client= Blueprint('client_route', __name__)

@bp_client.route('/client',methods=["POST"])
def client():
    session = current_app.db.session
    data = request.get_json()

    if validate_data(data) == False:
        return "Dados Invalidos", 400
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
