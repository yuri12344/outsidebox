from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models.signup_company_model import CompanyModel
import os
base_url = os.getenv('BASE_URL')

bp_companys = Blueprint('bp_companys', __name__)


@bp_companys.route("/companys/")
def companys():
    companys = CompanyModel.query.all()
    json_return = {}
    conter = 1

    for company in companys:
        profile_url = base_url + "/company/" + str(company.id)
        conter_str = str(conter)
        concat = "company_" + conter_str
        json_return[concat] = {"name": company.nome, "company_profile": profile_url}
        conter += 1

    print(companys)
    return {"message": json_return}


@bp_companys.route('/companys/<int:id_company>', methods=['GET'])
def specific_company(id_company):

    # name = CompanyModel.query.filter_by(id=id_company).first_or_404(description='teste')
    company = CompanyModel.query.get(id_company)

    print(company.service_catalog_list)
    return jsonify({"company_name": company.nome,
                    "email": company.email,
                    "phone": company.phone,
                    "address": company.address,
                    "city": company.city,
                    "state": company.state,
                    "cpf/cnpj": company.cpf_cnpj,
                    "description": company.description,
                    "schedule": company.schedule,
                    "service_catalog": company.service_catalog_list
                    })
