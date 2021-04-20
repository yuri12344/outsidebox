from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.signup_client_model import ClientModel

bp_client = Blueprint('client_route', __name__)


@bp_client.route('/client', methods=["POST"])
def client():
    session = current_app.db.session
    data = request.get_json()
    client = ClientModel(  # criação da model
        name=data["name"],
        email=data["email"],
        password_hash=data["password_hash"],
        phone=data["phone"],
        adress=data["adress"],
        city=data["city"],
        state=data["state"]
    )
    try:
        session.add(client)  # Adicionando essa model a o nossa tabela 'bands'
        session.commit()  # Dando commit nas inserções feita na nossa tabela
    except:
        return {"status": "Email já cadastrado"}, HTTPStatus.UNPROCESSABLE_ENTITY

    return {"id": client.id,
            "name": client.name,
            "email": client.email,
            "password": client.password_hash,
            "phone": client.phone,
            "adress": client.adress,
            "city": client.city,
            "state": client.state
            }
