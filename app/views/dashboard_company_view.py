from flask import Blueprint, request, jsonify

dashboard_company = Blueprint(
    'dashboard_company', __name__, url_prefix='/company_dashboard/')


@dashboard_company.route('/', methods=['GET'])
def slash_route():

    return {"message": "You need to pass a id_company in URL ex: /company_dashboard/<id_company>/"}


@dashboard_company.route('/<id_company>', methods=['GET'])
def specific_company(id_company=0):
    return jsonify({'message': f'Dashboard company to id_company {id_company}'})
