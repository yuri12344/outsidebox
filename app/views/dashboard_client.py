from flask import Blueprint

bp = Blueprint('client_route', __name__)

@bp.route('/client')
def client():
    return "teste rota cliente"
