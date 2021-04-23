from flask.helpers import make_response
from app.models.signup_company_model import CompanyModel
from flask.globals import current_app
from app.views.login_view import token_required
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

from flask.json import jsonify

bp_client_profile = Blueprint(
    'bp_client_profile', __name__, url_prefix='/client_profile/')


@bp_client_profile.route('/', methods=['GET'])
@token_required
def get_user_data(id_client=0):
    user = current_app.secret_key[2]
    user = user['user']
    try:
        user.get(user['description'])
        return jsonify({"message": "This page is only for CLIENTS, not company, please leave, you are not welcome"})
    except KeyError:
        return jsonify(
            {
                "name": user['name'],
                "email": user['email'],
                "phone": user['phone'],
                "address": user['address'],
                "city": user['city'],
                "state": user['state'],
                "services_done": [{}]
            }
        )
