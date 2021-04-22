from flask import Blueprint, request, jsonify

bp_companys = Blueprint(
    'bp_companys', __name__)


@bp_companys.route('/gti', methods=['GET'])
def list_companys():

    return {"message": "LIST ALL COMPANYS, but you can also give a id_company ex: companys/<id_company>"}


@bp_companys.route('/teste/<int:id_company>', methods=['GET'])
def specific_company(id_company):
    return jsonify({'message': f'This is all information about id_company {id_company}'})
