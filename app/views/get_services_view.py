from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models.signup_company_model import CompanyModel

bp_get_services = Blueprint(
    'bp_get_services', __name__, url_prefix='/get_services/')


@bp_get_services.route('/<id_company>/<id_service>', methods=['GET'])
def service_catalog(id_company=0, id_service=0):
    if id_company == 0 or id_service == 0:
        return jsonify({'message': 'id_company cannot be blank, id_service cannot be blank, you need to pass a valid value'})

    get_company = CompanyModel.query.filter_by(id=id_company).first()
    get_company = get_company.__dict__
    print(get_company)

    return {"ROTA": "ROTA GET SERVICES"}


@bp_get_services.route('/', methods=['GET', 'POST'])
def only_slash():
    return jsonify({'message': 'Use this url: /get_services/<id_company>/<id_service> '})


@bp_get_services.route('/<id_company>', methods=['GET', 'POST'])
def only_slash_and_one_number(id_company=0):
    return jsonify({'message': 'Use this url: /get_services/<id_company>/<id_service> '})
