from flask import Blueprint, request, jsonify

bp_companys = Blueprint(
    'bp_companys', __name__, url_prefix='/companys/')


@bp_companys.route('/', methods=['GET'])
def list_companys():

    return {"message": "LIST ALL COMPANYS, but you can also give a id_company ex: companys/<id_company>"}


@bp_companys.route('/<id_company>', methods=['GET'])
def specific_company(id_company=0):
    return jsonify({'message': f'This is all information about id_company {id_company}'})
