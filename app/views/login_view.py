from flask import Blueprint, jsonify, request, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
from app.models.signup_company_model import CompanyModel
from app.models.signup_client_model import ClientModel
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = current_app.secret_key[1]['token']
        if token == "vazio":
            return jsonify({'message': 'Faça o login'}), 403
        return f(*args, **kwargs)
    return decorated


bp_login = Blueprint('/login', __name__, url_prefix='/login')


@bp_login.route('/', methods=['POST'])
def login():
    auth = request.get_json()

    company = CompanyModel.query.filter_by(email=auth['email']).first()
    client = ClientModel.query.filter_by(email=auth['email']).first()

    if len(auth['email']) == 0 or len(auth['password']) == 0:
        return make_response('Preencha todos os dados', 401)

    if not company and not client:
        return make_response('Não existe nenhum usuário com este e-mail', 401)

    if company:
        if company.password == auth['password']:
            current_app.secret_key[1]['token'] = "logado"
            return jsonify({'message': f'Usuário {company.nome} logado com sucesso'})
        return jsonify({'message': 'senha errada ou email errado'})

    if client:
        if company.password == auth['password']:
            current_app.secret_key[1]['token'] = "logado"
            return jsonify({'message': f'Usuário {client.name} logado com sucesso'})
        return jsonify({'message': 'senha errada ou email errado'})

    return make_response('Could not verify!', 401)
