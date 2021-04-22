from flask.globals import current_app
from app.views.login_view import token_required
from flask import Blueprint, request, jsonify
import os

dashboard_company = Blueprint(
    'dashboard_company', __name__, url_prefix='/company_dashboard/')

base_url = os.getenv('BASE_URL')


@dashboard_company.route('/<id_company>', methods=['GET'])
@token_required
def all_companys(id_company=0):
    user_logged = current_app.secret_key[2]['user']
    try:
        user_logged.get(user_logged['description'])
        id_company_loged = user_logged['id']
        json_to_return = {
            "your_id_company": user_logged['id'],
            "company_name": user_logged['nome'],
            "clients_list": [],
            "services_catalog": user_logged['service_catalog_list'],
            "link_create_service_catalog": f"{base_url}/services_catalog/create/{id_company_loged}",
            "link_create_service_specific": f"{base_url}/services_specific/create/{id_company_loged}",
            "company_profile": f"{base_url}/company/{id_company_loged}"
        }
        if int(id_company) != int(user_logged['id']):
            return jsonify(
                {
                    "error": "You cant see the others companys dashboards, returning your data only",
                    "your_data": json_to_return
                }
            )
        return jsonify(json_to_return)
    except KeyError:
        return jsonify({'message': 'This route is only for companys'})


@dashboard_company.route('/', methods=['GET'])
def slash_route():
    return jsonify({'message': f'You need login and was company and pass id_company'})
