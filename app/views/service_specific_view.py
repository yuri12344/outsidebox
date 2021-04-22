from app.views.login_view import token_required
from flask import Blueprint, request, jsonify

bp_services_specific = Blueprint(
    'bp_services_specific', __name__, url_prefix='/services_specific/create')


@bp_services_specific.route('/<id_company>', methods=['POST'])
def specific_service(id_company=0):

    return {"message": "Rota services specific"}


@bp_services_specific.route('/', methods=['POST'])
def only_slash():
    return jsonify({'message': 'you need use url => services_specific/create/<id_company> '})
