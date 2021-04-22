from flask.globals import current_app
from app.views.login_view import token_required
from flask import Blueprint, request, jsonify

dashboard_company = Blueprint(
    'dashboard_company', __name__, url_prefix='/company_dashboard/')


@dashboard_company.route('/<id_company>', methods=['GET'])
@token_required
def all_companys():
    user_logged = current_app.secret_key[2]['user']
    try:
        user_logged.get(user_logged['description'])
        print(user_logged)
        json_to_return = {
            "company_name": "Mecanica do Pedro",
            "clients_list": ["Yuri Caetano", "Felipe"],
            "services_catalog": [{"service_name": "Limpeza de bico", "price": 50, "id_service": 1}],
            "link_create_service_catalog": "/services_catalog/create/<id_company>",
            "link_create_service_specific": "/services_specific/create/<id_company>",
            "company_profile": "/company/<id_company>"
        }
    except KeyError:
        return jsonify({'message': 'This route is only for companys'})

    return {"message": "You need to pass a id_company in URL ex: /company_dashboard/<id_company>/"}


@dashboard_company.route('/', methods=['GET'])
def slash_route():
    return jsonify({'message': f'You need login and was company and pass id_company'})
